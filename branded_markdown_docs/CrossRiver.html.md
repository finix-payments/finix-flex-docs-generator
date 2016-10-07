---
title: CrossRiver API Reference

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

These guides provide a collection of resources for utilizing the CrossRiver
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
	        "default_statement_descriptor": "Dunder Mifflin", 
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
	        "doing_business_as": "Dunder Mifflin", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Dunder Mifflin", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.DunderMifflin.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

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
	        "default_statement_descriptor"=> "Dunder Mifflin", 
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
	        "doing_business_as"=> "Dunder Mifflin", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Dunder Mifflin", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.DunderMifflin.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java
import io.crossriver.payments.processing.client.model.Identity;

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
  "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Dunder Mifflin",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-06T23:01:37.90Z",
  "updated_at" : "2016-10-06T23:01:37.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

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
	    "identity"=> "ID5YEW5VQNfrgZtpA4zkdkqK"
	));
$bank_account = $bank_account->save();

```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

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
  "id" : "PI7rUZfEahb3XV35ytxvg6vW",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-06T23:01:47.87Z",
  "updated_at" : "2016-10-06T23:01:47.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "verification" : "VImprTEDXDVBSw9H6Cpk7CG8",
  "merchant_profile" : "MPua6zQzjnzXr4eXrNRVkP1N",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-06T23:01:50.52Z",
  "updated_at" : "2016-10-06T23:01:50.52Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPua6zQzjnzXr4eXrNRVkP1N"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VImprTEDXDVBSw9H6Cpk7CG8"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
	        "last_name": "Chang", 
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Amy", 
	        "last_name"=> "Chang", 
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

import io.crossriver.payments.processing.client.model.Identity;

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
  "id" : "ID8y7HxvJGffxUHBfysAFa2r",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
    "last_name" : "Chang",
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
  "created_at" : "2016-10-06T23:01:52.29Z",
  "updated_at" : "2016-10-06T23:01:52.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "name": "Laura Chang", 
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
	    "identity": "ID8y7HxvJGffxUHBfysAFa2r"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Laura Chang", 
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
	    "identity"=> "ID8y7HxvJGffxUHBfysAFa2r"
	));
$card = $card->save();


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

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
  "id" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "fingerprint" : "FPR1472555584",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Chang",
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
  "created_at" : "2016-10-06T23:01:53.14Z",
  "updated_at" : "2016-10-06T23:01:53.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID8y7HxvJGffxUHBfysAFa2r",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/updates"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "merchant_identity": "ID5YEW5VQNfrgZtpA4zkdkqK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3N2hZ9Y1NM5d52RUDGdUeN", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID5YEW5VQNfrgZtpA4zkdkqK", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3N2hZ9Y1NM5d52RUDGdUeN", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```java
import io.crossriver.payments.processing.client.model.Authorization;

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
  "id" : "AUay9Bxr6ezkNRzoVePFadzw",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:04.62Z",
  "updated_at" : "2016-10-06T23:02:04.64Z",
  "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : false,
  "expires_at" : "2016-10-13T23:02:04.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
curl https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUay9Bxr6ezkNRzoVePFadzw');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUay9Bxr6ezkNRzoVePFadzw");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUay9Bxr6ezkNRzoVePFadzw",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:04.49Z",
  "updated_at" : "2016-10-06T23:02:06.08Z",
  "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : false,
  "expires_at" : "2016-10-13T23:02:04.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Settlement;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');
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
import io.crossriver.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STgE15agz7NyTRZaqDYWJsJ6",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "currency" : "USD",
  "created_at" : "2016-10-06T23:09:23.23Z",
  "updated_at" : "2016-10-06T23:09:23.24Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 104946,
  "total_fee" : 10496,
  "net_amount" : 94450,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
of PCI scope by sending this info over SSL directly to CrossRiver. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the CrossRiver API.
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
          applicationId: 'APkv7UWjnRDVnTmfsQYBpW9j',
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
  "id" : "TKatiyTcXfJaAF492pMU66BT",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-06T23:02:08.34Z",
  "updated_at" : "2016-10-06T23:02:08.34Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-07T23:02:08.34Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	});
$card = $card->save();

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

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
  "id" : "PIatiyTcXfJaAF492pMU66BT",
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
  "created_at" : "2016-10-06T23:02:09.96Z",
  "updated_at" : "2016-10-06T23:02:09.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/updates"
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
    -u USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
	        "last_name": "White", 
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID72NcqXWWCPm2F14XWgRc7g",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
    "last_name" : "White",
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
  "created_at" : "2016-10-06T23:02:22.38Z",
  "updated_at" : "2016-10-06T23:02:22.38Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "name": "Maggie Henderson", 
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
	    "identity": "ID72NcqXWWCPm2F14XWgRc7g"
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USvg7UiC7V7hZzvwQHqrzMCM", 
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
	        "doing_business_as"=> "Square", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Square", 
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
  "id" : "PIbsqGcCtsvo9WabdKngXh4G",
  "fingerprint" : "FPR365123526",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Henderson",
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
  "created_at" : "2016-10-06T23:02:23.20Z",
  "updated_at" : "2016-10-06T23:02:23.20Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID72NcqXWWCPm2F14XWgRc7g",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/updates"
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
    -u USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID72NcqXWWCPm2F14XWgRc7g", 
	    "destination": "PIbsqGcCtsvo9WabdKngXh4G", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USvg7UiC7V7hZzvwQHqrzMCM", 
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
	        "doing_business_as"=> "Square", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Square", 
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
  "id" : "TRnhNBkrUJZet8wKwLnh5A3U",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "FAILED",
  "trace_id" : "1079",
  "currency" : "USD",
  "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
  "source" : "PIsAGPDDFM5jTVmrs78WEtcD",
  "destination" : "PIbsqGcCtsvo9WabdKngXh4G",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:24.69Z",
  "updated_at" : "2016-10-06T23:02:26.45Z",
  "merchant_identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "merchant_identity": "ID5YEW5VQNfrgZtpA4zkdkqK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3N2hZ9Y1NM5d52RUDGdUeN", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID5YEW5VQNfrgZtpA4zkdkqK", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3N2hZ9Y1NM5d52RUDGdUeN", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```java
import io.crossriver.payments.processing.client.model.Authorization;

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
  "id" : "AUay9Bxr6ezkNRzoVePFadzw",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:04.62Z",
  "updated_at" : "2016-10-06T23:02:04.64Z",
  "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : false,
  "expires_at" : "2016-10-13T23:02:04.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
curl https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUay9Bxr6ezkNRzoVePFadzw');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUay9Bxr6ezkNRzoVePFadzw");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUay9Bxr6ezkNRzoVePFadzw",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:04.49Z",
  "updated_at" : "2016-10-06T23:02:06.08Z",
  "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : false,
  "expires_at" : "2016-10-13T23:02:04.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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

curl https://api-staging.finix.io/authorizations/AUxhgpQnQDcisP1pfgyCEUtk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUxhgpQnQDcisP1pfgyCEUtk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:11.24Z",
  "updated_at" : "2016-10-06T23:02:12.52Z",
  "trace_id" : "47fa622f-0fd7-4488-9275-e07ae4d11935",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : true,
  "expires_at" : "2016-10-13T23:02:11.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUxhgpQnQDcisP1pfgyCEUtk"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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

curl https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUay9Bxr6ezkNRzoVePFadzw');

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUay9Bxr6ezkNRzoVePFadzw");

```
> Example Response:

```json
{
  "id" : "AUay9Bxr6ezkNRzoVePFadzw",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:04.49Z",
  "updated_at" : "2016-10-06T23:02:06.08Z",
  "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "is_void" : false,
  "expires_at" : "2016-10-13T23:02:04.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "AUxhgpQnQDcisP1pfgyCEUtk",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:11.24Z",
      "updated_at" : "2016-10-06T23:02:12.52Z",
      "trace_id" : "47fa622f-0fd7-4488-9275-e07ae4d11935",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "is_void" : true,
      "expires_at" : "2016-10-13T23:02:11.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUxhgpQnQDcisP1pfgyCEUtk"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        }
      }
    }, {
      "id" : "AUay9Bxr6ezkNRzoVePFadzw",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:04.49Z",
      "updated_at" : "2016-10-06T23:02:06.08Z",
      "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "is_void" : false,
      "expires_at" : "2016-10-13T23:02:04.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUay9Bxr6ezkNRzoVePFadzw"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
	        "last_name": "Chang", 
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Amy", 
	        "last_name"=> "Chang", 
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

import io.crossriver.payments.processing.client.model.Identity;

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
  "id" : "ID8y7HxvJGffxUHBfysAFa2r",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
    "last_name" : "Chang",
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
  "created_at" : "2016-10-06T23:01:52.29Z",
  "updated_at" : "2016-10-06T23:01:52.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
	        "default_statement_descriptor": "Dunder Mifflin", 
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
	        "doing_business_as": "Dunder Mifflin", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Dunder Mifflin", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.DunderMifflin.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

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
	        "default_statement_descriptor"=> "Dunder Mifflin", 
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
	        "doing_business_as"=> "Dunder Mifflin", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Dunder Mifflin", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.DunderMifflin.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```java

import io.crossriver.payments.processing.client.model.Identity;

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
  "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Dunder Mifflin",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-06T23:01:37.90Z",
  "updated_at" : "2016-10-06T23:01:37.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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

curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');
```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID5YEW5VQNfrgZtpA4zkdkqK");

```
> Example Response:

```json
{
  "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Dunder Mifflin",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-10-06T23:01:37.83Z",
  "updated_at" : "2016-10-06T23:01:37.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Identity;

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
      "id" : "ID72NcqXWWCPm2F14XWgRc7g",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
        "last_name" : "White",
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
      "created_at" : "2016-10-06T23:02:22.32Z",
      "updated_at" : "2016-10-06T23:02:22.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID8y7HxvJGffxUHBfysAFa2r",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
        "last_name" : "Chang",
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
      "created_at" : "2016-10-06T23:01:52.24Z",
      "updated_at" : "2016-10-06T23:01:52.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDoTsrtT68Jic71Nvz7nEU9F",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-10-06T23:01:46.68Z",
      "updated_at" : "2016-10-06T23:01:46.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDgdzZDjrFxLu6FWBtaV5vBg",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-06T23:01:45.73Z",
      "updated_at" : "2016-10-06T23:01:45.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID5DSP61gnAvsgJdQfSEHvfP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-06T23:01:44.83Z",
      "updated_at" : "2016-10-06T23:01:44.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID9aqAWVDAUAPoQNPsMWvt4B",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-10-06T23:01:43.81Z",
      "updated_at" : "2016-10-06T23:01:43.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDnXJhgHbKqjsqCsgGS7xrKM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-06T23:01:42.89Z",
      "updated_at" : "2016-10-06T23:01:42.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID64jDTULbuqqvH3NBSwEdxL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_PARTNERSHIP",
        "doing_business_as" : "Pawny City Hall",
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
        "url" : "www.PawnyCityHall.com",
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
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-06T23:01:41.96Z",
      "updated_at" : "2016-10-06T23:01:41.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDvrukPSkPHUKLKigJ9Pk5pP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-06T23:01:40.94Z",
      "updated_at" : "2016-10-06T23:01:40.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID2Erw5S9SRrFJYJQoqj94wG",
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
      "created_at" : "2016-10-06T23:01:39.65Z",
      "updated_at" : "2016-10-06T23:01:39.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDrt1HsAWnnt7zPjN5nMSV8N",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "CORPORATION",
        "doing_business_as" : "Golds Gym",
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
        "key" : "value"
      },
      "created_at" : "2016-10-06T23:01:38.75Z",
      "updated_at" : "2016-10-06T23:01:38.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-10-06T23:01:37.83Z",
      "updated_at" : "2016-10-06T23:01:37.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Square",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Square",
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
        "application_name" : "Square"
      },
      "created_at" : "2016-10-06T23:01:30.04Z",
      "updated_at" : "2016-10-06T23:01:30.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Marshall", 
	        "last_name": "Le", 
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Marshall",
    "last_name" : "Le",
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
  "created_at" : "2016-10-06T23:01:37.83Z",
  "updated_at" : "2016-10-06T23:02:40.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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

curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);
```
```java

import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```

> Example Response:

```json
{
  "id" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "verification" : "VImprTEDXDVBSw9H6Cpk7CG8",
  "merchant_profile" : "MPua6zQzjnzXr4eXrNRVkP1N",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-06T23:01:50.52Z",
  "updated_at" : "2016-10-06T23:01:50.52Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPua6zQzjnzXr4eXrNRVkP1N"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VImprTEDXDVBSw9H6Cpk7CG8"
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
curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "verification" : "VImprTEDXDVBSw9H6Cpk7CG8",
  "merchant_profile" : "MPua6zQzjnzXr4eXrNRVkP1N",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-06T23:01:50.52Z",
  "updated_at" : "2016-10-06T23:01:50.52Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPua6zQzjnzXr4eXrNRVkP1N"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VImprTEDXDVBSw9H6Cpk7CG8"
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
curl https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MU6g5SM6Fo8pfMFJHaES7gVc');

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU6g5SM6Fo8pfMFJHaES7gVc");

```
> Example Response:

```json
{
  "id" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "verification" : null,
  "merchant_profile" : "MPua6zQzjnzXr4eXrNRVkP1N",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-06T23:01:50.42Z",
  "updated_at" : "2016-10-06T23:01:50.64Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPua6zQzjnzXr4eXrNRVkP1N"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US4kze2baMFcvwP7aEYRfJtp",
  "password" : "d0dcf47d-83f9-46a0-b32d-53f9d1ece347",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-06T23:02:00.23Z",
  "updated_at" : "2016-10-06T23:02:00.23Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US4kze2baMFcvwP7aEYRfJtp"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIiUGRZ4QS3i3sUBrZmTq237",
  "external_trace_id" : "c85f4b1e-7127-4158-a9d5-f0788ac6aa13",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-06T23:02:41.62Z",
  "updated_at" : "2016-10-06T23:02:41.65Z",
  "payment_instrument" : null,
  "merchant" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIiUGRZ4QS3i3sUBrZmTq237"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
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
curl https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIiUGRZ4QS3i3sUBrZmTq237",
  "external_trace_id" : "c85f4b1e-7127-4158-a9d5-f0788ac6aa13",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-06T23:02:41.62Z",
  "updated_at" : "2016-10-06T23:02:41.65Z",
  "payment_instrument" : null,
  "merchant" : "MU6g5SM6Fo8pfMFJHaES7gVc",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIiUGRZ4QS3i3sUBrZmTq237"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU6g5SM6Fo8pfMFJHaES7gVc",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "verification" : null,
      "merchant_profile" : "MPua6zQzjnzXr4eXrNRVkP1N",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-10-06T23:01:50.42Z",
      "updated_at" : "2016-10-06T23:01:50.64Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPua6zQzjnzXr4eXrNRVkP1N"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/merchants/MU6g5SM6Fo8pfMFJHaES7gVc/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID72NcqXWWCPm2F14XWgRc7g",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
        "last_name" : "White",
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
      "created_at" : "2016-10-06T23:02:22.32Z",
      "updated_at" : "2016-10-06T23:02:22.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID8y7HxvJGffxUHBfysAFa2r",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
        "last_name" : "Chang",
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
      "created_at" : "2016-10-06T23:01:52.24Z",
      "updated_at" : "2016-10-06T23:01:52.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDoTsrtT68Jic71Nvz7nEU9F",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-10-06T23:01:46.68Z",
      "updated_at" : "2016-10-06T23:01:46.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoTsrtT68Jic71Nvz7nEU9F/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDgdzZDjrFxLu6FWBtaV5vBg",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-06T23:01:45.73Z",
      "updated_at" : "2016-10-06T23:01:45.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgdzZDjrFxLu6FWBtaV5vBg/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID5DSP61gnAvsgJdQfSEHvfP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-06T23:01:44.83Z",
      "updated_at" : "2016-10-06T23:01:44.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5DSP61gnAvsgJdQfSEHvfP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID9aqAWVDAUAPoQNPsMWvt4B",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-10-06T23:01:43.81Z",
      "updated_at" : "2016-10-06T23:01:43.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9aqAWVDAUAPoQNPsMWvt4B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDnXJhgHbKqjsqCsgGS7xrKM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-06T23:01:42.89Z",
      "updated_at" : "2016-10-06T23:01:42.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnXJhgHbKqjsqCsgGS7xrKM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID64jDTULbuqqvH3NBSwEdxL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_PARTNERSHIP",
        "doing_business_as" : "Pawny City Hall",
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
        "url" : "www.PawnyCityHall.com",
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
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-10-06T23:01:41.96Z",
      "updated_at" : "2016-10-06T23:01:41.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID64jDTULbuqqvH3NBSwEdxL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDvrukPSkPHUKLKigJ9Pk5pP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-06T23:01:40.94Z",
      "updated_at" : "2016-10-06T23:01:40.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvrukPSkPHUKLKigJ9Pk5pP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID2Erw5S9SRrFJYJQoqj94wG",
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
      "created_at" : "2016-10-06T23:01:39.65Z",
      "updated_at" : "2016-10-06T23:01:39.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2Erw5S9SRrFJYJQoqj94wG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDrt1HsAWnnt7zPjN5nMSV8N",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "CORPORATION",
        "doing_business_as" : "Golds Gym",
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
        "key" : "value"
      },
      "created_at" : "2016-10-06T23:01:38.75Z",
      "updated_at" : "2016-10-06T23:01:38.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrt1HsAWnnt7zPjN5nMSV8N/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-10-06T23:01:37.83Z",
      "updated_at" : "2016-10-06T23:01:37.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Square",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Square",
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
        "application_name" : "Square"
      },
      "created_at" : "2016-10-06T23:01:30.04Z",
      "updated_at" : "2016-10-06T23:01:30.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "name": "Laura Chang", 
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
	    "identity": "ID8y7HxvJGffxUHBfysAFa2r"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Laura Chang", 
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
	    "identity"=> "ID8y7HxvJGffxUHBfysAFa2r"
	));
$card = $card->save();


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

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
  "id" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "fingerprint" : "FPR1472555584",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Chang",
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
  "created_at" : "2016-10-06T23:01:53.14Z",
  "updated_at" : "2016-10-06T23:01:53.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID8y7HxvJGffxUHBfysAFa2r",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/updates"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

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
	    "identity"=> "ID5YEW5VQNfrgZtpA4zkdkqK"
	));
$bank_account = $bank_account->save();


```
```java

import io.crossriver.payments.processing.client.model.BankAccount;

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
  "id" : "PI7rUZfEahb3XV35ytxvg6vW",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-06T23:01:47.87Z",
  "updated_at" : "2016-10-06T23:01:47.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
of PCI scope by sending this info over SSL directly to CrossRiver. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the CrossRiver API.
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
          applicationId: 'APkv7UWjnRDVnTmfsQYBpW9j',
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
  "id" : "TKatiyTcXfJaAF492pMU66BT",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-06T23:02:08.34Z",
  "updated_at" : "2016-10-06T23:02:08.34Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-07T23:02:08.34Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	});
$card = $card->save();

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

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
  "id" : "PIatiyTcXfJaAF492pMU66BT",
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
  "created_at" : "2016-10-06T23:02:09.96Z",
  "updated_at" : "2016-10-06T23:02:09.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/updates"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKatiyTcXfJaAF492pMU66BT", 
	    "type": "TOKEN", 
	    "identity": "ID5YEW5VQNfrgZtpA4zkdkqK"
	});
$card = $card->save();

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

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
  "id" : "PIatiyTcXfJaAF492pMU66BT",
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
  "created_at" : "2016-10-06T23:02:09.96Z",
  "updated_at" : "2016-10-06T23:02:09.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/updates"
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


curl https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI7rUZfEahb3XV35ytxvg6vW');

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI7rUZfEahb3XV35ytxvg6vW")

```
> Example Response:

```json
{
  "id" : "PI7rUZfEahb3XV35ytxvg6vW",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-06T23:01:47.77Z",
  "updated_at" : "2016-10-06T23:01:48.78Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
curl https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PI7rUZfEahb3XV35ytxvg6vW",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-06T23:01:47.77Z",
  "updated_at" : "2016-10-06T23:01:48.78Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

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
      "id" : "PIbsqGcCtsvo9WabdKngXh4G",
      "fingerprint" : "FPR365123526",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Maggie Henderson",
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
      "created_at" : "2016-10-06T23:02:23.13Z",
      "updated_at" : "2016-10-06T23:02:23.13Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID72NcqXWWCPm2F14XWgRc7g",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID72NcqXWWCPm2F14XWgRc7g"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G/updates"
        }
      }
    }, {
      "id" : "PIaidxkpBUvpgBJsVERiPNQi",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:02:20.48Z",
      "updated_at" : "2016-10-06T23:02:20.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaidxkpBUvpgBJsVERiPNQi"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaidxkpBUvpgBJsVERiPNQi/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaidxkpBUvpgBJsVERiPNQi/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaidxkpBUvpgBJsVERiPNQi/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIwDfhfV6yN9N1tpAh1BJ45R",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:02:20.48Z",
      "updated_at" : "2016-10-06T23:02:20.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwDfhfV6yN9N1tpAh1BJ45R"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwDfhfV6yN9N1tpAh1BJ45R/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwDfhfV6yN9N1tpAh1BJ45R/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwDfhfV6yN9N1tpAh1BJ45R/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIxtweLRTs6Eb5qCb7ArU4pL",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:02:20.48Z",
      "updated_at" : "2016-10-06T23:02:20.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtweLRTs6Eb5qCb7ArU4pL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtweLRTs6Eb5qCb7ArU4pL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtweLRTs6Eb5qCb7ArU4pL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtweLRTs6Eb5qCb7ArU4pL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIsAGPDDFM5jTVmrs78WEtcD",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:02:20.48Z",
      "updated_at" : "2016-10-06T23:02:20.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIatiyTcXfJaAF492pMU66BT",
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
      "created_at" : "2016-10-06T23:02:09.83Z",
      "updated_at" : "2016-10-06T23:02:09.83Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIatiyTcXfJaAF492pMU66BT/updates"
        }
      }
    }, {
      "id" : "PItbBTq5XhURPLaDeVUPtGMM",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-06T23:01:54.05Z",
      "updated_at" : "2016-10-06T23:01:54.05Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID8y7HxvJGffxUHBfysAFa2r",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbBTq5XhURPLaDeVUPtGMM"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbBTq5XhURPLaDeVUPtGMM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbBTq5XhURPLaDeVUPtGMM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbBTq5XhURPLaDeVUPtGMM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "fingerprint" : "FPR1472555584",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Laura Chang",
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
      "created_at" : "2016-10-06T23:01:53.06Z",
      "updated_at" : "2016-10-06T23:02:04.63Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID8y7HxvJGffxUHBfysAFa2r",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8y7HxvJGffxUHBfysAFa2r"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN/updates"
        }
      }
    }, {
      "id" : "PI8ExBA7hW5rsjGGB44vjFk",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:50.42Z",
      "updated_at" : "2016-10-06T23:01:50.42Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ExBA7hW5rsjGGB44vjFk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ExBA7hW5rsjGGB44vjFk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ExBA7hW5rsjGGB44vjFk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ExBA7hW5rsjGGB44vjFk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIqu6mjvRdvvHCURAj4bmyfG",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:50.42Z",
      "updated_at" : "2016-10-06T23:01:50.42Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqu6mjvRdvvHCURAj4bmyfG"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqu6mjvRdvvHCURAj4bmyfG/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqu6mjvRdvvHCURAj4bmyfG/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqu6mjvRdvvHCURAj4bmyfG/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:50.42Z",
      "updated_at" : "2016-10-06T23:01:50.42Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PI7rUZfEahb3XV35ytxvg6vW",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-06T23:01:47.77Z",
      "updated_at" : "2016-10-06T23:01:48.78Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIjBJYLdu5ST7CXwVPUCA4oZ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:31.32Z",
      "updated_at" : "2016-10-06T23:01:31.32Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjBJYLdu5ST7CXwVPUCA4oZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjBJYLdu5ST7CXwVPUCA4oZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjBJYLdu5ST7CXwVPUCA4oZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjBJYLdu5ST7CXwVPUCA4oZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PI51SDtxyBjHvRvNfkyLoRW9",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:31.32Z",
      "updated_at" : "2016-10-06T23:01:31.32Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI51SDtxyBjHvRvNfkyLoRW9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI51SDtxyBjHvRvNfkyLoRW9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI51SDtxyBjHvRvNfkyLoRW9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI51SDtxyBjHvRvNfkyLoRW9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIu6T8FrzuRTouRVnMAJD8Ha",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:31.32Z",
      "updated_at" : "2016-10-06T23:01:31.32Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6T8FrzuRTouRVnMAJD8Ha"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6T8FrzuRTouRVnMAJD8Ha/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6T8FrzuRTouRVnMAJD8Ha/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6T8FrzuRTouRVnMAJD8Ha/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        }
      }
    }, {
      "id" : "PIxj8y2NGTa16M2QiCZCGWba",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-06T23:01:31.32Z",
      "updated_at" : "2016-10-06T23:01:31.32Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxj8y2NGTa16M2QiCZCGWba"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxj8y2NGTa16M2QiCZCGWba/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxj8y2NGTa16M2QiCZCGWba/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxj8y2NGTa16M2QiCZCGWba/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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

curl https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Settlement;

$identity = Identity::retrieve('ID5YEW5VQNfrgZtpA4zkdkqK');
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

import io.crossriver.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STgE15agz7NyTRZaqDYWJsJ6",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "currency" : "USD",
  "created_at" : "2016-10-06T23:09:23.23Z",
  "updated_at" : "2016-10-06T23:09:23.24Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 104946,
  "total_fee" : 10496,
  "net_amount" : 94450,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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


curl https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Settlement;

$settlement = Settlement::retrieve('STgE15agz7NyTRZaqDYWJsJ6');

```
```java

import io.crossriver.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STgE15agz7NyTRZaqDYWJsJ6");

```
> Example Response:

```json
{
  "id" : "STgE15agz7NyTRZaqDYWJsJ6",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "currency" : "USD",
  "created_at" : "2016-10-06T23:09:23.12Z",
  "updated_at" : "2016-10-06T23:09:24.25Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 104946,
  "total_fee" : 10496,
  "net_amount" : 94450,
  "destination" : "PI7rUZfEahb3XV35ytxvg6vW",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
curl https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "destination": "PI7rUZfEahb3XV35ytxvg6vW"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "STgE15agz7NyTRZaqDYWJsJ6",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "currency" : "USD",
  "created_at" : "2016-10-06T23:09:23.12Z",
  "updated_at" : "2016-10-06T23:09:24.25Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 104946,
  "total_fee" : 10496,
  "net_amount" : 94450,
  "destination" : "PI7rUZfEahb3XV35ytxvg6vW",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "STgE15agz7NyTRZaqDYWJsJ6",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "currency" : "USD",
      "created_at" : "2016-10-06T23:09:23.12Z",
      "updated_at" : "2016-10-06T23:09:24.25Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 104946,
      "total_fee" : 10496,
      "net_amount" : 94450,
      "destination" : "PI7rUZfEahb3XV35ytxvg6vW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
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
curl https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "TRiicxj3CM2XAHZKRmjk6V7S",
      "amount" : 89,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "5c77b0b4-fc65-4bec-92ed-89503f224353",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "destination" : "PI7rUZfEahb3XV35ytxvg6vW",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:09:23.99Z",
      "updated_at" : "2016-10-06T23:09:24.44Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRiicxj3CM2XAHZKRmjk6V7S"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRiicxj3CM2XAHZKRmjk6V7S/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRiicxj3CM2XAHZKRmjk6V7S/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRiicxj3CM2XAHZKRmjk6V7S/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
        }
      }
    }, {
      "id" : "TRrc46BcVR6dcZUGGK5GPbN7",
      "amount" : 94361,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "f1ba545f-2988-4a67-9bad-7a17d0a067b7",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "destination" : "PI7rUZfEahb3XV35ytxvg6vW",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:09:23.99Z",
      "updated_at" : "2016-10-06T23:09:24.34Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRrc46BcVR6dcZUGGK5GPbN7"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRrc46BcVR6dcZUGGK5GPbN7/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRrc46BcVR6dcZUGGK5GPbN7/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRrc46BcVR6dcZUGGK5GPbN7/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7rUZfEahb3XV35ytxvg6vW"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "ready_to_settle_at" : "2016-10-06T23:03:35.51Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:05.81Z",
      "updated_at" : "2016-10-06T23:03:14.94Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        }
      }
    }, {
      "id" : "TRuL2qWzw9vbaVqoGRpVm7XD",
      "amount" : 104846,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "6bccf31c-dd07-4a6c-98eb-c7867de623aa",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "ready_to_settle_at" : "2016-10-06T23:03:35.51Z",
      "fee" : 10485,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:01:55.42Z",
      "updated_at" : "2016-10-06T23:02:06.50Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STgE15agz7NyTRZaqDYWJsJ6/transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRuL2qWzw9vbaVqoGRpVm7XD');



```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRuL2qWzw9vbaVqoGRpVm7XD");

```
> Example Response:

```json
{
  "id" : "TRuL2qWzw9vbaVqoGRpVm7XD",
  "amount" : 104846,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "6bccf31c-dd07-4a6c-98eb-c7867de623aa",
  "currency" : "USD",
  "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
  "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
  "ready_to_settle_at" : null,
  "fee" : 10485,
  "statement_descriptor" : "FNX*DUNDER MIFFLIN",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:01:55.42Z",
  "updated_at" : "2016-10-06T23:02:06.50Z",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
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

curl https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRuL2qWzw9vbaVqoGRpVm7XD');
$refund = $debit->reverse(50);
```
```java

import io.crossriver.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRd6yNXYgKKLosgcFvpiN5Yz",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "3b7be040-62b4-4cc9-a492-7b5d4858b862",
  "currency" : "USD",
  "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
  "source" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
  "destination" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*DUNDER MIFFLIN",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-06T23:02:02.96Z",
  "updated_at" : "2016-10-06T23:02:03.11Z",
  "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRd6yNXYgKKLosgcFvpiN5Yz"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRd6yNXYgKKLosgcFvpiN5Yz/payment_instruments"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Transfer;

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
      "id" : "TRnhNBkrUJZet8wKwLnh5A3U",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "FAILED",
      "trace_id" : "1079",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PIsAGPDDFM5jTVmrs78WEtcD",
      "destination" : "PIbsqGcCtsvo9WabdKngXh4G",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:24.51Z",
      "updated_at" : "2016-10-06T23:02:26.45Z",
      "merchant_identity" : "IDpxsLZvvGhT1jXWNiaPsxCU",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpxsLZvvGhT1jXWNiaPsxCU"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRnhNBkrUJZet8wKwLnh5A3U/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsAGPDDFM5jTVmrs78WEtcD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbsqGcCtsvo9WabdKngXh4G"
        }
      }
    }, {
      "id" : "TRgnjMyVkXEJcHBJ27XtuZJ1",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "a879bd08-a1f5-4b1b-941e-8ab23c4be6b2",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:05.81Z",
      "updated_at" : "2016-10-06T23:02:06.08Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRgnjMyVkXEJcHBJ27XtuZJ1/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        }
      }
    }, {
      "id" : "TRd6yNXYgKKLosgcFvpiN5Yz",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "3b7be040-62b4-4cc9-a492-7b5d4858b862",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "destination" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:02:02.80Z",
      "updated_at" : "2016-10-06T23:02:10.88Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRd6yNXYgKKLosgcFvpiN5Yz"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRd6yNXYgKKLosgcFvpiN5Yz/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        }
      }
    }, {
      "id" : "TRmyY4JTnuY1xX84B8gdZaQ8",
      "amount" : 575519,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "9f7207fb-9039-4b35-a157-15e1e7d8108d",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PItbBTq5XhURPLaDeVUPtGMM",
      "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "ready_to_settle_at" : null,
      "fee" : 57552,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:01:58.06Z",
      "updated_at" : "2016-10-06T23:02:05.55Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRmyY4JTnuY1xX84B8gdZaQ8"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRmyY4JTnuY1xX84B8gdZaQ8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRmyY4JTnuY1xX84B8gdZaQ8/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRmyY4JTnuY1xX84B8gdZaQ8/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbBTq5XhURPLaDeVUPtGMM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
        }
      }
    }, {
      "id" : "TRuL2qWzw9vbaVqoGRpVm7XD",
      "amount" : 104846,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "6bccf31c-dd07-4a6c-98eb-c7867de623aa",
      "currency" : "USD",
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "source" : "PI3N2hZ9Y1NM5d52RUDGdUeN",
      "destination" : "PI3wu6gcNwrnCKwXu3R1Q1fw",
      "ready_to_settle_at" : null,
      "fee" : 10485,
      "statement_descriptor" : "FNX*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-06T23:01:55.42Z",
      "updated_at" : "2016-10-06T23:02:06.50Z",
      "merchant_identity" : "ID5YEW5VQNfrgZtpA4zkdkqK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5YEW5VQNfrgZtpA4zkdkqK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRuL2qWzw9vbaVqoGRpVm7XD/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3N2hZ9Y1NM5d52RUDGdUeN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3wu6gcNwrnCKwXu3R1Q1fw"
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
automated notifications (i.e. events) on the CrossRiver API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7 \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHmSvsRzK7qeSaYnUNYNX4Ru",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
  "created_at" : "2016-10-06T23:01:34.81Z",
  "updated_at" : "2016-10-06T23:01:34.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHmSvsRzK7qeSaYnUNYNX4Ru"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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



curl https://api-staging.finix.io/webhooks/WHmSvsRzK7qeSaYnUNYNX4Ru \
    -H "Content-Type: application/vnd.json+api" \
    -u USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHmSvsRzK7qeSaYnUNYNX4Ru');



```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHmSvsRzK7qeSaYnUNYNX4Ru");

```
> Example Response:

```json
{
  "id" : "WHmSvsRzK7qeSaYnUNYNX4Ru",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
  "created_at" : "2016-10-06T23:01:34.82Z",
  "updated_at" : "2016-10-06T23:01:34.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHmSvsRzK7qeSaYnUNYNX4Ru"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
    -u  USvg7UiC7V7hZzvwQHqrzMCM:0355f91e-3c43-44e7-a86e-ce57eab048d7

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Webhook;

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
      "id" : "WHmSvsRzK7qeSaYnUNYNX4Ru",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APkv7UWjnRDVnTmfsQYBpW9j",
      "created_at" : "2016-10-06T23:01:34.82Z",
      "updated_at" : "2016-10-06T23:01:34.82Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHmSvsRzK7qeSaYnUNYNX4Ru"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkv7UWjnRDVnTmfsQYBpW9j"
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USvg7UiC7V7hZzvwQHqrzMCM', '0355f91e-3c43-44e7-a86e-ce57eab048d7');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

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
