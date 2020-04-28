> Example Response:

```json
{{{{list_settlement_transfers_v2_scenario_response}}}}
```

List the batch of `Transfers` of type `DEBIT` and `REFUND` that comprise the net settled amount of a `Settlement`.

#### HTTP Request

`GET {{staging_base_url}}/settlement_engine/settlements/:SETTLEMENT_ID/transfers`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`

#### Response

Field | Type | Description
----- | ---- | -----------
id | *string*    | `Transfer` ID
amount| *integer* | The total amount that will be debited in cents (e.g. 100 cents to debit $1.00)
application | *string* | `Application` ID 
currency | *string* | Currency type 
destination| *string* | `Payment instrument` ID of destination for funds 
fee | *integer* | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
fee_type | *string* | Description of the `Fee` type. This description is determined by the type of `Fee Profile` set up in the dashboard
idempotency_id | *string* | A randomly generated value that you want associated with the request
merchant_identity | *string* | Identity ID of the `Merchant` whom you're charging on behalf of
messages | *string* | Displays specific decline fields from the `Processor`
raw | *string*  | Raw `Processor` response. It holds data that the `Processor` sends to us after we initiate a `Transfer`
ready_to_settle_at | *string* | Timestamp of when the `Transfer` is ready to be settled 
source | *string* | `Payment instrument` ID of the source of funds 
state | *string* | State of the `Transfer`
statement_descriptor| *string* | Description of the purchase that appears on a credit card statement
subtype | *string* | Additional `Transfer` information
tags | *object* | Key value pair for annotating custom meta data (e.g. order numbers)
trace_ID | *string* | The ID assigned to this transaction by the `Processor`
type | *string* | Type of `Transfer`. Options include: TRANSFER, FEE, REVERSE, SETTLEMENT, and DISPUTE