## Testing for specific responses and errors

Before taking your integration to production, use the information below to test it thoroughly. Please note, once a Payment Instrument has been flagged with AVS or CVC, it will continue to throw the respective error.

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

 Below are the different error codes and message values that are returned for Push to Card.

 Scenario                                     | number           | security_code | address.line1        | postal_code | region         | city          | country | address_verification_results | cvv2_result_code
  ---------------------------------------------|------------------|---------------|----------------------|-------------|----------------|---------------|---------|------------------------------|-----------------
  Successful push to card payout (credit card) | 4957030420210454 | 999           | 801 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Y                            | M   
  Successful push to card payout (debit card)  | 4895142232120006 | 022           | 900 Metro Center Blv | 94404       | CA             | San Francisco | USA     | M                            | M               
  Invalid account number                       | 4957040000000001 | 999           | 801 Metro Center Blv | 94404       | CA             | San Francisco | USA     | I                            | P               
  Invalid Zip Code and CVV2 values             | 4957030420210488 | 227           | 900 Metro Center Blv | 94402       | CA             | San Francisco | USA     | A                            | N               
  Invalid CVV2 value                           | 4957030420210496 | 664           | 900 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Y                            | N               
  Invalid Address, Zip code and CVV2 values    | 4957030420210504 | 322           | 901 Metro Center Blv | 94404       | CA             | San Francisco | USA     | Z                            | N
