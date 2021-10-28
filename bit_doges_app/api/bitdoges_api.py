import re
from doge_generation import bitdoges_generation, json_template
from flask import Flask, request, jsonify, make_response, abort
import coinaddr
from web3 import Web3


# Setup connection to Eth Network
infura_url = ""
web3 = Web3(Web3.HTTPProvider(infura_url))

# Link to BitDoges contract to supply uri after a user submits a form with a valid doge address requesting to mint
contract_abi = ""
contract_addr = ""

DogeCount = 1

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
    json, gif_path = bitdoges_generation.get_doge_data(token_id)
    # TODO: assemble doge_webpage_template data from bitdoge_json and bitdoge_gif
    return json


# JSON errorhandler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


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
        return make_response(jsonify({'error': 'Invalid Doge Address'}), 400)
    # TODO: return json for the resulting doge or a message asking to try again
    return jsonify(doge_json), 201


# Entry point for viewing bitdoge
@app.route("/bitdoge", methods=['GET'])
def view_bitdoge():
    doge_id = int(request.args['id'])
    # check if doge exists, if we have valid data return the appropriate json
    doge_data = get_bitdoge(doge_id)
    if doge_data :
        # TODO: update this to extract doge_data into doge_webpage_template
        json_template.doge_webpage_template
        return jsonify(doge_data), 200
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

