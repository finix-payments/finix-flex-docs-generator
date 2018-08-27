### Android SDK

#### Step 1: Installation

In the root module, make sure `jcenter()` is listed inside the repositories section. In the module, add this line to its `build.gradle` inside the dependencies section.

```
implementation 'com.payment.android:sdk:1.4'
```

#### Step 2: Instantiate Instrument Class

Create an `Instrument` and pass it the card number, expiration year, and expiration month.

```
 Instrument instrument = new Instrument(cardNumber, paymentType, expirationYear, expirationMonth);  
```

```
 Instrument instrument = new Instrument("4111111111111111", "PAYMENT_CARD", "2022", "12");  
```


##### Arguments
Field | Type | Description
----- | ---- | -----------
cardNumber | *string*, **required** | Payment card account number
paymentType | *string*, **required** | Use "Payment_CARD"
expirationYear | *integer*, **required** | 4-digit expiration year
expirationMonth | *integer*, **required** | Expiration month (e.g. 12 for December)


#### Step 3: Instantiate PaymentsSDK Class

Next, create a `PaymentsSDK` object and pass it either a sandbox or a live endpoint. In the second argument you will need to pass the Application ID.

```
PaymentsSDK paymentsSDK = new PaymentsSDK(apiEndpoint, applicationId);;  
```

```
PaymentsSDK paymentsSDK = new PaymentsSDK({{staging_base_url}}, {{fetch_application_scenario_id}});;  
```



##### Arguments
Field | Type | Description
----- | ---- | -----------
apiEndpoint | *string*, **required** | Sandbox or Live API endpoint (e.g. {{staging_base_url}} for Sandbox)
applicationId | *string*, **required** | ID of `Application`



#### Step 4: Tokenize Payment Card
Lastly, you will tokenize the payment card from that you received from step two by passing it to the `Tokenize` function.

```
Token token = paymentsSDK.Tokenize(instrument);

```
