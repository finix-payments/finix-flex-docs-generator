> Example Response:

```json
{{fetch_subscription_group_history_scenario_response}}
```

#### HTTP Request

`GET {{staging_base_url}}/subscription/subscription_groups/:SUBSCRIPTION_GROUP_ID/subscription_group_histories?subscription_schedule_id=:SUBSCRIPTION_SCHEDULE_ID&subscription_plan_id=:SUBSCRIPTION_PLAN_ID `

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SUBSCRIPTION_GROUP_ID | ID of the `Subscription Group`
:SUBSCRIPTION_SCHEDULE_ID | ID of the `Subscription Schedule`
:SUBSCRIPTION_PLAN_ID | ID of the `Subscription Plan`
