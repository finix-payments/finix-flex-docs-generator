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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);

require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USmE2fwTcEJpaeQefN5kKySk", "ec2d009a-f8da-4547-be43-917566e05162"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USmE2fwTcEJpaeQefN5kKySk`

- Password: `ec2d009a-f8da-4547-be43-917566e05162`

- Application ID: `APgoV5xQ927ZXcCAcgReVwpp`

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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	        "max_transaction_amount"=> 12000000, 
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
	        "max_transaction_amount": 12000000, 
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
  "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
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
    "max_transaction_amount" : 12000000,
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
  "created_at" : "2016-12-06T22:25:37.17Z",
  "updated_at" : "2016-12-06T22:25:37.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	    "identity"=> "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIpLfMCNjDzYFMHhEB3FgETR",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-12-06T22:25:42.77Z",
  "updated_at" : "2016-12-06T22:25:42.77Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDtHpzi9G6RfCgfSXE3JrVBA');

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

identity = Identity.get(id="IDtHpzi9G6RfCgfSXE3JrVBA")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "verification" : "VI7wgPgfY2BZoR7UYjEbXa97",
  "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-06T22:25:43.80Z",
  "updated_at" : "2016-12-06T22:25:43.80Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7wgPgfY2BZoR7UYjEbXa97"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marshall", 
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	        "first_name"=> "Marshall", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marshall", 
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
	}).save()

```
> Example Response:

```json
{
  "id" : "IDpMeBtXzSzKQT2nnUHufEz9",
  "entity" : {
    "title" : null,
    "first_name" : "Marshall",
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
  "created_at" : "2016-12-06T22:25:44.64Z",
  "updated_at" : "2016-12-06T22:25:44.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "name": "Joe Jones", 
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
	    "identity": "IDpMeBtXzSzKQT2nnUHufEz9"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Joe Jones", 
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
	    "identity"=> "IDpMeBtXzSzKQT2nnUHufEz9"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Jones", 
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
	    "identity": "IDpMeBtXzSzKQT2nnUHufEz9"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIec5tus61YKdxa8HibczNkk",
  "fingerprint" : "FPR417417416",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Jones",
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
  "created_at" : "2016-12-06T22:25:45.38Z",
  "updated_at" : "2016-12-06T22:25:45.38Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpMeBtXzSzKQT2nnUHufEz9",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/updates"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "merchant_identity": "IDtHpzi9G6RfCgfSXE3JrVBA", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIec5tus61YKdxa8HibczNkk", 
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDtHpzi9G6RfCgfSXE3JrVBA", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIec5tus61YKdxa8HibczNkk", 
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
	    "merchant_identity": "IDtHpzi9G6RfCgfSXE3JrVBA", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIec5tus61YKdxa8HibczNkk", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUivThfn3H96UVxwrrSmmpgi",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-06T22:25:49.31Z",
  "updated_at" : "2016-12-06T22:25:49.35Z",
  "trace_id" : "704aa6b6-d55f-41b8-8f3c-551000459129",
  "source" : "PIec5tus61YKdxa8HibczNkk",
  "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "is_void" : false,
  "expires_at" : "2016-12-13T22:25:49.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUivThfn3H96UVxwrrSmmpgi"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
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
curl https://api-staging.finix.io/authorizations/AUivThfn3H96UVxwrrSmmpgi \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUivThfn3H96UVxwrrSmmpgi");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUivThfn3H96UVxwrrSmmpgi');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUivThfn3H96UVxwrrSmmpgi")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUivThfn3H96UVxwrrSmmpgi",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRnVqmjZGv9mBE6gikLs94iT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-06T22:25:49.26Z",
  "updated_at" : "2016-12-06T22:25:49.88Z",
  "trace_id" : "704aa6b6-d55f-41b8-8f3c-551000459129",
  "source" : "PIec5tus61YKdxa8HibczNkk",
  "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "is_void" : false,
  "expires_at" : "2016-12-13T22:25:49.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUivThfn3H96UVxwrrSmmpgi"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
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
    -u USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ricardo", 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDbYez7g4pFhnn7JT9BbRufK",
  "entity" : {
    "title" : null,
    "first_name" : "Ricardo",
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
  "created_at" : "2016-12-06T22:25:57.13Z",
  "updated_at" : "2016-12-06T22:25:57.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "name": "Daphne James", 
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
	    "identity": "IDbYez7g4pFhnn7JT9BbRufK"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USmE2fwTcEJpaeQefN5kKySk", 
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
	        "max_transaction_amount"=> 1200000, 
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
```python



```
> Example Response:

```json
{
  "id" : "PI81cjN3HEk8nsmzfBGhK9oQ",
  "fingerprint" : "FPR-762566296",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Daphne James",
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
  "created_at" : "2016-12-06T22:25:58.65Z",
  "updated_at" : "2016-12-06T22:25:58.65Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/updates"
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
curl https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUqoTh8SrMcskR8QVR1HYmGc",
  "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
  "verification" : "VIdTYvuu35CBpxZLHux2nNWm",
  "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-06T22:25:57.50Z",
  "updated_at" : "2016-12-06T22:25:57.50Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUqoTh8SrMcskR8QVR1HYmGc"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUqoTh8SrMcskR8QVR1HYmGc/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIdTYvuu35CBpxZLHux2nNWm"
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
    -u USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDbYez7g4pFhnn7JT9BbRufK", 
	    "destination": "PI81cjN3HEk8nsmzfBGhK9oQ", 
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USmE2fwTcEJpaeQefN5kKySk", 
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
	        "max_transaction_amount"=> 1200000, 
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
```python



```
> Example Response:

```json
{
  "id" : "TRdXpmaGSMFTFxmtf69YGrNT",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "183031",
  "currency" : "USD",
  "application" : "APgoV5xQ927ZXcCAcgReVwpp",
  "source" : "PI9xi5dMbTzUudMyDn5UWbqr",
  "destination" : "PI81cjN3HEk8nsmzfBGhK9oQ",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-06T22:25:59.34Z",
  "updated_at" : "2016-12-06T22:26:00.78Z",
  "merchant_identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ"
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
          applicationId: 'APgoV5xQ927ZXcCAcgReVwpp',
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
  "id" : "TKmBH6EE9FGPsBU4mob77A4X",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-06T22:25:51.13Z",
  "updated_at" : "2016-12-06T22:25:51.13Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-07T22:25:51.13Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	}).save()

```
> Example Response:

```json
{
  "id" : "PImBH6EE9FGPsBU4mob77A4X",
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
  "created_at" : "2016-12-06T22:25:51.84Z",
  "updated_at" : "2016-12-06T22:25:51.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/updates"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marshall", 
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	        "first_name"=> "Marshall", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marshall", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "IDpMeBtXzSzKQT2nnUHufEz9",
  "entity" : {
    "title" : null,
    "first_name" : "Marshall",
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
  "created_at" : "2016-12-06T22:25:44.64Z",
  "updated_at" : "2016-12-06T22:25:44.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	        "max_transaction_amount"=> 12000000, 
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
	        "max_transaction_amount": 12000000, 
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
  "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
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
    "max_transaction_amount" : 12000000,
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
  "created_at" : "2016-12-06T22:25:37.17Z",
  "updated_at" : "2016-12-06T22:25:37.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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

curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDtHpzi9G6RfCgfSXE3JrVBA");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDtHpzi9G6RfCgfSXE3JrVBA');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDtHpzi9G6RfCgfSXE3JrVBA")

```
> Example Response:

```json
{
  "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
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
    "max_transaction_amount" : 12000000,
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
  "created_at" : "2016-12-06T22:25:37.14Z",
  "updated_at" : "2016-12-06T22:25:37.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162


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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identities= Identity::getPagination("/identities");


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
      "id" : "IDbYez7g4pFhnn7JT9BbRufK",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-12-06T22:25:57.11Z",
      "updated_at" : "2016-12-06T22:25:57.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDpMeBtXzSzKQT2nnUHufEz9",
      "entity" : {
        "title" : null,
        "first_name" : "Marshall",
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
      "created_at" : "2016-12-06T22:25:44.61Z",
      "updated_at" : "2016-12-06T22:25:44.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDiJ6QPKbbYpdiZ2xBWgSo87",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:42.23Z",
      "updated_at" : "2016-12-06T22:25:42.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDiD2KwdavYozHYdjbwCgMJT",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:41.75Z",
      "updated_at" : "2016-12-06T22:25:41.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDojkR9P7qUiK2TeBcg4Kxuw",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:41.24Z",
      "updated_at" : "2016-12-06T22:25:41.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDfd2rhbTAaRZGbc6EenAV2J",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:40.56Z",
      "updated_at" : "2016-12-06T22:25:40.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDw5wqAAnJ4vfEQdcLZXKF8z",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:40.17Z",
      "updated_at" : "2016-12-06T22:25:40.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDeSvYVwrWd7sXefBXGr4xCt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:39.49Z",
      "updated_at" : "2016-12-06T22:25:39.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDh7chRaUtW7hgc3vusBaA61",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:38.93Z",
      "updated_at" : "2016-12-06T22:25:38.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDkK7qJg6bTLwsgWURqtUqtP",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:38.16Z",
      "updated_at" : "2016-12-06T22:25:38.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDd6qJcDKj2U5mqymerMLm7m",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:37.68Z",
      "updated_at" : "2016-12-06T22:25:37.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:37.14Z",
      "updated_at" : "2016-12-06T22:25:37.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDxjz6HSyj6iuT4zev78ZZpt",
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
        "max_transaction_amount" : 1200000,
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
      "created_at" : "2016-12-06T22:25:34.28Z",
      "updated_at" : "2016-12-06T22:25:34.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Alex", 
	        "last_name": "Sterling", 
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
	        "max_transaction_amount": 1200000, 
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
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Alex",
    "last_name" : "Sterling",
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
    "max_transaction_amount" : 1200000,
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
  "created_at" : "2016-12-06T22:25:37.14Z",
  "updated_at" : "2016-12-06T22:26:06.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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

curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDtHpzi9G6RfCgfSXE3JrVBA');

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

identity = Identity.get(id="IDtHpzi9G6RfCgfSXE3JrVBA")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "verification" : "VI7wgPgfY2BZoR7UYjEbXa97",
  "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-06T22:25:43.80Z",
  "updated_at" : "2016-12-06T22:25:43.80Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7wgPgfY2BZoR7UYjEbXa97"
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
curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDtHpzi9G6RfCgfSXE3JrVBA');

$merchant = $identity->provisionMerchantOn(new Merchant(["processor" => "DUMMY_V1"]));




    
```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDtHpzi9G6RfCgfSXE3JrVBA")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "verification" : "VI7wgPgfY2BZoR7UYjEbXa97",
  "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-06T22:25:43.80Z",
  "updated_at" : "2016-12-06T22:25:43.80Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI7wgPgfY2BZoR7UYjEbXa97"
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
curl https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUw5bbBiD6HWGqXDV4EUbJ3w");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUw5bbBiD6HWGqXDV4EUbJ3w');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUw5bbBiD6HWGqXDV4EUbJ3w")

```
> Example Response:

```json
{
  "id" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "verification" : null,
  "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-12-06T22:25:43.76Z",
  "updated_at" : "2016-12-06T22:25:43.89Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "UScQH9zCSo8dBPm1DHWRbgab",
  "password" : "6d423d2c-4e12-40dc-85b2-fadd78c83d1b",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-12-06T22:25:46.94Z",
  "updated_at" : "2016-12-06T22:25:46.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UScQH9zCSo8dBPm1DHWRbgab"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIjAxEa4x19SpD4LTgAN7JPq",
  "external_trace_id" : "84b1aa27-b4c8-458c-a7f4-55673b5f4775",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-06T22:26:07.41Z",
  "updated_at" : "2016-12-06T22:26:07.43Z",
  "trace_id" : "84b1aa27-b4c8-458c-a7f4-55673b5f4775",
  "payment_instrument" : null,
  "merchant" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIjAxEa4x19SpD4LTgAN7JPq"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
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
curl https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIjAxEa4x19SpD4LTgAN7JPq",
  "external_trace_id" : "84b1aa27-b4c8-458c-a7f4-55673b5f4775",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-06T22:26:07.41Z",
  "updated_at" : "2016-12-06T22:26:07.43Z",
  "trace_id" : "84b1aa27-b4c8-458c-a7f4-55673b5f4775",
  "payment_instrument" : null,
  "merchant" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIjAxEa4x19SpD4LTgAN7JPq"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchants = Merchant::getPagination("/merchants");


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
      "id" : "MUqoTh8SrMcskR8QVR1HYmGc",
      "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
      "verification" : null,
      "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-12-06T22:25:57.47Z",
      "updated_at" : "2016-12-06T22:25:57.47Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUqoTh8SrMcskR8QVR1HYmGc"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUqoTh8SrMcskR8QVR1HYmGc/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "MUw5bbBiD6HWGqXDV4EUbJ3w",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "verification" : null,
      "merchant_profile" : "MPhYzDK7dCRLyRqTmAS1jRdX",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-12-06T22:25:43.76Z",
      "updated_at" : "2016-12-06T22:25:43.89Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPhYzDK7dCRLyRqTmAS1jRdX"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/merchants/MUw5bbBiD6HWGqXDV4EUbJ3w/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
      "id" : "IDbYez7g4pFhnn7JT9BbRufK",
      "entity" : {
        "title" : null,
        "first_name" : "Ricardo",
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
      "created_at" : "2016-12-06T22:25:57.11Z",
      "updated_at" : "2016-12-06T22:25:57.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDpMeBtXzSzKQT2nnUHufEz9",
      "entity" : {
        "title" : null,
        "first_name" : "Marshall",
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
      "created_at" : "2016-12-06T22:25:44.61Z",
      "updated_at" : "2016-12-06T22:25:44.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDiJ6QPKbbYpdiZ2xBWgSo87",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:42.23Z",
      "updated_at" : "2016-12-06T22:25:42.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiJ6QPKbbYpdiZ2xBWgSo87/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDiD2KwdavYozHYdjbwCgMJT",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:41.75Z",
      "updated_at" : "2016-12-06T22:25:41.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiD2KwdavYozHYdjbwCgMJT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDojkR9P7qUiK2TeBcg4Kxuw",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:41.24Z",
      "updated_at" : "2016-12-06T22:25:41.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDojkR9P7qUiK2TeBcg4Kxuw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDfd2rhbTAaRZGbc6EenAV2J",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:40.56Z",
      "updated_at" : "2016-12-06T22:25:40.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfd2rhbTAaRZGbc6EenAV2J/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDw5wqAAnJ4vfEQdcLZXKF8z",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:40.17Z",
      "updated_at" : "2016-12-06T22:25:40.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw5wqAAnJ4vfEQdcLZXKF8z/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDeSvYVwrWd7sXefBXGr4xCt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:39.49Z",
      "updated_at" : "2016-12-06T22:25:39.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeSvYVwrWd7sXefBXGr4xCt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDh7chRaUtW7hgc3vusBaA61",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:38.93Z",
      "updated_at" : "2016-12-06T22:25:38.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDh7chRaUtW7hgc3vusBaA61/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDkK7qJg6bTLwsgWURqtUqtP",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:38.16Z",
      "updated_at" : "2016-12-06T22:25:38.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkK7qJg6bTLwsgWURqtUqtP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDd6qJcDKj2U5mqymerMLm7m",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:37.68Z",
      "updated_at" : "2016-12-06T22:25:37.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd6qJcDKj2U5mqymerMLm7m/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDtHpzi9G6RfCgfSXE3JrVBA",
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
        "max_transaction_amount" : 12000000,
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
      "created_at" : "2016-12-06T22:25:37.14Z",
      "updated_at" : "2016-12-06T22:25:37.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "IDxjz6HSyj6iuT4zev78ZZpt",
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
        "max_transaction_amount" : 1200000,
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
      "created_at" : "2016-12-06T22:25:34.28Z",
      "updated_at" : "2016-12-06T22:25:34.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "name": "Joe Jones", 
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
	    "identity": "IDpMeBtXzSzKQT2nnUHufEz9"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Joe Jones", 
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
	    "identity"=> "IDpMeBtXzSzKQT2nnUHufEz9"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Jones", 
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
	    "identity": "IDpMeBtXzSzKQT2nnUHufEz9"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIec5tus61YKdxa8HibczNkk",
  "fingerprint" : "FPR417417416",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Jones",
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
  "created_at" : "2016-12-06T22:25:45.38Z",
  "updated_at" : "2016-12-06T22:25:45.38Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpMeBtXzSzKQT2nnUHufEz9",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/updates"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
	    "identity"=> "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIpLfMCNjDzYFMHhEB3FgETR",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-12-06T22:25:42.77Z",
  "updated_at" : "2016-12-06T22:25:42.77Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
          applicationId: 'APgoV5xQ927ZXcCAcgReVwpp',
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
  "id" : "TKmBH6EE9FGPsBU4mob77A4X",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-06T22:25:51.13Z",
  "updated_at" : "2016-12-06T22:25:51.13Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-07T22:25:51.13Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PImBH6EE9FGPsBU4mob77A4X",
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
  "created_at" : "2016-12-06T22:25:51.84Z",
  "updated_at" : "2016-12-06T22:25:51.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/updates"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
    -d '
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDtHpzi9G6RfCgfSXE3JrVBA"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKmBH6EE9FGPsBU4mob77A4X", 
	    "type": "TOKEN", 
	    "identity": "IDtHpzi9G6RfCgfSXE3JrVBA"
	}).save()
```
> Example Response:

```json
{
  "id" : "PImBH6EE9FGPsBU4mob77A4X",
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
  "created_at" : "2016-12-06T22:25:51.84Z",
  "updated_at" : "2016-12-06T22:25:51.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/updates"
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


curl https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIpLfMCNjDzYFMHhEB3FgETR")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIpLfMCNjDzYFMHhEB3FgETR');

```
```python



```
> Example Response:

```json
{
  "id" : "PIpLfMCNjDzYFMHhEB3FgETR",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-12-06T22:25:42.73Z",
  "updated_at" : "2016-12-06T22:25:43.29Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
curl https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PIpLfMCNjDzYFMHhEB3FgETR",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-12-06T22:25:42.73Z",
  "updated_at" : "2016-12-06T22:25:43.29Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI4xYdJYmoVNuBNLGQCbxZi3",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:26:04.37Z",
      "updated_at" : "2016-12-06T22:26:04.37Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xYdJYmoVNuBNLGQCbxZi3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xYdJYmoVNuBNLGQCbxZi3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xYdJYmoVNuBNLGQCbxZi3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xYdJYmoVNuBNLGQCbxZi3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PI5w4YwcfNrggiXDscGGNiyZ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:26:04.37Z",
      "updated_at" : "2016-12-06T22:26:04.37Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5w4YwcfNrggiXDscGGNiyZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5w4YwcfNrggiXDscGGNiyZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5w4YwcfNrggiXDscGGNiyZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5w4YwcfNrggiXDscGGNiyZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PI6swNV9YZDM4AjHZYukBeXM",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:26:04.37Z",
      "updated_at" : "2016-12-06T22:26:04.37Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6swNV9YZDM4AjHZYukBeXM"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6swNV9YZDM4AjHZYukBeXM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6swNV9YZDM4AjHZYukBeXM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6swNV9YZDM4AjHZYukBeXM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PI81cjN3HEk8nsmzfBGhK9oQ",
      "fingerprint" : "FPR-762566296",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Daphne James",
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
      "created_at" : "2016-12-06T22:25:58.61Z",
      "updated_at" : "2016-12-06T22:25:58.61Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDbYez7g4pFhnn7JT9BbRufK",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbYez7g4pFhnn7JT9BbRufK"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ/updates"
        }
      }
    }, {
      "id" : "PI9xi5dMbTzUudMyDn5UWbqr",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:56.26Z",
      "updated_at" : "2016-12-06T22:25:56.26Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIfnLSUJVua9qtH2Fa9ugnL",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:56.26Z",
      "updated_at" : "2016-12-06T22:25:56.26Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfnLSUJVua9qtH2Fa9ugnL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfnLSUJVua9qtH2Fa9ugnL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfnLSUJVua9qtH2Fa9ugnL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfnLSUJVua9qtH2Fa9ugnL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIqKKCGGWGDYDj1g83MLnHFH",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:56.26Z",
      "updated_at" : "2016-12-06T22:25:56.26Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqKKCGGWGDYDj1g83MLnHFH"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqKKCGGWGDYDj1g83MLnHFH/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqKKCGGWGDYDj1g83MLnHFH/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqKKCGGWGDYDj1g83MLnHFH/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PI84pYxQGhA25eEU3NXVyVWy",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:56.26Z",
      "updated_at" : "2016-12-06T22:25:56.26Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84pYxQGhA25eEU3NXVyVWy"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84pYxQGhA25eEU3NXVyVWy/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84pYxQGhA25eEU3NXVyVWy/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84pYxQGhA25eEU3NXVyVWy/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PImBH6EE9FGPsBU4mob77A4X",
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
      "created_at" : "2016-12-06T22:25:51.79Z",
      "updated_at" : "2016-12-06T22:25:51.79Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImBH6EE9FGPsBU4mob77A4X/updates"
        }
      }
    }, {
      "id" : "PIrFRPeYuHkiUUDvnUKFkwff",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-12-06T22:25:45.83Z",
      "updated_at" : "2016-12-06T22:25:45.83Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDpMeBtXzSzKQT2nnUHufEz9",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrFRPeYuHkiUUDvnUKFkwff"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrFRPeYuHkiUUDvnUKFkwff/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrFRPeYuHkiUUDvnUKFkwff/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrFRPeYuHkiUUDvnUKFkwff/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIec5tus61YKdxa8HibczNkk",
      "fingerprint" : "FPR417417416",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Joe Jones",
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
      "created_at" : "2016-12-06T22:25:45.34Z",
      "updated_at" : "2016-12-06T22:25:49.33Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDpMeBtXzSzKQT2nnUHufEz9",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpMeBtXzSzKQT2nnUHufEz9"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk/updates"
        }
      }
    }, {
      "id" : "PI9D7J7VWJoAorWpBwswc6X4",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:43.76Z",
      "updated_at" : "2016-12-06T22:25:43.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9D7J7VWJoAorWpBwswc6X4"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9D7J7VWJoAorWpBwswc6X4/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9D7J7VWJoAorWpBwswc6X4/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9D7J7VWJoAorWpBwswc6X4/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIrsoHtFnkRHsQMtC1tE2mLQ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:43.76Z",
      "updated_at" : "2016-12-06T22:25:43.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrsoHtFnkRHsQMtC1tE2mLQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrsoHtFnkRHsQMtC1tE2mLQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrsoHtFnkRHsQMtC1tE2mLQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrsoHtFnkRHsQMtC1tE2mLQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PI6QoBxcfTR8PCwMsvvEQyxX",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:43.76Z",
      "updated_at" : "2016-12-06T22:25:43.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIpLfMCNjDzYFMHhEB3FgETR",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-12-06T22:25:42.73Z",
      "updated_at" : "2016-12-06T22:25:43.29Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpLfMCNjDzYFMHhEB3FgETR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIeeYLvsmsNYW85PZK7AugRa",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:34.73Z",
      "updated_at" : "2016-12-06T22:25:34.73Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeeYLvsmsNYW85PZK7AugRa"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeeYLvsmsNYW85PZK7AugRa/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeeYLvsmsNYW85PZK7AugRa/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeeYLvsmsNYW85PZK7AugRa/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIpRwmwejac4dL36PnLYBWdH",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:34.73Z",
      "updated_at" : "2016-12-06T22:25:34.73Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpRwmwejac4dL36PnLYBWdH"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpRwmwejac4dL36PnLYBWdH/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpRwmwejac4dL36PnLYBWdH/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpRwmwejac4dL36PnLYBWdH/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIwi1wELdbbwAqrWVDErcT9U",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:34.73Z",
      "updated_at" : "2016-12-06T22:25:34.73Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi1wELdbbwAqrWVDErcT9U"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi1wELdbbwAqrWVDErcT9U/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi1wELdbbwAqrWVDErcT9U/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi1wELdbbwAqrWVDErcT9U/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        }
      }
    }, {
      "id" : "PIqXKKAKuiJjMCAzHR1i77UE",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-06T22:25:34.73Z",
      "updated_at" : "2016-12-06T22:25:34.73Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqXKKAKuiJjMCAzHR1i77UE"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqXKKAKuiJjMCAzHR1i77UE/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqXKKAKuiJjMCAzHR1i77UE/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqXKKAKuiJjMCAzHR1i77UE/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    "count" : 19
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

- **CANCELED:** Created, and then reversed before transfer has transitioned to succeeded

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRtnnFtjz7Kg8HWgXJPzgbp");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRtnnFtjz7Kg8HWgXJPzgbp');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRtnnFtjz7Kg8HWgXJPzgbp")

```
> Example Response:

```json
{
  "id" : "TRtnnFtjz7Kg8HWgXJPzgbp",
  "amount" : 179524,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "e9715d9c-d7aa-4ca4-899d-9cb37e0ac6de",
  "currency" : "USD",
  "application" : "APgoV5xQ927ZXcCAcgReVwpp",
  "source" : "PIec5tus61YKdxa8HibczNkk",
  "destination" : "PI6QoBxcfTR8PCwMsvvEQyxX",
  "ready_to_settle_at" : null,
  "fee" : 17952,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-06T22:25:46.29Z",
  "updated_at" : "2016-12-06T22:25:48.35Z",
  "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX"
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

curl https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRtnnFtjz7Kg8HWgXJPzgbp');
$refund = $debit->reverse(11);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRtnnFtjz7Kg8HWgXJPzgbp")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TR7WhbhYmuCY8TaWqADx8JXq",
  "amount" : 179524,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "382af71a-d514-4cf4-b0b1-991fb2e4d51e",
  "currency" : "USD",
  "application" : "APgoV5xQ927ZXcCAcgReVwpp",
  "source" : "PI6QoBxcfTR8PCwMsvvEQyxX",
  "destination" : "PIec5tus61YKdxa8HibczNkk",
  "ready_to_settle_at" : null,
  "fee" : 17952,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-06T22:25:48.38Z",
  "updated_at" : "2016-12-06T22:25:48.44Z",
  "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR7WhbhYmuCY8TaWqADx8JXq"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR7WhbhYmuCY8TaWqADx8JXq/payment_instruments"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


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
      "id" : "TRdXpmaGSMFTFxmtf69YGrNT",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "183031",
      "currency" : "USD",
      "application" : "APgoV5xQ927ZXcCAcgReVwpp",
      "source" : "PI9xi5dMbTzUudMyDn5UWbqr",
      "destination" : "PI81cjN3HEk8nsmzfBGhK9oQ",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-06T22:25:59.18Z",
      "updated_at" : "2016-12-06T22:26:00.78Z",
      "merchant_identity" : "IDxjz6HSyj6iuT4zev78ZZpt",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxjz6HSyj6iuT4zev78ZZpt"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRdXpmaGSMFTFxmtf69YGrNT/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9xi5dMbTzUudMyDn5UWbqr"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI81cjN3HEk8nsmzfBGhK9oQ"
        }
      }
    }, {
      "id" : "TRnVqmjZGv9mBE6gikLs94iT",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "704aa6b6-d55f-41b8-8f3c-551000459129",
      "currency" : "USD",
      "application" : "APgoV5xQ927ZXcCAcgReVwpp",
      "source" : "PIec5tus61YKdxa8HibczNkk",
      "destination" : "PI6QoBxcfTR8PCwMsvvEQyxX",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-06T22:25:49.77Z",
      "updated_at" : "2016-12-06T22:25:49.88Z",
      "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRnVqmjZGv9mBE6gikLs94iT/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX"
        }
      }
    }, {
      "id" : "TR7WhbhYmuCY8TaWqADx8JXq",
      "amount" : 179524,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "2e8f09d6-e392-464e-ba8f-2da0b15b336b",
      "currency" : "USD",
      "application" : "APgoV5xQ927ZXcCAcgReVwpp",
      "source" : "PI6QoBxcfTR8PCwMsvvEQyxX",
      "destination" : "PIec5tus61YKdxa8HibczNkk",
      "ready_to_settle_at" : null,
      "fee" : 17952,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-06T22:25:48.27Z",
      "updated_at" : "2016-12-06T22:25:48.44Z",
      "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7WhbhYmuCY8TaWqADx8JXq"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7WhbhYmuCY8TaWqADx8JXq/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
        }
      }
    }, {
      "id" : "TRtnnFtjz7Kg8HWgXJPzgbp",
      "amount" : 179524,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "e9715d9c-d7aa-4ca4-899d-9cb37e0ac6de",
      "currency" : "USD",
      "application" : "APgoV5xQ927ZXcCAcgReVwpp",
      "source" : "PIec5tus61YKdxa8HibczNkk",
      "destination" : "PI6QoBxcfTR8PCwMsvvEQyxX",
      "ready_to_settle_at" : null,
      "fee" : 17952,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-06T22:25:46.29Z",
      "updated_at" : "2016-12-06T22:25:48.35Z",
      "merchant_identity" : "IDtHpzi9G6RfCgfSXE3JrVBA",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtHpzi9G6RfCgfSXE3JrVBA"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtnnFtjz7Kg8HWgXJPzgbp/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIec5tus61YKdxa8HibczNkk"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6QoBxcfTR8PCwMsvvEQyxX"
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
    -u USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162 \
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = new Webhook(array("url"=>"http://requestb.in/1jb5zu11"));
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
  "id" : "WHeWPfkWM3trJLCH2VxytUXG",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgoV5xQ927ZXcCAcgReVwpp",
  "created_at" : "2016-12-06T22:25:36.83Z",
  "updated_at" : "2016-12-06T22:25:36.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHeWPfkWM3trJLCH2VxytUXG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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



curl https://api-staging.finix.io/webhooks/WHeWPfkWM3trJLCH2VxytUXG \
    -H "Content-Type: application/vnd.json+api" \
    -u USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHeWPfkWM3trJLCH2VxytUXG");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHeWPfkWM3trJLCH2VxytUXG');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHeWPfkWM3trJLCH2VxytUXG")

```
> Example Response:

```json
{
  "id" : "WHeWPfkWM3trJLCH2VxytUXG",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgoV5xQ927ZXcCAcgReVwpp",
  "created_at" : "2016-12-06T22:25:36.82Z",
  "updated_at" : "2016-12-06T22:25:36.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHeWPfkWM3trJLCH2VxytUXG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
    -u  USmE2fwTcEJpaeQefN5kKySk:ec2d009a-f8da-4547-be43-917566e05162

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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
	);


require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


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
      "id" : "WHeWPfkWM3trJLCH2VxytUXG",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APgoV5xQ927ZXcCAcgReVwpp",
      "created_at" : "2016-12-06T22:25:36.82Z",
      "updated_at" : "2016-12-06T22:25:36.82Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHeWPfkWM3trJLCH2VxytUXG"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgoV5xQ927ZXcCAcgReVwpp"
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
	"username" => 'USmE2fwTcEJpaeQefN5kKySk',
	"password" => 'ec2d009a-f8da-4547-be43-917566e05162']
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
