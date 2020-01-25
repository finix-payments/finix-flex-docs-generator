> Example Response:

```json
{{update_merchant_profile_scenario_response}}
```

Lastly, you'll update the Merchant's `risk_profile` by making a PUT request and passing the `risk_profile`'s attributes that you want to update.

#### HTTP Request

`PUT {{staging_base_url}}/merchant_profiles/:RISK_PROFILE`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:RISK_PROFILE | *string*, **required** | ID of the `RISK_PROFILE`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
avs_failure_allowed | *boolean*, **required** | Setting this value to true will allow authorizations to go through even if the authorization failed its address verification
csc_failure_allowed | *boolean*, **required** | Setting this value to true will allow authorizations to go through even if the authorization failed its CVV check
