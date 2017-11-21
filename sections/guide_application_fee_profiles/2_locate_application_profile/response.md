> Example Response:

```json
{{fetch_application_profile_scenario_response}}
```

In the links you'll see the application_profile, which you'll want to store for the following step.

#### HTTP Request

`GET {{staging_base_url}}/applications/:APPLICATION_ID/application_profile`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of the `Application`
