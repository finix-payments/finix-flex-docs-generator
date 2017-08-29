### Debit a Bank Account (ie eCheck)

Returns: Note eCheck transactions can be rejected for up to 60 days for a variety of reasons including insufficient funds, closed accounts, or a revoked authorization (i.e. dispute). When a return occurs a Transfer of type `REVERSAL` with a subtype `SYSTEM` is automatically created and will negatively impact the future settlement.
