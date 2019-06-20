#### HTTP Request

`PUT {{staging_base_url}}/devices/:DEVICE_ID`

#### URL Parameters

Field | Type | Description
----- | ---- | -----------
DEVICE_ID | *string*, **required** | ID of Device


#### Request Arguments
Field | Type | Description
----- | ---- | -----------
action | *string*, **required** | The action parameter must include REBOOT to reboot the device


```
{
  "id" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "merchant" : "MUu56ZGx3Xb6U9gAqKfgNisd",
  "name" : "Finix Tripos #1",
  "model" : "MX915",
  "description" : "Mike Jones",
  "serial_number" : "262-410-025",
  "idle_message" : null,
  "enabled" : true,
  "tags" : { },
  "created_at" : "2019-03-01T02:27:20.366",
  "updated_at" : "2019-03-11T23:22:39.690",
  "configuration_details" : {
    "allow_debit" : true,
    "check_for_duplicate_transactions" : true,
    "prompt_amount_confirmation" : true,
    "prompt_manual_entry" : false,
    "prompt_signature" : "NEVER",
    "signature_threshold_amount" : 0
  },
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
  ```   
