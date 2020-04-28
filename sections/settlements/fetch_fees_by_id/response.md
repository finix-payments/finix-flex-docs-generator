> Example Response:

```json
{{fetch_fees_by_id_scenario_response}}
```

This call allows you to view fees for a `Settlement` by the `Fee` ID


#### HTTP Request

`GET {{staging_base_url}}/fees/:FEE_ID`


#### URL Parameters
Parameter | Description
--------- | -------------------------------------------------------------------
:FEE_ID | ID of the `Fee`

#### Response

Field | Type | Description
----- | ---- | -----------
id | *string* | `Review Queue` ID
amount | *integer* | `Fee` amount
currency | *string* | Currency type
display_name | *string* | The default is 'null' unless a custom fee_subtype is added
fee_subtype | *string* | Type of `Fee`. Options available include: Custom, `Application`, and `Platform`
fee_type | *string* | Description of the `Fee` type. This description is determined by the type of `Fee Profile` set up in the dashboard
merchant_id | *string* | Unique `Merchant` ID
tags  | *object* | Key value pair for annotating custom meta data
