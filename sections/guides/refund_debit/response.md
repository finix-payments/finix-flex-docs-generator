
> Example Response:

```json
{{create_refund_scenario_response}}
```

What if we need to issue a refund to the buyer? Easy enough. Just remember that
the amount can be equal to or less than the original debit.

#### HTTP Request

`POST {{base_url}}/transfers/transfer_id/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | Amount of the refund in cents (Must be equal to or less than the amount of the original debit)

