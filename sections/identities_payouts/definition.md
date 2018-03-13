# Identities

An `Identity` resource represents either an individual recipient or business and is in many ways the centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must be associated with an `Identity`. This structure makes it easy to manage and reconcile their associated payment history, transaction history, and payouts.

This field is optionally used to collect KYC information for the recipient.
