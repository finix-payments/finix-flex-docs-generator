> Example Response:

```json
{{toggle_application_settlements_scenario_response}}
```

Disable an `Applications's` ability to create new `Settlements`

#### HTTP Request

`PUT {{staging_base_url}}/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | False to disable