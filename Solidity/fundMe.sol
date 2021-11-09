// SPDX-License-Identifier: minutes

pragma solidity >=0.6.0 <0.9.0;

// we want to know current price of eth so we will use an Oracle such as Chainlink
// when interacting with other contracts you always need their ABIs
import "/cahinlink.sol";

contract FundMe {
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
}
