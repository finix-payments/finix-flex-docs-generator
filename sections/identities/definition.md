# Identities

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.
