# to deploy the contracts
from solcx import compile_standard, install_solc
import json


# we want to read our simple storage Sol file
# basic text reading code
with open("/Users/nik/Desktop/School_work /IBDP/CAS/Solidity/Solidity/SimpleStorage.sol", "r") as file:
    simple_storage = file.read()
    print(simple_storage)

# creating the compiling function
compile = compile_standard(
    {
        "language": "Solidity",
        "source": {"/Users/nik/Desktop/School_work /IBDP/CAS/Solidity/Solidity/SimpleStorage.sol": {"content": simple_storage}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evem.sourceMap"]
                }
            }
        },
    },
    # versuon of our solidty code
    install_solc("0.6.0")
)

with open("/Users/nik/Desktop/School_work /IBDP/CAS/Solidity/Python Web3/abi.json", 'w') as file:
    json.dump(compile, file)

# obtain bytecode of the fie
# this is to find the object in the JSON file
bytecode = compile["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compile["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
