## iOS Integration

### Step 1: Import Payments SDK

Import the Payments SDK with with CocoaPods by adding pod `'PaymentsSDK', '~> 1.0.4'` to the Podfile

### Step 2: Import Library

```
 import PaymentsSDK
```


### Step 3: Initialize Tokenizer Class

```
let tokenizer = Tokenizer(
  host: apiEndpoint,
  applicationId: applicationId)
```

```javascript
let tokenizer = Tokenizer(
  host: {{staging_base_url}},
  applicationId: {{fetch_application_scenario_id}})
```

#### Arguments
Field | Type | Description
----- | ---- | -----------
apiEndpoint | *string*, **required** | Sandbox or Production API endpoint (e.g. {{staging_base_url}} for Sandbox)
applicationId | *string*, **required** | ID of `Application`



### Step 4: Tokenize Payment Card


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

```javascript
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


#### Arguments

#### Arguments
Field | Type | Description
----- | ---- | -----------
cardNumber | *string*, **required** | Payment card account number
paymentType | *string*, **required** | Use "Payment_CARD"
expirationYear | *integer*, **required** | 4-digit expiration year
expirationMonth | *integer*, **required** | Expiration month (e.g. 12 for December)
