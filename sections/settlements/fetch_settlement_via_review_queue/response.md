> Example Response:

```json
{{fetch_settlement_via_review_queue_response}}
```

This call allows you to view all `Pending` `Settlements` in the `Review Queue`.

#### HTTP Request

`GET {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&outcome=PENDING`

#### URL Parameters

Parameter | Description
----- | -----------------------
:ENTITY_TYPE | Refers to the type of `Review Queue` item. The entity_types available are: IDENTITY, MERCHANT, SETTLEMENT.
:OUTCOME | Refers to the status of the `Settlement`. The outcome types available are: PENDING, APPROVED and REJECTED. PENDING means no action has been taken. APPROVED means the settlement has been approved. REJECTED means the settlement has been rejected



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
