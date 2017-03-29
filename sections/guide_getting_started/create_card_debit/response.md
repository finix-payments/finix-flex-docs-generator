
> Example Response:

```json
{{create_debit_scenario_response}}
```

At this point we've created resources representing the merchant, the buyer, and
the buyer's card.

To debit a card, you'll need to create a `Transfer`. What's a `Transfer`? Glad
you asked! A `Transfer` is basically any flow of funds from or two a
`Payment Instrument`. In other words, a `Transfer` can be charging a card,
issuing a credit to a bank account or issuing a refund. For now let's focus on
charging a card.

To do this we'll supply the buyer's `Payment Instrument` ID as the source field
and the seller's `Identity` ID in the merchant_identity field. Note that the
amount field is in cents. The `fee` field is the amount in cents you would like to
keep before settling out to the merchant. For example, if you're charging the
 buyer $100 on behalf of your merchant, and you're taking a 10% service fee
you'll want to pass 10000 as the amount and 1000 as the fee. This way when the
funds are eventually settled out only $90 will be disbursed to your merchant.

Simple enough, right? You'll also want to store the ID from that `Transfer` for
your records. Next we're going to show you how to settle out the funds to your
merchant.


#### HTTP Request

`POST {{staging_base_url}}/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the transfer you would like to collect as your fee (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the transfer (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
