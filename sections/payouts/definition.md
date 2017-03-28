# Payouts

A `Payout` represents any flow of funds either to or from a `Payment Instrument`.
For example, a `Payout` can be either a [debit to a card](#debit-a-card), a
credit to a bank account, or a [refund to a card](#refund-a-debit) depending on
the request.

`Payouts` can have three possible states values: PENDING, SUCCEEDED, or FAILED.

- **SUCCEEDED:** Funds captured and available for settlement (i.e. disbursement
via ACH Credit)
        
- **FAILED:** Authorization attempt failed

By default, `Payouts` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.
