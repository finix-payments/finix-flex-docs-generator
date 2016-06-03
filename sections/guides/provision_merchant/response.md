> Example Response:

```json
{{underwrite_identity_scenario_response}}
```

Once the Identity has been verified, {{api_name}} will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.
