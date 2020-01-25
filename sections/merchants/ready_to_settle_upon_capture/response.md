> Example Response:

```json
{{fetch_merchant_settle_upon_scenario_response}}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can make this API call.
</aside>

Update a Merchant's ability to immediately allow its Transfer's to be marked ready to settle and be included in a Settlement. In this model, you can ignore the restriction of the processor confirming that funds have settled and payout merchants on an independent schedule.

#### HTTP Request

`PUT {{staging_base_url}}/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
ready_to_settle_upon | *string*, **required** |Pass `SUCCESSFUL_CAPTURE` in order to update Merchant's ability to have it's Transfers marked ready to settle immediately. To revert, pass `RECONCILIATION`.
