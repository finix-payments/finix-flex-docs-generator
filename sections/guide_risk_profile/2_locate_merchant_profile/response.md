> Example Response:

```json
{{fetch_merchant_profile_scenario_response}}
```

Make a GET request with the `merchant_profile` ID that you received from the previous step. You'll want to keep the `risk_profile` handy for the next step.

#### HTTP Request

`GET {{staging_base_url}}/merchants/:MERCHANT_PROFILE`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_PROFILE | *string*, **required** | ID of the `Merchant Profile`
