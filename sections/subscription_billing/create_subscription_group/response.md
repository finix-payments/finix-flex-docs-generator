> Example Response:

```json
{{create_subscription_group_scenario_response}}
```
A `Subscription Group` allows you to create a group that tides to a `Subscription Schedule` and `Subscription Plan`

#### HTTP Request

`POST {{staging_base_url}}/subscription/subscription_groups`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the group
:SUBSCRIPTION_SCHEDULE_ID | *string*, **required** | ID of the `Subscription Schedule`
:SUBSCRIPTION_PLAN_ID | *string*, **required** | ID of the `Subscription Plan`
