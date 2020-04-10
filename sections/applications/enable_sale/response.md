> Example Response:

```json
{{enable_sale_scenario_response}}
```

There are two variations:

* Batch sale: We use the processor's batch sale API.
* Online sale: We use the processor's real-time sale API.

As a part of the `application_config`, set the type of transfers you want to enable:

To use online sale: `"card_sale_submission_method" : "real_time"`

To use batch sale: `"card_sale_submission_method" : "batch"`

The default value for card_sale_submission_method is real_time.

<aside class="notice">
Only ROLE_PLATFORM Users can make this update.
</aside>


#### HTTP Request

`PUT {{staging_base_url}}/applications/:APPLICATION_ID/processors/:PROCESSOR_NAME`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
card_sale_submission_method | *string*, **required** | For online sale, pass `"real_time"`. For batch sale, pass `"batch"`.
