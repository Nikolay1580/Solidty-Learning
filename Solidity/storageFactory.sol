// SPDX-License_Identifier: MIT

pragma solidity ^0.6.0;

// we need to import the simple storage
import "./simpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        // we are creating a new simpleStorage contract and are using simpleStorage as a form of data type
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }

    // making a function to call the store function from simpleStorage
    // we have an index to chose which element from the simpleStorage array we have
    function callFunctionStore(
        uint256 _simpleStorageIndex,
        uint256 _simpleStorageNumber
    ) public view {
        // we need an address and an ABI
        SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
    }
}
