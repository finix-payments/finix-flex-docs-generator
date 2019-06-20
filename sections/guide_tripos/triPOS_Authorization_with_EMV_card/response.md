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

#### Configuration Arguments

allow_debit | *boolean*, **optional** |  Sets whether device will allow debit by default or not (defaults to true)
prompt_signature | *string*, **optional** |  Sets whether device will prompt the card holder for a signature by default or not, AMOUNT is used in conjuction with signature_threshold_amount so that when the threshold is reached the signature form appears on device screen (defaults to always). Options are: ALWAYS, NEVER, AMOUNT
check_for_duplicate_transactions | *boolean*, **optional** |  Sets whether the device will check for duplicate transactions
signature_threshold_amount | *integer*, **optional** |  Threshold set for when to prompt a signature if device_configuration#prompt_signature is set to AMOUNT (defaults to 0)
prompt_manual_entry | *boolean*, **optional** |  Sets whether or not the default card input method will be keyed in manual entry or not (defaults to false)


```
{
  "id" : "TReEok8811pDqsR1BbxZLbw1",
  "amount" : 150,
  "tags" : {
    "order_number" : "chris123transfer"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "FNXmEM7d6ns8LMMzt61AD8TrR",
  "currency" : "USD",
  "application" : "APeUbTUjvYb1CdPXvNcwW1wP",
  "source" : "PIcW77CfRyBUWJhA231TWXWf",
  "destination" : null,
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "card_present_details" : {
    "emv_data" : {
      "application_identifier" : "A0000000031010",
      "application_label" : "Visa Credit",
      "application_preferred_name" : null,
      "application_transaction_counter" : "004F",
      "cryptogram" : "TC F8C706E8A0368D15",
      "issuer_code_table_index" : null,
      "pin_verified" : false
    },
    "masked_account_number" : "************7564",
    "name" : "AARON/CHRISTOPHER W ",
    "brand" : "VISA",
    "entry_mode" : "CHIP_ENTRY",
    "payment_type" : "CREDIT",
    "approval_code" : "000036"
  },
  "created_at" : "2019-03-11T23:36:42.03Z",
  "updated_at" : "2019-03-11T23:36:57.09Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDsbTBawhnLBAVeinRb84vFR",
  "device" : "DVf2H8sh4LZZC52GTUrwCPPf",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://finix.sandbox-payments-api.com/applications/APeUbTUjvYb1CdPXvNcwW1wP"
    },
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TReEok8811pDqsR1BbxZLbw1"
    },
    "payment_instruments" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TReEok8811pDqsR1BbxZLbw1/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://finix.sandbox-payments-api.com/identities/IDsbTBawhnLBAVeinRb84vFR"
    },
    "device" : {
      "href" : "https://finix.sandbox-payments-api.com/devices/DVf2H8sh4LZZC52GTUrwCPPf"
    },
    "reversals" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TReEok8811pDqsR1BbxZLbw1/reversals"
    },
    "fees" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TReEok8811pDqsR1BbxZLbw1/fees"
    },
    "disputes" : {
      "href" : "https://finix.sandbox-payments-api.com/transfers/TReEok8811pDqsR1BbxZLbw1/disputes"
    },
    "source" : {
      "href" : "https://finix.sandbox-payments-api.com/payment_instruments/PIcW77CfRyBUWJhA231TWXWf"
    }
  }
```
