## Testing Data

Below are the different scenarios that we have available for the sandbox environment.

Cards for Testing a Payout  

Scenario                                     | number           | security_code | address.line1        | postal_code | region         | city          | country | address_verification_results | cvv2_result_code
 ---------------------------------------------|------------------|---------------|----------------------|-------------|----------------|---------------|---------|------------------------------|-----------------
 Successful push to card payout (credit card) | 4957030420210454 | 999           | 801 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Y                            | M   
 Successful push to card payout (debit card)  | 4895142232120006 | 022           | 900 Metro Center Blv | 94404       | CA             | San Francisco | USA     | M                            | M               
 Invalid account number                       | 4957040000000001 | 999           | 801 Metro Center Blv | 94404       | CA             | San Francisco | USA     | I                            | P               
 Invalid Zip Code and CVV2 values             | 4957030420210488 | 227           | 900 Metro Center Blv | 94402       | CA             | San Francisco | USA     | A                            | N               
 Invalid CVV2 value                           | 4957030420210496 | 664           | 900 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Y                            | N               
 Invalid Address, Zip code and CVV2 values    | 4957030420210504 | 322           | 901 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Z                            | N


Cards for Testing a Verification  

Scenario                                                     | number           | fast_funds_indicator | push_funds_block_indicator    | card_type_code | card_issuer_country_code  |
-------------------------------------------------------------|------------------|----------------------|-------------------------------|----------------|---------------------------|
Issuer does Participates in Fast Funds                       | 4815070000000018 | D                    | C                             | D              | 840                       |
Issuer does Not Participates in Fast Funds                   | 4855070000000035 | N                    | C                             | D              | 840                       |
Issuer does Not Participates in Fast Funds or Push to Card   | 4895047700003297 | N                    | N                             | C              | 840                       |
