> Example Response:

```json
{{fetch_subscription_filters_scenario_response}}
```

#### HTTP Request

`GET {{staging_base_url}}/subscription/subscription_schedules?name=:NAME&subscription_type=:SUBSCRIPTION_TYPE `

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:NAME | Name of the subscription plan
:SUBSCRIPTION_TYPE | 	Type of subscription plan. (e.g. PERIODIC, FIXED_TIME, AD_HOC)
