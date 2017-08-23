> Example Response:

```json
{{create_authorization_scenario_response}}
```

`Authorizations` have two possible states SUCCEEDED and FAILED. If the `Authorization`
 has succeeded, it must be captured before the `expires_at` or the funds will
 be released.

 You'll notice the response has a field named `idempotency_id`, its purpose is to ensure the API request only be performed once. Why is this important? We've all experienced a hanging request while on a checkout page, fearing that if we refresh or submit the payment again, we'll be charged twice.  With {{api_name}}, we remove the ambiguity by having the user generate a unique  `idempotency_id` and sending it with the normal payload. If the user attempts a request with the same `idempotency_id`, the response will raise an exception. Now you can rest assured that when you create an authorization or debit a bank account that the user will be protected from potential network issues by simply passing `idempotency_id` in body of the request.

<aside class="warning">
Authorizations on debit cards actually place a hold on funds in the cardholder's
bank account and may lead to lower than expected balances and/or insufficient
funds issues.
</aside>


<aside class="notice">
If the transfer field of an Authorization is null it has not yet been captured.
</aside>


#### HTTP Request

`POST {{staging_base_url}}/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The `Payment Instrument` that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
idempotency_id | *string*, **optional** | A randomly generated value that you want associated with the request
