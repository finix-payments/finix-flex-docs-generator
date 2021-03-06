> Example Response:

```json
{{approve_settlement_via_review_queue_response}}
```
In order to successfully fund a merchant from a `Settlement`, you need to approve the settlement. `Settlement` approvals occur using the `Review Queue`. This call can approve a `Settlement(s)` in the `Review Queue`. The outcome is noted as `APPROVED` in the response.  

#### HTTP Request

`POST {{staging_base_url}}/review_queue/:REVIEW_QUEUE_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:REVIEW_QUEUE_ID | ID of the `Review Queue`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
outcome | *string*, **required** | Pass in ACCEPTED to approve the `Review Queue`
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


#### Response

Field | Type | Description
----- | ---- | -----------
id | *string*    | `Review Queue` ID
tags  | *objects* | Key value pair for annotating custom meta data
review_type | *string* | Status of the `Review Queue` item
entity_type | *string* | Type of `Review Queue` item
outcome | *string* | Status of the `Settlement`
application | *string* | `Application` ID
reviewed_by | *string* | User ID of the person who is approving or rejecting the `Review Queue` item
entity_id | *string* | Entity ID. This ID can refer to belong to any entity type
processor_type | *string* | `Processor` type
created_at | *string* | Timestamp of when the `Review Queue` was created
updated_at | *string* | Timestamp of when the `Review Queue` was updated
completed_at | *string* | Timestamp of when the `Review Queue` was updated to its final state
