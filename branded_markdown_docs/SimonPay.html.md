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
curl https://simonpay-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
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
  "id" : "ID2F1qUXi8acLBRKvgTVis6X",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T20:44:51.80Z",
  "updated_at" : "2016-09-09T20:44:51.80Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://simonpay-staging.finix.io/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://simonpay-staging.finix.io/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://simonpay-staging.finix.io/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://simonpay-staging.finix.io/identities`

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
curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	    "identity"=> "ID2F1qUXi8acLBRKvgTVis6X"
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
  "id" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "fingerprint" : "FPR966610431",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T20:45:02.22Z",
  "updated_at" : "2016-09-09T20:45:02.22Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
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

`POST https://simonpay-staging.finix.io/payment_instruments`

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
curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('ID2F1qUXi8acLBRKvgTVis6X');

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
  "id" : "MUp6PKPZz2B6UyXewi6VF891",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "verification" : "VI9xQZtcKHBmUjL2s3TffV39",
  "merchant_profile" : "MPw3D5En4yHoUPqW2aWj9NAq",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-09-09T20:45:04.70Z",
  "updated_at" : "2016-09-09T20:45:04.70Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/merchants/MUp6PKPZz2B6UyXewi6VF891"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/merchants/MUp6PKPZz2B6UyXewi6VF891/verifications"
    },
    "merchant_profile" : {
      "href" : "https://simonpay-staging.finix.io/merchant_profiles/MPw3D5En4yHoUPqW2aWj9NAq"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "verification" : {
      "href" : "https://simonpay-staging.finix.io/verifications/VI9xQZtcKHBmUjL2s3TffV39"
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

`POST https://simonpay-staging.finix.io/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://simonpay-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "James", 
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	        "first_name"=> "Sean", 
	        "last_name"=> "James", 
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
  "id" : "IDbKNL4wNvH4LX8gjAiMHkna",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
    "last_name" : "James",
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
  "created_at" : "2016-09-09T20:45:07.22Z",
  "updated_at" : "2016-09-09T20:45:07.22Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
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

`POST https://simonpay-staging.finix.io/identities`

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


curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "name": "Walter Kline", 
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
	    "identity": "IDbKNL4wNvH4LX8gjAiMHkna"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Walter Kline", 
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
	    "identity"=> "IDbKNL4wNvH4LX8gjAiMHkna"
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
  "id" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "fingerprint" : "FPR-1069441177",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Kline",
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
  "created_at" : "2016-09-09T20:45:08.22Z",
  "updated_at" : "2016-09-09T20:45:08.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDbKNL4wNvH4LX8gjAiMHkna",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "updates" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/updates"
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

`POST https://simonpay-staging.finix.io/payment_instruments`

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
curl https://simonpay-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "merchant_identity": "ID2F1qUXi8acLBRKvgTVis6X", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIdKWrcmhTBppGUdVwuGS1FE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID2F1qUXi8acLBRKvgTVis6X", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIdKWrcmhTBppGUdVwuGS1FE", 
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
  "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:17.43Z",
  "updated_at" : "2016-09-09T20:45:17.50Z",
  "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : false,
  "expires_at" : "2016-09-16T20:45:17.43Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`POST https://simonpay-staging.finix.io/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The `Payment Instrument` that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 6: Create an Authorization
```shell
curl https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUto6Zz3qqmD4oLoPjsmHYYD');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUto6Zz3qqmD4oLoPjsmHYYD");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxrxHfcyHXzRazE84NTqU8r",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:17.28Z",
  "updated_at" : "2016-09-09T20:45:19.02Z",
  "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : false,
  "expires_at" : "2016-09-16T20:45:17.28Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfer" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`PUT https://simonpay-staging.finix.io/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the  `Authorization`  you would like to capture in cents. Must be less than or equal to the amount of the `Authorization`
fee | *integer*, **optional** | Amount of the captured `Authorization` you would like to collect as your fee. Must be less than or equal to the amount

### Step 7: Create a Batch Settlment
```shell
curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;
use SimonPay\Resources\Settlement;

$identity = Identity::retrieve('ID2F1qUXi8acLBRKvgTVis6X');
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
  "id" : "STjuSeTGramjYhex86TmorB1",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "currency" : "USD",
  "created_at" : "2016-09-09T20:56:34.87Z",
  "updated_at" : "2016-09-09T20:56:34.96Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2019594,
  "total_fee" : 201961,
  "net_amount" : 1817633,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers"
    },
    "funding_transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`POST https://simonpay-staging.finix.io/identities/:IDENTITY_ID/settlements`

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
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

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
          applicationId: 'APvj26M9x69JKYRN9qZ9YL2Y',
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
  "id" : "TKfRV6f81vpEW1J2GK8taC7n",
  "fingerprint" : "FPR222704565",
  "created_at" : "2016-09-09T20:45:21.30Z",
  "updated_at" : "2016-09-09T20:45:21.30Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-09-10T20:45:21.28Z",
  "_links" : {
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```


```shell

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```

# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://simonpay-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "merchant_identity": "ID2F1qUXi8acLBRKvgTVis6X", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIdKWrcmhTBppGUdVwuGS1FE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID2F1qUXi8acLBRKvgTVis6X", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIdKWrcmhTBppGUdVwuGS1FE", 
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
  "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:17.43Z",
  "updated_at" : "2016-09-09T20:45:17.50Z",
  "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : false,
  "expires_at" : "2016-09-16T20:45:17.43Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`POST https://simonpay-staging.finix.io/authorizations`

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
curl https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUto6Zz3qqmD4oLoPjsmHYYD');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUto6Zz3qqmD4oLoPjsmHYYD");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxrxHfcyHXzRazE84NTqU8r",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:17.28Z",
  "updated_at" : "2016-09-09T20:45:19.02Z",
  "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : false,
  "expires_at" : "2016-09-16T20:45:17.28Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfer" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`PUT https://simonpay-staging.finix.io/authorizations/:AUTHORIZATION_ID`

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

curl https://simonpay-staging.finix.io/authorizations/AU8UxptTL6VGb9mb3HSxKTFR \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AU8UxptTL6VGb9mb3HSxKTFR",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:23.52Z",
  "updated_at" : "2016-09-09T20:45:24.83Z",
  "trace_id" : "7c0e553c-31e3-4c91-872a-9fb0648cc981",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : true,
  "expires_at" : "2016-09-16T20:45:23.52Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AU8UxptTL6VGb9mb3HSxKTFR"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://simonpay-staging.finix.io/authorizations/:AUTHORIZATION_ID`

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

curl https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Authorization;

$authorization = Authorization::retrieve('AUto6Zz3qqmD4oLoPjsmHYYD');

```
```java

import io.simonpay.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUto6Zz3qqmD4oLoPjsmHYYD");

```
> Example Response:

```json
{
  "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxrxHfcyHXzRazE84NTqU8r",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:17.28Z",
  "updated_at" : "2016-09-09T20:45:19.02Z",
  "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "is_void" : false,
  "expires_at" : "2016-09-16T20:45:17.28Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfer" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    }
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://simonpay-staging.finix.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
```
import io.payline.payments.processing.client.model.Authorization;

client.authorizationsClient().<Resources<Authorization>>resourcesIterator()
  .forEachRemaining(page-> {
    Collection<Authorization> authorizations = page.getContent();
    //do something
  });
```
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU8UxptTL6VGb9mb3HSxKTFR",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:23.52Z",
      "updated_at" : "2016-09-09T20:45:24.83Z",
      "trace_id" : "7c0e553c-31e3-4c91-872a-9fb0648cc981",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "is_void" : true,
      "expires_at" : "2016-09-16T20:45:23.52Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/authorizations/AU8UxptTL6VGb9mb3HSxKTFR"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        }
      }
    }, {
      "id" : "AUto6Zz3qqmD4oLoPjsmHYYD",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRxrxHfcyHXzRazE84NTqU8r",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:17.28Z",
      "updated_at" : "2016-09-09T20:45:19.02Z",
      "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "is_void" : false,
      "expires_at" : "2016-09-16T20:45:17.28Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/authorizations/AUto6Zz3qqmD4oLoPjsmHYYD"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "transfer" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/authorizations?offset=0&limit=20&sort=created_at,desc"
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

`GET https://simonpay-staging.finix.io/authorizations/`

# Disputes

Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl https://simonpay-staging.finix.io/disputes/DI9qDTf6ub11tJ8TeKPFZ3zt \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Dispute;

$dispute = Dispute::retrieve('DI9qDTf6ub11tJ8TeKPFZ3zt');

```
```java

import io.simonpay.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("DI9qDTf6ub11tJ8TeKPFZ3zt");

```
> Example Response:

```json
{
  "id" : "DI9qDTf6ub11tJ8TeKPFZ3zt",
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "amount" : 0,
  "state" : "PENDING",
  "transfer" : "TRa7ynAZK4x5eM37bBwGt61M",
  "reason" : "FRAUD",
  "identity" : "IDbKNL4wNvH4LX8gjAiMHkna",
  "created_at" : "2016-09-09T20:46:02.54Z",
  "updated_at" : "2016-09-09T20:46:02.54Z",
  "occurred_at" : "2016-09-09T20:45:48.57Z",
  "respond_by" : "2016-09-16T20:46:03.06Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/disputes/DI9qDTf6ub11tJ8TeKPFZ3zt"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfer" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRa7ynAZK4x5eM37bBwGt61M"
    },
    "evidence" : {
      "href" : "https://simonpay-staging.finix.io/disputes/DI9qDTf6ub11tJ8TeKPFZ3zt/evidence"
    }
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/disputes/:DISPUTE_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:DISPUTE_ID | ID of the Dispute


## List all Disputes
```shell
curl https://simonpay-staging.finix.io/disputes/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java
import io.simonpay.payments.processing.client.model.Dispute;

transfer.disputeClient().<Resources<Dispute>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Dispute> disputes = page.getContent();
  })
```
> Example Response:

```json
{
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/disputes?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 0
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/disputes/`


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


curl https://simonpay-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "James", 
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	        "first_name"=> "Sean", 
	        "last_name"=> "James", 
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
  "id" : "IDbKNL4wNvH4LX8gjAiMHkna",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
    "last_name" : "James",
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
  "created_at" : "2016-09-09T20:45:07.22Z",
  "updated_at" : "2016-09-09T20:45:07.22Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://simonpay-staging.finix.io/identities`

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


curl https://simonpay-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
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
  "id" : "ID2F1qUXi8acLBRKvgTVis6X",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T20:44:51.80Z",
  "updated_at" : "2016-09-09T20:44:51.80Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
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

`POST https://simonpay-staging.finix.io/identities`

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

curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('ID2F1qUXi8acLBRKvgTVis6X');
```
```java

import io.simonpay.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID2F1qUXi8acLBRKvgTVis6X");

```
> Example Response:

```json
{
  "id" : "ID2F1qUXi8acLBRKvgTVis6X",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T20:44:51.73Z",
  "updated_at" : "2016-09-09T20:44:51.73Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl https://simonpay-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "IDbKNL4wNvH4LX8gjAiMHkna",
      "entity" : {
        "title" : null,
        "first_name" : "Sean",
        "last_name" : "James",
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
      "created_at" : "2016-09-09T20:45:07.16Z",
      "updated_at" : "2016-09-09T20:45:07.16Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDqqsk8zmSkynApYR2xP2adn",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-09-09T20:45:01.21Z",
      "updated_at" : "2016-09-09T20:45:01.21Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqqsk8zmSkynApYR2xP2adn/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDaz19ftFLs88QprgYF6pSFX",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-09-09T20:45:00.24Z",
      "updated_at" : "2016-09-09T20:45:00.24Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaz19ftFLs88QprgYF6pSFX/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDmWjGgbUJWjxA7T3wi3rNLT",
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
      "created_at" : "2016-09-09T20:44:59.23Z",
      "updated_at" : "2016-09-09T20:44:59.23Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDmWjGgbUJWjxA7T3wi3rNLT/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDqHJckZS1ygg6KpLnmCBzHY",
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
      "created_at" : "2016-09-09T20:44:58.30Z",
      "updated_at" : "2016-09-09T20:44:58.30Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDqHJckZS1ygg6KpLnmCBzHY/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDgDRweLa6zabgzsqNsASUr8",
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
      "created_at" : "2016-09-09T20:44:57.27Z",
      "updated_at" : "2016-09-09T20:44:57.27Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDgDRweLa6zabgzsqNsASUr8/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDnoXF5z7LiyR5qYNqhgFfF4",
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
      "created_at" : "2016-09-09T20:44:56.28Z",
      "updated_at" : "2016-09-09T20:44:56.28Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDnoXF5z7LiyR5qYNqhgFfF4/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDaxFy3XSQYDFQhR39VVR4oH",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "PARTNERSHIP",
        "doing_business_as" : "Pollos Hermanos",
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
        "url" : "www.PollosHermanos.com",
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
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-09-09T20:44:55.35Z",
      "updated_at" : "2016-09-09T20:44:55.35Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDaxFy3XSQYDFQhR39VVR4oH/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "ID4iTqxpLzwZuQwgNt3Vaqmi",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-09-09T20:44:54.00Z",
      "updated_at" : "2016-09-09T20:44:54.00Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID4iTqxpLzwZuQwgNt3Vaqmi/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "IDsJX9S36D3NmVrTKmTr2ExC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-09-09T20:44:52.79Z",
      "updated_at" : "2016-09-09T20:44:52.79Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDsJX9S36D3NmVrTKmTr2ExC/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "ID2F1qUXi8acLBRKvgTVis6X",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-09-09T20:44:51.73Z",
      "updated_at" : "2016-09-09T20:44:51.73Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "ID6qbfsX3BgWYzAwR5VzGFT2",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Google",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Google",
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
        "application_name" : "Google"
      },
      "created_at" : "2016-09-09T20:44:46.29Z",
      "updated_at" : "2016-09-09T20:44:46.45Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/verifications"
        },
        "merchants" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/merchants"
        },
        "settlements" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/settlements"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/authorizations"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2/disputes"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://simonpay-staging.finix.io/identities/`


## Update an Identity
```shell
curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Daphne", 
	        "last_name": "James", 
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
	        "doing_business_as": "Prestige World Wide", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Prestige World Wide", 
	        "url": "www.PrestigeWorldWide.com", 
	        "business_name": "Prestige World Wide", 
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID2F1qUXi8acLBRKvgTVis6X",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Daphne",
    "last_name" : "James",
    "email" : "user@example.org",
    "business_name" : "Prestige World Wide",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Prestige World Wide",
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
    "key" : "value_2"
  },
  "created_at" : "2016-09-09T20:44:51.73Z",
  "updated_at" : "2016-09-09T20:45:45.46Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/verifications"
    },
    "merchants" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants"
    },
    "settlements" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/authorizations"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/transfers"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/payment_instruments"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/disputes"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
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
 processor.](#update-merchant-information-on-processor)


#### HTTP Request

`POST https://simonpay-staging.finix.io/identities`

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

curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;

$identity = Identity::retrieve('ID2F1qUXi8acLBRKvgTVis6X');

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
  "id" : "MUp6PKPZz2B6UyXewi6VF891",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "verification" : "VI9xQZtcKHBmUjL2s3TffV39",
  "merchant_profile" : "MPw3D5En4yHoUPqW2aWj9NAq",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-09-09T20:45:04.70Z",
  "updated_at" : "2016-09-09T20:45:04.70Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/merchants/MUp6PKPZz2B6UyXewi6VF891"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/merchants/MUp6PKPZz2B6UyXewi6VF891/verifications"
    },
    "merchant_profile" : {
      "href" : "https://simonpay-staging.finix.io/merchant_profiles/MPw3D5En4yHoUPqW2aWj9NAq"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "verification" : {
      "href" : "https://simonpay-staging.finix.io/verifications/VI9xQZtcKHBmUjL2s3TffV39"
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

`POST https://simonpay-staging.finix.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Identity;
use SimonPay\Resources\Settlement;

$identity = Identity::retrieve('ID2F1qUXi8acLBRKvgTVis6X');
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
  "id" : "STjuSeTGramjYhex86TmorB1",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "currency" : "USD",
  "created_at" : "2016-09-09T20:56:34.87Z",
  "updated_at" : "2016-09-09T20:56:34.96Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2019594,
  "total_fee" : 201961,
  "net_amount" : 1817633,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers"
    },
    "funding_transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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
request to the transfers link (i.e. POST https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://simonpay-staging.finix.io/identities/:IDENTITY_ID/settlements`

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


curl https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Settlement;

$settlement = Settlement::retrieve('STjuSeTGramjYhex86TmorB1');

```
```java

import io.simonpay.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STjuSeTGramjYhex86TmorB1");

```
> Example Response:

```json
{
  "id" : "STjuSeTGramjYhex86TmorB1",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "currency" : "USD",
  "created_at" : "2016-09-09T20:56:34.72Z",
  "updated_at" : "2016-09-09T20:56:37.49Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2019594,
  "total_fee" : 201961,
  "net_amount" : 1817633,
  "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers"
    },
    "funding_transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkq2yiDni9oFNpcuRNDMPmA:b559b81b-5b6e-4e22-aba5-81fd12265314 \
    -X PUT \
    -d '
	{
	    "destination": "PI7B2Y3cCokTTpwkvyi3w9av"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "STjuSeTGramjYhex86TmorB1",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "currency" : "USD",
  "created_at" : "2016-09-09T20:56:34.72Z",
  "updated_at" : "2016-09-09T20:56:37.49Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2019594,
  "total_fee" : 201961,
  "net_amount" : 1817633,
  "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers"
    },
    "funding_transfers" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
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

`POST https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID`

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
curl https://simonpay-staging.finix.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "STjuSeTGramjYhex86TmorB1",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "currency" : "USD",
      "created_at" : "2016-09-09T20:56:34.72Z",
      "updated_at" : "2016-09-09T20:56:37.49Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 2019594,
      "total_fee" : 201961,
      "net_amount" : 1817633,
      "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers"
        },
        "funding_transfers" : {
          "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements?offset=0&limit=20&sort=created_at,desc"
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

`GET https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "TR7Q5gpY7aM1nHEBqC7JkCcN",
      "amount" : 421466,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "09168d1d-91f6-4bef-b319-56117b24c7a8",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIkXGzoygmDk5AG8VsofDD1v",
      "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:56:37.13Z",
      "updated_at" : "2016-09-09T20:56:37.88Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR7Q5gpY7aM1nHEBqC7JkCcN"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR7Q5gpY7aM1nHEBqC7JkCcN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR7Q5gpY7aM1nHEBqC7JkCcN/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR7Q5gpY7aM1nHEBqC7JkCcN/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
        }
      }
    }, {
      "id" : "TRahJndhkLFW8wdCUGVEoYBi",
      "amount" : 596079,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "5cf6f205-0d93-4ba4-a0fc-87646c8c7abc",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIkXGzoygmDk5AG8VsofDD1v",
      "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:56:37.13Z",
      "updated_at" : "2016-09-09T20:56:37.80Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRahJndhkLFW8wdCUGVEoYBi"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRahJndhkLFW8wdCUGVEoYBi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRahJndhkLFW8wdCUGVEoYBi/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRahJndhkLFW8wdCUGVEoYBi/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
        }
      }
    }, {
      "id" : "TRjctboG6do5bC4xgzGrexxu",
      "amount" : 90,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "639a374d-4011-4e95-861b-b776326063bb",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIkXGzoygmDk5AG8VsofDD1v",
      "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:56:37.13Z",
      "updated_at" : "2016-09-09T20:56:37.64Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRjctboG6do5bC4xgzGrexxu"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRjctboG6do5bC4xgzGrexxu/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRjctboG6do5bC4xgzGrexxu/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRjctboG6do5bC4xgzGrexxu/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
        }
      }
    }, {
      "id" : "TRqEjvVEbd66JEcWuV4G6HFn",
      "amount" : 799999,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "dfcb2e9c-72a2-4524-a5f9-77f6f3184b66",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIkXGzoygmDk5AG8VsofDD1v",
      "destination" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:56:37.13Z",
      "updated_at" : "2016-09-09T20:56:37.71Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRqEjvVEbd66JEcWuV4G6HFn"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRqEjvVEbd66JEcWuV4G6HFn/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRqEjvVEbd66JEcWuV4G6HFn/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRqEjvVEbd66JEcWuV4G6HFn/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/funding_transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 4
  }
}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "TRa7ynAZK4x5eM37bBwGt61M",
      "amount" : 888888,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "392fbce3-e5fc-4e56-ae26-f532cf6d1f3b",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : "2016-09-09T20:47:35.13Z",
      "fee" : 88889,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:48.57Z",
      "updated_at" : "2016-09-09T20:46:03.08Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRa7ynAZK4x5eM37bBwGt61M"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRa7ynAZK4x5eM37bBwGt61M/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRa7ynAZK4x5eM37bBwGt61M/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRa7ynAZK4x5eM37bBwGt61M/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    }, {
      "id" : "TRxrxHfcyHXzRazE84NTqU8r",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : "2016-09-09T20:47:35.13Z",
      "fee" : 10,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:18.74Z",
      "updated_at" : "2016-09-09T20:46:08.55Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    }, {
      "id" : "TRnoZ6TGApGq7LvgpFYcCvSh",
      "amount" : 662310,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "13e065c6-11fe-4bad-818f-6ef8a852ff2e",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : "2016-09-09T20:47:35.13Z",
      "fee" : 66231,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:11.70Z",
      "updated_at" : "2016-09-09T20:46:04.61Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    }, {
      "id" : "TR6ghb4zTRmAF7YEQR3u8BbX",
      "amount" : 468296,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "ee448f39-7db4-48fb-aad5-102148a78b34",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : "2016-09-09T20:47:35.13Z",
      "fee" : 46830,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:09.65Z",
      "updated_at" : "2016-09-09T20:46:04.96Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/settlements/STjuSeTGramjYhex86TmorB1/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 4
  }
}
```

List the batch of `Transfers` of type `DEBIT` and `REFUND` that comprise the net
 settled amount of a `Settlement`.

#### HTTP Request

`GET https://simonpay-staging.finix.io/settlements/:SETTLEMENT_ID/transfers`


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

curl https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Transfer;

$transfer = Transfer::retrieve('TRnoZ6TGApGq7LvgpFYcCvSh');



```
```java

import io.simonpay.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRnoZ6TGApGq7LvgpFYcCvSh");

```
> Example Response:

```json
{
  "id" : "TRnoZ6TGApGq7LvgpFYcCvSh",
  "amount" : 662310,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "13e065c6-11fe-4bad-818f-6ef8a852ff2e",
  "currency" : "USD",
  "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
  "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
  "ready_to_settle_at" : null,
  "fee" : 66231,
  "statement_descriptor" : "SPN*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:11.70Z",
  "updated_at" : "2016-09-09T20:45:12.05Z",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "self" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "reversals" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/reversals"
    },
    "disputes" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/disputes"
    },
    "source" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
    },
    "destination" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
    }
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Transfer;

$debit = Transfer::retrieve('TRnoZ6TGApGq7LvgpFYcCvSh');
$refund = $debit->reverse(50);
```
```java

import io.simonpay.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TR5DBmb6n5dfx8H6zVqcq5v5",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "797b2710-8953-4961-8970-0fd94a70a499",
  "currency" : "USD",
  "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
  "source" : "PIkXGzoygmDk5AG8VsofDD1v",
  "destination" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "SPN*PAWNY CITY HALL",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T20:45:15.53Z",
  "updated_at" : "2016-09-09T20:45:15.69Z",
  "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "self" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TR5DBmb6n5dfx8H6zVqcq5v5"
    },
    "parent" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh"
    },
    "destination" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
    },
    "merchant_identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "payment_instruments" : {
      "href" : "https://simonpay-staging.finix.io/transfers/TR5DBmb6n5dfx8H6zVqcq5v5/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://simonpay-staging.finix.io/transfers/:TRANSFER_ID/reversals`

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
curl https://simonpay-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "TRxrxHfcyHXzRazE84NTqU8r",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "195f2c2b-5d32-4b57-9c00-9f7f548a640f",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:18.74Z",
      "updated_at" : "2016-09-09T20:45:19.02Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRxrxHfcyHXzRazE84NTqU8r/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    }, {
      "id" : "TR5DBmb6n5dfx8H6zVqcq5v5",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "797b2710-8953-4961-8970-0fd94a70a499",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIkXGzoygmDk5AG8VsofDD1v",
      "destination" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:15.32Z",
      "updated_at" : "2016-09-09T20:45:15.69Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR5DBmb6n5dfx8H6zVqcq5v5"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR5DBmb6n5dfx8H6zVqcq5v5/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "parent" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        }
      }
    }, {
      "id" : "TRnoZ6TGApGq7LvgpFYcCvSh",
      "amount" : 662310,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "13e065c6-11fe-4bad-818f-6ef8a852ff2e",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : null,
      "fee" : 66231,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:11.70Z",
      "updated_at" : "2016-09-09T20:45:12.05Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TRnoZ6TGApGq7LvgpFYcCvSh/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    }, {
      "id" : "TR6ghb4zTRmAF7YEQR3u8BbX",
      "amount" : 468296,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "ee448f39-7db4-48fb-aad5-102148a78b34",
      "currency" : "USD",
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "source" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "destination" : "PIkXGzoygmDk5AG8VsofDD1v",
      "ready_to_settle_at" : null,
      "fee" : 46830,
      "statement_descriptor" : "SPN*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T20:45:09.65Z",
      "updated_at" : "2016-09-09T20:45:10.35Z",
      "merchant_identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "self" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX"
        },
        "payment_instruments" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "reversals" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/reversals"
        },
        "disputes" : {
          "href" : "https://simonpay-staging.finix.io/transfers/TR6ghb4zTRmAF7YEQR3u8BbX/disputes"
        },
        "source" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "destination" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://simonpay-staging.finix.io/transfers`
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

curl https://simonpay-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
  "id" : "WHiiEvg2ksMVBsoU3p4a3Sp2",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
  "created_at" : "2016-09-09T20:44:50.71Z",
  "updated_at" : "2016-09-09T20:44:50.71Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/webhooks/WHiiEvg2ksMVBsoU3p4a3Sp2"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

#### HTTP Request

`POST https://simonpay-staging.finix.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

## Retrieve a Webhook

```shell



curl https://simonpay-staging.finix.io/webhooks/WHiiEvg2ksMVBsoU3p4a3Sp2 \
    -H "Content-Type: application/vnd.json+api" \
    -u US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\Webhook;

$webhook = Webhook::retrieve('WHiiEvg2ksMVBsoU3p4a3Sp2');



```
```java

import io.simonpay.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHiiEvg2ksMVBsoU3p4a3Sp2");

```
> Example Response:

```json
{
  "id" : "WHiiEvg2ksMVBsoU3p4a3Sp2",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
  "created_at" : "2016-09-09T20:44:50.73Z",
  "updated_at" : "2016-09-09T20:44:50.73Z",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/webhooks/WHiiEvg2ksMVBsoU3p4a3Sp2"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://simonpay-staging.finix.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "WHiiEvg2ksMVBsoU3p4a3Sp2",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APvj26M9x69JKYRN9qZ9YL2Y",
      "created_at" : "2016-09-09T20:44:50.73Z",
      "updated_at" : "2016-09-09T20:44:50.73Z",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/webhooks/WHiiEvg2ksMVBsoU3p4a3Sp2"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/webhooks?offset=0&limit=20&sort=created_at,desc"
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

`GET https://simonpay-staging.finix.io/webhooks`
    

## Sample Payloads


```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Create a Card
```shell


curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "name": "Walter Kline", 
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
	    "identity": "IDbKNL4wNvH4LX8gjAiMHkna"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Walter Kline", 
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
	    "identity"=> "IDbKNL4wNvH4LX8gjAiMHkna"
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
  "id" : "PIdKWrcmhTBppGUdVwuGS1FE",
  "fingerprint" : "FPR-1069441177",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Kline",
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
  "created_at" : "2016-09-09T20:45:08.22Z",
  "updated_at" : "2016-09-09T20:45:08.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDbKNL4wNvH4LX8gjAiMHkna",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "updates" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/updates"
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

`POST https://simonpay-staging.finix.io/payment_instruments`

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

curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
	    "identity"=> "ID2F1qUXi8acLBRKvgTVis6X"
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
  "id" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "fingerprint" : "FPR966610431",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T20:45:02.22Z",
  "updated_at" : "2016-09-09T20:45:02.22Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

#### HTTP Request

`POST https://simonpay-staging.finix.io/payment_instruments`

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
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

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
          applicationId: 'APvj26M9x69JKYRN9qZ9YL2Y',
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
  "id" : "TKfRV6f81vpEW1J2GK8taC7n",
  "fingerprint" : "FPR222704565",
  "created_at" : "2016-09-09T20:45:21.30Z",
  "updated_at" : "2016-09-09T20:45:21.30Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-09-10T20:45:21.28Z",
  "_links" : {
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

```shell
curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "token": "TKfRV6f81vpEW1J2GK8taC7n", 
	    "type": "TOKEN", 
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKfRV6f81vpEW1J2GK8taC7n", 
	    "type": "TOKEN", 
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
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
  "id" : "PIfRV6f81vpEW1J2GK8taC7n",
  "fingerprint" : "FPR-752937284",
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
  "created_at" : "2016-09-09T20:45:22.23Z",
  "updated_at" : "2016-09-09T20:45:22.23Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "updates" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/updates"
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

`POST https://simonpay-staging.finix.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
    -d '
	{
	    "token": "TKfRV6f81vpEW1J2GK8taC7n", 
	    "type": "TOKEN", 
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKfRV6f81vpEW1J2GK8taC7n", 
	    "type": "TOKEN", 
	    "identity": "ID2F1qUXi8acLBRKvgTVis6X"
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
  "id" : "PIfRV6f81vpEW1J2GK8taC7n",
  "fingerprint" : "FPR-752937284",
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
  "created_at" : "2016-09-09T20:45:22.23Z",
  "updated_at" : "2016-09-09T20:45:22.23Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    },
    "updates" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/updates"
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

`POST https://simonpay-staging.finix.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Fetch a Payment Instrument

```shell


curl https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();

use SimonPay\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI7B2Y3cCokTTpwkvyi3w9av');

```
```java

import io.simonpay.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI7B2Y3cCokTTpwkvyi3w9av")

```
> Example Response:

```json
{
  "id" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "fingerprint" : "FPR966610431",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T20:45:02.12Z",
  "updated_at" : "2016-09-09T20:45:03.49Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
    }
  }
}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET https://simonpay-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965 \
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
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
require(__DIR__ . '/src/SimonPay/Bootstrap.php');
SimonPay\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PI7B2Y3cCokTTpwkvyi3w9av",
  "fingerprint" : "FPR966610431",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T20:45:02.12Z",
  "updated_at" : "2016-09-09T20:45:03.49Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
    },
    "authorizations" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/authorizations"
    },
    "identity" : {
      "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
    },
    "transfers" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/transfers"
    },
    "verifications" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/verifications"
    },
    "application" : {
      "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
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

`PUT https://simonpay-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


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
curl https://simonpay-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4eAvYntB9wTXD5qN7wGweJ:edd7cd57-0923-469f-bebc-aa2fda547965
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/SimonPay/Settings.php');
SimonPay\Settings::configure('https://simonpay-staging.finix.io', 'US4eAvYntB9wTXD5qN7wGweJ', 'edd7cd57-0923-469f-bebc-aa2fda547965');
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
      "id" : "PIfRV6f81vpEW1J2GK8taC7n",
      "fingerprint" : "FPR-752937284",
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
      "created_at" : "2016-09-09T20:45:22.09Z",
      "updated_at" : "2016-09-09T20:45:22.09Z",
      "instrument_type" : "PAYMENT_CARD",
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "updates" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIfRV6f81vpEW1J2GK8taC7n/updates"
        }
      }
    }, {
      "id" : "PIdKWrcmhTBppGUdVwuGS1FE",
      "fingerprint" : "FPR-1069441177",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Walter Kline",
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
      "created_at" : "2016-09-09T20:45:08.14Z",
      "updated_at" : "2016-09-09T20:45:17.50Z",
      "instrument_type" : "PAYMENT_CARD",
      "identity" : "IDbKNL4wNvH4LX8gjAiMHkna",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/IDbKNL4wNvH4LX8gjAiMHkna"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        },
        "updates" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIdKWrcmhTBppGUdVwuGS1FE/updates"
        }
      }
    }, {
      "id" : "PIpupgko78LKogAnMHTNX3X3",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:45:04.56Z",
      "updated_at" : "2016-09-09T20:45:04.56Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIpupgko78LKogAnMHTNX3X3"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIpupgko78LKogAnMHTNX3X3/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIpupgko78LKogAnMHTNX3X3/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIpupgko78LKogAnMHTNX3X3/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PIe713AhRsir6JPuaJt5adxE",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:45:04.56Z",
      "updated_at" : "2016-09-09T20:45:04.56Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIe713AhRsir6JPuaJt5adxE"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIe713AhRsir6JPuaJt5adxE/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIe713AhRsir6JPuaJt5adxE/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIe713AhRsir6JPuaJt5adxE/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PIkXGzoygmDk5AG8VsofDD1v",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:45:04.56Z",
      "updated_at" : "2016-09-09T20:45:04.56Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIkXGzoygmDk5AG8VsofDD1v/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PI7B2Y3cCokTTpwkvyi3w9av",
      "fingerprint" : "FPR966610431",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-09-09T20:45:02.12Z",
      "updated_at" : "2016-09-09T20:45:03.49Z",
      "instrument_type" : "BANK_ACCOUNT",
      "identity" : "ID2F1qUXi8acLBRKvgTVis6X",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2F1qUXi8acLBRKvgTVis6X"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI7B2Y3cCokTTpwkvyi3w9av/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PI5t4z8DFM2i5AvAMZfVc5vD",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:44:47.22Z",
      "updated_at" : "2016-09-09T20:44:47.22Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2f67hZpBDEM1xBfKSp7LPD",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI5t4z8DFM2i5AvAMZfVc5vD"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI5t4z8DFM2i5AvAMZfVc5vD/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID2f67hZpBDEM1xBfKSp7LPD"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI5t4z8DFM2i5AvAMZfVc5vD/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI5t4z8DFM2i5AvAMZfVc5vD/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PIuzS7LxXzxCAAyiZJdx9i2d",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:44:47.22Z",
      "updated_at" : "2016-09-09T20:44:47.22Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6qbfsX3BgWYzAwR5VzGFT2",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIuzS7LxXzxCAAyiZJdx9i2d"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIuzS7LxXzxCAAyiZJdx9i2d/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIuzS7LxXzxCAAyiZJdx9i2d/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIuzS7LxXzxCAAyiZJdx9i2d/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PIjtkFHPsGV2ejaAVS9spm9N",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:44:47.22Z",
      "updated_at" : "2016-09-09T20:44:47.22Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6qbfsX3BgWYzAwR5VzGFT2",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIjtkFHPsGV2ejaAVS9spm9N"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIjtkFHPsGV2ejaAVS9spm9N/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIjtkFHPsGV2ejaAVS9spm9N/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PIjtkFHPsGV2ejaAVS9spm9N/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    }, {
      "id" : "PI2NNJiPUQJ2CSv16LVseHdt",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T20:44:47.22Z",
      "updated_at" : "2016-09-09T20:44:47.22Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6qbfsX3BgWYzAwR5VzGFT2",
      "_links" : {
        "self" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI2NNJiPUQJ2CSv16LVseHdt"
        },
        "authorizations" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI2NNJiPUQJ2CSv16LVseHdt/authorizations"
        },
        "identity" : {
          "href" : "https://simonpay-staging.finix.io/identities/ID6qbfsX3BgWYzAwR5VzGFT2"
        },
        "transfers" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI2NNJiPUQJ2CSv16LVseHdt/transfers"
        },
        "verifications" : {
          "href" : "https://simonpay-staging.finix.io/payment_instruments/PI2NNJiPUQJ2CSv16LVseHdt/verifications"
        },
        "application" : {
          "href" : "https://simonpay-staging.finix.io/applications/APvj26M9x69JKYRN9qZ9YL2Y"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://simonpay-staging.finix.io/payment_instruments?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 10
  }
}
```

#### HTTP Request

`GET https://simonpay-staging.finix.io/payment_instruments`

