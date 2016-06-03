> Example Response:

```json
{{create_authorization_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/authorizations`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | {{create_card_scenario_id}}
merchant_identity | *string*, **required** | UID. | {{create_identity_scenario_id}}
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}
