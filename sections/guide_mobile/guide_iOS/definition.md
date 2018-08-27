### iOS SDK

#### Step 1: Import Payments SDK

Import the Payments SDK with with CocoaPods by adding pod `'PaymentsSDK', '~> 1.0.4'` to the Podfile

#### Step 2: Import Library

Import PaymentsSDK by running ` import PaymentsSDK`

```
 import PaymentsSDK
```


#### Step 3: Initialize Tokenizer Class

First, initiate `Tokenizer` class and pass it a sandbox or live endpoint. In addition to the endpoint, you need to pass the Application ID to the `Tokenizer` function.

```
let tokenizer = Tokenizer(
  host: apiEndpoint,
  applicationId: applicationId)
```

```
let tokenizer = Tokenizer(
  host: {{staging_base_url}},
  applicationId: {{fetch_application_scenario_id}})
```

##### Arguments
Field | Type | Description
----- | ---- | -----------
apiEndpoint | *string*, **required** | Sandbox or Live API endpoint (e.g. {{staging_base_url}} for Sandbox)
applicationId | *string*, **required** | ID of `Application`



#### Step 4: Tokenize Payment Card
Lastly, pass the card number, payment type, expiration month and year to the `createToken` function.

```
tokenizer.createToken(
  cardNumber: cardNumber,
  paymentType: paymentType,
  expirationMonth: expirationMonth,
  expirationYear: expirationYear) { (token, error) in
       guard let token = token else {
           print(error!.localizedDescription)
           return
       }
       print(token.id)
       print(token.fingerprint)
}   
```

```
tokenizer.createToken(
  cardNumber: "4111111111111111",
  paymentType: "PAYMENT_CARD",
  expirationMonth: 12,
  expirationYear: 2021) { (token, error) in
       guard let token = token else {
           print(error!.localizedDescription)
           return
       }
       print(token.id)
       print(token.fingerprint)
}   
```


##### Arguments
Field | Type | Description
----- | ---- | -----------
cardNumber | *string*, **required** | Payment card account number
paymentType | *string*, **required** | Use "Payment_CARD"
expirationYear | *integer*, **required** | 4-digit expiration year
expirationMonth | *integer*, **required** | Expiration month (e.g. 12 for December)
