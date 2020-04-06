> Example Response:

```json
{{create_subscription_plan_scenario_response}}
```


A `Subscription Plan` allows you to create a plan for making a transaction.

#### HTTP Request

`POST {{staging_base_url}}/subscription/subscription_plans`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
plan_type | *string*, **required** | Type of the plan
name | *string*, **required** | The name of the plan
display_name | *string*, **optional** | The display name for grouping the settlement
amount | *integer*, **required** | A positive integer in cents representing how much to charge on a recurring basis
currency | *string*, **required** | Three-letter ISO currency code in uppercase
