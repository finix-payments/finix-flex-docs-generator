> Example Response:

```json
{{capture_authorization_scenario_response}}
```

### HTTP Request

`PUT {{base_url}}/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
capture_amount | *integer*, **required** | The amount of the authorization you would like to capture in cents. Must be less than or equal to the amount of the authorization | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
