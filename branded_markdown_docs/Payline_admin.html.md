---
title: Payline API Reference

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

These guides provide a collection of resources for utilizing the Payline
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
## Authentication



```shell
# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```java

```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `UShEXo1fxJjJmK1eB3YScLM7`

- Password: `c148bc82-13b6-40e4-a495-9fe8fd29feae`

- Application ID: `APgLUKnuNCzL38SGfxgwDqyR`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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
import io.payline.payments.processing.client.model.Identity;

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
  "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
  "created_at" : "2016-10-04T18:25:24.17Z",
  "updated_at" : "2016-10-04T18:25:24.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://api-test.payline.io/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://api-test.payline.io/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://api-test.payline.io/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-test.payline.io/identities`

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
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "IDfVdfQ6jCMWctb33WQdCGjV"
	));
$bank_account = $bank_account->save();

```
```java
import io.payline.payments.processing.client.model.BankAccount;

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
  "id" : "PI5C4UNzdxx78okAGBCwwSMM",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T18:25:35.29Z",
  "updated_at" : "2016-10-04T18:25:35.29Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/payment_instruments`

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
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfVdfQ6jCMWctb33WQdCGjV');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "verification" : "VIbN4bZc1k32UmEw2J6yqgS8",
  "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T18:25:38.88Z",
  "updated_at" : "2016-10-04T18:25:38.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIbN4bZc1k32UmEw2J6yqgS8"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Michae", 
	        "last_name": "Lopez", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Michae", 
	        "last_name"=> "Lopez", 
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

import io.payline.payments.processing.client.model.Identity;

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
  "id" : "IDjbaEZJwYceHqTFXLHfjq5H",
  "entity" : {
    "title" : null,
    "first_name" : "Michae",
    "last_name" : "Lopez",
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
  "created_at" : "2016-10-04T18:25:41.41Z",
  "updated_at" : "2016-10-04T18:25:41.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/identities`

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


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "name": "Daphne Sterling", 
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
	    "identity": "IDjbaEZJwYceHqTFXLHfjq5H"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Daphne Sterling", 
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
	    "identity"=> "IDjbaEZJwYceHqTFXLHfjq5H"
	));
$card = $card->save();


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "fingerprint" : "FPR2061140472",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Daphne Sterling",
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
  "created_at" : "2016-10-04T18:25:42.25Z",
  "updated_at" : "2016-10-04T18:25:42.25Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDjbaEZJwYceHqTFXLHfjq5H",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/updates"
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

`POST https://api-test.payline.io/payment_instruments`

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
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "merchant_identity": "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuMKvG5kAzpCWBHkLL3ugx2", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuMKvG5kAzpCWBHkLL3ugx2", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```java
import io.payline.payments.processing.client.model.Authorization;

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
  "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:53.85Z",
  "updated_at" : "2016-10-04T18:25:53.86Z",
  "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : false,
  "expires_at" : "2016-10-11T18:25:53.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`POST https://api-test.payline.io/authorizations`

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
curl https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUdLMjYQtG2coSk5FjFxFbBX');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUdLMjYQtG2coSk5FjFxFbBX");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRiNk2zSe6RjKpC7DQBdhX7y",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:53.71Z",
  "updated_at" : "2016-10-04T18:25:55.55Z",
  "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : false,
  "expires_at" : "2016-10-11T18:25:53.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`PUT https://api-test.payline.io/authorizations/:AUTHORIZATION_ID`

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
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDfVdfQ6jCMWctb33WQdCGjV');
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
import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STdH6Ucpt6D6cpgrK4aMwmbW",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "currency" : "USD",
  "created_at" : "2016-10-04T18:33:07.87Z",
  "updated_at" : "2016-10-04T18:33:07.89Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 210466,
  "total_fee" : 21048,
  "net_amount" : 189418,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Embedded Tokenization Using Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to Payline. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/rserna2010/47kgeao9/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the Payline API.
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
          applicationId: 'APgLUKnuNCzL38SGfxgwDqyR',
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
  "id" : "TKqh6bJbgoAY7tzW4h5RvfLj",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-04T18:25:57.64Z",
  "updated_at" : "2016-10-04T18:25:57.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-05T18:25:57.64Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	});
$card = $card->save();

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIqh6bJbgoAY7tzW4h5RvfLj",
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
  "created_at" : "2016-10-04T18:25:58.90Z",
  "updated_at" : "2016-10-04T18:25:58.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/updates"
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

`POST https://api-test.payline.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


# Admin Guides

## Overview
These guides provide an overview of the API's administrative capabilities and
restricted requests not exposed to general users.

1. [Create an Application](#creating-an-application): A guide to programatically creating
 a new `Applications` and its API keys

2. [Tokenization.js](#tokenization-js): This guide explains how to properly
tokenize cards in production via our javascript client. Utilization of the
Tokenization.js client is an advanced feature that should only be exposed to
end-users that are PCI compliant.

## Creating an Application

This guide walks step by step how to create an `Application` via the API. To do
so you must make 3 API requests.

1. Create a new `User` with ROLE_PARTNER that will be the owner of the `Application`

2. Create the `Application` resource

3. Enable a processor for the `Application` where merchants will be onboarded and
transactions will be processed.

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can perform these requests.
</aside>

### Step 1: Create a new User
```shell
curl https://api-test.payline.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "role": "ROLE_PARTNER"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UShEXo1fxJjJmK1eB3YScLM7",
  "password" : "c148bc82-13b6-40e4-a495-9fe8fd29feae",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:15.41Z",
  "updated_at" : "2016-10-04T18:25:15.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UShEXo1fxJjJmK1eB3YScLM7"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    }
  }
}
```

We'll first start by creating a new `User` with ROLE_PARTNER permissions that
will be the owner of this new `Application`. Note that this is the equivalent of
provisioning API keys (i.e. credentials) that are not associated with any single
`Application`. You'll want to store the `password` as it is only returned once.
The keys will be associated in the next step.


#### HTTP Request

`POST https://api-test.payline.io/users`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user (use ROLE_PARTNER when creating a new `Application`)

### Step 2: Create the Application
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "UShEXo1fxJjJmK1eB3YScLM7", 
	    "entity": {
	        "business_type": "LIMITED_LIABILITY_COMPANY", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 5
	        }, 
	        "settlement_bank_account": "CORPORATE", 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "max_transaction_amount": 12000, 
	        "phone": "1234567890", 
	        "doing_business_as": "Facebook", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Facebook", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "UShEXo1fxJjJmK1eB3YScLM7", 
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
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-04T18:25:16.87Z",
  "updated_at" : "2016-10-04T18:25:16.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

Now that we have a new owner `User` let's create their `Application`. We'll be
collecting the same basic KYC and underwrting information that we typically
collect for provisioning a merchant account. You'll also be taking the ID for the
`User` that you created in the previous step and passing it in the `user` field.



<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can create a new Application.
</aside>

#### HTTP Request

`POST https://api-test.payline.io/applications`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
user | *string*, **required** | User ID for the owner of the `Application`


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
### Step 3: Enable a Processor
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PR3RLiFxfdaueG9ihdvRHk9h",
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "default_merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "created_at" : "2016-10-04T18:25:18.73Z",
  "updated_at" : "2016-10-04T18:25:18.73Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors/PR3RLiFxfdaueG9ihdvRHk9h"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The Payline Payment Platform is processor agnostic allowing for processing transactions
across multiple processors. Once a processor is enabled, the `Application` can begin
provisioning merchant accounts.

In this example we'll be enabling the DUMMY_V1 processor, which is utilized for
sandbox testing.

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can enable a processor for an Application.
</aside>

<aside class="warning">
The DUMMY_V1 processor should not be provisioned on production level Applications.
</aside>


#### HTTP Request

`POST https://api-test.payline.io/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

### Step 4: Enable Processing Functionality
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-10-04T18:25:16.79Z",
  "updated_at" : "2016-10-04T18:33:30.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

Now that we have a processor associated with an `Application` we'll want to
enable its ability to creaet new `Transfers` and `Authorizations`. This same
method can be used to shut off its ability to process transactions as a form of
risk management.

#### HTTP Request

`PUT https://api-test.payline.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processing_enabled | *boolean*, **required** | True to enable
### Step 4: Enable Settlement Functionality
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-10-04T18:25:16.79Z",
  "updated_at" : "2016-10-04T18:33:30.77Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

As an additional safety measure we have decoupled the processing and settlement
functionalities, so you will also need to enable its ability to settle out funds.

<aside class="notice">
You can enable an Applications settlement and processing capabilities in one API
request.
</aside>


#### HTTP Request

`PUT https://api-test.payline.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | True to enable
## Tokenization.js

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to Payline.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/sab76Lne/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Payline API.
</aside>


### Step 1: Create a form

```html
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
```

Before collecting the sensitive payment information, we will need to construct
an HTML form for users to input their data.

We have provided a simple example to the right for capturing Payment Instrument
data.


### Step 2: Include library

To use tokenization.js you will first need to include the library on the webpage
where you're hosting your form. Please include the script ta as demonstrated
to the right.

<aside class="notice">
Please refrain from hosting the tokenization.js library locally as doing so prevents important updates.
</aside>


```html
<script type="text/javascript" src="https://js.verygoodproxy.com/tokenization.1-latest.js"></script>
```


### Step 3: Configure and initialize

```javascript
var initTokenization = function() {
  Tokenization.init({
    server: "https://api-test.payline.io",
    applicationId: "APgLUKnuNCzL38SGfxgwDqyR",
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
```



Now we need to configure the client so that it `POSTs` to the correct endpoint and
associates the `Payment Instrument` to your application. We'll also use the JQuery
selector method to capture the form data during the initialization.

#### Initialization Fields
Field | Type | Description
----- | ---- | -----------
server | *string*, **required** |  The base url for the Payline API
applicationId | *string*, **required** | The ID for your `Application`
hosted_fields | *object*, **required** | An object containing the `Payment Instrument`information collected from your form

#### hosted_fields object for card
Field | Type | Description
----- | ---- | -----------
number | *string*, **required** | Credit card account number
security_code | *string*, **optional** | The 3-4 digit security code for the card (i.e. CVV code)
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | Expiration year

#### hosted_fields object for bankAccount
Field | Type | Description
----- | ---- | -----------
full_name | *string*, **optional** | Customer's full name on card
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
account_type | *string*, **required** | Either CHECKING or SAVINGS

### Step 4: Submit payload and handle response

```javascript
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
```

> Example Response:

```json
{
  "id" : "TKqh6bJbgoAY7tzW4h5RvfLj",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-04T18:25:57.64Z",
  "updated_at" : "2016-10-04T18:25:57.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-05T18:25:57.64Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Finally we will need to register a click event that fires when our users submit the form and define a callback for handling the tokenization.js response.

### Step 5: Send token to your back-end server for storing

```javascript
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

```
Great now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server, which you'll do by expanding on the callback that you created in the previous step.


### Step 6: Associate to an Identity
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	});
$card = $card->save();

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIqh6bJbgoAY7tzW4h5RvfLj",
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
  "created_at" : "2016-10-04T18:25:58.90Z",
  "updated_at" : "2016-10-04T18:25:58.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/updates"
    }
  }
}
```

Before you can use the newly tokenized card or bank account you will need to
associate it with an `Identity`. To do this you must make an authenticated
`POST` request to the `/payment_instruments` endpoint with the relevant token
and `Identity` information.

<aside class="warning">
Tokens should be associated right away. Tokens not associated within 30 mins
of creation will be invalidated. 
</aside>

#### HTTP Request

`POST https://api-test.payline.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).
## [ADMIN] Create a New Application

## Fetch an Application
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = Application::retrieve('APgLUKnuNCzL38SGfxgwDqyR');

```
```java

```
> Example Response:

```json
{
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-10-04T18:25:16.79Z",
  "updated_at" : "2016-10-04T18:25:22.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`


```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "UShEXo1fxJjJmK1eB3YScLM7", 
	    "entity": {
	        "business_type": "LIMITED_LIABILITY_COMPANY", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 5
	        }, 
	        "settlement_bank_account": "CORPORATE", 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "max_transaction_amount": 12000, 
	        "phone": "1234567890", 
	        "doing_business_as": "Facebook", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Facebook", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "UShEXo1fxJjJmK1eB3YScLM7", 
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
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-04T18:25:16.87Z",
  "updated_at" : "2016-10-04T18:25:16.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can create a new Application.
</aside>

#### HTTP Request

`POST https://api-test.payline.io/applications`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
user | *string*, **required** | User ID for the owner of the `Application`


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
## Disable Processing Functionality
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-10-04T18:25:16.79Z",
  "updated_at" : "2016-10-04T18:33:26.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

Disable an `Applications's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-test.payline.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processing_enabled | *boolean*, **required** | False to disable
## Disable Settlement Functionality
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APgLUKnuNCzL38SGfxgwDqyR",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-04T18:25:16.79Z",
  "updated_at" : "2016-10-04T18:33:27.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
    }
  }
}
```

Disable an `Applications's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-test.payline.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | False to disable
## Create an Application User
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USsKU9b5DcAFHBrwEzUsFtLc",
  "password" : "fd46e236-6bd3-4136-81ca-d7787676abac",
  "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:20.52Z",
  "updated_at" : "2016-10-04T18:25:20.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USsKU9b5DcAFHBrwEzUsFtLc"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

This is the equivalent of provisioning API keys (i.e. credentials) for an `Application`.

<aside class="notice">
Each Application can have multiple Users which allows each merchant to have multiple
API keys that can be independently enabled and disabled. Merchants only have read
access to the API.
</aside>


#### HTTP Request

`POST https://api-test.payline.io/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## [ADMIN] Enable the Dummy Processor (i.e. Sandbox)
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PR3RLiFxfdaueG9ihdvRHk9h",
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "default_merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "created_at" : "2016-10-04T18:25:18.73Z",
  "updated_at" : "2016-10-04T18:25:18.73Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors/PR3RLiFxfdaueG9ihdvRHk9h"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Enables the DUMMY_V1 acquiring processor for an `Application` to provision
 `Merchant` accounts, process `Transfers` and issue `Settlements`.

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can enable a processor for an Application.
</aside>

<aside class="warning">
The DUMMY_V1 processor should not be provisioned on production level Applications.
To enable this processor please use the request body exactly as demonstrated in
the example to the right.
</aside>


#### HTTP Request

`POST https://api-test.payline.io/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## [ADMIN] List all Applications
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APgLUKnuNCzL38SGfxgwDqyR",
      "enabled" : true,
      "tags" : {
        "application_name" : "Facebook"
      },
      "owner" : "IDwwsoqPrya1augHxp1Yrp2N",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-10-04T18:25:16.79Z",
      "updated_at" : "2016-10-04T18:25:22.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "processors" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/processors"
        },
        "users" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users"
        },
        "owner_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/transfers"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/disputes"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/authorizations"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/settlements"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/merchants"
        },
        "identities" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/identities"
        },
        "webhooks" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/webhooks"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/reversals"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/applications/`


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "merchant_identity": "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuMKvG5kAzpCWBHkLL3ugx2", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuMKvG5kAzpCWBHkLL3ugx2", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```java
import io.payline.payments.processing.client.model.Authorization;

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
  "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:53.85Z",
  "updated_at" : "2016-10-04T18:25:53.86Z",
  "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : false,
  "expires_at" : "2016-10-11T18:25:53.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`POST https://api-test.payline.io/authorizations`

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
curl https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUdLMjYQtG2coSk5FjFxFbBX');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUdLMjYQtG2coSk5FjFxFbBX");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRiNk2zSe6RjKpC7DQBdhX7y",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:53.71Z",
  "updated_at" : "2016-10-04T18:25:55.55Z",
  "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : false,
  "expires_at" : "2016-10-11T18:25:53.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`PUT https://api-test.payline.io/authorizations/:AUTHORIZATION_ID`

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

curl https://api-test.payline.io/authorizations/AUvJRYVsMvkxkSueS7ApvMHg \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUvJRYVsMvkxkSueS7ApvMHg",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:26:00.14Z",
  "updated_at" : "2016-10-04T18:26:01.98Z",
  "trace_id" : "b09119c4-92e9-4911-b236-276939e0b08b",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : true,
  "expires_at" : "2016-10-11T18:26:00.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUvJRYVsMvkxkSueS7ApvMHg"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://api-test.payline.io/authorizations/:AUTHORIZATION_ID`

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

curl https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUdLMjYQtG2coSk5FjFxFbBX');

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUdLMjYQtG2coSk5FjFxFbBX");

```
> Example Response:

```json
{
  "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRiNk2zSe6RjKpC7DQBdhX7y",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:53.71Z",
  "updated_at" : "2016-10-04T18:25:55.55Z",
  "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "is_void" : false,
  "expires_at" : "2016-10-11T18:25:53.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://api-test.payline.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


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
      "id" : "AUvJRYVsMvkxkSueS7ApvMHg",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:26:00.14Z",
      "updated_at" : "2016-10-04T18:26:01.98Z",
      "trace_id" : "b09119c4-92e9-4911-b236-276939e0b08b",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "is_void" : true,
      "expires_at" : "2016-10-11T18:26:00.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUvJRYVsMvkxkSueS7ApvMHg"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        }
      }
    }, {
      "id" : "AUdLMjYQtG2coSk5FjFxFbBX",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRiNk2zSe6RjKpC7DQBdhX7y",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:53.71Z",
      "updated_at" : "2016-10-04T18:25:55.55Z",
      "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "is_void" : false,
      "expires_at" : "2016-10-11T18:25:53.71Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUdLMjYQtG2coSk5FjFxFbBX"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/authorizations/`

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


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Michae", 
	        "last_name": "Lopez", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Michae", 
	        "last_name"=> "Lopez", 
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

import io.payline.payments.processing.client.model.Identity;

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
  "id" : "IDjbaEZJwYceHqTFXLHfjq5H",
  "entity" : {
    "title" : null,
    "first_name" : "Michae",
    "last_name" : "Lopez",
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
  "created_at" : "2016-10-04T18:25:41.41Z",
  "updated_at" : "2016-10-04T18:25:41.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://api-test.payline.io/identities`

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


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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

import io.payline.payments.processing.client.model.Identity;

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
  "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
  "created_at" : "2016-10-04T18:25:24.17Z",
  "updated_at" : "2016-10-04T18:25:24.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/identities`

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

curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfVdfQ6jCMWctb33WQdCGjV');
```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDfVdfQ6jCMWctb33WQdCGjV");

```
> Example Response:

```json
{
  "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
  "created_at" : "2016-10-04T18:25:24.12Z",
  "updated_at" : "2016-10-04T18:25:24.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Update an Identity
```shell
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Laura", 
	        "last_name": "Serna", 
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
	        "doing_business_as": "Dunder Mifflin", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Dunder Mifflin", 
	        "url": "www.DunderMifflin.com", 
	        "business_name": "Dunder Mifflin", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Laura",
    "last_name" : "Serna",
    "email" : "user@example.org",
    "business_name" : "Dunder Mifflin",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Dunder Mifflin",
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
    "key" : "value_2"
  },
  "created_at" : "2016-10-04T18:25:24.12Z",
  "updated_at" : "2016-10-04T18:26:24.07Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/identities`

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
## List all Identities
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Identity;

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
      "id" : "IDjbaEZJwYceHqTFXLHfjq5H",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Lopez",
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
      "created_at" : "2016-10-04T18:25:41.36Z",
      "updated_at" : "2016-10-04T18:25:41.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoy3C3hespDcCLfLNNX8Nzp",
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
      "created_at" : "2016-10-04T18:25:34.32Z",
      "updated_at" : "2016-10-04T18:25:34.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID3v9KVKrMy9JsQJ5B1fftfU",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-04T18:25:33.33Z",
      "updated_at" : "2016-10-04T18:25:33.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoWj9HK2LWwXrY7HhwZGAuU",
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
      "created_at" : "2016-10-04T18:25:32.33Z",
      "updated_at" : "2016-10-04T18:25:32.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfb83T1g4JsggCjpMJC84RE",
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
      "created_at" : "2016-10-04T18:25:31.34Z",
      "updated_at" : "2016-10-04T18:25:31.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID2LY7AKMVqsxgeYdhfV4miR",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:29.16Z",
      "updated_at" : "2016-10-04T18:25:29.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDqNsBbeoQiAwmco5HSbYBiC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:28.18Z",
      "updated_at" : "2016-10-04T18:25:28.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwTcMhB94uAcn9rY5VGwxan",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:27.28Z",
      "updated_at" : "2016-10-04T18:25:27.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDaR3921SniyJks4qhxZNDye",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-10-04T18:25:26.38Z",
      "updated_at" : "2016-10-04T18:25:26.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDo1Pr2mJgrtJqpNFmYuPRj9",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-10-04T18:25:25.24Z",
      "updated_at" : "2016-10-04T18:25:25.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
      "created_at" : "2016-10-04T18:25:24.12Z",
      "updated_at" : "2016-10-04T18:25:24.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwwsoqPrya1augHxp1Yrp2N",
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
      "created_at" : "2016-10-04T18:25:16.79Z",
      "updated_at" : "2016-10-04T18:25:16.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/identities/`


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfVdfQ6jCMWctb33WQdCGjV');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "verification" : "VIbN4bZc1k32UmEw2J6yqgS8",
  "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T18:25:38.88Z",
  "updated_at" : "2016-10-04T18:25:38.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIbN4bZc1k32UmEw2J6yqgS8"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Retrieve a Merchant
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MU5WB4TCKpVnNvJLvTNN3Rd6');

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU5WB4TCKpVnNvJLvTNN3Rd6");

```
> Example Response:

```json
{
  "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "verification" : null,
  "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-04T18:25:38.77Z",
  "updated_at" : "2016-10-04T18:25:39.01Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIiw3vZZDrdGLwdDoL7hFDcS",
  "external_trace_id" : "b6d79bb8-1b79-4432-a916-af9c1e9aca8a",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-04T18:26:25.30Z",
  "updated_at" : "2016-10-04T18:26:25.33Z",
  "payment_instrument" : null,
  "merchant" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIiw3vZZDrdGLwdDoL7hFDcS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    }
  }
}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST https://api-test.payline.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Reattempt Merchant Provisioning
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIiw3vZZDrdGLwdDoL7hFDcS",
  "external_trace_id" : "b6d79bb8-1b79-4432-a916-af9c1e9aca8a",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-04T18:26:25.30Z",
  "updated_at" : "2016-10-04T18:26:25.33Z",
  "payment_instrument" : null,
  "merchant" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIiw3vZZDrdGLwdDoL7hFDcS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    }
  }
}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST https://api-test.payline.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Disable Processing Functionality
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "verification" : null,
  "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-04T18:25:38.77Z",
  "updated_at" : "2016-10-04T18:33:25.15Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Disable a `Merchant's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-test.payline.io/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processing_enabled | *boolean*, **required** | False to disable
## Disable Settlement Functionality
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "verification" : null,
  "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-04T18:25:38.77Z",
  "updated_at" : "2016-10-04T18:33:25.84Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```
Disable a `Merchant's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-test.payline.io/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | False to disable
## List all Merchants
```shell
curl https://api-test.payline.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU5WB4TCKpVnNvJLvTNN3Rd6",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "verification" : null,
      "merchant_profile" : "MPsb6P51nzybqVqGzzLBzhJK",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-10-04T18:25:38.77Z",
      "updated_at" : "2016-10-04T18:25:39.01Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPsb6P51nzybqVqGzzLBzhJK"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/merchants/`

## List Merchant Verifications
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDjbaEZJwYceHqTFXLHfjq5H",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Lopez",
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
      "created_at" : "2016-10-04T18:25:41.36Z",
      "updated_at" : "2016-10-04T18:25:41.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoy3C3hespDcCLfLNNX8Nzp",
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
      "created_at" : "2016-10-04T18:25:34.32Z",
      "updated_at" : "2016-10-04T18:25:34.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID3v9KVKrMy9JsQJ5B1fftfU",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-04T18:25:33.33Z",
      "updated_at" : "2016-10-04T18:25:33.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoWj9HK2LWwXrY7HhwZGAuU",
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
      "created_at" : "2016-10-04T18:25:32.33Z",
      "updated_at" : "2016-10-04T18:25:32.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfb83T1g4JsggCjpMJC84RE",
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
      "created_at" : "2016-10-04T18:25:31.34Z",
      "updated_at" : "2016-10-04T18:25:31.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID2LY7AKMVqsxgeYdhfV4miR",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:29.16Z",
      "updated_at" : "2016-10-04T18:25:29.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDqNsBbeoQiAwmco5HSbYBiC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:28.18Z",
      "updated_at" : "2016-10-04T18:25:28.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwTcMhB94uAcn9rY5VGwxan",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:27.28Z",
      "updated_at" : "2016-10-04T18:25:27.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDaR3921SniyJks4qhxZNDye",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-10-04T18:25:26.38Z",
      "updated_at" : "2016-10-04T18:25:26.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDo1Pr2mJgrtJqpNFmYuPRj9",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-10-04T18:25:25.24Z",
      "updated_at" : "2016-10-04T18:25:25.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
      "created_at" : "2016-10-04T18:25:24.12Z",
      "updated_at" : "2016-10-04T18:25:24.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwwsoqPrya1augHxp1Yrp2N",
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
      "created_at" : "2016-10-04T18:25:16.79Z",
      "updated_at" : "2016-10-04T18:25:16.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`




## [ADMIN] List Merchant Verifications
```shell
curl https://api-test.payline.io/merchants/MU5WB4TCKpVnNvJLvTNN3Rd6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDjbaEZJwYceHqTFXLHfjq5H",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Lopez",
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
      "created_at" : "2016-10-04T18:25:41.36Z",
      "updated_at" : "2016-10-04T18:25:41.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoy3C3hespDcCLfLNNX8Nzp",
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
      "created_at" : "2016-10-04T18:25:34.32Z",
      "updated_at" : "2016-10-04T18:25:34.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoy3C3hespDcCLfLNNX8Nzp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID3v9KVKrMy9JsQJ5B1fftfU",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-04T18:25:33.33Z",
      "updated_at" : "2016-10-04T18:25:33.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID3v9KVKrMy9JsQJ5B1fftfU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDoWj9HK2LWwXrY7HhwZGAuU",
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
      "created_at" : "2016-10-04T18:25:32.33Z",
      "updated_at" : "2016-10-04T18:25:32.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoWj9HK2LWwXrY7HhwZGAuU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfb83T1g4JsggCjpMJC84RE",
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
      "created_at" : "2016-10-04T18:25:31.34Z",
      "updated_at" : "2016-10-04T18:25:31.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfb83T1g4JsggCjpMJC84RE/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "ID2LY7AKMVqsxgeYdhfV4miR",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:29.16Z",
      "updated_at" : "2016-10-04T18:25:29.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2LY7AKMVqsxgeYdhfV4miR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDqNsBbeoQiAwmco5HSbYBiC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:28.18Z",
      "updated_at" : "2016-10-04T18:25:28.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqNsBbeoQiAwmco5HSbYBiC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwTcMhB94uAcn9rY5VGwxan",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-10-04T18:25:27.28Z",
      "updated_at" : "2016-10-04T18:25:27.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwTcMhB94uAcn9rY5VGwxan/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDaR3921SniyJks4qhxZNDye",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-10-04T18:25:26.38Z",
      "updated_at" : "2016-10-04T18:25:26.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaR3921SniyJks4qhxZNDye/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDo1Pr2mJgrtJqpNFmYuPRj9",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-10-04T18:25:25.24Z",
      "updated_at" : "2016-10-04T18:25:25.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDo1Pr2mJgrtJqpNFmYuPRj9/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDfVdfQ6jCMWctb33WQdCGjV",
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
      "created_at" : "2016-10-04T18:25:24.12Z",
      "updated_at" : "2016-10-04T18:25:24.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "IDwwsoqPrya1augHxp1Yrp2N",
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
      "created_at" : "2016-10-04T18:25:16.79Z",
      "updated_at" : "2016-10-04T18:25:16.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities?offset=0&limit=20&sort=created_at,desc"
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
Only `Users` with ROLE_PLATFORM permissions can view the `message` and `raw`
 fields.



#### HTTP Request

`GET https://api-test.payline.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


## Create a Merchant User
```shell
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USqMctyDaWhxww8KV4oK1gnr",
  "password" : "87fedccc-2a76-4b36-b3d2-44ccebc88412",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:48.46Z",
  "updated_at" : "2016-10-04T18:25:48.46Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USqMctyDaWhxww8KV4oK1gnr"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`


# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Tokenize Card with Embedded Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to Payline. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/rserna2010/47kgeao9/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the Payline API.
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
          applicationId: 'APgLUKnuNCzL38SGfxgwDqyR',
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
  "id" : "TKqh6bJbgoAY7tzW4h5RvfLj",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-04T18:25:57.64Z",
  "updated_at" : "2016-10-04T18:25:57.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-05T18:25:57.64Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	});
$card = $card->save();

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIqh6bJbgoAY7tzW4h5RvfLj",
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
  "created_at" : "2016-10-04T18:25:58.90Z",
  "updated_at" : "2016-10-04T18:25:58.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/updates"
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

`POST https://api-test.payline.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqh6bJbgoAY7tzW4h5RvfLj", 
	    "type": "TOKEN", 
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	});
$card = $card->save();

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIqh6bJbgoAY7tzW4h5RvfLj",
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
  "created_at" : "2016-10-04T18:25:58.90Z",
  "updated_at" : "2016-10-04T18:25:58.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/updates"
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

`POST https://api-test.payline.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Create a Card
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "name": "Daphne Sterling", 
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
	    "identity": "IDjbaEZJwYceHqTFXLHfjq5H"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Daphne Sterling", 
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
	    "identity"=> "IDjbaEZJwYceHqTFXLHfjq5H"
	));
$card = $card->save();


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

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
  "id" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "fingerprint" : "FPR2061140472",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Daphne Sterling",
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
  "created_at" : "2016-10-04T18:25:42.25Z",
  "updated_at" : "2016-10-04T18:25:42.25Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDjbaEZJwYceHqTFXLHfjq5H",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/updates"
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

`POST https://api-test.payline.io/payment_instruments`

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

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
	    "identity": "IDfVdfQ6jCMWctb33WQdCGjV"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "IDfVdfQ6jCMWctb33WQdCGjV"
	));
$bank_account = $bank_account->save();


```
```java

import io.payline.payments.processing.client.model.BankAccount;

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
  "id" : "PI5C4UNzdxx78okAGBCwwSMM",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T18:25:35.29Z",
  "updated_at" : "2016-10-04T18:25:35.29Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **optional** | Account owner's full name
## Fetch a Payment Instrument

```shell


curl https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI5C4UNzdxx78okAGBCwwSMM');

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI5C4UNzdxx78okAGBCwwSMM")

```
> Example Response:

```json
{
  "id" : "PI5C4UNzdxx78okAGBCwwSMM",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T18:25:35.19Z",
  "updated_at" : "2016-10-04T18:25:37.54Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PI5C4UNzdxx78okAGBCwwSMM",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-04T18:25:35.19Z",
  "updated_at" : "2016-10-04T18:25:37.54Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`PUT https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


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
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.BankAccount;

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
      "id" : "PIqh6bJbgoAY7tzW4h5RvfLj",
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
      "created_at" : "2016-10-04T18:25:58.77Z",
      "updated_at" : "2016-10-04T18:25:58.77Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqh6bJbgoAY7tzW4h5RvfLj/updates"
        }
      }
    }, {
      "id" : "PIs4KGEzuxCp5HehFRuPHnq7",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-04T18:25:43.25Z",
      "updated_at" : "2016-10-04T18:25:43.25Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDjbaEZJwYceHqTFXLHfjq5H",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "fingerprint" : "FPR2061140472",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Daphne Sterling",
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
      "created_at" : "2016-10-04T18:25:42.17Z",
      "updated_at" : "2016-10-04T18:25:53.86Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDjbaEZJwYceHqTFXLHfjq5H",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjbaEZJwYceHqTFXLHfjq5H"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2/updates"
        }
      }
    }, {
      "id" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:38.77Z",
      "updated_at" : "2016-10-04T18:25:38.77Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PI2fcapRXPPr9RNCtHLVD8qB",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:38.77Z",
      "updated_at" : "2016-10-04T18:25:38.77Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2fcapRXPPr9RNCtHLVD8qB"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2fcapRXPPr9RNCtHLVD8qB/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2fcapRXPPr9RNCtHLVD8qB/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2fcapRXPPr9RNCtHLVD8qB/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PIhQuKDWiswg49vQ72ci4U9Q",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:38.77Z",
      "updated_at" : "2016-10-04T18:25:38.77Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhQuKDWiswg49vQ72ci4U9Q"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhQuKDWiswg49vQ72ci4U9Q/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhQuKDWiswg49vQ72ci4U9Q/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhQuKDWiswg49vQ72ci4U9Q/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PI5C4UNzdxx78okAGBCwwSMM",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-04T18:25:35.19Z",
      "updated_at" : "2016-10-04T18:25:37.54Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PI5T7fLvf7q4wCkFSszfkV33",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:18.64Z",
      "updated_at" : "2016-10-04T18:25:18.64Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5T7fLvf7q4wCkFSszfkV33"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5T7fLvf7q4wCkFSszfkV33/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5T7fLvf7q4wCkFSszfkV33/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5T7fLvf7q4wCkFSszfkV33/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PIai3TNG3cdEyRUG8JfQk99J",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:18.64Z",
      "updated_at" : "2016-10-04T18:25:18.64Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIai3TNG3cdEyRUG8JfQk99J"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIai3TNG3cdEyRUG8JfQk99J/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIai3TNG3cdEyRUG8JfQk99J/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIai3TNG3cdEyRUG8JfQk99J/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PIhnZBUb9EXgR23127v3iqDY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:18.64Z",
      "updated_at" : "2016-10-04T18:25:18.64Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhnZBUb9EXgR23127v3iqDY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhnZBUb9EXgR23127v3iqDY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhnZBUb9EXgR23127v3iqDY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIhnZBUb9EXgR23127v3iqDY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "PIdnAboMSmJf7kRzTbCueuYm",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-04T18:25:18.64Z",
      "updated_at" : "2016-10-04T18:25:18.64Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIdnAboMSmJf7kRzTbCueuYm"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIdnAboMSmJf7kRzTbCueuYm/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwwsoqPrya1augHxp1Yrp2N"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIdnAboMSmJf7kRzTbCueuYm/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIdnAboMSmJf7kRzTbCueuYm/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/payment_instruments`

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDfVdfQ6jCMWctb33WQdCGjV');
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

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json
{
  "id" : "STdH6Ucpt6D6cpgrK4aMwmbW",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "currency" : "USD",
  "created_at" : "2016-10-04T18:33:07.87Z",
  "updated_at" : "2016-10-04T18:33:07.89Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 210466,
  "total_fee" : 21048,
  "net_amount" : 189418,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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
request to the transfers link (i.e. POST https://api-test.payline.io/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://api-test.payline.io/identities/:IDENTITY_ID/settlements`

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


curl https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STdH6Ucpt6D6cpgrK4aMwmbW');

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STdH6Ucpt6D6cpgrK4aMwmbW");

```
> Example Response:

```json
{
  "id" : "STdH6Ucpt6D6cpgrK4aMwmbW",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "currency" : "USD",
  "created_at" : "2016-10-04T18:33:07.76Z",
  "updated_at" : "2016-10-04T18:33:09.76Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 210466,
  "total_fee" : 21048,
  "net_amount" : 189418,
  "destination" : "PI5C4UNzdxx78okAGBCwwSMM",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://api-test.payline.io/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PI5C4UNzdxx78okAGBCwwSMM"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "STdH6Ucpt6D6cpgrK4aMwmbW",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "currency" : "USD",
  "created_at" : "2016-10-04T18:33:07.76Z",
  "updated_at" : "2016-10-04T18:33:09.76Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 210466,
  "total_fee" : 21048,
  "net_amount" : 189418,
  "destination" : "PI5C4UNzdxx78okAGBCwwSMM",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
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

`POST https://api-test.payline.io/settlements/:SETTLEMENT_ID`

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
curl https://api-test.payline.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


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
      "id" : "STdH6Ucpt6D6cpgrK4aMwmbW",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "currency" : "USD",
      "created_at" : "2016-10-04T18:33:07.76Z",
      "updated_at" : "2016-10-04T18:33:09.76Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 210466,
      "total_fee" : 21048,
      "net_amount" : 189418,
      "destination" : "PI5C4UNzdxx78okAGBCwwSMM",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


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
      "id" : "TRjf5PBCL7YAr8CeDV2Z5W9G",
      "amount" : 89,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "205bb3b9-68dd-438d-9c4f-eef4e0e41089",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "destination" : "PI5C4UNzdxx78okAGBCwwSMM",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:33:09.51Z",
      "updated_at" : "2016-10-04T18:33:09.87Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRjf5PBCL7YAr8CeDV2Z5W9G"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRjf5PBCL7YAr8CeDV2Z5W9G/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRjf5PBCL7YAr8CeDV2Z5W9G/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRjf5PBCL7YAr8CeDV2Z5W9G/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
        }
      }
    }, {
      "id" : "TRa3ciN98q1LqrGqQ9ZamjC2",
      "amount" : 189329,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "fd2814b4-cfa9-4f70-b47d-ea0ab18352d5",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "destination" : "PI5C4UNzdxx78okAGBCwwSMM",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:33:09.51Z",
      "updated_at" : "2016-10-04T18:33:09.99Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRa3ciN98q1LqrGqQ9ZamjC2"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRa3ciN98q1LqrGqQ9ZamjC2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRa3ciN98q1LqrGqQ9ZamjC2/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRa3ciN98q1LqrGqQ9ZamjC2/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5C4UNzdxx78okAGBCwwSMM"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRiNk2zSe6RjKpC7DQBdhX7y",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "ready_to_settle_at" : "2016-10-04T18:27:10.92Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:55.27Z",
      "updated_at" : "2016-10-04T18:26:01.64Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        }
      }
    }, {
      "id" : "TRpznGSUWSQZdhHpYsYyNN1u",
      "amount" : 210366,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "734ed8a3-2f10-4f1f-b832-57389472a8b1",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "ready_to_settle_at" : "2016-10-04T18:27:10.76Z",
      "fee" : 21037,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:44.51Z",
      "updated_at" : "2016-10-04T18:26:04.34Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STdH6Ucpt6D6cpgrK4aMwmbW/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/transfers`


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
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	{
	    "fee": 38906, 
	    "source": "PIs4KGEzuxCp5HehFRuPHnq7", 
	    "merchant_identity": "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 389057
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 21037, 
	    "source"=> "PIuMKvG5kAzpCWBHkLL3ugx2", 
	    "merchant_identity"=> "IDfVdfQ6jCMWctb33WQdCGjV", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 210366
	));
$debit = $debit->save();
```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```


> Example Response:

```json
{
  "id" : "TRoq8Khbbpkkg9RVXSYaAAgg",
  "amount" : 389057,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "06569f20-7d84-4f04-b7dd-4b166d6b9397",
  "currency" : "USD",
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "source" : "PIs4KGEzuxCp5HehFRuPHnq7",
  "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
  "ready_to_settle_at" : null,
  "fee" : 38906,
  "statement_descriptor" : "PLD*DUNDER MIFFLIN",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:46.99Z",
  "updated_at" : "2016-10-04T18:25:47.11Z",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/reversals"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
    }
  }
}
```

A `Transfer` representing a customer payment where funds are obtained from a
bank account (i.e. ACH Debit, eCheck). These specific `Transfers` are
distinguished by their type which return DEBIT.

#### HTTP Request

`POST https://api-test.payline.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRpznGSUWSQZdhHpYsYyNN1u');



```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRpznGSUWSQZdhHpYsYyNN1u");

```
> Example Response:

```json
{
  "id" : "TRpznGSUWSQZdhHpYsYyNN1u",
  "amount" : 210366,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "734ed8a3-2f10-4f1f-b832-57389472a8b1",
  "currency" : "USD",
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
  "ready_to_settle_at" : null,
  "fee" : 21037,
  "statement_descriptor" : "PLD*DUNDER MIFFLIN",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:44.51Z",
  "updated_at" : "2016-10-04T18:26:04.34Z",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/reversals"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRpznGSUWSQZdhHpYsYyNN1u');
$refund = $debit->reverse(50);
```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TR6Nq5KbysrXuQMbghzBs911",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "cc5a6097-cec2-45a9-a49a-41e9c4625ec3",
  "currency" : "USD",
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "source" : "PIfR1UTZsVnaa4kFKjHz7xep",
  "destination" : "PIuMKvG5kAzpCWBHkLL3ugx2",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "PLD*DUNDER MIFFLIN",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-04T18:25:52.17Z",
  "updated_at" : "2016-10-04T18:25:52.29Z",
  "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR6Nq5KbysrXuQMbghzBs911"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR6Nq5KbysrXuQMbghzBs911/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://api-test.payline.io/transfers/:TRANSFER_ID/reversals`

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
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Transfer;

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
      "id" : "TRiNk2zSe6RjKpC7DQBdhX7y",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6a81470e-d7bf-40f3-8771-65a89598cfcd",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:55.27Z",
      "updated_at" : "2016-10-04T18:26:01.64Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRiNk2zSe6RjKpC7DQBdhX7y/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        }
      }
    }, {
      "id" : "TR6Nq5KbysrXuQMbghzBs911",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "cc5a6097-cec2-45a9-a49a-41e9c4625ec3",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "destination" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:52.01Z",
      "updated_at" : "2016-10-04T18:26:03.62Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR6Nq5KbysrXuQMbghzBs911"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR6Nq5KbysrXuQMbghzBs911/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        }
      }
    }, {
      "id" : "TRoq8Khbbpkkg9RVXSYaAAgg",
      "amount" : 389057,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "06569f20-7d84-4f04-b7dd-4b166d6b9397",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIs4KGEzuxCp5HehFRuPHnq7",
      "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "ready_to_settle_at" : null,
      "fee" : 38906,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:46.84Z",
      "updated_at" : "2016-10-04T18:26:03.98Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRoq8Khbbpkkg9RVXSYaAAgg/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIs4KGEzuxCp5HehFRuPHnq7"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        }
      }
    }, {
      "id" : "TRpznGSUWSQZdhHpYsYyNN1u",
      "amount" : 210366,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "734ed8a3-2f10-4f1f-b832-57389472a8b1",
      "currency" : "USD",
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "source" : "PIuMKvG5kAzpCWBHkLL3ugx2",
      "destination" : "PIfR1UTZsVnaa4kFKjHz7xep",
      "ready_to_settle_at" : null,
      "fee" : 21037,
      "statement_descriptor" : "PLD*DUNDER MIFFLIN",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-04T18:25:44.51Z",
      "updated_at" : "2016-10-04T18:26:04.34Z",
      "merchant_identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRpznGSUWSQZdhHpYsYyNN1u/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuMKvG5kAzpCWBHkLL3ugx2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfR1UTZsVnaa4kFKjHz7xep"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/transfers`
# Users (API Keys)

A `User` resource represents a pair of API keys which are used to perform
authenticated requests against the Payline API. When making authenticated
requests via [http basic access authentication](https://en.wikipedia.org/wiki/HTTPS)
the `id` of a `User` resource maps to the username, while the `password`
corresponds to the password (i.e. secret).


<aside class="notice">
The password field for a User resource is only returned during the initial
creation. Following GET requests for the resource return the field as null for
security purposes.
</aside>


Users have 3 potential roles which provide different levels of access to the API:


1. **ROLE_PLATFORM:** Access to all Application and Merchant data

2. **ROLE_PARTNER:** Access to one Application's data and that Application's Merchant
data (i.e. Merchant's created under this Application)

3. **ROLE_MERCHANT:** Access to one Merchant data
## Create an Application User
```shell
curl https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USsKU9b5DcAFHBrwEzUsFtLc",
  "password" : "fd46e236-6bd3-4136-81ca-d7787676abac",
  "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:20.52Z",
  "updated_at" : "2016-10-04T18:25:20.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USsKU9b5DcAFHBrwEzUsFtLc"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

This is the equivalent of provisioning API keys (i.e. credentials) for an `Application`.

<aside class="notice">
Each Application can have multiple Users which allows each merchant to have multiple
API keys that can be independently enabled and disabled. Merchants only have read
access to the API.
</aside>


#### HTTP Request

`POST https://api-test.payline.io/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## Create a Merchant User

```shell
curl https://api-test.payline.io/identities/IDfVdfQ6jCMWctb33WQdCGjV/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USqMctyDaWhxww8KV4oK1gnr",
  "password" : "87fedccc-2a76-4b36-b3d2-44ccebc88412",
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:48.46Z",
  "updated_at" : "2016-10-04T18:25:48.46Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USqMctyDaWhxww8KV4oK1gnr"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`



## Retrieve a User
```shell
curl https://api-test.payline.io/users/TRpznGSUWSQZdhHpYsYyNN1u \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UShEXo1fxJjJmK1eB3YScLM7",
  "password" : null,
  "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:15.36Z",
  "updated_at" : "2016-10-04T18:25:16.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UShEXo1fxJjJmK1eB3YScLM7"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User`

## Disable a User
```shell
curl https://api-test.payline.io/users/USqMctyDaWhxww8KV4oK1gnr \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USqMctyDaWhxww8KV4oK1gnr",
  "password" : null,
  "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-04T18:25:48.36Z",
  "updated_at" : "2016-10-04T18:25:49.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USqMctyDaWhxww8KV4oK1gnr"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

Disable API keys (i.e. credentials) for a previously created `User`

<aside class="notice">
Only Users with ROLE_PLATFORM can disable another user.
</aside>


#### HTTP Request


`PUT https://api-test.payline.io/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User` you would like to disable

## List all Users
```shell
curl https://api-test.payline.io/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USqMctyDaWhxww8KV4oK1gnr",
      "password" : null,
      "identity" : "IDfVdfQ6jCMWctb33WQdCGjV",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-10-04T18:25:48.36Z",
      "updated_at" : "2016-10-04T18:25:51.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USqMctyDaWhxww8KV4oK1gnr"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "USsKU9b5DcAFHBrwEzUsFtLc",
      "password" : null,
      "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-10-04T18:25:20.43Z",
      "updated_at" : "2016-10-04T18:25:20.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USsKU9b5DcAFHBrwEzUsFtLc"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    }, {
      "id" : "UShEXo1fxJjJmK1eB3YScLM7",
      "password" : null,
      "identity" : "IDwwsoqPrya1augHxp1Yrp2N",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-10-04T18:25:15.36Z",
      "updated_at" : "2016-10-04T18:25:16.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/UShEXo1fxJjJmK1eB3YScLM7"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 3
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/users`

# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the Payline API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://api-test.payline.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHmY8wJSKc3QU4uoeKSfvhV7",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "created_at" : "2016-10-04T18:25:23.09Z",
  "updated_at" : "2016-10-04T18:25:23.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHmY8wJSKc3QU4uoeKSfvhV7"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`POST https://api-test.payline.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

## Retrieve a Webhook

```shell



curl https://api-test.payline.io/webhooks/WHmY8wJSKc3QU4uoeKSfvhV7 \
    -H "Content-Type: application/vnd.json+api" \
    -u UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHmY8wJSKc3QU4uoeKSfvhV7');



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHmY8wJSKc3QU4uoeKSfvhV7");

```
> Example Response:

```json
{
  "id" : "WHmY8wJSKc3QU4uoeKSfvhV7",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgLUKnuNCzL38SGfxgwDqyR",
  "created_at" : "2016-10-04T18:25:23.09Z",
  "updated_at" : "2016-10-04T18:25:23.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHmY8wJSKc3QU4uoeKSfvhV7"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://api-test.payline.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEXo1fxJjJmK1eB3YScLM7:c148bc82-13b6-40e4-a495-9fe8fd29feae

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Webhook;

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
      "id" : "WHmY8wJSKc3QU4uoeKSfvhV7",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APgLUKnuNCzL38SGfxgwDqyR",
      "created_at" : "2016-10-04T18:25:23.09Z",
      "updated_at" : "2016-10-04T18:25:23.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHmY8wJSKc3QU4uoeKSfvhV7"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APgLUKnuNCzL38SGfxgwDqyR"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/webhooks`
    

## Sample Payloads


```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UShEXo1fxJjJmK1eB3YScLM7', 'c148bc82-13b6-40e4-a495-9fe8fd29feae');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

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
