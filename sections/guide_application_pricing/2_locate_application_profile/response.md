> Example Response:

```json
{{fetch_application_profile_scenario_response}}
```

Make a GET request with your `Application`'s ID. You'll want to keep the `application_profile` in the link sections of the response for the following step.

#### HTTP Request

`GET {{staging_base_url}}/applications/:APPLICATION_ID/application_profile`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of the `Application`
