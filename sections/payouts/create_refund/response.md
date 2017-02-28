> Example Response:

```json
{{create_refund_scenario_response}}
```

A `Payout` representing the refund (i.e. reversal) of a previously created
`Payout` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Payout`. These specific `Payouts` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST {{staging_base_url}}/transfers/:PAYOUT_ID/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYOUT_ID | ID of the original `Payout`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | The amount of the refund in cents (Must be equal to or less than the amount of the original `Payout`)
