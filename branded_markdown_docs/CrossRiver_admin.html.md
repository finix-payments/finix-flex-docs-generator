---
title: CrossRiver API Reference

language_tabs:
- shell: cURL
- java: Java
- php: PHP
- python: Python



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

4. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("US7SmioH7VFU7C7FJemcwAGE", "5325d272-1fa0-4927-bfd3-aa735ea4d57c"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US7SmioH7VFU7C7FJemcwAGE`

- Password: `5325d272-1fa0-4927-bfd3-aa735ea4d57c`

- Application ID: `APrzEC6Mru5WBDG18hyeqtgi`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** https://api-staging.finix.io

- **Production API:** https://api.finix.io

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
```python


from crossriver.resources import Identity

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
	}).save()

```
> Example Response:

```json
{
  "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
  "created_at" : "2016-11-14T18:02:16.76Z",
  "updated_at" : "2016-11-14T18:02:16.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	    "identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L"
	));
$bank_account = $bank_account->save();

```
```python


from crossriver.resources import BankAccount

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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-14T18:02:23.30Z",
  "updated_at" : "2016-11-14T18:02:23.30Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuvxRzFoqCoAp9aVBQ7uo3L');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuvxRzFoqCoAp9aVBQ7uo3L")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : "VI6eQTXmGp8SVPMKSJPLjdgB",
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.91Z",
  "updated_at" : "2016-11-14T18:02:24.91Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI6eQTXmGp8SVPMKSJPLjdgB"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	        "first_name"=> "Alex", 
	        "last_name"=> "Green", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
	}).save()

```
> Example Response:

```json
{
  "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2016-11-14T18:02:26.10Z",
  "updated_at" : "2016-11-14T18:02:26.10Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Sean Le", 
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
	    "identity"=> "ID4Z6Zkn9AE8sAr92UHJQ16V"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI24rqMazsB5Jp9xmVX36A9T",
  "fingerprint" : "FPR760037534",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Le",
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
  "created_at" : "2016-11-14T18:02:26.69Z",
  "updated_at" : "2016-11-14T18:02:26.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/updates"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```python


from crossriver.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.29Z",
  "updated_at" : "2016-11-14T18:02:32.30Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
curl https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnN3ftUTegqBw6aBc7hvpCP");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUnN3ftUTegqBw6aBc7hvpCP');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUnN3ftUTegqBw6aBc7hvpCP")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6qLSZrACvtg3ZfJtcHhuK2",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.14Z",
  "updated_at" : "2016-11-14T18:02:33.37Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
          applicationId: 'APrzEC6Mru5WBDG18hyeqtgi',
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
  "id" : "TKkD2HrpqWb6Gh3VHqWqEutU",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-14T18:02:35.26Z",
  "updated_at" : "2016-11-14T18:02:35.26Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-15T18:02:35.26Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIkD2HrpqWb6Gh3VHqWqEutU",
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
  "created_at" : "2016-11-14T18:02:35.92Z",
  "updated_at" : "2016-11-14T18:02:35.92Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/updates"
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


## Push-to-Card
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Fran", 
	        "last_name": "Diaz", 
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
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDfkpWJZyVTX9sYw1wJHQTCP",
  "entity" : {
    "title" : null,
    "first_name" : "Fran",
    "last_name" : "Diaz",
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
  "created_at" : "2016-11-14T18:02:45.32Z",
  "updated_at" : "2016-11-14T18:02:45.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "name": "Jessie Kline", 
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
	    "identity": "IDfkpWJZyVTX9sYw1wJHQTCP"
	}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as"=> "Paypal", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Paypal", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```python



```
> Example Response:

```json
{
  "id" : "PI5zk4KBXurNYd5uwhSvZGzK",
  "fingerprint" : "FPR292298856",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Kline",
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
  "created_at" : "2016-11-14T18:02:46.77Z",
  "updated_at" : "2016-11-14T18:02:46.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfkpWJZyVTX9sYw1wJHQTCP",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/updates"
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

### Step 3: Provision Merchant Account
```shell
curl https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MU7U2eNNCfjnKkgJMZEwe5Kd",
  "identity" : "IDfkpWJZyVTX9sYw1wJHQTCP",
  "verification" : "VI6iKQaVEdboNkddhNaQv2pZ",
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:45.89Z",
  "updated_at" : "2016-11-14T18:02:45.89Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU7U2eNNCfjnKkgJMZEwe5Kd"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU7U2eNNCfjnKkgJMZEwe5Kd/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI6iKQaVEdboNkddhNaQv2pZ"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor


### Step 4: Send Payout

Once you have tokenized the payment card as above you can send funds to it at any time by simply calling the API


```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDfkpWJZyVTX9sYw1wJHQTCP", 
	    "destination": "PI5zk4KBXurNYd5uwhSvZGzK", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as"=> "Paypal", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Paypal", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRcDfLssaSgBSwWrjR9jmx8Q",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "91521",
  "currency" : "USD",
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "source" : "PIpq9xRB7YVVbKaWYZHXTZaZ",
  "destination" : "PI5zk4KBXurNYd5uwhSvZGzK",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:48.11Z",
  "updated_at" : "2016-11-14T18:02:49.43Z",
  "merchant_identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK"
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
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
```python


from crossriver.resources import Identity

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
	}).save()

```
> Example Response:

```json
{
  "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
  "created_at" : "2016-11-14T18:02:16.76Z",
  "updated_at" : "2016-11-14T18:02:16.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	    "identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L"
	));
$bank_account = $bank_account->save();

```
```python


from crossriver.resources import BankAccount

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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-14T18:02:23.30Z",
  "updated_at" : "2016-11-14T18:02:23.30Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuvxRzFoqCoAp9aVBQ7uo3L');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuvxRzFoqCoAp9aVBQ7uo3L")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : "VI6eQTXmGp8SVPMKSJPLjdgB",
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.91Z",
  "updated_at" : "2016-11-14T18:02:24.91Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI6eQTXmGp8SVPMKSJPLjdgB"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	        "first_name"=> "Alex", 
	        "last_name"=> "Green", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
	}).save()

```
> Example Response:

```json
{
  "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2016-11-14T18:02:26.10Z",
  "updated_at" : "2016-11-14T18:02:26.10Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Sean Le", 
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
	    "identity"=> "ID4Z6Zkn9AE8sAr92UHJQ16V"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI24rqMazsB5Jp9xmVX36A9T",
  "fingerprint" : "FPR760037534",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Le",
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
  "created_at" : "2016-11-14T18:02:26.69Z",
  "updated_at" : "2016-11-14T18:02:26.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/updates"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```python


from crossriver.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.29Z",
  "updated_at" : "2016-11-14T18:02:32.30Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
curl https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnN3ftUTegqBw6aBc7hvpCP");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUnN3ftUTegqBw6aBc7hvpCP');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUnN3ftUTegqBw6aBc7hvpCP")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6qLSZrACvtg3ZfJtcHhuK2",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.14Z",
  "updated_at" : "2016-11-14T18:02:33.37Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
curl https://api-staging.finix.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "role": "ROLE_PARTNER"
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "US7SmioH7VFU7C7FJemcwAGE",
  "password" : "5325d272-1fa0-4927-bfd3-aa735ea4d57c",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:11.48Z",
  "updated_at" : "2016-11-14T18:02:11.48Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US7SmioH7VFU7C7FJemcwAGE"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
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

`POST https://api-staging.finix.io/users`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user (use ROLE_PARTNER when creating a new `Application`)

### Step 2: Create the Application
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as"=> "Paypal", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Paypal", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```python



```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-14T18:02:11.96Z",
  "updated_at" : "2016-11-14T18:02:11.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
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

`POST https://api-staging.finix.io/applications`

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
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PRtW7NmF1Cum9sVmJHkQz6VX",
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "default_merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "created_at" : "2016-11-14T18:02:12.55Z",
  "updated_at" : "2016-11-14T18:02:12.55Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors/PRtW7NmF1Cum9sVmJHkQz6VX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The CrossRiver Payment Platform is processor agnostic allowing for processing transactions
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

`POST https://api-staging.finix.io/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

### Step 4: Enable Processing Functionality
```shell
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-11-14T18:02:11.90Z",
  "updated_at" : "2016-11-14T18:03:02.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
    }
  }
}
```

Now that we have a processor associated with an `Application` we'll want to
enable its ability to creaet new `Transfers` and `Authorizations`. This same
method can be used to shut off its ability to process transactions as a form of
risk management.

#### HTTP Request

`PUT https://api-staging.finix.io/applications/:APPLICATION_ID`

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
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-14T18:02:11.90Z",
  "updated_at" : "2016-11-14T18:03:03.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
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

`PUT https://api-staging.finix.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | True to enable
## Tokenization.js

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to CrossRiver.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/2hxnjL0q/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the CrossRiver API.
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
    server: "https://api-staging.finix.io",
    applicationId: "APrzEC6Mru5WBDG18hyeqtgi",
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
server | *string*, **required** |  The base url for the CrossRiver API
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
  "id" : "TKkD2HrpqWb6Gh3VHqWqEutU",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-14T18:02:35.26Z",
  "updated_at" : "2016-11-14T18:02:35.26Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-15T18:02:35.26Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'

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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIkD2HrpqWb6Gh3VHqWqEutU",
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
  "created_at" : "2016-11-14T18:02:35.92Z",
  "updated_at" : "2016-11-14T18:02:35.92Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/updates"
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

`POST https://api-staging.finix.io/payment_instruments`


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

## Fetch an Application
```shell
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = Application::retrieve('APrzEC6Mru5WBDG18hyeqtgi');

```
```python


from crossriver.resources import Application

application = Application.get(id="APrzEC6Mru5WBDG18hyeqtgi")
```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-14T18:02:11.90Z",
  "updated_at" : "2016-11-14T18:02:15.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## Create an Application
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -d '
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as"=> "Paypal", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Paypal", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();

```
```python


from crossriver.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "US7SmioH7VFU7C7FJemcwAGE", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-14T18:02:11.96Z",
  "updated_at" : "2016-11-14T18:02:11.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
    }
  }
}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can create a new Application.
</aside>

#### HTTP Request

`POST https://api-staging.finix.io/applications`

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
## [ADMIN] Disable Processing Functionality
```shell
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-11-14T18:02:11.90Z",
  "updated_at" : "2016-11-14T18:02:59.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
    }
  }
}
```

Disable an `Applications's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-staging.finix.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processing_enabled | *boolean*, **required** | False to disable
## [ADMIN] Disable Settlement Functionality
```shell
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "APrzEC6Mru5WBDG18hyeqtgi",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-14T18:02:11.90Z",
  "updated_at" : "2016-11-14T18:03:00.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
    }
  }
}
```

Disable an `Applications's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-staging.finix.io/applications/:APPLICATION_ID`

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
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USkC2TAG3o9ysHSQ7XCmcrgV",
  "password" : "ad92f1a9-1903-4794-ab19-1c32d8e942ac",
  "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:13.73Z",
  "updated_at" : "2016-11-14T18:02:13.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USkC2TAG3o9ysHSQ7XCmcrgV"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

`POST https://api-staging.finix.io/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## [ADMIN] Enable the Dummy Processor (i.e. Sandbox)
```shell
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PRtW7NmF1Cum9sVmJHkQz6VX",
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "default_merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "created_at" : "2016-11-14T18:02:12.55Z",
  "updated_at" : "2016-11-14T18:02:12.55Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors/PRtW7NmF1Cum9sVmJHkQz6VX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

`POST https://api-staging.finix.io/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## [ADMIN] List all Applications
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Application

application = Application.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APrzEC6Mru5WBDG18hyeqtgi",
      "enabled" : true,
      "tags" : {
        "application_name" : "Paypal"
      },
      "owner" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-11-14T18:02:11.90Z",
      "updated_at" : "2016-11-14T18:02:15.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/tokens"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/applications/`


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```python


from crossriver.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDuvxRzFoqCoAp9aVBQ7uo3L", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI24rqMazsB5Jp9xmVX36A9T", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.29Z",
  "updated_at" : "2016-11-14T18:02:32.30Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
curl https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnN3ftUTegqBw6aBc7hvpCP");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUnN3ftUTegqBw6aBc7hvpCP');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUnN3ftUTegqBw6aBc7hvpCP")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6qLSZrACvtg3ZfJtcHhuK2",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.14Z",
  "updated_at" : "2016-11-14T18:02:33.37Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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

curl https://api-staging.finix.io/authorizations/AU7VmErJFGUBY892kz3LVCpb \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUnN3ftUTegqBw6aBc7hvpCP")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AU7VmErJFGUBY892kz3LVCpb",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:36.73Z",
  "updated_at" : "2016-11-14T18:02:38.61Z",
  "trace_id" : "8490abc1-14e3-4744-b181-884354447be3",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : true,
  "expires_at" : "2016-11-21T18:02:36.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU7VmErJFGUBY892kz3LVCpb"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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

curl https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnN3ftUTegqBw6aBc7hvpCP");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUnN3ftUTegqBw6aBc7hvpCP');

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUnN3ftUTegqBw6aBc7hvpCP")
```
> Example Response:

```json
{
  "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6qLSZrACvtg3ZfJtcHhuK2",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:32.14Z",
  "updated_at" : "2016-11-14T18:02:33.37Z",
  "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "is_void" : false,
  "expires_at" : "2016-11-21T18:02:32.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java
import io.payline.payments.processing.client.model.Authorization;

client.authorizationsClient().<Resources<Authorization>>resourcesIterator()
  .forEachRemaining(page-> {
    Collection<Authorization> authorizations = page.getContent();
    //do something
  });
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Authorization

authorization = Authorization.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU7VmErJFGUBY892kz3LVCpb",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:36.73Z",
      "updated_at" : "2016-11-14T18:02:38.61Z",
      "trace_id" : "8490abc1-14e3-4744-b181-884354447be3",
      "source" : "PI24rqMazsB5Jp9xmVX36A9T",
      "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "is_void" : true,
      "expires_at" : "2016-11-21T18:02:36.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU7VmErJFGUBY892kz3LVCpb"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        }
      }
    }, {
      "id" : "AUnN3ftUTegqBw6aBc7hvpCP",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR6qLSZrACvtg3ZfJtcHhuK2",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:32.14Z",
      "updated_at" : "2016-11-14T18:02:33.37Z",
      "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
      "source" : "PI24rqMazsB5Jp9xmVX36A9T",
      "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "is_void" : false,
      "expires_at" : "2016-11-21T18:02:32.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUnN3ftUTegqBw6aBc7hvpCP"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	        "first_name"=> "Alex", 
	        "last_name"=> "Green", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2016-11-14T18:02:26.10Z",
  "updated_at" : "2016-11-14T18:02:26.10Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
```python


from crossriver.resources import Identity

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
	}).save()
```
> Example Response:

```json
{
  "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
  "created_at" : "2016-11-14T18:02:16.76Z",
  "updated_at" : "2016-11-14T18:02:16.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDuvxRzFoqCoAp9aVBQ7uo3L");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuvxRzFoqCoAp9aVBQ7uo3L');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDuvxRzFoqCoAp9aVBQ7uo3L")

```
> Example Response:

```json
{
  "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
  "created_at" : "2016-11-14T18:02:16.70Z",
  "updated_at" : "2016-11-14T18:02:16.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

## Update an Identity
```shell
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Walter", 
	        "last_name": "White", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Lees Sandwiches", 
	        "url": "www.LeesSandwiches.com", 
	        "business_name": "Lees Sandwiches", 
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
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Walter",
    "last_name" : "White",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Lees Sandwiches",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-14T18:02:16.70Z",
  "updated_at" : "2016-11-14T18:02:56.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
## List all Identities
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c


```
```java
import io.crossriver.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Identity
identity = Identity.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDfkpWJZyVTX9sYw1wJHQTCP",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Diaz",
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
      "created_at" : "2016-11-14T18:02:45.25Z",
      "updated_at" : "2016-11-14T18:02:45.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-14T18:02:26.04Z",
      "updated_at" : "2016-11-14T18:02:26.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdGcBGZvYQPvYdj76nbvSgy",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-14T18:02:22.51Z",
      "updated_at" : "2016-11-14T18:02:22.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDnsiSBB8QrRGvGx2yuptVpx",
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
      "created_at" : "2016-11-14T18:02:21.76Z",
      "updated_at" : "2016-11-14T18:02:21.76Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDmoVmcZSLbhicE2ACF9p9se",
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
      "created_at" : "2016-11-14T18:02:21.17Z",
      "updated_at" : "2016-11-14T18:02:21.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDgq6R2eGM2JsGRexi13eUTf",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-14T18:02:20.42Z",
      "updated_at" : "2016-11-14T18:02:20.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuBDEhJWprb5t8qoNw698Cu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.86Z",
      "updated_at" : "2016-11-14T18:02:19.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDh1DLPRFXKx44ezKsgHA4Hj",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.18Z",
      "updated_at" : "2016-11-14T18:02:19.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDjWiBrYEdfYADy2sWgnxSZY",
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
      "created_at" : "2016-11-14T18:02:18.46Z",
      "updated_at" : "2016-11-14T18:02:18.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID3uj3ynnHsCdALBUXNUD3DQ",
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
      "created_at" : "2016-11-14T18:02:17.85Z",
      "updated_at" : "2016-11-14T18:02:17.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdsJWN4LAzBvhBq8mhx6pgc",
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
      "created_at" : "2016-11-14T18:02:17.24Z",
      "updated_at" : "2016-11-14T18:02:17.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
      "created_at" : "2016-11-14T18:02:16.70Z",
      "updated_at" : "2016-11-14T18:02:16.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Paypal",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Paypal",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2016-11-14T18:02:11.90Z",
      "updated_at" : "2016-11-14T18:02:11.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuvxRzFoqCoAp9aVBQ7uo3L');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuvxRzFoqCoAp9aVBQ7uo3L")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : "VI6eQTXmGp8SVPMKSJPLjdgB",
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.91Z",
  "updated_at" : "2016-11-14T18:02:24.91Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI6eQTXmGp8SVPMKSJPLjdgB"
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
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUpzwfJ8iFqpSECibyCcscBj");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUpzwfJ8iFqpSECibyCcscBj');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUpzwfJ8iFqpSECibyCcscBj")

```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : null,
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.80Z",
  "updated_at" : "2016-11-14T18:02:25.02Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

## Update Info on Processor
```shell
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VI5qGe3YUuXXC3Qd2JLnoCYB",
  "external_trace_id" : "b35d60f5-5a4f-479a-b5cc-0c39560a6df1",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-14T18:02:57.87Z",
  "updated_at" : "2016-11-14T18:02:57.89Z",
  "payment_instrument" : null,
  "merchant" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI5qGe3YUuXXC3Qd2JLnoCYB"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
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

## Reattempt Merchant Provisioning
```shell
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VI5qGe3YUuXXC3Qd2JLnoCYB",
  "external_trace_id" : "b35d60f5-5a4f-479a-b5cc-0c39560a6df1",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-14T18:02:57.87Z",
  "updated_at" : "2016-11-14T18:02:57.89Z",
  "payment_instrument" : null,
  "merchant" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI5qGe3YUuXXC3Qd2JLnoCYB"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
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

## Disable Processing Functionality
```shell
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : null,
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.80Z",
  "updated_at" : "2016-11-14T18:02:58.42Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

Disable a `Merchant's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-staging.finix.io/merchants/:MERCHANT_ID`

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
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUpzwfJ8iFqpSECibyCcscBj",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "verification" : null,
  "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-14T18:02:24.80Z",
  "updated_at" : "2016-11-14T18:02:59.16Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```
Disable a `Merchant's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-staging.finix.io/merchants/:MERCHANT_ID`

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
curl https://api-staging.finix.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Merchant
merchant = Merchant.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU7U2eNNCfjnKkgJMZEwe5Kd",
      "identity" : "IDfkpWJZyVTX9sYw1wJHQTCP",
      "verification" : null,
      "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-14T18:02:45.82Z",
      "updated_at" : "2016-11-14T18:02:45.82Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU7U2eNNCfjnKkgJMZEwe5Kd"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU7U2eNNCfjnKkgJMZEwe5Kd/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "MUpzwfJ8iFqpSECibyCcscBj",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "verification" : null,
      "merchant_profile" : "MPqLm1jcrrdqoPX5B6cuQPhs",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-14T18:02:24.80Z",
      "updated_at" : "2016-11-14T18:02:25.02Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPqLm1jcrrdqoPX5B6cuQPhs"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    "count" : 2
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/merchants/`

## List Merchant Verifications
```shell
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDfkpWJZyVTX9sYw1wJHQTCP",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Diaz",
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
      "created_at" : "2016-11-14T18:02:45.25Z",
      "updated_at" : "2016-11-14T18:02:45.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-14T18:02:26.04Z",
      "updated_at" : "2016-11-14T18:02:26.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdGcBGZvYQPvYdj76nbvSgy",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-14T18:02:22.51Z",
      "updated_at" : "2016-11-14T18:02:22.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDnsiSBB8QrRGvGx2yuptVpx",
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
      "created_at" : "2016-11-14T18:02:21.76Z",
      "updated_at" : "2016-11-14T18:02:21.76Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDmoVmcZSLbhicE2ACF9p9se",
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
      "created_at" : "2016-11-14T18:02:21.17Z",
      "updated_at" : "2016-11-14T18:02:21.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDgq6R2eGM2JsGRexi13eUTf",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-14T18:02:20.42Z",
      "updated_at" : "2016-11-14T18:02:20.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuBDEhJWprb5t8qoNw698Cu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.86Z",
      "updated_at" : "2016-11-14T18:02:19.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDh1DLPRFXKx44ezKsgHA4Hj",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.18Z",
      "updated_at" : "2016-11-14T18:02:19.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDjWiBrYEdfYADy2sWgnxSZY",
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
      "created_at" : "2016-11-14T18:02:18.46Z",
      "updated_at" : "2016-11-14T18:02:18.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID3uj3ynnHsCdALBUXNUD3DQ",
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
      "created_at" : "2016-11-14T18:02:17.85Z",
      "updated_at" : "2016-11-14T18:02:17.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdsJWN4LAzBvhBq8mhx6pgc",
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
      "created_at" : "2016-11-14T18:02:17.24Z",
      "updated_at" : "2016-11-14T18:02:17.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
      "created_at" : "2016-11-14T18:02:16.70Z",
      "updated_at" : "2016-11-14T18:02:16.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Paypal",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Paypal",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2016-11-14T18:02:11.90Z",
      "updated_at" : "2016-11-14T18:02:11.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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




## [ADMIN] List Merchant Verifications
```shell
curl https://api-staging.finix.io/merchants/MUpzwfJ8iFqpSECibyCcscBj/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDfkpWJZyVTX9sYw1wJHQTCP",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Diaz",
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
      "created_at" : "2016-11-14T18:02:45.25Z",
      "updated_at" : "2016-11-14T18:02:45.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-14T18:02:26.04Z",
      "updated_at" : "2016-11-14T18:02:26.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdGcBGZvYQPvYdj76nbvSgy",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-14T18:02:22.51Z",
      "updated_at" : "2016-11-14T18:02:22.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcBGZvYQPvYdj76nbvSgy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDnsiSBB8QrRGvGx2yuptVpx",
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
      "created_at" : "2016-11-14T18:02:21.76Z",
      "updated_at" : "2016-11-14T18:02:21.76Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnsiSBB8QrRGvGx2yuptVpx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDmoVmcZSLbhicE2ACF9p9se",
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
      "created_at" : "2016-11-14T18:02:21.17Z",
      "updated_at" : "2016-11-14T18:02:21.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmoVmcZSLbhicE2ACF9p9se/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDgq6R2eGM2JsGRexi13eUTf",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-14T18:02:20.42Z",
      "updated_at" : "2016-11-14T18:02:20.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgq6R2eGM2JsGRexi13eUTf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuBDEhJWprb5t8qoNw698Cu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.86Z",
      "updated_at" : "2016-11-14T18:02:19.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuBDEhJWprb5t8qoNw698Cu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDh1DLPRFXKx44ezKsgHA4Hj",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-14T18:02:19.18Z",
      "updated_at" : "2016-11-14T18:02:19.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDh1DLPRFXKx44ezKsgHA4Hj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDjWiBrYEdfYADy2sWgnxSZY",
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
      "created_at" : "2016-11-14T18:02:18.46Z",
      "updated_at" : "2016-11-14T18:02:18.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjWiBrYEdfYADy2sWgnxSZY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "ID3uj3ynnHsCdALBUXNUD3DQ",
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
      "created_at" : "2016-11-14T18:02:17.85Z",
      "updated_at" : "2016-11-14T18:02:17.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3uj3ynnHsCdALBUXNUD3DQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDdsJWN4LAzBvhBq8mhx6pgc",
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
      "created_at" : "2016-11-14T18:02:17.24Z",
      "updated_at" : "2016-11-14T18:02:17.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdsJWN4LAzBvhBq8mhx6pgc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
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
      "created_at" : "2016-11-14T18:02:16.70Z",
      "updated_at" : "2016-11-14T18:02:16.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Paypal",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Paypal",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2016-11-14T18:02:11.90Z",
      "updated_at" : "2016-11-14T18:02:11.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
Only `Users` with ROLE_PLATFORM permissions can view the `message` and `raw`
 fields.



#### HTTP Request

`GET https://api-staging.finix.io/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


## Create a Merchant User
```shell
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "US8Yxf2efAQauM1MaTWziXGD",
  "password" : "3ca53f89-5f81-4710-8e94-679df8add34b",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:29.08Z",
  "updated_at" : "2016-11-14T18:02:29.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US8Yxf2efAQauM1MaTWziXGD"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
          applicationId: 'APrzEC6Mru5WBDG18hyeqtgi',
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
  "id" : "TKkD2HrpqWb6Gh3VHqWqEutU",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-14T18:02:35.26Z",
  "updated_at" : "2016-11-14T18:02:35.26Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-15T18:02:35.26Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'

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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIkD2HrpqWb6Gh3VHqWqEutU",
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
  "created_at" : "2016-11-14T18:02:35.92Z",
  "updated_at" : "2016-11-14T18:02:35.92Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/updates"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkD2HrpqWb6Gh3VHqWqEutU", 
	    "type": "TOKEN", 
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIkD2HrpqWb6Gh3VHqWqEutU",
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
  "created_at" : "2016-11-14T18:02:35.92Z",
  "updated_at" : "2016-11-14T18:02:35.92Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/updates"
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


## Create a Card
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Sean Le", 
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
	    "identity"=> "ID4Z6Zkn9AE8sAr92UHJQ16V"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Sean Le", 
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
	    "identity": "ID4Z6Zkn9AE8sAr92UHJQ16V"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI24rqMazsB5Jp9xmVX36A9T",
  "fingerprint" : "FPR760037534",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Le",
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
  "created_at" : "2016-11-14T18:02:26.69Z",
  "updated_at" : "2016-11-14T18:02:26.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/updates"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}'


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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
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
	    "identity"=> "IDuvxRzFoqCoAp9aVBQ7uo3L"
	));
$bank_account = $bank_account->save();


```
```python


from crossriver.resources import BankAccount

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
	    "identity": "IDuvxRzFoqCoAp9aVBQ7uo3L"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-14T18:02:23.30Z",
  "updated_at" : "2016-11-14T18:02:23.30Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
## Fetch a Payment Instrument

```shell


curl https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI6mLN9oKiih9FiXFPSf4ZaP")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI6mLN9oKiih9FiXFPSf4ZaP');

```
```python



```
> Example Response:

```json
{
  "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-14T18:02:23.20Z",
  "updated_at" : "2016-11-14T18:02:24.00Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
curl https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
	    }
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-14T18:02:23.20Z",
  "updated_at" : "2016-11-14T18:02:24.00Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c
```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI5zk4KBXurNYd5uwhSvZGzK",
      "fingerprint" : "FPR292298856",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jessie Kline",
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
      "created_at" : "2016-11-14T18:02:46.68Z",
      "updated_at" : "2016-11-14T18:02:46.68Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDfkpWJZyVTX9sYw1wJHQTCP",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfkpWJZyVTX9sYw1wJHQTCP"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK/updates"
        }
      }
    }, {
      "id" : "PIp1XHMz4pUN9uFE3QVAvs6F",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:43.96Z",
      "updated_at" : "2016-11-14T18:02:43.96Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp1XHMz4pUN9uFE3QVAvs6F"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp1XHMz4pUN9uFE3QVAvs6F/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp1XHMz4pUN9uFE3QVAvs6F/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp1XHMz4pUN9uFE3QVAvs6F/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PIpq9xRB7YVVbKaWYZHXTZaZ",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:43.96Z",
      "updated_at" : "2016-11-14T18:02:43.96Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PI4JHF3RSnjsJSGDJFX3V7rD",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:43.96Z",
      "updated_at" : "2016-11-14T18:02:43.96Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4JHF3RSnjsJSGDJFX3V7rD"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4JHF3RSnjsJSGDJFX3V7rD/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4JHF3RSnjsJSGDJFX3V7rD/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4JHF3RSnjsJSGDJFX3V7rD/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PIaugTQrtbsYKeC5fhdfqhLy",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:43.96Z",
      "updated_at" : "2016-11-14T18:02:43.96Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaugTQrtbsYKeC5fhdfqhLy"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaugTQrtbsYKeC5fhdfqhLy/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaugTQrtbsYKeC5fhdfqhLy/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaugTQrtbsYKeC5fhdfqhLy/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PIkD2HrpqWb6Gh3VHqWqEutU",
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
      "created_at" : "2016-11-14T18:02:35.78Z",
      "updated_at" : "2016-11-14T18:02:35.78Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkD2HrpqWb6Gh3VHqWqEutU/updates"
        }
      }
    }, {
      "id" : "PIqoV3CRD2mqaFGSqWWB6yXX",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-14T18:02:27.30Z",
      "updated_at" : "2016-11-14T18:02:27.30Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqoV3CRD2mqaFGSqWWB6yXX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqoV3CRD2mqaFGSqWWB6yXX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqoV3CRD2mqaFGSqWWB6yXX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqoV3CRD2mqaFGSqWWB6yXX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PI24rqMazsB5Jp9xmVX36A9T",
      "fingerprint" : "FPR760037534",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Sean Le",
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
      "created_at" : "2016-11-14T18:02:26.61Z",
      "updated_at" : "2016-11-14T18:02:32.30Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID4Z6Zkn9AE8sAr92UHJQ16V",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4Z6Zkn9AE8sAr92UHJQ16V"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T/updates"
        }
      }
    }, {
      "id" : "PImPboqJ9Tu2oCXArX7RxshV",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:24.80Z",
      "updated_at" : "2016-11-14T18:02:24.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImPboqJ9Tu2oCXArX7RxshV"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImPboqJ9Tu2oCXArX7RxshV/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImPboqJ9Tu2oCXArX7RxshV/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImPboqJ9Tu2oCXArX7RxshV/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PIfxtHrRCW33Arun5vg1tZQm",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:24.80Z",
      "updated_at" : "2016-11-14T18:02:24.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PItbZcoQ23M9vuaAvKq73Yv9",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:24.80Z",
      "updated_at" : "2016-11-14T18:02:24.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbZcoQ23M9vuaAvKq73Yv9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbZcoQ23M9vuaAvKq73Yv9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbZcoQ23M9vuaAvKq73Yv9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItbZcoQ23M9vuaAvKq73Yv9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PI6mLN9oKiih9FiXFPSf4ZaP",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-14T18:02:23.20Z",
      "updated_at" : "2016-11-14T18:02:24.00Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6mLN9oKiih9FiXFPSf4ZaP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PI3m1rBBrrWPrSV4Rm5DqkpS",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:12.47Z",
      "updated_at" : "2016-11-14T18:02:12.47Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3m1rBBrrWPrSV4Rm5DqkpS"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3m1rBBrrWPrSV4Rm5DqkpS/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3m1rBBrrWPrSV4Rm5DqkpS/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3m1rBBrrWPrSV4Rm5DqkpS/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PIbFw4HFf7vaq2SZBYyG7SL5",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:12.47Z",
      "updated_at" : "2016-11-14T18:02:12.47Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbFw4HFf7vaq2SZBYyG7SL5"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbFw4HFf7vaq2SZBYyG7SL5/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbFw4HFf7vaq2SZBYyG7SL5/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbFw4HFf7vaq2SZBYyG7SL5/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PI85rQ91MLUhKrTwx8gDXGeC",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:12.47Z",
      "updated_at" : "2016-11-14T18:02:12.47Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI85rQ91MLUhKrTwx8gDXGeC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI85rQ91MLUhKrTwx8gDXGeC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI85rQ91MLUhKrTwx8gDXGeC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI85rQ91MLUhKrTwx8gDXGeC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "PImG19REpFqDrZfvprHkMHkm",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-14T18:02:12.47Z",
      "updated_at" : "2016-11-14T18:02:12.47Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImG19REpFqDrZfvprHkMHkm"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImG19REpFqDrZfvprHkMHkm/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImG19REpFqDrZfvprHkMHkm/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImG19REpFqDrZfvprHkMHkm/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

curl https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR5PYMoYaSFsrnTyntZ5nJuS");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TR5PYMoYaSFsrnTyntZ5nJuS');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TR5PYMoYaSFsrnTyntZ5nJuS")

```
> Example Response:

```json
{
  "id" : "TR5PYMoYaSFsrnTyntZ5nJuS",
  "amount" : 441533,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "fc68974d-e9ea-47d7-b338-6bbc7c87c849",
  "currency" : "USD",
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "source" : "PI24rqMazsB5Jp9xmVX36A9T",
  "destination" : "PIfxtHrRCW33Arun5vg1tZQm",
  "ready_to_settle_at" : null,
  "fee" : 44153,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:28.21Z",
  "updated_at" : "2016-11-14T18:02:31.02Z",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm"
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

curl https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```java

import io.crossriver.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TR5PYMoYaSFsrnTyntZ5nJuS');
$refund = $debit->reverse(50);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TR5PYMoYaSFsrnTyntZ5nJuS")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRbNRY26KcA77vY9FiS6Dfup",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "5786647f-28ca-4438-a1af-d7281ba6607f",
  "currency" : "USD",
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "source" : "PIfxtHrRCW33Arun5vg1tZQm",
  "destination" : "PI24rqMazsB5Jp9xmVX36A9T",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-14T18:02:31.06Z",
  "updated_at" : "2016-11-14T18:02:31.15Z",
  "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRbNRY26KcA77vY9FiS6Dfup"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRbNRY26KcA77vY9FiS6Dfup/payment_instruments"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java
import io.crossriver.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Transfer
transfer = Transfer.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRcDfLssaSgBSwWrjR9jmx8Q",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "91521",
      "currency" : "USD",
      "application" : "APrzEC6Mru5WBDG18hyeqtgi",
      "source" : "PIpq9xRB7YVVbKaWYZHXTZaZ",
      "destination" : "PI5zk4KBXurNYd5uwhSvZGzK",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:47.88Z",
      "updated_at" : "2016-11-14T18:02:49.43Z",
      "merchant_identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDr3JqaKV76zBAvB48Hcjfoa"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcDfLssaSgBSwWrjR9jmx8Q/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpq9xRB7YVVbKaWYZHXTZaZ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5zk4KBXurNYd5uwhSvZGzK"
        }
      }
    }, {
      "id" : "TR6qLSZrACvtg3ZfJtcHhuK2",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "65d9abe3-9c53-4cef-888f-39f740ffcbcb",
      "currency" : "USD",
      "application" : "APrzEC6Mru5WBDG18hyeqtgi",
      "source" : "PI24rqMazsB5Jp9xmVX36A9T",
      "destination" : "PIfxtHrRCW33Arun5vg1tZQm",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:33.14Z",
      "updated_at" : "2016-11-14T18:02:33.37Z",
      "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR6qLSZrACvtg3ZfJtcHhuK2/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm"
        }
      }
    }, {
      "id" : "TRbNRY26KcA77vY9FiS6Dfup",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "42460a46-0ae1-4d2e-90da-46a931646523",
      "currency" : "USD",
      "application" : "APrzEC6Mru5WBDG18hyeqtgi",
      "source" : "PIfxtHrRCW33Arun5vg1tZQm",
      "destination" : "PI24rqMazsB5Jp9xmVX36A9T",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:30.83Z",
      "updated_at" : "2016-11-14T18:02:31.15Z",
      "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRbNRY26KcA77vY9FiS6Dfup"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRbNRY26KcA77vY9FiS6Dfup/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
        }
      }
    }, {
      "id" : "TR5PYMoYaSFsrnTyntZ5nJuS",
      "amount" : 441533,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "fc68974d-e9ea-47d7-b338-6bbc7c87c849",
      "currency" : "USD",
      "application" : "APrzEC6Mru5WBDG18hyeqtgi",
      "source" : "PI24rqMazsB5Jp9xmVX36A9T",
      "destination" : "PIfxtHrRCW33Arun5vg1tZQm",
      "ready_to_settle_at" : null,
      "fee" : 44153,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-14T18:02:28.21Z",
      "updated_at" : "2016-11-14T18:02:31.02Z",
      "merchant_identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PYMoYaSFsrnTyntZ5nJuS/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI24rqMazsB5Jp9xmVX36A9T"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfxtHrRCW33Arun5vg1tZQm"
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
    "count" : 4
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers`
# Users (API Keys)

A `User` resource represents a pair of API keys which are used to perform
authenticated requests against the CrossRiver API. When making authenticated
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
curl https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USkC2TAG3o9ysHSQ7XCmcrgV",
  "password" : "ad92f1a9-1903-4794-ab19-1c32d8e942ac",
  "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:13.73Z",
  "updated_at" : "2016-11-14T18:02:13.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USkC2TAG3o9ysHSQ7XCmcrgV"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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

`POST https://api-staging.finix.io/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## Create a Merchant User

```shell
curl https://api-staging.finix.io/identities/IDuvxRzFoqCoAp9aVBQ7uo3L/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "US8Yxf2efAQauM1MaTWziXGD",
  "password" : "3ca53f89-5f81-4710-8e94-679df8add34b",
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:29.08Z",
  "updated_at" : "2016-11-14T18:02:29.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US8Yxf2efAQauM1MaTWziXGD"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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



## Retrieve a User
```shell
curl https://api-staging.finix.io/users/TR5PYMoYaSFsrnTyntZ5nJuS \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import User
user = User.get(id="US7SmioH7VFU7C7FJemcwAGE")

```
> Example Response:

```json
{
  "id" : "US7SmioH7VFU7C7FJemcwAGE",
  "password" : null,
  "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:11.47Z",
  "updated_at" : "2016-11-14T18:02:11.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US7SmioH7VFU7C7FJemcwAGE"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User`

## Disable a User
```shell
curl https://api-staging.finix.io/users/US8Yxf2efAQauM1MaTWziXGD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "US8Yxf2efAQauM1MaTWziXGD",
  "password" : null,
  "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-14T18:02:28.98Z",
  "updated_at" : "2016-11-14T18:02:29.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US8Yxf2efAQauM1MaTWziXGD"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
    }
  }
}
```

Disable API keys (i.e. credentials) for a previously created `User`

<aside class="notice">
Only Users with ROLE_PLATFORM can disable another user.
</aside>


#### HTTP Request


`PUT https://api-staging.finix.io/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User` you would like to disable

## List all Users
```shell
curl https://api-staging.finix.io/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import User
users = User.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "US8Yxf2efAQauM1MaTWziXGD",
      "password" : null,
      "identity" : "IDuvxRzFoqCoAp9aVBQ7uo3L",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-11-14T18:02:28.98Z",
      "updated_at" : "2016-11-14T18:02:30.26Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US8Yxf2efAQauM1MaTWziXGD"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "USkC2TAG3o9ysHSQ7XCmcrgV",
      "password" : null,
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-14T18:02:13.66Z",
      "updated_at" : "2016-11-14T18:02:13.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USkC2TAG3o9ysHSQ7XCmcrgV"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    }, {
      "id" : "US7SmioH7VFU7C7FJemcwAGE",
      "password" : null,
      "identity" : "IDr3JqaKV76zBAvB48Hcjfoa",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-14T18:02:11.47Z",
      "updated_at" : "2016-11-14T18:02:11.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US7SmioH7VFU7C7FJemcwAGE"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.finix.io/users`

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
    -u US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```python


from crossriver.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
> Example Response:

```json
{
  "id" : "WHccXKzkm7H8GtweixSuyJ1C",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "created_at" : "2016-11-14T18:02:16.32Z",
  "updated_at" : "2016-11-14T18:02:16.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHccXKzkm7H8GtweixSuyJ1C"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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



curl https://api-staging.finix.io/webhooks/WHccXKzkm7H8GtweixSuyJ1C \
    -H "Content-Type: application/vnd.json+api" \
    -u US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHccXKzkm7H8GtweixSuyJ1C");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHccXKzkm7H8GtweixSuyJ1C');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHccXKzkm7H8GtweixSuyJ1C")

```
> Example Response:

```json
{
  "id" : "WHccXKzkm7H8GtweixSuyJ1C",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APrzEC6Mru5WBDG18hyeqtgi",
  "created_at" : "2016-11-14T18:02:16.31Z",
  "updated_at" : "2016-11-14T18:02:16.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHccXKzkm7H8GtweixSuyJ1C"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
    -u  US7SmioH7VFU7C7FJemcwAGE:5325d272-1fa0-4927-bfd3-aa735ea4d57c

```
```java
import io.crossriver.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python


from crossriver.resources import Webhook
webhooks = Webhook.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHccXKzkm7H8GtweixSuyJ1C",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APrzEC6Mru5WBDG18hyeqtgi",
      "created_at" : "2016-11-14T18:02:16.31Z",
      "updated_at" : "2016-11-14T18:02:16.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHccXKzkm7H8GtweixSuyJ1C"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APrzEC6Mru5WBDG18hyeqtgi"
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
```java
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US7SmioH7VFU7C7FJemcwAGE', '5325d272-1fa0-4927-bfd3-aa735ea4d57c');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


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
