## Android Integration

### Step 1: Installation
Gradle

In the root module, make sure `jcenter()` is listed inside the repositories section In the module making use of the SDK, add this line to its `build.gradle` inside the dependencies section:

```
implementation 'com.finixpayments.android:sdk:1.0'
```

### Step 2: Configure the SDK

Using the SDK is as simple as creating an Instrument with credit card details, creating a PaymentsSDK object with an environment and Application ID, and calling a static method to tokenize the Instrument. You can choose to use either a staging or production environment for the API call. below is an example:


### Step 3: Instantiate Instrument Class

```
 Instrument instrument = new Instrument(cardNumber, paymentType, expirationYear, expirationMonth);  
```

```javascript
 Instrument instrument = new Instrument("4111111111111111", "PAYMENT_CARD", "2022", "12");  
```


#### Arguments
Field | Type | Description
----- | ---- | -----------
cardNumber | *string*, **required** | Payment card account number
paymentType | *string*, **required** | Use "Payment_CARD"
expirationYear | *integer*, **required** | 4-digit expiration year
expirationMonth | *integer*, **required** | Expiration month (e.g. 12 for December)


### Step 4: Instantiate PaymentsSDK Class

```
PaymentsSDK paymentsSDK = new PaymentsSDK(apiEndpoint, applicationId);;  
```

```javascript
PaymentsSDK paymentsSDK = new PaymentsSDK({{staging_base_url}}, {{fetch_application_scenario_id}});;  
```



#### Arguments
Field | Type | Description
----- | ---- | -----------
apiEndpoint | *string*, **required** | Sandbox or Production API endpoint (e.g. {{staging_base_url}} for Sandbox)
applicationId | *string*, **required** | ID of `Application`



### Step 5: Tokenize Payment Card


```
Token token = paymentsSDK.Tokenize(instrument);

```
