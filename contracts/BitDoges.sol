// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract BitDoges is ERC721URIStorage{
    address proj_owner;
    uint256 public tokenCounter;

    constructor() ERC721("bitDoges", "BTDG") {
        proj_owner = msg.sender;
        tokenCounter = 0;
    }

    function printBitdoge(string memory tokenURI) external payable  {
        require(msg.value >= .0069 ether , "price is too small");
        require(tokenCounter >= 11 && tokenCounter <= 1000,"token out of bounds");
        tokenCounter = tokenCounter + 1;
        _safeMint(msg.sender, tokenCounter);
        _setTokenURI(tokenCounter, tokenURI);
        payable(proj_owner).transfer(msg.value);
    }

    function premintBitdoge(string[11] memory tokenURI) external{
        require(proj_owner ==  msg.sender,"you are not allowed");
        require(tokenCounter < 11,"premint complete");
        for (uint i = 0; i < 11; i++){
            tokenCounter = i+1;
            _safeMint(msg.sender, tokenCounter);
            _setTokenURI(tokenCounter, tokenURI[i]);
        }
    }

}