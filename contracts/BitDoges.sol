// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract BitDoges is ERC721URIStorage{
    using Strings for uint256;

    address proj_owner;
    uint256 public tokenCounter;

    string[] private fur1 = ["653","532","444","a71","ffc","ca9","f89","777","049","901","fc5","ffe","574","bcc","d04","222","889","7f9","fd1"];
    string[] private fur2 = ["532","653","653","653","653","653","653","653","653","653","110","653","711","344","799","555","8a8","32f","653"];
    string[] private foils = ["plain", "silver", "gold", "pink"];
    // 0: foil
    // 1: throat
    // 2: body
    // 3: eye_pupils
    // 4: eye_white
    // 5: snoz
    string[] private skeleton0 = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -0.5 24 24" shape-rendering="crispEdges"><path stroke="#',
    '" d="M0 0h24M0 1h24M0 2h7M9 2h7M17 2h7M0 3h6M10 3h5M18 3h6M0 4h6M19 4h5M0 5h5M19 5h5M0 6h5M20 6h4M0 7h5M20 7h4M0 8h4M21 8h3M0 9h4M21 9h3M0 10h3M21 10h3M0 11h3M21 11h3M0 12h2M22 12h2M0 13h2M22 13h2M0 14h2M22 14h2M0 15h2M22 15h2M0 16h2M22 16h2M0 17h2M21 17h3M0 18h3M21 18h3M0 19h3M20 19h4M0 20h4M19 20h5M0 21h5M18 21h6M0 22h24M0 23h24" /><path stroke="#000000" d="M7 2h2M16 2h1M6 3h1M9 3h1M15 3h1M17 3h1M6 4h1M10 4h5M18 4h1M5 5h1M18 5h1M5 6h1M19 6h1M5 7h1M19 7h1M4 8h1M20 8h1M4 9h1M20 9h1M3 10h1M20 10h1M3 11h1M20 11h1M2 12h1M21 12h1M2 13h1M21 13h1M2 14h1M21 14h1M2 15h1M21 15h1M2 16h1M21 16h1M2 17h1M20 17h1M3 18h1M20 18h1M3 19h1M19 19h1M4 20h1M18 20h1M5 21h13" /><path stroke="#',
    '" d="M7 3h2M16 3h1M7 4h3M15 4h3M6 5h3M6 6h2M6 7h1M8 13h5M20 13h1M7 14h8M20 14h1M7 15h6M15 15h3M19 15h2M7 16h8M18 16h3M7 17h13M8 18h12M8 19h11M9 20h9" /><path stroke="#',
    '" d="M9 5h9M8 6h11M7 7h12M5 8h2M5 9h1M7 9h3M14 9h2M4 10h1M6 10h5M13 10h4M19 10h1M4 11h16M3 12h14M20 12h1M3 13h5M13 13h4M3 14h4M15 14h2M3 15h4M3 16h4M3 17h4M4 18h4M4 19h4M5 20h4" /><path stroke="#',
    '" d="M7 8h13M6 9h1M10 9h1M13 9h1M16 9h1M19 9h1M5 10h1M11 10h2M17 10h2" /><path stroke="#',
    '" d="M11 9h2M17 9h2" /><path stroke="#',
    '" d="M17 12h3M17 13h3M17 14h3M13 15h2M18 15h1M15 16h3" /></svg>'
    ];
    
    struct Doge {
        uint8 skeleton;
        string throat;
        string body;
        string eye_p;
        string eye_w;
        string snoz;
        string foil;
        uint256 id;
        string dogeaddress;
    }

    // generates a 'random' number from input
    function random(string memory input) internal pure returns (uint256) {
        return uint256(keccak256(abi.encodePacked(input)));
    }

    // returns a substring at the given indexes
    function substring(string memory str, uint startIndex, uint endIndex) internal pure returns (string memory) {
        bytes memory strBytes = bytes(str);
        bytes memory result = new bytes(endIndex-startIndex);
        for(uint i = startIndex; i < endIndex; i++) {
            result[i-startIndex] = strBytes[i];
        }
        return string(result);
    }

    function randomDoge(uint256 tokenID, string memory dogeaddress) external view returns (Doge memory){
        // split doge address into 5 parts and use as seeds for random numbers
        Doge memory doge;
        doge.dogeaddress = dogeaddress;
        
        uint foilcount = 0;
        // for testing use the first skeleton
        doge.skeleton = 0;
        // pick any of the throat colors unweighted
        doge.throat = string(abi.encodePacked("#",fur1[uint8(random(substring(dogeaddress, 0, 5)) % 19)],fur2[uint8(random(substring(dogeaddress, 0, 5)) % 19)]));
        doge.body = string(abi.encodePacked("#",fur1[uint8(random(substring(dogeaddress, 5, 10)) % 19)],fur2[uint8(random(substring(dogeaddress, 5, 10)) % 19)]));
        // pick the eye white and eye color
        uint8 seed = uint8(random(substring(dogeaddress, 10, 15)) % 1000);
        doge.eye_w = "#ffffff";
        if (333 >= seed && seed > 50) {
            // set to silver
            doge.eye_p = "#c0c0c0";
            if (foilcount < 1){ 
                foilcount = 1;
            }            
        }
        else if (seed <= 50) {
            // set to gold and pick eye white color
            doge.eye_p = "#b8860b";
            doge.eye_w = string(abi.encodePacked("#",fur1[uint8(random(substring(dogeaddress, 15, 20)) % 19)],fur2[uint8(random(substring(dogeaddress, 15, 20)) % 19)]));
            if (foilcount < 2){ 
                foilcount = 2;
            }
        }
        else {
            // set to black
            doge.eye_p = "#000000";
            doge.eye_w = "#ffffff";
        }
        seed = uint8(random(substring(dogeaddress, 20, 25)) % 1000);
        if ( seed > 333) {
            // set to black
            doge.snoz = "#000000";
        }
        else if ( 333 >= seed && seed > 84) {
            // set to silver
            doge.snoz = "#c0c0c0";
            if (foilcount < 1){ 
                foilcount = 1;
            }
        }
        else {
            // set to gold
            doge.snoz = "#b8860b";
            if (foilcount < 2){ 
                foilcount = 2;
            }
        }
        doge.foil = foils[foilcount];
        doge.id = tokenID;
        return doge;
    }

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