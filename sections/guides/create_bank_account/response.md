> Example Response:

```json
{{create_bank_account_scenario_response}}
```

Now that we've created an `Identity` for our merchant, we'll need to add a bank
account where we can settle out the funds that are processed on behalf of your
merchant (i.e. their funding account).

In the API, bank accounts -- as well as credit cards -- are represented by the
`Payment Instrument` resource. There are two means of creating a
`Payment Instrument`: 1) directly via the API and 2) via our Tokenization.js
library. For testing purposes, we'll create one directly via the API; however,
please review our guide on how to tokenize payment instruments via the
[tokenization.js library](#tokenization-js) when in production.

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>

To classify the `Payment Instrument` as a bank account you'll need to pass
BANK_ACCOUNT in the `type` field of your request, and you'll also want to pass
the ID of the `Identity` that you created in the last step via the `identity`
field to properly associate it with your merchant.


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
