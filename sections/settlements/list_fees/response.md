> Example Response:

```json
{{list_fees_response}}
```



#### HTTP Request

`GET {{staging_base_url}}/fees`


#### URL Parameters

#### URL Fields
Field | Type | Description
----- | ---- | -----------
id | *string*    | `Fee` ID
amount | *integer* | Fee amount
currency | *string* | Currency type
display_name | *string* | The default is `null` unless a custom fee_subtype is added
fee_subtype | *string* | Type of fee. Options available include: Custom, Application, and Platform
fee_type | *string* | Description of the fee type. This description is determined by the type of fee profile set up in the dashboard
merchant_id | *string* | Unique merchant ID
tags  | *object* | Key value pair for annotating custom meta data
