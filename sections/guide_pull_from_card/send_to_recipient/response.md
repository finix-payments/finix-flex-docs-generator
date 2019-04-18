> Example Response:

```json
{{create_recipient_push_to_card_transfer_response}}
```


Now the final step - time to payout the recipient!

Next you'll need to create a `Transfer`.  What's a `Transfer`? Glad you asked! A `Transfer` represents any flow of funds either to or from a Payment Instrument. In this case a Payout to a card.

To create a `Transfer` we'll simply supply the Payment Instrument ID of the previously tokenized card as the destination field. Also, be sure to note that the amount field is in cents.

Simple enough, right? You'll also want to store the ID from that `Transfer` for your records. `Transfers` can have two possible states SUCCEEDED and FAILED.


#### HTTP Request

`POST {{staging_base_url}}/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where funds will be sent
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD, CAD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
