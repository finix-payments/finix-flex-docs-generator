> Example Response:

```json
{{avs_scenario_response}}
```

#### HTTP Request

`PUT {{staging_base_url}}/risk_profiles/:RISK_PROFILE_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:RISK_PROFILE_ID| ID of the `Merchant`'s risk profile 


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
avs_failure_allowed | *boolean*, **required** | False to disable
cvv_failure_allowed | *boolean*, **required** | False to disable

