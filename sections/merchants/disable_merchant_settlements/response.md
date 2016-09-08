> Example Response:

```json
{{toggle_merchant_settlements_scenario_response}}
```
Disable a `Merchant's` ability to create new `Settlements`

#### HTTP Request

`PUT {{base_url}}/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | False to disable