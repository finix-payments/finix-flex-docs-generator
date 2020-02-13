# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

In v2 of the settlement engine, the `destination` attribute will be deprecated from all API's that return the settlement resource (e.g. STxxx). The `destination` field will be stored in `settlements/:SETTLEMENT_ID/funding_transfers`.
