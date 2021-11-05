pragma solidity >=0.6.0 <0.9.0;

// contract is used as a keyword to define your smart contract and has the property of class
contract SimpleStorage {
    // data variables
    uint256 public num = 5;
    bool tru = true;
    string name = "Nikolay";
    int256 neg = -5;
    // eth address
    address myAddresss = 0xdF88E33BdFAFfE349dBEe8658C9087e9831f055F;

    // property of method
    function store(uint256 _favouriteNumber) public {
        num = _favouriteNumber;
    }

    // view, you need to specifiy which data type it returns
    function retreive() public view returns (uint256) {
        return num;
    }

    //pure
    //function math() public peer
}
