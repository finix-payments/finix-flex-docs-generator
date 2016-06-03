

> Example Response:

```json
{{create_settlement_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities/:identity_id/settlements`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}
currency | *integer*, **required** | The currency for the settlement. | USD

