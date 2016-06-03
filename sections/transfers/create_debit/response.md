

> Example Response:

```json
{{create_debit_scenario_response}}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST {{base_url}}/transfers`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | {{create_card_scenario_id}}
merchant_identity | *string*, **required** | UID. | {{create_identity_scenario_id}}
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}
