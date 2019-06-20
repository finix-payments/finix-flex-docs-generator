#### HTTP Request

`POST {{staging_base_url}}/transfers`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
device | *string*, **required** | The ID of the activated device
amount | *integer*, **required** | Amount of sale
currency | *string*, **required** | Currency of sale
operation_key | *string*, **required** | Describes the operation to be performed in the transaction
device_configuration#allow_debit | *boolean*, **optional** |  Sets whether device will allow debit by default or not (defaults to true)
device_configuration#prompt_signature | *string*, **optional** |  Sets whether device will prompt the card holder for a signature by default or not, AMOUNT is used in conjuction with device_configuration#signature_threshold_amount so that when the threshold is reached the signature form appears on device screen (defaults to always). Options are: ALWAYS, NEVER, AMOUNT
device_configuration#check_for_duplicate_transactions | *boolean*, **optional** |  Sets whether the device will check for duplicate transactions
device_configuration#signature_threshold_amount | *integer*, **optional** |  Threshold set for when to prompt a signature if device_configuration#prompt_signature is set to AMOUNT (defaults to 0)
device_configuration#prompt_manual_entry | *boolean*, **optional** |  Sets whether or not the default card input method will be keyed in manual entry or not (defaults to false)


```
{
  "id" : "TRgRGp55tsSiFPr6ZxQoMAWd",
  "amount" : 150,
  "tags" : {
    "order_number" : "chris123transfer"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "1e04d599-797a-4526-adf0-aa1130865042",
  "currency" : "USD",
  "application" : "APeUbTUjvYb1CdPXvNcwW1wP",
  "source" : "PIpuTNXGFiMn69bAV4ApzeYX",
  "destination" : null,
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "card_present_details" : {
    "emv_data" : null,
    "masked_account_number" : "************0011",
    "name" : "TEST/WORLDPAY",
    "brand" : "UNKNOWN",
    "entry_mode" : "SWIPED",
    "payment_type" : "CREDIT",
    "approval_code" : "000004"
  },
  "created_at" : "2019-03-01T03:04:18.25Z",
  "updated_at" : "2019-03-01T03:04:33.09Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDsbTBawhnLBAVeinRb84vFR",
  "device" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://finix.sandbox-payments-api.com/applications/APeUbTUjvYb1CdPXvNcwW1wP"
    },
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRgRGp55tsSiFPr6ZxQoMAWd"
    },
    "payment_instruments" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRgRGp55tsSiFPr6ZxQoMAWd/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://finix.sandbox-payments-api.com/identities/IDsbTBawhnLBAVeinRb84vFR"
    },
    "device" : {
      "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf"
    },
    "reversals" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRgRGp55tsSiFPr6ZxQoMAWd/reversals"
    },
    "fees" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRgRGp55tsSiFPr6ZxQoMAWd/fees"
    },
    "disputes" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TRgRGp55tsSiFPr6ZxQoMAWd/disputes"
    },
    "source" : {
      "href" : "https://finix.sandbox-payments-api.com/payment_instruments/PIpuTNXGFiMn69bAV4ApzeYX"
    }
  }
}
```
