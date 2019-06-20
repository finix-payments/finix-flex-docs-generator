#### HTTP Request

`POST {{staging_base_url}}/identities/:IDENTITY_ID/merchants`

#### URL Parameters
Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the `Identity`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | Name of the processor
gateway | *string*, **required** |  Name of the gateway
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


```
{
  "id" : "MUu56ZGx3Xb6U9gAqKfgNisd",
  "application" : "APeUbTUjvYb1CdPXvNcwW1wP",
  "identity" : "IDsbTBawhnLBAVeinRb84vFR",
  "verification" : "VIhjGSJCnvXLzFQZUsUaeHxb",
  "merchant_profile" : "MPgDcdhXsdcJ9MVeJrZRNp79",
  "processor" : "VANTIV_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "creating_transfer_from_report_enabled" : false,
  "tags" : { },
  "created_at" : "2019-03-01T00:49:02.47Z",
  "updated_at" : "2019-03-01T00:49:02.47Z",
  "onboarding_state" : "PROVISIONING",
  "processor_details" : { },
  "_links" : {
    "self" : {
      "href" : "https://finix.sandbox-payments-api.com/merchants/MUu56ZGx3Xb6U9gAqKfgNisd"
    },
    "identity" : {
      "href" : "https://finix.sandbox-payments-api.com/identities/IDsbTBawhnLBAVeinRb84vFR"
    },
    "verifications" : {
      "href" : "https://finix.sandbox-payments-api.com/merchants/MUu56ZGx3Xb6U9gAqKfgNisd/verifications"
    },
    "merchant_profile" : {
      "href" : "https://finix.sandbox-payments-api.com/merchant_profiles/MPgDcdhXsdcJ9MVeJrZRNp79"
    },
    "application" : {
      "href" : "https://finix.sandbox-payments-api.com/applications/APeUbTUjvYb1CdPXvNcwW1wP"
    },
    "verification" : {
      "href" : "https://finix.sandbox-payments-api.com/verifications/VIhjGSJCnvXLzFQZUsUaeHxb"
    }
  }
}
```
