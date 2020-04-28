> Example Response:

```json
{{list_settlement_funding_instructions_v2_scenario_response}}
```

This call displays the funding instructions for each `Settlement` ID. This displays the following information on the Funding Transfers in the dashboard: Created, Type, State, and Amount. 

#### HTTP Request

`GET {{staging_base_url}}/settlements/:SETTLEMENT_ID/funding_instructions`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


#### Response 

Field | Type | Description
----- | ---- | -----------
id | *string* | `Review Queue` ID 
amount | *integer* | Total amount for the funding instructions
code | *string*| The end state of the funding instructions
created_at | *string* | Timestamp when the resource was created
currency | *string* | Currency type 
destination_instrument_id | *string* | Payment instrument ID of destination for funds 
level | *string* | Description of the level to be paid
name | *string* | Description of the funding instructions 
overriden | *boolean* | The default  is "false". When it is set to "true", the customer has changed the default payment for a `Settlement`
rail | *instrument* | The rail used for a the funding instructions 
source_instrument_id | *string* | `Payment instrument` ID of source of funds 
tags  | *objects* | Key value pair for annotating custom meta data
updated_at | *string* | Timestamp when any change occurs to any of the fields listed above 