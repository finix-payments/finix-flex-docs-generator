> Example Response:

```json
{{toggle_on_application_processing_scenario_response}}
```

Now that we have a processor associated with an `Application` we'll want to
enable its ability to creaet new `Transfers` and `Authorizations`. This same
method can be used to shut off its ability to process transactions as a form of
risk management.

#### HTTP Request

`PUT {{base_url}}/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processing_enabled | *boolean*, **required** | True to enable