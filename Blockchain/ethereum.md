### Ethereum Accounts
---
an account is a 20-byte **address**

* 4 fields of each account
    * ++nonce++: used to make sure each transaction can only be processed once
    * current ++ether balance++
    * ++contract code++ (if present)
    * ++storage++ (empty by default)

* 2 types of Ethereum accounts
    1. ++**externally owned accounts**++
        * controlled by private key
        * no contract code
        * the owner of an externally owned account can send messages to other objects in Ethereum system through this account
            * by creating and signing a transaction

    2. ++**contract accounts**++
        * controlled by its contract code
        * code activates (when the contract account receives a message)
            * read and write to its internal storage
            * send messages to other accounts
            * create contracts
        
        like "autonomous agents" live inside of the Ethereum execution environment
    
### Messages and Transactions
---
transaction is a **signed data package** that stores a message to be sent from an externally owned account

transactions contain:
* the **recipient** of the transaction
* a **signature** identifying the **sender**
* the **amount of ether** to transfer from sender to recipient
* an optional **data field**
    * default: no function
    * a contract account can use an opcode provided by virtual machine to access the data in the data field 
* `STARTGAS` value - representing the maximum number of computational steps the transaction execution is allowed to take
* `GASPRICE` value - representing the fee the sender pay **per** computational step
    * the STARTGAS and GASPRICE are two crucial fields for Ethereum's anti-denial of service model

### Message
---
messages are virtual objects that are never serialized and exist only in the Ethereum environment

messages contain:
* the **sender** of the message 
* the **recipient** of the message
* **the amount of ether** to transfer alongside the message 
* an optional **data field**
* `STARTGAS` value

notes:
* a message are essentially like a transaction, except it is produced by a contract and not an external actor
* produced of a message: when a contract currently executing code executes the `call` opcode
    * `call` opcode: an opcode that produce and execute a message
* contracts can have relationship with other contracts in exactly the same way that external actors can
    * a message leads to the recipient account running its code (just likes transactions)

### Ethereum State Transition Function
---
Ethereum State Transition Function, `APPLY(S,TX) -> S` can be defined as:
1. **transaction validation** (return an error when the validation fails)
    * if the transaction is well-formed
    * if the signature is valid
    * if the nonce matches the nonce in the sender's account

2. **substract value from sender's account**
    * use `STARTGAS * GASPRICE` to calculate the transaction fee
    * determine the sending address from the signature 
    * substract the fee from the sender's account balance and increment the sender's nonce (return an error when the balance of sender's account is not enough)

3.  **gas initialization**
    * `GAS = STARTGAS - fee/byte * bytes`

4. **value transfer**
    * transfer the transaction value to the receiving account
        * if the receiving account doesn't exist, create it 
    * if the receiving account is a contract, run the contract code
        * until the execution is complete or run out of gas
5. **trancation fee clearing**
    * if the value transfer is falied, revert all state changes except the payment of the fees, and add the fees to miner's account
        * reasons for failure:
            1. there is no enough money in sender's account
            2. the code execution ran out of gas
    * else:
        * refund the fees for remaining gas to sender
        * and send the fees paid for gas consumed to the miner

If there is no contract code at the receiving end of the transaction, then the total transaction fee would simply be equal to the `GASPRICE * length of transaction in bytes`.

### Code Execution
---
**EVM code** - Ethereum virtual machine code: **a low-level, stack-based bytecode language** used in writting Ethereum contract.

* the code consist of a series of bytes
    * each byte represents an operation

* code execution is a infinite loop (in general case)
    * stop when:
        1. reached the end of code
        2. met an error
        3. `STOP` or `RETURN` instruction is detected

    * the loop repeatedly carry out the operation at the current **program counter (PC)**
        * PC is zero at the beginning
        * every time an operation was carried out, increse the PC by one
        * the operations have access to 3 types space in which to store data
            1. **stack** -  a LIFO container to which values can be pushed and popped
            2. **memory** - an infinitely expandable byte array
            3. the contract's long-term **storage** - a key/value store    
            
            stack and memory reset after compution ends, storage persists for long term
    
* code can also 
    
    * access the value, sender and data of the incoming message, as well as the block header data
    * return a byte array of data as output
        
* formal execution model of EVM code
    
    when EVM is running, the full **computional state** can be defined by the tuple `(block_state, transaction, message, code, memory, stack, pc, gas)`
    * `(block_state)`: the global state containing all accounts and includes balances and storage
    * in every round of execution:

        1. find the current instruction by taking the `pc-`th byte of `code` (or 0 if `pc >+ len(code)`)
        2. each instruction has it own definition in terms of how it affects the tuple
        
### Blockchain and Mining
---
**Bitcoin blockchain**: only contains transaction list   

**Ethereum blockchain** contains:
* a copy of the transaction list
* the most recent state
* the block number
* the difficulty
