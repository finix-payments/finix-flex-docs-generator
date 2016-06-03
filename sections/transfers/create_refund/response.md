

> Example Response:

```json
{{create_refund_scenario_response}}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

### HTTP Request

`POST {{base_url}}/transfers/transfer_id/reversals`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
refund_amount | *integer*, **required** | The amount of the refund in cents. Must be equal to or less than the amount of the original debit. | 100
