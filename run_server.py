from doge_generation import bitdoges_generation_script
from flask import Flask, render_template, send_file, make_response, request
import subprocess
import re

# TODO: Link to BitDoges contract to supply uri after a user submits a form with a valid doge address requesting to mint


app = Flask(__name__)


# connects to local dogecoin node to confirm the user supplied doge address is valid before minting new BitDoge
def confirm_doge_addr(doge_addr):
    found = False
    data = subprocess.run(["./checkDogeAddr.sh", str(doge_addr)],capture_output=True)
    # Confirm data has match with '"isValid": true'
    data_str = data.stdout.decode("utf-8")
    res = re.search(".*isvalid\": true.*", data_str)
    if res:
        found = True
    return found


# Uses the contract supplied token id and generation number, and the user supplied doge address to forge a new doge
def mint_doge(token_id, gen_number, doge_addr):
    if confirm_doge_addr(doge_addr):
        print("Forging new doge #:" + str(token_id))
        bitdoges_generation_script.doge_factory(token_id, gen_number, doge_addr)
        # TODO: add function to upload to IPFS and call here
        # Todo: add call to _safemint from BitDoges.sol wiht uri supplied by IPFS upload function
    else:
        print("Invalid Doge Address, please try again")


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/mint")
def mint():
    # TODO: Get doge addr from user, and get gen number and token ID from stmark contract
    temmplateData = {
        'title': "Mint New BitDoge",
        'DogeAddr': "Enter Address",
        'valid': ""
    }
    return render_template("mint.html", **temmplateData)


@app.route("/mint", methods=["POST"])
def mint():
    # TODO: Get doge addr from user, and get gen number and token ID from stmark contract
    doge_addr = str(request.form['DogeAddr'])
    if confirm_doge_addr(doge_addr):
        status = "Valid"
    else:
        status = "InValid"
    temmplateData = {
        'title': "Mint New BitDoge",
        'DogeAddr': doge_addr,
        'valid': status
    }
    return render_template("mint.html", **temmplateData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

