## Testing for specific responses and errors

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
