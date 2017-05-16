> Example Response:

```json
{{payment_instrument_verification_scenario_response}}
```

#### HTTP Request

`POST {{staging_base_url}}/payment_instruments/:PAYMENT_INSTRUMENT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | The name of the processor

#### Address Verification Results (address_verification_results)
Letter | Description
------ | -------------------------------------------------------------------
D, F, M | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Type (card_type_code)

This one-character code indicates whether the account is credit, debit, prepaid, deferred debit, or charge. (This is the same Card Type Code field available through the General Attributes Inquiry API.)

Letter | Description
------ | -------------------------------------------------------------------
C | Credit  
D | Debit  
H | Charge Card    
P | Prepaid  
R | Deferred Debit  

#### Fasts Funds Indicator (fast_funds_indicator)

For use in push-payment transactions, this code indicates whether or not the issuer of the recipient account participates in the Fast Funds service for Original Credit Transactions (OCTs).

Letter | Description
------ | -------------------------------------------------------------------
B | Recipient issuer participates in Fast Funds for all transactions
C | Reserved for future use
D | Recipient issuer participates in Fast Funds for domestic transactions only
N | Recipient issuer does not participate in Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

For use in push-payment transactions, this code indicates if the recipient account can receive push-payments (Original Credit Transactions).  

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push to card payments
C | Does not accept push to card payments

#### Online Gambling Block Indicator.

For use in push-payment transactions, this code indicates if the recipient account can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y | Accepts push to card payments
N | Does not accept push to card payments
