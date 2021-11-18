# Project-Towards-Solidity
All the things I am learning to begin learning Solidity

This will include:
  JAVA and JAVA OOP
  Python OOP
  Node.JS
  React JS
  HTML 
  CSS
  
  
# 30/10/2021

I have finished the OOP part and am currently looking at front end dev. I have so far uploaded my 2 / 3 hours of working and mostly reading documentations while trying to understand them. CSS I am undertsanidng more and right now is to make mt rectangle with "Hello World" in it move acording to my WASD key presses. So far I am not succeding so I need to break this problem into smaller ones. For now I will try and make my code undertsand which key I am pressing by using the "AddEventListener" and recording the key press with "console.log()". 


# 31/10/2021

I have solved the issue with the event listener. it is a bit embarrassing, I had to ad 'keyDown' to the function. Next step is to create an element that moves and change its direction depending on the key input. I will have to chage basically constantly change its X,Y coordinates by adding or subtracting a value by me.


# 5/11/2021

I have began learning some of the basic syntax for Solidity. This includes the unit256 and what it means and the newest thing for me.. the "visibility" data can be. By default all data is "internal" meaning that it can be used by all components within the smart contract. There are 3 other types, "public", "external" and "private" which all have their own uses and differences. External and private being polar opposites. So far it is easy and I am understanding a bit more about Solidity and OOP in general making me more comfortable with understanding how it works.


# 8/11/2021

I have begun to do more with inheritance even though I haven't yet published, I have begun working with sending funds to other accounts which is the core of creating a dap. If A happens send x amount of WEI (Etherium's smallest form of currency) else do not send anything. It is getting a bit overwhelming for me but with breaks and time to revise and go back onto older material to make sure this is not going to fast, everything should be alright. I can't wait to create one day my own crypto coin, DAPP or both!


# 9/11/2021

Haven't done much. I have made my first smart contract which has a payable function meaning people can send money to to the contract. I have also began using oracles such as Chainlink. An oracle is (in theory) a decentralised link from blockchains to real world data such as USD, views on a Youtube video etc. It is how a smart contract can display to a person how many ETH or how many USD or any FIAT currency they have spent. It is a bit confusing but I am getting there. The most "annoying" part about this is that every blockchain including individual test-nets have their own address which is how we get the Oracle info so I need to have different addresses for different blockchains even if it is for the same purpose.


# 11/11/2021 

Finished the fundMe contract. It is so far my most interesting contract as it has not 1 but 2 functions which are payable. I also learned about constructors which are function that get executed as soon as the contract is deployed and never again. The 2 payable functions are one to fund the contract and the other to withdraw from the contract. The second function is only available for the owner. This can be done in 2 ways. 1, use a require function which is like an if else but if the condition has not been met, the funds are returned to the user - gas fees. 2, is to use a modifier. The modifier will have also the exact same require function but the reason on why modifiers are better is because you can apply to any function countless of times.


# 15/11/2021

I have began using python to deploy my Solidity code. So far I am using. VSCode which is very inefficient, not because VSCode is bad but because it is not built for this. I will for now wait and later will install Brownie which is an IDE which has built in environments and makes my life easier by not making me have to include the ABI, Bytecode and all of the JSON files


# 18/11/2021

I have been working with the brownie environment which saves me a lot of times when it comes to programming the python (web3) part of the code. I should will update my Github repository a bit later as I have not finished writing and fully deploying my Fund me contract on the test nets. ﻿I might also download truffle as it is another software that allows me to use my own local network meaning I can work on this offline. With the current knowledge I have from Solidity I think I will begin planning my NFT project where I write most if not all of the programming for the Minting of uniquely generated NFTS which will be in the form of art.
