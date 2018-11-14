#### 4 main features of systems based on block chain tech
1. **Distributed**
2. **Autonomous**
    * peer to peer
    * block generation and data update in a running system is automatic
3. **Contractual**
    * nodes which violate contract will be abandoned by other nodes
    * only those transactions which run smart contract can be accepted
        * smart contract: programmable contracts & rules & stipulations
4. **Trackable**
    * data in block chain system is transparent and interrelated
    * block chain codes are open source

#### Bitcorn Address
* usually: as the payee in the transaction
* a string which contains number and characters 
    * generation: use Hash Function to public keys  

==Base58Check==
 
#### Transaction
Transaction is a data structure:
##### Transaction Structure:
* contain a list of inputs and a list of outputs
* input: an input is a reference to an output from another transaction
    * ++previous tx++: Hash value of an old transaction
    * ++index++: the specific output number of referred output
    * ++scriptSig++: the first half of a Script
    * the total value of outputs which are referred by transaction A will be used in A's outputs
* output: an output is instruction of sending Bitcoin
    * ++value++: the amount(an Integer) of this output / Satoshi (1BTC = 100,000,000 Satoshi) 
    * ++scriptPubKey++: another half of Script
    * change: 
        * the output of a transaction
            * only can be referred once by at most one input of another transaction
            * must be spent entirely
            * the transactions which never be referred by any input of any other transaction are called ==**Unspent TransaXtion Outpot - UTXO**==
        * change address is used when the value of the used output is higher than what the user wishes to pay

    A transaction refers to a prior transaction.

##### Scripting System
featrues of bitcoin scripting language:
* Forth-like
* simple
* stack-based
* processed from left to right
* no loops, not Turning-complete

++a scriptPublicKey + a scriptSig = a script++

scriptPublicKey: a part of a transaction output, like a question, it locks specific award of this question (the BTC amount of this transaction output), people who can solve the question can spend the award of it

scriptSig: a part of a transaction input, like an answer for a certain question, it indicate that the locked award fund of another transaction output can be unlocked by this scriptSig and be used in this transaction



 



##### Different types of transactions (classified by different output address):
1. pay to Hash Value of a public key   
    
2. pay to Hash Value of a script
    
    commonly: aim address is an address with multiple signatures
3. coinbase transaction   
    * generate brand new BTC
    * always be the first transaction of a block
    * only 1 input:
        * ++coinbase:++ data in this variable can be anything and will not be used
            * ++extraNonce++ is stored here
        * no scriptSig


#### Block
Block is a data structure (file).
* contains some or all recent transactions (permanently store the transaction data)
* contains a reference to the block that came immediately before it
* contains an answer to a difficult-to-solve mathematical puzzle 

##### Block Structure:
* ###### Magic no: value always 0xD9B4BEF9
* ###### Block size: number of bytes following up to end of block
* ###### Blockheader: consist of 6 items
    1. ++version++: block version number   
        update when: the new version of software came out

    2. ++hasPrevBlock++: 256-bit hash of the **previous block header**    
        update when: a new block comes in   
        
        > *SHA-256(SHA-256(Header))*   
        why is hash value of header?    -the hash value of the complete data of a block has the same size as the hash value of the header of that block, but the time of generate the hash value will be less
        
    3. ++hashMerkleRoot++: 256-bit hash based on all of the transactions in the block   
        update when: a transaction is accepted
        
    4. ++time++: current timestamp as seconds since 1970-01-01T00:00 UTC   
        update when: every few seconds
        
    5. ++bits (the difficulty of mining)++: current target in compact format
        update when: the difficulty is adjusted
        
    6. ++nonce++: 32-bit number (starts at 0)
        update when: a hash is tried (increments)
        
* ###### Transaction counter: postive integer
* ###### Transactions: the (non-empty) list of transactions