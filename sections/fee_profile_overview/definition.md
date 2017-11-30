# Fee Profiles

A `Fee Profile` represents a pricing scheme that automatically applies fees to each transaction. When the `Merchant` receives a settlement the resulting fees are automatically deducted and disbursed as a credit to the payment facilitator.
`Fee profiles` support interchange plus, percentage-based pricing (e.g. 2.9%) and fixed-based fees (e.g. $0.20 per transaction).

`Fee Profiles` follow a tree-like data structure - all `Applications` and subsequently their `Merchants` inherit from a single default `Fee Profile` but can be overridden to set custom billing for individual `Applications` or `Merchants`. Note, that by default both an `Application's` and a `Merchant's` `Fee Profiles` will be set to null. When a `Merchant's` fee profile is set to null then it inherits from the parent node, which in this case is the `Application`. If the `Application` is also null then it inherits from the default `Fee Profile`.
