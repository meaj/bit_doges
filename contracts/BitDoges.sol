pragma solidity 0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract BitDoges is ERC721URIStorage{
    address proj_owner;
    uint256 public tokenCounter;

    constructor() ERC721("bitDoges", "BTDG") {
        proj_owner = msg.sender;
        tokenCounter = 0;
    }

    function printDoge(string memory tokenURI) external payable  {
        require(msg.value >= .01 ether , "price is too small");
        require(tokenCounter >= 8 && tokenCounter <= 500,"token out of bounds");
        _safeMint(msg.sender, tokenCounter);
        _setTokenURI(tokenCounter, tokenURI);
        tokenCounter = tokenCounter + 1;
        payable(proj_owner).transfer(msg.value);
    }

    function premint(string[8] memory tokenURI) external{
        require(proj_owner ==  msg.sender,"you are not allowed");
        require(tokenCounter < 8,"premint complete");
        for (uint i = 0; i <= 7; i++){
            _safeMint(msg.sender, tokenCounter);
            _setTokenURI(tokenCounter, tokenURI[i]);
            tokenCounter = tokenCounter + 1;
        }
    }
}