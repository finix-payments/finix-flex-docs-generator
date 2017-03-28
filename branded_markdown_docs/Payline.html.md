---
title: Payline API Reference

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

3. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.

3. [Tokenization with Hosted Fields](#tokenization-with-hosted-fields): This guide
explains how to properly tokenize cards in production via our hosted fields solution.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.payline.payments.processing.client</groupId>
  <artifactId>payline-data</artifactId>
  <version>${version}</version>
</dependency>

...

<repositories>
  <repository>
    <id>oss-snapshots</id>
    <url>https://oss.sonatype.org/content/repositories/snapshots</url>
    <snapshots>
      <enabled>true</enabled>
    </snapshots>
  </repository>
</repositories>

*/

import io.payline.payments.processing.client.ProcessingClient;
import io.payline.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("https://api-test.payline.io");
  client.setupUserIdAndPassword("USp1kfJp3wqYRm7txAM1PmBG", "ff9b1de8-d2b5-4555-b049-7f44923daf71");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USp1kfJp3wqYRm7txAM1PmBG',
	"password" => 'ff9b1de8-d2b5-4555-b049-7f44923daf71']
	);

require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("USp1kfJp3wqYRm7txAM1PmBG", "ff9b1de8-d2b5-4555-b049-7f44923daf71"))

```
```ruby
# To download the Ruby gem:
# gem install payline-data

require 'payline'

Payline.configure(
    :root_url => 'https://api-test.payline.io',
    :user=>'USp1kfJp3wqYRm7txAM1PmBG',
    :password => 'ff9b1de8-d2b5-4555-b049-7f44923daf71'
)
```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USp1kfJp3wqYRm7txAM1PmBG`

- Password: `ff9b1de8-d2b5-4555-b049-7f44923daf71`

- Application ID: `APueARWWD8YjyYDUDx5ZiguK`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://api-test.payline.io`

- **Production API:** `https://api.payline.io`

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
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
	        "ownership_type": "PRIVATE", 
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
```java

import io.payline.payments.processing.client.model.Address;
import io.payline.payments.processing.client.model.BankAccountType;
import io.payline.payments.processing.client.model.BusinessType;
import io.payline.payments.processing.client.model.Date;
import io.payline.payments.processing.client.model.Entity;
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
        .dob(Date.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1000l)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .defaultStatementDescriptor("Business Inc")
        .incorporationDate(Date.builder()
          .day(1)
          .month(12)
          .year(2012)
          .build()
        )
        .principalPercentageOwnership(51)
        .build()
    )
    .build()
);
```
```php
<?php
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
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
	        "ownership_type"=> "PRIVATE", 
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": True, 
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
	        "ownership_type": "PRIVATE", 
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
	}).save()

```
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Bobs Burgers", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.BobsBurgers.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDjAKAeJpcMnhjeANbdTkcht",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T03:41:18.94Z",
  "updated_at" : "2017-03-28T03:41:18.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
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
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDjAKAeJpcMnhjeANbdTkcht"
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
use Payline\Resources\Identity;
use Payline\Resources\BankAccount;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
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
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
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
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}).save()

```
```ruby
bank_account = Payline::BankAccount.new(
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
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2c8hJ1P8U3oH5YaSbZydia",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T03:41:24.08Z",
  "updated_at" : "2017-03-28T03:41:24.08Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Payline\Resources\Identity;
use Payline\Resources\Merchant;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "verification" : "VI2i9MffNqwgBoJacMSUm6Fv",
  "merchant_profile" : "MPszfxydK2dpFsLQy698Vpia",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T03:41:25.13Z",
  "updated_at" : "2017-03-28T03:41:25.13Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPszfxydK2dpFsLQy698Vpia"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VI2i9MffNqwgBoJacMSUm6Fv"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
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

import io.payline.payments.processing.client.model.Identity;

Identity buyerIdentity = client.identitiesClient().save(
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
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Diaz", 
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


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
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
	}).save()

```
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Diaz", 
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
  "id" : "IDuN9GzXzE8gnB3zM4iLgb4H",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-03-28T03:41:25.91Z",
  "updated_at" : "2017-03-28T03:41:25.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "name": "Laura Green", 
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
	    "identity": "IDuN9GzXzE8gnB3zM4iLgb4H"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentCard;
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Green", 
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
	    "identity"=> "IDuN9GzXzE8gnB3zM4iLgb4H"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Green", 
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
	    "identity": "IDuN9GzXzE8gnB3zM4iLgb4H"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Laura Green", 
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
	    "identity"=> "IDuN9GzXzE8gnB3zM4iLgb4H"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeq2wr8Mouvzym2BstDoBuj",
  "fingerprint" : "FPR1101267070",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Green",
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
  "created_at" : "2017-03-28T03:41:26.36Z",
  "updated_at" : "2017-03-28T03:41:26.36Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuN9GzXzE8gnB3zM4iLgb4H",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/updates"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "merchant_identity": "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("IDjAKAeJpcMnhjeANbdTkcht")
    .source("PIeq2wr8Mouvzym2BstDoBuj")
    .build()
);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```python


from payline.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:31.41Z",
  "updated_at" : "2017-03-28T03:41:31.46Z",
  "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : false,
  "expires_at" : "2017-04-04T03:41:31.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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
source | *string*, **required** | The buyer's `Payment Instrument` ID that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Capture the Authorization
```shell
curl https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUsRDLf4ArvstWpwxxJnvk5D");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsRDLf4ArvstWpwxxJnvk5D');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUsRDLf4ArvstWpwxxJnvk5D")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUsRDLf4ArvstWpwxxJnvk5D")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRcH771hhEU9zxL8Z2qbsLsk",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:31.34Z",
  "updated_at" : "2017-03-28T03:41:32.10Z",
  "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : false,
  "expires_at" : "2017-04-04T03:41:31.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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
curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

```
```php
<?php
use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
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


from payline.resources import Identity
from payline.resources import Settlement

identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")
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
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")
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
  "id" : "STopQZHHosXutaEf9AUJW3qi",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "currency" : "USD",
  "created_at" : "2017-03-28T03:42:37.41Z",
  "updated_at" : "2017-03-28T03:42:37.42Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1416170,
  "total_fees" : 141618,
  "total_fee" : 141618,
  "net_amount" : 1274552,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=debit"
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

## Embedded Tokenization

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
          applicationId: 'APueARWWD8YjyYDUDx5ZiguK',
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
  "id" : "TK2LN5pE7NjyCL7Ecbn9aZ9s",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-28T03:41:33.14Z",
  "updated_at" : "2017-03-28T03:41:33.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-29T03:41:33.14Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TK2LN5pE7NjyCL7Ecbn9aZ9s")
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2LN5pE7NjyCL7Ecbn9aZ9s",
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
  "created_at" : "2017-03-28T03:41:33.60Z",
  "updated_at" : "2017-03-28T03:41:33.60Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/updates"
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


## Tokenization with Hosted Fields

### Library summary

The `SecureForm` library is a javascript library that allows you to integrate
secure fields with non-secure fields in your page. The secure fields behave like
traditional input fields while preventing access to the unsecured data.

Once the fields are initialized the library communicates the state of the fields
through a JavaScript callback. The state object includes information about the
validity, focused value and if the user has entered information in the field.

For a complete example of how to use the library please refer to this
[jsFiddle example](https://jsfiddle.net/rserna2010/vap35hru/).

### Step 1: Include library

```html
 <script type="text/javascript" src="https://js.verygoodvault.com/js-vgfield-2/payline.js"></script>
```

First we'll need to include the library on the webpage where you're hosting your
form. Please include the script as demonstrated to the right.


### Step 2: Initialize the secure form

`SecureForm.create(environment, onUpdateCallback)-> Form`

```javascript

/*
SecureForm.create(environment, onUpdateCallback)-> Form
*/

const secureForm = SecureForm.create('sandbox', function(state) {
   // Logic for interacting with form's potential states
 });
```

The next step is to configure the library. This method is the single entry point into the library.
It initializes and returns a `Form` object representing the secured form.


#### Arguments
Field | Type | Description
----- | ---- | -----------
environment | *string*, **required** |  `sandbox` for testing and `live` for production
onUpdateCallback | *function*, **required** | Callback that will be called whenever the form state changes. It receives the state object representing the current state.

### Step 3: Configure the form fields

`Form#field(selector, properties)-> Field`

```javascript

/*
Form#field(selector, properties)-> Field
*/

secureForm.field('#my-cool-parent', {
    'successColor': '#3c763d',
    'errorColor': '#a94442',
    'lineHeight': '1.5rem',
    'fontSize': '24px',
    'fontFamily': 'Comic Sans',
    'color': '#31708f',
    'placeholder': 'Card number',
    'name': 'cc-number',
    'type': 'card-number',
    'validations': [],
});

```

Now that we have a `Form` object we'll want to style it and add any validations.

#### Arguments
Field | Type | Description
----- | ---- | -----------
selector | *string*, **required** | CSS Selector that points to the element where the field will be added

#### Properties Object
Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the input field. Will be used when submitting the data.
type | *string*, **required** | Type of the input field (`card-number`, `card-security-code`, `card-expiration-date`, `text`, `password`, `number`, `zip-code`)
validations | *array*, **optional** |  Array of validations that will be used to calculate the `isValid` state (`required`, `validCardExpirationDate`, `validCardNumber`, `validCardSecurityCode`)
placeholder | *string*, **optional** | Text displayed when the field is empty
successColor | *string*, **optional** | Text color when the field is valid
errorColor | *string*, **optional** | Text color when the field is invalid
color | *string*, **optional** | Text color
lineHeight | *string*, **optional** | Line height value
fontSize | *string*, **optional** | Size of text
fontFamily | *string*, **optional** | Font family used in the text.

> Example Response:

```javascript
{
  "number": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required",
      "is not a valid card number"
    ],
    "isValid": false,
    "name": "number"
  },
  "security_code": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required",
      "is not a valid security code"
    ],
    "isValid": false,
    "name": "security_code"
  },
  "expiration_month": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required"
    ],
    "isValid": false,
    "name": "expiration_month"
  },
  "expiration_year": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required"
    ],
    "isValid": false,
    "name": "expiration_year"
  }
}
```

### Step 4: Submit payload and handle response


`Form#submit(path, options, callback) -> Form
`


```javascript

/*
Form#submit(path, options, callback)-> Form
*/

document.getElementById('cc-form')
  .addEventListener('submit', function(e) {
    e.preventDefault();
    secureForm.submit('/applications/APueARWWD8YjyYDUDx5ZiguK/tokens', {
        data: {
            type: 'PAYMENT_CARD',
        },
    }, function(status, response) {
        // callback for handling response and sending token to back-end server
        console.log("Response has been received", status, response);
    });
}, false);

```

> Example Response:

```json
{
  "id" : "TK2LN5pE7NjyCL7Ecbn9aZ9s",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-28T03:41:33.14Z",
  "updated_at" : "2017-03-28T03:41:33.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-29T03:41:33.14Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    }
  }
}
```


Finally we will need to register a click event that fires when our users submit
the form and define a callback for handling the response.

Next, configure the library to your specific `Application` where all of the form
fields will be submitted during the executed `POST` request. We'll also want to
register a click event that fires when our users submit the form and define a
callback for handling the response.

Once you've handled the response you will want to store that ID to utilize
the token in the future. To do this you will need to send the ID from your
front-end client to your back-end server.


#### Arguments
Field | Type | Description
----- | ---- | -----------
path | *string*, **required** | Path to your `Application's` tokens endpoint
options | *object*, **required** | Options object that can include additional `data`, such as the type of Payment Instrument
callback | *function*, **required** | Callback that will be executed when the HTTPRequest is finished. The callback receives the HTTP status code and the data as two arguments.

### Step 5: Associate to an Identity
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TK2LN5pE7NjyCL7Ecbn9aZ9s")
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2LN5pE7NjyCL7Ecbn9aZ9s",
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
  "created_at" : "2017-03-28T03:41:33.60Z",
  "updated_at" : "2017-03-28T03:41:33.60Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/updates"
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


## Testing for specific responses and errors

Before taking your integration to production, use the information below to test it thoroughly.

Amount| Description
----- | -----------
`100` | Success amount
`102` | Failed amount
`103` | Canceled amount
`104` | Exception amount
`888888` | Disputed amount
`193` | Insufficient funds amount
`194` | Invalid card number amount
`889986` | AVS total failure amount 
`889987` | CVC failure amount
`889988` | Risk amount canceled amount

Card| Description
----- | -----------
 `4000000000000036` | Payment card AVS total failure
 `4000000000000127` | Payment card CVC failure 
# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "merchant_identity": "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("IDjAKAeJpcMnhjeANbdTkcht")
    .source("PIeq2wr8Mouvzym2BstDoBuj")
    .build()
);


```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```python


from payline.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeq2wr8Mouvzym2BstDoBuj", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:31.41Z",
  "updated_at" : "2017-03-28T03:41:31.46Z",
  "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : false,
  "expires_at" : "2017-04-04T03:41:31.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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
curl https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUsRDLf4ArvstWpwxxJnvk5D");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsRDLf4ArvstWpwxxJnvk5D');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUsRDLf4ArvstWpwxxJnvk5D")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUsRDLf4ArvstWpwxxJnvk5D")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRcH771hhEU9zxL8Z2qbsLsk",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:31.34Z",
  "updated_at" : "2017-03-28T03:41:32.10Z",
  "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : false,
  "expires_at" : "2017-04-04T03:41:31.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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

curl https://api-test.payline.io/authorizations/AUedRkeK2LSyTfhTUxEuoWoG \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```java
Authorization authorization = client.authorizationsClient().fetch(authorization.getId());
authorization.voidMe(true);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsRDLf4ArvstWpwxxJnvk5D');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUsRDLf4ArvstWpwxxJnvk5D")
authorization.void()

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUsRDLf4ArvstWpwxxJnvk5D")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AUedRkeK2LSyTfhTUxEuoWoG",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:34.11Z",
  "updated_at" : "2017-03-28T03:41:34.67Z",
  "trace_id" : "1726b507-9a02-4a1a-9442-0d13d40633e6",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : true,
  "expires_at" : "2017-04-04T03:41:34.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUedRkeK2LSyTfhTUxEuoWoG"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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

curl https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUsRDLf4ArvstWpwxxJnvk5D");

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsRDLf4ArvstWpwxxJnvk5D');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUsRDLf4ArvstWpwxxJnvk5D")
```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUsRDLf4ArvstWpwxxJnvk5D")


```
> Example Response:

```json
{
  "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRcH771hhEU9zxL8Z2qbsLsk",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:31.34Z",
  "updated_at" : "2017-03-28T03:41:32.10Z",
  "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "is_void" : false,
  "expires_at" : "2017-04-04T03:41:31.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

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
use Payline\Resources\Authorization;

$authorizations = Authorization::getPagination("/authorizations");


```
```python


from payline.resources import Authorization

authorization = Authorization.get()
```
```ruby
authorizations = Payline::Authorization.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUedRkeK2LSyTfhTUxEuoWoG",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:34.11Z",
      "updated_at" : "2017-03-28T03:41:34.67Z",
      "trace_id" : "1726b507-9a02-4a1a-9442-0d13d40633e6",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "is_void" : true,
      "expires_at" : "2017-04-04T03:41:34.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUedRkeK2LSyTfhTUxEuoWoG"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        }
      }
    }, {
      "id" : "AUsRDLf4ArvstWpwxxJnvk5D",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRcH771hhEU9zxL8Z2qbsLsk",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:31.34Z",
      "updated_at" : "2017-03-28T03:41:32.10Z",
      "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "is_void" : false,
      "expires_at" : "2017-04-04T03:41:31.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUsRDLf4ArvstWpwxxJnvk5D"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
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
```php
<?php
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Diaz", 
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


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Sean", 
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
	}).save()
```
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Sean", 
	        "last_name"=> "Diaz", 
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
  "id" : "IDuN9GzXzE8gnB3zM4iLgb4H",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-03-28T03:41:25.91Z",
  "updated_at" : "2017-03-28T03:41:25.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
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
	        "ownership_type": "PRIVATE", 
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
```java

import io.payline.payments.processing.client.model.Address;
import io.payline.payments.processing.client.model.BankAccountType;
import io.payline.payments.processing.client.model.BusinessType;
import io.payline.payments.processing.client.model.Date;
import io.payline.payments.processing.client.model.Entity;
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
        .dob(Date.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1000l)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .defaultStatementDescriptor("Business Inc")
        .incorporationDate(Date.builder()
          .day(1)
          .month(12)
          .year(2012)
          .build()
        )
        .principalPercentageOwnership(51)
        .build()
    )
    .build()
);

```
```php
<?php
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
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
	        "ownership_type"=> "PRIVATE", 
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": True, 
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
	        "ownership_type": "PRIVATE", 
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
	}).save()
```
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Bobs Burgers", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.BobsBurgers.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDjAKAeJpcMnhjeANbdTkcht",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T03:41:18.94Z",
  "updated_at" : "2017-03-28T03:41:18.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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

curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDjAKAeJpcMnhjeANbdTkcht");

```
```php
<?php
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
```
```python


from payline.resources import Identity
identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")

```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")


```
> Example Response:

```json
{
  "id" : "IDjAKAeJpcMnhjeANbdTkcht",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T03:41:18.93Z",
  "updated_at" : "2017-03-28T03:41:18.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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

## List all Identities
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71


```
```java
import io.payline.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
```php
<?php
use Payline\Resources\Identity;

$identities= Identity::getPagination("/identities");


```
```python


from payline.resources import Identity
identity = Identity.get()

```
```ruby
identities = Payline::Identity.retrieve


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDuN9GzXzE8gnB3zM4iLgb4H",
      "entity" : {
        "title" : null,
        "first_name" : "Sean",
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
        "ownership_type" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2017-03-28T03:41:25.89Z",
      "updated_at" : "2017-03-28T03:41:25.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "ID8sWF18TKXmzHov5KzYJJPC",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:23.59Z",
      "updated_at" : "2017-03-28T03:41:23.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8sWF18TKXmzHov5KzYJJPC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDpLmCYUz2y1sd9fBf4VoFVK",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:23.03Z",
      "updated_at" : "2017-03-28T03:41:23.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpLmCYUz2y1sd9fBf4VoFVK/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDc7QroXgK68fMrweJUeYhHp",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:22.53Z",
      "updated_at" : "2017-03-28T03:41:22.53Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDc7QroXgK68fMrweJUeYhHp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDggXZDmJt2BMVHy78Kh9cZb",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:22.11Z",
      "updated_at" : "2017-03-28T03:41:22.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDggXZDmJt2BMVHy78Kh9cZb/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDbPLE1JpAoNTR4PnYfqvp2V",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:21.62Z",
      "updated_at" : "2017-03-28T03:41:21.62Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDbPLE1JpAoNTR4PnYfqvp2V/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDoiHb5q9DF6X18FyXVpiykn",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:21.18Z",
      "updated_at" : "2017-03-28T03:41:21.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoiHb5q9DF6X18FyXVpiykn/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDdrbp779SvsBkPaQU8tQSjK",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:20.58Z",
      "updated_at" : "2017-03-28T03:41:20.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDdrbp779SvsBkPaQU8tQSjK/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "ID5GxQhqZG7wsQk23jcswrQb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:19.83Z",
      "updated_at" : "2017-03-28T03:41:19.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID5GxQhqZG7wsQk23jcswrQb/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "ID691sSZwVAA333j8vPo1PzT",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:19.38Z",
      "updated_at" : "2017-03-28T03:41:19.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID691sSZwVAA333j8vPo1PzT/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDjAKAeJpcMnhjeANbdTkcht",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T03:41:18.93Z",
      "updated_at" : "2017-03-28T03:41:18.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "IDoSP8BhmrXvshLR31gPQFAC",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Google"
      },
      "created_at" : "2017-03-28T03:41:15.34Z",
      "updated_at" : "2017-03-28T03:41:15.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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


## Update an Identity
```shell
curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Curry", 
	        "title": "CTO", 
	        "dob": {
	            "year": 1988, 
	            "day": 2, 
	            "month": 5
	        }, 
	        "ownership_type": "PRIVATE", 
	        "has_accepted_credit_cards_previously": true, 
	        "mcc": "0742", 
	        "phone": "7144177878", 
	        "business_tax_id": "123456789", 
	        "max_transaction_amount": 1200000, 
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
```java

```
```php
<?php

```
```python



```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDjAKAeJpcMnhjeANbdTkcht",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Curry",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Dunder Mifflin"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-03-28T03:41:18.93Z",
  "updated_at" : "2017-03-28T03:41:43.77Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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

curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java

import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Payline\Resources\Identity;
use Payline\Resources\Merchant;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")

merchant = identity.provision_merchant
```

> Example Response:

```json
{
  "id" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "verification" : "VI2i9MffNqwgBoJacMSUm6Fv",
  "merchant_profile" : "MPszfxydK2dpFsLQy698Vpia",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T03:41:25.13Z",
  "updated_at" : "2017-03-28T03:41:25.13Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPszfxydK2dpFsLQy698Vpia"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VI2i9MffNqwgBoJacMSUm6Fv"
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

`POST https://api-test.payline.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Payline\Resources\Identity;
use Payline\Resources\Merchant;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Payline::Identity.retrieve(:id => "MUanEA7cH6uotyBSTBsnUYK8")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "verification" : "VI2i9MffNqwgBoJacMSUm6Fv",
  "merchant_profile" : "MPszfxydK2dpFsLQy698Vpia",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T03:41:25.13Z",
  "updated_at" : "2017-03-28T03:41:25.13Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPszfxydK2dpFsLQy698Vpia"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VI2i9MffNqwgBoJacMSUm6Fv"
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
curl https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUanEA7cH6uotyBSTBsnUYK8");

```
```php
<?php
use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUanEA7cH6uotyBSTBsnUYK8');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUanEA7cH6uotyBSTBsnUYK8")

```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUanEA7cH6uotyBSTBsnUYK8")

```
> Example Response:

```json
{
  "id" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "verification" : null,
  "merchant_profile" : "MPszfxydK2dpFsLQy698Vpia",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-03-28T03:41:25.09Z",
  "updated_at" : "2017-03-28T03:41:25.22Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPszfxydK2dpFsLQy698Vpia"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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

## Reattempt Merchant Provisioning
```shell
curl https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUanEA7cH6uotyBSTBsnUYK8");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUanEA7cH6uotyBSTBsnUYK8');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUanEA7cH6uotyBSTBsnUYK8")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIqNY17m1JsssvM89s3F9WCg",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-28T03:41:44.31Z",
  "updated_at" : "2017-03-28T03:41:44.32Z",
  "trace_id" : "06a24da2-be02-48d6-af30-7d9087461af8",
  "payment_instrument" : null,
  "merchant" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIqNY17m1JsssvM89s3F9WCg"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
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

## Update Info on Processor
```shell
curl https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '{}'

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUanEA7cH6uotyBSTBsnUYK8');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUanEA7cH6uotyBSTBsnUYK8")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIqNY17m1JsssvM89s3F9WCg",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-28T03:41:44.31Z",
  "updated_at" : "2017-03-28T03:41:44.32Z",
  "trace_id" : "06a24da2-be02-48d6-af30-7d9087461af8",
  "payment_instrument" : null,
  "merchant" : "MUanEA7cH6uotyBSTBsnUYK8",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIqNY17m1JsssvM89s3F9WCg"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
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

## List all Merchants
```shell
curl https://api-test.payline.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java

```
```php
<?php
use Payline\Resources\Merchant;

$merchants = Merchant::getPagination("/merchants");


```
```python


from payline.resources import Merchant
merchant = Merchant.get()

```
```ruby
merchants = Payline::Merchant.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUanEA7cH6uotyBSTBsnUYK8",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "verification" : null,
      "merchant_profile" : "MPszfxydK2dpFsLQy698Vpia",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-03-28T03:41:25.09Z",
      "updated_at" : "2017-03-28T03:41:25.22Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPszfxydK2dpFsLQy698Vpia"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
curl https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUanEA7cH6uotyBSTBsnUYK8');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUanEA7cH6uotyBSTBsnUYK8")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VI2i9MffNqwgBoJacMSUm6Fv",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-03-28T03:41:25.09Z",
      "updated_at" : "2017-03-28T03:41:25.27Z",
      "trace_id" : "b553bdbd-2ca8-4391-9f2e-49b5363cb268",
      "payment_instrument" : null,
      "merchant" : "MUanEA7cH6uotyBSTBsnUYK8",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/verifications/VI2i9MffNqwgBoJacMSUm6Fv"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUanEA7cH6uotyBSTBsnUYK8/verifications?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
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




# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Create a Card
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "name": "Laura Green", 
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
	    "identity": "IDuN9GzXzE8gnB3zM4iLgb4H"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentCard;
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Green", 
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
	    "identity"=> "IDuN9GzXzE8gnB3zM4iLgb4H"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Green", 
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
	    "identity": "IDuN9GzXzE8gnB3zM4iLgb4H"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Laura Green", 
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
	    "identity"=> "IDuN9GzXzE8gnB3zM4iLgb4H"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeq2wr8Mouvzym2BstDoBuj",
  "fingerprint" : "FPR1101267070",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Green",
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
  "created_at" : "2017-03-28T03:41:26.36Z",
  "updated_at" : "2017-03-28T03:41:26.36Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuN9GzXzE8gnB3zM4iLgb4H",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/updates"
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
form](#embedded-tokenization)

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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
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
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
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
use Payline\Resources\Identity;
use Payline\Resources\BankAccount;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
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
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
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
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}).save()
```
```ruby
bank_account = Payline::BankAccount.new(
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
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2c8hJ1P8U3oH5YaSbZydia",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T03:41:24.08Z",
  "updated_at" : "2017-03-28T03:41:24.08Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
## Associate a Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TK2LN5pE7NjyCL7Ecbn9aZ9s")
    .identity("IDjAKAeJpcMnhjeANbdTkcht")
    .build()
);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type": "TOKEN", 
	    "identity": "IDjAKAeJpcMnhjeANbdTkcht"
	}).save()
```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK2LN5pE7NjyCL7Ecbn9aZ9s", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDjAKAeJpcMnhjeANbdTkcht"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2LN5pE7NjyCL7Ecbn9aZ9s",
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
  "created_at" : "2017-03-28T03:41:33.60Z",
  "updated_at" : "2017-03-28T03:41:33.60Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/updates"
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


## Fetch a Bank Account

```shell
curl https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PI2c8hJ1P8U3oH5YaSbZydia")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PI2c8hJ1P8U3oH5YaSbZydia');

```
```python



```
```ruby
bank_account = Payline::BankAccount.retrieve(:id=> "PI2c8hJ1P8U3oH5YaSbZydia")

```
> Example Response:

```json
{
  "id" : "PI2c8hJ1P8U3oH5YaSbZydia",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T03:41:24.05Z",
  "updated_at" : "2017-03-28T03:41:24.53Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `BANK_ACCOUNT`

#### HTTP Request

`GET https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Fetch a Credit Card
```shell
curl https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIeq2wr8Mouvzym2BstDoBuj")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIeq2wr8Mouvzym2BstDoBuj');

```
```python



```
```ruby
card = Payline::PaymentCard.retrieve(:id=> "PIeq2wr8Mouvzym2BstDoBuj")


```
> Example Response:

```json
{
  "id" : "PIeq2wr8Mouvzym2BstDoBuj",
  "fingerprint" : "FPR1101267070",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Green",
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
  "created_at" : "2017-03-28T03:41:26.33Z",
  "updated_at" : "2017-03-28T03:41:31.44Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuN9GzXzE8gnB3zM4iLgb4H",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Check for Card Updates

```shell
curl https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "merchant": "MUanEA7cH6uotyBSTBsnUYK8"
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

```
> Example Response:

```json
{
  "id" : "IUvjrSe7D6eNsyqELTeTLquc",
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "merchant" : "MUanEA7cH6uotyBSTBsnUYK8",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-03-28T03:41:35.21Z",
  "updated_at" : "2017-03-28T03:41:35.23Z",
  "payment_instrument" : "PIeq2wr8Mouvzym2BstDoBuj",
  "trace_id" : "6b119244-8f5c-4657-b691-075c722d6b69",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/updates/IUvjrSe7D6eNsyqELTeTLquc"
    },
    "payment_instrument" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    }
  }
}
```

#### HTTP Request

`POST https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID/updates/`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant` 
:PAYMENT_INSTRUMENT_ID | *string*, **required** | ID of the `Payment Instrument`




## List all Payment Instruments

```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71
```
```java
import io.payline.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
```python



```
```ruby
payment_instruments = Payline::PaymentInstruments.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI2LN5pE7NjyCL7Ecbn9aZ9s",
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
      "created_at" : "2017-03-28T03:41:33.56Z",
      "updated_at" : "2017-03-28T03:41:33.56Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2LN5pE7NjyCL7Ecbn9aZ9s/updates"
        }
      }
    }, {
      "id" : "PI8AXi8fVZ9QbupatsKY6duy",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-28T03:41:26.76Z",
      "updated_at" : "2017-03-28T03:41:26.76Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDuN9GzXzE8gnB3zM4iLgb4H",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PIeq2wr8Mouvzym2BstDoBuj",
      "fingerprint" : "FPR1101267070",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Laura Green",
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
      "created_at" : "2017-03-28T03:41:26.33Z",
      "updated_at" : "2017-03-28T03:41:31.44Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDuN9GzXzE8gnB3zM4iLgb4H",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDuN9GzXzE8gnB3zM4iLgb4H"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj/updates"
        }
      }
    }, {
      "id" : "PIbJgzPFUuGKcjaWmXhChfv",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:25.09Z",
      "updated_at" : "2017-03-28T03:41:25.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbJgzPFUuGKcjaWmXhChfv"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbJgzPFUuGKcjaWmXhChfv/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbJgzPFUuGKcjaWmXhChfv/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbJgzPFUuGKcjaWmXhChfv/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PIa8YTQHXapmBR1UYWRDYZwx",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:25.09Z",
      "updated_at" : "2017-03-28T03:41:25.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIa8YTQHXapmBR1UYWRDYZwx"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIa8YTQHXapmBR1UYWRDYZwx/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIa8YTQHXapmBR1UYWRDYZwx/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIa8YTQHXapmBR1UYWRDYZwx/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:25.09Z",
      "updated_at" : "2017-03-28T03:41:25.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PI2c8hJ1P8U3oH5YaSbZydia",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-28T03:41:24.05Z",
      "updated_at" : "2017-03-28T03:41:24.53Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PImAcj1gZc6hQkxuFf1t7NtU",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:16.25Z",
      "updated_at" : "2017-03-28T03:41:16.25Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PIf3scJdzMgyvQNALwqD12JH",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:16.25Z",
      "updated_at" : "2017-03-28T03:41:16.25Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoSP8BhmrXvshLR31gPQFAC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PIeqQrRPBexvkLwQ55C3Yb1F",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:16.25Z",
      "updated_at" : "2017-03-28T03:41:16.25Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoSP8BhmrXvshLR31gPQFAC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeqQrRPBexvkLwQ55C3Yb1F"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeqQrRPBexvkLwQ55C3Yb1F/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeqQrRPBexvkLwQ55C3Yb1F/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeqQrRPBexvkLwQ55C3Yb1F/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        }
      }
    }, {
      "id" : "PI3tmp46VJHFz8e9Ckc6Wxrw",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T03:41:16.25Z",
      "updated_at" : "2017-03-28T03:41:16.25Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDoSP8BhmrXvshLR31gPQFAC",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3tmp46VJHFz8e9Ckc6Wxrw"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3tmp46VJHFz8e9Ckc6Wxrw/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3tmp46VJHFz8e9Ckc6Wxrw/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3tmp46VJHFz8e9Ckc6Wxrw/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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

curl https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

```
```php
<?php
use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDjAKAeJpcMnhjeANbdTkcht');
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


from payline.resources import Identity
from payline.resources import Settlement

identity = Identity.get(id="IDjAKAeJpcMnhjeANbdTkcht")
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
identity = Payline::Identity.retrieve(:id=>"IDjAKAeJpcMnhjeANbdTkcht")
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
  "id" : "STopQZHHosXutaEf9AUJW3qi",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "currency" : "USD",
  "created_at" : "2017-03-28T03:42:37.41Z",
  "updated_at" : "2017-03-28T03:42:37.42Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1416170,
  "total_fees" : 141618,
  "total_fee" : 141618,
  "net_amount" : 1274552,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=debit"
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


curl https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STopQZHHosXutaEf9AUJW3qi");

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STopQZHHosXutaEf9AUJW3qi');

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STopQZHHosXutaEf9AUJW3qi")

```
> Example Response:

```json
{
  "id" : "STopQZHHosXutaEf9AUJW3qi",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "currency" : "USD",
  "created_at" : "2017-03-28T03:42:37.36Z",
  "updated_at" : "2017-03-28T03:42:38.55Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1416170,
  "total_fees" : 141618,
  "total_fee" : 141618,
  "net_amount" : 1274552,
  "destination" : "PI2c8hJ1P8U3oH5YaSbZydia",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=debit"
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


## List all Settlements
```shell
curl https://api-test.payline.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

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
use Payline\Resources\Settlement;

$settlements = Settlement::getPagination("/settlements");


```
```python


from payline.resources import Settlement
settlements = Settlement.get()

```
```ruby
settlements = Payline::Settlement.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STopQZHHosXutaEf9AUJW3qi",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "currency" : "USD",
      "created_at" : "2017-03-28T03:42:37.36Z",
      "updated_at" : "2017-03-28T03:42:38.55Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 1416170,
      "total_fees" : 141618,
      "total_fee" : 141618,
      "net_amount" : 1274552,
      "destination" : "PI2c8hJ1P8U3oH5YaSbZydia",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

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
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STopQZHHosXutaEf9AUJW3qi');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STopQZHHosXutaEf9AUJW3qi")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRoj8yxNLkokrHHLEXKg7vPm",
      "amount" : 1274552,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "625b7091-d610-4834-b5c9-147cca9297d6",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PI2c8hJ1P8U3oH5YaSbZydia",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:38.02Z",
      "updated_at" : "2017-03-28T03:42:38.35Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRoj8yxNLkokrHHLEXKg7vPm"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRoj8yxNLkokrHHLEXKg7vPm/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRoj8yxNLkokrHHLEXKg7vPm/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRoj8yxNLkokrHHLEXKg7vPm/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRoj8yxNLkokrHHLEXKg7vPm/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2c8hJ1P8U3oH5YaSbZydia"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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


## List Transfers in a Settlement
```shell

curl https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STopQZHHosXutaEf9AUJW3qi');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STopQZHHosXutaEf9AUJW3qi")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRRSykv7ZSMvCyGCYD9GEj",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "a9d15db9-cf47-4663-8cd7-7d6af4733774",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PImAcj1gZc6hQkxuFf1t7NtU",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:36.70Z",
      "updated_at" : "2017-03-28T03:42:36.91Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRRSykv7ZSMvCyGCYD9GEj"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRRSykv7ZSMvCyGCYD9GEj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRRSykv7ZSMvCyGCYD9GEj/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRRSykv7ZSMvCyGCYD9GEj/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRRSykv7ZSMvCyGCYD9GEj/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU"
        }
      }
    }, {
      "id" : "TRsZkbgUKhyZzYZpHspvXfzP",
      "amount" : 89790,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "e6de71a3-a9c6-4a1d-a907-31c61c100b0f",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PIf3scJdzMgyvQNALwqD12JH",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:36.43Z",
      "updated_at" : "2017-03-28T03:42:36.66Z",
      "merchant_identity" : "IDoSP8BhmrXvshLR31gPQFAC",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRsZkbgUKhyZzYZpHspvXfzP"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRsZkbgUKhyZzYZpHspvXfzP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRsZkbgUKhyZzYZpHspvXfzP/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRsZkbgUKhyZzYZpHspvXfzP/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRsZkbgUKhyZzYZpHspvXfzP/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH"
        }
      }
    }, {
      "id" : "TRkVCCzv7QJ6AeyNPVMLZmSi",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "ef0ce20f-0764-4d6f-be21-2ac59426bc06",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PImAcj1gZc6hQkxuFf1t7NtU",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:36.19Z",
      "updated_at" : "2017-03-28T03:42:36.41Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRkVCCzv7QJ6AeyNPVMLZmSi"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRkVCCzv7QJ6AeyNPVMLZmSi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRkVCCzv7QJ6AeyNPVMLZmSi/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRkVCCzv7QJ6AeyNPVMLZmSi/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRkVCCzv7QJ6AeyNPVMLZmSi/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU"
        }
      }
    }, {
      "id" : "TRxhU5P6NcBoB4txLxLaMVZ1",
      "amount" : 51795,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "7a19c488-784d-4daa-8eb8-ac54f640ec5b",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PIf3scJdzMgyvQNALwqD12JH",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:35.90Z",
      "updated_at" : "2017-03-28T03:42:36.14Z",
      "merchant_identity" : "IDoSP8BhmrXvshLR31gPQFAC",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRxhU5P6NcBoB4txLxLaMVZ1"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRxhU5P6NcBoB4txLxLaMVZ1/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDoSP8BhmrXvshLR31gPQFAC"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRxhU5P6NcBoB4txLxLaMVZ1/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRxhU5P6NcBoB4txLxLaMVZ1/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRxhU5P6NcBoB4txLxLaMVZ1/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIf3scJdzMgyvQNALwqD12JH"
        }
      }
    }, {
      "id" : "TRwQ3Sf1W3fLMF6j1imFEzQs",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "f85a6767-9e86-4407-af54-4974fc0326c2",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PImAcj1gZc6hQkxuFf1t7NtU",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:42:35.62Z",
      "updated_at" : "2017-03-28T03:42:35.88Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRwQ3Sf1W3fLMF6j1imFEzQs"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRwQ3Sf1W3fLMF6j1imFEzQs/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRwQ3Sf1W3fLMF6j1imFEzQs/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRwQ3Sf1W3fLMF6j1imFEzQs/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRwQ3Sf1W3fLMF6j1imFEzQs/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImAcj1gZc6hQkxuFf1t7NtU"
        }
      }
    }, {
      "id" : "TRcH771hhEU9zxL8Z2qbsLsk",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:31.95Z",
      "updated_at" : "2017-03-28T03:42:02.41Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    }, {
      "id" : "TR2BmEGCnMVJTjB85KCHYW2d",
      "amount" : 518057,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "117acf43-a7d4-43b0-bb9e-c82a10354ebe",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PI8AXi8fVZ9QbupatsKY6duy",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 51806,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:28.01Z",
      "updated_at" : "2017-03-28T03:42:02.98Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    }, {
      "id" : "TR74sWgBFXDGEcQejHFvCoLs",
      "amount" : 898013,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "19772ef4-887a-456f-a472-4ebb385500d8",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : "2017-03-28T03:42:35.54Z",
      "fee" : 89801,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:27.25Z",
      "updated_at" : "2017-03-28T03:42:01.81Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STopQZHHosXutaEf9AUJW3qi/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 8
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

- **CANCELED:** Created, and then reversed before transfer has transitioned to succeeded

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

`ready_to_settle_at` field can have 2 possible values:

1. `null`: Funds have been captured, but are not yet ready to be paid out
2. `TIMESTAMP`: A UTC timestamp that specifies when the funds will be available to be payout out. Once in the past, the Transfer will be eligible for inclusion in a batch Settlement.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
	{
	    "fee": 51806, 
	    "source": "PI8AXi8fVZ9QbupatsKY6duy", 
	    "merchant_identity": "IDjAKAeJpcMnhjeANbdTkcht", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 518057
	}'


```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDjAKAeJpcMnhjeANbdTkcht")
      .source("PIeq2wr8Mouvzym2BstDoBuj")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```
```php
<?php
use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 89801, 
	    "source"=> "PIeq2wr8Mouvzym2BstDoBuj", 
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 898013
	));
$debit = $debit->save();
```
```python



```
```ruby
Payline::Transfer.new(
	{
	    "fee"=> 51806, 
	    "source"=> "PI8AXi8fVZ9QbupatsKY6duy", 
	    "merchant_identity"=> "IDjAKAeJpcMnhjeANbdTkcht", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "currency"=> "USD", 
	    "amount"=> 518057
	}}).save
```


> Example Response:

```json
{
  "id" : "TR2BmEGCnMVJTjB85KCHYW2d",
  "amount" : 518057,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "117acf43-a7d4-43b0-bb9e-c82a10354ebe",
  "currency" : "USD",
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "source" : "PI8AXi8fVZ9QbupatsKY6duy",
  "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
  "ready_to_settle_at" : null,
  "fee" : 51806,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:28.06Z",
  "updated_at" : "2017-03-28T03:41:28.14Z",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
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
source | *string*, **required** | ID of the `Payment Instrument` that will be debited
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be debited in cents (e.g. 100 cents to debit $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR74sWgBFXDGEcQejHFvCoLs");

```
```php
<?php
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TR74sWgBFXDGEcQejHFvCoLs');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TR74sWgBFXDGEcQejHFvCoLs")

```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TR74sWgBFXDGEcQejHFvCoLs")

```
> Example Response:

```json
{
  "id" : "TR74sWgBFXDGEcQejHFvCoLs",
  "amount" : 898013,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "19772ef4-887a-456f-a472-4ebb385500d8",
  "currency" : "USD",
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "source" : "PIeq2wr8Mouvzym2BstDoBuj",
  "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
  "ready_to_settle_at" : null,
  "fee" : 89801,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:27.25Z",
  "updated_at" : "2017-03-28T03:41:27.39Z",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
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

curl https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
```php
<?php
use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TR74sWgBFXDGEcQejHFvCoLs');
$refund = $debit->reverse(11);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TR74sWgBFXDGEcQejHFvCoLs")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TR74sWgBFXDGEcQejHFvCoLs")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TR6yvAF5qparhpfCCEkdwUhq",
  "amount" : 166770,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "2d07bbf7-9245-4966-8326-5912a6f73ad8",
  "currency" : "USD",
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
  "destination" : "PIeq2wr8Mouvzym2BstDoBuj",
  "ready_to_settle_at" : null,
  "fee" : 16677,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T03:41:30.64Z",
  "updated_at" : "2017-03-28T03:41:30.73Z",
  "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR6yvAF5qparhpfCCEkdwUhq"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR6yvAF5qparhpfCCEkdwUhq/payment_instruments"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java
import io.payline.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
```php
<?php
use Payline\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


```
```python


from payline.resources import Transfer
transfer = Transfer.get()

```
```ruby
transfers = Payline::Transfer.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRcH771hhEU9zxL8Z2qbsLsk",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "8b34e9da-4c8b-4163-96d5-c2ba209dc823",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:31.95Z",
      "updated_at" : "2017-03-28T03:41:32.10Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRcH771hhEU9zxL8Z2qbsLsk/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    }, {
      "id" : "TR6yvAF5qparhpfCCEkdwUhq",
      "amount" : 166770,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c1c879d5-38b1-4b77-a498-41955c4cbbe0",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "destination" : "PIeq2wr8Mouvzym2BstDoBuj",
      "ready_to_settle_at" : null,
      "fee" : 16677,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:30.50Z",
      "updated_at" : "2017-03-28T03:41:30.73Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR6yvAF5qparhpfCCEkdwUhq"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR6yvAF5qparhpfCCEkdwUhq/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        }
      }
    }, {
      "id" : "TRqdScmTeRKV5F3F4s8PeAGy",
      "amount" : 166770,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "77cb4811-8e29-4fff-8d92-21be566aa470",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : null,
      "fee" : 16677,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:29.95Z",
      "updated_at" : "2017-03-28T03:41:30.60Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRqdScmTeRKV5F3F4s8PeAGy/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    }, {
      "id" : "TR2BmEGCnMVJTjB85KCHYW2d",
      "amount" : 518057,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "117acf43-a7d4-43b0-bb9e-c82a10354ebe",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PI8AXi8fVZ9QbupatsKY6duy",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : null,
      "fee" : 51806,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:28.01Z",
      "updated_at" : "2017-03-28T03:41:28.14Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR2BmEGCnMVJTjB85KCHYW2d/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8AXi8fVZ9QbupatsKY6duy"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
        }
      }
    }, {
      "id" : "TR74sWgBFXDGEcQejHFvCoLs",
      "amount" : 898013,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "19772ef4-887a-456f-a472-4ebb385500d8",
      "currency" : "USD",
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "source" : "PIeq2wr8Mouvzym2BstDoBuj",
      "destination" : "PIgp7jp8qZZ91tEgeG3KgK8R",
      "ready_to_settle_at" : null,
      "fee" : 89801,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T03:41:27.25Z",
      "updated_at" : "2017-03-28T03:41:27.39Z",
      "merchant_identity" : "IDjAKAeJpcMnhjeANbdTkcht",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjAKAeJpcMnhjeANbdTkcht"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR74sWgBFXDGEcQejHFvCoLs/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeq2wr8Mouvzym2BstDoBuj"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgp7jp8qZZ91tEgeG3KgK8R"
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
    "count" : 5
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/transfers`
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
    -u USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
```php
<?php
use Payline\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
$webhook = $webhook->save();

```
```python


from payline.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```ruby
webhook = Payline::Webhook.new(
                    {
                    "url" => "http=>//requestb.in/1jb5zu11"
                    }
                ).save
```
> Example Response:

```json
{
  "id" : "WH6KgAWAbaxwHwgyf3xqQQRB",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "created_at" : "2017-03-28T03:41:18.58Z",
  "updated_at" : "2017-03-28T03:41:18.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WH6KgAWAbaxwHwgyf3xqQQRB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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



curl https://api-test.payline.io/webhooks/WH6KgAWAbaxwHwgyf3xqQQRB \
    -H "Content-Type: application/vnd.json+api" \
    -u USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH6KgAWAbaxwHwgyf3xqQQRB");

```
```php
<?php
use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WH6KgAWAbaxwHwgyf3xqQQRB');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WH6KgAWAbaxwHwgyf3xqQQRB")

```
```ruby
webhook = Payline::Webhook.retrieve(:id=> "WH6KgAWAbaxwHwgyf3xqQQRB")


```
> Example Response:

```json
{
  "id" : "WH6KgAWAbaxwHwgyf3xqQQRB",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APueARWWD8YjyYDUDx5ZiguK",
  "created_at" : "2017-03-28T03:41:18.58Z",
  "updated_at" : "2017-03-28T03:41:18.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WH6KgAWAbaxwHwgyf3xqQQRB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
    -u  USp1kfJp3wqYRm7txAM1PmBG:ff9b1de8-d2b5-4555-b049-7f44923daf71

```
```java
import io.payline.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
```php
<?php
use Payline\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


```
```python


from payline.resources import Webhook
webhooks = Webhook.get()

```
```ruby
webhooks = Payline::Webhook.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WH6KgAWAbaxwHwgyf3xqQQRB",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APueARWWD8YjyYDUDx5ZiguK",
      "created_at" : "2017-03-28T03:41:18.58Z",
      "updated_at" : "2017-03-28T03:41:18.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WH6KgAWAbaxwHwgyf3xqQQRB"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APueARWWD8YjyYDUDx5ZiguK"
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
