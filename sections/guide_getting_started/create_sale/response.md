

> Example Response:

```json
{{create_sale_scenario_response}}
```

At this point we've created resources representing the merchant, the buyer, and
the buyer's card.

Next you'll need to create a `Transfer`. To generate a `Transfer` we'll supply the buyer's `Payment Instrument` ID as the source field and the seller's `Merchant` ID in the merchant field. Note that the `amount` field is in cents. These specific `Transfers` are distinguished by their type which return DEBIT.

Alternatively, a user can create an `Authorization` and then proceed to capture the `Authorization` in two API calls. This is useful when you're looking to capture a specific amount on a card at a later date. You can find more information on [Authorization's flow](#authorizations).  

Learn how to prevent duplicate transfers by passing an [idempotency ID](#idempotency-requests) in the payload.

#### HTTP Request

`POST {{staging_base_url}}/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be debited
merchant | *string*, **required** | `Merchant` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be debited in cents (e.g. 100 cents to debit $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)processor | *string*, **optional** | If the Application has more than one processor associated to it, it's required to pass the processor (e.g. DUMMY_V1)
idempotency_id | *string*, **optional** | A randomly generated value that you want associated with the request
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
