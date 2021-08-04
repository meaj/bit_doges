from doge_generation import bitdoges_generation_script
from flask import Flask, render_template, send_file, make_response, request
import coinaddr
from web3 import Web3


# Setup connection to Eth Network
infura_url = ""
web3 = Web3(Web3.HTTPProvider(infura_url))

# Link to BitDoges contract to supply uri after a user submits a form with a valid doge address requesting to mint
contract_abi = ""
contract_addr = ""


app = Flask(__name__)


# connects to local dogecoin node to confirm the user supplied doge address is valid before minting new BitDoge
def confirm_doge_addr(doge_addr):
    found = False
    print(doge_addr)
    try:
        data = coinaddr.validate('dogecoin', doge_addr.encode("utf-8"))
    except TypeError:
        data = None
    if data:
        found = data.valid
    return found


# Uses the contract supplied token id and generation number, and the user supplied doge address to forge a new doge
def mint_doge(token_id, gen_number, doge_addr):
    if confirm_doge_addr(doge_addr):
        print("Forging new doge #:" + str(token_id))
        bitdoges_generation_script.doge_factory(token_id, gen_number, doge_addr)
        # TODO: add call to _safemint from BitDoges.sol
        # TODO: add function to upload to IPFS when _safemint is complete
        # TODO: attach URI generated from uploading to IPFS when complete/once URI can be validated

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


@app.route("/gallery")
def gallery():
    temmplateData = {
        'title': "Gallery"
    }
    return render_template("gallery.html", **temmplateData)


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")


@app.route("/mint", methods=["POST"])
def mint_post():
    # TODO: Get doge addr from user, and get gen number and token ID from stmark contract
    doge_addr = str(request.form['DogeAddr'])
    if confirm_doge_addr(doge_addr):
        status = str(doge_addr) + ": Valid"
    else:
        status = str(doge_addr) + ": InValid"
    temmplateData = {
        'title': "Mint New BitDoge",
        'DogeAddr': doge_addr,
        'valid': status
    }
    return render_template("mint.html", **temmplateData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

