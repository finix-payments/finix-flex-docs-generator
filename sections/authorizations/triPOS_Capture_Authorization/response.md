#### HTTP Request

`PUT {{staging_base_url}}/authorizations/:AUTHORIZATION_ID`


#### URL Parameters
Field | Type | Description
----- | ---- | -----------
AUTHORIZATION_ID | *string*, **required** | ID of Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the  `Authorization`  you would like to capture in cents.


```
{
  "id" : "AUuCfRve8QG6G1wnPCReiLma",
  "application" : "APeUbTUjvYb1CdPXvNcwW1wP",
  "amount" : 150,
  "tags" : {
    "order_number" : "chris123transfer"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRjiUo5CXLmaJp4k9PL7iP8z",
  "messages" : [ ],
  "raw" : null,
  "card_present_details" : null,
  "created_at" : "2019-03-01T03:42:13.59Z",
  "updated_at" : "2019-03-01T03:49:28.67Z",
  "trace_id" : "957ce193-b4e4-4a39-88e2-d88a019982d2",
  "source" : "PIjnHHLBZvRu6GPEZdFt7E2q",
  "merchant_identity" : "IDsbTBawhnLBAVeinRb84vFR",
  "device" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "is_void" : false,
  "expires_at" : "2019-03-08T03:42:13.59Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/authorizations/AUuCfRve8QG6G1wnPCReiLma"
    },
    "application" : {
      "href" : "https://finix.sandbox-payments-api.com/applications/APeUbTUjvYb1CdPXvNcwW1wP"
    },
    "transfer" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRjiUo5CXLmaJp4k9PL7iP8z"
    },
    "device" : {
      "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf"
    },
    "merchant_identity" : {
      "href" : "https://finix.sandbox-payments-api.com/identities/IDsbTBawhnLBAVeinRb84vFR"
    }
  }
}
```
