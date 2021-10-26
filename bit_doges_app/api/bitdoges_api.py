import re
from doge_generation import bitdoges_generation, json_template
from flask import Flask, request, jsonify
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


def get_bitdoge(token_id):
    # TODO: add logic to check for existence of relevant doge_data folder
    return True


# Entry point for minting bitdoge
@app.route("/mint", methods=['POST'])
def mint_bitdoge():
    # Get doge addr from api call
    doge_id = int(request.args['id'])
    doge_addr = request.args['addr']
    # confirm address is valid and mint new doge
    if confirm_doge_addr(doge_addr):
        # TODO ensure duplicate doges are not created with get_bitdoge
        print("Forging new doge #:" + str(doge_id))
        # Get json data about doge from generation script
        doge_json = bitdoges_generation.doge_factory(doge_id, doge_addr)
        # TODO: Manage DogeCount by checking and updating contract
        global DogeCount
        DogeCount = DogeCount + 1
    else:
        doge_json = "<p> Invalid Address, no BitDoge minted </p>"
    # TODO: return json for the resulting doge or a message asking to try again
    return jsonify(doge_json)


# Entry point for viewing bitdoge
@app.route("/bitdoge", methods=['GET'])
def view_bitdoge():
    doge_id = int(request.args['id'])
    # check if doge exists, if we have valid data return the appropriate json
    doge_data = get_bitdoge(doge_id)
    if doge_data :
        # TODO: update this to extract doge_data into doge_webpage_template
        return jsonify(json_template.doge_webpage_template)
    else:
        return "<p> 404 BitDoge not found </p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

