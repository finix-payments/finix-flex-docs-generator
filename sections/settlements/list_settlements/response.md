> Example Response:

```json
{{create_identity_verification_scenario_response}}
```

Perform an identity verification check against a previously created Identity.

#### HTTP Request

`POST {{base_url}}/identities/identity_id/verifications`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | Service used for verifying the Identity, please use "{{identity_verification_processor}}" for now to test the API

