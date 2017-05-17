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
processor | *string*, **required** | The name of the processor, which needs to be: `VISA_V1`

#### Address Verification Results (address_verification_results)
Letter | Description
------ | -------------------------------------------------------------------
D, F, M | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Type (card_type_code)

This one-character code indicates whether the account is credit, debit, prepaid, deferred debit, or charge.

Letter | Description
------ | -------------------------------------------------------------------
C | Credit  
D | Debit  
H | Charge Card    
P | Prepaid  
R | Deferred Debit  

#### Fasts Funds Indicator (fast_funds_indicator)

Indicates whether or not the card is Fast Funds eligible (i.e. if the funds will settle in 30 mins or less). If not eligible, typically funds will settle within 2 days.

Letter | Description
------ | -------------------------------------------------------------------
B | Fast Funds eligible for all transactions
D | Fast Funds eligible for all transactions
N | Not eligible for Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

This code indicates if the associated card can receive push-payments (Original Credit Transactions).

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push to card payments
C | Does not accept push to card payments

#### Online Gambling Block Indicator.


Indicates if the card can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y |
Indicates if the card can receive push-payments for online gambling payouts
N | Not eligible for online gambling payouts
