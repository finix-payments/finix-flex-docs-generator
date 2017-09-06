

> Example Response:

```json
{{create_bank_debit_scenario_response}}
```

A `Transfer` representing a customer payment where funds are obtained from a
bank account (i.e. ACH Debit, eCheck). These specific `Transfers` are
distinguished by their type which return DEBIT.

Learn how to prevent duplicate transfers by passing an [idempotency ID](#idempotency-requests) in the payload.

#### HTTP Request

`POST {{staging_base_url}}/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be debited
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be debited in cents (e.g. 100 cents to debit $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
idempotency_id | *string*, **optional** | A randomly generated value that you want associated with the request
