> Example Response:

```json
{{fetch_merchant_profile_scenario_response}}
```

Make a GET request with your `Merchant`'s ID. You'll want to keep the `merchant_profile` located in the links section of the response for the following step.

#### HTTP Request

`GET {{staging_base_url}}/merchants/:MERCHANT_ID`

#### URL Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant`
