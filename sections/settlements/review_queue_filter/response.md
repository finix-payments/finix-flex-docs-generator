> Example Response:

```json
{{approve_settlement_via_review_queue_response}}
```

This call can filter the review queue for an individual `Settlement`. The response displays the status of the `Settlement`.   

#### HTTP Request

`GET {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&entity_id=:ENTITY_ID `

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
entity_type |
:ENTITY_ID | ID of the `Settlement`


#### Response

Field | Type | Description
----- | ---- | -----------
id | *string*    | Review queue ID
application | *string* | Application ID
completed_at | *string* | Timestamp of when the review queue was updated to its final state
created_at | *string* | Timestamp of when the review queue was created
entity_id | *string* | Entity ID. This ID can refer to any entity type
entity_type | *string* | Type of review queue item
outcome | *string* | Status of the `Settlement`
processor_type | *string* | Processor type
reviewed_by | *string* | User ID of the person who is approving or rejecting the review queue item
review_type | *string* | Status of the review queue item
tags  | *object* | Key value pair for annotating custom meta data
updated_at | *string* | Timestamp of when the review queue was updated
