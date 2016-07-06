
> Example Response:

```json
{{provision_merchant_scenario_response}}
```

Now that we've associated a `Payment Instrument` with our seller's `Identity` we're ready to provision a `Merchant` account. This is the last step before you can begin processing on their behalf. Luckily you've already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource. Take a second to inspect this newly created resource, particularly the `underwriting_state`, which can have 3 potential states:

1. `PROVISIONING`: Request is pending (state will typically change after two minutes)

2. `APPROVED`: Merchant has been approved and can begin processing

3. `REJECTED`: Merchant was rejected by the processor either because the collected underwriting information was invalid or it failed one a number of regulatory and compliance checks (e.g. KYC, OFAC or MATCH)

<aside class="notice">
Provisioning a `Merchant` account is an asynchronous request. We recommend creating a Webhook to listen for the state change.
</aside>


#### HTTP Request

`POST {{base_url}}/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity
