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

DogeCount = 12

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
        # TODO: Manage DogeCount by checking contract
        global DogeCount
        DogeCount = DogeCount + 1

    else:
        print("Invalid Doge Address, please try again")



@app.route("/mint", methods=["POST"])
def mint_post():
    # TODO: Get doge addr from api call
    doge_addr = str(request.form['DogeAddr'])
    if confirm_doge_addr(doge_addr):
        # TODO: get json resulting from minting doge
        mint_doge(DogeCount, 0, doge_addr)
        status = "Minted BitDoge with address: " + str(doge_addr)
    else:
        status = "Invalid Address, no BitDoge minted"
    # TODO: return json for the resulting doge or a message asking to try again
    return doge_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

