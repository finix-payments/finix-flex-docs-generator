> Example Response:

```json
{{create_subscription_schedule_scenario_response}}
```
Subscription plans allow you to perform an action on a merchant on a recurring basis.

#### HTTP Request

`POST {{staging_base_url}}/subscription/subscription_schedules`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the subscription plan
subscription_type | *string*, **required** | Type of subscription plan. (e.g. PERIODIC, FIXED_TIME, AD_HOC)
period_type | *string*, **optional** | Specifies billing frequency. (e.g. MONTHLY, or YEARLY)
period_offset | *string*, **optional** | Specifies when the schedule begins (e.g. 5 means 5th of the month for MONTHLY)

fixed_time_interval | *integer*, **optional** | Unit : hour
fixed_time_count | *integer*, **optional** | Specifies how many times for triggering the bill plan
