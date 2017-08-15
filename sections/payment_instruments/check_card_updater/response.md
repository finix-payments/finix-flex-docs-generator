> Example Response:

```json
{{check_card_updater_scenario_response}}
```

#### Immediate Response

When first making a Post request to the `updates` endpoint, the state field will either be pending or failed.

1. `PENDING`: The initial Account Update request has been approved by the card networks and is awaiting review.

2. `FAILED`: Request rejected due to one of the following reasons:
  * Invalid credit card number
  * Invalid expiration date


#### Subsequent Response


Once {{api_name}} receives a response from the card network, the state of the `Update` resource will return either `SUCCEEDED` or `FAILED`. Each `Update` will also provide a message that details the reason for the outcome. If either an account number or expiration date was found, {{api_name}} will automatically update the
associated `Payment Instrument` resource with the new details and the card will be
ready for use.


<aside class="warning">
This process can take up to five days. {{api_name}} suggests utilizing webhooks
to listen for the response.
</aside>

1. `SUCCEEDED` Messages:
  * No changes found
  * The account number was changed
  * The expiration date was changed

2. `FAILED` Messages:
  * No match found
  * Invalid payment type (often due to unsupported card brands, e.g. Amex)
  * The issuing bank does not participate in the update program
  * The account was closed

#### HTTP Request

`POST {{staging_base_url}}/payment_instruments/:PAYMENT_INSTRUMENT_ID/updates/`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant`
:PAYMENT_INSTRUMENT_ID | *string*, **required** | ID of the `Payment Instrument`
