> Example Response:

```json
{{list_settlements_v2_scenario_response}}
```

This call displays all settlements in the review queue and their status. 

#### HTTP Request

`GET {{staging_base_url}}/settlement_engine/settlements`

#### Response

Field | Type | Description
----- | ---- | -----------
id | *string* | `Review Queue` ID
adjustment_credit_count | *integer* | Number of adjustments that are negative for a `Merchant` in a `Settlement` 
adjustment_debit_count | *integer* | Number of adjustments that are positive for a `Merchant` in a `Settlement` 
dispute_credit_count| *integer*| Number of credits that are negative for a `Merchant` in a `Settlement` 
dispute_debit_count | *integer* | Number of credits that are positive for a `Merchant` in a `Settlement` 
exception| *boolean* | The default is "false". When the field is set to "true", the `Settlement` contains exceptions that were removed from another `Settlement`
fee_count | *integer* | Number of fees collected in a `Settlement` 
merchant_id | *string* | `Merchant` ID 
net_amount | *integer | Total amount minus the total fee amount 
processor_type | *string* | `Processor` type 
reverse_count | *integer* | Number of reversals 
settlement_group_id | *string* | A collection of settlements that can be combined into a single line item 
status | *string* | `Settlement` status. Statuses available are: PENDING, AWAITING APPROVAL, STAGED, APPROVED
tags  | *object* | Key value pair for annotating custom meta data
total_amount  | *integer* | Total of all `Transfers` in a `Settlement` 
total_fee_amount| *integer* | Sum of all fees collected from a `Settlement` 
transfer_credit_count | *integer* | Number of `Transfers` that are negative for a `Merchant` in a `Settlement` 
transfer_debit_count| *integer* | Number of `Transfers` that are positive for a `Merchant` in a `Settlement`