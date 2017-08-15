> Example Response:

```json
{{associate_dummyV1_payment_processor_scenario_response}}
```

Enables the DUMMY_V1 acquiring processor for an `Application` to provision
 `Merchant` accounts, process `Transfers` and issue `Settlements`.

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can enable a processor for an Application.
</aside>

<aside class="warning">
The DUMMY_V1 processor should not be provisioned on production level Applications.
To enable this processor please use the request body exactly as demonstrated in
the example to the right.
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
