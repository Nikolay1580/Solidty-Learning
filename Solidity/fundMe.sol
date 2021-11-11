// SPDX-License-Identifier: minutes

pragma solidity ^0.6.0 <0.9.0;

// we want to know current price of eth so we will use an Oracle such as Chainlink
// when interacting with other contracts you always need their ABIs
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {

     // to make sure that there inst an issue with a number being too big. After  version 0.8, that becomes automatic
    using SafeMathChainlink for uint256;
    
    address public owner;
    
    // making a function that'll designate the owner 
    // constructer is executed once and instantly the contract is created
    constructor() public {
        owner = msg.sender;
    }

    // keeping track of who sent money
    mapping(address => uint256) public addresToAmountFunded;

    // we want this contract to accept payments
    // the payable keyword is telling the function that we can use this to pay
    // each transaction has a value usually made in Wei
    function fund() public payable {
        // msg.send is the sender of the function call and msg.value is the value sent (all in wei)
        // issue is that we want it to be in euros or USD
        addresToAmountFunded[msg.sender] += msg.value;
    }

    // we calling a function from cahinlink.sol and its view as we will only look at it
    function getVersion() public view returns (uint256) {
        // AggregatorV3Interface is the data type
        // in the brackets we need the address of the feed which can be found on the chainlink website
        AggregatorV3Interface piceFeed = AggregatorV3Interface(
            0xdCA36F27cbC4E38aE16C4E9f99D39b42337F6dcf
        );
        return piceFeed.version();
    }
    
    function getPrice() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
         return uint256(answer * 10000000000);
    }
    
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }
    
    // modifiers is how we change properties for the function
    // now we put onlyOwner in the fuction to modify the function
    modifier onlyOwner {
        require(msg.sender == owner);
        // underscor means to just tun the code, we can have it above but that means that we will check for the requirment after the function which is inneficient GAS
        _;
    }
    
    // withdraeing money from the smart contract
    
    function withdraw() public onlyOwner payable {
        // this is a keyword and it reffers to the contract you are currently in. so the address of the current contract. like self in python
        // we will uses the requrie for the sender to be the owner 
        require(msg.sender == owner);
        msg.sender.transfer(address(this).balance);
    }
}
