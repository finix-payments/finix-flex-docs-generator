# Transfers

A `Transfer` represents any flow of funds either to or from a `Payment Instrument`.
For example, a `Transfer` can be either a [debit to a card](#debit-a-card), a
credit to a bank account, or a [refund to a card](#refund-a-debit) depending on
the request.

A `Transfer` can have one of three types: `Debit`, `Credit`, or `Reversal`. Each type indicates a different funds flow. For example:

* A **Debit** is created after capturing an Authorization or creating eCheck where funds are pulled from the issuer into the settlement account

* A **Reversal** represents a refund or chargeback where funds are returned to a customer

* A **Credit** is produced when funds are transferred to a merchant's bank account when funding (i.e. paying out) a batch settlement

`Transfers` can have four possible states values: PENDING, SUCCEEDED, FAILED, or CANCELED.

- **PENDING:** Authorization on `Payment Instrument` successfully created (i.e.
funds are being held), but awaiting system to batch submit the capture request
to complete the transaction

- **SUCCEEDED:** Funds captured and available for settlement (i.e. disbursement
via ACH Credit)

- **FAILED:** Authorization attempt failed

- **CANCELED:** Created, and then reversed before transfer has transitioned to succeeded

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

`ready_to_settle_at` field can have 2 possible values:

1. `null`: Funds have been captured, but are not yet ready to be paid out
2. `TIMESTAMP`: A UTC timestamp that specifies when the funds will be available to be payout out. Once in the past, the Transfer will be eligible for inclusion in a batch Settlement.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
