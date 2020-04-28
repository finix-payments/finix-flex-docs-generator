> Example Response:

```json
{{list_fees_response}}
```

This call displays all the fees in a `Settlement` for a `Merchant`. 

#### HTTP Request

`GET {{staging_base_url}}/fees`


#### URL Parameters

#### URL Fields
Field | Type | Description
----- | ---- | -----------
id | *string*    | `Fee` ID
amount | *integer* | `Fee` amount
currency | *string* | Currency type
display_name | *string* | The default is `null` unless a custom fee_subtype is added
fee_subtype | *string* | Type of `Fee`. Options available include: Custom, Application, and Platform
fee_type | *string* | Description of the `Fee` type. This description is determined by the type of `Fee Profile` set up in the dashboard
merchant_id | *string* | Unique `Merchant` ID
tags  | *object* | Key value pair for annotating custom meta data
