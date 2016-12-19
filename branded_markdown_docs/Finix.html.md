---
title: Finix API Reference

language_tabs:
- shell: cURL
- java: Java
- php: PHP
- python: Python
- ruby: Ruby



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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');

Finix\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USgxidPLBeHb82t4LEoJcUkB',
	"password" => '3bd5be80-588c-42ca-8543-9c097e9844fb']
	);

require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USgxidPLBeHb82t4LEoJcUkB", "3bd5be80-588c-42ca-8543-9c097e9844fb"))

```
```ruby
# To download the Ruby gem:
# gem install finix

require 'finix'

Finix.configure(
    :root_url => 'https://api-staging.finix.io',
    :user=>'USgxidPLBeHb82t4LEoJcUkB',
    :password => '3bd5be80-588c-42ca-8543-9c097e9844fb'
)
```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USgxidPLBeHb82t4LEoJcUkB`

- Password: `3bd5be80-588c-42ca-8543-9c097e9844fb`

- Application ID: `APtQNQpPihoWYaUK26c2XyhY`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://api-staging.finix.io`

- **Production API:** `https://api.finix.io`

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
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


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Lees Sandwiches", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "incorporation_date"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "business_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
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
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.LeesSandwiches.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
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
    "max_transaction_amount" : 12000000,
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:24:27.32Z",
  "updated_at" : "2016-12-19T22:24:27.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
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
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}'


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
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\BankAccount;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$bank_account = new BankAccount(
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
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
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
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save()

```
```ruby
bank_account = Finix::BankAccount.new(
	{
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> {
	        "Bank Account"=> "Company Account"
	    }, 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save
```
> Example Response:

```json
{
  "id" : "PIrThBosxrALH9mZtgfoNBBd",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:24:32.66Z",
  "updated_at" : "2016-12-19T22:24:32.66Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "verification" : "VI3Q5Qm6isumtjbwdEbbaiif",
  "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:33.69Z",
  "updated_at" : "2016-12-19T22:24:33.69Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI3Q5Qm6isumtjbwdEbbaiif"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "Wade", 
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
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Wade", 
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
	));
$identity = $identity->save();

```
```python


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "Wade", 
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
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Wade", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }
	    }
	}).save

```
> Example Response:

```json
{
  "id" : "ID8MtWGeo3YG9S7AHfwvkBn2",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
    "last_name" : "Wade",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:24:34.40Z",
  "updated_at" : "2016-12-19T22:24:34.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "name": "Laura Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card_name": "Business Card"
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
	    "identity": "ID8MtWGeo3YG9S7AHfwvkBn2"
	}'


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
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card_name"=> "Business Card"
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
	    "identity"=> "ID8MtWGeo3YG9S7AHfwvkBn2"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card_name": "Business Card"
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
	    "identity": "ID8MtWGeo3YG9S7AHfwvkBn2"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Laura Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> {
	        "card_name"=> "Business Card"
	    }, 
	    "number"=> "4957030420210454", 
	    "expiration_month"=> 12, 
	    "address"=> {
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    }, 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "ID8MtWGeo3YG9S7AHfwvkBn2"
	}).save
```
> Example Response:

```json
{
  "id" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "fingerprint" : "FPR1264366140",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Lopez",
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
  "created_at" : "2016-12-19T22:24:34.81Z",
  "updated_at" : "2016-12-19T22:24:34.81Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID8MtWGeo3YG9S7AHfwvkBn2",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/updates"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "merchant_identity": "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

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
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```python


from finix.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUqM5jopmHyrXpXxBetSGVg6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:40.18Z",
  "updated_at" : "2016-12-19T22:24:40.22Z",
  "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:24:40.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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
curl https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUqM5jopmHyrXpXxBetSGVg6");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUqM5jopmHyrXpXxBetSGVg6');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUqM5jopmHyrXpXxBetSGVg6")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUqM5jopmHyrXpXxBetSGVg6")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUqM5jopmHyrXpXxBetSGVg6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahte6dDJodiWVhgr8okvZ",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:40.13Z",
  "updated_at" : "2016-12-19T22:24:40.74Z",
  "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:24:40.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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
curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$settlement = new Settlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));
$settlement = $identity->createSettlement($settlement);

```
```python


from finix.resources import Identity
from finix.resources import Settlement

identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")
settlement = identity.create_settlement(
	{
	    "currency"=> "USD", 
	    "tags"=> {
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    }
	})
```
> Example Response:

```json
{
  "id" : "STdGwzmTectPa65NjJYZiBcV",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "currency" : "USD",
  "created_at" : "2016-12-19T22:25:21.85Z",
  "updated_at" : "2016-12-19T22:25:21.86Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 685327,
  "total_fees" : 68534,
  "total_fee" : 68534,
  "net_amount" : 616793,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=debit"
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

## Push-to-Card
### Step 1: Create an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
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

```
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Bob", 
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
	));
$identity = $identity->save();

```
```python



```
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Bob", 
	        "last_name"=> "Green", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "ID53m75hc5JQkEPSGsiVsBMJ",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:24:47.93Z",
  "updated_at" : "2016-12-19T22:24:47.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "name": "Jessie Green", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card_name": "Business Card"
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
	    "identity": "ID53m75hc5JQkEPSGsiVsBMJ"
	}'
```
```java

```
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('ID53m75hc5JQkEPSGsiVsBMJ');
$card = new PaymentCard(
	array(
	    "name"=> "Jessie Green", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card_name"=> "Business Card"
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
	    "identity"=> "ID53m75hc5JQkEPSGsiVsBMJ"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Jessie Green", 
	    "expiration_year"=> 2020, 
	    "tags"=> {
	        "card_name"=> "Business Card"
	    }, 
	    "number"=> "4957030420210454", 
	    "expiration_month"=> 12, 
	    "address"=> {
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    }, 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "ID53m75hc5JQkEPSGsiVsBMJ"
	}).save
```
> Example Response:

```json
{
  "id" : "PI3RpJzGMeYWKxewwigBfmzE",
  "fingerprint" : "FPR1419155432",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Green",
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
  "created_at" : "2016-12-19T22:24:49.60Z",
  "updated_at" : "2016-12-19T22:24:49.60Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/updates"
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
curl https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('ID53m75hc5JQkEPSGsiVsBMJ');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"PI3RpJzGMeYWKxewwigBfmzE")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUj1s1nqLUBLJvudCJVFvpe1",
  "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
  "verification" : "VIbZHhjyG2yjF9vgfY1JSUeA",
  "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:48.43Z",
  "updated_at" : "2016-12-19T22:24:48.43Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUj1s1nqLUBLJvudCJVFvpe1"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUj1s1nqLUBLJvudCJVFvpe1/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIbZHhjyG2yjF9vgfY1JSUeA"
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
    -u USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID53m75hc5JQkEPSGsiVsBMJ", 
	    "destination": "PI3RpJzGMeYWKxewwigBfmzE", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```java

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "merchant_identity"=> "ID53m75hc5JQkEPSGsiVsBMJ", 
	    "destination"=> "PI3RpJzGMeYWKxewwigBfmzE", 
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "processor"=> "VISA_V1"
	));
$transfer = $transfer->save();
```
```python



```
```ruby
transfer = Finix::Transfer.new(
	{
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "merchant_identity"=> "ID53m75hc5JQkEPSGsiVsBMJ", 
	    "destination"=> "PI3RpJzGMeYWKxewwigBfmzE", 
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "processor"=> "VISA_V1"
	}).save
```
> Example Response:

```json
{
  "id" : "TR3SRPPxQiqgo7tTUo4Dv2LX",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "184732",
  "currency" : "USD",
  "application" : "APtQNQpPihoWYaUK26c2XyhY",
  "source" : "PIp8WyZcC6NL4mYZsbVoqXWy",
  "destination" : "PI3RpJzGMeYWKxewwigBfmzE",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:50.20Z",
  "updated_at" : "2016-12-19T22:24:51.53Z",
  "merchant_identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE"
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
          applicationId: 'APtQNQpPihoWYaUK26c2XyhY',
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
  "id" : "TK5hyKPo5VMBXaAF16N2Cstn",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-19T22:24:41.75Z",
  "updated_at" : "2016-12-19T22:24:41.75Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-20T22:24:41.75Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}'


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
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save
```
> Example Response:

```json
{
  "id" : "PI5hyKPo5VMBXaAF16N2Cstn",
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
  "created_at" : "2016-12-19T22:24:42.14Z",
  "updated_at" : "2016-12-19T22:24:42.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/updates"
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
    applicationId: "APtQNQpPihoWYaUK26c2XyhY",
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
  "id" : "TK5hyKPo5VMBXaAF16N2Cstn",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-19T22:24:41.75Z",
  "updated_at" : "2016-12-19T22:24:41.75Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-20T22:24:41.75Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}'

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
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save
```
> Example Response:

```json
{
  "id" : "PI5hyKPo5VMBXaAF16N2Cstn",
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
  "created_at" : "2016-12-19T22:24:42.14Z",
  "updated_at" : "2016-12-19T22:24:42.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/updates"
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


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "merchant_identity": "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

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
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDnLUgLcQw7omKRvWLNPw8HL", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuDqr7neGkj9LYcfWQzpxWJ", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUqM5jopmHyrXpXxBetSGVg6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:40.18Z",
  "updated_at" : "2016-12-19T22:24:40.22Z",
  "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:24:40.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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
curl https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUqM5jopmHyrXpXxBetSGVg6");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUqM5jopmHyrXpXxBetSGVg6');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUqM5jopmHyrXpXxBetSGVg6")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUqM5jopmHyrXpXxBetSGVg6")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUqM5jopmHyrXpXxBetSGVg6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahte6dDJodiWVhgr8okvZ",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:40.13Z",
  "updated_at" : "2016-12-19T22:24:40.74Z",
  "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:24:40.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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

curl https://api-staging.finix.io/authorizations/AUkbP2BWNo9PMjqXtVXQmMfX \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
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
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUqM5jopmHyrXpXxBetSGVg6');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUqM5jopmHyrXpXxBetSGVg6")
authorization.void()

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUqM5jopmHyrXpXxBetSGVg6")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AUkbP2BWNo9PMjqXtVXQmMfX",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:42.67Z",
  "updated_at" : "2016-12-19T22:24:43.30Z",
  "trace_id" : "d5847e26-6e95-47a2-b02d-148cdfe04f31",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : true,
  "expires_at" : "2016-12-26T22:24:42.67Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUkbP2BWNo9PMjqXtVXQmMfX"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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

curl https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUqM5jopmHyrXpXxBetSGVg6");

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUqM5jopmHyrXpXxBetSGVg6');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUqM5jopmHyrXpXxBetSGVg6")
```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUqM5jopmHyrXpXxBetSGVg6")


```
> Example Response:

```json
{
  "id" : "AUqM5jopmHyrXpXxBetSGVg6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahte6dDJodiWVhgr8okvZ",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:40.13Z",
  "updated_at" : "2016-12-19T22:24:40.74Z",
  "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:24:40.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

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
use Finix\Resources\Authorization;

$authorizations = Authorization::getPagination("/authorizations");


```
```python


from finix.resources import Authorization

authorization = Authorization.get()
```
```ruby
authorizations = Finix::Authorization.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUkbP2BWNo9PMjqXtVXQmMfX",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:42.67Z",
      "updated_at" : "2016-12-19T22:24:43.30Z",
      "trace_id" : "d5847e26-6e95-47a2-b02d-148cdfe04f31",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "is_void" : true,
      "expires_at" : "2016-12-26T22:24:42.67Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUkbP2BWNo9PMjqXtVXQmMfX"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        }
      }
    }, {
      "id" : "AUqM5jopmHyrXpXxBetSGVg6",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRahte6dDJodiWVhgr8okvZ",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:40.13Z",
      "updated_at" : "2016-12-19T22:24:40.74Z",
      "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "is_void" : false,
      "expires_at" : "2016-12-26T22:24:40.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUqM5jopmHyrXpXxBetSGVg6"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "Wade", 
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
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Wade", 
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
	));
$identity = $identity->save();

```
```python


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
	        "last_name": "Wade", 
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
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Wade", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "ID8MtWGeo3YG9S7AHfwvkBn2",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
    "last_name" : "Wade",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:24:34.40Z",
  "updated_at" : "2016-12-19T22:24:34.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
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


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 12000000, 
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
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Lees Sandwiches", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "incorporation_date"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "business_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
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
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.LeesSandwiches.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
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
    "max_transaction_amount" : 12000000,
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:24:27.32Z",
  "updated_at" : "2016-12-19T22:24:27.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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

curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDnLUgLcQw7omKRvWLNPw8HL");

```
```php
<?php
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
```
```python


from finix.resources import Identity
identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")

```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")


```
> Example Response:

```json
{
  "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
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
    "max_transaction_amount" : 12000000,
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:24:27.30Z",
  "updated_at" : "2016-12-19T22:24:27.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb


```
```java
import io.finix.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
```php
<?php
use Finix\Resources\Identity;

$identities= Identity::getPagination("/identities");


```
```python


from finix.resources import Identity
identity = Identity.get()

```
```ruby
identities = Finix::Identity.retrieve


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:47.92Z",
      "updated_at" : "2016-12-19T22:24:47.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID8MtWGeo3YG9S7AHfwvkBn2",
      "entity" : {
        "title" : null,
        "first_name" : "Sean",
        "last_name" : "Wade",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:34.38Z",
      "updated_at" : "2016-12-19T22:24:34.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID8RGNWHhQYZWxjgCMxRUVuP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:32.13Z",
      "updated_at" : "2016-12-19T22:24:32.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID4vPCXsAHa5whwERgTv1mwW",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:31.74Z",
      "updated_at" : "2016-12-19T22:24:31.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDmhJ1qg4pTaistwnH4WcQUx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:30.89Z",
      "updated_at" : "2016-12-19T22:24:30.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDt4S8nWFcBZJBZhDpXZCsKL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:30.39Z",
      "updated_at" : "2016-12-19T22:24:30.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDj4dTX1NsjFso7EbPDFP9Md",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "GENERAL_PARTNERSHIP",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:29.93Z",
      "updated_at" : "2016-12-19T22:24:29.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID2fEkPpQmEv6PX5fzD7snJM",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:29.42Z",
      "updated_at" : "2016-12-19T22:24:29.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDpC7HjbSjmCMhKhpbUgqHnM",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:28.79Z",
      "updated_at" : "2016-12-19T22:24:28.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID98NRUDHfRUJyZVjaPeqXqY",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:28.43Z",
      "updated_at" : "2016-12-19T22:24:28.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID89W5dUeq9EZ4DeivHgaFc7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:27.91Z",
      "updated_at" : "2016-12-19T22:24:27.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:27.30Z",
      "updated_at" : "2016-12-19T22:24:27.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
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
        "max_transaction_amount" : 1200000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-12-19T22:24:23.03Z",
      "updated_at" : "2016-12-19T22:24:23.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
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
	        "max_transaction_amount": 1200000, 
	        "principal_percentage_ownership": 50, 
	        "doing_business_as": "Pawny City Hall", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Pawny City Hall", 
	        "url": "www.PawnyCityHall.com", 
	        "business_name": "Pawny City Hall", 
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

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Serna",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Pawny City Hall",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2016-12-19T22:24:27.30Z",
  "updated_at" : "2016-12-19T22:24:57.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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

curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java

import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")

merchant = identity.provision_merchant
```

> Example Response:

```json
{
  "id" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "verification" : "VI3Q5Qm6isumtjbwdEbbaiif",
  "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:33.69Z",
  "updated_at" : "2016-12-19T22:24:33.69Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI3Q5Qm6isumtjbwdEbbaiif"
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
curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id => "MUjn3cFRC1aoMvK4R7Z8i6Pz")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "verification" : "VI3Q5Qm6isumtjbwdEbbaiif",
  "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:33.69Z",
  "updated_at" : "2016-12-19T22:24:33.69Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI3Q5Qm6isumtjbwdEbbaiif"
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
curl https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUjn3cFRC1aoMvK4R7Z8i6Pz");

```
```php
<?php
use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUjn3cFRC1aoMvK4R7Z8i6Pz');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MUjn3cFRC1aoMvK4R7Z8i6Pz")

```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUjn3cFRC1aoMvK4R7Z8i6Pz")

```
> Example Response:

```json
{
  "id" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "verification" : null,
  "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:33.65Z",
  "updated_at" : "2016-12-19T22:24:33.77Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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

## Reattempt Merchant Provisioning
```shell
curl https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '{}'
```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUjn3cFRC1aoMvK4R7Z8i6Pz');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUjn3cFRC1aoMvK4R7Z8i6Pz")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIsRCeGTXcXcsaL8NDVZGSpq",
  "external_trace_id" : "5d4a31f1-6fbf-4f65-a5f9-d0a669d4499b",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-19T22:24:58.41Z",
  "updated_at" : "2016-12-19T22:24:58.43Z",
  "trace_id" : "5d4a31f1-6fbf-4f65-a5f9-d0a669d4499b",
  "payment_instrument" : null,
  "merchant" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIsRCeGTXcXcsaL8NDVZGSpq"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
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
curl https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '{}'

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUjn3cFRC1aoMvK4R7Z8i6Pz');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUjn3cFRC1aoMvK4R7Z8i6Pz")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIsRCeGTXcXcsaL8NDVZGSpq",
  "external_trace_id" : "5d4a31f1-6fbf-4f65-a5f9-d0a669d4499b",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-19T22:24:58.41Z",
  "updated_at" : "2016-12-19T22:24:58.43Z",
  "trace_id" : "5d4a31f1-6fbf-4f65-a5f9-d0a669d4499b",
  "payment_instrument" : null,
  "merchant" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIsRCeGTXcXcsaL8NDVZGSpq"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

```
```php
<?php
use Finix\Resources\Merchant;

$merchants = Merchant::getPagination("/merchants");


```
```python


from finix.resources import Merchant
merchant = Merchant.get()

```
```ruby
merchants = Finix::Merchant.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUj1s1nqLUBLJvudCJVFvpe1",
      "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "verification" : null,
      "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
      "processor" : "VISA_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-12-19T22:24:48.37Z",
      "updated_at" : "2016-12-19T22:24:49.01Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUj1s1nqLUBLJvudCJVFvpe1"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUj1s1nqLUBLJvudCJVFvpe1/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "MUjn3cFRC1aoMvK4R7Z8i6Pz",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "verification" : null,
      "merchant_profile" : "MPnsRE3L4QZXduWmbXEs2LS5",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-12-19T22:24:33.65Z",
      "updated_at" : "2016-12-19T22:24:33.77Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPnsRE3L4QZXduWmbXEs2LS5"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
curl https://api-staging.finix.io/merchants/MUjn3cFRC1aoMvK4R7Z8i6Pz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUjn3cFRC1aoMvK4R7Z8i6Pz');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUjn3cFRC1aoMvK4R7Z8i6Pz")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:47.92Z",
      "updated_at" : "2016-12-19T22:24:47.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID8MtWGeo3YG9S7AHfwvkBn2",
      "entity" : {
        "title" : null,
        "first_name" : "Sean",
        "last_name" : "Wade",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:34.38Z",
      "updated_at" : "2016-12-19T22:24:34.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID8RGNWHhQYZWxjgCMxRUVuP",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:32.13Z",
      "updated_at" : "2016-12-19T22:24:32.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8RGNWHhQYZWxjgCMxRUVuP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID4vPCXsAHa5whwERgTv1mwW",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:31.74Z",
      "updated_at" : "2016-12-19T22:24:31.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4vPCXsAHa5whwERgTv1mwW/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDmhJ1qg4pTaistwnH4WcQUx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:30.89Z",
      "updated_at" : "2016-12-19T22:24:30.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmhJ1qg4pTaistwnH4WcQUx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDt4S8nWFcBZJBZhDpXZCsKL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:30.39Z",
      "updated_at" : "2016-12-19T22:24:30.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDt4S8nWFcBZJBZhDpXZCsKL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDj4dTX1NsjFso7EbPDFP9Md",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "GENERAL_PARTNERSHIP",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:29.93Z",
      "updated_at" : "2016-12-19T22:24:29.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDj4dTX1NsjFso7EbPDFP9Md/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID2fEkPpQmEv6PX5fzD7snJM",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:29.42Z",
      "updated_at" : "2016-12-19T22:24:29.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2fEkPpQmEv6PX5fzD7snJM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDpC7HjbSjmCMhKhpbUgqHnM",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:28.79Z",
      "updated_at" : "2016-12-19T22:24:28.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpC7HjbSjmCMhKhpbUgqHnM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID98NRUDHfRUJyZVjaPeqXqY",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:28.43Z",
      "updated_at" : "2016-12-19T22:24:28.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID98NRUDHfRUJyZVjaPeqXqY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "ID89W5dUeq9EZ4DeivHgaFc7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:27.91Z",
      "updated_at" : "2016-12-19T22:24:27.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID89W5dUeq9EZ4DeivHgaFc7/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDnLUgLcQw7omKRvWLNPw8HL",
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
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:24:27.30Z",
      "updated_at" : "2016-12-19T22:24:27.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
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
        "max_transaction_amount" : 1200000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-12-19T22:24:23.03Z",
      "updated_at" : "2016-12-19T22:24:23.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "name": "Laura Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card_name": "Business Card"
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
	    "identity": "ID8MtWGeo3YG9S7AHfwvkBn2"
	}'


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
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card_name"=> "Business Card"
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
	    "identity"=> "ID8MtWGeo3YG9S7AHfwvkBn2"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card_name": "Business Card"
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
	    "identity": "ID8MtWGeo3YG9S7AHfwvkBn2"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Laura Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> {
	        "card_name"=> "Business Card"
	    }, 
	    "number"=> "4957030420210454", 
	    "expiration_month"=> 12, 
	    "address"=> {
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    }, 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "ID8MtWGeo3YG9S7AHfwvkBn2"
	}).save
```
> Example Response:

```json
{
  "id" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "fingerprint" : "FPR1264366140",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Lopez",
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
  "created_at" : "2016-12-19T22:24:34.81Z",
  "updated_at" : "2016-12-19T22:24:34.81Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID8MtWGeo3YG9S7AHfwvkBn2",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/updates"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
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
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}'


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
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\BankAccount;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$bank_account = new BankAccount(
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
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
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
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save()
```
```ruby
bank_account = Finix::BankAccount.new(
	{
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> {
	        "Bank Account"=> "Company Account"
	    }, 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save
```
> Example Response:

```json
{
  "id" : "PIrThBosxrALH9mZtgfoNBBd",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:24:32.66Z",
  "updated_at" : "2016-12-19T22:24:32.66Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}'


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
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type": "TOKEN", 
	    "identity": "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save()
```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK5hyKPo5VMBXaAF16N2Cstn", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDnLUgLcQw7omKRvWLNPw8HL"
	}).save
```
> Example Response:

```json
{
  "id" : "PI5hyKPo5VMBXaAF16N2Cstn",
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
  "created_at" : "2016-12-19T22:24:42.14Z",
  "updated_at" : "2016-12-19T22:24:42.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/updates"
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


curl https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIrThBosxrALH9mZtgfoNBBd")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIrThBosxrALH9mZtgfoNBBd');

```
```python



```
```ruby
payment_instrument = Finix::PaymentInstrument.retrieve(:id=> "PIrThBosxrALH9mZtgfoNBBd")

```
> Example Response:

```json
{
  "id" : "PIrThBosxrALH9mZtgfoNBBd",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:24:32.63Z",
  "updated_at" : "2016-12-19T22:24:33.06Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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

## List all Payment Instruments

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb
```
```java
import io.finix.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
```python



```
```ruby
payment_instruments = Finix::PaymentInstruments.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI3RpJzGMeYWKxewwigBfmzE",
      "fingerprint" : "FPR1419155432",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jessie Green",
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
      "created_at" : "2016-12-19T22:24:49.55Z",
      "updated_at" : "2016-12-19T22:24:49.55Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE/updates"
        }
      }
    }, {
      "id" : "PIin2GY65iyswFcY7YgZTQun",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:48.37Z",
      "updated_at" : "2016-12-19T22:24:48.37Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIin2GY65iyswFcY7YgZTQun"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIin2GY65iyswFcY7YgZTQun/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIin2GY65iyswFcY7YgZTQun/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIin2GY65iyswFcY7YgZTQun/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIWwUoKMSRWgfQBbjrKpTsY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:48.37Z",
      "updated_at" : "2016-12-19T22:24:48.37Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIWwUoKMSRWgfQBbjrKpTsY"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIWwUoKMSRWgfQBbjrKpTsY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIWwUoKMSRWgfQBbjrKpTsY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIWwUoKMSRWgfQBbjrKpTsY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIp8WyZcC6NL4mYZsbVoqXWy",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:48.37Z",
      "updated_at" : "2016-12-19T22:24:48.37Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIkGDz2fREzNTT9RevJR4Eu9",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:47.20Z",
      "updated_at" : "2016-12-19T22:24:47.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkGDz2fREzNTT9RevJR4Eu9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkGDz2fREzNTT9RevJR4Eu9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkGDz2fREzNTT9RevJR4Eu9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkGDz2fREzNTT9RevJR4Eu9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PI6UMv12LzK3YvoBQetYL6iK",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:47.20Z",
      "updated_at" : "2016-12-19T22:24:47.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6UMv12LzK3YvoBQetYL6iK"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6UMv12LzK3YvoBQetYL6iK/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6UMv12LzK3YvoBQetYL6iK/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6UMv12LzK3YvoBQetYL6iK/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIKV741rir6G3jYyUbEE61U",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:47.20Z",
      "updated_at" : "2016-12-19T22:24:47.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIKV741rir6G3jYyUbEE61U"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIKV741rir6G3jYyUbEE61U/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIKV741rir6G3jYyUbEE61U/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIKV741rir6G3jYyUbEE61U/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIkDwvLx1fThvUpJmmrvP7ti",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:47.20Z",
      "updated_at" : "2016-12-19T22:24:47.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkDwvLx1fThvUpJmmrvP7ti"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkDwvLx1fThvUpJmmrvP7ti/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkDwvLx1fThvUpJmmrvP7ti/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkDwvLx1fThvUpJmmrvP7ti/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PI5hyKPo5VMBXaAF16N2Cstn",
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
      "created_at" : "2016-12-19T22:24:42.10Z",
      "updated_at" : "2016-12-19T22:24:42.10Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5hyKPo5VMBXaAF16N2Cstn/updates"
        }
      }
    }, {
      "id" : "PI2DJNHaJEiB4pJWXchYVdFv",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2016-12-19T22:24:35.33Z",
      "updated_at" : "2016-12-19T22:24:35.33Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID8MtWGeo3YG9S7AHfwvkBn2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2DJNHaJEiB4pJWXchYVdFv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2DJNHaJEiB4pJWXchYVdFv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2DJNHaJEiB4pJWXchYVdFv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2DJNHaJEiB4pJWXchYVdFv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "fingerprint" : "FPR1264366140",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Laura Lopez",
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
      "created_at" : "2016-12-19T22:24:34.77Z",
      "updated_at" : "2016-12-19T22:24:40.20Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID8MtWGeo3YG9S7AHfwvkBn2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8MtWGeo3YG9S7AHfwvkBn2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ/updates"
        }
      }
    }, {
      "id" : "PI6iRaxLxFfqVGsNHBDMhrNS",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:33.65Z",
      "updated_at" : "2016-12-19T22:24:33.65Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6iRaxLxFfqVGsNHBDMhrNS"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6iRaxLxFfqVGsNHBDMhrNS/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6iRaxLxFfqVGsNHBDMhrNS/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6iRaxLxFfqVGsNHBDMhrNS/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIoYLDonYqkMvACJVF2d9g9u",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:33.65Z",
      "updated_at" : "2016-12-19T22:24:33.65Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoYLDonYqkMvACJVF2d9g9u"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoYLDonYqkMvACJVF2d9g9u/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoYLDonYqkMvACJVF2d9g9u/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoYLDonYqkMvACJVF2d9g9u/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PI6RZCi3hNi69kfRq22s5X7R",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:33.65Z",
      "updated_at" : "2016-12-19T22:24:33.65Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIrThBosxrALH9mZtgfoNBBd",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2016-12-19T22:24:32.63Z",
      "updated_at" : "2016-12-19T22:24:33.06Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PI2wvnn1MHez5QkCj81abTCR",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:23.61Z",
      "updated_at" : "2016-12-19T22:24:23.61Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2wvnn1MHez5QkCj81abTCR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2wvnn1MHez5QkCj81abTCR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2wvnn1MHez5QkCj81abTCR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2wvnn1MHez5QkCj81abTCR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PIHgk7dsK6hXhkt4og8M1U3",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:23.61Z",
      "updated_at" : "2016-12-19T22:24:23.61Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PI6WXLDMSpy69uADUDRgSain",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:23.61Z",
      "updated_at" : "2016-12-19T22:24:23.61Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6WXLDMSpy69uADUDRgSain"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6WXLDMSpy69uADUDRgSain/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6WXLDMSpy69uADUDRgSain/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6WXLDMSpy69uADUDRgSain/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        }
      }
    }, {
      "id" : "PItEGSn7RW7ZLKSC1DTK32Tf",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:23.61Z",
      "updated_at" : "2016-12-19T22:24:23.61Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItEGSn7RW7ZLKSC1DTK32Tf"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItEGSn7RW7ZLKSC1DTK32Tf/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItEGSn7RW7ZLKSC1DTK32Tf/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItEGSn7RW7ZLKSC1DTK32Tf/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDnLUgLcQw7omKRvWLNPw8HL');
$settlement = new Settlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));
$settlement = $identity->createSettlement($settlement);

```
```python


from finix.resources import Identity
from finix.resources import Settlement

identity = Identity.get(id="IDnLUgLcQw7omKRvWLNPw8HL")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDnLUgLcQw7omKRvWLNPw8HL")
settlement = identity.create_settlement(
	{
	    "currency"=> "USD", 
	    "tags"=> {
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    }
	})
```
> Example Response:

```json
{
  "id" : "STdGwzmTectPa65NjJYZiBcV",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "currency" : "USD",
  "created_at" : "2016-12-19T22:25:21.85Z",
  "updated_at" : "2016-12-19T22:25:21.86Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 685327,
  "total_fees" : 68534,
  "total_fee" : 68534,
  "net_amount" : 616793,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STdGwzmTectPa65NjJYZiBcV");

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STdGwzmTectPa65NjJYZiBcV');

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STdGwzmTectPa65NjJYZiBcV")

```
> Example Response:

```json
{
  "id" : "STdGwzmTectPa65NjJYZiBcV",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "currency" : "USD",
  "created_at" : "2016-12-19T22:25:21.82Z",
  "updated_at" : "2016-12-19T22:25:22.89Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 685327,
  "total_fees" : 68534,
  "total_fee" : 68534,
  "net_amount" : 616793,
  "destination" : "PIrThBosxrALH9mZtgfoNBBd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=debit"
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


## List all Settlements
```shell
curl https://api-staging.finix.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
```php
<?php
use Finix\Resources\Settlement;

$settlements = Settlement::getPagination("/settlements");


```
```python


from finix.resources import Settlement
settlements = Settlement.get()

```
```ruby
settlements = Finix::Settlement.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STdGwzmTectPa65NjJYZiBcV",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "currency" : "USD",
      "created_at" : "2016-12-19T22:25:21.82Z",
      "updated_at" : "2016-12-19T22:25:22.89Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 685327,
      "total_fees" : 68534,
      "total_fee" : 68534,
      "net_amount" : 616793,
      "destination" : "PIrThBosxrALH9mZtgfoNBBd",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STdGwzmTectPa65NjJYZiBcV');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STdGwzmTectPa65NjJYZiBcV")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR7dt5D2T69uuPqcYvbUscnp",
      "amount" : 616793,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "5cccc6bd-7c29-4ce7-a826-aded97c4d011",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PI6RZCi3hNi69kfRq22s5X7R",
      "destination" : "PIrThBosxrALH9mZtgfoNBBd",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:25:22.42Z",
      "updated_at" : "2016-12-19T22:25:22.73Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7dt5D2T69uuPqcYvbUscnp"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7dt5D2T69uuPqcYvbUscnp/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7dt5D2T69uuPqcYvbUscnp/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7dt5D2T69uuPqcYvbUscnp/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7dt5D2T69uuPqcYvbUscnp/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrThBosxrALH9mZtgfoNBBd"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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


## List Transfers in a Settlement
```shell

curl https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STdGwzmTectPa65NjJYZiBcV');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STdGwzmTectPa65NjJYZiBcV")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRxbr3XoPzQnoCFM36HAME2U",
      "amount" : 68512,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "0de86daf-2467-4ea0-9996-987287a373f3",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PI6RZCi3hNi69kfRq22s5X7R",
      "destination" : "PI6WXLDMSpy69uADUDRgSain",
      "ready_to_settle_at" : "2016-12-19T22:25:17.38Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:25:20.17Z",
      "updated_at" : "2016-12-19T22:25:21.41Z",
      "merchant_identity" : "IDjDG2Vb1iTUzE6TMZjn7PfZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxbr3XoPzQnoCFM36HAME2U"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxbr3XoPzQnoCFM36HAME2U/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDjDG2Vb1iTUzE6TMZjn7PfZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRxbr3XoPzQnoCFM36HAME2U/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRxbr3XoPzQnoCFM36HAME2U/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRxbr3XoPzQnoCFM36HAME2U/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6WXLDMSpy69uADUDRgSain"
        }
      }
    }, {
      "id" : "TRtbpKp5M1eYw5mCWG64miEB",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "aecad403-15c6-4841-b3c6-c893d2914c30",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PI6RZCi3hNi69kfRq22s5X7R",
      "destination" : "PIHgk7dsK6hXhkt4og8M1U3",
      "ready_to_settle_at" : "2016-12-19T22:25:17.38Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:25:18.10Z",
      "updated_at" : "2016-12-19T22:25:20.02Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbpKp5M1eYw5mCWG64miEB"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbpKp5M1eYw5mCWG64miEB/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbpKp5M1eYw5mCWG64miEB/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbpKp5M1eYw5mCWG64miEB/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbpKp5M1eYw5mCWG64miEB/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3"
        }
      }
    }, {
      "id" : "TRh5XXrc3ZrgVr3sbufUsQTT",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "138a7a42-78d6-4d1a-8afe-2136d505c90f",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PI6RZCi3hNi69kfRq22s5X7R",
      "destination" : "PIHgk7dsK6hXhkt4og8M1U3",
      "ready_to_settle_at" : "2016-12-19T22:25:08.85Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:25:09.53Z",
      "updated_at" : "2016-12-19T22:25:11.38Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRh5XXrc3ZrgVr3sbufUsQTT"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRh5XXrc3ZrgVr3sbufUsQTT/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRh5XXrc3ZrgVr3sbufUsQTT/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRh5XXrc3ZrgVr3sbufUsQTT/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRh5XXrc3ZrgVr3sbufUsQTT/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIHgk7dsK6hXhkt4og8M1U3"
        }
      }
    }, {
      "id" : "TRahte6dDJodiWVhgr8okvZ",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
      "ready_to_settle_at" : "2016-12-19T22:25:09.14Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:40.64Z",
      "updated_at" : "2016-12-19T22:25:08.57Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        }
      }
    }, {
      "id" : "TRtbsy5xbdSGWJBovBxgLAsp",
      "amount" : 685227,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "f9209197-4261-40c6-8f85-b25e5bfe2516",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
      "ready_to_settle_at" : "2016-12-19T22:25:17.67Z",
      "fee" : 68523,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:35.95Z",
      "updated_at" : "2016-12-19T22:25:17.28Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STdGwzmTectPa65NjJYZiBcV/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 5
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

- **CANCELED:** Created, and then reversed before transfer has transitioned to succeeded

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb


```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRtbsy5xbdSGWJBovBxgLAsp");

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRtbsy5xbdSGWJBovBxgLAsp');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TRtbsy5xbdSGWJBovBxgLAsp")

```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRtbsy5xbdSGWJBovBxgLAsp")

```
> Example Response:

```json
{
  "id" : "TRtbsy5xbdSGWJBovBxgLAsp",
  "amount" : 685227,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "f9209197-4261-40c6-8f85-b25e5bfe2516",
  "currency" : "USD",
  "application" : "APtQNQpPihoWYaUK26c2XyhY",
  "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
  "ready_to_settle_at" : null,
  "fee" : 68523,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:35.95Z",
  "updated_at" : "2016-12-19T22:24:36.06Z",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
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

curl https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```java

import io.finix.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
```php
<?php
use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TRtbsy5xbdSGWJBovBxgLAsp');
$refund = $debit->reverse(11);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TRtbsy5xbdSGWJBovBxgLAsp")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRtbsy5xbdSGWJBovBxgLAsp")

refund = Finix::Transfer.reverse(
          {
          "refund_amount" => 100
        }
        ).save
```
> Example Response:

```json
{
  "id" : "TRw7eYiA7uGCXMhfYc5bL9He",
  "amount" : 719231,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "f3d13b71-4c79-42fd-ac40-6193325b1537",
  "currency" : "USD",
  "application" : "APtQNQpPihoWYaUK26c2XyhY",
  "source" : "PI6RZCi3hNi69kfRq22s5X7R",
  "destination" : "PIuDqr7neGkj9LYcfWQzpxWJ",
  "ready_to_settle_at" : null,
  "fee" : 71923,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:39.35Z",
  "updated_at" : "2016-12-19T22:24:39.41Z",
  "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRw7eYiA7uGCXMhfYc5bL9He"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRw7eYiA7uGCXMhfYc5bL9He/payment_instruments"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java
import io.finix.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
```php
<?php
use Finix\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


```
```python


from finix.resources import Transfer
transfer = Transfer.get()

```
```ruby
transfers = Finix::Transfer.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR3SRPPxQiqgo7tTUo4Dv2LX",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "184732",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIp8WyZcC6NL4mYZsbVoqXWy",
      "destination" : "PI3RpJzGMeYWKxewwigBfmzE",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:50.06Z",
      "updated_at" : "2016-12-19T22:24:51.53Z",
      "merchant_identity" : "ID53m75hc5JQkEPSGsiVsBMJ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID53m75hc5JQkEPSGsiVsBMJ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SRPPxQiqgo7tTUo4Dv2LX/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8WyZcC6NL4mYZsbVoqXWy"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3RpJzGMeYWKxewwigBfmzE"
        }
      }
    }, {
      "id" : "TRahte6dDJodiWVhgr8okvZ",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "3cd32892-65f0-4ff0-acaa-e88764ed9cf3",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:40.64Z",
      "updated_at" : "2016-12-19T22:24:40.74Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRahte6dDJodiWVhgr8okvZ/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        }
      }
    }, {
      "id" : "TRw7eYiA7uGCXMhfYc5bL9He",
      "amount" : 719231,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "bdd7f36b-d2d2-4b72-887b-3e1bce816c83",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PI6RZCi3hNi69kfRq22s5X7R",
      "destination" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "ready_to_settle_at" : null,
      "fee" : 71923,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:39.26Z",
      "updated_at" : "2016-12-19T22:24:39.41Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRw7eYiA7uGCXMhfYc5bL9He"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRw7eYiA7uGCXMhfYc5bL9He/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        }
      }
    }, {
      "id" : "TRcGoT9ZhfAo2NfL1RG64Gse",
      "amount" : 719231,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "31348f54-0b47-448e-86e8-25661db32cf6",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
      "ready_to_settle_at" : null,
      "fee" : 71923,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:38.22Z",
      "updated_at" : "2016-12-19T22:24:39.33Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGoT9ZhfAo2NfL1RG64Gse/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
        }
      }
    }, {
      "id" : "TRtbsy5xbdSGWJBovBxgLAsp",
      "amount" : 685227,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "f9209197-4261-40c6-8f85-b25e5bfe2516",
      "currency" : "USD",
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "source" : "PIuDqr7neGkj9LYcfWQzpxWJ",
      "destination" : "PI6RZCi3hNi69kfRq22s5X7R",
      "ready_to_settle_at" : null,
      "fee" : 68523,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:35.95Z",
      "updated_at" : "2016-12-19T22:24:36.06Z",
      "merchant_identity" : "IDnLUgLcQw7omKRvWLNPw8HL",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDnLUgLcQw7omKRvWLNPw8HL"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtbsy5xbdSGWJBovBxgLAsp/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuDqr7neGkj9LYcfWQzpxWJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6RZCi3hNi69kfRq22s5X7R"
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
    -u USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
```php
<?php
use Finix\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
$webhook = $webhook->save();

```
```python


from finix.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```ruby
webhook = Finix::Webhook.new(
                    {
                    "url" => "http=>//requestb.in/1jb5zu11"
                    }
                ).save
```
> Example Response:

```json
{
  "id" : "WHfaPBt2bj8K1WXAeerJnWhW",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APtQNQpPihoWYaUK26c2XyhY",
  "created_at" : "2016-12-19T22:24:26.49Z",
  "updated_at" : "2016-12-19T22:24:26.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHfaPBt2bj8K1WXAeerJnWhW"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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



curl https://api-staging.finix.io/webhooks/WHfaPBt2bj8K1WXAeerJnWhW \
    -H "Content-Type: application/vnd.json+api" \
    -u USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb


```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHfaPBt2bj8K1WXAeerJnWhW");

```
```php
<?php
use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHfaPBt2bj8K1WXAeerJnWhW');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WHfaPBt2bj8K1WXAeerJnWhW")

```
```ruby
webhook = Finix::Webhook.retrieve(:id=> "WHfaPBt2bj8K1WXAeerJnWhW")


```
> Example Response:

```json
{
  "id" : "WHfaPBt2bj8K1WXAeerJnWhW",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APtQNQpPihoWYaUK26c2XyhY",
  "created_at" : "2016-12-19T22:24:26.49Z",
  "updated_at" : "2016-12-19T22:24:26.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHfaPBt2bj8K1WXAeerJnWhW"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
    -u  USgxidPLBeHb82t4LEoJcUkB:3bd5be80-588c-42ca-8543-9c097e9844fb

```
```java
import io.finix.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
```php
<?php
use Finix\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


```
```python


from finix.resources import Webhook
webhooks = Webhook.get()

```
```ruby
webhooks = Finix::Webhook.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHfaPBt2bj8K1WXAeerJnWhW",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APtQNQpPihoWYaUK26c2XyhY",
      "created_at" : "2016-12-19T22:24:26.49Z",
      "updated_at" : "2016-12-19T22:24:26.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHfaPBt2bj8K1WXAeerJnWhW"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APtQNQpPihoWYaUK26c2XyhY"
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
```
```python


```
```ruby
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
