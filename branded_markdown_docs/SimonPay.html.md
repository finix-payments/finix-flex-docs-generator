---
title: SimonPay API Reference

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

These guides provide a collection of resources for utilizing the SimonPay
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
## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "ACME Anchors", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "incorporation_date": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 120000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "ACME Anchors", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.ACMEAnchors.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java
import io.simonpay.payments.processing.client.model.Identity;

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
{
  "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "ACME Anchors",
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
    "mcc" : 742,
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 120000,
    "amex_mid" : "12345678910",
    "discover_mid" : null,
    "url" : "www.ACMEAnchors.com",
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
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-10-04T23:43:11.12Z",
  "updated_at" : "2016-10-04T23:43:11.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://api-staging.simonpayments.com/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://api-staging.simonpayments.com/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "account_type": "SAVINGS", 
	    "name": "Fran Lemke", 
	    "tags": {
	        "Bank Account": "Company Account"
	    }, 
	    "country": "USA", 
	    "bank_code": "123123123", 
	    "account_number": "123123123", 
	    "type": "BANK_ACCOUNT", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> array(
	        "Bank Account"=> "Company Account"
	    ), 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDs3XCSAdBXoqMjtsTpMDrh5"
	));
$bank_account = $bank_account->save();

```
```java
import io.simonpay.payments.processing.client.model.BankAccount;

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
{
  "id" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T23:43:23.91Z",
  "updated_at" : "2016-10-04T23:43:23.91Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/payment_instruments`

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
curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.simonpay.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "verification" : "VIfdMDaMiPyEpNgaxgojryYd",
  "merchant_profile" : "MPovQP6nFotXCzStYYyQq1WD",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T23:43:26.26Z",
  "updated_at" : "2016-10-04T23:43:26.26Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MPovQP6nFotXCzStYYyQq1WD"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIfdMDaMiPyEpNgaxgojryYd"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marcie", 
	        "last_name": "Henderson", 
	        "email": "therock@gmail.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Marcie", 
	        "last_name"=> "Henderson", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        )
	    )
	)
);
$identity = $identity->save();

```
```java

import io.simonpay.payments.processing.client.model.Identity;

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
{
  "id" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
  "entity" : {
    "title" : null,
    "first_name" : "Marcie",
    "last_name" : "Henderson",
    "email" : "therock@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677613",
    "business_phone" : null,
    "personal_address" : {
      "line1" : "741 Douglass St",
      "line2" : "Apartment 7",
      "city" : "San Mateo",
      "region" : "CA",
      "postal_code" : "94114",
      "country" : "USA"
    },
    "business_address" : null,
    "mcc" : null,
    "dob" : null,
    "max_transaction_amount" : 0,
    "amex_mid" : null,
    "discover_mid" : null,
    "url" : null,
    "annual_card_volume" : 0,
    "has_accepted_credit_cards_previously" : false,
    "incorporation_date" : null,
    "principal_percentage_ownership" : null,
    "short_business_name" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-10-04T23:43:27.81Z",
  "updated_at" : "2016-10-04T23:43:27.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities`

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


curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "name": "Ricardo White", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4242424242424242", 
	    "expiration_month": 12, 
	    "address": {
	        "city": "San Mateo", 
	        "country": "USA", 
	        "region": "CA", 
	        "line2": "Apartment 7", 
	        "line1": "741 Douglass St", 
	        "postal_code": "94114"
	    }, 
	    "security_code": "112", 
	    "type": "PAYMENT_CARD", 
	    "identity": "IDcwkUSpMa4EQyjgDQ4YjP3q"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Ricardo White", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
	    "number"=> "4242424242424242", 
	    "expiration_month"=> 12, 
	    "address"=> array(
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    ), 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDcwkUSpMa4EQyjgDQ4YjP3q"
	));
$card = $card->save();


```
```java

import io.simonpay.payments.processing.client.model.PaymentCard;

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
{
  "id" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "fingerprint" : "FPR-657319974",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ricardo White",
  "address" : {
    "line1" : "741 Douglass St",
    "line2" : "Apartment 7",
    "city" : "San Mateo",
    "region" : "CA",
    "postal_code" : "94114",
    "country" : "USA"
  },
  "address_verification" : "UNKNOWN",
  "security_code_verification" : "UNKNOWN",
  "created_at" : "2016-10-04T23:43:28.85Z",
  "updated_at" : "2016-10-04T23:43:28.85Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/updates"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/payment_instruments`

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
curl https://api-staging.simonpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "merchant_identity": "IDs3XCSAdBXoqMjtsTpMDrh5", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIsWAgCjqrgp7w2eP4vP7uWj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDs3XCSAdBXoqMjtsTpMDrh5", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIsWAgCjqrgp7w2eP4vP7uWj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```java
import io.simonpay.payments.processing.client.model.Authorization;

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
{
  "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:37.63Z",
  "updated_at" : "2016-10-04T23:43:37.65Z",
  "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : false,
  "expires_at" : "2016-10-11T23:43:37.63Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/authorizations`

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
curl https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUg6yBTbAobSFN2xdHtVnXeH');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUg6yBTbAobSFN2xdHtVnXeH");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:37.50Z",
  "updated_at" : "2016-10-04T23:43:38.99Z",
  "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : false,
  "expires_at" : "2016-10-11T23:43:37.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
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

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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
curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;
use SimonPay\Resources\Settlement;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```java
import io.simonpay.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STvq7bQrBSqa8fPzXobfHa84",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "currency" : "USD",
  "created_at" : "2016-10-04T23:50:46.63Z",
  "updated_at" : "2016-10-04T23:50:46.78Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 434885,
  "total_fee" : 43490,
  "net_amount" : 391395,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Embedded Tokenization Using Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to SimonPay. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/rserna2010/1626475h/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the SimonPay API.
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
<script type="text/javascript" src="https://vgs-assets.s3.amazonaws.com/payline-1.latest.js"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: 'APdAAD1S6HYtHTVnrqFdPrsp',
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
{
  "id" : "TK6qtbPN4cUUXyy5wi2s6dqs",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-04T23:43:40.99Z",
  "updated_at" : "2016-10-04T23:43:40.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-05T23:43:40.99Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	});
$card = $card->save();

```
```java
import io.simonpay.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{
  "id" : "PI6qtbPN4cUUXyy5wi2s6dqs",
  "fingerprint" : "FPR-1132692079",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : null,
  "address" : {
    "line1" : "741 Douglass St",
    "line2" : "Apartment 7",
    "city" : "San Mateo",
    "region" : "CA",
    "postal_code" : "94114",
    "country" : "USA"
  },
  "address_verification" : "UNKNOWN",
  "security_code_verification" : "UNKNOWN",
  "created_at" : "2016-10-04T23:43:41.84Z",
  "updated_at" : "2016-10-04T23:43:41.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/updates"
    }
  }
}
```

Associate the newly tokenized card or bank with the instrument owner's `Identity`.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated.
</aside>

#### HTTP Request

`POST https://api-staging.simonpayments.com/payment_instruments`


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
curl https://api-staging.simonpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "merchant_identity": "IDs3XCSAdBXoqMjtsTpMDrh5", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIsWAgCjqrgp7w2eP4vP7uWj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDs3XCSAdBXoqMjtsTpMDrh5", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIsWAgCjqrgp7w2eP4vP7uWj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```java
import io.simonpay.payments.processing.client.model.Authorization;

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
{
  "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:37.63Z",
  "updated_at" : "2016-10-04T23:43:37.65Z",
  "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : false,
  "expires_at" : "2016-10-11T23:43:37.63Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/authorizations`

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
curl https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUg6yBTbAobSFN2xdHtVnXeH');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUg6yBTbAobSFN2xdHtVnXeH");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:37.50Z",
  "updated_at" : "2016-10-04T23:43:38.99Z",
  "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : false,
  "expires_at" : "2016-10-11T23:43:37.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
```

Once successfully captured the `transfer` field of the `Authorization` will
contain the ID for the corresponding `Transfer` resource. By default, `Transfers`
will be in a PENDING state. PENDING means that the system hasn't submitted the
capture request as they are submitted via batch request. Once submited
the state of the `Transfer` will update to SUCCEEDED.



#### HTTP Request

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.simonpayments.com/authorizations/AUfppmw6T6Sn9n6K18ygxLFT \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUfppmw6T6Sn9n6K18ygxLFT",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:43.10Z",
  "updated_at" : "2016-10-04T23:43:44.30Z",
  "trace_id" : "24335363-88bd-4dc8-ba0e-dbd630023b28",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : true,
  "expires_at" : "2016-10-11T23:43:43.10Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUfppmw6T6Sn9n6K18ygxLFT"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUg6yBTbAobSFN2xdHtVnXeH');

```
```java

import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUg6yBTbAobSFN2xdHtVnXeH");

```
> Example Response:

```json
{
  "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:37.50Z",
  "updated_at" : "2016-10-04T23:43:38.99Z",
  "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "is_void" : false,
  "expires_at" : "2016-10-11T23:43:37.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://api-staging.simonpayments.com/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


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
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUfppmw6T6Sn9n6K18ygxLFT",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:43.10Z",
      "updated_at" : "2016-10-04T23:43:44.30Z",
      "trace_id" : "24335363-88bd-4dc8-ba0e-dbd630023b28",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "is_void" : true,
      "expires_at" : "2016-10-11T23:43:43.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AUfppmw6T6Sn9n6K18ygxLFT"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        }
      }
    }, {
      "id" : "AUg6yBTbAobSFN2xdHtVnXeH",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:37.50Z",
      "updated_at" : "2016-10-04T23:43:38.99Z",
      "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "is_void" : false,
      "expires_at" : "2016-10-11T23:43:37.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AUg6yBTbAobSFN2xdHtVnXeH"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "transfer" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 2
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/authorizations/`

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


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marcie", 
	        "last_name": "Henderson", 
	        "email": "therock@gmail.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Marcie", 
	        "last_name"=> "Henderson", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        )
	    )
	)
);
$identity = $identity->save();

```
```java

import io.simonpay.payments.processing.client.model.Identity;

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
{
  "id" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
  "entity" : {
    "title" : null,
    "first_name" : "Marcie",
    "last_name" : "Henderson",
    "email" : "therock@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677613",
    "business_phone" : null,
    "personal_address" : {
      "line1" : "741 Douglass St",
      "line2" : "Apartment 7",
      "city" : "San Mateo",
      "region" : "CA",
      "postal_code" : "94114",
      "country" : "USA"
    },
    "business_address" : null,
    "mcc" : null,
    "dob" : null,
    "max_transaction_amount" : 0,
    "amex_mid" : null,
    "discover_mid" : null,
    "url" : null,
    "annual_card_volume" : 0,
    "has_accepted_credit_cards_previously" : false,
    "incorporation_date" : null,
    "principal_percentage_ownership" : null,
    "short_business_name" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-10-04T23:43:27.81Z",
  "updated_at" : "2016-10-04T23:43:27.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "ACME Anchors", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "incorporation_date": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 120000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "ACME Anchors", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.ACMEAnchors.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java

import io.simonpay.payments.processing.client.model.Identity;

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
{
  "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "ACME Anchors",
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
    "mcc" : 742,
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 120000,
    "amex_mid" : "12345678910",
    "discover_mid" : null,
    "url" : "www.ACMEAnchors.com",
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
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-10-04T23:43:11.12Z",
  "updated_at" : "2016-10-04T23:43:11.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account
for your seller. This requires 3-steps:

1. Create an `Identity` resource with the merchant's underwriting and identity
verification information (API request to the right)


2. [Create a Payment Instrument](#create-a-bank-account) representing the
merchant's bank account where processed funds will be settled (i.e. deposited)


3. [Provision the Merchant account](##provision-a-merchant)


#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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

curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');
```
```java

import io.simonpay.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDs3XCSAdBXoqMjtsTpMDrh5");

```
> Example Response:

```json
{
  "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "ACME Anchors",
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
    "mcc" : 742,
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 120000,
    "amex_mid" : "12345678910",
    "discover_mid" : null,
    "url" : "www.ACMEAnchors.com",
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
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-10-04T23:43:11.06Z",
  "updated_at" : "2016-10-04T23:43:11.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl https://api-staging.simonpayments.com/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
import io.simonpay.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
      "entity" : {
        "title" : null,
        "first_name" : "Marcie",
        "last_name" : "Henderson",
        "email" : "therock@gmail.com",
        "business_name" : null,
        "business_type" : null,
        "doing_business_as" : null,
        "phone" : "7145677613",
        "business_phone" : null,
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "business_address" : null,
        "mcc" : null,
        "dob" : null,
        "max_transaction_amount" : 0,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:27.75Z",
      "updated_at" : "2016-10-04T23:43:27.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "ID582rm3UZiUXvvhTmhg5q5n",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "GOVERNMENT_AGENCY",
        "doing_business_as" : "Lees Sandwiches",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.LeesSandwiches.com",
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
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:22.77Z",
      "updated_at" : "2016-10-04T23:43:22.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDcs2K61xEh6zz2QbFppswWo",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:21.73Z",
      "updated_at" : "2016-10-04T23:43:21.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDeAJMyBJCRVGuBopKaRB748",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:20.74Z",
      "updated_at" : "2016-10-04T23:43:20.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDknUF3Lep3HLNCbwHASQfLP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:19.68Z",
      "updated_at" : "2016-10-04T23:43:19.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDrzf86q5Kr6DVuay3jzvf9v",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GENERAL_PARTNERSHIP",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:18.23Z",
      "updated_at" : "2016-10-04T23:43:18.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDqe1H62ohL9z3zp9tC66YWs",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_PARTNERSHIP",
        "doing_business_as" : "Petes Coffee",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PetesCoffee.com",
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
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:16.91Z",
      "updated_at" : "2016-10-04T23:43:16.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDNzj2WiJtSbzqCS7y1Lre7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "PARTNERSHIP",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:15.58Z",
      "updated_at" : "2016-10-04T23:43:15.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDrdCzHjXTDrAMx6oQSRujXb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
      },
      "created_at" : "2016-10-04T23:43:14.11Z",
      "updated_at" : "2016-10-04T23:43:14.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "ID6MzAm5hKno9t6yBvpk2gLR",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "CORPORATION",
        "doing_business_as" : "Lees Sandwiches",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.LeesSandwiches.com",
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
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:12.65Z",
      "updated_at" : "2016-10-04T23:43:12.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:11.06Z",
      "updated_at" : "2016-10-04T23:43:11.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDt3i17wodcs2rjpLrYF653g",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Venmo",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Venmo",
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
        "mcc" : null,
        "dob" : {
          "day" : 27,
          "month" : 5,
          "year" : 1978
        },
        "max_transaction_amount" : 12000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-10-04T23:43:06.70Z",
      "updated_at" : "2016-10-04T23:43:06.76Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 12
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/identities/`


## Update an Identity
```shell
curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Step", 
	        "last_name": "Lopez", 
	        "amex_mid": "12345678910", 
	        "title": "CTO", 
	        "dob": {
	            "year": 1988, 
	            "day": 2, 
	            "month": 5
	        }, 
	        "has_accepted_credit_cards_previously": true, 
	        "mcc": "0742", 
	        "phone": "7144177878", 
	        "business_tax_id": "123456789", 
	        "max_transaction_amount": 120000, 
	        "principal_percentage_ownership": 50, 
	        "doing_business_as": "Golds Gym", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Golds Gym", 
	        "url": "www.GoldsGym.com", 
	        "business_name": "Golds Gym", 
	        "personal_address": {
	            "city": "San Diego", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 2", 
	            "line1": "712 Douglass St", 
	            "postal_code": "94194"
	        }, 
	        "email": "user@example.org", 
	        "tax_id": "999999999"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Step",
    "last_name" : "Lopez",
    "email" : "user@example.org",
    "business_name" : "Golds Gym",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Golds Gym",
    "phone" : "7144177878",
    "business_phone" : "+1 (408) 756-4497",
    "personal_address" : {
      "line1" : "712 Douglass St",
      "line2" : "Apartment 2",
      "city" : "San Diego",
      "region" : "CA",
      "postal_code" : "94194",
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
    "mcc" : 742,
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 120000,
    "amex_mid" : "12345678910",
    "discover_mid" : null,
    "url" : "www.GoldsGym.com",
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
    "default_statement_descriptor" : "Golds Gym"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2016-10-04T23:43:11.06Z",
  "updated_at" : "2016-10-04T23:44:03.72Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities`

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

curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);
```
```java

import io.simonpay.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```

> Example Response:

```json
{
  "id" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "verification" : "VIfdMDaMiPyEpNgaxgojryYd",
  "merchant_profile" : "MPovQP6nFotXCzStYYyQq1WD",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T23:43:26.26Z",
  "updated_at" : "2016-10-04T23:43:26.26Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MPovQP6nFotXCzStYYyQq1WD"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIfdMDaMiPyEpNgaxgojryYd"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.simonpay.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "verification" : "VIfdMDaMiPyEpNgaxgojryYd",
  "merchant_profile" : "MPovQP6nFotXCzStYYyQq1WD",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T23:43:26.26Z",
  "updated_at" : "2016-10-04T23:43:26.26Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MPovQP6nFotXCzStYYyQq1WD"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIfdMDaMiPyEpNgaxgojryYd"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Retrieve a Merchant
```shell
curl https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Merchant;

$merchant = Merchant::retrieve('MU44oTHgF4SpA6dTGc1m6eu7');

```
```java
import io.simonpay.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU44oTHgF4SpA6dTGc1m6eu7");

```
> Example Response:

```json
{
  "id" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "verification" : null,
  "merchant_profile" : "MPovQP6nFotXCzStYYyQq1WD",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-04T23:43:26.16Z",
  "updated_at" : "2016-10-04T23:43:26.38Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MPovQP6nFotXCzStYYyQq1WD"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Create a Merchant User
```shell
curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US9D1BFHCEmHxk7bJLwwT2Db",
  "password" : "f5245e14-ee53-425b-961f-5b0d4424f32d",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-04T23:43:33.93Z",
  "updated_at" : "2016-10-04T23:43:33.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/US9D1BFHCEmHxk7bJLwwT2Db"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

This is the equivalent of provisioning API keys (i.e. credentials) for a `Merchant`.

<aside class="notice">
Each Identity can have multiple Users which allows each merchant to have multiple
API keys that can be independently enabled and disabled. Merchants only have read
access to the API.
</aside>

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`


## Reattempt Merchant Provisioning
```shell
curl https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIn62CaT8ypqK7r915P51G1F",
  "external_trace_id" : "3c16bb72-8b6d-4f11-9e9a-6a2285ecc9ee",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-04T23:44:05.03Z",
  "updated_at" : "2016-10-04T23:44:05.05Z",
  "payment_instrument" : null,
  "merchant" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIn62CaT8ypqK7r915P51G1F"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    }
  }
}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIn62CaT8ypqK7r915P51G1F",
  "external_trace_id" : "3c16bb72-8b6d-4f11-9e9a-6a2285ecc9ee",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-04T23:44:05.03Z",
  "updated_at" : "2016-10-04T23:44:05.05Z",
  "payment_instrument" : null,
  "merchant" : "MU44oTHgF4SpA6dTGc1m6eu7",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIn62CaT8ypqK7r915P51G1F"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
    }
  }
}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## List all Merchants
```shell
curl https://api-staging.simonpayments.com/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU44oTHgF4SpA6dTGc1m6eu7",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "verification" : null,
      "merchant_profile" : "MPovQP6nFotXCzStYYyQq1WD",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-10-04T23:43:26.16Z",
      "updated_at" : "2016-10-04T23:43:26.38Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.simonpayments.com/merchant_profiles/MPovQP6nFotXCzStYYyQq1WD"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/merchants/`

## List Merchant Verifications
```shell
curl https://api-staging.simonpayments.com/merchants/MU44oTHgF4SpA6dTGc1m6eu7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
      "entity" : {
        "title" : null,
        "first_name" : "Marcie",
        "last_name" : "Henderson",
        "email" : "therock@gmail.com",
        "business_name" : null,
        "business_type" : null,
        "doing_business_as" : null,
        "phone" : "7145677613",
        "business_phone" : null,
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "business_address" : null,
        "mcc" : null,
        "dob" : null,
        "max_transaction_amount" : 0,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:27.75Z",
      "updated_at" : "2016-10-04T23:43:27.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "ID582rm3UZiUXvvhTmhg5q5n",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "GOVERNMENT_AGENCY",
        "doing_business_as" : "Lees Sandwiches",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.LeesSandwiches.com",
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
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:22.77Z",
      "updated_at" : "2016-10-04T23:43:22.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID582rm3UZiUXvvhTmhg5q5n/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDcs2K61xEh6zz2QbFppswWo",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:21.73Z",
      "updated_at" : "2016-10-04T23:43:21.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcs2K61xEh6zz2QbFppswWo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDeAJMyBJCRVGuBopKaRB748",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:20.74Z",
      "updated_at" : "2016-10-04T23:43:20.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeAJMyBJCRVGuBopKaRB748/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDknUF3Lep3HLNCbwHASQfLP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:19.68Z",
      "updated_at" : "2016-10-04T23:43:19.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDknUF3Lep3HLNCbwHASQfLP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDrzf86q5Kr6DVuay3jzvf9v",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GENERAL_PARTNERSHIP",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:18.23Z",
      "updated_at" : "2016-10-04T23:43:18.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrzf86q5Kr6DVuay3jzvf9v/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDqe1H62ohL9z3zp9tC66YWs",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_PARTNERSHIP",
        "doing_business_as" : "Petes Coffee",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PetesCoffee.com",
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
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:16.91Z",
      "updated_at" : "2016-10-04T23:43:16.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDqe1H62ohL9z3zp9tC66YWs/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDNzj2WiJtSbzqCS7y1Lre7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "PARTNERSHIP",
        "doing_business_as" : "Prestige World Wide",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.PrestigeWorldWide.com",
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
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:15.58Z",
      "updated_at" : "2016-10-04T23:43:15.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDNzj2WiJtSbzqCS7y1Lre7/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDrdCzHjXTDrAMx6oQSRujXb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
      },
      "created_at" : "2016-10-04T23:43:14.11Z",
      "updated_at" : "2016-10-04T23:43:14.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDrdCzHjXTDrAMx6oQSRujXb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "ID6MzAm5hKno9t6yBvpk2gLR",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "CORPORATION",
        "doing_business_as" : "Lees Sandwiches",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.LeesSandwiches.com",
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
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:12.65Z",
      "updated_at" : "2016-10-04T23:43:12.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6MzAm5hKno9t6yBvpk2gLR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
        "doing_business_as" : "ACME Anchors",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
        "amex_mid" : "12345678910",
        "discover_mid" : null,
        "url" : "www.ACMEAnchors.com",
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
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-04T23:43:11.06Z",
      "updated_at" : "2016-10-04T23:43:11.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "IDt3i17wodcs2rjpLrYF653g",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Venmo",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Venmo",
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
        "mcc" : null,
        "dob" : {
          "day" : 27,
          "month" : 5,
          "year" : 1978
        },
        "max_transaction_amount" : 12000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-10-04T23:43:06.70Z",
      "updated_at" : "2016-10-04T23:43:06.76Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 12
  }
}
```

Retrieve all attempts to onboard (i.e. provision) a merchant onto a processor.

#### HTTP Request

`GET https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

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


curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "name": "Ricardo White", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4242424242424242", 
	    "expiration_month": 12, 
	    "address": {
	        "city": "San Mateo", 
	        "country": "USA", 
	        "region": "CA", 
	        "line2": "Apartment 7", 
	        "line1": "741 Douglass St", 
	        "postal_code": "94114"
	    }, 
	    "security_code": "112", 
	    "type": "PAYMENT_CARD", 
	    "identity": "IDcwkUSpMa4EQyjgDQ4YjP3q"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Ricardo White", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
	    "number"=> "4242424242424242", 
	    "expiration_month"=> 12, 
	    "address"=> array(
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    ), 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDcwkUSpMa4EQyjgDQ4YjP3q"
	));
$card = $card->save();


```
```java

import io.simonpay.payments.processing.client.model.PaymentCard;

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
{
  "id" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "fingerprint" : "FPR-657319974",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ricardo White",
  "address" : {
    "line1" : "741 Douglass St",
    "line2" : "Apartment 7",
    "city" : "San Mateo",
    "region" : "CA",
    "postal_code" : "94114",
    "country" : "USA"
  },
  "address_verification" : "UNKNOWN",
  "security_code_verification" : "UNKNOWN",
  "created_at" : "2016-10-04T23:43:28.85Z",
  "updated_at" : "2016-10-04T23:43:28.85Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/updates"
    }
  }
}
```

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Please review our guide on how to tokenize cards via the [embedded tokenization
form](#embedded-tokenization-using-iframe)

#### HTTP Request

`POST https://api-staging.simonpayments.com/payment_instruments`

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

curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "account_type": "SAVINGS", 
	    "name": "Fran Lemke", 
	    "tags": {
	        "Bank Account": "Company Account"
	    }, 
	    "country": "USA", 
	    "bank_code": "123123123", 
	    "account_number": "123123123", 
	    "type": "BANK_ACCOUNT", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> array(
	        "Bank Account"=> "Company Account"
	    ), 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDs3XCSAdBXoqMjtsTpMDrh5"
	));
$bank_account = $bank_account->save();


```
```java

import io.simonpay.payments.processing.client.model.BankAccount;

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
{
  "id" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T23:43:23.91Z",
  "updated_at" : "2016-10-04T23:43:23.91Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.simonpayments.com/payment_instruments`

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
of PCI scope by sending this info over SSL directly to SimonPay. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/rserna2010/1626475h/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the SimonPay API.
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
<script type="text/javascript" src="https://vgs-assets.s3.amazonaws.com/payline-1.latest.js"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: 'APdAAD1S6HYtHTVnrqFdPrsp',
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
{
  "id" : "TK6qtbPN4cUUXyy5wi2s6dqs",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-04T23:43:40.99Z",
  "updated_at" : "2016-10-04T23:43:40.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-05T23:43:40.99Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	});
$card = $card->save();

```
```java
import io.simonpay.payments.processing.client.model.PaymentCard;

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
{
  "id" : "PI6qtbPN4cUUXyy5wi2s6dqs",
  "fingerprint" : "FPR-1132692079",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : null,
  "address" : {
    "line1" : "741 Douglass St",
    "line2" : "Apartment 7",
    "city" : "San Mateo",
    "region" : "CA",
    "postal_code" : "94114",
    "country" : "USA"
  },
  "address_verification" : "UNKNOWN",
  "security_code_verification" : "UNKNOWN",
  "created_at" : "2016-10-04T23:43:41.84Z",
  "updated_at" : "2016-10-04T23:43:41.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/updates"
    }
  }
}
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

`POST https://api-staging.simonpayments.com/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK6qtbPN4cUUXyy5wi2s6dqs", 
	    "type": "TOKEN", 
	    "identity": "IDs3XCSAdBXoqMjtsTpMDrh5"
	});
$card = $card->save();

```
```java
import io.simonpay.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
> Example Response:

```json
{
  "id" : "PI6qtbPN4cUUXyy5wi2s6dqs",
  "fingerprint" : "FPR-1132692079",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : null,
  "address" : {
    "line1" : "741 Douglass St",
    "line2" : "Apartment 7",
    "city" : "San Mateo",
    "region" : "CA",
    "postal_code" : "94114",
    "country" : "USA"
  },
  "address_verification" : "UNKNOWN",
  "security_code_verification" : "UNKNOWN",
  "created_at" : "2016-10-04T23:43:41.84Z",
  "updated_at" : "2016-10-04T23:43:41.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/updates"
    }
  }
}
```

Associate the newly tokenized card or bank with the instrument owner's `Identity`.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated.
</aside>

#### HTTP Request

`POST https://api-staging.simonpayments.com/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Fetch a Payment Instrument

```shell


curl https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIq1dqfyMaezBaCGGwzWQmyB');

```
```java

import io.simonpay.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIq1dqfyMaezBaCGGwzWQmyB")

```
> Example Response:

```json
{
  "id" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T23:43:23.81Z",
  "updated_at" : "2016-10-04T23:43:25.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET https://api-staging.simonpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T23:43:23.81Z",
  "updated_at" : "2016-10-04T23:43:25.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

Update a previously created `Payment Instrument`.

<aside class="notice">
Only the tags field can be updated. If it is required to update other fields,
such as account information or expiration dates please retokenize the payment
instrument.
</aside>

#### HTTP Request

`PUT https://api-staging.simonpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
import io.simonpay.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI6qtbPN4cUUXyy5wi2s6dqs",
      "fingerprint" : "FPR-1132692079",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : null,
      "address" : {
        "line1" : "741 Douglass St",
        "line2" : "Apartment 7",
        "city" : "San Mateo",
        "region" : "CA",
        "postal_code" : "94114",
        "country" : "USA"
      },
      "address_verification" : "UNKNOWN",
      "security_code_verification" : "UNKNOWN",
      "created_at" : "2016-10-04T23:43:41.71Z",
      "updated_at" : "2016-10-04T23:43:41.71Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI6qtbPN4cUUXyy5wi2s6dqs/updates"
        }
      }
    }, {
      "id" : "PIkpHPDjN9dgWn3Qe2vtNbW",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-04T23:43:29.66Z",
      "updated_at" : "2016-10-04T23:43:29.66Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIkpHPDjN9dgWn3Qe2vtNbW"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIkpHPDjN9dgWn3Qe2vtNbW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIkpHPDjN9dgWn3Qe2vtNbW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIkpHPDjN9dgWn3Qe2vtNbW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "fingerprint" : "FPR-657319974",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Ricardo White",
      "address" : {
        "line1" : "741 Douglass St",
        "line2" : "Apartment 7",
        "city" : "San Mateo",
        "region" : "CA",
        "postal_code" : "94114",
        "country" : "USA"
      },
      "address_verification" : "POSTAL_CODE_AND_STREET_MATCH",
      "security_code_verification" : "MATCHED",
      "created_at" : "2016-10-04T23:43:28.77Z",
      "updated_at" : "2016-10-04T23:43:37.64Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDcwkUSpMa4EQyjgDQ4YjP3q",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDcwkUSpMa4EQyjgDQ4YjP3q"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj/updates"
        }
      }
    }, {
      "id" : "PInQqESDuQkLQ3TwrcJH166t",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:26.16Z",
      "updated_at" : "2016-10-04T23:43:26.16Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIbMVsgFAfDi8pqJghnzd4o",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:26.16Z",
      "updated_at" : "2016-10-04T23:43:26.16Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbMVsgFAfDi8pqJghnzd4o"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbMVsgFAfDi8pqJghnzd4o/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbMVsgFAfDi8pqJghnzd4o/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbMVsgFAfDi8pqJghnzd4o/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PI4BEPvWyuB7X1hw2KnPiihb",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:26.16Z",
      "updated_at" : "2016-10-04T23:43:26.16Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4BEPvWyuB7X1hw2KnPiihb"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4BEPvWyuB7X1hw2KnPiihb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4BEPvWyuB7X1hw2KnPiihb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4BEPvWyuB7X1hw2KnPiihb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIq1dqfyMaezBaCGGwzWQmyB",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-04T23:43:23.81Z",
      "updated_at" : "2016-10-04T23:43:25.07Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIfejCmYCnavDjL6Tg3RpxM",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:07.35Z",
      "updated_at" : "2016-10-04T23:43:07.35Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2f67hZpBDEM1xBfKSp7LPD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIfejCmYCnavDjL6Tg3RpxM"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIfejCmYCnavDjL6Tg3RpxM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2f67hZpBDEM1xBfKSp7LPD"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIfejCmYCnavDjL6Tg3RpxM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIfejCmYCnavDjL6Tg3RpxM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIgw6PwPGBvvxdhaGxs7gnNs",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:07.35Z",
      "updated_at" : "2016-10-04T23:43:07.35Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDt3i17wodcs2rjpLrYF653g",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgw6PwPGBvvxdhaGxs7gnNs"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgw6PwPGBvvxdhaGxs7gnNs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgw6PwPGBvvxdhaGxs7gnNs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgw6PwPGBvvxdhaGxs7gnNs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PIwSL7c1igqnU7PKeSb6aswK",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:07.35Z",
      "updated_at" : "2016-10-04T23:43:07.35Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDt3i17wodcs2rjpLrYF653g",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwSL7c1igqnU7PKeSb6aswK"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwSL7c1igqnU7PKeSb6aswK/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwSL7c1igqnU7PKeSb6aswK/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwSL7c1igqnU7PKeSb6aswK/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    }, {
      "id" : "PI56eKDaQWQf6LvidJtBg9Nu",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T23:43:07.35Z",
      "updated_at" : "2016-10-04T23:43:07.35Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDt3i17wodcs2rjpLrYF653g",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI56eKDaQWQf6LvidJtBg9Nu"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI56eKDaQWQf6LvidJtBg9Nu/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDt3i17wodcs2rjpLrYF653g"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI56eKDaQWQf6LvidJtBg9Nu/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI56eKDaQWQf6LvidJtBg9Nu/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 11
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/payment_instruments`

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;
use SimonPay\Resources\Settlement;

$identity = Identity::retrieve('IDs3XCSAdBXoqMjtsTpMDrh5');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```java

import io.simonpay.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STvq7bQrBSqa8fPzXobfHa84",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "currency" : "USD",
  "created_at" : "2016-10-04T23:50:46.63Z",
  "updated_at" : "2016-10-04T23:50:46.78Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 434885,
  "total_fee" : 43490,
  "net_amount" : 391395,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
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
request to the transfers link (i.e. POST https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/settlements`

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


curl https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Settlement;

$settlement = Settlement::retrieve('STvq7bQrBSqa8fPzXobfHa84');

```
```java

import io.simonpay.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STvq7bQrBSqa8fPzXobfHa84");

```
> Example Response:

```json
{
  "id" : "STvq7bQrBSqa8fPzXobfHa84",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "currency" : "USD",
  "created_at" : "2016-10-04T23:50:46.49Z",
  "updated_at" : "2016-10-04T23:50:48.44Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 434885,
  "total_fee" : 43490,
  "net_amount" : 391395,
  "destination" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkq2yiDni9oFNpcuRNDMPmA:b559b81b-5b6e-4e22-aba5-81fd12265314 \
    -X PUT \
    -d '
	{
	    "destination": "PIq1dqfyMaezBaCGGwzWQmyB"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "STvq7bQrBSqa8fPzXobfHa84",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "currency" : "USD",
  "created_at" : "2016-10-04T23:50:46.49Z",
  "updated_at" : "2016-10-04T23:50:48.44Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 434885,
  "total_fee" : 43490,
  "net_amount" : 391395,
  "destination" : "PIq1dqfyMaezBaCGGwzWQmyB",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    }
  }
}
```

Issue funding instructions to pay out funds that are allocated in a previously
 created batch `Settlement` resource for a merchant.

<aside class="warning">
Once instructions have been issued to a particular destination it cannot be
updated.
</aside>


#### HTTP Request

`POST https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID`

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
curl https://api-staging.simonpayments.com/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


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
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STvq7bQrBSqa8fPzXobfHa84",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "currency" : "USD",
      "created_at" : "2016-10-04T23:50:46.49Z",
      "updated_at" : "2016-10-04T23:50:48.44Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 434885,
      "total_fee" : 43490,
      "net_amount" : 391395,
      "destination" : "PIq1dqfyMaezBaCGGwzWQmyB",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
  }
}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


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
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRf9YEPHEHQRNZEjtHE373Ej",
      "amount" : 89,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "24aab36c-7ac8-411f-bb31-d26feb255357",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PInQqESDuQkLQ3TwrcJH166t",
      "destination" : "PIq1dqfyMaezBaCGGwzWQmyB",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:50:48.06Z",
      "updated_at" : "2016-10-04T23:51:01.78Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRf9YEPHEHQRNZEjtHE373Ej"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRf9YEPHEHQRNZEjtHE373Ej/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRf9YEPHEHQRNZEjtHE373Ej/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRf9YEPHEHQRNZEjtHE373Ej/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
        }
      }
    }, {
      "id" : "TRdTYRARubSA1NuNGdLArf4K",
      "amount" : 391306,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "f261e85a-0699-4bb2-a6db-09a209bb159a",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PInQqESDuQkLQ3TwrcJH166t",
      "destination" : "PIq1dqfyMaezBaCGGwzWQmyB",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:50:48.06Z",
      "updated_at" : "2016-10-04T23:51:01.37Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRdTYRARubSA1NuNGdLArf4K"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRdTYRARubSA1NuNGdLArf4K/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRdTYRARubSA1NuNGdLArf4K/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRdTYRARubSA1NuNGdLArf4K/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIq1dqfyMaezBaCGGwzWQmyB"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/funding_transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 2
  }
}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "destination" : "PInQqESDuQkLQ3TwrcJH166t",
      "ready_to_settle_at" : "2016-10-04T23:46:35.29Z",
      "fee" : 10,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:38.71Z",
      "updated_at" : "2016-10-04T23:44:01.21Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        }
      }
    }, {
      "id" : "TRnHSdBJQtdwZSoBmVqLgRjA",
      "amount" : 434785,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "bd61c954-7825-4bd4-a6f4-58f9119ac522",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "destination" : "PInQqESDuQkLQ3TwrcJH166t",
      "ready_to_settle_at" : "2016-10-04T23:46:35.29Z",
      "fee" : 43479,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:30.97Z",
      "updated_at" : "2016-10-04T23:44:04.79Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/settlements/STvq7bQrBSqa8fPzXobfHa84/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 2
  }
}
```

List the batch of `Transfers` of type `DEBIT` and `REFUND` that comprise the net
 settled amount of a `Settlement`.

#### HTTP Request

`GET https://api-staging.simonpayments.com/settlements/:SETTLEMENT_ID/transfers`


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

curl https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Transfer;

$transfer = Transfer::retrieve('TRnHSdBJQtdwZSoBmVqLgRjA');



```
```java

import io.simonpay.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRnHSdBJQtdwZSoBmVqLgRjA");

```
> Example Response:

```json
{
  "id" : "TRnHSdBJQtdwZSoBmVqLgRjA",
  "amount" : 434785,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "bd61c954-7825-4bd4-a6f4-58f9119ac522",
  "currency" : "USD",
  "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
  "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "destination" : "PInQqESDuQkLQ3TwrcJH166t",
  "ready_to_settle_at" : null,
  "fee" : 43479,
  "statement_descriptor" : "SPN*ACME ANCHORS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:30.97Z",
  "updated_at" : "2016-10-04T23:43:31.27Z",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/disputes"
    },
    "source" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Transfer;

$debit = Transfer::retrieve('TRnHSdBJQtdwZSoBmVqLgRjA');
$refund = $debit->reverse(50);
```
```java

import io.simonpay.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRsFK6nU6xUKnvGQ6HqBN3T6",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "442f1a46-8119-48df-bdc5-500ad5ec2a55",
  "currency" : "USD",
  "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
  "source" : "PInQqESDuQkLQ3TwrcJH166t",
  "destination" : "PIsWAgCjqrgp7w2eP4vP7uWj",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "SPN*ACME ANCHORS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T23:43:35.91Z",
  "updated_at" : "2016-10-04T23:43:36.04Z",
  "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRsFK6nU6xUKnvGQ6HqBN3T6"
    },
    "parent" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRsFK6nU6xUKnvGQ6HqBN3T6/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://api-staging.simonpayments.com/transfers/:TRANSFER_ID/reversals`

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
curl https://api-staging.simonpayments.com/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
import io.simonpay.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR2DdZMC9Tsj9WZyS2T1BaxR",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "86c29f52-b157-48da-a165-7b8fea7be2f4",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "destination" : "PInQqESDuQkLQ3TwrcJH166t",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:38.71Z",
      "updated_at" : "2016-10-04T23:43:38.99Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2DdZMC9Tsj9WZyS2T1BaxR/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        }
      }
    }, {
      "id" : "TRsFK6nU6xUKnvGQ6HqBN3T6",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "442f1a46-8119-48df-bdc5-500ad5ec2a55",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PInQqESDuQkLQ3TwrcJH166t",
      "destination" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:35.74Z",
      "updated_at" : "2016-10-04T23:43:36.04Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsFK6nU6xUKnvGQ6HqBN3T6"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsFK6nU6xUKnvGQ6HqBN3T6/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "parent" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        }
      }
    }, {
      "id" : "TR6kHzVAEsr2385j2mrRhjiz",
      "amount" : 648873,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "f1e430ed-8e4b-4e03-8eee-92163e4f458e",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PIkpHPDjN9dgWn3Qe2vtNbW",
      "destination" : "PInQqESDuQkLQ3TwrcJH166t",
      "ready_to_settle_at" : null,
      "fee" : 64887,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:32.52Z",
      "updated_at" : "2016-10-04T23:43:32.80Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6kHzVAEsr2385j2mrRhjiz"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6kHzVAEsr2385j2mrRhjiz/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6kHzVAEsr2385j2mrRhjiz/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6kHzVAEsr2385j2mrRhjiz/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIkpHPDjN9dgWn3Qe2vtNbW"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        }
      }
    }, {
      "id" : "TRnHSdBJQtdwZSoBmVqLgRjA",
      "amount" : 434785,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "bd61c954-7825-4bd4-a6f4-58f9119ac522",
      "currency" : "USD",
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "source" : "PIsWAgCjqrgp7w2eP4vP7uWj",
      "destination" : "PInQqESDuQkLQ3TwrcJH166t",
      "ready_to_settle_at" : null,
      "fee" : 43479,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T23:43:30.97Z",
      "updated_at" : "2016-10-04T23:43:31.27Z",
      "merchant_identity" : "IDs3XCSAdBXoqMjtsTpMDrh5",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDs3XCSAdBXoqMjtsTpMDrh5"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRnHSdBJQtdwZSoBmVqLgRjA/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsWAgCjqrgp7w2eP4vP7uWj"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInQqESDuQkLQ3TwrcJH166t"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 4
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/transfers`
# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the SimonPay API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://api-staging.simonpayments.com/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092 \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.simonpay.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHbWPqwbEksFgcb5XF3FGKSZ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
  "created_at" : "2016-10-04T23:43:09.93Z",
  "updated_at" : "2016-10-04T23:43:09.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WHbWPqwbEksFgcb5XF3FGKSZ"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.simonpayments.com/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

## Retrieve a Webhook

```shell



curl https://api-staging.simonpayments.com/webhooks/WHbWPqwbEksFgcb5XF3FGKSZ \
    -H "Content-Type: application/vnd.json+api" \
    -u USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Webhook;

$webhook = Webhook::retrieve('WHbWPqwbEksFgcb5XF3FGKSZ');



```
```java

import io.simonpay.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHbWPqwbEksFgcb5XF3FGKSZ");

```
> Example Response:

```json
{
  "id" : "WHbWPqwbEksFgcb5XF3FGKSZ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
  "created_at" : "2016-10-04T23:43:09.93Z",
  "updated_at" : "2016-10-04T23:43:09.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WHbWPqwbEksFgcb5XF3FGKSZ"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://api-staging.simonpayments.com/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USubGCBT17WgSQ6muYS4fxpu:3123fde8-58cc-4620-99a2-e24b073e4092

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
import io.simonpay.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHbWPqwbEksFgcb5XF3FGKSZ",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APdAAD1S6HYtHTVnrqFdPrsp",
      "created_at" : "2016-10-04T23:43:09.93Z",
      "updated_at" : "2016-10-04T23:43:09.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/webhooks/WHbWPqwbEksFgcb5XF3FGKSZ"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APdAAD1S6HYtHTVnrqFdPrsp"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/webhooks`
    

## Sample Payloads


```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://api-staging.simonpayments.com', 'USubGCBT17WgSQ6muYS4fxpu', '3123fde8-58cc-4620-99a2-e24b073e4092');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

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
