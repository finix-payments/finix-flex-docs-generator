
> Example Response:

```json
{{underwrite_identity_scenario_response}}
```

Underwrite a previously created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


### HTTP Request

`POST {{base_url}}/identities/identity_id/merchants`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}
