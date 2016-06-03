> Example Response:

```json
{{create_card_scenario_response}}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST {{base_url}}/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
identity | *string*, **required** | Identity resource which the card is associated. | {{create_buyer_identity_scenario_id}}
first_name | *string*, **optional** | Customer's first name on card. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | PAYMENT_CARD
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020
line1 | *string*, **optional** | Street address of the associated card. | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address of the associated card. |  Apt. 3
city | *string*, **optional** | City of the associated card. | San Mateo
region | *string*, **optional** | State of the associated card. | CA
postal_code | *string*, **optional** | Postal of the associated card. | 92704
country | *string*, **optional** | Country of the associated card. | USA