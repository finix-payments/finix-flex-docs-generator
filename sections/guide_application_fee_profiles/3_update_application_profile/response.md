> Example Response:

```json
{{update_application_profile_scenario_response}}
```

Next, locate the Application's `application_profile`- there's a link to it on the application resource from the previous step. Lastly, you'll update the Application's `application_profile` by making a PUT request and passing the `fee_profile` that you received from the previous step.

#### HTTP Request

`PUT {{staging_base_url}}/application_profiles/:APPLICATION_PROFILE`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_PROFILE | *string*, **required** | ID of the `APPLICATION_PROFILE`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
fee_profile | *string*, **required** | ID of the `fee_profile`
