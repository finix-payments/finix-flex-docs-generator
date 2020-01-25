#### HTTP Request

`POST {{staging_base_url}}/merchants/:MERCHANT_ID/devices`


#### URL Parameters

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of Device


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
model | *string*, **required** | Please select one of the following values which will let Finix know the type of device being used: MX915
name | *string*, **required** | Name of device
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
description | *string*, **optional** |  Additional information about device (e.g. self serving terminal)

#### Configuration Arguments
Field | Type | Description
----- | ---- | -----------
allow_debit | *boolean*, **optional** |  Sets whether device will allow debit by default or not (defaults to true)  
prompt_signature | *string*, **optional** |  Sets whether device will prompt the card holder for a signature by default or not, AMOUNT is used in conjuction with signature_threshold_amount so that when the threshold is reached the signature form appears on device screen (defaults to always). Options are: ALWAYS, NEVER, AMOUNT  
check_for_duplicate_transactions | *boolean*, **optional** |  Sets whether the device will check for duplicate transactions  
prompt_amount_confirmation | *boolean*, **optional** |  Sets whether or not to make card holder confirm the amount they will pay (defaults is true)  
signature_threshold_amount | *integer*, **optional** |  Threshold set for when to prompt a signature prompt_signature is set to AMOUNT (defaults to 0)  
prompt_manual_entry | *boolean*, **optional** |  Sets whether or not the default card input method will be keyed in manual entry or not (defaults to false)  




```
{
  "id" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "merchant" : "MUu56ZGx3Xb6U9gAqKfgNisd",
  "name" : "Finix  triPOS #1",
  "model" : "MX915",
  "description" : "Mike Jones",
  "serial_number" : null,
  "idle_message" : null,
  "enabled" : false,
  "device_config_details" : {
    "allow_debit" : true,
    "check_for_duplicate_transactions" : true,
    "prompt_amount_confirmation" : true,
    "prompt_manual_entry" : false,
    "prompt_signature" : "NEVER",
    "signature_threshold_amount" : 0
  },
  "created_at" : "2019-03-01T01:07:17.015",
  "updated_at" : "2019-03-01T01:07:17.022",
  "_links" : {
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf"
    },
    "activations" : {
      "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf/activations"
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
