---
title: {{api_name}} API Reference

language_tabs:
  - shell: cURL
  - php: PHP
  - java: Java

includes:
  - errors

search: true
---

# Guides

## Overview

These guides provide a collection of resources for utilizing the {{api_name}}
API and its client libraries. We offer a number of client libraries for
interfacing with the API, and you can view example code snippets for each in
the dark area to the right.

1. [Authentication](#authentication): A quick guide on how to properly
authenticate and interface with the API.

2. [Getting Started](#getting-started): A step-by-step guide demonstrating the basic workflow
of charing a card. This guide will walk you through provisioning merchant
accounts, tokenizing cards, charging those cards, and finally settling (i.e.
payout) those funds out to your merchants.

3. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.

4. [Push-to-Card Private [BETA]](#push-to-card-private-beta): This guide walks 
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl {{base_url}}/ \
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

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

```
```java

```
To communicate with the {{api_name}} API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `{{basic_auth_username}}`

- Password: `{{basic_auth_password}}`

- Application ID: `{{create_app_scenario_id}}`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

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

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST {{base_url}}/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST {{base_url}}/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST {{base_url}}/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST {{base_url}}/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative
last_name | *string*, **required** | Full legal last name of the merchant's principal representative
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number
email | *string*, **required** | Principal's email address where they can be reached
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City
region | *string*, **required** | State
postal_code | *string*, **required** | Zip or Postal code
country | *string*, **required** | 3-Letter Country code

#### Incorporation Date-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day business was incorporated (between 1 and 31)
month | *integer*, **required** | Month business was incorporated (between 1 and 12)
year | *integer*, **required** | Year business was incorporated (4-digit)


#### DOB-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day of birth (between 1 and 31)
month | *integer*, **required** | Month of birth (between 1 and 12)
year | *integer*, **required** | Year of birth (4-digit)

### Step 2: Tokenize a Bank Account for Funding your Merchant
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

Now that we've created an `Identity` for our merchant, we'll need to add a bank
account where funds will be disbursed (i.e. their funding
account).

In the API, bank accounts -- as well as credit cards -- are represented by the
`Payment Instrument` resource.

To classify the `Payment Instrument` as a bank account you'll need to pass
BANK_ACCOUNT in the `type` field of your request, and you'll also want to pass
the ID of the `Identity` that you created in the last step via the `identity`
field to properly associate it with your merchant.


#### HTTP Request

`POST {{base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **optional** | Account owner's full name
### Step 3: Provision Merchant Account

```shell
curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{provision_merchant_scenario_curl_request}}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_merchant_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{provision_merchant_scenario_php_request}});

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{{provision_merchant_scenario_response}}
```

Now that we've associated a `Payment Instrument` with our seller's `Identity`
we're ready to provision a `Merchant` account. This is the last step before you
can begin processing on their behalf. Luckily you've already done most of the
heavy lifting. Just make one final POST request, and you'll be returned a
`Merchant` resource. Take a second to inspect this newly created resource,
particularly the `onboarding_state`, which can have 3 potential states that
indicate its ability to process and settle funds:

1. `PROVISIONING`: Request is pending (state will typically change after two minutes)
  * processing_enabled: False
  * settlement_enabled: False

2. `APPROVED`: Merchant has been approved and can begin processing
  * processing_enabled: True
  * settlement_enabled: True

3. `REJECTED`: Merchant was rejected by the processor either because the collected
information was invalid or it failed one of a number of regulatory and/or
compliance checks (e.g. KYC, OFAC or MATCH)
  * processing_enabled: False
  * settlement_enabled: False

<aside class="notice">
Provisioning a Merchant account is an asynchronous request. We recommend creating
a Webhook to listen for the state change.
</aside>


#### HTTP Request

`POST {{base_url}}/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
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

Now that we have successfully provisioned a `Merchant` we'll need to create an
`Identity` that represents your buyer. Don't worry tho you won't need to capture
the same amount of information from your buyer. **So long as you
don't pass a business_type field all the fields are optional.**

<aside class="warning">
Passing a business_type will introduce the underwriting form validators.
</aside>

Typically, we suggest at least collecting the buyer's name and email to help
with accounting, reconciliation, and chargebacks.

#### HTTP Request

`POST {{base_url}}/identities`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **optional** | First name
last_name | *string*, **optional** | Last name
email | *string*, **optional** | Email
phone | *string*, **optional** | Phone number
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
personal_address | *object*, **optional** | Customers shipping address or billing address (Full description of child attributes below)

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City
region | *string*, **required** | State
postal_code | *string*, **required** | Zip or Postal code
country | *string*, **required** | 3-Letter Country code

### Step 5: Tokenize a Card
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

Now that we have an `Identity` resource representing our buyer, we'll need to
create a `Payment Instrument` which represents the credit card you'll be debiting
(i.e. charging).

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

You'll also need to interpolate your own buyer's `Identity` ID
from the previous request to properly associate it.

Please review our guide on how to tokenize cards via the [embedded tokenization
form](#embedded-tokenization-using-iframe)

#### HTTP Request

`POST {{base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
identity | *string*, **required** | ID of the `Identity` that the card should be associated
type | *string*, **required** | Type of Payment Instrument (for cards input PAYMENT_CARD)
number | *string*, **required** | Credit card account number
security_code | *string*, **optional** | The 3-4 digit security code for the card (i.e. CVV code)
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | 4-digit expiration year
name | *string*, **optional** | Full name of the registered card holder
address | *object*, **optional** | Billing address (Full description of child attributes below)


#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code
### Step 6: Create an Authorization
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
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
> Example Response:

```json
{{create_authorization_scenario_response}}
```

At this point we've created resources representing the merchant, the buyer, and
the buyer's card.

Next you'll need to create an `Authorization`. What's a `Authorization`? Glad
you asked! An `Authorization` (also known as a card hold) reserves a specific
amount on a card to be captured (i.e. debited) at a later point, usually within
7 days. When an `Authorization` is captured it produces a `Transfer` resource.

To create an `Authorization` we'll supply the buyer's `Payment Instrument` ID
as the source field and the seller's `Identity` ID in the merchant_identity field.
Note that the `amount` field is in cents.

Simple enough, right? You'll also want to store the ID from that `Authorization`
for your records and so that we can capture those funds in the next step.


`Authorizations` have two possible states SUCCEEDED and FAILED. If the `Authorization`
 has succeeded, it must be captured before the `expires_at` or the funds will
 be released.

<aside class="warning">
Authorizations on debit cards actually place a hold on funds in the cardholder's
bank account and may lead to lower than expected balances and/or insufficient
funds issues.
</aside>


<aside class="notice">
If the transfer field of an Authorization is null it has not yet been captured.
</aside>


#### HTTP Request

`POST {{base_url}}/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The `Payment Instrument` that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Capture the Authorization
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

Now that we have the funds held on a card, we'll need to capture them. Failing to
do so will result in the funds being released (i.e. returned) to the buyer.

Note you can capture any amount less than or equal to the `amount` of the original
 `Authorization`. You will also want to pass a `fee`. The `fee` field is the amount
 in cents you would like to keep before settling out to the merchant. For example,
 if you're charging the buyer $100 on behalf of your merchant, and you're taking
 a %10 service fee you'll want to pass 1000 as the fee. This way when the
 funds are eventually settled out only $90 will be disbursed to your merchant.

Once successfully captured the `transfer` field of the `Authorization` will
contain the ID for the corresponding `Transfer` resource. By default, `Transfers`
will be in a PENDING state. PENDING means that the system hasn't submitted the
capture request as they are submitted via batch request. Once submited
the state of the `Transfer` will update to SUCCEEDED.

Next we're going to show you how to settle out the funds to your merchant.

#### HTTP Request

`PUT {{base_url}}/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the  `Authorization`  you would like to capture in cents. Must be less than or equal to the amount of the `Authorization`
fee | *integer*, **optional** | Amount of the captured `Authorization` you would like to collect as your fee. Must be less than or equal to the amount

### Step 8: Create a Batch Settlment
```shell
curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/settlements \
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
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{{create_settlement_scenario_response}}
```

Awesome! Now you know how to charge a card. Next you need to settle out the
funds to your merchant's bank account (i.e. issue an ACH Credit). To do so you
will create a `Settlement` resource. A `Settlement` is a logical construct
representing a collection (i.e. batch) of `Transfers` that are intended to be
paid out to a specific `Merchant`.


Each settlement is comprised of all the `Transfers` that have a SUCCEEDED `state` and
that have not yet been previously settled out. In other words, if a merchant has a
`Transfer` in the PENDING state it will not be included in the batch settlement.
In addition, `Settlements` will include any refunded Transfers as a deduction.
The `total_amount` is the net settled amount in cents (i.e. the amount in cents
that will be deposited into your merchant's bank account after your fees have
been deducted).

<aside class="notice">
Once a batch Settlement has been created it will undergo review and typically
paid out within 24 hours.
</aside>

Note, that for reconciliation purposes each `Settlement` contains a [transfers
link](#list-transfers-in-a-settlement) which returns a list of all the
`Transfers` that comprise the batch.

#### HTTP Request

`POST {{base_url}}/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## API Endpoints

There are two different endpoints (base urls) that you can make API calls with. "Stage" if you are testing, and "Production" for when your application is ready to go live.

The URLs are:

Stage API: https://api-staging.payline.com/

Production API: https://payline.com/
## Embedded Tokenization Using Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to {{api_name}}. For your
convenience we've provided a [jsfiddle]({{embedded_iframe_jsfiddle}}) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the {{api_name}} API.
</aside>

### Step 1: Create a Button

```html
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <body>
        <button id="show-form">Add Your Card</button>
    </body>
</html>
```

Before collecting the sensitive payment information, we will to add a button
to the HTML where we'll be hosting the iframe so that end-users can input their
details.

We have provided a simple example to the right.


### Step 2: Include library

To use the iframe you will need to include the library on the webpage
where you're hosting the aforementioned button. Please include the script as
demonstrated to the right. Please refrain from hosting the iframe library locally
as doing so prevents important updates.


```html
<script type="text/javascript" src="{{embedded_iframe_src}}"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: '{{application}}',
        }, function (tokenizedResponse) {
          // Define a callback to send your token to your back-end server
        });
      });
    });
 </script>
```

Next we need to configure the client so that it associates the card with your `Application`.
We will also need to register a click event that fires when our users click on the
button, thereby rendering the iframe on the page. Then when the form is submitted
you'll be returned a unique `Token` resource representing the submitted card
details. We will also need to define a callback for handling that response.

In the next step we'll show you how to claim the instrument via an authenticated
HTTPS request on your back-end for future use.

> Example Response:

```json
{{create_token_scenario_response}}
```

### Step 4: Associate the Token
```shell
curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{associate_token_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_curl_request}});
$card = $card->save();

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{{associate_token_scenario_response}}
```

Associate the newly tokenized card or bank with the instrument owner's `Identity`.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated.
</aside>

#### HTTP Request

`POST {{base_url}}/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


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
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);


```
> Example Response:

```json
{{create_authorization_scenario_response}}
```

`Authorizations` have two possible states SUCCEEDED and FAILED. If the `Authorization`
 has succeeded, it must be captured before the `expires_at` or the funds will
 be released.

<aside class="warning">
Authorizations on debit cards actually place a hold on funds in the cardholder's
bank account and may lead to lower than expected balances and/or insufficient
funds issues.
</aside>


<aside class="notice">
If the transfer field of an Authorization is null it has not yet been captured.
</aside>


#### HTTP Request

`POST {{base_url}}/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The `Payment Instrument` that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
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

Once successfully captured the `transfer` field of the `Authorization` will
contain the ID for the corresponding `Transfer` resource. By default, `Transfers`
will be in a PENDING state. PENDING means that the system hasn't submitted the
capture request as they are submitted via batch request. Once submited
the state of the `Transfer` will update to SUCCEEDED.



#### HTTP Request

`PUT {{base_url}}/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the `Authorization`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the  `Authorization`  you would like to capture in cents. Must be less than or equal to the amount of the `Authorization`
fee | *integer*, **optional** | Amount of the captured `Authorization` you would like to collect as your fee. Must be less than or equal to the amount

## Void an Authorization
```shell

curl {{base_url}}/authorizations/{{void_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{void_authorization_scenario_curl_request}}'

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
> Example Response:

```json
{{void_authorization_scenario_response}}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT {{base_url}}/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
void_me | *boolean*, **required** | Set to True to void the `Authorization`

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

#### HTTP Request

`GET {{base_url}}/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl {{base_url}}/authorizations/ \
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


```
```java
import io.payline.payments.processing.client.model.Authorization;

client.authorizationsClient().<Resources<Authorization>>resourcesIterator()
  .forEachRemaining(page-> {
    Collection<Authorization> authorizations = page.getContent();
    //do something
  });
```
> Example Response:

```json
{{list_authorizations_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/authorizations/`

# Identities

An `Identity` resource represents either a buyer or a merchant and is in many
ways the centerpiece of the payment API's architecture. `Transfers` and
`Payment Instruments` must be associated with an `Identity`. For both buyers
and merchants this structure makes it easy to manage and reconcile their
associated bank accounts, transaction history, and payouts.

For merchants, the `Identity` resource is used to collect underwriting
information for the business and its principal.

## Create an Identity for a Buyer


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
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST {{base_url}}/identities`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **optional** | First name
last_name | *string*, **optional** | Last name
phone | *string*, **optional** | Phone number
email | *string*, **optional** | Email address
line1 | *string*, **optional** | Street address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Postal code
country | *string*, **optional** | Country
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

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

Before we can begin charging cards we'll need to provision a `Merchant` account
for your seller. This requires 3-steps:

1. Create an `Identity` resource with the merchant's underwriting and identity
verification information (API request to the right)


2. [Create a Payment Instrument](#create-a-bank-account) representing the
merchant's bank account where processed funds will be settled (i.e. deposited)


3. [Provision the Merchant account](##provision-a-merchant)


#### HTTP Request

`POST {{base_url}}/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative
last_name | *string*, **required** | Full legal last name of the merchant's principal representative
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number
email | *string*, **required** | Principal's email address where they can be reached
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City
region | *string*, **required** | State
postal_code | *string*, **required** | Zip or Postal code
country | *string*, **required** | 3-Letter Country code

#### Incorporation Date-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day business was incorporated (between 1 and 31)
month | *integer*, **required** | Month business was incorporated (between 1 and 12)
year | *integer*, **required** | Year business was incorporated (4-digit)


#### DOB-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day of birth (between 1 and 31)
month | *integer*, **required** | Month of birth (between 1 and 12)
year | *integer*, **required** | Year of birth (4-digit)
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

#### HTTP Request

`GET {{base_url}}/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl {{base_url}}/identities/ \
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


```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
> Example Response:

```json
{{list_identities_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/identities/`


## Update an Identity
```shell
curl {{base_url}}/identities/{{update_identity_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{update_identity_scenario_curl_request}}'

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
> Example Response:

```json
{{update_identity_scenario_response}}
```
<aside class="notice">
tax_id and business_tax_id are not updatable. If either field was input incorrectly,
please create a new Identity resource.
</aside>


Update the information of a previously created `Identity`. Please note that in
the case of merchant accounts this API request alone does not update this
information on the underlying processor. To update the merchant's information
 on the underlying processor you must [update the merchant on the
 processor.](#update-info-on-processor)


#### HTTP Request

`POST {{base_url}}/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
url | *string*, **required** | Merchant's publicly available website
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative
last_name | *string*, **required** | Full legal last name of the merchant's principal representative
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number
email | *string*, **required** | Principal's email address where they can be reached
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City
region | *string*, **required** | State
postal_code | *string*, **required** | Zip or Postal code
country | *string*, **required** | 3-Letter Country code

#### Incorporation Date-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day business was incorporated (between 1 and 31)
month | *integer*, **required** | Month business was incorporated (between 1 and 12)
year | *integer*, **required** | Year business was incorporated (4-digit)


#### DOB-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day of birth (between 1 and 31)
month | *integer*, **required** | Month of birth (between 1 and 12)
year | *integer*, **required** | Year of birth (4-digit)
## Provision a Merchant

```shell

curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{provision_merchant_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_merchant_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{provision_merchant_scenario_php_request}});
```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```

> Example Response:

```json
{{provision_merchant_scenario_response}}
```

Provision a `Merchant` for a previously created `Identity` resource to begin
transacting on their behalf.

<aside class="warning">
Please make sure that a bank account has been created and associated to the
previously created Identity before attempting to provision a Merchant account.
</aside>


`Merchant` resources can have 3 potential states:

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


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{provision_merchant_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_merchant_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{provision_merchant_scenario_php_request}});

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{{provision_merchant_scenario_response}}
```

Provision a `Merchant` for a previously created `Identity` resource to begin
transacting on their behalf.

<aside class="warning">
Please make sure that a bank account has been created and associated to the
previously created Identity before attempting to provision a Merchant account.
</aside>


`Merchant` resources can have 3 potential `onboarding_states`:

1. `PROVISIONING`: Request is pending (state will typically change after two minutes)
  * processing_enabled: False
  * settlement_enabled: False

2. `APPROVED`: Merchant has been approved and can begin processing
  * processing_enabled: True
  * settlement_enabled: True

3. `REJECTED`: Merchant was rejected by the processor either because the collected
information was invalid or it failed one of a number of regulatory and/or
compliance checks (e.g. KYC, OFAC or MATCH)
  * processing_enabled: False
  * settlement_enabled: False

<aside class="notice">
Provisioning a `Merchant` account is an asynchronous request. We recommend creating a Webhook to listen for the state change.
</aside>



#### HTTP Request

`POST {{base_url}}/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Retrieve a Merchant
```shell
curl {{base_url}}/merchants/{{fetch_merchant_scenario_id}} \
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

use {{api_name}}\Resources\Merchant;

$merchant = Merchant::retrieve('{{fetch_merchant_scenario_id}}');

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("{{fetch_merchant_scenario_id}}");

```
> Example Response:

```json
{{fetch_merchant_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Create a Merchant User
```shell
curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{}'

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
> Example Response:

```json
{{create_user_merchant_role_scenario_response}}
```

This is the equivalent of provisioning API keys (i.e. credentials) for a `Merchant`.

<aside class="notice">
Each Identity can have multiple Users which allows each merchant to have multiple
API keys that can be independently enabled and disabled. Merchants only have read
access to the API.
</aside>

#### HTTP Request

`POST {{base_url}}/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`


## Reattempt Merchant Provisioning
```shell
curl {{base_url}}/merchants/{{fetch_merchant_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{}'
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
> Example Response:

```json
{{reattempt_provision_merchant_scenario_response}}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST {{base_url}}/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl {{base_url}}/merchants/{{fetch_merchant_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{}'

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
> Example Response:

```json
{{reattempt_provision_merchant_scenario_response}}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST {{base_url}}/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## List all Merchants
```shell
curl {{base_url}}/merchants/ \
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


```
```java

```
> Example Response:

```json
{{list_merchants_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/merchants/`

## List Merchant Verifications
```shell
curl {{base_url}}/merchants/{{fetch_merchant_scenario_id}}/verifications \
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


```
```java

```
> Example Response:

```json
{{list_merchant_verifications_scenario_response}}
```

Retrieve all attempts to onboard (i.e. provision) a merchant onto a processor.

#### HTTP Request

`GET {{base_url}}/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`




# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Create a Card
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
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Please review our guide on how to tokenize cards via the [embedded tokenization
form](#embedded-tokenization-using-iframe)

#### HTTP Request

`POST {{base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
identity | *string*, **required** | ID of the `Identity` that the card should be associated
type | *string*, **required** | Type of Payment Instrument (for cards input PAYMENT_CARD)
number | *string*, **required** | Credit card account number
security_code | *string*, **optional** | The 3-4 digit security code for the card (i.e. CVV code)
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | 4-digit expiration year
name | *string*, **optional** | Full name of the registered card holder
address | *object*, **optional** | Billing address (Full description of child attributes below)


#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code

## Create a Bank Account
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

#### HTTP Request

`POST {{base_url}}/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **optional** | Account owner's full name
## Tokenize Card with Embedded Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to {{api_name}}. For your
convenience we've provided a [jsfiddle]({{embedded_iframe_jsfiddle}}) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the {{api_name}} API.
</aside>

### Step 1: Create a Button

```html
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <body>
        <button id="show-form">Add Your Card</button>
    </body>
</html>
```

Before collecting the sensitive payment information, we will to add a button
to the HTML where we'll be hosting the iframe so that end-users can input their
details.

We have provided a simple example to the right.


### Step 2: Include library

To use the iframe you will need to include the library on the webpage
where you're hosting the aforementioned button. Please include the script as
demonstrated to the right. Please refrain from hosting the iframe library locally
as doing so prevents important updates.


```html
<script type="text/javascript" src="{{embedded_iframe_src}}"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: '{{application}}',
        }, function (tokenizedResponse) {
          // Define a callback to send your token to your back-end server
        });
      });
    });
 </script>
```

Next we need to configure the client so that it associates the card with your `Application`.
We will also need to register a click event that fires when our users click on the
button, thereby rendering the iframe on the page. Then when the form is submitted
you'll be returned a unique `Token` resource representing the submitted card
details. We will also need to define a callback for handling that response.

In the next step we'll show you how to claim the instrument via an authenticated
HTTPS request on your back-end for future use.

> Example Response:

```json
{{create_token_scenario_response}}
```

```shell
curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{associate_token_scenario_curl_request}}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_curl_request}});
$card = $card->save();

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);


```
### Step 4: Associate to an Identity

> Example Response:

```json
{{associate_token_scenario_response}}
```

Before you can use the newly tokenized card you will need to associate it with
an `Identity`. To do this you must make an authenticated `POST` request to the
`/payment_instruments` endpoint with the relevant token and the buyer's
`Identity` information.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated.
</aside>

#### HTTP Request

`POST {{base_url}}/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{associate_token_scenario_curl_request}}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_curl_request}});
$card = $card->save();

```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{{associate_token_scenario_response}}
```

Associate the newly tokenized card or bank with the instrument owner's `Identity`.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated.
</aside>

#### HTTP Request

`POST {{base_url}}/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Fetch a Payment Instrument

```shell


curl {{base_url}}/payment_instruments/{{fetch_payment_instrument_scenario_id}} \
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

$card = PaymentInstrument::retrieve('{{fetch_payment_instrument_scenario_id}}');

```
```java

import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("{{fetch_payment_instrument_scenario_id}}")

```
> Example Response:

```json
{{fetch_payment_instrument_scenario_response}}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET {{base_url}}/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl {{base_url}}/payment_instruments/{{update_payment_instrument_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{update_payment_instrument_scenario_curl_request}}'

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
> Example Response:

```json
{{update_payment_instrument_scenario_response}}
```

Update a previously created `Payment Instrument`.

<aside class="notice">
Only the tags field can be updated. If it is required to update other fields,
such as account information or expiration dates please retokenize the payment
instrument.
</aside>

#### HTTP Request

`PUT {{base_url}}/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
tags | *object*, **optional** | Single level key value pair for annotating custom meta data


## List all Payment Instruments

```shell
curl {{base_url}}/payment_instruments \
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
{{list_payment_instruments_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/payment_instruments`

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl {{base_url}}/identities/{{create_merchant_identity_scenario_id}}/settlements \
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
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{{create_settlement_scenario_response}}
```
Each settlement is comprised of all the `Transfers` that have a SUCCEEDED state and
that have not been previously settled out. In other words, if a merchant has a
`Transfer` in the PENDING state it will not be included in the batch settlement.
In addition, `Settlements` will include any refunded Transfers as a deduction.
The `total_amount` is the net settled amount in cents (i.e. the amount in cents
that will be deposited into your merchant's bank account after your fees have
been deducted).

<aside class="notice">
To view all the Transfers that were included in a Settlement you can make a
request to the transfers link (i.e. POST {{base_url}}/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST {{base_url}}/identities/:IDENTITY_ID/settlements`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the `Identity` for the merchant you wish to settle out


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Retrieve a Settlement

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

Fetch a previously created `Settlement`.

#### HTTP Request

`POST {{base_url}}/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl {{base_url}}/settlements/{{create_settlement_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -X PUT \
    -d '{{fund_settlement_scenario_curl_request}}'

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
> Example Response:

```json
{{fund_settlement_scenario_response}}
```

Issue funding instructions to pay out funds that are allocated in a previously
 created batch `Settlement` resource for a merchant.

<aside class="warning">
Once instructions have been issued to a particular destination it cannot be
updated.
</aside>


#### HTTP Request

`PUT {{base_url}}/settlements/:SETTLEMENT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where the funds should be deposited

## List all Settlements
```shell
curl {{base_url}}/settlements/ \
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


```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
> Example Response:

```json
{{list_settlements_scenario_response}}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET {{base_url}}/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl {{base_url}}/settlements/{{fetch_settlement_scenario_id}}/funding_transfers \
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


```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
> Example Response:

```json
{{list_settlement_funding_transfers_scenario_response}}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET {{base_url}}/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl {{base_url}}/settlements/{{fetch_settlement_scenario_id}}/transfers \
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


```
```java

```
> Example Response:

```json
{{list_settlement_transfers_scenario_response}}
```

List the batch of `Transfers` of type `DEBIT` and `REFUND` that comprise the net
 settled amount of a `Settlement`.

#### HTTP Request

`GET {{base_url}}/settlements/:SETTLEMENT_ID/transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


# Transfers

A `Transfer` represents any flow of funds either to or from a `Payment Instrument`.
For example, a `Transfer` can be either a [debit to a card](#debit-a-card), a
credit to a bank account, or a [refund to a card](#refund-a-debit) depending on
the request.

`Transfers` can have three possible states values: PENDING, SUCCEEDED, or FAILED.

- **PENDING:** Authorization on `Payment Instrument` successfully created (i.e.
funds are being held), but awaiting system to batch submit the capture request
to complete the transaction

- **SUCCEEDED:** Funds captured and available for settlement (i.e. disbursement
via ACH Credit)

- **FAILED:** Authorization attempt failed

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
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

#### HTTP Request

`GET {{base_url}}/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

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

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST {{base_url}}/transfers/:TRANSFER_ID/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the original `Transfer`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | The amount of the refund in cents (Must be equal to or less than the amount of the original `Transfer`)

## List all Transfers
```shell
curl {{base_url}}/transfers \
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


```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
> Example Response:

```json
{{list_transfers_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/transfers`
# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the {{api_name}} API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
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

#### HTTP Request

`POST {{base_url}}/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

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

#### HTTP Request

`GET {{base_url}}/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl {{base_url}}/webhooks/ \
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


```
```java
import io.{{api_name_downcase}}.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
> Example Response:

```json
{{list_webhooks_scenario_response}}
```

#### HTTP Request

`GET {{base_url}}/webhooks`
    

## Sample Payloads


```shell
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
### Created Authorization

```javascript

{
  "type" : "created",
  "entity" : "authorization",
  "occurred_at" : "2016-07-06T08:15:21.734",
  "_embedded" : {
    "authorizations" : [ {
      "amount" : 100,
      "trace_id" : "5e157d2f-1362-4ab2-86af-3f97a8f28f0d",
      "created_at" : "2016-07-06T08:15:21.63Z",
      "source" : "PIeAkgVK9TPBnmyf6CSskv5i",
      "merchant_identity" : "IDradKrsCKMYJyj3VFKimKuy",
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "transfer" : null,
      "expires_at" : "2016-07-13T08:15:21.63Z",
      "updated_at" : "2016-07-06T08:15:21.65Z",
      "is_void" : false,
      "currency" : "USD",
      "id" : "AUfU8FU7RfgTmhfRagrF1RpS",
      "state" : "SUCCEEDED"
    } ]
  }
}
```

### Created New Transfer

```javascript
{
 "type" : "created",
  "entity" : "transfer",
  "occurred_at" : "2016-07-06T07:41:38.466",
  "_embedded" : {
    "transfers" : [ {
      "amount" : 100,
      "trace_id" : "e87b8ebc-177e-4e11-9cc3-6cfcfae7adc8",
      "fee" : 0,
      "destination" : "PIg3pCsoqrygp1gCvBNvfT3x",
      "created_at" : "2016-07-06T07:41:38.24Z",
      "source" : "PI2f1E5JVeQriDMeDpULnae3",
      "merchant_identity" : "IDoXe9ce6ztf6Pbpoq2WbeMt",
      "type" : "REVERSAL",
      "tags" : { },
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "application" : "APdHz4LE8cNmJbbK7WW2egcg",
      "updated_at" : "2016-07-06T07:41:38.37Z",
      "currency" : "USD",
      "id" : "TRjgpj7b7xZXN18XyD7G3JER",
      "state" : "PENDING"
    } ]
  }
}
```

### Updated Transfer

```javascript
{
  "type" : "updated",
  "entity" : "transfer",
  "occurred_at" : "2016-07-06T07:08:02.342",
  "_embedded" : {
    "transfers" : [ {
      "amount" : 100,
      "trace_id" : "55ab6c90-2cfd-47ea-8f9b-c7385880617d",
      "fee" : 0,
      "destination" : "PIx7rQE9dzEGoccQ76D22xuZ",
      "created_at" : "2016-07-06T07:07:39.51Z",
      "source" : "PIoHzz6XzUzCqi5YqL9TVGN6",
      "merchant_identity" : "IDhxk2ESd2eFF38ewG7Eth93",
      "type" : "REVERSAL",
      "tags" : { },
      "statement_descriptor" : "PLD*PRESTIGE WORLD WI",
      "application" : "APwD1R6mEokpr84pypG4TBZv",
      "updated_at" : "2016-07-06T07:08:02.19Z",
      "currency" : "USD",
      "id" : "TR4CUpq9T8E6tBDmWMxQQ2P1",
      "state" : "SUCCEEDED"
    } ]
  }
}

```



### Created Payment Instrument

```javascript
{
  "type" : "created",
  "entity" : "instrument",
  "occurred_at" : "2016-07-06T07:06:04.751",
  "_embedded" : {
    "instruments" : [ {
      "updated_at" : "2016-07-06T07:06:04.63Z",
      "identity" : "IDbtqHvNT1eJHi3WbkbzAb5y",
      "fingerprint" : "FPR369385117",
      "created_at" : "2016-07-06T07:06:04.63Z",
      "id" : "PIx7rQE9dzEGoccQ76D22xuZ",
      "instrument_type" : "PAYMENT_CARD",
      "tags" : { }
    } ]
  }
}
```

### Created Identity

```javascript
{
  "type" : "created",
  "entity" : "identity",
  "occurred_at" : "2016-07-06T07:05:57.659",
  "_embedded" : {
    "identitys" : [ {
      "updated_at" : "2016-07-06T07:05:57.55Z",
      "created_at" : "2016-07-06T07:05:57.55Z",
      "id" : "IDt9PQrHhTmmwxHrmcxt46Eq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
        "doing_business_as" : "Bobs Burgers",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "business_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 8",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.BobsBurgers.com",
        "annual_card_volume" : 12000000,
        "has_accepted_credit_cards_previously" : true,
        "incorporation_date" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "principal_percentage_ownership" : 50,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "key" : "value"
      }
    } ]
  }
}
```

### Provisioned Merchant

```javascript
{
  "type" : "created",
  "entity" : "merchant",
  "occurred_at" : "2016-07-06T07:40:01.224",
  "_embedded" : {
    "merchants" : [ {
      "updated_at" : "2016-07-06T07:40:00.77Z",
      "identity" : "IDoXe9ce6ztf6Pbpoq2WbeMt",
      "created_at" : "2016-07-06T07:40:00.66Z",
      "id" : "MU6LMTZMw5X1MmjzqzkaPE7v",
      "underwriting_state" : "APPROVED",
      "processor" : "DUMMY_V1",
      "verification" : null,
      "merchant_profile" : "MP5LCjDsB6kY7wEPHK9szmAw"
    } ]
  }
}
```

### Successfully Underwritten Merchant

```javascript
{
  "type" : "underwritten",
  "entity" : "merchant",
  "occurred_at" : "2016-07-06T08:13:42.460",
  "_embedded" : {
    "merchants" : [ {
      "updated_at" : "2016-07-06T08:13:42.28Z",
      "identity" : "IDradKrsCKMYJyj3VFKimKuy",
      "created_at" : "2016-07-06T08:13:42.28Z",
      "id" : "MUew1oPVk5nBHypxa33U39n3",
      "underwriting_state" : "APPROVED",
      "processor" : "DUMMY_V1",
      "verification" : null,
      "merchant_profile" : "MPtn5JmNnABFXHBtkmaS1aBP"
    } ]
  }
}
```

### Created Dispute

```javascript
{
  "type" : "created",
  "entity" : "dispute",
  "occurred_at" : "2016-07-06T08:14:01.288",
  "_embedded" : {
    "disputes" : [ {
      "occurred_at" : "2016-07-06T08:13:47.56Z",
      "reason" : "FRAUD",
      "amount" : 0,
      "transfer" : "TRnEarDDVuVkBJLBL6PhZTLT",
      "updated_at" : "2016-07-06T08:14:01.18Z",
      "identity" : "ID4DFq8Q2V1zHoaU8WCTzpge",
      "created_at" : "2016-07-06T08:14:01.18Z",
      "id" : "DIvHQsw2tcwUhkMtzXVbksxo",
      "state" : "PENDING",
      "respond_by" : "2016-07-13T08:14:01.18Z",
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      }
    } ]
  }
}
```
