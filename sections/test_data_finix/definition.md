## Testing for specific responses and errors

### Payment Facilitation Testing
Before taking your integration to live, use the information below to test it thoroughly. Please note, once a Payment Instrument has been flagged with AVS or CVC, it will continue to throw the respective error.

Amount| Description
----- | -----------
`100` | Success amount
`102` | Failed amount
`888888` | Disputed amount
`193` | Insufficient funds amount
`194` | Invalid card number amount
`889986` | AVS total failure amount
`889987` | CVC failure amount

Card| Description
----- | -----------
 `4000000000000036` | Payment card AVS total failure  
 `4000000000000127` | Payment card CVC failure  

### Push-to-Card Testing  
Cards for Testing a Push to Card Payout  

 Scenario                                       | number              | region          | country | code
  ----------------------------------------------|--------------------|-----------------|---------  |-----------------
  Successful push to a Visa (debit card)        | 4895142232120006  | CA              | USA        | N/A               
  Successful push to a Visa (credit card)       | 4957030420210454  | CA              | USA        | N/A   
  Successful push to a Mastercard (debit card)  | 5123280115058611  | CA              | USA        | N/A               
  Invalid account number                        | 4957030420210504  | CA              | USA        | INVALID_INSTRUMENT               
  Exceeds approval amount limit                 | 4957030420210488  | CA              | USA        | EXCEEDS_ISSUER_AMOUNT_LIMIT               
  Exceeds withdrawal frequency limit            | 4957030420210496  | CA              | USA        | EXCEEDS_ISSUER_COUNT_LIMIT               
  Refer to card issuer                          | 4895070000007685  | CA              | USA        | CALL_ISSUER
  Do not honor                                  | 4895070000006687  | CA              | USA        | DECLINE
  Lost card, pick up (fraud account)            | 4895070000005671  | CA              | USA        | LOST_OR_STOLEN_CARD
  Suspected fraud                               | 4895070000004674  | CA              | USA        | SUSPECTED_FRAUD
  Transaction does not fulfill AML requirement  | 4895070000003551  | CA              | USA        | COMPLIANCE_VIOLATION


Cards for Testing a Verification  

Scenario                                                     | number           | fast_funds_indicator | push_funds_block_indicator    | card_type_code | card_issuer_country_code  |
-------------------------------------------------------------|------------------|----------------------|-------------------------------|----------------|---------------------------|
Issuer does Participates in Fast Funds                       | 4815070000000018 | D                    | C                             | D              | 840                       |
Issuer does Not Participates in Fast Funds                   | 4855070000000035 | N                    | C                             | D              | 840                       |
Issuer does Not Participates in Fast Funds or Push to Card   | 4895047700003297 | N                    | N                             | C              | 840                       |
