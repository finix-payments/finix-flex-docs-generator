> Example Response:

```json
{{review_queue_filter_scenario_response}}
```

This call can filter the `Review Queue` for an individual `Settlement`. The response displays the status of the `Settlement`.   

#### HTTP Request

`GET {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&entity_id=:ENTITY_ID`

#### URL Parameters

Parameter | Description
----- | -----------------------
:ENTITY_TYPE | Refers to the type of `Review Queue` item. The entity_type available are: IDENTITY, MERCHANT, and SETTLEMENT
:ENTITY_ID | Entity ID. This ID can refer to any entity type



#### Response

Field | Type | Description
----- | ---- | -----------
id | *string* | `Review Queue` ID
application | *string* | `Application` ID
completed_at | *string* | Timestamp of when the `Review Queue` was updated to its final state
entity_id | *string* | Entity ID. This ID can refer to any entity type
entity_type | *string* | Type of `Review Queue` item
outcome | *string* | Status of the `Settlement`
processor_type | *string* | `Processor` type
reviewed_by | *string* | `User` ID of the person who is approving or rejecting the `Review Queue` item
review_type | *string* | Status of the `Review Queue` item
tags  | *object* | Key value pair for annotating custom meta data
created_at | *string* | Timestamp of when the `Review Queue` was created
updated_at | *string* | Timestamp of when the `Review Queue` was updated
