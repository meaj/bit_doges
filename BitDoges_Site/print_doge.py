from doge_generation import bitdoges_generation_script

# TODO: Link to BitDoges contract to supply uri after a user submits a form with a valid doge address requesting to mint


# connects to local dogecoin node to confirm the user supplied doge address is valid before minting new BitDoge
def confirm_doge_addr(doge_addr):
    # TODO: connect to local node and confirm doge address is valid
    return True


# Uses the contract supplied token id and generation number, and the user supplied doge address to forge a new doge
def mint_doge(token_id, gen_number, doge_addr):
    if confirm_doge_addr(doge_addr):
        print("Forging new doge #:" + str(token_id))
        bitdoges_generation_script.doge_factory(token_id, gen_number, doge_addr)
        # TODO: add function to upload to IPFS and call here
        # Todo: add call to _safemint from BitDoges.sol wiht uri supplied by IPFS upload function
    else:
        print("Invalid Doge Address, please try again")
