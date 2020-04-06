> Example Response:

```json
{{update_subsciption_group_scenario_response}}
```


#### HTTP Request

`PATCH {{staging_base_url}}/subscription/subscription_groups/:SUBSCRIPTION_GROUP_ID`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
SUBSCRIPTION_SCHEDULE_ID | *string*, **required** | ID of `Subscription Schedule`
SUBSCRIPTION_PLAN_ID | *string*, **required** | ID of `Subscription Plan`
name | *string*, **required** | Name of the group
