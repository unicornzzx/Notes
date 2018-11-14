#### Multisignature 
General form of a M-N multisignature:
* locking script:
```
M <publicKey1> <publicKey2> ... <publicKeyN> N CHECKMULTISIG
```
* unlocking script:
```
<SignatureA> <SignatureB> //any combination of 2 signatures from listed public keys
```
***a bug in <CHECKMULTISIG>***: *it pop an extra item in stack, to fix it, we have to put an extra disregarded item (customarily is 0) in the front of unlocking script*
```
// the correct version of unlocking script
0 <SignatureA> <SignatureB>
```

#### Pay-to-Script-Hash (P2SH)
make the use of complex scripts as easy as a payment to a bitcoin address

++*different from normal complex scripts:*++
* replace the complex locking script with its ***digital fingerprint*** (the cryptographic hash)
* add the ***redeem script*** to the end of the original unlocking script
    * regard the complex locking script as the redeem script

example:
```
// the original complex script
locking script: 2 publicKeyA publicKeyB publicKeyC 3 CHECKMULTISIG
unlocking script: 0 SignatureA SignatureB
```
```
// translate to P2SH
redeem script: 2 publicKeyA publicKeyB publicKeyC 3 CHECKMULTISIG
locking script: HASH160 <20-byte hash of redeem script> EQUAL
unlocking script: 0 SignatureA SignatureB <redeem script>

```

++*P2SH Addresses:*++:   
* P2SH addresses are Base58Check encodings of the 20-byte hash of a script 
* bitcoin addresses are Base58Check encodings of the 20-byte hash of a public key

example:
```
20-byte hash of a script: 54c557e07dde5bb6cb791c7a540e0a4796f5e97e
Base58Check encoding of it: 39RF6JqABiHdYHkfChV6USGMe6Nsr66Gzw

//P2SH addresses use the version prefix "5," which results in Base58Check-encoded addresses that start with a "3."
```

***P2SH addresses hide all of the complexity, so that the person making a payment does not see the script.***

++*Benefits of P2SH*++
* Complex scripts are replaced by shorter fingerprints in the transaction output, making the transaction smaller.
* Scripts can be coded as an address, so the sender and the sender’s wallet don’t need complex engineering to implement P2SH.
* P2SH shifts the burden of constructing the script to the recipient, not the sender.
* P2SH shifts the burden in data storage for the long script from the output (which additionally to being stored on the blockchain is in the UTXO set) to the input (only stored on the blockchain).
* P2SH shifts the burden in data storage for the long script from the present time (payment) to a future time (when it is spent).
* P2SH shifts the transaction fee cost of a long script from the sender to the recipient, who has to include the long redeem script to spend it.

++*Redeem Script and Validation*++
* P2SH transactions can contain ant valid script (after version 0.9.2 of the Bitcoin Core client)
* P2SH is not recursive: not able to put a P2SH inside a P2SH redeem script
* the UTXO of a P2SH transaction can be locked successfully even if it contain a hash of an invalid redeem script
    * because the redeem script is not presented to the network until you attempt to spend a P2SH UTXO
    * risk of locking bitcoin accidently - a user lock his bitcoin in a P2SH output which contain the hash of an unexcepted invalid redeem script, the UTXO will be locked successfully but no one can unlock it because the redeem script is invalid

#### Data Recording Output (RETURN)


#### Timelocks

timelocks are ***restrictions*** on transactions or outputs that ***only allow spending after a point in time***

* transaction-level timelock: 
    * exist from the begining of bitcoin
    * implemented by the nLocktime field in a transaction 
* UTXO-level timelocks:
    * introduced in late 2015 and mid-2016
    * implemented by operator codes - CHECKLOCKTIMEVERIFY and CHECKSEQUENCEVERIFY


#### nLocktime - transaction-level timelock
 
a field in transaction data structure
 
defines the earliest time that a transaction is valid and can be relayed on the network or added to the blockchain

++*nLocktime*++ (the variable name used in the Bitcoin codebase)
* ***be set to zero*** (in most transactions): to indicate ***immediate propagation and execution***
* ***0 < nLocktime < 500,000,000***: be interpreted as a ***block height***
    * meaning the transaction is not valid and is not relayed or included in the blockchain prior to the specified block height
* ***nLocktime > 500,000,000***: be interpreted as a ***Unix Epoch timestamp*** (seconds since Jan-1-1970)
    * meaning the transaction is not valid prior to the specified time   
if a transaction is transmitted to the network before the specified nLocktime, the transaction will be rejected by the first node as invalid and will not to be relayed to other nodes

++*transaction locktime limitations*++
* only guarantee : ***remittee*** of the transaction which is set specified nLocktime is ***not possible*** to spend the fund in UTXOs referred by this transation ***prior to the specified nLocktime***
* not guarantee: ***remitter*** of the transaction which is set specified nLocktime is not possible to spend the fund in UTXOs referred by this transation prior to the specified nLocktime
    * the remitter ***can double spend*** the funds in referred UTXOs by creating another transaction referred the same UTXOs without set specified nLocktime ***before remittee can spend it***


#### Check Lock Time Verify (CLTV) - UTXO-level timelock

introduce a new script operator called *CHECKLOCKTIMEVERIFY* (CLTV) to the bitcoin scripting language
 
++*CLTV opcode*++
* ***restrict a output*** by adding the CLTV opcode in the ***redeem script*** of it, so that it can only be spent after the specified time has elapsed
* CLTV ***doesn't replace*** nLocktime
    * it restricts specific UTXOs such that they can only be spent in a future transaction with nLocktime  set to a greater or equal value
* take one parameter as input
    * the parameter is expressed as a number in the same format as nLocktime (either a block height or Unix epoch time)
    
++*an example of using CLTV*++
 
case 1. without CLTV
Alice is paying Bob's address - the output normally contain a P2PKH script like:
```
DUP HASH160 <Bob's Public Key Hash> EQUALVERIFY CHECKSIG
```

case 2. using CLTV
to lock it to a 3 mothers from now, the output would be a P2SH transaction output with redeem script like:
```
<now + 3 months> CHECKLOCKTIMEVERIFY DROP DUP HASH160 <Bob's Public Key Hash> EQUALVERIFY CHECKSIG
```
* <now + 3 months> = ***current block height + 12,960 (blocks)*** or ***current Unix epoch time + 7,760,000***
* DROP opcode: ignore it now
* if Bob want to spend this UTXO, he need:
    1. constructs a transaction that references the UTXO as the input
    2. uses his signature and public key in the unlocking script of that input
    3. sets the ***transaction nLocktime*** to be ***equal or greater*** to the ***timelock in the CHECKLOCKTIMEVERIFY*** Alice set
    4. broadcasts the transaction on the bitcoin network
