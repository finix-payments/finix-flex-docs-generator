> Example Response:

```json
{{associate_dummyV1_payment_processor_scenario_response}}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The {{api_name}} Payment Platform is processor agnostic allowing for processing transactions
across multiple processors. Once a processor is enabled, the `Application` can begin
provisioning merchant accounts.

In this example we'll be enabling the DUMMY_V1 processor, which is utilized for
sandbox testing.

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can enable a processor for an Application.
</aside>

<aside class="warning">
The DUMMY_V1 processor should not be provisioned on live level Applications.
</aside>


#### HTTP Request

`POST {{staging_base_url}}/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
canDebitBankAccount | *boolean*, **optional** | Allows a payment instrument of type `BANK_ACCOUNT` which is associated with the processor to be debited (i.e. eCheck)
