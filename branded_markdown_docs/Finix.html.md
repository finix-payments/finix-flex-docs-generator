---
title: Finix API Reference

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

These guides provide a collection of resources for utilizing the Finix
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
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
	        "default_statement_descriptor": "Bobs Burgers", 
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
	        "doing_business_as": "Bobs Burgers", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Bobs Burgers", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.BobsBurgers.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

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
	        "default_statement_descriptor"=> "Bobs Burgers", 
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
	        "doing_business_as"=> "Bobs Burgers", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Bobs Burgers", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.BobsBurgers.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java
import io.finix.payments.processing.client.model.Identity;

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
  "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-05T23:52:55.93Z",
  "updated_at" : "2016-10-05T23:52:55.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://api-staging.finix.io/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://api-staging.finix.io/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://api-staging.finix.io/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-staging.finix.io/identities`

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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

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
	    "identity"=> "IDoVSH2TYLRBe7d9pprcgMLd"
	));
$bank_account = $bank_account->save();

```
```java
import io.finix.payments.processing.client.model.BankAccount;

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
  "id" : "PItTHbUEVodMPoibEbiiHPqS",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-05T23:53:06.06Z",
  "updated_at" : "2016-10-05T23:53:06.06Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`POST https://api-staging.finix.io/payment_instruments`

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
curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "verification" : "VIgFoNUQ1mKYyrxxLN3gQgvo",
  "merchant_profile" : "MP8oXVuGMCg65WBdMj5smEEE",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-05T23:53:08.21Z",
  "updated_at" : "2016-10-05T23:53:08.21Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8oXVuGMCg65WBdMj5smEEE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIgFoNUQ1mKYyrxxLN3gQgvo"
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

`POST https://api-staging.finix.io/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
	        "last_name": "Curry", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jessie", 
	        "last_name"=> "Curry", 
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

import io.finix.payments.processing.client.model.Identity;

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
  "id" : "ID2xpWjexhTZxLo8zamyUkdH",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
    "last_name" : "Curry",
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
  "created_at" : "2016-10-05T23:53:09.98Z",
  "updated_at" : "2016-10-05T23:53:09.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`POST https://api-staging.finix.io/identities`

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


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "name": "Daphne Diaz", 
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
	    "identity": "ID2xpWjexhTZxLo8zamyUkdH"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Daphne Diaz", 
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
	    "identity"=> "ID2xpWjexhTZxLo8zamyUkdH"
	));
$card = $card->save();


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
  "id" : "PItxT8YNpKC95GNvayrbzWq7",
  "fingerprint" : "FPR-1045815956",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Daphne Diaz",
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
  "created_at" : "2016-10-05T23:53:10.96Z",
  "updated_at" : "2016-10-05T23:53:10.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2xpWjexhTZxLo8zamyUkdH",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/updates"
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

`POST https://api-staging.finix.io/payment_instruments`

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
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "merchant_identity": "IDoVSH2TYLRBe7d9pprcgMLd", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItxT8YNpKC95GNvayrbzWq7", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDoVSH2TYLRBe7d9pprcgMLd", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItxT8YNpKC95GNvayrbzWq7", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```java
import io.finix.payments.processing.client.model.Authorization;

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
  "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:20.84Z",
  "updated_at" : "2016-10-05T23:53:20.85Z",
  "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : false,
  "expires_at" : "2016-10-12T23:53:20.84Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`POST https://api-staging.finix.io/authorizations`

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
curl https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUwcCYUrL9k3LhPJ48Yyfz5s');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUwcCYUrL9k3LhPJ48Yyfz5s");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7tKQZ7Uooeu17DwSe35Sfj",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:20.71Z",
  "updated_at" : "2016-10-05T23:53:22.28Z",
  "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : false,
  "expires_at" : "2016-10-12T23:53:20.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`PUT https://api-staging.finix.io/authorizations/:AUTHORIZATION_ID`

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
curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');
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
import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "ST27ub5j8TQTozuoVjGU58Cy",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "currency" : "USD",
  "created_at" : "2016-10-06T00:00:38.73Z",
  "updated_at" : "2016-10-06T00:00:38.74Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 732984,
  "total_fee" : 73299,
  "net_amount" : 659685,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`POST https://api-staging.finix.io/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Embedded Tokenization Using Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to Finix. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the Finix API.
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
          applicationId: 'APg1ojcH1J1we1MFvnRc6P97',
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
  "id" : "TKr7JgwX7ekxxBwM1pRMrPGb",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-05T23:53:24.47Z",
  "updated_at" : "2016-10-05T23:53:24.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-06T23:53:24.47Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	});
$card = $card->save();

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
  "id" : "PIr7JgwX7ekxxBwM1pRMrPGb",
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
  "created_at" : "2016-10-05T23:53:25.47Z",
  "updated_at" : "2016-10-05T23:53:25.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/updates"
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

`POST https://api-staging.finix.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Push-to-Card [PRIVATE BETA]
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marshall", 
	        "last_name": "Green", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDkjVEbLenpKNEgermBj7cGF",
  "entity" : {
    "title" : null,
    "first_name" : "Marshall",
    "last_name" : "Green",
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
  "created_at" : "2016-10-05T23:53:36.92Z",
  "updated_at" : "2016-10-05T23:53:36.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

Use the resulting ID of the newly created Identity to associate any transfers or payment instruments that are used. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds.

#### HTTP Request

`POST https://api-staging.finix.io/identities`

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

### Step 2:  Add a Payment Instrument

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "name": "Jim Jones", 
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
	    "identity": "IDkjVEbLenpKNEgermBj7cGF"
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USupdQBdHKc58rBx1urfeXfg", 
	    "entity"=> array(
	        "business_type"=> "LIMITED_LIABILITY_COMPANY", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 5
	        ), 
	        "settlement_bank_account"=> "CORPORATE", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 12000, 
	        "phone"=> "1234567890", 
	        "doing_business_as"=> "Facebook", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Facebook", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```java

```
> Example Response:

```json
{
  "id" : "PI932yvKVJUuQBFipQsazUEq",
  "fingerprint" : "FPR1459643778",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jim Jones",
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
  "created_at" : "2016-10-05T23:53:38.83Z",
  "updated_at" : "2016-10-05T23:53:38.83Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkjVEbLenpKNEgermBj7cGF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/updates"
    }
  }
}
```

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Again, keep track of the ID of the newly created payment instrument. This is used to determine the destination of funds when sending money.

#### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`

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

### Step 3: Send Money to Recipient

Once you have tokenized the payment card as above you can send funds to it at any time by simply calling the API


```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDkjVEbLenpKNEgermBj7cGF", 
	    "destination": "PI932yvKVJUuQBFipQsazUEq", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USupdQBdHKc58rBx1urfeXfg", 
	    "entity"=> array(
	        "business_type"=> "LIMITED_LIABILITY_COMPANY", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 5
	        ), 
	        "settlement_bank_account"=> "CORPORATE", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 12000, 
	        "phone"=> "1234567890", 
	        "doing_business_as"=> "Facebook", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Facebook", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```java

```
> Example Response:

```json
{
  "id" : "TR5vKixEBego7wJkSsUYEbq9",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "FAILED",
  "trace_id" : "1024",
  "currency" : "USD",
  "application" : "APg1ojcH1J1we1MFvnRc6P97",
  "source" : "PI2FrLrvtFCenshjv9rBwzMp",
  "destination" : "PI932yvKVJUuQBFipQsazUEq",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:40.27Z",
  "updated_at" : "2016-10-05T23:53:40.99Z",
  "merchant_identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq"
    }
  }
}
```

Now that we have a new owner `User` let's create their `Application`. We'll be
collecting the same basic KYC and underwrting information that we typically
collect for provisioning a merchant account. You'll also be taking the ID for the
`User` that you created in the previous step and passing it in the `user` field.

#### HTTP Request

`POST https://api-staging.finix.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where funds will be sent
merchant_identity | *string*, **required** | `Identity` ID of the recipient of whom you're sending the money to
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "merchant_identity": "IDoVSH2TYLRBe7d9pprcgMLd", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItxT8YNpKC95GNvayrbzWq7", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDoVSH2TYLRBe7d9pprcgMLd", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItxT8YNpKC95GNvayrbzWq7", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```java
import io.finix.payments.processing.client.model.Authorization;

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
  "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:20.84Z",
  "updated_at" : "2016-10-05T23:53:20.85Z",
  "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : false,
  "expires_at" : "2016-10-12T23:53:20.84Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`POST https://api-staging.finix.io/authorizations`

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
curl https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUwcCYUrL9k3LhPJ48Yyfz5s');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUwcCYUrL9k3LhPJ48Yyfz5s");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7tKQZ7Uooeu17DwSe35Sfj",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:20.71Z",
  "updated_at" : "2016-10-05T23:53:22.28Z",
  "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : false,
  "expires_at" : "2016-10-12T23:53:20.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`PUT https://api-staging.finix.io/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.finix.io/authorizations/AUnjKrmjD59EStBKfEtkrihJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUnjKrmjD59EStBKfEtkrihJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:26.70Z",
  "updated_at" : "2016-10-05T23:53:27.99Z",
  "trace_id" : "bea3f644-abce-412f-8fc8-339c33770cb4",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : true,
  "expires_at" : "2016-10-12T23:53:26.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnjKrmjD59EStBKfEtkrihJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://api-staging.finix.io/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUwcCYUrL9k3LhPJ48Yyfz5s');

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUwcCYUrL9k3LhPJ48Yyfz5s");

```
> Example Response:

```json
{
  "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7tKQZ7Uooeu17DwSe35Sfj",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:20.71Z",
  "updated_at" : "2016-10-05T23:53:22.28Z",
  "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "is_void" : false,
  "expires_at" : "2016-10-12T23:53:20.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://api-staging.finix.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


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
      "id" : "AUnjKrmjD59EStBKfEtkrihJ",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:26.70Z",
      "updated_at" : "2016-10-05T23:53:27.99Z",
      "trace_id" : "bea3f644-abce-412f-8fc8-339c33770cb4",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "is_void" : true,
      "expires_at" : "2016-10-12T23:53:26.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUnjKrmjD59EStBKfEtkrihJ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        }
      }
    }, {
      "id" : "AUwcCYUrL9k3LhPJ48Yyfz5s",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR7tKQZ7Uooeu17DwSe35Sfj",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:20.71Z",
      "updated_at" : "2016-10-05T23:53:22.28Z",
      "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "is_void" : false,
      "expires_at" : "2016-10-12T23:53:20.71Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUwcCYUrL9k3LhPJ48Yyfz5s"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/authorizations/`

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


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
	        "last_name": "Curry", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jessie", 
	        "last_name"=> "Curry", 
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

import io.finix.payments.processing.client.model.Identity;

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
  "id" : "ID2xpWjexhTZxLo8zamyUkdH",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
    "last_name" : "Curry",
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
  "created_at" : "2016-10-05T23:53:09.98Z",
  "updated_at" : "2016-10-05T23:53:09.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://api-staging.finix.io/identities`

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


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
	        "default_statement_descriptor": "Bobs Burgers", 
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
	        "doing_business_as": "Bobs Burgers", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Bobs Burgers", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.BobsBurgers.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

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
	        "default_statement_descriptor"=> "Bobs Burgers", 
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
	        "doing_business_as"=> "Bobs Burgers", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Bobs Burgers", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.BobsBurgers.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java

import io.finix.payments.processing.client.model.Identity;

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
  "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-05T23:52:55.93Z",
  "updated_at" : "2016-10-05T23:52:55.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`POST https://api-staging.finix.io/identities`

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

curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');
```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDoVSH2TYLRBe7d9pprcgMLd");

```
> Example Response:

```json
{
  "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-05T23:52:55.87Z",
  "updated_at" : "2016-10-05T23:52:55.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java
import io.finix.payments.processing.client.model.Identity;

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
      "id" : "IDkjVEbLenpKNEgermBj7cGF",
      "entity" : {
        "title" : null,
        "first_name" : "Marshall",
        "last_name" : "Green",
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
      "created_at" : "2016-10-05T23:53:36.86Z",
      "updated_at" : "2016-10-05T23:53:36.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "ID2xpWjexhTZxLo8zamyUkdH",
      "entity" : {
        "title" : null,
        "first_name" : "Jessie",
        "last_name" : "Curry",
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
      "created_at" : "2016-10-05T23:53:09.92Z",
      "updated_at" : "2016-10-05T23:53:09.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDdi6DCuCrUn1Ntg8CuD3EYN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-10-05T23:53:05.00Z",
      "updated_at" : "2016-10-05T23:53:05.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDjG57uAUkTGrqLA5x7U3U43",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-05T23:53:04.05Z",
      "updated_at" : "2016-10-05T23:53:04.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDjVA65Mqy5PBPMxs2MB1C1Y",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-05T23:53:03.16Z",
      "updated_at" : "2016-10-05T23:53:03.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDaPQNwdBLF9atgavB4Zcwyj",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
        "doing_business_as" : "Dunder Mifflin",
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
        "url" : "www.DunderMifflin.com",
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
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-05T23:53:02.06Z",
      "updated_at" : "2016-10-05T23:53:02.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDwgHdUVQWPBDVDYmHWUsiif",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:53:01.10Z",
      "updated_at" : "2016-10-05T23:53:01.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDrz4xoDuYdA3kPqAP9mbHeS",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:53:00.21Z",
      "updated_at" : "2016-10-05T23:53:00.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "ID34pVDvbmBpbEpWryvvW69u",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:52:59.07Z",
      "updated_at" : "2016-10-05T23:52:59.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDqGS2ryygFeQGNkC7VqeTVb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-10-05T23:52:58.21Z",
      "updated_at" : "2016-10-05T23:52:58.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDdAosA1qCpaQg2e14vSnZPa",
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
      "created_at" : "2016-10-05T23:52:57.32Z",
      "updated_at" : "2016-10-05T23:52:57.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-10-05T23:52:55.87Z",
      "updated_at" : "2016-10-05T23:52:55.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Facebook",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Facebook",
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
        "application_name" : "Facebook"
      },
      "created_at" : "2016-10-05T23:52:49.36Z",
      "updated_at" : "2016-10-05T23:52:49.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 13
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/identities/`


## Update an Identity
```shell
curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Alex", 
	        "last_name": "Jones", 
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
	        "doing_business_as": "Bobs Burgers", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Bobs Burgers", 
	        "url": "www.BobsBurgers.com", 
	        "business_name": "Bobs Burgers", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Alex",
    "last_name" : "Jones",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Bobs Burgers",
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
    "key" : "value_2"
  },
  "created_at" : "2016-10-05T23:52:55.87Z",
  "updated_at" : "2016-10-05T23:53:55.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`POST https://api-staging.finix.io/identities`

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

curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);
```
```java

import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```

> Example Response:

```json
{
  "id" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "verification" : "VIgFoNUQ1mKYyrxxLN3gQgvo",
  "merchant_profile" : "MP8oXVuGMCg65WBdMj5smEEE",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-05T23:53:08.21Z",
  "updated_at" : "2016-10-05T23:53:08.21Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8oXVuGMCg65WBdMj5smEEE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIgFoNUQ1mKYyrxxLN3gQgvo"
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

`POST https://api-staging.finix.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "verification" : "VIgFoNUQ1mKYyrxxLN3gQgvo",
  "merchant_profile" : "MP8oXVuGMCg65WBdMj5smEEE",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-05T23:53:08.21Z",
  "updated_at" : "2016-10-05T23:53:08.21Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8oXVuGMCg65WBdMj5smEEE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIgFoNUQ1mKYyrxxLN3gQgvo"
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

`POST https://api-staging.finix.io/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Retrieve a Merchant
```shell
curl https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUpJdkX59UFaE13BoQBjYsH1');

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUpJdkX59UFaE13BoQBjYsH1");

```
> Example Response:

```json
{
  "id" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "verification" : null,
  "merchant_profile" : "MP8oXVuGMCg65WBdMj5smEEE",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-05T23:53:08.11Z",
  "updated_at" : "2016-10-05T23:53:08.31Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8oXVuGMCg65WBdMj5smEEE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Create a Merchant User
```shell
curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USoBeyq8f6mHYfCf8ehqPJJA",
  "password" : "149d8ca3-e3b3-4579-87c9-6ba5c129392b",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-05T23:53:16.73Z",
  "updated_at" : "2016-10-05T23:53:16.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USoBeyq8f6mHYfCf8ehqPJJA"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`POST https://api-staging.finix.io/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`


## Reattempt Merchant Provisioning
```shell
curl https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VI8w3sPUXGSQDFdyTACgCJwU",
  "external_trace_id" : "767d67a6-c967-41b0-a4c4-cee464e19fed",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-05T23:53:57.61Z",
  "updated_at" : "2016-10-05T23:53:57.63Z",
  "payment_instrument" : null,
  "merchant" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI8w3sPUXGSQDFdyTACgCJwU"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    }
  }
}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST https://api-staging.finix.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VI8w3sPUXGSQDFdyTACgCJwU",
  "external_trace_id" : "767d67a6-c967-41b0-a4c4-cee464e19fed",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-05T23:53:57.61Z",
  "updated_at" : "2016-10-05T23:53:57.63Z",
  "payment_instrument" : null,
  "merchant" : "MUpJdkX59UFaE13BoQBjYsH1",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI8w3sPUXGSQDFdyTACgCJwU"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
    }
  }
}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST https://api-staging.finix.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## List all Merchants
```shell
curl https://api-staging.finix.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUpJdkX59UFaE13BoQBjYsH1",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "verification" : null,
      "merchant_profile" : "MP8oXVuGMCg65WBdMj5smEEE",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-10-05T23:53:08.11Z",
      "updated_at" : "2016-10-05T23:53:08.31Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MP8oXVuGMCg65WBdMj5smEEE"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/merchants/`

## List Merchant Verifications
```shell
curl https://api-staging.finix.io/merchants/MUpJdkX59UFaE13BoQBjYsH1/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDkjVEbLenpKNEgermBj7cGF",
      "entity" : {
        "title" : null,
        "first_name" : "Marshall",
        "last_name" : "Green",
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
      "created_at" : "2016-10-05T23:53:36.86Z",
      "updated_at" : "2016-10-05T23:53:36.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "ID2xpWjexhTZxLo8zamyUkdH",
      "entity" : {
        "title" : null,
        "first_name" : "Jessie",
        "last_name" : "Curry",
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
      "created_at" : "2016-10-05T23:53:09.92Z",
      "updated_at" : "2016-10-05T23:53:09.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDdi6DCuCrUn1Ntg8CuD3EYN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-10-05T23:53:05.00Z",
      "updated_at" : "2016-10-05T23:53:05.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdi6DCuCrUn1Ntg8CuD3EYN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDjG57uAUkTGrqLA5x7U3U43",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-05T23:53:04.05Z",
      "updated_at" : "2016-10-05T23:53:04.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjG57uAUkTGrqLA5x7U3U43/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDjVA65Mqy5PBPMxs2MB1C1Y",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-05T23:53:03.16Z",
      "updated_at" : "2016-10-05T23:53:03.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjVA65Mqy5PBPMxs2MB1C1Y/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDaPQNwdBLF9atgavB4Zcwyj",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
        "doing_business_as" : "Dunder Mifflin",
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
        "url" : "www.DunderMifflin.com",
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
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-05T23:53:02.06Z",
      "updated_at" : "2016-10-05T23:53:02.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaPQNwdBLF9atgavB4Zcwyj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDwgHdUVQWPBDVDYmHWUsiif",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:53:01.10Z",
      "updated_at" : "2016-10-05T23:53:01.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwgHdUVQWPBDVDYmHWUsiif/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDrz4xoDuYdA3kPqAP9mbHeS",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:53:00.21Z",
      "updated_at" : "2016-10-05T23:53:00.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrz4xoDuYdA3kPqAP9mbHeS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "ID34pVDvbmBpbEpWryvvW69u",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-05T23:52:59.07Z",
      "updated_at" : "2016-10-05T23:52:59.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID34pVDvbmBpbEpWryvvW69u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDqGS2ryygFeQGNkC7VqeTVb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-10-05T23:52:58.21Z",
      "updated_at" : "2016-10-05T23:52:58.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqGS2ryygFeQGNkC7VqeTVb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDdAosA1qCpaQg2e14vSnZPa",
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
      "created_at" : "2016-10-05T23:52:57.32Z",
      "updated_at" : "2016-10-05T23:52:57.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdAosA1qCpaQg2e14vSnZPa/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-10-05T23:52:55.87Z",
      "updated_at" : "2016-10-05T23:52:55.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Facebook",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Facebook",
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
        "application_name" : "Facebook"
      },
      "created_at" : "2016-10-05T23:52:49.36Z",
      "updated_at" : "2016-10-05T23:52:49.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 13
  }
}
```

Retrieve all attempts to onboard (i.e. provision) a merchant onto a processor.

#### HTTP Request

`GET https://api-staging.finix.io/merchants/:MERCHANT_ID/verifications`

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


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "name": "Daphne Diaz", 
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
	    "identity": "ID2xpWjexhTZxLo8zamyUkdH"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Daphne Diaz", 
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
	    "identity"=> "ID2xpWjexhTZxLo8zamyUkdH"
	));
$card = $card->save();


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
  "id" : "PItxT8YNpKC95GNvayrbzWq7",
  "fingerprint" : "FPR-1045815956",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Daphne Diaz",
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
  "created_at" : "2016-10-05T23:53:10.96Z",
  "updated_at" : "2016-10-05T23:53:10.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2xpWjexhTZxLo8zamyUkdH",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/updates"
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

`POST https://api-staging.finix.io/payment_instruments`

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

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

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
	    "identity"=> "IDoVSH2TYLRBe7d9pprcgMLd"
	));
$bank_account = $bank_account->save();


```
```java

import io.finix.payments.processing.client.model.BankAccount;

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
  "id" : "PItTHbUEVodMPoibEbiiHPqS",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-05T23:53:06.06Z",
  "updated_at" : "2016-10-05T23:53:06.06Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`

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
of PCI scope by sending this info over SSL directly to Finix. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the Finix API.
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
          applicationId: 'APg1ojcH1J1we1MFvnRc6P97',
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
  "id" : "TKr7JgwX7ekxxBwM1pRMrPGb",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-05T23:53:24.47Z",
  "updated_at" : "2016-10-05T23:53:24.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-06T23:53:24.47Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	});
$card = $card->save();

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
  "id" : "PIr7JgwX7ekxxBwM1pRMrPGb",
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
  "created_at" : "2016-10-05T23:53:25.47Z",
  "updated_at" : "2016-10-05T23:53:25.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/updates"
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

`POST https://api-staging.finix.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKr7JgwX7ekxxBwM1pRMrPGb", 
	    "type": "TOKEN", 
	    "identity": "IDoVSH2TYLRBe7d9pprcgMLd"
	});
$card = $card->save();

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
  "id" : "PIr7JgwX7ekxxBwM1pRMrPGb",
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
  "created_at" : "2016-10-05T23:53:25.47Z",
  "updated_at" : "2016-10-05T23:53:25.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/updates"
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

`POST https://api-staging.finix.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Fetch a Payment Instrument

```shell


curl https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PItTHbUEVodMPoibEbiiHPqS');

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PItTHbUEVodMPoibEbiiHPqS")

```
> Example Response:

```json
{
  "id" : "PItTHbUEVodMPoibEbiiHPqS",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-05T23:53:05.97Z",
  "updated_at" : "2016-10-05T23:53:07.15Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PItTHbUEVodMPoibEbiiHPqS",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-05T23:53:05.97Z",
  "updated_at" : "2016-10-05T23:53:07.15Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
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

`PUT https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java
import io.finix.payments.processing.client.model.BankAccount;

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
      "id" : "PI932yvKVJUuQBFipQsazUEq",
      "fingerprint" : "FPR1459643778",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jim Jones",
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
      "created_at" : "2016-10-05T23:53:38.73Z",
      "updated_at" : "2016-10-05T23:53:38.73Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDkjVEbLenpKNEgermBj7cGF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkjVEbLenpKNEgermBj7cGF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq/updates"
        }
      }
    }, {
      "id" : "PIw6SC3dNofXckDUZKSQaw3G",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:35.09Z",
      "updated_at" : "2016-10-05T23:53:35.09Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw6SC3dNofXckDUZKSQaw3G"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw6SC3dNofXckDUZKSQaw3G/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw6SC3dNofXckDUZKSQaw3G/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw6SC3dNofXckDUZKSQaw3G/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIdaRmk9KMTsZhGHG9qemFEA",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:35.09Z",
      "updated_at" : "2016-10-05T23:53:35.09Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdaRmk9KMTsZhGHG9qemFEA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdaRmk9KMTsZhGHG9qemFEA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdaRmk9KMTsZhGHG9qemFEA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdaRmk9KMTsZhGHG9qemFEA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PImTQqmBj39XaCqYNgUJPZMZ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:35.09Z",
      "updated_at" : "2016-10-05T23:53:35.09Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImTQqmBj39XaCqYNgUJPZMZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImTQqmBj39XaCqYNgUJPZMZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImTQqmBj39XaCqYNgUJPZMZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImTQqmBj39XaCqYNgUJPZMZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PI2FrLrvtFCenshjv9rBwzMp",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:35.09Z",
      "updated_at" : "2016-10-05T23:53:35.09Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIr7JgwX7ekxxBwM1pRMrPGb",
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
      "created_at" : "2016-10-05T23:53:25.34Z",
      "updated_at" : "2016-10-05T23:53:25.34Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr7JgwX7ekxxBwM1pRMrPGb/updates"
        }
      }
    }, {
      "id" : "PIi3nT9F39StMo4FrXfbuzQ8",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-05T23:53:12.31Z",
      "updated_at" : "2016-10-05T23:53:12.31Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID2xpWjexhTZxLo8zamyUkdH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi3nT9F39StMo4FrXfbuzQ8"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi3nT9F39StMo4FrXfbuzQ8/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi3nT9F39StMo4FrXfbuzQ8/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi3nT9F39StMo4FrXfbuzQ8/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PItxT8YNpKC95GNvayrbzWq7",
      "fingerprint" : "FPR-1045815956",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Daphne Diaz",
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
      "created_at" : "2016-10-05T23:53:10.88Z",
      "updated_at" : "2016-10-05T23:53:20.85Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2xpWjexhTZxLo8zamyUkdH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2xpWjexhTZxLo8zamyUkdH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7/updates"
        }
      }
    }, {
      "id" : "PIhGMheVesSPhuXYqJCNw4UN",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:08.11Z",
      "updated_at" : "2016-10-05T23:53:08.11Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhGMheVesSPhuXYqJCNw4UN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhGMheVesSPhuXYqJCNw4UN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhGMheVesSPhuXYqJCNw4UN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhGMheVesSPhuXYqJCNw4UN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIwU7fb5fyofuYgSx36VMjBL",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:08.11Z",
      "updated_at" : "2016-10-05T23:53:08.11Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwU7fb5fyofuYgSx36VMjBL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwU7fb5fyofuYgSx36VMjBL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwU7fb5fyofuYgSx36VMjBL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwU7fb5fyofuYgSx36VMjBL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:53:08.11Z",
      "updated_at" : "2016-10-05T23:53:08.11Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PItTHbUEVodMPoibEbiiHPqS",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-05T23:53:05.97Z",
      "updated_at" : "2016-10-05T23:53:07.15Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIiDtzKUpVdrHCH5hmpDpGua",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:52:50.58Z",
      "updated_at" : "2016-10-05T23:52:50.58Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiDtzKUpVdrHCH5hmpDpGua"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiDtzKUpVdrHCH5hmpDpGua/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiDtzKUpVdrHCH5hmpDpGua/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiDtzKUpVdrHCH5hmpDpGua/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIvee9gvm4NhvAUQXaeK1Ee",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:52:50.58Z",
      "updated_at" : "2016-10-05T23:52:50.58Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvee9gvm4NhvAUQXaeK1Ee"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvee9gvm4NhvAUQXaeK1Ee/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvee9gvm4NhvAUQXaeK1Ee/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvee9gvm4NhvAUQXaeK1Ee/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIajUZdXCjiZMaTG6Dn24VmC",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:52:50.58Z",
      "updated_at" : "2016-10-05T23:52:50.58Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIajUZdXCjiZMaTG6Dn24VmC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIajUZdXCjiZMaTG6Dn24VmC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIajUZdXCjiZMaTG6Dn24VmC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIajUZdXCjiZMaTG6Dn24VmC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    }, {
      "id" : "PIcoaWyrWnRNF4nuBT8PE1S2",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-05T23:52:50.58Z",
      "updated_at" : "2016-10-05T23:52:50.58Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcoaWyrWnRNF4nuBT8PE1S2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcoaWyrWnRNF4nuBT8PE1S2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcoaWyrWnRNF4nuBT8PE1S2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcoaWyrWnRNF4nuBT8PE1S2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 16
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments`

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDoVSH2TYLRBe7d9pprcgMLd');
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

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "ST27ub5j8TQTozuoVjGU58Cy",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "currency" : "USD",
  "created_at" : "2016-10-06T00:00:38.73Z",
  "updated_at" : "2016-10-06T00:00:38.74Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 732984,
  "total_fee" : 73299,
  "net_amount" : 659685,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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
request to the transfers link (i.e. POST https://api-staging.finix.io/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://api-staging.finix.io/identities/:IDENTITY_ID/settlements`

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


curl https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('ST27ub5j8TQTozuoVjGU58Cy');

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("ST27ub5j8TQTozuoVjGU58Cy");

```
> Example Response:

```json
{
  "id" : "ST27ub5j8TQTozuoVjGU58Cy",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "currency" : "USD",
  "created_at" : "2016-10-06T00:00:38.62Z",
  "updated_at" : "2016-10-06T00:00:40.16Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 732984,
  "total_fee" : 73299,
  "net_amount" : 659685,
  "destination" : "PItTHbUEVodMPoibEbiiHPqS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://api-staging.finix.io/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "destination": "PItTHbUEVodMPoibEbiiHPqS"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ST27ub5j8TQTozuoVjGU58Cy",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "currency" : "USD",
  "created_at" : "2016-10-06T00:00:38.62Z",
  "updated_at" : "2016-10-06T00:00:40.16Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 732984,
  "total_fee" : 73299,
  "net_amount" : 659685,
  "destination" : "PItTHbUEVodMPoibEbiiHPqS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
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

`POST https://api-staging.finix.io/settlements/:SETTLEMENT_ID`

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
curl https://api-staging.finix.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


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
      "id" : "ST27ub5j8TQTozuoVjGU58Cy",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "currency" : "USD",
      "created_at" : "2016-10-06T00:00:38.62Z",
      "updated_at" : "2016-10-06T00:00:40.16Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 732984,
      "total_fee" : 73299,
      "net_amount" : 659685,
      "destination" : "PItTHbUEVodMPoibEbiiHPqS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


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
      "id" : "TRp4fFL8HWzLVFP7kcCfN2ER",
      "amount" : 89,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "60ccb176-a580-4751-8a04-c8acc4dd34e6",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "destination" : "PItTHbUEVodMPoibEbiiHPqS",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T00:00:39.90Z",
      "updated_at" : "2016-10-06T00:00:40.30Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRp4fFL8HWzLVFP7kcCfN2ER"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRp4fFL8HWzLVFP7kcCfN2ER/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRp4fFL8HWzLVFP7kcCfN2ER/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRp4fFL8HWzLVFP7kcCfN2ER/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
        }
      }
    }, {
      "id" : "TRwLjb5FzUw5uMJfew9kp5FY",
      "amount" : 659596,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "d5c25d26-2a04-4fa6-8aea-0d4c26880b6b",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "destination" : "PItTHbUEVodMPoibEbiiHPqS",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T00:00:39.90Z",
      "updated_at" : "2016-10-06T00:00:40.23Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRwLjb5FzUw5uMJfew9kp5FY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRwLjb5FzUw5uMJfew9kp5FY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRwLjb5FzUw5uMJfew9kp5FY/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRwLjb5FzUw5uMJfew9kp5FY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTHbUEVodMPoibEbiiHPqS"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR7tKQZ7Uooeu17DwSe35Sfj",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "ready_to_settle_at" : "2016-10-05T23:58:19.26Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:22.02Z",
      "updated_at" : "2016-10-05T23:54:09.93Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        }
      }
    }, {
      "id" : "TRcioz1FxEYHRkuDiK3FsSLV",
      "amount" : 732884,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "c1a29ae2-50bc-4a7b-9b89-ac231cfe5c82",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "ready_to_settle_at" : "2016-10-05T23:58:19.26Z",
      "fee" : 73288,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:13.74Z",
      "updated_at" : "2016-10-05T23:54:21.08Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST27ub5j8TQTozuoVjGU58Cy/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/settlements/:SETTLEMENT_ID/transfers`


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

curl https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRcioz1FxEYHRkuDiK3FsSLV');



```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRcioz1FxEYHRkuDiK3FsSLV");

```
> Example Response:

```json
{
  "id" : "TRcioz1FxEYHRkuDiK3FsSLV",
  "amount" : 732884,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "c1a29ae2-50bc-4a7b-9b89-ac231cfe5c82",
  "currency" : "USD",
  "application" : "APg1ojcH1J1we1MFvnRc6P97",
  "source" : "PItxT8YNpKC95GNvayrbzWq7",
  "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
  "ready_to_settle_at" : null,
  "fee" : 73288,
  "statement_descriptor" : "FNX*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:13.74Z",
  "updated_at" : "2016-10-05T23:53:13.99Z",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TRcioz1FxEYHRkuDiK3FsSLV');
$refund = $debit->reverse(50);
```
```java

import io.finix.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRa1QGvCxXTGEnQTmqbczFZ7",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "078718d0-4f2e-4a71-a657-3959c8751b5f",
  "currency" : "USD",
  "application" : "APg1ojcH1J1we1MFvnRc6P97",
  "source" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
  "destination" : "PItxT8YNpKC95GNvayrbzWq7",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*BOBS BURGERS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-05T23:53:19.43Z",
  "updated_at" : "2016-10-05T23:53:19.54Z",
  "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRa1QGvCxXTGEnQTmqbczFZ7"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRa1QGvCxXTGEnQTmqbczFZ7/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://api-staging.finix.io/transfers/:TRANSFER_ID/reversals`

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
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java
import io.finix.payments.processing.client.model.Transfer;

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
      "id" : "TR5vKixEBego7wJkSsUYEbq9",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "FAILED",
      "trace_id" : "1024",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PI2FrLrvtFCenshjv9rBwzMp",
      "destination" : "PI932yvKVJUuQBFipQsazUEq",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:40.09Z",
      "updated_at" : "2016-10-05T23:53:40.99Z",
      "merchant_identity" : "IDabjyqwpe2Kxa55pw9dyV8B",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDabjyqwpe2Kxa55pw9dyV8B"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5vKixEBego7wJkSsUYEbq9/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2FrLrvtFCenshjv9rBwzMp"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI932yvKVJUuQBFipQsazUEq"
        }
      }
    }, {
      "id" : "TR7tKQZ7Uooeu17DwSe35Sfj",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "312927dd-d833-4a7b-825f-48ec01a38337",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:22.02Z",
      "updated_at" : "2016-10-05T23:53:22.28Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7tKQZ7Uooeu17DwSe35Sfj/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        }
      }
    }, {
      "id" : "TRa1QGvCxXTGEnQTmqbczFZ7",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "078718d0-4f2e-4a71-a657-3959c8751b5f",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "destination" : "PItxT8YNpKC95GNvayrbzWq7",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:19.27Z",
      "updated_at" : "2016-10-05T23:53:19.54Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRa1QGvCxXTGEnQTmqbczFZ7"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRa1QGvCxXTGEnQTmqbczFZ7/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        }
      }
    }, {
      "id" : "TRa8UZ5pfFA7RDtARifostFP",
      "amount" : 76258,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "b8162cf7-6cdf-42e7-b39c-64617345f797",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PIi3nT9F39StMo4FrXfbuzQ8",
      "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "ready_to_settle_at" : null,
      "fee" : 7626,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:15.17Z",
      "updated_at" : "2016-10-05T23:53:15.42Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRa8UZ5pfFA7RDtARifostFP"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRa8UZ5pfFA7RDtARifostFP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRa8UZ5pfFA7RDtARifostFP/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRa8UZ5pfFA7RDtARifostFP/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi3nT9F39StMo4FrXfbuzQ8"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        }
      }
    }, {
      "id" : "TRcioz1FxEYHRkuDiK3FsSLV",
      "amount" : 732884,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "c1a29ae2-50bc-4a7b-9b89-ac231cfe5c82",
      "currency" : "USD",
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "source" : "PItxT8YNpKC95GNvayrbzWq7",
      "destination" : "PItTtN2bEQXn6Zbm2u8R5KHQ",
      "ready_to_settle_at" : null,
      "fee" : 73288,
      "statement_descriptor" : "FNX*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-05T23:53:13.74Z",
      "updated_at" : "2016-10-05T23:53:13.99Z",
      "merchant_identity" : "IDoVSH2TYLRBe7d9pprcgMLd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDoVSH2TYLRBe7d9pprcgMLd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcioz1FxEYHRkuDiK3FsSLV/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItxT8YNpKC95GNvayrbzWq7"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItTtN2bEQXn6Zbm2u8R5KHQ"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 5
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers`
# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the Finix API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1 \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHgSxpcWcoe1bWcktKRqVNHZ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APg1ojcH1J1we1MFvnRc6P97",
  "created_at" : "2016-10-05T23:52:54.06Z",
  "updated_at" : "2016-10-05T23:52:54.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHgSxpcWcoe1bWcktKRqVNHZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

## Retrieve a Webhook

```shell



curl https://api-staging.finix.io/webhooks/WHgSxpcWcoe1bWcktKRqVNHZ \
    -H "Content-Type: application/vnd.json+api" \
    -u USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHgSxpcWcoe1bWcktKRqVNHZ');



```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHgSxpcWcoe1bWcktKRqVNHZ");

```
> Example Response:

```json
{
  "id" : "WHgSxpcWcoe1bWcktKRqVNHZ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APg1ojcH1J1we1MFvnRc6P97",
  "created_at" : "2016-10-05T23:52:54.06Z",
  "updated_at" : "2016-10-05T23:52:54.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHgSxpcWcoe1bWcktKRqVNHZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://api-staging.finix.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USupdQBdHKc58rBx1urfeXfg:6fb57b70-cd4c-483d-bb79-be35ec246ff1

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java
import io.finix.payments.processing.client.model.Webhook;

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
      "id" : "WHgSxpcWcoe1bWcktKRqVNHZ",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APg1ojcH1J1we1MFvnRc6P97",
      "created_at" : "2016-10-05T23:52:54.06Z",
      "updated_at" : "2016-10-05T23:52:54.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHgSxpcWcoe1bWcktKRqVNHZ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APg1ojcH1J1we1MFvnRc6P97"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/webhooks`
    

## Sample Payloads


```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USupdQBdHKc58rBx1urfeXfg', '6fb57b70-cd4c-483d-bb79-be35ec246ff1');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

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
