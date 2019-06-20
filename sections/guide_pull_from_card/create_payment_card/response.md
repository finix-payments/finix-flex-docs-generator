> Example Response:

```json
{{create_sender_card_scenario_response}}
```

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Now that we've created an `Identity` for our sender, we'll need to tokenize a payment card where funds will be pulled from.

In the API, payment cards are represented by the `Payment Instrument` resource.

To classify the `Payment Instrument` as a payment card you'll need to pass `PAYMENT_CARD` in the type field of your request, and you'll also want to pass the ID of the `Identity` that you created in the last step via the identity field to properly associate it with your sender.

#### HTTP Request

`POST {{staging_base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
identity | *string*, **required** | ID of the `Identity` that the card should be associated
type | *string*, **required** | Type of Payment Instrument (for cards input PAYMENT_CARD)
number | *string*, **required** | Primary card account number
security_code | *string*, **optional** | The 3-4 digit security code for the card (i.e. CVV code)
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | 4-digit expiration year
name | *string*, **optional** | Full name of the registered card holder
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Payment Instruments` (e.g. USD, CAD)
address | *object*, **optional** | Billing address (Full description of child attributes below)



#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City 
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code
