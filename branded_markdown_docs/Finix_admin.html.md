---
title: Finix API Reference

language_tabs:
- shell: cURL
- python: Python
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

4. [Push-to-Card Private](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USjZw8DMjyWKmbDnMDNYtsY5", "bc313e15-e7e5-4315-a4e5-c58d83912f9d"))

```
```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```java

```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USjZw8DMjyWKmbDnMDNYtsY5`

- Password: `bc313e15-e7e5-4315-a4e5-c58d83912f9d`

- Application ID: `APq4WU6mhrReZSHq94MjJmoM`

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

```python


from finix.resources import Identity

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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PollosHermanos.com", 
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
  "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-13T20:48:55.82Z",
  "updated_at" : "2016-11-13T20:48:55.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import BankAccount

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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	    "identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PI9TLT598vBecd8dzySDceZw",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:03.14Z",
  "updated_at" : "2016-11-13T20:49:03.14Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDgpfa9VLoPgh4D8yzB5kzuK")
merchant = identity.provision_merchant_on(Merchant())
```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDgpfa9VLoPgh4D8yzB5kzuK');

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
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : "VI7G2sQbfwYyc8zqm55bu29V",
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.68Z",
  "updated_at" : "2016-11-13T20:49:04.68Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7G2sQbfwYyc8zqm55bu29V"
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
```python


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
	}).save()

```
```shell

curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "first_name"=> "Ricardo", 
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
  "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "entity" : {
    "title" : null,
    "first_name" : "Ricardo",
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
  "created_at" : "2016-11-13T20:49:05.97Z",
  "updated_at" : "2016-11-13T20:49:05.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Joe Sterling", 
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
	    "identity"=> "IDgCjoBRVAA3YZ5fpbeACugt"
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
  "id" : "PIeytuYczoH8APKsg1FYPkXG",
  "fingerprint" : "FPR-199645992",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Sterling",
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
  "created_at" : "2016-11-13T20:49:06.55Z",
  "updated_at" : "2016-11-13T20:49:06.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/updates"
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
```python


from finix.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeytuYczoH8APKsg1FYPkXG", 
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
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.56Z",
  "updated_at" : "2016-11-13T20:49:12.57Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU8tj9kxdVHg7w5zKmjFUzSz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU8tj9kxdVHg7w5zKmjFUzSz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8tj9kxdVHg7w5zKmjFUzSz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR3kDCWLQhwuohQxzdsPe8N4",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.42Z",
  "updated_at" : "2016-11-13T20:49:13.39Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
          applicationId: 'APq4WU6mhrReZSHq94MjJmoM',
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
  "id" : "TKdBb5JNp2qukUGvMD5m4dbg",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T20:49:14.97Z",
  "updated_at" : "2016-11-13T20:49:14.97Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T20:49:14.97Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    }
  }
}
```

### Step 4: Associate the Token
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PIdBb5JNp2qukUGvMD5m4dbg",
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
  "created_at" : "2016-11-13T20:49:15.56Z",
  "updated_at" : "2016-11-13T20:49:15.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/updates"
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
```python



```
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID3TzemceWBfHjXxRNX9sUjT",
  "entity" : {
    "title" : null,
    "first_name" : "Ricardo",
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
  "created_at" : "2016-11-13T20:49:22.85Z",
  "updated_at" : "2016-11-13T20:49:22.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "name": "Marshall Curry", 
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
	    "identity": "ID3TzemceWBfHjXxRNX9sUjT"
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USjZw8DMjyWKmbDnMDNYtsY5", 
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
  "id" : "PIahyqdxHXUGZzm4mXKYsZru",
  "fingerprint" : "FPR-473844280",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marshall Curry",
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
  "created_at" : "2016-11-13T20:49:23.46Z",
  "updated_at" : "2016-11-13T20:49:23.46Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3TzemceWBfHjXxRNX9sUjT",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/updates"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MUhhLU2fwCBc1Stn2SRB4ATM",
  "identity" : "ID3TzemceWBfHjXxRNX9sUjT",
  "verification" : "VIb36Wy4stxM5dDHnzukw2KY",
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:25.95Z",
  "updated_at" : "2016-11-13T20:49:25.95Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUhhLU2fwCBc1Stn2SRB4ATM"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUhhLU2fwCBc1Stn2SRB4ATM/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIb36Wy4stxM5dDHnzukw2KY"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Nmae of Processor


### Step 4: Send Payout

Once you have tokenized the payment card as above you can send funds to it at any time by simply calling the API


```python



```
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID3TzemceWBfHjXxRNX9sUjT", 
	    "destination": "PIahyqdxHXUGZzm4mXKYsZru", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USjZw8DMjyWKmbDnMDNYtsY5", 
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
  "id" : "TRsPGJTrFrc2JRYJNs6xvKmn",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "89805",
  "currency" : "USD",
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "source" : "PI4D1KrkT4vM9bf1rH2riibR",
  "destination" : "PIahyqdxHXUGZzm4mXKYsZru",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:24.48Z",
  "updated_at" : "2016-11-13T20:49:25.40Z",
  "merchant_identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru"
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


## Getting Started
### Step 1: Create an Identity for a Merchant

```python


from finix.resources import Identity

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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PollosHermanos.com", 
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
  "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-13T20:48:55.82Z",
  "updated_at" : "2016-11-13T20:48:55.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import BankAccount

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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	    "identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PI9TLT598vBecd8dzySDceZw",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:03.14Z",
  "updated_at" : "2016-11-13T20:49:03.14Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDgpfa9VLoPgh4D8yzB5kzuK")
merchant = identity.provision_merchant_on(Merchant())
```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDgpfa9VLoPgh4D8yzB5kzuK');

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
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : "VI7G2sQbfwYyc8zqm55bu29V",
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.68Z",
  "updated_at" : "2016-11-13T20:49:04.68Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7G2sQbfwYyc8zqm55bu29V"
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
```python


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
	}).save()

```
```shell

curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "first_name"=> "Ricardo", 
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
  "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "entity" : {
    "title" : null,
    "first_name" : "Ricardo",
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
  "created_at" : "2016-11-13T20:49:05.97Z",
  "updated_at" : "2016-11-13T20:49:05.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Joe Sterling", 
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
	    "identity"=> "IDgCjoBRVAA3YZ5fpbeACugt"
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
  "id" : "PIeytuYczoH8APKsg1FYPkXG",
  "fingerprint" : "FPR-199645992",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Sterling",
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
  "created_at" : "2016-11-13T20:49:06.55Z",
  "updated_at" : "2016-11-13T20:49:06.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/updates"
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
```python


from finix.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeytuYczoH8APKsg1FYPkXG", 
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
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.56Z",
  "updated_at" : "2016-11-13T20:49:12.57Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU8tj9kxdVHg7w5zKmjFUzSz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU8tj9kxdVHg7w5zKmjFUzSz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8tj9kxdVHg7w5zKmjFUzSz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR3kDCWLQhwuohQxzdsPe8N4",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.42Z",
  "updated_at" : "2016-11-13T20:49:13.39Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python



```
```shell
curl https://api-staging.finix.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "role": "ROLE_PARTNER"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USjZw8DMjyWKmbDnMDNYtsY5",
  "password" : "bc313e15-e7e5-4315-a4e5-c58d83912f9d",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T20:48:52.08Z",
  "updated_at" : "2016-11-13T20:48:52.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjZw8DMjyWKmbDnMDNYtsY5"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "USjZw8DMjyWKmbDnMDNYtsY5", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USjZw8DMjyWKmbDnMDNYtsY5", 
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
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T20:48:52.54Z",
  "updated_at" : "2016-11-13T20:48:52.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PRgVoiiVpkLquLqTWwWamJNt",
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "default_merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "created_at" : "2016-11-13T20:48:53.10Z",
  "updated_at" : "2016-11-13T20:48:53.10Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors/PRgVoiiVpkLquLqTWwWamJNt"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    }
  }
}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The Finix Payment Platform is processor agnostic allowing for processing transactions
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T20:48:52.48Z",
  "updated_at" : "2016-11-13T20:49:38.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T20:48:52.48Z",
  "updated_at" : "2016-11-13T20:49:39.02Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to Finix.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/2hxnjL0q/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Finix API.
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
    applicationId: "APq4WU6mhrReZSHq94MjJmoM",
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
server | *string*, **required** |  The base url for the Finix API
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
  "id" : "TKdBb5JNp2qukUGvMD5m4dbg",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T20:49:14.97Z",
  "updated_at" : "2016-11-13T20:49:14.97Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T20:49:14.97Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PIdBb5JNp2qukUGvMD5m4dbg",
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
  "created_at" : "2016-11-13T20:49:15.56Z",
  "updated_at" : "2016-11-13T20:49:15.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/updates"
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
## [ADMIN] Create a New Application

## Fetch an Application
```python


from finix.resources import Application

application = Application.get(id="APq4WU6mhrReZSHq94MjJmoM")
```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = Application::retrieve('APq4WU6mhrReZSHq94MjJmoM');

```
```java

```
> Example Response:

```json
{
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T20:48:52.48Z",
  "updated_at" : "2016-11-13T20:48:54.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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


```python


from finix.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "USjZw8DMjyWKmbDnMDNYtsY5", 
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
	}).save()
```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "USjZw8DMjyWKmbDnMDNYtsY5", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USjZw8DMjyWKmbDnMDNYtsY5", 
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
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T20:48:52.54Z",
  "updated_at" : "2016-11-13T20:48:52.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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
## Disable Processing Functionality
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T20:48:52.48Z",
  "updated_at" : "2016-11-13T20:49:35.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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
## Disable Settlement Functionality
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APq4WU6mhrReZSHq94MjJmoM",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T20:48:52.48Z",
  "updated_at" : "2016-11-13T20:49:36.47Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USe5p1RoUSSCjheRgwzUVXz7",
  "password" : "f3988c56-d24d-4b50-8bfa-2b98c5aeef57",
  "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T20:48:53.74Z",
  "updated_at" : "2016-11-13T20:48:53.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USe5p1RoUSSCjheRgwzUVXz7"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PRgVoiiVpkLquLqTWwWamJNt",
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "default_merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "created_at" : "2016-11-13T20:48:53.10Z",
  "updated_at" : "2016-11-13T20:48:53.10Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors/PRgVoiiVpkLquLqTWwWamJNt"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Application

application = Application.get()
```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APq4WU6mhrReZSHq94MjJmoM",
      "enabled" : true,
      "tags" : {
        "application_name" : "Facebook"
      },
      "owner" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-11-13T20:48:52.48Z",
      "updated_at" : "2016-11-13T20:48:54.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/tokens"
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


```python


from finix.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "merchant_identity": "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeytuYczoH8APKsg1FYPkXG", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeytuYczoH8APKsg1FYPkXG", 
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
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.56Z",
  "updated_at" : "2016-11-13T20:49:12.57Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU8tj9kxdVHg7w5zKmjFUzSz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU8tj9kxdVHg7w5zKmjFUzSz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8tj9kxdVHg7w5zKmjFUzSz");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR3kDCWLQhwuohQxzdsPe8N4",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.42Z",
  "updated_at" : "2016-11-13T20:49:13.39Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU8tj9kxdVHg7w5zKmjFUzSz")
authorization.void()

```
```shell

curl https://api-staging.finix.io/authorizations/AU8sNQLgDbJtXAybepc7kU7G \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AU8sNQLgDbJtXAybepc7kU7G",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:16.40Z",
  "updated_at" : "2016-11-13T20:49:17.20Z",
  "trace_id" : "74d797f9-ec67-461a-a402-922428608d9f",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : true,
  "expires_at" : "2016-11-20T20:49:16.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8sNQLgDbJtXAybepc7kU7G"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU8tj9kxdVHg7w5zKmjFUzSz")
```
```shell

curl https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU8tj9kxdVHg7w5zKmjFUzSz');

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8tj9kxdVHg7w5zKmjFUzSz");

```
> Example Response:

```json
{
  "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR3kDCWLQhwuohQxzdsPe8N4",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:12.42Z",
  "updated_at" : "2016-11-13T20:49:13.39Z",
  "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:12.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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
```python


from finix.resources import Authorization

authorization = Authorization.get()
```
```shell
curl https://api-staging.finix.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "AU8sNQLgDbJtXAybepc7kU7G",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:16.40Z",
      "updated_at" : "2016-11-13T20:49:17.20Z",
      "trace_id" : "74d797f9-ec67-461a-a402-922428608d9f",
      "source" : "PIeytuYczoH8APKsg1FYPkXG",
      "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "is_void" : true,
      "expires_at" : "2016-11-20T20:49:16.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU8sNQLgDbJtXAybepc7kU7G"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        }
      }
    }, {
      "id" : "AU8tj9kxdVHg7w5zKmjFUzSz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR3kDCWLQhwuohQxzdsPe8N4",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:12.42Z",
      "updated_at" : "2016-11-13T20:49:13.39Z",
      "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
      "source" : "PIeytuYczoH8APKsg1FYPkXG",
      "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "is_void" : false,
      "expires_at" : "2016-11-20T20:49:12.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU8tj9kxdVHg7w5zKmjFUzSz"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
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


```python


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
	}).save()
```
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "first_name"=> "Ricardo", 
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
  "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "entity" : {
    "title" : null,
    "first_name" : "Ricardo",
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
  "created_at" : "2016-11-13T20:49:05.97Z",
  "updated_at" : "2016-11-13T20:49:05.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Identity

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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PollosHermanos.com", 
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
  "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-13T20:48:55.82Z",
  "updated_at" : "2016-11-13T20:48:55.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Identity
identity = Identity.get(id="IDgpfa9VLoPgh4D8yzB5kzuK")

```
```shell

curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDgpfa9VLoPgh4D8yzB5kzuK');
```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDgpfa9VLoPgh4D8yzB5kzuK");

```
> Example Response:

```json
{
  "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-13T20:48:55.77Z",
  "updated_at" : "2016-11-13T20:48:55.77Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Fran", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Fran",
    "last_name" : "Lopez",
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
  "created_at" : "2016-11-13T20:48:55.77Z",
  "updated_at" : "2016-11-13T20:49:33.04Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Identity
identity = Identity.get()

```
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "ID3TzemceWBfHjXxRNX9sUjT",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:22.79Z",
      "updated_at" : "2016-11-13T20:49:22.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:05.91Z",
      "updated_at" : "2016-11-13T20:49:05.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "ID5JzZKheJB1uqrHhomjfvKy",
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
      "created_at" : "2016-11-13T20:49:01.96Z",
      "updated_at" : "2016-11-13T20:49:01.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDe6Gnjqv3cCNVcs4nS8javG",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:49:00.50Z",
      "updated_at" : "2016-11-13T20:49:00.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDi32zFnexnxjCqf8T4zbL7A",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:48:59.94Z",
      "updated_at" : "2016-11-13T20:48:59.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDjvZhoG68wySR2wzapMKcqQ",
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
      "created_at" : "2016-11-13T20:48:59.33Z",
      "updated_at" : "2016-11-13T20:48:59.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDcCVnWdWFDaonV2BFs4wbTK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.75Z",
      "updated_at" : "2016-11-13T20:48:58.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDiShQNi5t7iF1Rt9XsCFUgL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.20Z",
      "updated_at" : "2016-11-13T20:48:58.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDrU8eXeQc6HeH494zVM6q1B",
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
      "created_at" : "2016-11-13T20:48:57.61Z",
      "updated_at" : "2016-11-13T20:48:57.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDBRbdwS4BW61eMMTrzXChk",
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
      "created_at" : "2016-11-13T20:48:56.96Z",
      "updated_at" : "2016-11-13T20:48:56.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnxEgtawq9u9Hyvsuc8wjh4",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T20:48:56.42Z",
      "updated_at" : "2016-11-13T20:48:56.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-13T20:48:55.77Z",
      "updated_at" : "2016-11-13T20:48:55.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnf3YjRTNRw8HSkM3wvY5cR",
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
      "created_at" : "2016-11-13T20:48:52.48Z",
      "updated_at" : "2016-11-13T20:48:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDgpfa9VLoPgh4D8yzB5kzuK")
merchant = identity.provision_merchant_on(Merchant())

```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDgpfa9VLoPgh4D8yzB5kzuK');

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
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : "VI7G2sQbfwYyc8zqm55bu29V",
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.68Z",
  "updated_at" : "2016-11-13T20:49:04.68Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7G2sQbfwYyc8zqm55bu29V"
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
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MU2tsH498affyrCBYh64AaWq")

```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MU2tsH498affyrCBYh64AaWq');

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU2tsH498affyrCBYh64AaWq");

```
> Example Response:

```json
{
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : null,
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.57Z",
  "updated_at" : "2016-11-13T20:49:04.79Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VImPQskzwN9Jp9qDoT1z7CXX",
  "external_trace_id" : "8b546fc0-1943-4232-9f57-22b40f85e483",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T20:49:34.04Z",
  "updated_at" : "2016-11-13T20:49:34.06Z",
  "payment_instrument" : null,
  "merchant" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImPQskzwN9Jp9qDoT1z7CXX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VImPQskzwN9Jp9qDoT1z7CXX",
  "external_trace_id" : "8b546fc0-1943-4232-9f57-22b40f85e483",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T20:49:34.04Z",
  "updated_at" : "2016-11-13T20:49:34.06Z",
  "payment_instrument" : null,
  "merchant" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImPQskzwN9Jp9qDoT1z7CXX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : null,
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.57Z",
  "updated_at" : "2016-11-13T20:49:34.57Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MU2tsH498affyrCBYh64AaWq",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "verification" : null,
  "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:04.57Z",
  "updated_at" : "2016-11-13T20:49:35.30Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Merchant
merchant = Merchant.get()

```
```shell
curl https://api-staging.finix.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "MUhhLU2fwCBc1Stn2SRB4ATM",
      "identity" : "ID3TzemceWBfHjXxRNX9sUjT",
      "verification" : null,
      "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-13T20:49:25.88Z",
      "updated_at" : "2016-11-13T20:49:25.88Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUhhLU2fwCBc1Stn2SRB4ATM"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUhhLU2fwCBc1Stn2SRB4ATM/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "MU2tsH498affyrCBYh64AaWq",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "verification" : null,
      "merchant_profile" : "MPhWiwBxYmkcckmnaTDsj4CK",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-13T20:49:04.57Z",
      "updated_at" : "2016-11-13T20:49:04.79Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPhWiwBxYmkcckmnaTDsj4CK"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "ID3TzemceWBfHjXxRNX9sUjT",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:22.79Z",
      "updated_at" : "2016-11-13T20:49:22.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:05.91Z",
      "updated_at" : "2016-11-13T20:49:05.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "ID5JzZKheJB1uqrHhomjfvKy",
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
      "created_at" : "2016-11-13T20:49:01.96Z",
      "updated_at" : "2016-11-13T20:49:01.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDe6Gnjqv3cCNVcs4nS8javG",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:49:00.50Z",
      "updated_at" : "2016-11-13T20:49:00.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDi32zFnexnxjCqf8T4zbL7A",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:48:59.94Z",
      "updated_at" : "2016-11-13T20:48:59.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDjvZhoG68wySR2wzapMKcqQ",
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
      "created_at" : "2016-11-13T20:48:59.33Z",
      "updated_at" : "2016-11-13T20:48:59.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDcCVnWdWFDaonV2BFs4wbTK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.75Z",
      "updated_at" : "2016-11-13T20:48:58.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDiShQNi5t7iF1Rt9XsCFUgL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.20Z",
      "updated_at" : "2016-11-13T20:48:58.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDrU8eXeQc6HeH494zVM6q1B",
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
      "created_at" : "2016-11-13T20:48:57.61Z",
      "updated_at" : "2016-11-13T20:48:57.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDBRbdwS4BW61eMMTrzXChk",
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
      "created_at" : "2016-11-13T20:48:56.96Z",
      "updated_at" : "2016-11-13T20:48:56.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnxEgtawq9u9Hyvsuc8wjh4",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T20:48:56.42Z",
      "updated_at" : "2016-11-13T20:48:56.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-13T20:48:55.77Z",
      "updated_at" : "2016-11-13T20:48:55.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnf3YjRTNRw8HSkM3wvY5cR",
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
      "created_at" : "2016-11-13T20:48:52.48Z",
      "updated_at" : "2016-11-13T20:48:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MU2tsH498affyrCBYh64AaWq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "ID3TzemceWBfHjXxRNX9sUjT",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:22.79Z",
      "updated_at" : "2016-11-13T20:49:22.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgCjoBRVAA3YZ5fpbeACugt",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-11-13T20:49:05.91Z",
      "updated_at" : "2016-11-13T20:49:05.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "ID5JzZKheJB1uqrHhomjfvKy",
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
      "created_at" : "2016-11-13T20:49:01.96Z",
      "updated_at" : "2016-11-13T20:49:01.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5JzZKheJB1uqrHhomjfvKy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDe6Gnjqv3cCNVcs4nS8javG",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:49:00.50Z",
      "updated_at" : "2016-11-13T20:49:00.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDe6Gnjqv3cCNVcs4nS8javG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDi32zFnexnxjCqf8T4zbL7A",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-11-13T20:48:59.94Z",
      "updated_at" : "2016-11-13T20:48:59.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi32zFnexnxjCqf8T4zbL7A/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDjvZhoG68wySR2wzapMKcqQ",
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
      "created_at" : "2016-11-13T20:48:59.33Z",
      "updated_at" : "2016-11-13T20:48:59.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjvZhoG68wySR2wzapMKcqQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDcCVnWdWFDaonV2BFs4wbTK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.75Z",
      "updated_at" : "2016-11-13T20:48:58.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcCVnWdWFDaonV2BFs4wbTK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDiShQNi5t7iF1Rt9XsCFUgL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-13T20:48:58.20Z",
      "updated_at" : "2016-11-13T20:48:58.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiShQNi5t7iF1Rt9XsCFUgL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDrU8eXeQc6HeH494zVM6q1B",
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
      "created_at" : "2016-11-13T20:48:57.61Z",
      "updated_at" : "2016-11-13T20:48:57.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrU8eXeQc6HeH494zVM6q1B/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDBRbdwS4BW61eMMTrzXChk",
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
      "created_at" : "2016-11-13T20:48:56.96Z",
      "updated_at" : "2016-11-13T20:48:56.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDBRbdwS4BW61eMMTrzXChk/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnxEgtawq9u9Hyvsuc8wjh4",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T20:48:56.42Z",
      "updated_at" : "2016-11-13T20:48:56.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnxEgtawq9u9Hyvsuc8wjh4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-13T20:48:55.77Z",
      "updated_at" : "2016-11-13T20:48:55.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "IDnf3YjRTNRw8HSkM3wvY5cR",
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
      "created_at" : "2016-11-13T20:48:52.48Z",
      "updated_at" : "2016-11-13T20:48:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USckAiFw2BnGrZQCsKfYgHHC",
  "password" : "b05fd725-9875-491d-a875-ea7bf7bbb3a6",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T20:49:09.44Z",
  "updated_at" : "2016-11-13T20:49:09.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USckAiFw2BnGrZQCsKfYgHHC"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
          applicationId: 'APq4WU6mhrReZSHq94MjJmoM',
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
  "id" : "TKdBb5JNp2qukUGvMD5m4dbg",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T20:49:14.97Z",
  "updated_at" : "2016-11-13T20:49:14.97Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T20:49:14.97Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    }
  }
}
```

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PIdBb5JNp2qukUGvMD5m4dbg",
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
  "created_at" : "2016-11-13T20:49:15.56Z",
  "updated_at" : "2016-11-13T20:49:15.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/updates"
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
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()
```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKdBb5JNp2qukUGvMD5m4dbg", 
	    "type": "TOKEN", 
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PIdBb5JNp2qukUGvMD5m4dbg",
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
  "created_at" : "2016-11-13T20:49:15.56Z",
  "updated_at" : "2016-11-13T20:49:15.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/updates"
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
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '
	{
	    "name": "Joe Sterling", 
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
	    "identity": "IDgCjoBRVAA3YZ5fpbeACugt"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Joe Sterling", 
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
	    "identity"=> "IDgCjoBRVAA3YZ5fpbeACugt"
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
  "id" : "PIeytuYczoH8APKsg1FYPkXG",
  "fingerprint" : "FPR-199645992",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Sterling",
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
  "created_at" : "2016-11-13T20:49:06.55Z",
  "updated_at" : "2016-11-13T20:49:06.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgCjoBRVAA3YZ5fpbeACugt",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/updates"
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
```python


from finix.resources import BankAccount

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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}).save()
```
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
	    "identity": "IDgpfa9VLoPgh4D8yzB5kzuK"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
	    "identity"=> "IDgpfa9VLoPgh4D8yzB5kzuK"
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
  "id" : "PI9TLT598vBecd8dzySDceZw",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:03.14Z",
  "updated_at" : "2016-11-13T20:49:03.14Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python



```
```shell


curl https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI9TLT598vBecd8dzySDceZw');

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI9TLT598vBecd8dzySDceZw")

```
> Example Response:

```json
{
  "id" : "PI9TLT598vBecd8dzySDceZw",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:03.05Z",
  "updated_at" : "2016-11-13T20:49:03.84Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PI9TLT598vBecd8dzySDceZw",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:03.05Z",
  "updated_at" : "2016-11-13T20:49:03.84Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "PIahyqdxHXUGZzm4mXKYsZru",
      "fingerprint" : "FPR-473844280",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marshall Curry",
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
      "created_at" : "2016-11-13T20:49:23.39Z",
      "updated_at" : "2016-11-13T20:49:23.39Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID3TzemceWBfHjXxRNX9sUjT",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3TzemceWBfHjXxRNX9sUjT"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru/updates"
        }
      }
    }, {
      "id" : "PIuBftESBcdWgMv3td9bue9p",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:21.50Z",
      "updated_at" : "2016-11-13T20:49:21.50Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuBftESBcdWgMv3td9bue9p"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuBftESBcdWgMv3td9bue9p/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuBftESBcdWgMv3td9bue9p/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuBftESBcdWgMv3td9bue9p/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIkSDvrGpNY5dHFKiD1MSwuT",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:21.50Z",
      "updated_at" : "2016-11-13T20:49:21.50Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkSDvrGpNY5dHFKiD1MSwuT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkSDvrGpNY5dHFKiD1MSwuT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkSDvrGpNY5dHFKiD1MSwuT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkSDvrGpNY5dHFKiD1MSwuT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PI4D1KrkT4vM9bf1rH2riibR",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:21.50Z",
      "updated_at" : "2016-11-13T20:49:21.50Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PI5YubNLuf29mRCqcTmEcwCh",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:21.50Z",
      "updated_at" : "2016-11-13T20:49:21.50Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5YubNLuf29mRCqcTmEcwCh"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5YubNLuf29mRCqcTmEcwCh/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5YubNLuf29mRCqcTmEcwCh/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5YubNLuf29mRCqcTmEcwCh/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIdBb5JNp2qukUGvMD5m4dbg",
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
      "created_at" : "2016-11-13T20:49:15.42Z",
      "updated_at" : "2016-11-13T20:49:15.42Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdBb5JNp2qukUGvMD5m4dbg/updates"
        }
      }
    }, {
      "id" : "PIwwrcubWwRAP93Mn62F1aH9",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T20:49:07.39Z",
      "updated_at" : "2016-11-13T20:49:07.39Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDgCjoBRVAA3YZ5fpbeACugt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwwrcubWwRAP93Mn62F1aH9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwwrcubWwRAP93Mn62F1aH9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwwrcubWwRAP93Mn62F1aH9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwwrcubWwRAP93Mn62F1aH9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIeytuYczoH8APKsg1FYPkXG",
      "fingerprint" : "FPR-199645992",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Joe Sterling",
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
      "created_at" : "2016-11-13T20:49:06.47Z",
      "updated_at" : "2016-11-13T20:49:12.57Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDgCjoBRVAA3YZ5fpbeACugt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgCjoBRVAA3YZ5fpbeACugt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG/updates"
        }
      }
    }, {
      "id" : "PIsjTNjeR8Y47Rj72W8mAgki",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:04.57Z",
      "updated_at" : "2016-11-13T20:49:04.57Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIcJoyA7e1GbKu1y6XoRFLKC",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:04.57Z",
      "updated_at" : "2016-11-13T20:49:04.57Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcJoyA7e1GbKu1y6XoRFLKC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcJoyA7e1GbKu1y6XoRFLKC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcJoyA7e1GbKu1y6XoRFLKC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcJoyA7e1GbKu1y6XoRFLKC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIcvWTCH2k7KmFBBeQyfmMXo",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:04.57Z",
      "updated_at" : "2016-11-13T20:49:04.57Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcvWTCH2k7KmFBBeQyfmMXo"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcvWTCH2k7KmFBBeQyfmMXo/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcvWTCH2k7KmFBBeQyfmMXo/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcvWTCH2k7KmFBBeQyfmMXo/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PI9TLT598vBecd8dzySDceZw",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T20:49:03.05Z",
      "updated_at" : "2016-11-13T20:49:03.84Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9TLT598vBecd8dzySDceZw/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PI6eU5iFyof848srtHxsyQXP",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:48:53.02Z",
      "updated_at" : "2016-11-13T20:48:53.02Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6eU5iFyof848srtHxsyQXP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6eU5iFyof848srtHxsyQXP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6eU5iFyof848srtHxsyQXP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6eU5iFyof848srtHxsyQXP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIoVcUKyhaE6bBeHN6jZNxcW",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:48:53.02Z",
      "updated_at" : "2016-11-13T20:48:53.02Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoVcUKyhaE6bBeHN6jZNxcW"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoVcUKyhaE6bBeHN6jZNxcW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoVcUKyhaE6bBeHN6jZNxcW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoVcUKyhaE6bBeHN6jZNxcW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PIq2AmwDMUu7fcW5NfLQconT",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:48:53.02Z",
      "updated_at" : "2016-11-13T20:48:53.02Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIq2AmwDMUu7fcW5NfLQconT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIq2AmwDMUu7fcW5NfLQconT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIq2AmwDMUu7fcW5NfLQconT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIq2AmwDMUu7fcW5NfLQconT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "PI9vN1VY9jtgKAkqgJUEXB2k",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:48:53.02Z",
      "updated_at" : "2016-11-13T20:48:53.02Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vN1VY9jtgKAkqgJUEXB2k"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vN1VY9jtgKAkqgJUEXB2k/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vN1VY9jtgKAkqgJUEXB2k/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vN1VY9jtgKAkqgJUEXB2k/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TR5Y2qFXddcPwemK5pCV19Xw")

```
```shell

curl https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TR5Y2qFXddcPwemK5pCV19Xw');



```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR5Y2qFXddcPwemK5pCV19Xw");

```
> Example Response:

```json
{
  "id" : "TR5Y2qFXddcPwemK5pCV19Xw",
  "amount" : 338901,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "f0d93d38-f92a-4874-b357-9105ea182484",
  "currency" : "USD",
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "source" : "PIeytuYczoH8APKsg1FYPkXG",
  "destination" : "PIsjTNjeR8Y47Rj72W8mAgki",
  "ready_to_settle_at" : null,
  "fee" : 33890,
  "statement_descriptor" : "FNX*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:08.56Z",
  "updated_at" : "2016-11-13T20:49:11.28Z",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki"
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
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TR5Y2qFXddcPwemK5pCV19Xw")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```shell

curl https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TR5Y2qFXddcPwemK5pCV19Xw');
$refund = $debit->reverse(50);
```
```java

import io.finix.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRuqZREoeJZGCkAiGZ3GHGG6",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "e63d635c-aef3-4186-b72b-f00b0c2e961d",
  "currency" : "USD",
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "source" : "PIsjTNjeR8Y47Rj72W8mAgki",
  "destination" : "PIeytuYczoH8APKsg1FYPkXG",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*POLLOS HERMANOS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:11.34Z",
  "updated_at" : "2016-11-13T20:49:11.43Z",
  "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRuqZREoeJZGCkAiGZ3GHGG6"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRuqZREoeJZGCkAiGZ3GHGG6/payment_instruments"
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
```python


from finix.resources import Transfer
transfer = Transfer.get()

```
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "TRsPGJTrFrc2JRYJNs6xvKmn",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "89805",
      "currency" : "USD",
      "application" : "APq4WU6mhrReZSHq94MjJmoM",
      "source" : "PI4D1KrkT4vM9bf1rH2riibR",
      "destination" : "PIahyqdxHXUGZzm4mXKYsZru",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:24.26Z",
      "updated_at" : "2016-11-13T20:49:25.40Z",
      "merchant_identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnf3YjRTNRw8HSkM3wvY5cR"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsPGJTrFrc2JRYJNs6xvKmn/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4D1KrkT4vM9bf1rH2riibR"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIahyqdxHXUGZzm4mXKYsZru"
        }
      }
    }, {
      "id" : "TR3kDCWLQhwuohQxzdsPe8N4",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "a15ae55b-16e0-4bb0-af14-616a7b3a2895",
      "currency" : "USD",
      "application" : "APq4WU6mhrReZSHq94MjJmoM",
      "source" : "PIeytuYczoH8APKsg1FYPkXG",
      "destination" : "PIsjTNjeR8Y47Rj72W8mAgki",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:13.16Z",
      "updated_at" : "2016-11-13T20:49:13.39Z",
      "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR3kDCWLQhwuohQxzdsPe8N4/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki"
        }
      }
    }, {
      "id" : "TRuqZREoeJZGCkAiGZ3GHGG6",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "b48c1ba0-3826-4241-8fd3-6a2185771f4e",
      "currency" : "USD",
      "application" : "APq4WU6mhrReZSHq94MjJmoM",
      "source" : "PIsjTNjeR8Y47Rj72W8mAgki",
      "destination" : "PIeytuYczoH8APKsg1FYPkXG",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:11.09Z",
      "updated_at" : "2016-11-13T20:49:11.43Z",
      "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuqZREoeJZGCkAiGZ3GHGG6"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuqZREoeJZGCkAiGZ3GHGG6/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
        }
      }
    }, {
      "id" : "TR5Y2qFXddcPwemK5pCV19Xw",
      "amount" : 338901,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "f0d93d38-f92a-4874-b357-9105ea182484",
      "currency" : "USD",
      "application" : "APq4WU6mhrReZSHq94MjJmoM",
      "source" : "PIeytuYczoH8APKsg1FYPkXG",
      "destination" : "PIsjTNjeR8Y47Rj72W8mAgki",
      "ready_to_settle_at" : null,
      "fee" : 33890,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:08.56Z",
      "updated_at" : "2016-11-13T20:49:11.28Z",
      "merchant_identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5Y2qFXddcPwemK5pCV19Xw/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeytuYczoH8APKsg1FYPkXG"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsjTNjeR8Y47Rj72W8mAgki"
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
authenticated requests against the Finix API. When making authenticated
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
curl https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USe5p1RoUSSCjheRgwzUVXz7",
  "password" : "f3988c56-d24d-4b50-8bfa-2b98c5aeef57",
  "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T20:48:53.74Z",
  "updated_at" : "2016-11-13T20:48:53.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USe5p1RoUSSCjheRgwzUVXz7"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python



```
```shell
curl https://api-staging.finix.io/identities/IDgpfa9VLoPgh4D8yzB5kzuK/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USckAiFw2BnGrZQCsKfYgHHC",
  "password" : "b05fd725-9875-491d-a875-ea7bf7bbb3a6",
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T20:49:09.44Z",
  "updated_at" : "2016-11-13T20:49:09.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USckAiFw2BnGrZQCsKfYgHHC"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import User
user = User.get(id="USjZw8DMjyWKmbDnMDNYtsY5")

```
```shell
curl https://api-staging.finix.io/users/TR5Y2qFXddcPwemK5pCV19Xw \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USjZw8DMjyWKmbDnMDNYtsY5",
  "password" : null,
  "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T20:48:52.07Z",
  "updated_at" : "2016-11-13T20:48:52.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjZw8DMjyWKmbDnMDNYtsY5"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python



```
```shell
curl https://api-staging.finix.io/users/USckAiFw2BnGrZQCsKfYgHHC \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USckAiFw2BnGrZQCsKfYgHHC",
  "password" : null,
  "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T20:49:09.35Z",
  "updated_at" : "2016-11-13T20:49:10.01Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USckAiFw2BnGrZQCsKfYgHHC"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
```python


from finix.resources import User
users = User.get()

```
```shell
curl https://api-staging.finix.io/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USckAiFw2BnGrZQCsKfYgHHC",
      "password" : null,
      "identity" : "IDgpfa9VLoPgh4D8yzB5kzuK",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-11-13T20:49:09.35Z",
      "updated_at" : "2016-11-13T20:49:10.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USckAiFw2BnGrZQCsKfYgHHC"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "USe5p1RoUSSCjheRgwzUVXz7",
      "password" : null,
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-13T20:48:53.67Z",
      "updated_at" : "2016-11-13T20:48:53.67Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USe5p1RoUSSCjheRgwzUVXz7"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
        }
      }
    }, {
      "id" : "USjZw8DMjyWKmbDnMDNYtsY5",
      "password" : null,
      "identity" : "IDnf3YjRTNRw8HSkM3wvY5cR",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-13T20:48:52.07Z",
      "updated_at" : "2016-11-13T20:48:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USjZw8DMjyWKmbDnMDNYtsY5"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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
automated notifications (i.e. events) on the Finix API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```python


from finix.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d \
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
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
  "id" : "WHuT6PFaNLwaKYEbkLeCp1DF",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "created_at" : "2016-11-13T20:48:55.40Z",
  "updated_at" : "2016-11-13T20:48:55.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHuT6PFaNLwaKYEbkLeCp1DF"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python


from finix.resources import Webhook
webhook = Webhook.get(id="WHuT6PFaNLwaKYEbkLeCp1DF")

```
```shell



curl https://api-staging.finix.io/webhooks/WHuT6PFaNLwaKYEbkLeCp1DF \
    -H "Content-Type: application/vnd.json+api" \
    -u USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHuT6PFaNLwaKYEbkLeCp1DF');



```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHuT6PFaNLwaKYEbkLeCp1DF");

```
> Example Response:

```json
{
  "id" : "WHuT6PFaNLwaKYEbkLeCp1DF",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APq4WU6mhrReZSHq94MjJmoM",
  "created_at" : "2016-11-13T20:48:55.40Z",
  "updated_at" : "2016-11-13T20:48:55.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHuT6PFaNLwaKYEbkLeCp1DF"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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

```python


from finix.resources import Webhook
webhooks = Webhook.get()

```
```shell
curl https://api-staging.finix.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjZw8DMjyWKmbDnMDNYtsY5:bc313e15-e7e5-4315-a4e5-c58d83912f9d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
      "id" : "WHuT6PFaNLwaKYEbkLeCp1DF",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APq4WU6mhrReZSHq94MjJmoM",
      "created_at" : "2016-11-13T20:48:55.40Z",
      "updated_at" : "2016-11-13T20:48:55.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHuT6PFaNLwaKYEbkLeCp1DF"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APq4WU6mhrReZSHq94MjJmoM"
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


```python


```
```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USjZw8DMjyWKmbDnMDNYtsY5', 'bc313e15-e7e5-4315-a4e5-c58d83912f9d');
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
