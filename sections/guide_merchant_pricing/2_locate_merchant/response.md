> Example Response:

```json
{{fetch_merchant_fee_scenario_response}}
```

Make a GET request with your `Merchant`'s ID. You'll want to keep the `merchant_profile` from the response for the following step.

#### HTTP Request

`GET {{staging_base_url}}/merchants/:MERCHANT_ID`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant`
