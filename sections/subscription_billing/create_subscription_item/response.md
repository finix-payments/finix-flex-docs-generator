> Example Response:

```json
{{create_subsciption_item_scenario_response}}
```

Subscription items allow you to create a merchant subscription

#### HTTP Request

`POST {{staging_base_url}}/subscription/subscription_group/:SUBSCRIPTION_GROUP_ID/subscription_items`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SUBSCRIPTION_GROUP_ID | ID of the `Subscription Group`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the subscription item
:MERCHANT_ID | *string*, **required** | ID of the `Merchant`
started_at | *string*, **required** | Time the subscription will begin in DateTime format
ended_at | *string*, **required** | Time the subscription will end in DateTime format. If left blank, it will continue in perpetuity
