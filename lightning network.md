#### Lightning Network
One of the first implementations of a ==multi-party Smart Contract== using ++bitcoin's built-in scripting++.

1. **Instant Payments**   
    * ++normal bitcoin transactions++: widely regarded as secure on bitcoin after confirmation of 6 blocks 
    * ++lightning++: payments don't need block confirmations
        * instant and atomic

2. **Micropayment**
    * ++bitcoin blockchain++: 
        * currently enforces  a minimum output size many hundreds of times higher than 1 Satoshi (0.00000001 BTC)
        * fixed per-transaction fee (makes micropayments impratical)
    * ++lightning++: enables one to send funds down to 0.00000001 BTC without custodial risk
3. **Scalability**
> **bitcoin scalability problem**: refers to the discussion concerning the limits on the amount of transactions the bitcoin network can process
> * the on chain transaction processing capacity of the bitcoin network is limited by the average block creation time of 10 minutes and the block size limit

* ++bitcoin network++ need: to support orders of magnitude higher transaction volume
    * the coming increase in internet-connected devices needs a platform for machine-to-machine payments and automated micropayment services
* ++lightning++:  
    * transactions are conducted the blockchain without delegation of trust and ownership
    * allowing users to conduct nearly unlimited transactions between other devices

#### How it works
channel: a two-party, multisignature bitcoin address, funds will be placed here

