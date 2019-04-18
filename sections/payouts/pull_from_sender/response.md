> Example Response:

```json
{{create_sender_push_to_card_transfer_response}}
```

To create a `Transfer` we'll simply supply the Payment Instrument ID of a card that you want to pull funds from. In addition, you'll pass the an operational key which describes the action that you're taking.

You'll also want to store the ID from that `Transfer` for your records. `Transfers` can have two possible states SUCCEEDED and FAILED.

#### HTTP Request

`POST {{staging_base_url}}/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` where funds will be pulled from
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD, CAD)
operation_key | *string*, **required** | PULL_FROM_CARD
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
