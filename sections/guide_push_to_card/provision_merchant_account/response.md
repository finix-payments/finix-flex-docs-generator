> Example Response:

```json
{{provision_push_merchant_scenario_response}}
```

Now that we've associated a Payment Instrument with our recipient’s `Identity` we’re ready to provision a Recipient account. This is the last step before you can begin paying out an Identity. Luckily you’ve already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource.

#### HTTP Request

`POST {{staging_base_url}}/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor

