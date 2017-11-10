> Example Response:

```json
{{update_merchant_profile_scenario_response}}
```

Lastly, you'll update the Merchant's `merchant_profile` by making a PUT request and passing the `fee_profile` that you received from the previous step.

#### HTTP Request

`PUT {{staging_base_url}}/merchant_profiles/:MERCHANT_PROFILE`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_PROFILE | *string*, **required** | ID of the `MERCHANT_PROFILE`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
fee_profile | *string*, **required** | ID of the `fee_profile`
