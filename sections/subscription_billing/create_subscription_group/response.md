> Example Response:

```json
{{create_subscription_group_scenario_response}}
```
Subscription group allows you to create a group that tides to a subscription schedule and subscription plan

#### HTTP Request

`POST {{staging_base_url}}/subscription/subscription_groups`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the group
:SUBSCRIPTION_PLAN_ID | *string*, **required** | ID of the `Subscription Plan`
:SUBSCRIPTION_SCHEDULE_ID | *string*, **required** | ID of the `Subscription Schedule`
