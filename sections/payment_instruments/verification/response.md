> Example Response:

```json
{{payment_instrument_verification_payouts_scenario_response}}
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
------ | -------------------------------------------------  ------------------
D, F, M, Y | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Verification 2 Results (cvv2_result_code)
Letter | Description
------ | -------------------------------------------------------------------
M | CVV and expiration dates verified
N, P, S | Either CVV or expiration date is incorrect
U | Issuer does not participate in CVV2 service

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

Indicates whether or not the card is Fast Funds eligible (i.e. if the funds will settle in 30 mins or less). If not eligible, typically funds will settle within 2 business days.

Letter | Description
------ | -------------------------------------------------------------------
B, D | Fast Funds eligible
N | Not eligible for Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

This code indicates if the associated card can receive push-to-card disbursements.

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push-to-card payments
N | Does not accept push-to-card payments

#### Online Gambling Block Indicator (online_gambing_block_indicator)

Indicates if the card can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y | Blocked for online gambling payouts
N | Not blocked for online gambling payouts

#### Card Product ID (card_product_id)

A combination of card brand, platform, class and scheme.

Letter | Description
------ | -------------------------------------------------------------------
A | Visa Traditional
AX | American Express
B | Visa Traditional Rewards
C | Visa Signature
D | Visa Signature Preferred
DI | Discover
DN | Diners
E | Proprietary ATM
F | Visa Classic
G | Visa Business
G1 | Visa Signature Business
G2 | Visa Business Check Card
G3 | Visa Business Enhanced
G4 | Visa Infinite Business
G5 | Visa Business Rewards
I | Visa Infinite
I1 | Visa Infinite Privilege
I2 | Visa UHNW
J3 | Visa Healthcare
JC | JCB
K | Visa Corporate T&E
K1 | Visa Government Corporate T&E
L | Visa Electron
M | MasterCard
N | Visa Platinum
N1 | Visa Rewards
N2 | Visa Select
P | Visa Gold
Q | Private Label
Q1 | Private Label Prepaid
Q2 | Private Label Basic
Q3 | Private Label Standard
Q4 | Private Label Enhanced
Q5 | Private Label Specialized
Q6 | Private Label Premium
R | Proprietary
S | Visa Purchasing
S1 | Visa Purchasing with Fleet
S2 | Visa Government Purchasing
S3 | Visa Government Purchasing with Fleet
S4 | Visa Commercial Agriculture
S5 | Visa Commercial Transport
S6 | Visa Commercial Marketplace
U | Visa Travel Money
V | Visa V PAY

#### Product Sub-Type (card_product_subtype)

Description of product subtype.

Letter | Description
------ | -------------------------------------------------------------------
AC | Agriculture Maintenance Account
AE | Agriculture Debit Account/Electron
AG | Agriculture
AI | Agriculture Investment Loan
CG | Brazil Cargo
CS | Construction
DS | Distribution
HC | Healthcare
LP | Visa Large Purchase Advantage
MA | Visa Mobile Agent
MB | Interoperable Mobile Branchless Banking
MG | Visa Mobile General
VA | Visa Vale - Supermarket
VF | Visa Vale - Fuel
VR | Visa Vale - Restaurant

#### Card Sub-Type (card_subtype_code)

The code for account funding source subtype, such as reloadable and non-reloadable.

Letter | Description
------ | -------------------------------------------------------------------
N | Non-Reloadable
R | Reloadable
