> Example Response:

```json
{{create_bank_account_scenario_response}}
```

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing
purposes.
</aside>

Please review our guide on how to tokenize `Payment Instruments` via the
[tokenization.js library](#tokenization-js)


#### HTTP Request

`POST {{base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **optional** | Account owner's full name
