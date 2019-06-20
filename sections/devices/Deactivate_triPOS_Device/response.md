#### HTTP Request

`PUT {{staging_base_url}}/devices/:DEVICE_ID`


#### URL Parameters

Field | Type | Description
----- | ---- | -----------
DEVICE_ID | *string*, **required** | ID of Device


#### Request Arguments

  Field | Type | Description
  ----- | ---- | -----------
  action | *string*, **required** | The action parameter must include DEACTIVATE to deactivate the device


  ```
    {
      "id" : "DVf2H8sh4LZZC52GTUrwCPPf",
      "merchant" : "MUu56ZGx3Xb6U9gAqKfgNisd",
      "name" : "Finix Tripos #1",
      "model" : "MX915",
      "description" : "Mike Jones",
      "serial_number" : null,
      "idle_message" : null,
      "enabled" : false,
      "tags" : { },
      "created_at" : "2019-03-01T02:27:20.366",
      "updated_at" : "2019-03-11T23:30:05.816",
      "configuration_details" : null,
      "_links" : {
        "self" : {
          "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf"
        },
        "merchant" : {
          "href" : "https://finix.sandbox-payments-api.com/merchants/MUu56ZGx3Xb6U9gAqKfgNisd"
        },
        "transfers" : {
          "href" : "https://finix.sandbox-payments-api.com/transfers"
        },
        "authorizations" : {
          "href" : "https://finix.sandbox-payments-api.com/authorizations"
        }
      }
    }
  ```
