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

3. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 

4. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```php
<?php

// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("US4CoseCAaB5RjTYrnwfDrZa", "4ca5aef5-f077-4277-a785-00f2cab07c21"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US4CoseCAaB5RjTYrnwfDrZa`

- Password: `4ca5aef5-f077-4277-a785-00f2cab07c21`

- Application ID: `APsxAXQJUaNyWNSan25sZSHm`

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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
> Example Response:

```json
{
  "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
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
  "created_at" : "2016-11-29T20:33:46.82Z",
  "updated_at" : "2016-11-29T20:33:46.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
	    "identity"=> "IDv1UPzNTeqGw6KPRYrPtRTn"
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
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIaGytKBP4hZQtfoDdpjjwtC",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T20:33:58.07Z",
  "updated_at" : "2016-11-29T20:33:58.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDv1UPzNTeqGw6KPRYrPtRTn');

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

identity = Identity.get(id="IDv1UPzNTeqGw6KPRYrPtRTn")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "verification" : "VI41RFG81YqYoorHRBjSFUbs",
  "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T20:33:59.50Z",
  "updated_at" : "2016-11-29T20:33:59.50Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI41RFG81YqYoorHRBjSFUbs"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
	        "first_name"=> "Collen", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
	}).save()

```
> Example Response:

```json
{
  "id" : "ID94UsfETgEeBYwWezAxUYNm",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
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
  "created_at" : "2016-11-29T20:34:01.31Z",
  "updated_at" : "2016-11-29T20:34:01.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "name": "Marcie Jones", 
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
	    "identity": "ID94UsfETgEeBYwWezAxUYNm"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Marcie Jones", 
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
	    "identity"=> "ID94UsfETgEeBYwWezAxUYNm"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Jones", 
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
	    "identity": "ID94UsfETgEeBYwWezAxUYNm"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIwyq9ias8N5spMpY5i91ZDW",
  "fingerprint" : "FPR-1499426136",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Jones",
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
  "created_at" : "2016-11-29T20:34:01.84Z",
  "updated_at" : "2016-11-29T20:34:01.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID94UsfETgEeBYwWezAxUYNm",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/updates"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "merchant_identity": "IDv1UPzNTeqGw6KPRYrPtRTn", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIwyq9ias8N5spMpY5i91ZDW", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDv1UPzNTeqGw6KPRYrPtRTn", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIwyq9ias8N5spMpY5i91ZDW", 
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
	    "merchant_identity": "IDv1UPzNTeqGw6KPRYrPtRTn", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIwyq9ias8N5spMpY5i91ZDW", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUrFuUfVGVJMvUFR1EXziuS2",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T20:34:18.32Z",
  "updated_at" : "2016-11-29T20:34:18.50Z",
  "trace_id" : "c6a43e59-6dc5-4800-86b3-5cf9768954be",
  "source" : "PIwyq9ias8N5spMpY5i91ZDW",
  "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "is_void" : false,
  "expires_at" : "2016-12-06T20:34:18.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUrFuUfVGVJMvUFR1EXziuS2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
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
curl https://api-staging.finix.io/authorizations/AUrFuUfVGVJMvUFR1EXziuS2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUrFuUfVGVJMvUFR1EXziuS2");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUrFuUfVGVJMvUFR1EXziuS2');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUrFuUfVGVJMvUFR1EXziuS2")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUrFuUfVGVJMvUFR1EXziuS2",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRwPpYqDKR9JhkYYdqnbP4pb",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T20:34:18.17Z",
  "updated_at" : "2016-11-29T20:34:20.01Z",
  "trace_id" : "c6a43e59-6dc5-4800-86b3-5cf9768954be",
  "source" : "PIwyq9ias8N5spMpY5i91ZDW",
  "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "is_void" : false,
  "expires_at" : "2016-12-06T20:34:18.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUrFuUfVGVJMvUFR1EXziuS2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
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

## Push-to-Card
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ayisha", 
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
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDktyWMR9u1pe86aJ6wfKtDB",
  "entity" : {
    "title" : null,
    "first_name" : "Ayisha",
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
  "created_at" : "2016-11-29T20:34:31.41Z",
  "updated_at" : "2016-11-29T20:34:31.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "name": "Ayisha Kline", 
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
	    "identity": "IDktyWMR9u1pe86aJ6wfKtDB"
	}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US4CoseCAaB5RjTYrnwfDrZa", 
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
  "id" : "PI9vChtNjk2SZbdyrVWZUJWv",
  "fingerprint" : "FPR616367336",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ayisha Kline",
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
  "created_at" : "2016-11-29T20:34:33.16Z",
  "updated_at" : "2016-11-29T20:34:33.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDktyWMR9u1pe86aJ6wfKtDB",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/updates"
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
curl https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUdXxef9RhzBrunxA7XGihjL",
  "identity" : "IDktyWMR9u1pe86aJ6wfKtDB",
  "verification" : "VIxxvY7LpNPXdaNaT1qTJ9v",
  "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T20:34:32.16Z",
  "updated_at" : "2016-11-29T20:34:32.16Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUdXxef9RhzBrunxA7XGihjL"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUdXxef9RhzBrunxA7XGihjL/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIxxvY7LpNPXdaNaT1qTJ9v"
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
    -u US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDktyWMR9u1pe86aJ6wfKtDB", 
	    "destination": "PI9vChtNjk2SZbdyrVWZUJWv", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "US4CoseCAaB5RjTYrnwfDrZa", 
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
  "id" : "TRq2EdeCT1UxM36cDdsaCnav",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "178897",
  "currency" : "USD",
  "application" : "APsxAXQJUaNyWNSan25sZSHm",
  "source" : "PIpvSJz5jmaVraz1RbYwDSiz",
  "destination" : "PI9vChtNjk2SZbdyrVWZUJWv",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T20:34:34.30Z",
  "updated_at" : "2016-11-29T20:34:36.84Z",
  "merchant_identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv"
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


## Embedded Tokenization

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
          applicationId: 'APsxAXQJUaNyWNSan25sZSHm',
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
  "id" : "TKgTyETeC1GvsPnEkeD7Qnr",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-29T20:34:22.30Z",
  "updated_at" : "2016-11-29T20:34:22.30Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-30T20:34:22.30Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIgTyETeC1GvsPnEkeD7Qnr",
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
  "created_at" : "2016-11-29T20:34:22.83Z",
  "updated_at" : "2016-11-29T20:34:22.83Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/updates"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
	        "first_name"=> "Collen", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "ID94UsfETgEeBYwWezAxUYNm",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
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
  "created_at" : "2016-11-29T20:34:01.31Z",
  "updated_at" : "2016-11-29T20:34:01.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
> Example Response:

```json
{
  "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
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
  "created_at" : "2016-11-29T20:33:46.82Z",
  "updated_at" : "2016-11-29T20:33:46.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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

curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDv1UPzNTeqGw6KPRYrPtRTn");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDv1UPzNTeqGw6KPRYrPtRTn');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDv1UPzNTeqGw6KPRYrPtRTn")

```
> Example Response:

```json
{
  "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
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
  "created_at" : "2016-11-29T20:33:46.78Z",
  "updated_at" : "2016-11-29T20:33:46.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21


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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "IDktyWMR9u1pe86aJ6wfKtDB",
      "entity" : {
        "title" : null,
        "first_name" : "Ayisha",
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
      "created_at" : "2016-11-29T20:34:31.39Z",
      "updated_at" : "2016-11-29T20:34:31.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "ID94UsfETgEeBYwWezAxUYNm",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
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
      "created_at" : "2016-11-29T20:34:01.29Z",
      "updated_at" : "2016-11-29T20:34:01.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDxAyZ37HWX45qfSNKcbMZFA",
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
      "created_at" : "2016-11-29T20:33:57.37Z",
      "updated_at" : "2016-11-29T20:33:57.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDgWCUjMMMga9MZ6447MEjHP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-29T20:33:55.13Z",
      "updated_at" : "2016-11-29T20:33:55.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDhDLFmTFBQiJ6XC6xH7KDQQ",
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
      "created_at" : "2016-11-29T20:33:54.09Z",
      "updated_at" : "2016-11-29T20:33:54.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDptutBWRbh5fSKx9BFQ8iRk",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-29T20:33:53.39Z",
      "updated_at" : "2016-11-29T20:33:53.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDsXjRFvaawYpZ2skqBpfNPQ",
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
      "created_at" : "2016-11-29T20:33:52.62Z",
      "updated_at" : "2016-11-29T20:33:52.62Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDvd6rDMQTcQFYWeUeT4PSbB",
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
      "created_at" : "2016-11-29T20:33:52.05Z",
      "updated_at" : "2016-11-29T20:33:52.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDe1bJb15MuT6tt6d93YLsTc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-29T20:33:50.87Z",
      "updated_at" : "2016-11-29T20:33:50.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "ID9nCDTuyp8RZwzuY6DxA4Fn",
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
      "created_at" : "2016-11-29T20:33:50.08Z",
      "updated_at" : "2016-11-29T20:33:50.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDjWmaFD5NK6xHh9LfayyHL6",
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
      "created_at" : "2016-11-29T20:33:49.07Z",
      "updated_at" : "2016-11-29T20:33:49.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
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
      "created_at" : "2016-11-29T20:33:46.78Z",
      "updated_at" : "2016-11-29T20:33:46.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDrb4vj5NsNSJjPNbv2Fhej",
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
      "created_at" : "2016-11-29T20:33:40.01Z",
      "updated_at" : "2016-11-29T20:33:40.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Joe", 
	        "last_name": "Wade", 
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
	        "doing_business_as": "ACME Anchors", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "ACME Anchors", 
	        "url": "www.ACMEAnchors.com", 
	        "business_name": "ACME Anchors", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Joe",
    "last_name" : "Wade",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "ACME Anchors",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-29T20:33:46.78Z",
  "updated_at" : "2016-11-29T20:34:46.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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

curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDv1UPzNTeqGw6KPRYrPtRTn');

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

identity = Identity.get(id="IDv1UPzNTeqGw6KPRYrPtRTn")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "verification" : "VI41RFG81YqYoorHRBjSFUbs",
  "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T20:33:59.50Z",
  "updated_at" : "2016-11-29T20:33:59.50Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI41RFG81YqYoorHRBjSFUbs"
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
curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDv1UPzNTeqGw6KPRYrPtRTn');

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

identity = Identity.get(id="IDv1UPzNTeqGw6KPRYrPtRTn")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "verification" : "VI41RFG81YqYoorHRBjSFUbs",
  "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T20:33:59.50Z",
  "updated_at" : "2016-11-29T20:33:59.50Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI41RFG81YqYoorHRBjSFUbs"
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
curl https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUhRcsYeDZzz5AyJkRJ2743u");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUhRcsYeDZzz5AyJkRJ2743u');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUhRcsYeDZzz5AyJkRJ2743u")

```
> Example Response:

```json
{
  "id" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "verification" : null,
  "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-29T20:33:59.43Z",
  "updated_at" : "2016-11-29T20:33:59.79Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USiagGx4V3qBbPNUY3cwrotB",
  "password" : "27d130f6-7604-46d0-ad86-478b677fedb6",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-29T20:34:07.07Z",
  "updated_at" : "2016-11-29T20:34:07.07Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USiagGx4V3qBbPNUY3cwrotB"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIeWCJrPLbyNRZoE86XdGefG",
  "external_trace_id" : "b6969c18-43aa-4529-96eb-5f906fe635b1",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-29T20:34:47.53Z",
  "updated_at" : "2016-11-29T20:34:47.55Z",
  "trace_id" : "b6969c18-43aa-4529-96eb-5f906fe635b1",
  "payment_instrument" : null,
  "merchant" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIeWCJrPLbyNRZoE86XdGefG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
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
curl https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIeWCJrPLbyNRZoE86XdGefG",
  "external_trace_id" : "b6969c18-43aa-4529-96eb-5f906fe635b1",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-29T20:34:47.53Z",
  "updated_at" : "2016-11-29T20:34:47.55Z",
  "trace_id" : "b6969c18-43aa-4529-96eb-5f906fe635b1",
  "payment_instrument" : null,
  "merchant" : "MUhRcsYeDZzz5AyJkRJ2743u",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIeWCJrPLbyNRZoE86XdGefG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "MUdXxef9RhzBrunxA7XGihjL",
      "identity" : "IDktyWMR9u1pe86aJ6wfKtDB",
      "verification" : null,
      "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-29T20:34:32.07Z",
      "updated_at" : "2016-11-29T20:34:32.07Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUdXxef9RhzBrunxA7XGihjL"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUdXxef9RhzBrunxA7XGihjL/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "MUhRcsYeDZzz5AyJkRJ2743u",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "verification" : null,
      "merchant_profile" : "MPwPdENU2M4TwoMySQgabuR2",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-29T20:33:59.43Z",
      "updated_at" : "2016-11-29T20:33:59.79Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPwPdENU2M4TwoMySQgabuR2"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/merchants/MUhRcsYeDZzz5AyJkRJ2743u/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "IDktyWMR9u1pe86aJ6wfKtDB",
      "entity" : {
        "title" : null,
        "first_name" : "Ayisha",
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
      "created_at" : "2016-11-29T20:34:31.39Z",
      "updated_at" : "2016-11-29T20:34:31.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "ID94UsfETgEeBYwWezAxUYNm",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
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
      "created_at" : "2016-11-29T20:34:01.29Z",
      "updated_at" : "2016-11-29T20:34:01.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDxAyZ37HWX45qfSNKcbMZFA",
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
      "created_at" : "2016-11-29T20:33:57.37Z",
      "updated_at" : "2016-11-29T20:33:57.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxAyZ37HWX45qfSNKcbMZFA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDgWCUjMMMga9MZ6447MEjHP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-29T20:33:55.13Z",
      "updated_at" : "2016-11-29T20:33:55.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgWCUjMMMga9MZ6447MEjHP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDhDLFmTFBQiJ6XC6xH7KDQQ",
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
      "created_at" : "2016-11-29T20:33:54.09Z",
      "updated_at" : "2016-11-29T20:33:54.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhDLFmTFBQiJ6XC6xH7KDQQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDptutBWRbh5fSKx9BFQ8iRk",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-29T20:33:53.39Z",
      "updated_at" : "2016-11-29T20:33:53.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDptutBWRbh5fSKx9BFQ8iRk/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDsXjRFvaawYpZ2skqBpfNPQ",
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
      "created_at" : "2016-11-29T20:33:52.62Z",
      "updated_at" : "2016-11-29T20:33:52.62Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsXjRFvaawYpZ2skqBpfNPQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDvd6rDMQTcQFYWeUeT4PSbB",
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
      "created_at" : "2016-11-29T20:33:52.05Z",
      "updated_at" : "2016-11-29T20:33:52.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvd6rDMQTcQFYWeUeT4PSbB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDe1bJb15MuT6tt6d93YLsTc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-29T20:33:50.87Z",
      "updated_at" : "2016-11-29T20:33:50.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDe1bJb15MuT6tt6d93YLsTc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "ID9nCDTuyp8RZwzuY6DxA4Fn",
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
      "created_at" : "2016-11-29T20:33:50.08Z",
      "updated_at" : "2016-11-29T20:33:50.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9nCDTuyp8RZwzuY6DxA4Fn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDjWmaFD5NK6xHh9LfayyHL6",
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
      "created_at" : "2016-11-29T20:33:49.07Z",
      "updated_at" : "2016-11-29T20:33:49.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjWmaFD5NK6xHh9LfayyHL6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDv1UPzNTeqGw6KPRYrPtRTn",
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
      "created_at" : "2016-11-29T20:33:46.78Z",
      "updated_at" : "2016-11-29T20:33:46.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "IDrb4vj5NsNSJjPNbv2Fhej",
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
      "created_at" : "2016-11-29T20:33:40.01Z",
      "updated_at" : "2016-11-29T20:33:40.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "name": "Marcie Jones", 
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
	    "identity": "ID94UsfETgEeBYwWezAxUYNm"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Marcie Jones", 
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
	    "identity"=> "ID94UsfETgEeBYwWezAxUYNm"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Jones", 
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
	    "identity": "ID94UsfETgEeBYwWezAxUYNm"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIwyq9ias8N5spMpY5i91ZDW",
  "fingerprint" : "FPR-1499426136",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Jones",
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
  "created_at" : "2016-11-29T20:34:01.84Z",
  "updated_at" : "2016-11-29T20:34:01.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID94UsfETgEeBYwWezAxUYNm",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/updates"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
	    "identity"=> "IDv1UPzNTeqGw6KPRYrPtRTn"
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
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIaGytKBP4hZQtfoDdpjjwtC",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T20:33:58.07Z",
  "updated_at" : "2016-11-29T20:33:58.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
          applicationId: 'APsxAXQJUaNyWNSan25sZSHm',
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
  "id" : "TKgTyETeC1GvsPnEkeD7Qnr",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-29T20:34:22.30Z",
  "updated_at" : "2016-11-29T20:34:22.30Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-30T20:34:22.30Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIgTyETeC1GvsPnEkeD7Qnr",
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
  "created_at" : "2016-11-29T20:34:22.83Z",
  "updated_at" : "2016-11-29T20:34:22.83Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/updates"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
    -d '
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKgTyETeC1GvsPnEkeD7Qnr", 
	    "type": "TOKEN", 
	    "identity": "IDv1UPzNTeqGw6KPRYrPtRTn"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIgTyETeC1GvsPnEkeD7Qnr",
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
  "created_at" : "2016-11-29T20:34:22.83Z",
  "updated_at" : "2016-11-29T20:34:22.83Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/updates"
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


curl https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIaGytKBP4hZQtfoDdpjjwtC")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIaGytKBP4hZQtfoDdpjjwtC');

```
```python



```
> Example Response:

```json
{
  "id" : "PIaGytKBP4hZQtfoDdpjjwtC",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T20:33:58.01Z",
  "updated_at" : "2016-11-29T20:33:58.73Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
curl https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PIaGytKBP4hZQtfoDdpjjwtC",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T20:33:58.01Z",
  "updated_at" : "2016-11-29T20:33:58.73Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "PI9vChtNjk2SZbdyrVWZUJWv",
      "fingerprint" : "FPR616367336",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Ayisha Kline",
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
      "created_at" : "2016-11-29T20:34:33.09Z",
      "updated_at" : "2016-11-29T20:34:33.09Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDktyWMR9u1pe86aJ6wfKtDB",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDktyWMR9u1pe86aJ6wfKtDB"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv/updates"
        }
      }
    }, {
      "id" : "PIpvSJz5jmaVraz1RbYwDSiz",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:34:30.08Z",
      "updated_at" : "2016-11-29T20:34:30.08Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIgnMH8rEUVKPnqC5XDU9R8L",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:34:30.08Z",
      "updated_at" : "2016-11-29T20:34:30.08Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnMH8rEUVKPnqC5XDU9R8L"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnMH8rEUVKPnqC5XDU9R8L/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnMH8rEUVKPnqC5XDU9R8L/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnMH8rEUVKPnqC5XDU9R8L/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIhTAcHTfwMvovqbmmkbuT1h",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:34:30.08Z",
      "updated_at" : "2016-11-29T20:34:30.08Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhTAcHTfwMvovqbmmkbuT1h"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhTAcHTfwMvovqbmmkbuT1h/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhTAcHTfwMvovqbmmkbuT1h/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhTAcHTfwMvovqbmmkbuT1h/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIbiHmDz1ZLHg7SKK68LNMqe",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:34:30.08Z",
      "updated_at" : "2016-11-29T20:34:30.08Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbiHmDz1ZLHg7SKK68LNMqe"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbiHmDz1ZLHg7SKK68LNMqe/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbiHmDz1ZLHg7SKK68LNMqe/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbiHmDz1ZLHg7SKK68LNMqe/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIgTyETeC1GvsPnEkeD7Qnr",
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
      "created_at" : "2016-11-29T20:34:22.76Z",
      "updated_at" : "2016-11-29T20:34:22.76Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgTyETeC1GvsPnEkeD7Qnr/updates"
        }
      }
    }, {
      "id" : "PI5C6Gkgvoy4GpX57c7cgRmn",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-29T20:34:02.62Z",
      "updated_at" : "2016-11-29T20:34:02.62Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID94UsfETgEeBYwWezAxUYNm",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5C6Gkgvoy4GpX57c7cgRmn"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5C6Gkgvoy4GpX57c7cgRmn/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5C6Gkgvoy4GpX57c7cgRmn/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5C6Gkgvoy4GpX57c7cgRmn/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIwyq9ias8N5spMpY5i91ZDW",
      "fingerprint" : "FPR-1499426136",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marcie Jones",
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
      "created_at" : "2016-11-29T20:34:01.77Z",
      "updated_at" : "2016-11-29T20:34:18.41Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID94UsfETgEeBYwWezAxUYNm",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID94UsfETgEeBYwWezAxUYNm"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW/updates"
        }
      }
    }, {
      "id" : "PIxtSTb6siniaxU4NeoZ3iGq",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:59.43Z",
      "updated_at" : "2016-11-29T20:33:59.43Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIt25uBqYiudh1AkuApUByMF",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:59.43Z",
      "updated_at" : "2016-11-29T20:33:59.43Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt25uBqYiudh1AkuApUByMF"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt25uBqYiudh1AkuApUByMF/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt25uBqYiudh1AkuApUByMF/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt25uBqYiudh1AkuApUByMF/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIcS5qBGAADBmctZMaU6XZSK",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:59.43Z",
      "updated_at" : "2016-11-29T20:33:59.43Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcS5qBGAADBmctZMaU6XZSK"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcS5qBGAADBmctZMaU6XZSK/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcS5qBGAADBmctZMaU6XZSK/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcS5qBGAADBmctZMaU6XZSK/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIaGytKBP4hZQtfoDdpjjwtC",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-29T20:33:58.01Z",
      "updated_at" : "2016-11-29T20:33:58.73Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaGytKBP4hZQtfoDdpjjwtC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PInzMLH5Czp3Kq6fKAQ7ZDLi",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:41.34Z",
      "updated_at" : "2016-11-29T20:33:41.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInzMLH5Czp3Kq6fKAQ7ZDLi"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInzMLH5Czp3Kq6fKAQ7ZDLi/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInzMLH5Czp3Kq6fKAQ7ZDLi/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInzMLH5Czp3Kq6fKAQ7ZDLi/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIek4Ejv9VdsPYS5ETi6cNpv",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:41.34Z",
      "updated_at" : "2016-11-29T20:33:41.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIek4Ejv9VdsPYS5ETi6cNpv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIek4Ejv9VdsPYS5ETi6cNpv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIek4Ejv9VdsPYS5ETi6cNpv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIek4Ejv9VdsPYS5ETi6cNpv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PI6KTMXUbVh4FBVsNshCnLuu",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:41.34Z",
      "updated_at" : "2016-11-29T20:33:41.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KTMXUbVh4FBVsNshCnLuu"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KTMXUbVh4FBVsNshCnLuu/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KTMXUbVh4FBVsNshCnLuu/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KTMXUbVh4FBVsNshCnLuu/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        }
      }
    }, {
      "id" : "PIu6U9AZTZo9wfJjWrZMub9M",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T20:33:41.34Z",
      "updated_at" : "2016-11-29T20:33:41.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6U9AZTZo9wfJjWrZMub9M"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6U9AZTZo9wfJjWrZMub9M/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6U9AZTZo9wfJjWrZMub9M/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu6U9AZTZo9wfJjWrZMub9M/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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

curl https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRiWbmNagP9kaFMsv9fdHByb");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRiWbmNagP9kaFMsv9fdHByb');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRiWbmNagP9kaFMsv9fdHByb")

```
> Example Response:

```json
{
  "id" : "TRiWbmNagP9kaFMsv9fdHByb",
  "amount" : 148414,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "1776ba35-323a-44f2-b053-f986cbdb1b85",
  "currency" : "USD",
  "application" : "APsxAXQJUaNyWNSan25sZSHm",
  "source" : "PIwyq9ias8N5spMpY5i91ZDW",
  "destination" : "PIxtSTb6siniaxU4NeoZ3iGq",
  "ready_to_settle_at" : null,
  "fee" : 14841,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T20:34:03.55Z",
  "updated_at" : "2016-11-29T20:34:12.98Z",
  "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq"
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

curl https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRiWbmNagP9kaFMsv9fdHByb');
$refund = $debit->reverse(50);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRiWbmNagP9kaFMsv9fdHByb")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRxkynDdccqmgRNKdWbkmEhH",
  "amount" : 148414,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "fdc66178-2e10-4197-b13b-5dfb108db531",
  "currency" : "USD",
  "application" : "APsxAXQJUaNyWNSan25sZSHm",
  "source" : "PIxtSTb6siniaxU4NeoZ3iGq",
  "destination" : "PIwyq9ias8N5spMpY5i91ZDW",
  "ready_to_settle_at" : null,
  "fee" : 14841,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T20:34:13.49Z",
  "updated_at" : "2016-11-29T20:34:14.00Z",
  "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRxkynDdccqmgRNKdWbkmEhH"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRxkynDdccqmgRNKdWbkmEhH/payment_instruments"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "TRq2EdeCT1UxM36cDdsaCnav",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "178897",
      "currency" : "USD",
      "application" : "APsxAXQJUaNyWNSan25sZSHm",
      "source" : "PIpvSJz5jmaVraz1RbYwDSiz",
      "destination" : "PI9vChtNjk2SZbdyrVWZUJWv",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T20:34:34.00Z",
      "updated_at" : "2016-11-29T20:34:36.84Z",
      "merchant_identity" : "IDrb4vj5NsNSJjPNbv2Fhej",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDrb4vj5NsNSJjPNbv2Fhej"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRq2EdeCT1UxM36cDdsaCnav/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpvSJz5jmaVraz1RbYwDSiz"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9vChtNjk2SZbdyrVWZUJWv"
        }
      }
    }, {
      "id" : "TRwPpYqDKR9JhkYYdqnbP4pb",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "c6a43e59-6dc5-4800-86b3-5cf9768954be",
      "currency" : "USD",
      "application" : "APsxAXQJUaNyWNSan25sZSHm",
      "source" : "PIwyq9ias8N5spMpY5i91ZDW",
      "destination" : "PIxtSTb6siniaxU4NeoZ3iGq",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T20:34:19.34Z",
      "updated_at" : "2016-11-29T20:34:20.01Z",
      "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRwPpYqDKR9JhkYYdqnbP4pb/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq"
        }
      }
    }, {
      "id" : "TRxkynDdccqmgRNKdWbkmEhH",
      "amount" : 148414,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "f154795a-e18d-4c85-a353-65a1096a82cc",
      "currency" : "USD",
      "application" : "APsxAXQJUaNyWNSan25sZSHm",
      "source" : "PIxtSTb6siniaxU4NeoZ3iGq",
      "destination" : "PIwyq9ias8N5spMpY5i91ZDW",
      "ready_to_settle_at" : null,
      "fee" : 14841,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T20:34:12.71Z",
      "updated_at" : "2016-11-29T20:34:14.00Z",
      "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxkynDdccqmgRNKdWbkmEhH"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxkynDdccqmgRNKdWbkmEhH/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
        }
      }
    }, {
      "id" : "TRiWbmNagP9kaFMsv9fdHByb",
      "amount" : 148414,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "1776ba35-323a-44f2-b053-f986cbdb1b85",
      "currency" : "USD",
      "application" : "APsxAXQJUaNyWNSan25sZSHm",
      "source" : "PIwyq9ias8N5spMpY5i91ZDW",
      "destination" : "PIxtSTb6siniaxU4NeoZ3iGq",
      "ready_to_settle_at" : null,
      "fee" : 14841,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T20:34:03.55Z",
      "updated_at" : "2016-11-29T20:34:12.98Z",
      "merchant_identity" : "IDv1UPzNTeqGw6KPRYrPtRTn",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv1UPzNTeqGw6KPRYrPtRTn"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRiWbmNagP9kaFMsv9fdHByb/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwyq9ias8N5spMpY5i91ZDW"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxtSTb6siniaxU4NeoZ3iGq"
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
    -u US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21 \
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
  "id" : "WHn4tC3H4igy6Yig1vBeQjDv",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APsxAXQJUaNyWNSan25sZSHm",
  "created_at" : "2016-11-29T20:33:46.24Z",
  "updated_at" : "2016-11-29T20:33:46.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHn4tC3H4igy6Yig1vBeQjDv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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



curl https://api-staging.finix.io/webhooks/WHn4tC3H4igy6Yig1vBeQjDv \
    -H "Content-Type: application/vnd.json+api" \
    -u US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHn4tC3H4igy6Yig1vBeQjDv");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHn4tC3H4igy6Yig1vBeQjDv');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHn4tC3H4igy6Yig1vBeQjDv")

```
> Example Response:

```json
{
  "id" : "WHn4tC3H4igy6Yig1vBeQjDv",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APsxAXQJUaNyWNSan25sZSHm",
  "created_at" : "2016-11-29T20:33:46.26Z",
  "updated_at" : "2016-11-29T20:33:46.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHn4tC3H4igy6Yig1vBeQjDv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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
    -u  US4CoseCAaB5RjTYrnwfDrZa:4ca5aef5-f077-4277-a785-00f2cab07c21

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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
      "id" : "WHn4tC3H4igy6Yig1vBeQjDv",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APsxAXQJUaNyWNSan25sZSHm",
      "created_at" : "2016-11-29T20:33:46.26Z",
      "updated_at" : "2016-11-29T20:33:46.26Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHn4tC3H4igy6Yig1vBeQjDv"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APsxAXQJUaNyWNSan25sZSHm"
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US4CoseCAaB5RjTYrnwfDrZa',
	"password" => '4ca5aef5-f077-4277-a785-00f2cab07c21']
	);


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
