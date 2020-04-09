> Example Response:

```json
{{create_bank_account_scenario_response}}
```

<aside class="warning">
 Ensure that you create an additional buyer Identity separate from the merchant Identity. Associate the buyer Identity with the bank account you tokenize.  
</aside>


#### HTTP Request

`POST {{staging_base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **required** | Account owner's full name (max 40 characters)
