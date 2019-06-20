#### HTTP Request

`POST {{staging_base_url}}/authorizations`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
device | *string*, **required** | The ID of the activated device
amount | *integer*, **required** | Amount of sale
currency | *string*, **required** | Currency of sale
operation_key | *string*, **required** | Describes the operation to be performed in the transaction
device_configuration#prompt_signature | *string*, **optional** |  Sets whether device will prompt the card holder for a signature by default or not, AMOUNT is used in conjuction with device_configuration#signature_threshold_amount so that when the threshold is reached the signature form appears on device screen (defaults to always). Options are: ALWAYS, NEVER, AMOUNT
device_configuration#signature_threshold_amount | *integer*, **optional** |  Threshold set for when to prompt a signature if device_configuration#prompt_signature is set to AMOUNT (defaults to 0)
device_configuration#prompt_manual_entry | *boolean*, **optional** |  Sets whether or not the default card input method will be keyed in manual entry or not (defaults to false)


```
{
  "id" : "AUiJS1VhMy8zpACLoacPFG7m",
  "application" : "APeUbTUjvYb1CdPXvNcwW1wP",
  "amount" : 150,
  "tags" : {
    "order_number" : "chris123transfer"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "card_present_details" : {
    "emv_data" : null,
    "masked_account_number" : "************0011",
    "name" : "TEST/WORLDPAY",
    "brand" : "UNKNOWN",
    "entry_mode" : "SWIPED",
    "payment_type" : "CREDIT",
    "approval_code" : "000037"
  },
  "created_at" : "2019-03-01T03:37:10.10Z",
  "updated_at" : "2019-03-01T03:37:23.63Z",
  "trace_id" : "556185b9-ceaa-490b-bae2-a662757b42e0",
  "source" : "PIaqFoGabsBTTowVr5z7jiLv",
  "merchant_identity" : "IDsbTBawhnLBAVeinRb84vFR",
  "device" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "is_void" : false,
  "expires_at" : "2019-03-08T03:37:10.10Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/authorizations/AUiJS1VhMy8zpACLoacPFG7m"
    },
    "application" : {
      "href" : "https://finix.sandbox-payments-api.com/applications/APeUbTUjvYb1CdPXvNcwW1wP"
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
