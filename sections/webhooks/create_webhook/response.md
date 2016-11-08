> Example Response:

```json
{{create_webhook_scenario_response}}
```

#### HTTP Request

`POST {{staging_base_url}}/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request
