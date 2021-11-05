// SPDX-License-Identifier: MIT

pragma solidity >=0.6.4 <0.9.0;

contract Sruct {
    
    // from my understanding structs are like creating instances 
    struct Person {
        uint256 age;
        string name;
    }
    
    // declaring the instance 
    Person public person = Person({age:50, name: "John"});
    
    // soldity can have both dynamic and static arrays
    Person[] public peron;
    
    // memory is a special keyword. 
    // memory is one of three ways to store data and is more costly as it increases and creates a freshly cleared instance for each message call
    function addPerson(string memory _name, uint256 _age) public {
        // appends to the list
        peron.push(Person({age:_age, name:_name}));
        findFavNumByName[_name] = _age;
    }
    
    // mapping 
    mapping(string => uint256) public findFavNumByName;
    
    
}
