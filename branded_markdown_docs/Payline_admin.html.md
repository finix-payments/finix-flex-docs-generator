---
title: Payline API Reference

language_tabs:
- python: Python
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

4. [Push-to-Card Private [BETA]](#push-to-card-private-beta): This guide walks 
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```python


from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("USetR78WdNpBy7TG3R5pkf22", "e80c0f67-7d70-4190-a3a8-82194c072e4b"))

```
```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```java

```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USetR78WdNpBy7TG3R5pkf22`

- Password: `e80c0f67-7d70-4190-a3a8-82194c072e4b`

- Application ID: `APcRz1ht766SckkM2PWh7AGT`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "default_statement_descriptor"=> "Lees Sandwiches", 
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
	        "doing_business_as"=> "Lees Sandwiches", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Lees Sandwiches", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.LeesSandwiches.com", 
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
  "id" : "ID83THqukvoRDbEe696oGSvC",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-09T22:33:04.24Z",
  "updated_at" : "2016-11-09T22:33:04.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import BankAccount

bank_account = BankAccount(**
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}).save()

```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	    "identity"=> "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PI5JXborVmN6x5HBPJr7KWyk",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-09T22:33:10.80Z",
  "updated_at" : "2016-11-09T22:33:10.80Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID83THqukvoRDbEe696oGSvC');

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
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : "VIbrfe2M9Rkx1d6rQRCSyUwV",
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.31Z",
  "updated_at" : "2016-11-09T22:33:12.31Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIbrfe2M9Rkx1d6rQRCSyUwV"
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
	}).save()

```
```shell

curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "first_name"=> "Collen", 
	        "last_name"=> "Sterling", 
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
  "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
    "last_name" : "Sterling",
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
  "created_at" : "2016-11-09T22:33:13.52Z",
  "updated_at" : "2016-11-09T22:33:13.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "name": "Step Curry", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4957030420210454", 
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
	    "identity": "IDw4wTFFG5FU4Rg1nuzKCnCq"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Step Curry", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
	    "number"=> "4957030420210454", 
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
	    "identity"=> "IDw4wTFFG5FU4Rg1nuzKCnCq"
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
  "id" : "PIqDevPePVdTiRwodJKf87dE",
  "fingerprint" : "FPR1778398984",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Curry",
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
  "created_at" : "2016-11-09T22:33:14.20Z",
  "updated_at" : "2016-11-09T22:33:14.20Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/updates"
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
```python


from payline.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID83THqukvoRDbEe696oGSvC", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIqDevPePVdTiRwodJKf87dE", 
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
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.99Z",
  "updated_at" : "2016-11-09T22:33:20.01Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUhH5z1FYhZbppnpiEQ9WKuz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUhH5z1FYhZbppnpiEQ9WKuz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUhH5z1FYhZbppnpiEQ9WKuz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRSbdGwMA7TNWRGRkz3iSoG",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.85Z",
  "updated_at" : "2016-11-09T22:33:20.93Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** https://api-test.payline.io

- **Production API:** https://api.payline.io

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
          applicationId: 'APcRz1ht766SckkM2PWh7AGT',
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
  "id" : "TKu2zxtZ8nyjF99HZRAkA2Vb",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-09T22:33:22.43Z",
  "updated_at" : "2016-11-09T22:33:22.43Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-10T22:33:22.43Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    }
  }
}
```

### Step 4: Associate the Token
```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PIu2zxtZ8nyjF99HZRAkA2Vb",
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
  "created_at" : "2016-11-09T22:33:22.99Z",
  "updated_at" : "2016-11-09T22:33:22.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/updates"
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


## Getting Started
### Step 1: Create an Identity for a Merchant

```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "default_statement_descriptor"=> "Lees Sandwiches", 
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
	        "doing_business_as"=> "Lees Sandwiches", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Lees Sandwiches", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.LeesSandwiches.com", 
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
  "id" : "ID83THqukvoRDbEe696oGSvC",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-09T22:33:04.24Z",
  "updated_at" : "2016-11-09T22:33:04.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import BankAccount

bank_account = BankAccount(**
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}).save()

```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	    "identity"=> "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PI5JXborVmN6x5HBPJr7KWyk",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-09T22:33:10.80Z",
  "updated_at" : "2016-11-09T22:33:10.80Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID83THqukvoRDbEe696oGSvC');

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
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : "VIbrfe2M9Rkx1d6rQRCSyUwV",
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.31Z",
  "updated_at" : "2016-11-09T22:33:12.31Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIbrfe2M9Rkx1d6rQRCSyUwV"
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
	}).save()

```
```shell

curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "first_name"=> "Collen", 
	        "last_name"=> "Sterling", 
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
  "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
    "last_name" : "Sterling",
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
  "created_at" : "2016-11-09T22:33:13.52Z",
  "updated_at" : "2016-11-09T22:33:13.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "name": "Step Curry", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4957030420210454", 
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
	    "identity": "IDw4wTFFG5FU4Rg1nuzKCnCq"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Step Curry", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
	    "number"=> "4957030420210454", 
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
	    "identity"=> "IDw4wTFFG5FU4Rg1nuzKCnCq"
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
  "id" : "PIqDevPePVdTiRwodJKf87dE",
  "fingerprint" : "FPR1778398984",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Curry",
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
  "created_at" : "2016-11-09T22:33:14.20Z",
  "updated_at" : "2016-11-09T22:33:14.20Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/updates"
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
```python


from payline.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID83THqukvoRDbEe696oGSvC", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIqDevPePVdTiRwodJKf87dE", 
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
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.99Z",
  "updated_at" : "2016-11-09T22:33:20.01Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUhH5z1FYhZbppnpiEQ9WKuz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUhH5z1FYhZbppnpiEQ9WKuz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUhH5z1FYhZbppnpiEQ9WKuz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRSbdGwMA7TNWRGRkz3iSoG",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.85Z",
  "updated_at" : "2016-11-09T22:33:20.93Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python



```
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USetR78WdNpBy7TG3R5pkf22",
  "password" : "e80c0f67-7d70-4190-a3a8-82194c072e4b",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:00.32Z",
  "updated_at" : "2016-11-09T22:33:00.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USetR78WdNpBy7TG3R5pkf22"
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
```python



```
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "tags": {
	        "application_name": "BrainTree"
	    }, 
	    "user": "USetR78WdNpBy7TG3R5pkf22", 
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
	        "doing_business_as": "BrainTree", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "BrainTree", 
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "BrainTree"
	    ), 
	    "user"=> "USetR78WdNpBy7TG3R5pkf22", 
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
	        "doing_business_as"=> "BrainTree", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "BrainTree", 
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
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-09T22:33:00.81Z",
  "updated_at" : "2016-11-09T22:33:00.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PR6MutXcZE9sHCBBErEuW1Af",
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "default_merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "created_at" : "2016-11-09T22:33:01.42Z",
  "updated_at" : "2016-11-09T22:33:01.42Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors/PR6MutXcZE9sHCBBErEuW1Af"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-11-09T22:33:00.76Z",
  "updated_at" : "2016-11-09T22:33:41.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-09T22:33:00.76Z",
  "updated_at" : "2016-11-09T22:33:41.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
    applicationId: "APcRz1ht766SckkM2PWh7AGT",
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
  "id" : "TKu2zxtZ8nyjF99HZRAkA2Vb",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-09T22:33:22.43Z",
  "updated_at" : "2016-11-09T22:33:22.43Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-10T22:33:22.43Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PIu2zxtZ8nyjF99HZRAkA2Vb",
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
  "created_at" : "2016-11-09T22:33:22.99Z",
  "updated_at" : "2016-11-09T22:33:22.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/updates"
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
```python


from payline.resources import Application

application = Application.get(id="APcRz1ht766SckkM2PWh7AGT")
```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = Application::retrieve('APcRz1ht766SckkM2PWh7AGT');

```
```java

```
> Example Response:

```json
{
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-09T22:33:00.76Z",
  "updated_at" : "2016-11-09T22:33:03.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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


```python



```
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -d '
	{
	    "tags": {
	        "application_name": "BrainTree"
	    }, 
	    "user": "USetR78WdNpBy7TG3R5pkf22", 
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
	        "doing_business_as": "BrainTree", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "BrainTree", 
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "BrainTree"
	    ), 
	    "user"=> "USetR78WdNpBy7TG3R5pkf22", 
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
	        "doing_business_as"=> "BrainTree", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "BrainTree", 
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
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-09T22:33:00.81Z",
  "updated_at" : "2016-11-09T22:33:00.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-11-09T22:33:00.76Z",
  "updated_at" : "2016-11-09T22:33:38.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APcRz1ht766SckkM2PWh7AGT",
  "enabled" : true,
  "tags" : {
    "application_name" : "BrainTree"
  },
  "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-09T22:33:00.76Z",
  "updated_at" : "2016-11-09T22:33:38.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USknYzEC7guR3xFosFZxJ7Zf",
  "password" : "e1df9f2a-1a70-465d-877f-c1b29ab9b392",
  "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:02.11Z",
  "updated_at" : "2016-11-09T22:33:02.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USknYzEC7guR3xFosFZxJ7Zf"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PR6MutXcZE9sHCBBErEuW1Af",
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "default_merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "created_at" : "2016-11-09T22:33:01.42Z",
  "updated_at" : "2016-11-09T22:33:01.42Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors/PR6MutXcZE9sHCBBErEuW1Af"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Application

application = Application.get()
```
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "APcRz1ht766SckkM2PWh7AGT",
      "enabled" : true,
      "tags" : {
        "application_name" : "BrainTree"
      },
      "owner" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-11-09T22:33:00.76Z",
      "updated_at" : "2016-11-09T22:33:03.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "processors" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/processors"
        },
        "users" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users"
        },
        "owner_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/transfers"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/disputes"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/authorizations"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/settlements"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/merchants"
        },
        "identities" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/identities"
        },
        "webhooks" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/webhooks"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/reversals"
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


```python


from payline.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "merchant_identity": "ID83THqukvoRDbEe696oGSvC", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIqDevPePVdTiRwodJKf87dE", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID83THqukvoRDbEe696oGSvC", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIqDevPePVdTiRwodJKf87dE", 
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
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.99Z",
  "updated_at" : "2016-11-09T22:33:20.01Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python



```
```shell
curl https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUhH5z1FYhZbppnpiEQ9WKuz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUhH5z1FYhZbppnpiEQ9WKuz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRSbdGwMA7TNWRGRkz3iSoG",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.85Z",
  "updated_at" : "2016-11-09T22:33:20.93Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python



```
```shell

curl https://api-test.payline.io/authorizations/AUoEqTaFGVzR5aixyNEZbKGm \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUoEqTaFGVzR5aixyNEZbKGm",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:23.73Z",
  "updated_at" : "2016-11-09T22:33:24.56Z",
  "trace_id" : "47b2be6c-8362-48e0-b32a-433343a17ffc",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : true,
  "expires_at" : "2016-11-16T22:33:23.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUoEqTaFGVzR5aixyNEZbKGm"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUhH5z1FYhZbppnpiEQ9WKuz")
```
```shell

curl https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUhH5z1FYhZbppnpiEQ9WKuz');

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUhH5z1FYhZbppnpiEQ9WKuz");

```
> Example Response:

```json
{
  "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRSbdGwMA7TNWRGRkz3iSoG",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:19.85Z",
  "updated_at" : "2016-11-09T22:33:20.93Z",
  "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "is_void" : false,
  "expires_at" : "2016-11-16T22:33:19.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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
```python


from payline.resources import Authorization

authorization = Authorization.get()
```
```shell
curl https://api-test.payline.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "AUoEqTaFGVzR5aixyNEZbKGm",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-09T22:33:23.73Z",
      "updated_at" : "2016-11-09T22:33:24.56Z",
      "trace_id" : "47b2be6c-8362-48e0-b32a-433343a17ffc",
      "source" : "PIqDevPePVdTiRwodJKf87dE",
      "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
      "is_void" : true,
      "expires_at" : "2016-11-16T22:33:23.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUoEqTaFGVzR5aixyNEZbKGm"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        }
      }
    }, {
      "id" : "AUhH5z1FYhZbppnpiEQ9WKuz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRSbdGwMA7TNWRGRkz3iSoG",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-09T22:33:19.85Z",
      "updated_at" : "2016-11-09T22:33:20.93Z",
      "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
      "source" : "PIqDevPePVdTiRwodJKf87dE",
      "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
      "is_void" : false,
      "expires_at" : "2016-11-16T22:33:19.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUhH5z1FYhZbppnpiEQ9WKuz"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
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


```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
	}).save()
```
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
	        "last_name": "Sterling", 
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "first_name"=> "Collen", 
	        "last_name"=> "Sterling", 
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
  "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
    "last_name" : "Sterling",
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
  "created_at" : "2016-11-09T22:33:13.52Z",
  "updated_at" : "2016-11-09T22:33:13.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	        "default_statement_descriptor"=> "Lees Sandwiches", 
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
	        "doing_business_as"=> "Lees Sandwiches", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Lees Sandwiches", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.LeesSandwiches.com", 
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
  "id" : "ID83THqukvoRDbEe696oGSvC",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-09T22:33:04.24Z",
  "updated_at" : "2016-11-09T22:33:04.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Identity
identity = Identity.get(id="ID83THqukvoRDbEe696oGSvC")

```
```shell

curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID83THqukvoRDbEe696oGSvC');
```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID83THqukvoRDbEe696oGSvC");

```
> Example Response:

```json
{
  "id" : "ID83THqukvoRDbEe696oGSvC",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-09T22:33:04.18Z",
  "updated_at" : "2016-11-09T22:33:04.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Alex", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID83THqukvoRDbEe696oGSvC",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Alex",
    "last_name" : "James",
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
  "created_at" : "2016-11-09T22:33:04.18Z",
  "updated_at" : "2016-11-09T22:33:35.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Identity
identity = Identity.get()

```
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
        "last_name" : "Sterling",
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
      "created_at" : "2016-11-09T22:33:13.46Z",
      "updated_at" : "2016-11-09T22:33:13.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID8b2TLNncPg1B7yrkczNf6U",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-09T22:33:09.94Z",
      "updated_at" : "2016-11-09T22:33:09.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2CJxB2ap4CcH4kKGejFrdU",
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
      "created_at" : "2016-11-09T22:33:09.13Z",
      "updated_at" : "2016-11-09T22:33:09.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaEvkFiAWRaaaBhgg6YQYcL",
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
      "created_at" : "2016-11-09T22:33:08.46Z",
      "updated_at" : "2016-11-09T22:33:08.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDYkSqhtsEHSq9txQACq6oC",
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
      "created_at" : "2016-11-09T22:33:07.81Z",
      "updated_at" : "2016-11-09T22:33:07.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDhGHtVLbdJaB422GtBpfKE8",
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
      "created_at" : "2016-11-09T22:33:07.17Z",
      "updated_at" : "2016-11-09T22:33:07.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDsufA2oEe6U2znsc7Y9xxo2",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-09T22:33:06.63Z",
      "updated_at" : "2016-11-09T22:33:06.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID6hYJ2GB3GSDnyhdemAhPLR",
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
      "created_at" : "2016-11-09T22:33:05.94Z",
      "updated_at" : "2016-11-09T22:33:05.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDwm3kTmPpdn4QrdbvgjF3N",
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
      "created_at" : "2016-11-09T22:33:05.37Z",
      "updated_at" : "2016-11-09T22:33:05.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2aBM8DKRa8nvGa5E2dtXpK",
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
      "created_at" : "2016-11-09T22:33:04.84Z",
      "updated_at" : "2016-11-09T22:33:04.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID83THqukvoRDbEe696oGSvC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-09T22:33:04.18Z",
      "updated_at" : "2016-11-09T22:33:04.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "BrainTree",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "BrainTree",
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
        "application_name" : "BrainTree"
      },
      "created_at" : "2016-11-09T22:33:00.76Z",
      "updated_at" : "2016-11-09T22:33:00.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID83THqukvoRDbEe696oGSvC');

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
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : "VIbrfe2M9Rkx1d6rQRCSyUwV",
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.31Z",
  "updated_at" : "2016-11-09T22:33:12.31Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIbrfe2M9Rkx1d6rQRCSyUwV"
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
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MU5R5N3CTx99dUtTDXmgz2L2")

```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MU5R5N3CTx99dUtTDXmgz2L2');

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU5R5N3CTx99dUtTDXmgz2L2");

```
> Example Response:

```json
{
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : null,
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.21Z",
  "updated_at" : "2016-11-09T22:33:12.41Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIbCr1kaAjCMsyijaQ9JkuFs",
  "external_trace_id" : "dc8fefe3-6ab2-4bec-83e1-3ed5a8573f07",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-09T22:33:36.04Z",
  "updated_at" : "2016-11-09T22:33:36.06Z",
  "payment_instrument" : null,
  "merchant" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIbCr1kaAjCMsyijaQ9JkuFs"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIbCr1kaAjCMsyijaQ9JkuFs",
  "external_trace_id" : "dc8fefe3-6ab2-4bec-83e1-3ed5a8573f07",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-09T22:33:36.04Z",
  "updated_at" : "2016-11-09T22:33:36.06Z",
  "payment_instrument" : null,
  "merchant" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIbCr1kaAjCMsyijaQ9JkuFs"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : null,
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.21Z",
  "updated_at" : "2016-11-09T22:33:36.86Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/ \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "verification" : null,
  "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-09T22:33:12.21Z",
  "updated_at" : "2016-11-09T22:33:37.61Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Merchant
merchant = Merchant.get()

```
```shell
curl https://api-test.payline.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "MU5R5N3CTx99dUtTDXmgz2L2",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "verification" : null,
      "merchant_profile" : "MPoA6q2uCr8ALZcJuNTng96R",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-09T22:33:12.21Z",
      "updated_at" : "2016-11-09T22:33:12.41Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPoA6q2uCr8ALZcJuNTng96R"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
        "last_name" : "Sterling",
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
      "created_at" : "2016-11-09T22:33:13.46Z",
      "updated_at" : "2016-11-09T22:33:13.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID8b2TLNncPg1B7yrkczNf6U",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-09T22:33:09.94Z",
      "updated_at" : "2016-11-09T22:33:09.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2CJxB2ap4CcH4kKGejFrdU",
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
      "created_at" : "2016-11-09T22:33:09.13Z",
      "updated_at" : "2016-11-09T22:33:09.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaEvkFiAWRaaaBhgg6YQYcL",
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
      "created_at" : "2016-11-09T22:33:08.46Z",
      "updated_at" : "2016-11-09T22:33:08.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDYkSqhtsEHSq9txQACq6oC",
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
      "created_at" : "2016-11-09T22:33:07.81Z",
      "updated_at" : "2016-11-09T22:33:07.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDhGHtVLbdJaB422GtBpfKE8",
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
      "created_at" : "2016-11-09T22:33:07.17Z",
      "updated_at" : "2016-11-09T22:33:07.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDsufA2oEe6U2znsc7Y9xxo2",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-09T22:33:06.63Z",
      "updated_at" : "2016-11-09T22:33:06.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID6hYJ2GB3GSDnyhdemAhPLR",
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
      "created_at" : "2016-11-09T22:33:05.94Z",
      "updated_at" : "2016-11-09T22:33:05.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDwm3kTmPpdn4QrdbvgjF3N",
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
      "created_at" : "2016-11-09T22:33:05.37Z",
      "updated_at" : "2016-11-09T22:33:05.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2aBM8DKRa8nvGa5E2dtXpK",
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
      "created_at" : "2016-11-09T22:33:04.84Z",
      "updated_at" : "2016-11-09T22:33:04.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID83THqukvoRDbEe696oGSvC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-09T22:33:04.18Z",
      "updated_at" : "2016-11-09T22:33:04.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "BrainTree",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "BrainTree",
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
        "application_name" : "BrainTree"
      },
      "created_at" : "2016-11-09T22:33:00.76Z",
      "updated_at" : "2016-11-09T22:33:00.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MU5R5N3CTx99dUtTDXmgz2L2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
        "last_name" : "Sterling",
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
      "created_at" : "2016-11-09T22:33:13.46Z",
      "updated_at" : "2016-11-09T22:33:13.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID8b2TLNncPg1B7yrkczNf6U",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-09T22:33:09.94Z",
      "updated_at" : "2016-11-09T22:33:09.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8b2TLNncPg1B7yrkczNf6U/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2CJxB2ap4CcH4kKGejFrdU",
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
      "created_at" : "2016-11-09T22:33:09.13Z",
      "updated_at" : "2016-11-09T22:33:09.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2CJxB2ap4CcH4kKGejFrdU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaEvkFiAWRaaaBhgg6YQYcL",
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
      "created_at" : "2016-11-09T22:33:08.46Z",
      "updated_at" : "2016-11-09T22:33:08.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaEvkFiAWRaaaBhgg6YQYcL/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDYkSqhtsEHSq9txQACq6oC",
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
      "created_at" : "2016-11-09T22:33:07.81Z",
      "updated_at" : "2016-11-09T22:33:07.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDYkSqhtsEHSq9txQACq6oC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDhGHtVLbdJaB422GtBpfKE8",
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
      "created_at" : "2016-11-09T22:33:07.17Z",
      "updated_at" : "2016-11-09T22:33:07.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhGHtVLbdJaB422GtBpfKE8/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDsufA2oEe6U2znsc7Y9xxo2",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-09T22:33:06.63Z",
      "updated_at" : "2016-11-09T22:33:06.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDsufA2oEe6U2znsc7Y9xxo2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID6hYJ2GB3GSDnyhdemAhPLR",
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
      "created_at" : "2016-11-09T22:33:05.94Z",
      "updated_at" : "2016-11-09T22:33:05.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID6hYJ2GB3GSDnyhdemAhPLR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDwm3kTmPpdn4QrdbvgjF3N",
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
      "created_at" : "2016-11-09T22:33:05.37Z",
      "updated_at" : "2016-11-09T22:33:05.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwm3kTmPpdn4QrdbvgjF3N/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID2aBM8DKRa8nvGa5E2dtXpK",
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
      "created_at" : "2016-11-09T22:33:04.84Z",
      "updated_at" : "2016-11-09T22:33:04.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2aBM8DKRa8nvGa5E2dtXpK/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "ID83THqukvoRDbEe696oGSvC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-09T22:33:04.18Z",
      "updated_at" : "2016-11-09T22:33:04.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "BrainTree",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "BrainTree",
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
        "application_name" : "BrainTree"
      },
      "created_at" : "2016-11-09T22:33:00.76Z",
      "updated_at" : "2016-11-09T22:33:00.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UScDQQqXrvFyRHtJ91HvDkLZ",
  "password" : "17aebe76-27e2-44c9-9d04-53c7c6f088e0",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:16.75Z",
  "updated_at" : "2016-11-09T22:33:16.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UScDQQqXrvFyRHtJ91HvDkLZ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
          applicationId: 'APcRz1ht766SckkM2PWh7AGT',
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
  "id" : "TKu2zxtZ8nyjF99HZRAkA2Vb",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-09T22:33:22.43Z",
  "updated_at" : "2016-11-09T22:33:22.43Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-10T22:33:22.43Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    }
  }
}
```

```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PIu2zxtZ8nyjF99HZRAkA2Vb",
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
  "created_at" : "2016-11-09T22:33:22.99Z",
  "updated_at" : "2016-11-09T22:33:22.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/updates"
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
```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKu2zxtZ8nyjF99HZRAkA2Vb", 
	    "type": "TOKEN", 
	    "identity": "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PIu2zxtZ8nyjF99HZRAkA2Vb",
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
  "created_at" : "2016-11-09T22:33:22.99Z",
  "updated_at" : "2016-11-09T22:33:22.99Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/updates"
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
```python



```
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '
	{
	    "name": "Step Curry", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4957030420210454", 
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
	    "identity": "IDw4wTFFG5FU4Rg1nuzKCnCq"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Step Curry", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
	    "number"=> "4957030420210454", 
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
	    "identity"=> "IDw4wTFFG5FU4Rg1nuzKCnCq"
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
  "id" : "PIqDevPePVdTiRwodJKf87dE",
  "fingerprint" : "FPR1778398984",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Curry",
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
  "created_at" : "2016-11-09T22:33:14.20Z",
  "updated_at" : "2016-11-09T22:33:14.20Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/updates"
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
```python


from payline.resources import BankAccount

bank_account = BankAccount(**
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}).save()
```
```shell

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
	    "identity": "ID83THqukvoRDbEe696oGSvC"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
	    "identity"=> "ID83THqukvoRDbEe696oGSvC"
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
  "id" : "PI5JXborVmN6x5HBPJr7KWyk",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-09T22:33:10.80Z",
  "updated_at" : "2016-11-09T22:33:10.80Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python



```
```shell


curl https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI5JXborVmN6x5HBPJr7KWyk');

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI5JXborVmN6x5HBPJr7KWyk")

```
> Example Response:

```json
{
  "id" : "PI5JXborVmN6x5HBPJr7KWyk",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-09T22:33:10.70Z",
  "updated_at" : "2016-11-09T22:33:11.44Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PI5JXborVmN6x5HBPJr7KWyk",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-09T22:33:10.70Z",
  "updated_at" : "2016-11-09T22:33:11.44Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "PIu2zxtZ8nyjF99HZRAkA2Vb",
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
      "created_at" : "2016-11-09T22:33:22.87Z",
      "updated_at" : "2016-11-09T22:33:22.87Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIu2zxtZ8nyjF99HZRAkA2Vb/updates"
        }
      }
    }, {
      "id" : "PIrLnVW86nYgSSrhcbpQN1eK",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-09T22:33:14.85Z",
      "updated_at" : "2016-11-09T22:33:14.85Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrLnVW86nYgSSrhcbpQN1eK"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrLnVW86nYgSSrhcbpQN1eK/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrLnVW86nYgSSrhcbpQN1eK/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrLnVW86nYgSSrhcbpQN1eK/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PIqDevPePVdTiRwodJKf87dE",
      "fingerprint" : "FPR1778398984",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Step Curry",
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
      "created_at" : "2016-11-09T22:33:14.13Z",
      "updated_at" : "2016-11-09T22:33:20.01Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDw4wTFFG5FU4Rg1nuzKCnCq",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDw4wTFFG5FU4Rg1nuzKCnCq"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE/updates"
        }
      }
    }, {
      "id" : "PIgiN4W9RLNKczqyoVjTgFL6",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:12.21Z",
      "updated_at" : "2016-11-09T22:33:12.21Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgiN4W9RLNKczqyoVjTgFL6"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgiN4W9RLNKczqyoVjTgFL6/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgiN4W9RLNKczqyoVjTgFL6/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgiN4W9RLNKczqyoVjTgFL6/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PI99eLwtCGb2ujft2P9K3KLY",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:12.21Z",
      "updated_at" : "2016-11-09T22:33:12.21Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PIiFY5xM361UCJnc28X9xpN3",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:12.21Z",
      "updated_at" : "2016-11-09T22:33:12.21Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiFY5xM361UCJnc28X9xpN3"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiFY5xM361UCJnc28X9xpN3/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiFY5xM361UCJnc28X9xpN3/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiFY5xM361UCJnc28X9xpN3/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PI5JXborVmN6x5HBPJr7KWyk",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-09T22:33:10.70Z",
      "updated_at" : "2016-11-09T22:33:11.44Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5JXborVmN6x5HBPJr7KWyk/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PIaad8Enk1Y3T7j1GEnxFegE",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:01.36Z",
      "updated_at" : "2016-11-09T22:33:01.36Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIaad8Enk1Y3T7j1GEnxFegE"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIaad8Enk1Y3T7j1GEnxFegE/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIaad8Enk1Y3T7j1GEnxFegE/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIaad8Enk1Y3T7j1GEnxFegE/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PI2rcLTZgxEqsFJkK5VsFrPe",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:01.36Z",
      "updated_at" : "2016-11-09T22:33:01.36Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2rcLTZgxEqsFJkK5VsFrPe"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2rcLTZgxEqsFJkK5VsFrPe/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2rcLTZgxEqsFJkK5VsFrPe/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2rcLTZgxEqsFJkK5VsFrPe/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PIr8ms6GZpK39VVrk2thrXpf",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:01.36Z",
      "updated_at" : "2016-11-09T22:33:01.36Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIr8ms6GZpK39VVrk2thrXpf"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIr8ms6GZpK39VVrk2thrXpf/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIr8ms6GZpK39VVrk2thrXpf/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIr8ms6GZpK39VVrk2thrXpf/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "PI2dYE9vKRF2ZE5Xdg4AdzYM",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-09T22:33:01.36Z",
      "updated_at" : "2016-11-09T22:33:01.36Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2dYE9vKRF2ZE5Xdg4AdzYM"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2dYE9vKRF2ZE5Xdg4AdzYM/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaHB4eaMoswCLwgQ12P1JLS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2dYE9vKRF2ZE5Xdg4AdzYM/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2dYE9vKRF2ZE5Xdg4AdzYM/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRaDDS8eTQSXrvZ5fgUKoJWP")

```
```shell

curl https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRaDDS8eTQSXrvZ5fgUKoJWP');



```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRaDDS8eTQSXrvZ5fgUKoJWP");

```
> Example Response:

```json
{
  "id" : "TRaDDS8eTQSXrvZ5fgUKoJWP",
  "amount" : 207388,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "b5b07c7e-d8de-42a7-8c96-273a52248a3e",
  "currency" : "USD",
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "source" : "PIqDevPePVdTiRwodJKf87dE",
  "destination" : "PI99eLwtCGb2ujft2P9K3KLY",
  "ready_to_settle_at" : null,
  "fee" : 20739,
  "statement_descriptor" : "PLD*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:15.66Z",
  "updated_at" : "2016-11-09T22:33:18.86Z",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY"
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
```python



```
```shell

curl https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRaDDS8eTQSXrvZ5fgUKoJWP');
$refund = $debit->reverse(50);
```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRuyXQyaaPseVqH7duKrFc7M",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "e75a180f-4b2c-4086-acb7-aebd0d910b9d",
  "currency" : "USD",
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "source" : "PI99eLwtCGb2ujft2P9K3KLY",
  "destination" : "PIqDevPePVdTiRwodJKf87dE",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "PLD*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-09T22:33:18.88Z",
  "updated_at" : "2016-11-09T22:33:18.94Z",
  "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRuyXQyaaPseVqH7duKrFc7M"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRuyXQyaaPseVqH7duKrFc7M/payment_instruments"
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
```python


from payline.resources import Transfer
transfer = Transfer.get()

```
```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "TRSbdGwMA7TNWRGRkz3iSoG",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "bff0a578-d187-4ff0-b579-cdc3aa13ae91",
      "currency" : "USD",
      "application" : "APcRz1ht766SckkM2PWh7AGT",
      "source" : "PIqDevPePVdTiRwodJKf87dE",
      "destination" : "PI99eLwtCGb2ujft2P9K3KLY",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-09T22:33:20.74Z",
      "updated_at" : "2016-11-09T22:33:20.93Z",
      "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRSbdGwMA7TNWRGRkz3iSoG/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY"
        }
      }
    }, {
      "id" : "TRuyXQyaaPseVqH7duKrFc7M",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "356c3b02-c643-446e-be5b-273ec2892f87",
      "currency" : "USD",
      "application" : "APcRz1ht766SckkM2PWh7AGT",
      "source" : "PI99eLwtCGb2ujft2P9K3KLY",
      "destination" : "PIqDevPePVdTiRwodJKf87dE",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-09T22:33:18.69Z",
      "updated_at" : "2016-11-09T22:33:18.94Z",
      "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRuyXQyaaPseVqH7duKrFc7M"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRuyXQyaaPseVqH7duKrFc7M/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
        }
      }
    }, {
      "id" : "TRaDDS8eTQSXrvZ5fgUKoJWP",
      "amount" : 207388,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "b5b07c7e-d8de-42a7-8c96-273a52248a3e",
      "currency" : "USD",
      "application" : "APcRz1ht766SckkM2PWh7AGT",
      "source" : "PIqDevPePVdTiRwodJKf87dE",
      "destination" : "PI99eLwtCGb2ujft2P9K3KLY",
      "ready_to_settle_at" : null,
      "fee" : 20739,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-09T22:33:15.66Z",
      "updated_at" : "2016-11-09T22:33:18.86Z",
      "merchant_identity" : "ID83THqukvoRDbEe696oGSvC",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRaDDS8eTQSXrvZ5fgUKoJWP/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqDevPePVdTiRwodJKf87dE"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI99eLwtCGb2ujft2P9K3KLY"
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
    "count" : 3
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
```python



```
```shell
curl https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USknYzEC7guR3xFosFZxJ7Zf",
  "password" : "e1df9f2a-1a70-465d-877f-c1b29ab9b392",
  "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:02.11Z",
  "updated_at" : "2016-11-09T22:33:02.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USknYzEC7guR3xFosFZxJ7Zf"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python



```
```shell
curl https://api-test.payline.io/identities/ID83THqukvoRDbEe696oGSvC/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UScDQQqXrvFyRHtJ91HvDkLZ",
  "password" : "17aebe76-27e2-44c9-9d04-53c7c6f088e0",
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:16.75Z",
  "updated_at" : "2016-11-09T22:33:16.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UScDQQqXrvFyRHtJ91HvDkLZ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import User
user = User.get(id="USetR78WdNpBy7TG3R5pkf22")

```
```shell
curl https://api-test.payline.io/users/TRaDDS8eTQSXrvZ5fgUKoJWP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USetR78WdNpBy7TG3R5pkf22",
  "password" : null,
  "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:00.32Z",
  "updated_at" : "2016-11-09T22:33:00.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USetR78WdNpBy7TG3R5pkf22"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python



```
```shell
curl https://api-test.payline.io/users/UScDQQqXrvFyRHtJ91HvDkLZ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UScDQQqXrvFyRHtJ91HvDkLZ",
  "password" : null,
  "identity" : "ID83THqukvoRDbEe696oGSvC",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-09T22:33:16.64Z",
  "updated_at" : "2016-11-09T22:33:17.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UScDQQqXrvFyRHtJ91HvDkLZ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import User
users = User.get()

```
```shell
curl https://api-test.payline.io/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "UScDQQqXrvFyRHtJ91HvDkLZ",
      "password" : null,
      "identity" : "ID83THqukvoRDbEe696oGSvC",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-11-09T22:33:16.64Z",
      "updated_at" : "2016-11-09T22:33:18.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/UScDQQqXrvFyRHtJ91HvDkLZ"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "USknYzEC7guR3xFosFZxJ7Zf",
      "password" : null,
      "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-09T22:33:02.05Z",
      "updated_at" : "2016-11-09T22:33:02.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USknYzEC7guR3xFosFZxJ7Zf"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
        }
      }
    }, {
      "id" : "USetR78WdNpBy7TG3R5pkf22",
      "password" : null,
      "identity" : "IDaHB4eaMoswCLwgQ12P1JLS",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-09T22:33:00.32Z",
      "updated_at" : "2016-11-09T22:33:00.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USetR78WdNpBy7TG3R5pkf22"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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
```python


from payline.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```shell

curl https://api-test.payline.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b \
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
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
  "id" : "WHs8643F7gcZCKdhtZqWnaDv",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "created_at" : "2016-11-09T22:33:03.60Z",
  "updated_at" : "2016-11-09T22:33:03.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHs8643F7gcZCKdhtZqWnaDv"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python


from payline.resources import Webhook
webhook = Webhook.get(id="WHs8643F7gcZCKdhtZqWnaDv")

```
```shell



curl https://api-test.payline.io/webhooks/WHs8643F7gcZCKdhtZqWnaDv \
    -H "Content-Type: application/vnd.json+api" \
    -u USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHs8643F7gcZCKdhtZqWnaDv');



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHs8643F7gcZCKdhtZqWnaDv");

```
> Example Response:

```json
{
  "id" : "WHs8643F7gcZCKdhtZqWnaDv",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APcRz1ht766SckkM2PWh7AGT",
  "created_at" : "2016-11-09T22:33:03.60Z",
  "updated_at" : "2016-11-09T22:33:03.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHs8643F7gcZCKdhtZqWnaDv"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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

```python


from payline.resources import Webhook
webhooks = Webhook.get()

```
```shell
curl https://api-test.payline.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USetR78WdNpBy7TG3R5pkf22:e80c0f67-7d70-4190-a3a8-82194c072e4b

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
      "id" : "WHs8643F7gcZCKdhtZqWnaDv",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APcRz1ht766SckkM2PWh7AGT",
      "created_at" : "2016-11-09T22:33:03.60Z",
      "updated_at" : "2016-11-09T22:33:03.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHs8643F7gcZCKdhtZqWnaDv"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APcRz1ht766SckkM2PWh7AGT"
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


```python


```
```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USetR78WdNpBy7TG3R5pkf22', 'e80c0f67-7d70-4190-a3a8-82194c072e4b');
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
