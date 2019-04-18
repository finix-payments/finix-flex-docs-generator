## Testing Data

Below are the different scenarios that we have available for the sandbox environment.

Cards for Testing a Payout  

Scenario                                 | number           | postal_code | region   | country |
 ----------------------------------------|------------------|-------------|----------|---------|
 Successful push to card payout          | 4957030420210454 | 94404       | AB       |  CAN    |
 Transaction not permitted to cardholder | 4957030420210462 | 94404       | AB       |  CAN    |

 Cards for Testing the Pulling of Funds

 Scenario                                | number           | expiration_month     | expiration_year | postal_code   |
  ---------------------------------------|------------------|----------------------|-----------------|---------------|
  Approved and completed successfully    | 4957030005123304 | 03                   | 2020            | 94404         |
  Do not honor                           | 4957030420210488 | 03                   | 2020            | 94404         |
  Lost card, pick up (fraud account)     | 4957030420210496 | 03                   | 2020            | 94404         |


Cards for Testing a Verification  

Scenario                                                              | number           | fast_funds_indicator | push_funds_block_indicator    | card_type_code | card_issuer_country_code  |
----------------------------------------------------------------------|------------------|----------------------|-------------------------------|----------------|---------------------------|
Issuer does Participates in Fast Funds for domestic transactions only | 4815090000000016 | D                    | C                             | D              | 124                       |
Issuer does not Participates in Fast Funds                            | 4895069900009916 | N                    | B                             | D              | 124                       |
