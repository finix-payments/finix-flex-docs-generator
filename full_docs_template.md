---
title: {{api_name}} API Reference

language_tabs:
  - shell: cURL
  - php: PHP
  - java: JAVA

includes:
  - errors

search: true
---

# Guides


## Getting Started
```shell


# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u {{basic_auth_username}}:{{basic_auth_password}}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();


```
```java

```
This guide will demonstrate the main workflows for utilizing the {{api_name}} Payments API for platforms and marketplaces. We have language bindings in cURL, PHP, Ruby, Python, C#, Java and Perl! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

To communicate with the {{api_name}} API you'll need to authenticate your requests with a username and password. For the sandbox environment you may use the credentials listed below or you can supply your own.

- Username: `{{basic_auth_username}}`

- Password: `{{basic_auth_password}}`

You should also know your Application ID. An Application, also referred as an "App", is a resource that represents your web App or any service that connects customers (i.e. buyers) and merchants (i.e. sellers). For the sandbox environment you may use the following ID:

- App ID: `{{create_app_scenario_id}}`


## Create an Identity for a Merchant

```shell


curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_merchant_identity_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_merchant_identity_scenario_php_request}}
);
$identity = $identity->save();

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .businessName("business inc")
        .businessType(BusinessType.LIMITED_LIABILITY_COMPANY)
        .doingBusinessAs("doingBusinessAs")
        .phone("1234567890")
        .businessPhone("+1 (408) 756-4497")
        .taxId("123456789")
        .businessTaxId("123456789")
        .personalAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .businessAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .dob(DateOfBirth.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .build()
    )
    .build()
);

```

> Example Response:

```json
{{create_merchant_identity_scenario_response}}
```

Before we can charge a card we need to create an Identity resource. An Identity represents a person or business. In this case, the Identity will represent the merchant (i.e. seller). Let's create one now.You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Create a New Bank Account
```shell

curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{create_bank_account_scenario_curl_request}}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument({{create_bank_account_scenario_php_request}});
$bank_account = $bank_account->save();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name("Joe-Doe")
      .identity("IDaAUrraYjDT4i2w1C2VGBpY")
      .accountNumber("84012312415")
      .bankCode("840123124")
      .accountType(BankAccountType.SAVINGS)
      .companyName("company name")
      .country("USA")
      .currency("USD")
      .build()
);

```
> Example Response:

```json
{{create_bank_account_scenario_response}}
```
<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST {{base_url}}/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | {{create_identity_scenario_id}}
account_type | *string*, **required** | Checking or Savings | SAVINGS
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | BANK_ACCOUNT
currency | *string*, **optional** | Default currency used when settling funds. | USD
first_name | *string*, **optional** | Customer's first name on bank account. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
country | *string*, **optional** | Country of the associated bank account. | USA
bic | *string*, **optional** | TBD. | foo
iban | *string*, **optional** | International Bank Account integer | foo
company_name | *string*, **optional** | Name of company if the bank account is a company account. |  Bob's Burgers


## Perform an Identity Verification
```shell


curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_identity_verification_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{underwrite_identity_scenario_php_request}});
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);

```

> Example Response:

```json
{{create_identity_verification_scenario_response}}
```

Before, being able to process funds to this seller we will need to perform an identity verification to underwrite them as a Merchant. Only underwritten Identities can be paid out per KYC regulations.


## Provision Merchant Account
```shell

curl {{base_url}}/identities/{{create_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{underwrite_identity_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{underwrite_identity_scenario_php_request}});
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());

```
> Example Response:

```json
{{underwrite_identity_scenario_response}}
```

Once the Identity has been verified, {{api_name}} will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.

## Create an Identity for a Buyer (i.e. buyer)
```shell


curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_buyer_identity_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_buyer_identity_scenario_php_request}}
);
$identity = $identity->save();

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .build()
    )
    .build()
);

```
> Example Response:

```json
{{create_buyer_identity_scenario_response}}
```
This next step should sound familiar. Let's create an Identity to represent the buyer. You'll want to store the ID of the newly created Identity resource as you'll reference it later.


## Create a Payment Instrument (i.e. card)
```shell


curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_card_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{create_card_scenario_php_request}});
$card = $card->save();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe-Doe")
    .identity("ID572pSyFj71oVExp6XWiGRP")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{{create_card_scenario_response}}
```

Now that we have an Identity resource representing our buyer, we'll need to create a Payment Instrument which can represent either a card or bank account. In this instance we'll create a card with the request to the right (note you'll need to interpolate your own buyer's Identity from the previous request).

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

Be sure to store the ID of your newly tokenized Payment Instrument.


## Create a Transfer (i.e. debit the card)
```shell


curl {{base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_debit_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Transfer;

$debit = new Transfer({{create_debit_scenario_php_request}});
$debit = $debit->save();
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);

```

> Example Response:

```json
{{create_debit_scenario_response}}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.


## Reverse the Transfer (i.e. issue a refund)
```shell

curl {{base_url}}/transfers/{{create_debit_scenario_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d  '{{create_refund_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```

> Example Response:

```json
{{create_refund_scenario_response}}
```

What if we need to issue a refund to the buyer? First, you'll need to take the previously stored Transfer ID and interpolate it into the following url path. The amount can be equal to or less than the original debit.

## Settle out funds to a Merchant
```shell

curl {{base_url}}/identities/{{create_identity_scenario_id}}/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_settlement_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = $identity->createSettlement({{create_settlement_scenario_php_request}});

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{{create_settlement_scenario_response}}
```

Awesome! Now you know how to charge a card and reverse the debit.

Now you need to settle out the funds to your merchant. To do so you will create a Settlement resource. Each settlement is comprised of all the Transfers that have a SUCCEEDED state and that have not been previously settled out.
# Tokenization.js
To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js, keeps you out of the PCI scope by sending sensitive payment information over SSL directly to the {{api_name}} servers.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example]({{jsfiddle}}).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the {{api_name}} API.
</aside>


## Step 1: Include library
To use tokenization.js you will first need to include the library. Please include the script tag as demonstrated to the right.

html
<script type="text/javascript" src="https://js.verygoodproxy.com/tokenization.1-latest.js"></script>


<aside class="notice">
Note that we do not recommend hosting the tokenization.js library locally as doing so prevents important updates.
</aside>

## Step 2: Create a form
html
<!--This is an example for for Cards-->
<form role="form" class="form-horizontal">
  <div class="form-group">
    <label class="col-lg-5 control-label">Card Number</label>
    <div class="col-lg-5">
      <input type="text" id="cc-number" class="form-control" autocomplete="off" placeholder="4111111111111111" maxlength="16" />
    </div>
  </div>
  <div class="form-group">
    <label class="col-lg-5 control-label">Expiration</label>
    <div class="col-lg-2">
      <input type="text" id="cc-ex-month" class="form-control" autocomplete="off" placeholder="01" maxlength="2" />
    </div>
    <div class="col-lg-2">
      <input type="text" id="cc-ex-year" class="form-control" autocomplete="off" placeholder="2013" maxlength="4" />
    </div>
  </div>
  <div class="form-group">
    <label class="col-lg-5 control-label">Security Code (CVV)</label>
    <div class="col-lg-2">
      <input type="text" id="cc-cvv" class="form-control" autocomplete="off" placeholder="453" maxlength="4" />
    </div>
  </div>
  <a id="cc-submit" class="btn btn-large btn-primary pull-right">Tokenize</a>
</form>

<!--This is an example for for Bank Accounts-->
<form role="form" class="form-horizontal">
  <div class="form-group">
    <label class="col-lg-5 control-label">Account Holder's Name</label>
    <div class="col-lg-6">
      <input type="text" id="ba-name" class="form-control" autocomplete="off" placeholder="John Doe" />
    </div>
  </div>
  <div class="form-group">
    <label class="col-lg-5 control-label">Routing Number</label>
    <div class="col-lg-6">
      <input type="text" id="ba-routing" class="form-control" autocomplete="off" placeholder="322271627" />
    </div>
  </div>
  <div class="form-group">
    <label class="col-lg-5 control-label">Account Number</label>
    <div class="col-lg-6">
      <input type="text" id="ba-number" class="form-control" autocomplete="off" placeholder="8887776665555" />
    </div>
  </div>
  <a id="ba-submit" class="btn btn-large btn-primary pull-right">Tokenize</a>
</form>

Before collecting the sensitive payment information, we will need to construct an HTML form for users to input the data.

We have provided a simple example to the right for capturing Payment Instrument data.

## Step 3: Configure and initialize

javascript
var initTokenization = function() {
  Tokenization.init({
    server: "{{base_url}}",
    applicationId: "{{create_app_scenario_id}}",
    hosted_fields: {
      card: {
        number: {
          selector: "#cc-number"
        },
        expiration_month: {
          selector: "#cc-ex-month"
        },
        expiration_year: {
          selector: "#cc-ex-year"
        },
        security_code: {
          selector: "#cc-cvv"
        }
      },

      bankAccount: {
        account_type: "SAVINGS",
        account_number: {
          selector: "#ba-number"
        },
        bank_code: {
          selector: "#ba-routing"
        },
        full_name: {
          selector: "#ba-name"
        }
      }
    }
  });
};

We will need to configure the client so that it POSTs to the correct endpoint and associates the Payment Instrument to your application. During the initialization we will also use the JQuery selector method to capture the form data.

### Initialization Fields
Field | Type | Description | Example
----- | ---- | ----------- | -------
server | *string*, **required** |  The base url for the {{api_name}} API| {{base_url}}
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | {{create_app_scenario_id}}
hosted_fields | *object*, **required** |  An object containing the payment instrument information collected from your form.  | Johnson

### hosted_fields object for card
Field | Type | Description | Example
----- | ---- | ----------- | -------
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020

### hosted_fields object for bankAccount
Field | Type | Description | Example
----- | ---- | ----------- | -------
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124


## Step 4: Submit payload and handle response

javascript
// Register "Click" event for the Card form
$('#cc-submit').click(function(e) {
    e.preventDefault();

    // Initialize the client to capture form data
    initTokenization();

    // Tokenization.card.create to submit the payload and include a callback to capture the response
    Tokenization.card.create({

      // callback for handling response
      callback: function(errorThrown, response) {

      }
    });
});

// Register "Click" event for the Bank Account form
$('#ba-submit').click(function(e) {
    e.preventDefault();

    // Initialize the client to capture form data
    initTokenization();

    // Tokenization.bankAccount.create to submit the payload and include a callback to capture the response
    Tokenization.bankAccount.create({

      // callback for handling response
      callback: function(errorThrown, response) {

      }
    });
});


> Example Tokenization Response:
javascript
{
    "id": "{{create_token_scenario_id}}",
    "fingerprint": "FPR-1392097976",
    "created_at": "2016-03-07T22:27:01.611",
    "updated_at": "2016-03-07T22:27:01.611",
    "instrument_type": "PAYMENT_CARD"
}


Finally we will need to register a click event that fires when our users submit the form and define a callback for handling the tokenization.js response. We have included an example to the right.

## Step 5: Send token to your back-end server for storing

javascript
callback: function(errorThrown, response) {
    // POST to your back-end server
    jQuery.post("PATH TO YOUR BACK END", {
        uri: response.id
        }, function(r) {
            // Inspect HTTP response
            if (r.status === 201) {
                // Logic if successful response
            } else {
                // Logic if failed response
            }
    });
}


Great now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server. You can expand on the callback that you previously created like so:

## Step 6: Associate to an Identity



curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{associate_token_scenario_curl_request}}"


> Example Response:

json
{{associate_token_scenario_response}}

Before you can use the newly tokenized card or bank account you will need to associate it with an Identity. To do this you must make an authenticated POST request to `{{base_url}}/payment_instruments` like demonstrated to the right.

### HTTP Request

`POST {{base_url}}/payment_instruments`
# Authorizations
An Authorization resource (also known as a card hold) reserves a specific amount on a card to be captured (debited) at a later date, usually within 7 days. When an Authorization is captured it produces a Transfer resource.


## Create a New Authorization
```shell

curl {{base_url}}/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_authorization_scenario_curl_request}}'



```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Authorization;

$authorization = new Authorization({{create_authorization_scenario_php_request}});
$authorization = $authorization->save();

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .processor("DUMMY_V1")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
> Example Response:

```json
{{create_authorization_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/authorizations`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | {{create_card_scenario_id}}
merchant_identity | *string*, **required** | UID. | {{create_identity_scenario_id}}
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}

## Capture an Authorization

```shell

curl {{base_url}}/authorizations/{{fetch_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{capture_authorization_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("{{fetch_authorization_scenario_id}}");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{{capture_authorization_scenario_response}}
```

### HTTP Request

`PUT {{base_url}}/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
capture_amount | *integer*, **required** | The amount of the authorization you would like to capture in cents. Must be less than or equal to the amount of the authorization | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100

## Retrieve an Authorization
```shell

curl {{base_url}}/authorizations/{{fetch_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("{{fetch_authorization_scenario_id}}");

```
> Example Response:

```json
{{fetch_authorization_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


# Disputes
Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl {{base_url}}/disputes/{{fetch_dispute_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Dispute;

$dispute = Dispute::retrieve('{{fetch_dispute_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("{{fetch_dispute_scenario_id}}");

```
> Example Response:

```json
{{fetch_dispute_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/disputes/dispute_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
dispute_id | ID of the Dispute

# Identities
An Identity resource represents a business or person. Payment Instrument resources may be associated to an Identity.

## Create an Identity for a Buyer
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

```shell


curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_buyer_identity_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_buyer_identity_scenario_php_request}}
);
$identity = $identity->save();

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .build()
    )
    .build()
);

```
> Example Response:

```json
{{create_buyer_identity_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
first_name | *string*, **optional** | First name  | Dwayne
last_name | *string*, **optional** | Last name  | Johnson
phone | *string*, **optional** | Phone number | 1408756449
email | *string*, **optional** | Email address | someone@example.com
line1 | *string*, **optional** | Street address | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address |  Apt. 3
city | *string*, **optional** | City | San Mateo
region | *string*, **optional** | State | CA
postal_code | *string*, **optional** | Postal code | 92704
country | *string*, **optional** | Country  | USA
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}

## Create an Identity for a Merchant
```shell


curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_merchant_identity_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_merchant_identity_scenario_php_request}}
);
$identity = $identity->save();

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .businessName("business inc")
        .businessType(BusinessType.LIMITED_LIABILITY_COMPANY)
        .doingBusinessAs("doingBusinessAs")
        .phone("1234567890")
        .businessPhone("+1 (408) 756-4497")
        .taxId("123456789")
        .businessTaxId("123456789")
        .personalAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .businessAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .dob(DateOfBirth.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .build()
    )
    .build()
);

```
> Example Response:

```json
{{create_merchant_identity_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
business_name | *string*, **required** | Full legal business name | Business, Inc
doing_business_as | *string*, **required** | Business name used if different from its legal name | Bob's Burgers
business_type | *string*, **required** | Type of business | INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, LIMITED_PARTNERSHIP, GENERAL_PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit SSN if business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP or EIN for all other business types | 123456789
business_phone | *string*, **required** | Phone number of the business | 0123456789
first_name | *string*, **required** | First name of the representative of the business | Dwayne
last_name | *string*, **required** | Last name of the representative of the business | Johnson
tax_id | *string*, **required** | Nine digit Social Security Number for the company representative | 123456789
phone | *string*, **required** | Company representative's phone number (Note: There's a separate field for the business phone integer) | 1408756449
email | *string*, **required** | Email address where support requests will be sent | someone@example.com
line1 | *string*, **required** | Street address | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address |  Apt. 3
city | *string*, **required** | City | San Mateo
region | *string*, **required** | State | CA
postal_code | *string*, **required** | Postal code | 92704
country | *string*, **required** | Country  | USA
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales in cents expected to be processed under this Merchant | 10000
max_transaction_amount | *integer*, **required** |  Maximum amount in cents that can be transacted on a single transaction | 10000
mcc | *string*, **required** |  MCC code that this merchant will be classified under | 5422
url | *string*, **required** |  Company website | www.mybusiness.com
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}
default_statement_descriptor | *string*, *required** | String displayed on the buyer's bank or card statement. Length must be between 1 and 20 charactesrs. | {'order_number': '123123123'}
principal_percentage_ownership | *integer*, *required** | Percentage of company owned by the principal | 51
incorporation_date  | *object*, **required** | Date company was incorporated. Comprised of day, month, and year. | see below
day | *integer*, **required** | Day field of the incorporation date| 1
month | *integer*, **required** | Month field of the incorporation date | 2
year | *string*, **required** | Year field of the incorporation date | 1988
dob | *object*, **required** | Date of birth of the company reprentative's date of birth. Comprised of day, month, and year. | see below
day | *integer*, **required** | Day field of the company reprentative's date of birth | 1
month | *integer*, **required** | Month field of the company reprentative's date of birth | 2
year | *string*, **required** | Year field of the company reprentative's date of birth | 1988
## Retrieve a Identity
```shell

curl {{base_url}}/identities/{{fetch_identity_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("{{fetch_identity_scenario_id}}");

```
> Example Response:

```json
{{fetch_identity_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/identities/identity_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

## Underwrite an Identity

```shell

curl {{base_url}}/identities/{{create_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{underwrite_identity_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{underwrite_identity_scenario_php_request}});
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());

```

> Example Response:

```json
{{underwrite_identity_scenario_response}}
```

Underwrite a previously created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


### HTTP Request

`POST {{base_url}}/identities/identity_id/merchants`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}

# Identity Verifications
Identities (merchants) to whom you wish to pay out must be underwritten as per KYC regulations. Each attempt at verifying an Identity creates a Verification resource.

## Create an Identity Verification

```shell


curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_identity_verification_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{underwrite_identity_scenario_php_request}});
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);

```
> Example Response:

```json
{{create_identity_verification_scenario_response}}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST {{base_url}}/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "{{identity_verification_processor}}" for now to test the API. | {{payment_processor}}


## Retrieve an Identity Verification
```shell

curl {{base_url}}/verifications/{{fetch_identity_verification_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Verification;

$verification = Verification::retrieve('{{fetch_identity_verification_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = client.verificationsClient().fetch("{{fetch_identity_verification_scenario_id}}");

```

> Example Response:

```json
{{fetch_identity_verification_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/verifications/verification_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
verification_id | ID of the Identity Verification

# Settlements
A Settlement resource represents a collection of Transfers that are to be paid out to a specific Merchant.


## Create a New Settlement
```shell

curl {{base_url}}/identities/{{create_identity_scenario_id}}/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_settlement_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = $identity->createSettlement({{create_settlement_scenario_php_request}});

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)

```


> Example Response:

```json
{{create_settlement_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities/:identity_id/settlements`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}
currency | *integer*, **required** | The currency for the settlement. | USD


## Fetch a Settlement

```shell


curl {{base_url}}/settlements/{{fetch_settlement_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Settlement;

$settlement = Settlement::retrieve('{{fetch_settlement_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("{{fetch_settlement_scenario_id}}");

```
> Example Response:

```json
{{fetch_settlement_scenario_response}}
```

Fetch a previously created Settlement.

### HTTP Request

`POST {{base_url}}/settlements/settlement_id/`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
settlement_id | ID of the Settlment

# Transfers
A Transfer resource represents any omnidirectional flow of funds. Transfers can represent either a debit to a card, a credit to a bank account, or a refund to a card depending on the request. Transfers have a state attribute representing the current state of the transaction. There are three possible status values: PENDING, SUCCEEDED, or FAILED.

## Debit a Card

```shell


curl {{base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_debit_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Transfer;

$debit = new Transfer({{create_debit_scenario_php_request}});
$debit = $debit->save();
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);

```


> Example Response:

```json
{{create_debit_scenario_response}}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST {{base_url}}/transfers`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | {{create_card_scenario_id}}
merchant_identity | *string*, **required** | UID. | {{create_identity_scenario_id}}
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "{{payment_processor}}" for now to test the API. | {{payment_processor}}

## Refund a Debit
```shell

curl {{base_url}}/transfers/{{create_debit_scenario_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d  '{{create_refund_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Transfer;

$debit = Transfer::retrieve('{{create_debit_scenario_id}}');
$refund = $debit->reverse(50);
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```


> Example Response:

```json
{{create_refund_scenario_response}}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

### HTTP Request

`POST {{base_url}}/transfers/transfer_id/reversals`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
refund_amount | *integer*, **required** | The amount of the refund in cents. Must be equal to or less than the amount of the original debit. | 100

## Retrieve a Transfer
```shell

curl {{base_url}}/transfers/{{fetch_transfer_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Transfer;

$transfer = Transfer::retrieve('{{fetch_transfer_scenario_id}}');



```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("{{fetch_transfer_scenario_id}}");

```
> Example Response:

```json
{{fetch_transfer_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/transfers/transfer_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the Transfer


# Webhooks
Webhooks allow you to build or set up integrations which subscribe to certain events on the {{api_name}} API. When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL. Webhooks are particularly useful for updating asynchronous state changes in Transfers or notifications of newly created Disputes.

## Create a New Webhook
```shell

curl {{base_url}}/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_webhook_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{{create_webhook_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/webhooks`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
url | *string*, **required** | The HTTP or HTTPS url the callbacks will be made to | https://examplesite.com


## Retrieve a Webhook

```shell



curl {{base_url}}/webhooks/{{fetch_webhook_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}}


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Webhook;

$webhook = Webhook::retrieve('{{fetch_webhook_scenario_id}}');



```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("{{fetch_webhook_scenario_id}}");

```

> Example Response:

```json
{{fetch_webhook_scenario_response}}
```

### HTTP Request

`GET {{base_url}}/webhooks/webhook_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
webhook_id | ID of the Webhook

# Payment Instruments
A Payment Instrument resource represents either a credit card or bank account. All information is securely vaulted and referenced by an ID. A Payment Instrument may be created multiple times, and each tokenization produces a unique ID. Each ID may only be associated one time and to only one Identity. Once associated, a Payment Instrument may not be disassociated from an Identity.


## Create a New Card
```shell


curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_card_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{create_card_scenario_php_request}});
$card = $card->save();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe-Doe")
    .identity("ID572pSyFj71oVExp6XWiGRP")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{{create_card_scenario_response}}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST {{base_url}}/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
identity | *string*, **required** | Identity resource which the card is associated. | {{create_buyer_identity_scenario_id}}
first_name | *string*, **optional** | Customer's first name on card. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | PAYMENT_CARD
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020
line1 | *string*, **optional** | Street address of the associated card. | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address of the associated card. |  Apt. 3
city | *string*, **optional** | City of the associated card. | San Mateo
region | *string*, **optional** | State of the associated card. | CA
postal_code | *string*, **optional** | Postal of the associated card. | 92704
country | *string*, **optional** | Country of the associated card. | USA
## Create a New Bank Account
```shell

curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_bank_account_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument({{create_bank_account_scenario_php_request}});
$bank_account = $bank_account->save();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name("Joe-Doe")
      .identity("IDaAUrraYjDT4i2w1C2VGBpY")
      .accountNumber("84012312415")
      .bankCode("840123124")
      .accountType(BankAccountType.SAVINGS)
      .companyName("company name")
      .country("USA")
      .currency("USD")
      .build()
);

```
> Example Response:

```json
{{create_bank_account_scenario_response}}
```

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST {{base_url}}/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | {{create_identity_scenario_id}}
account_type | *string*, **required** | Checking or Savings | SAVINGS
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | BANK_ACCOUNT
currency | *string*, **optional** | Default currency used when settling funds. | USD
first_name | *string*, **optional** | Customer's first name on bank account. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
country | *string*, **optional** | Country of the associated bank account. | USA
bic | *string*, **optional** | TBD. | foo
iban | *string*, **optional** | International Bank Account integer | foo
company_name | *string*, **optional** | Name of company if the bank account is a company account. |  Bob's Burgers


## Create an Identity Verification

```shell


curl {{base_url}}/payment_instruments/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('{{fetch_dispute_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

BankAccount bankAccount = client.bankAccountsClient().fetch("{{fetch_dispute_scenario_id}}")

```
> Example Response:

```json
{{create_identity_verification_scenario_response}}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST {{base_url}}/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "{{identity_verification_processor}}" for now to test the API. | {{payment_processor}}


## Create an Identity Verification

```shell


curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{create_identity_verification_scenario_curl_request}}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();


```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
> Example Response:

```json
{{create_identity_verification_scenario_response}}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST {{base_url}}/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "{{identity_verification_processor}}" for now to test the API. | {{payment_processor}}


