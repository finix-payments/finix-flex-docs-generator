> Example Response:

```json
{{update_transfer_scenario_response}}
```

#### HTTP Request

`PUT {{staging_base_url}}/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`


#### Request Parameters
Field | Type | Description
----- | ---- | -----------
tags | *object*, **required** | Key value pair for annotating custom meta data (e.g. order numbers)
