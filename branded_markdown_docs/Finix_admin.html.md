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
of charging a card. This guide will walk you through provisioning merchant
accounts, tokenizing cards, charging those cards, and finally settling (i.e.
payout) those funds out to your merchants.

3. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 

4. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.finix.payments.processing.client</groupId>
  <artifactId>finix</artifactId>
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

import io.finix.payments.processing.client.ProcessingClient;
import io.finix.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("https://api-staging.finix.io");
  client.setupUserIdAndPassword("US7WwPZ8N8nGwt48GdeCmqoG", "09539f06-cdc1-43d2-beb6-4d58c9a0fc92");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');

Finix\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US7WwPZ8N8nGwt48GdeCmqoG',
	"password" => '09539f06-cdc1-43d2-beb6-4d58c9a0fc92']
	);

require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("US7WwPZ8N8nGwt48GdeCmqoG", "09539f06-cdc1-43d2-beb6-4d58c9a0fc92"))

```
```ruby
# To download the Ruby gem:
# gem install finix

require 'finix'

Finix.configure(
    :root_url => 'https://api-staging.finix.io',
    :user=>'US7WwPZ8N8nGwt48GdeCmqoG',
    :password => '09539f06-cdc1-43d2-beb6-4d58c9a0fc92'
)
```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US7WwPZ8N8nGwt48GdeCmqoG`

- Password: `09539f06-cdc1-43d2-beb6-4d58c9a0fc92`

- Application ID: `AP22AGPHEqD1fwgycz9DaTYk`

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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

import io.finix.payments.processing.client.model.Address;
import io.finix.payments.processing.client.model.BankAccountType;
import io.finix.payments.processing.client.model.BusinessType;
import io.finix.payments.processing.client.model.Date;
import io.finix.payments.processing.client.model.Entity;
import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .title("CEO")
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
        .ownershipType("PRIVATE")
        .hasAcceptedCreditCardsPreviously(false)
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


from finix.resources import Identity

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
identity = Finix::Identity.new(
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
  "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
  "created_at" : "2017-04-17T23:48:38.85Z",
  "updated_at" : "2017-04-17T23:48:38.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-staging.finix.io/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDfNKgun2WNruSqAPBFYXaXz"
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

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
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
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
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
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
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
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	}).save
```
> Example Response:

```json
{
  "id" : "PIcgLj6AecVH1XbMpZpCF4Td",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:48:42.65Z",
  "updated_at" : "2017-04-17T23:48:42.65Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
name | *string*, **required** | Account owner's full name (max 40 characters)
### Step 3: Provision Merchant Account

```shell
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDfNKgun2WNruSqAPBFYXaXz")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDfNKgun2WNruSqAPBFYXaXz")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "verification" : "VI5fgYrVj3pNEFyBsUVqhS45",
  "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:43.69Z",
  "updated_at" : "2017-04-17T23:48:43.69Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI5fgYrVj3pNEFyBsUVqhS45"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ayisha", 
	        "last_name": "Le", 
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
use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Ayisha", 
	        "last_name"=> "Le", 
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
	        "first_name": "Ayisha", 
	        "last_name": "Le", 
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
	        "first_name"=> "Ayisha", 
	        "last_name"=> "Le", 
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
  "id" : "ID3xkAW9p2qaQRdCvNo8cchE",
  "entity" : {
    "title" : null,
    "first_name" : "Ayisha",
    "last_name" : "Le",
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
  "created_at" : "2017-04-17T23:48:44.45Z",
  "updated_at" : "2017-04-17T23:48:44.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

Now that we have successfully provisioned a `Merchant` we'll need to create an
`Identity` that represents your buyer. Don't worry though you won't need to capture
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 5: Tokenize a Card
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "name": "Walter Henderson", 
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
	    "identity": "ID3xkAW9p2qaQRdCvNo8cchE"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDfNKgun2WNruSqAPBFYXaXz")
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

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Henderson", 
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
	    "identity"=> "ID3xkAW9p2qaQRdCvNo8cchE"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Henderson", 
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
	    "identity": "ID3xkAW9p2qaQRdCvNo8cchE"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Walter Henderson", 
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
	    "identity"=> "ID3xkAW9p2qaQRdCvNo8cchE"
	}).save
```
> Example Response:

```json
{
  "id" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "fingerprint" : "FPR739722504",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Henderson",
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
  "created_at" : "2017-04-17T23:48:44.85Z",
  "updated_at" : "2017-04-17T23:48:44.85Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3xkAW9p2qaQRdCvNo8cchE",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/updates"
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 6: Create an Authorization
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "merchant_identity": "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIw9KSQJAEiBMCdkeiYHm4kx", 
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
    .merchantIdentity("IDfNKgun2WNruSqAPBFYXaXz")
    .source("PIw9KSQJAEiBMCdkeiYHm4kx")
    .build()
);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIw9KSQJAEiBMCdkeiYHm4kx", 
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
	    "merchant_identity": "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIw9KSQJAEiBMCdkeiYHm4kx", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIw9KSQJAEiBMCdkeiYHm4kx", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUnmDrd5efjNpyrovvwb6PZn",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:50.71Z",
  "updated_at" : "2017-04-17T23:48:50.77Z",
  "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:48:50.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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
for your records so that we can capture those funds in the next step.


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
source | *string*, **required** | The buyer's `Payment Instrument` ID that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Capture the Authorization
```shell
curl https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnmDrd5efjNpyrovvwb6PZn");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUnmDrd5efjNpyrovvwb6PZn');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUnmDrd5efjNpyrovvwb6PZn")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUnmDrd5efjNpyrovvwb6PZn")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUnmDrd5efjNpyrovvwb6PZn",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7hEkZRcxzuCSiAAV6WCcUh",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:50.66Z",
  "updated_at" : "2017-04-17T23:48:51.52Z",
  "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:48:50.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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
 a 10% service fee you'll want to pass 1000 as the fee. This way when the
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

### Step 8: Create a Batch Settlement
```shell
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
);

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
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

identity = Identity.get(id="IDfNKgun2WNruSqAPBFYXaXz")
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
identity = Finix::Identity.retrieve(:id=>"IDfNKgun2WNruSqAPBFYXaXz")
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
  "id" : "SThZK4ge46CJV27dV3LDbyF4",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:52:11.62Z",
  "updated_at" : "2017-04-17T23:52:11.67Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1209845,
  "total_fees" : 120985,
  "total_fee" : 120985,
  "net_amount" : 1088860,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=debit"
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
Once a batch Settlement has been created it will undergo review and typically be
paid out within 24 hours.
</aside>

Note that for reconciliation purposes each `Settlement` contains a [transfers
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
### Step 1: Create a Recipient Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Michae", 
	        "last_name": "Chang", 
	        "email": "Michae@gmail.com", 
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

import io.finix.payments.processing.client.model.Address;
import io.finix.payments.processing.client.model.BankAccountType;
import io.finix.payments.processing.client.model.BusinessType;
import io.finix.payments.processing.client.model.Date;
import io.finix.payments.processing.client.model.Entity;
import io.finix.payments.processing.client.model.Identity;;

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
use Finix\Resources\Identity;

$identity = new Identity(IDwicRDJNVwHEwkmrX3CBJYj);
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
	        "phone": "7145677612", 
	        "first_name": "Michae", 
	        "last_name": "Chang", 
	        "email": "Michae@gmail.com", 
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
	        "phone"=> "7145677612", 
	        "first_name"=> "Michae", 
	        "last_name"=> "Chang", 
	        "email"=> "Michae@gmail.com", 
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
  "id" : "IDwicRDJNVwHEwkmrX3CBJYj",
  "entity" : {
    "title" : null,
    "first_name" : "Michae",
    "last_name" : "Chang",
    "email" : "Michae@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677612",
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
  "created_at" : "2017-04-17T23:52:21.93Z",
  "updated_at" : "2017-04-17T23:52:21.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APj7nxdkKFmjnNZUwWLnSUhX"
    }
  }
}
```

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 2:  Add a Payment Instrument for the Recipient 

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "name": "Laura Jones", 
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
	    "identity": "IDwicRDJNVwHEwkmrX3CBJYj"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDfNKgun2WNruSqAPBFYXaXz")
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

$identity = Identity::retrieve('IDwicRDJNVwHEwkmrX3CBJYj');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Jones", 
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
	    "identity"=> "IDwicRDJNVwHEwkmrX3CBJYj"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Laura Jones", 
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
	    "identity"=> "IDwicRDJNVwHEwkmrX3CBJYj"
	}).save
```
> Example Response:

```json
{
  "id" : "PI2H7t8Wkr9VDW3uJz6yatSR",
  "fingerprint" : "FPR738669030",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Jones",
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
  "created_at" : "2017-04-17T23:52:22.32Z",
  "updated_at" : "2017-04-17T23:52:22.32Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwicRDJNVwHEwkmrX3CBJYj",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APj7nxdkKFmjnNZUwWLnSUhX"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR/updates"
    }
  }
}
```

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Now that we've created an `Identity` for our recipient, we'll need to tokenize a credit card where funds will be disbursed.

In the API, credit cards are represented by the `Payment Instrument` resource.

To classify the `Payment Instrument` as a credit card you'll need to pass `PAYMENT_CARD` in the type field of your request, and you'll also want to pass the ID of the `Identity` that you created in the last step via the identity field to properly associate it with your recipient.

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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 3: Provision Recipient Account
```shell
curl https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
Identity identity = client.identitiesClient().fetchResource("IDwicRDJNVwHEwkmrX3CBJYj");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDwicRDJNVwHEwkmrX3CBJYj');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDwicRDJNVwHEwkmrX3CBJYj")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUuirVRYErDX1MCbJPA7r7pE",
  "identity" : "IDwicRDJNVwHEwkmrX3CBJYj",
  "verification" : "VIvHRAcBR7SHFMrUtUFuEgrH",
  "merchant_profile" : "MPpA2nAAoQGTfrgkZY2H82ti",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:22.73Z",
  "updated_at" : "2017-04-17T23:52:22.73Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUuirVRYErDX1MCbJPA7r7pE"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUuirVRYErDX1MCbJPA7r7pE/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpA2nAAoQGTfrgkZY2H82ti"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APj7nxdkKFmjnNZUwWLnSUhX"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIvHRAcBR7SHFMrUtUFuEgrH"
    }
  }
}
```

Now that we've associated a Payment Instrument with our recipient's `Identity` we're ready to provision a Recipient account. This is the last step before you can begin paying out an Identity. Luckily you've already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource.

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor


### Step 4: Send Payout




```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PI2H7t8Wkr9VDW3uJz6yatSR", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
Map<String,String> tags = new HashMap<String,String>();
tags.put("order_number", "21DFASJSAKAS");

Transfer cardPayout = client.transfersClient().save(
  Transfer.builder()
    .tags(tags)
    .merchantIdentity(identity.getId())
    .destination(paymentCard.getId())
    .currency("USD")
    .amount(10000l)
    .processor("VISA_V1")
    .build()
);

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI2H7t8Wkr9VDW3uJz6yatSR", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$transfer = $transfer->save();
```
```python



```
```ruby
transfer = Finix::Transfer.new(
	{
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI2H7t8Wkr9VDW3uJz6yatSR", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "TRdVmy8Hjb3zJpfGazVnGw8P",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190855",
  "currency" : "USD",
  "application" : "APj7nxdkKFmjnNZUwWLnSUhX",
  "source" : "PIewCnhiuZZcJjSLACCs4jk5",
  "destination" : "PI2H7t8Wkr9VDW3uJz6yatSR",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:23.95Z",
  "updated_at" : "2017-04-17T23:52:26.42Z",
  "merchant_identity" : "IDwicRDJNVwHEwkmrX3CBJYj",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APj7nxdkKFmjnNZUwWLnSUhX"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRdVmy8Hjb3zJpfGazVnGw8P"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRdVmy8Hjb3zJpfGazVnGw8P/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwicRDJNVwHEwkmrX3CBJYj"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRdVmy8Hjb3zJpfGazVnGw8P/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRdVmy8Hjb3zJpfGazVnGw8P/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRdVmy8Hjb3zJpfGazVnGw8P/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIewCnhiuZZcJjSLACCs4jk5"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI2H7t8Wkr9VDW3uJz6yatSR"
    }
  }
}
```


Now the final step - time to payout the recipient!

Next you'll need to create a `Transfer`.  What's a `Transfer`? Glad you asked! A `Transfer` represents any flow of funds either to or from a Payment Instrument. In this case a Payout to a card.

To create a `Transfer` we'll simply supply the Payment Instrument ID of the previously tokenized card as the destination field. Also, be sure to note that the amount field is in cents.

Simple enough, right? You'll also want to store the ID from that `Transfer` for your records. `Transfers` can have two possible states SUCCEEDED and FAILED.


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

Before collecting the sensitive payment information, we will need to add a button
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
          applicationId: 'AP22AGPHEqD1fwgycz9DaTYk',
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
  "id" : "TK7ci8PhpqSGXsLKmi6ZeM21",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:48:52.96Z",
  "updated_at" : "2017-04-17T23:48:52.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:48:52.96Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;
import io.finix.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TK7ci8PhpqSGXsLKmi6ZeM21")
            .identity("IDfNKgun2WNruSqAPBFYXaXz")
    .build()
);
```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7ci8PhpqSGXsLKmi6ZeM21",
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
  "created_at" : "2017-04-17T23:48:53.48Z",
  "updated_at" : "2017-04-17T23:48:53.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/updates"
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


## Tokenization with Hosted Fields

### Library summary

The `SecureForm` library is a javascript library that allows you to integrate
secure fields with non-secure fields in your page. The secure fields behave like
traditional input fields while preventing access to the unsecured data.

Once the fields are initialized the library communicates the state of the fields
through a JavaScript callback. The state object includes information about the
validity, focused value and if the user has entered information in the field.

For a complete example of how to use the library please refer to this
[jsFiddle example](https://jsfiddle.net/rserna2010/Ls101sou/).

### Step 1: Include library

```html
 <script type="text/javascript" src="https://js.verygoodvault.com/js-vgfield-2/finix.js"></script>
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
    secureForm.submit('/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens', {
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
  "id" : "TK7ci8PhpqSGXsLKmi6ZeM21",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:48:52.96Z",
  "updated_at" : "2017-04-17T23:48:52.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:48:52.96Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}'

```
```java
import io.finix.payments.processing.client.model.PaymentCard;
import io.finix.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TK7ci8PhpqSGXsLKmi6ZeM21")
            .identity("IDfNKgun2WNruSqAPBFYXaXz")
    .build()
);
```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7ci8PhpqSGXsLKmi6ZeM21",
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
  "created_at" : "2017-04-17T23:48:53.48Z",
  "updated_at" : "2017-04-17T23:48:53.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/updates"
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

3. [Fees](#fees): A guide describing the four different pricing tiers

##Fees

You can find the live example of how fees are calculated in this [spreadsheet](https://docs.google.com/spreadsheets/d/1UFmKg7EvhlCduM31bQ3rOeslszOlO49rOw3frllBj9c/edit#gid=0)

### Case 1
- Fee profile not set
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.00 | $100.00 | $0.00 | $0.00 | $0.00 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.00 | $90.00 | $10.00 | $0.00 | $0.00 |

### Case 2
- Fee profile not set
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.11 | $90.00 | $9.89 | $0.11 | $0.11 |
| $100 | $0.10 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |

### Case 3
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.00 | $96.00 | $0.80 | $3.20 | $3.20 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.00 | $1.00 | $95.80 | $3.20 | $3.20 |

### Case 4
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.11 | $96.00 | $0.69 | $3.31 | $3.31 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.11 | $1.00 | $95.69 | $3.31 | $3.31 |

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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "UShascJpYqtfe9fxa9KSUHTP",
  "password" : "29b4afd7-055d-40c4-8442-3342cefe763a",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:34.63Z",
  "updated_at" : "2017-04-17T23:48:34.63Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UShascJpYqtfe9fxa9KSUHTP"
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
	        "application_name": "WePay"
	    }, 
	    "user": "UShascJpYqtfe9fxa9KSUHTP", 
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
	        "max_transaction_amount": 1200000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
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
use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "UShascJpYqtfe9fxa9KSUHTP", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:48:35.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
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
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "canDebitBankAccount": true, 
	        "key2": "value-2", 
	        "key1": "value-1"
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

```
> Example Response:

```json
{
  "id" : "PRbU3B5GZywdusHJLycNH7VG",
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "default_merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "created_at" : "2017-04-17T23:48:36.22Z",
  "updated_at" : "2017-04-17T23:48:36.22Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors/PRbU3B5GZywdusHJLycNH7VG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:52:18.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
### Step 5: Enable Settlement Functionality
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:52:19.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use Finix\Resources\Application;

$application = Application::retrieve('AP22AGPHEqD1fwgycz9DaTYk');

```
```python


from finix.resources import Application

application = Application.get(id="AP22AGPHEqD1fwgycz9DaTYk")
```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:48:37.89Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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

## Create an Application User
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'

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
  "id" : "USuT2XqryENsxHKtrQrBK5n2",
  "password" : "097c33df-7ca5-4cdb-9db9-537951084929",
  "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:36.90Z",
  "updated_at" : "2017-04-17T23:48:36.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USuT2XqryENsxHKtrQrBK5n2"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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

## Create an Application
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -d '
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "UShascJpYqtfe9fxa9KSUHTP", 
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
	        "max_transaction_amount": 1200000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
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
use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "UShascJpYqtfe9fxa9KSUHTP", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();

```
```python


from finix.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "UShascJpYqtfe9fxa9KSUHTP", 
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
	        "max_transaction_amount": 1200000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}).save()
```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:48:35.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
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
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:52:17.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "AP22AGPHEqD1fwgycz9DaTYk",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:48:35.68Z",
  "updated_at" : "2017-04-17T23:52:17.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
## [ADMIN] Enable the Dummy Processor (i.e. Sandbox)
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "canDebitBankAccount": true, 
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}

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
  "id" : "PRbU3B5GZywdusHJLycNH7VG",
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "default_merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "created_at" : "2017-04-17T23:48:36.22Z",
  "updated_at" : "2017-04-17T23:48:36.22Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors/PRbU3B5GZywdusHJLycNH7VG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java

```
```php
<?php

```
```python


from finix.resources import Application

application = Application.get()
```
```ruby

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "AP22AGPHEqD1fwgycz9DaTYk",
      "enabled" : true,
      "tags" : {
        "application_name" : "WePay"
      },
      "owner" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-04-17T23:48:35.68Z",
      "updated_at" : "2017-04-17T23:48:37.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/application_profile"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "merchant_identity": "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIw9KSQJAEiBMCdkeiYHm4kx", 
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
    .merchantIdentity("IDfNKgun2WNruSqAPBFYXaXz")
    .source("PIw9KSQJAEiBMCdkeiYHm4kx")
    .build()
);


```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIw9KSQJAEiBMCdkeiYHm4kx", 
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
	    "merchant_identity": "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIw9KSQJAEiBMCdkeiYHm4kx", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDfNKgun2WNruSqAPBFYXaXz", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIw9KSQJAEiBMCdkeiYHm4kx", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUnmDrd5efjNpyrovvwb6PZn",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:50.71Z",
  "updated_at" : "2017-04-17T23:48:50.77Z",
  "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:48:50.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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
curl https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnmDrd5efjNpyrovvwb6PZn");
Long captureAmount = 50L;
Long feeAmount = 10L;
authorization = authorization.capture(captureAmount, feeAmount);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUnmDrd5efjNpyrovvwb6PZn');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUnmDrd5efjNpyrovvwb6PZn")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUnmDrd5efjNpyrovvwb6PZn")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUnmDrd5efjNpyrovvwb6PZn",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7hEkZRcxzuCSiAAV6WCcUh",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:50.66Z",
  "updated_at" : "2017-04-17T23:48:51.52Z",
  "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:48:50.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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

curl https://api-staging.finix.io/authorizations/AU6CPYo3hiizZUcXCsbR4vKz \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUnmDrd5efjNpyrovvwb6PZn');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUnmDrd5efjNpyrovvwb6PZn")
authorization.void()

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUnmDrd5efjNpyrovvwb6PZn")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AU6CPYo3hiizZUcXCsbR4vKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:54.37Z",
  "updated_at" : "2017-04-17T23:48:55.17Z",
  "trace_id" : "57b9de0e-8ff8-4244-aecc-08e045a9ae0e",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : true,
  "expires_at" : "2017-04-24T23:48:54.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU6CPYo3hiizZUcXCsbR4vKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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

curl https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUnmDrd5efjNpyrovvwb6PZn");

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUnmDrd5efjNpyrovvwb6PZn');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUnmDrd5efjNpyrovvwb6PZn")
```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUnmDrd5efjNpyrovvwb6PZn")


```
> Example Response:

```json
{
  "id" : "AUnmDrd5efjNpyrovvwb6PZn",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR7hEkZRcxzuCSiAAV6WCcUh",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:50.66Z",
  "updated_at" : "2017-04-17T23:48:51.52Z",
  "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:48:50.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

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
      "id" : "AU6CPYo3hiizZUcXCsbR4vKz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:54.37Z",
      "updated_at" : "2017-04-17T23:48:55.17Z",
      "trace_id" : "57b9de0e-8ff8-4244-aecc-08e045a9ae0e",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "is_void" : true,
      "expires_at" : "2017-04-24T23:48:54.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU6CPYo3hiizZUcXCsbR4vKz"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        }
      }
    }, {
      "id" : "AUnmDrd5efjNpyrovvwb6PZn",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR7hEkZRcxzuCSiAAV6WCcUh",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:50.66Z",
      "updated_at" : "2017-04-17T23:48:51.52Z",
      "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "is_void" : false,
      "expires_at" : "2017-04-24T23:48:50.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUnmDrd5efjNpyrovvwb6PZn"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
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

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.

## Create an Identity for a Buyer


```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Ayisha", 
	        "last_name": "Le", 
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
	        "first_name"=> "Ayisha", 
	        "last_name"=> "Le", 
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
	        "first_name": "Ayisha", 
	        "last_name": "Le", 
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
	        "first_name"=> "Ayisha", 
	        "last_name"=> "Le", 
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
  "id" : "ID3xkAW9p2qaQRdCvNo8cchE",
  "entity" : {
    "title" : null,
    "first_name" : "Ayisha",
    "last_name" : "Le",
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
  "created_at" : "2017-04-17T23:48:44.45Z",
  "updated_at" : "2017-04-17T23:48:44.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Create an Identity for a Sender
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

import io.finix.payments.processing.client.model.Address;
import io.finix.payments.processing.client.model.BankAccountType;
import io.finix.payments.processing.client.model.BusinessType;
import io.finix.payments.processing.client.model.Date;
import io.finix.payments.processing.client.model.Entity;
import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .title("CEO")
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
        .ownershipType("PRIVATE")
        .hasAcceptedCreditCardsPreviously(false)
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


from finix.resources import Identity

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
identity = Finix::Identity.new(
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
  "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
  "created_at" : "2017-04-17T23:48:38.85Z",
  "updated_at" : "2017-04-17T23:48:38.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account
for your seller. This requires 3-steps:

1. Create an `Identity` resource with the sender's underwriting and identity
verification information (API request to the right)


2. [Create a Payment Instrument](#create-a-card) representing the
sender's bank account where processed funds will be settled (i.e. deposited)



#### HTTP Request

`POST https://api-staging.finix.io/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
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

curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDfNKgun2WNruSqAPBFYXaXz");

```
```php
<?php
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
```
```python


from finix.resources import Identity
identity = Identity.get(id="IDfNKgun2WNruSqAPBFYXaXz")

```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDfNKgun2WNruSqAPBFYXaXz")


```
> Example Response:

```json
{
  "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
  "created_at" : "2017-04-17T23:48:38.84Z",
  "updated_at" : "2017-04-17T23:48:38.84Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Green", 
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
```java

```
```php
<?php

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDfNKgun2WNruSqAPBFYXaXz")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDfNKgun2WNruSqAPBFYXaXz",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Green",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Prestige World Wide"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-04-17T23:48:38.84Z",
  "updated_at" : "2017-04-17T23:49:04.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code


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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92


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
      "id" : "ID3xkAW9p2qaQRdCvNo8cchE",
      "entity" : {
        "title" : null,
        "first_name" : "Ayisha",
        "last_name" : "Le",
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
      "created_at" : "2017-04-17T23:48:44.43Z",
      "updated_at" : "2017-04-17T23:48:44.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfMPhBzN1X7Wok1FUU6LUWK",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:42.08Z",
      "updated_at" : "2017-04-17T23:48:42.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDpPdjLcgGFHseoWLkT5NNrq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-04-17T23:48:41.69Z",
      "updated_at" : "2017-04-17T23:48:41.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID6AKxLcQQXR7aRRkydXPX5F",
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
      "created_at" : "2017-04-17T23:48:41.07Z",
      "updated_at" : "2017-04-17T23:48:41.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqEso4JwpiqtrXAx4axTw5M",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2017-04-17T23:48:40.56Z",
      "updated_at" : "2017-04-17T23:48:40.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID48Z5ZCKnn44Mu1StZbfenp",
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
      "created_at" : "2017-04-17T23:48:40.10Z",
      "updated_at" : "2017-04-17T23:48:40.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqJ6qXLxDg5sCw21e6wEPxr",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.68Z",
      "updated_at" : "2017-04-17T23:48:39.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDvzSm8Wi7qDtCYfM9HbjiBi",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.27Z",
      "updated_at" : "2017-04-17T23:48:39.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
      "created_at" : "2017-04-17T23:48:38.84Z",
      "updated_at" : "2017-04-17T23:48:38.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "WePay",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
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
        "application_name" : "WePay"
      },
      "created_at" : "2017-04-17T23:48:35.68Z",
      "updated_at" : "2017-04-17T23:48:35.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    "count" : 10
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
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDfNKgun2WNruSqAPBFYXaXz")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id => "MUnv85XMcN6G7FchWRm1epEx")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "verification" : "VI5fgYrVj3pNEFyBsUVqhS45",
  "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:43.69Z",
  "updated_at" : "2017-04-17T23:48:43.69Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI5fgYrVj3pNEFyBsUVqhS45"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUnv85XMcN6G7FchWRm1epEx");

```
```php
<?php
use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUnv85XMcN6G7FchWRm1epEx');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MUnv85XMcN6G7FchWRm1epEx")

```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUnv85XMcN6G7FchWRm1epEx")

```
> Example Response:

```json
{
  "id" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "verification" : null,
  "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:43.66Z",
  "updated_at" : "2017-04-17T23:48:43.78Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUnv85XMcN6G7FchWRm1epEx');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUnv85XMcN6G7FchWRm1epEx")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VImiopeQbZ8ysoU1pYNQWHM3",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:49:04.61Z",
  "updated_at" : "2017-04-17T23:49:04.64Z",
  "trace_id" : "831c3915-fff7-4410-a2e7-503561a614c6",
  "payment_instrument" : null,
  "merchant" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImiopeQbZ8ysoU1pYNQWHM3"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUnv85XMcN6G7FchWRm1epEx");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUnv85XMcN6G7FchWRm1epEx');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUnv85XMcN6G7FchWRm1epEx")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VImiopeQbZ8ysoU1pYNQWHM3",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:49:04.61Z",
  "updated_at" : "2017-04-17T23:49:04.64Z",
  "trace_id" : "831c3915-fff7-4410-a2e7-503561a614c6",
  "payment_instrument" : null,
  "merchant" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImiopeQbZ8ysoU1pYNQWHM3"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "verification" : null,
  "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:43.66Z",
  "updated_at" : "2017-04-17T23:52:16.02Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/ \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "MUnv85XMcN6G7FchWRm1epEx",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "verification" : null,
  "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:43.66Z",
  "updated_at" : "2017-04-17T23:52:16.46Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

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
      "id" : "MUnv85XMcN6G7FchWRm1epEx",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "verification" : null,
      "merchant_profile" : "MP7oRterYoyXdfgbXwVgL3ZY",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-04-17T23:48:43.66Z",
      "updated_at" : "2017-04-17T23:48:43.78Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MP7oRterYoyXdfgbXwVgL3ZY"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUnv85XMcN6G7FchWRm1epEx');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUnv85XMcN6G7FchWRm1epEx")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID3xkAW9p2qaQRdCvNo8cchE",
      "entity" : {
        "title" : null,
        "first_name" : "Ayisha",
        "last_name" : "Le",
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
      "created_at" : "2017-04-17T23:48:44.43Z",
      "updated_at" : "2017-04-17T23:48:44.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfMPhBzN1X7Wok1FUU6LUWK",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:42.08Z",
      "updated_at" : "2017-04-17T23:48:42.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDpPdjLcgGFHseoWLkT5NNrq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-04-17T23:48:41.69Z",
      "updated_at" : "2017-04-17T23:48:41.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID6AKxLcQQXR7aRRkydXPX5F",
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
      "created_at" : "2017-04-17T23:48:41.07Z",
      "updated_at" : "2017-04-17T23:48:41.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqEso4JwpiqtrXAx4axTw5M",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2017-04-17T23:48:40.56Z",
      "updated_at" : "2017-04-17T23:48:40.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID48Z5ZCKnn44Mu1StZbfenp",
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
      "created_at" : "2017-04-17T23:48:40.10Z",
      "updated_at" : "2017-04-17T23:48:40.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqJ6qXLxDg5sCw21e6wEPxr",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.68Z",
      "updated_at" : "2017-04-17T23:48:39.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDvzSm8Wi7qDtCYfM9HbjiBi",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.27Z",
      "updated_at" : "2017-04-17T23:48:39.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
      "created_at" : "2017-04-17T23:48:38.84Z",
      "updated_at" : "2017-04-17T23:48:38.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "WePay",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
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
        "application_name" : "WePay"
      },
      "created_at" : "2017-04-17T23:48:35.68Z",
      "updated_at" : "2017-04-17T23:48:35.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    "count" : 10
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
curl https://api-staging.finix.io/merchants/MUnv85XMcN6G7FchWRm1epEx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

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
  "_embedded" : {
    "identities" : [ {
      "id" : "ID3xkAW9p2qaQRdCvNo8cchE",
      "entity" : {
        "title" : null,
        "first_name" : "Ayisha",
        "last_name" : "Le",
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
      "created_at" : "2017-04-17T23:48:44.43Z",
      "updated_at" : "2017-04-17T23:48:44.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfMPhBzN1X7Wok1FUU6LUWK",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:42.08Z",
      "updated_at" : "2017-04-17T23:48:42.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfMPhBzN1X7Wok1FUU6LUWK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDpPdjLcgGFHseoWLkT5NNrq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-04-17T23:48:41.69Z",
      "updated_at" : "2017-04-17T23:48:41.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpPdjLcgGFHseoWLkT5NNrq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID6AKxLcQQXR7aRRkydXPX5F",
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
      "created_at" : "2017-04-17T23:48:41.07Z",
      "updated_at" : "2017-04-17T23:48:41.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6AKxLcQQXR7aRRkydXPX5F/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqEso4JwpiqtrXAx4axTw5M",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2017-04-17T23:48:40.56Z",
      "updated_at" : "2017-04-17T23:48:40.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqEso4JwpiqtrXAx4axTw5M/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "ID48Z5ZCKnn44Mu1StZbfenp",
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
      "created_at" : "2017-04-17T23:48:40.10Z",
      "updated_at" : "2017-04-17T23:48:40.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID48Z5ZCKnn44Mu1StZbfenp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDqJ6qXLxDg5sCw21e6wEPxr",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.68Z",
      "updated_at" : "2017-04-17T23:48:39.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqJ6qXLxDg5sCw21e6wEPxr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDvzSm8Wi7qDtCYfM9HbjiBi",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:48:39.27Z",
      "updated_at" : "2017-04-17T23:48:39.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvzSm8Wi7qDtCYfM9HbjiBi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDfNKgun2WNruSqAPBFYXaXz",
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
      "created_at" : "2017-04-17T23:48:38.84Z",
      "updated_at" : "2017-04-17T23:48:38.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "WePay",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
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
        "application_name" : "WePay"
      },
      "created_at" : "2017-04-17T23:48:35.68Z",
      "updated_at" : "2017-04-17T23:48:35.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    "count" : 10
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
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'

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
  "id" : "US2p6VAPg3zRdgQyrGVAAjNA",
  "password" : "5c972764-c0a8-4882-9632-7efcdf1a2626",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:46.92Z",
  "updated_at" : "2017-04-17T23:48:46.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US2p6VAPg3zRdgQyrGVAAjNA"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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


## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;
import io.finix.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TK7ci8PhpqSGXsLKmi6ZeM21")
            .identity("IDfNKgun2WNruSqAPBFYXaXz")
    .build()
);
```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type": "TOKEN", 
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}).save()
```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TK7ci8PhpqSGXsLKmi6ZeM21", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7ci8PhpqSGXsLKmi6ZeM21",
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
  "created_at" : "2017-04-17T23:48:53.48Z",
  "updated_at" : "2017-04-17T23:48:53.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/updates"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "name": "Walter Henderson", 
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
	    "identity": "ID3xkAW9p2qaQRdCvNo8cchE"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDfNKgun2WNruSqAPBFYXaXz")
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

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Henderson", 
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
	    "identity"=> "ID3xkAW9p2qaQRdCvNo8cchE"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Henderson", 
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
	    "identity": "ID3xkAW9p2qaQRdCvNo8cchE"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Walter Henderson", 
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
	    "identity"=> "ID3xkAW9p2qaQRdCvNo8cchE"
	}).save
```
> Example Response:

```json
{
  "id" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "fingerprint" : "FPR739722504",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Henderson",
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
  "created_at" : "2017-04-17T23:48:44.85Z",
  "updated_at" : "2017-04-17T23:48:44.85Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3xkAW9p2qaQRdCvNo8cchE",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/updates"
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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
## Create a Bank Account
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDfNKgun2WNruSqAPBFYXaXz")
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

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
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
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
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
	    "identity": "IDfNKgun2WNruSqAPBFYXaXz"
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
	    "identity"=> "IDfNKgun2WNruSqAPBFYXaXz"
	}).save
```
> Example Response:

```json
{
  "id" : "PIcgLj6AecVH1XbMpZpCF4Td",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:48:42.65Z",
  "updated_at" : "2017-04-17T23:48:42.65Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
name | *string*, **required** | Account owner's full name (max 40 characters)
## Fetch a Bank Account

```shell
curl https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIcgLj6AecVH1XbMpZpCF4Td")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIcgLj6AecVH1XbMpZpCF4Td');

```
```python



```
```ruby
bank_account = Finix::BankAccount.retrieve(:id=> "PIcgLj6AecVH1XbMpZpCF4Td")

```
> Example Response:

```json
{
  "id" : "PIcgLj6AecVH1XbMpZpCF4Td",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:48:42.62Z",
  "updated_at" : "2017-04-17T23:48:43.08Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `BANK_ACCOUNT`

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Fetch a Credit Card
```shell
curl https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIw9KSQJAEiBMCdkeiYHm4kx")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIw9KSQJAEiBMCdkeiYHm4kx');

```
```python



```
```ruby
card = Finix::PaymentCard.retrieve(:id=> "PIw9KSQJAEiBMCdkeiYHm4kx")


```
> Example Response:

```json
{
  "id" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "fingerprint" : "FPR739722504",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Henderson",
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
  "created_at" : "2017-04-17T23:48:44.81Z",
  "updated_at" : "2017-04-17T23:48:50.73Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3xkAW9p2qaQRdCvNo8cchE",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Check for Card Updates

```shell
curl https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '
	{
	    "merchant": "MUnv85XMcN6G7FchWRm1epEx"
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
  "id" : "IUfTYWJ7RRTs1gZLpyx8MyLQ",
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "merchant" : "MUnv85XMcN6G7FchWRm1epEx",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-04-17T23:48:55.83Z",
  "updated_at" : "2017-04-17T23:48:55.86Z",
  "payment_instrument" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "trace_id" : "759eb87d-b08c-4778-9057-2bab1522f421",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/updates/IUfTYWJ7RRTs1gZLpyx8MyLQ"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID/updates/`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant` 
:PAYMENT_INSTRUMENT_ID | *string*, **required** | ID of the `Payment Instrument`




## List all Payment Instruments

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92
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
      "id" : "PI7ci8PhpqSGXsLKmi6ZeM21",
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
      "created_at" : "2017-04-17T23:48:53.44Z",
      "updated_at" : "2017-04-17T23:48:53.44Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7ci8PhpqSGXsLKmi6ZeM21/updates"
        }
      }
    }, {
      "id" : "PIh6qmthgVJNXaYCG5ahB5wN",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:48:45.25Z",
      "updated_at" : "2017-04-17T23:48:45.25Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID3xkAW9p2qaQRdCvNo8cchE",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "fingerprint" : "FPR739722504",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Walter Henderson",
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
      "created_at" : "2017-04-17T23:48:44.81Z",
      "updated_at" : "2017-04-17T23:48:50.73Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID3xkAW9p2qaQRdCvNo8cchE",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3xkAW9p2qaQRdCvNo8cchE"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx/updates"
        }
      }
    }, {
      "id" : "PIuYoj7cLT4FJXqBuPHHkxW7",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:43.66Z",
      "updated_at" : "2017-04-17T23:48:43.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYoj7cLT4FJXqBuPHHkxW7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYoj7cLT4FJXqBuPHHkxW7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYoj7cLT4FJXqBuPHHkxW7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYoj7cLT4FJXqBuPHHkxW7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PI5eBJ31fgnU6XjrfK3R4Z87",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:43.66Z",
      "updated_at" : "2017-04-17T23:48:43.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5eBJ31fgnU6XjrfK3R4Z87"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5eBJ31fgnU6XjrfK3R4Z87/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5eBJ31fgnU6XjrfK3R4Z87/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5eBJ31fgnU6XjrfK3R4Z87/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:43.66Z",
      "updated_at" : "2017-04-17T23:48:43.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PIcgLj6AecVH1XbMpZpCF4Td",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:48:42.62Z",
      "updated_at" : "2017-04-17T23:48:43.08Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PIi4aybz3MGpEaVzqboRr5vT",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:36.20Z",
      "updated_at" : "2017-04-17T23:48:36.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PIczY73VrpaCScZmSptbYXLX",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:36.20Z",
      "updated_at" : "2017-04-17T23:48:36.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PI6KGNqPV9mBHh9QBtevdZz8",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:36.20Z",
      "updated_at" : "2017-04-17T23:48:36.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KGNqPV9mBHh9QBtevdZz8"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KGNqPV9mBHh9QBtevdZz8/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KGNqPV9mBHh9QBtevdZz8/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6KGNqPV9mBHh9QBtevdZz8/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "PIiuS5feUwxmrpJJnpBrQyqR",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:48:36.20Z",
      "updated_at" : "2017-04-17T23:48:36.20Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiuS5feUwxmrpJJnpBrQyqR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiuS5feUwxmrpJJnpBrQyqR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiuS5feUwxmrpJJnpBrQyqR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiuS5feUwxmrpJJnpBrQyqR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    "count" : 11
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

curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
);

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDfNKgun2WNruSqAPBFYXaXz');
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

identity = Identity.get(id="IDfNKgun2WNruSqAPBFYXaXz")
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
identity = Finix::Identity.retrieve(:id=>"IDfNKgun2WNruSqAPBFYXaXz")
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
  "id" : "SThZK4ge46CJV27dV3LDbyF4",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:52:11.62Z",
  "updated_at" : "2017-04-17T23:52:11.67Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1209845,
  "total_fees" : 120985,
  "total_fee" : 120985,
  "net_amount" : 1088860,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("SThZK4ge46CJV27dV3LDbyF4");

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('SThZK4ge46CJV27dV3LDbyF4');

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"SThZK4ge46CJV27dV3LDbyF4")

```
> Example Response:

```json
{
  "id" : "SThZK4ge46CJV27dV3LDbyF4",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:52:11.58Z",
  "updated_at" : "2017-04-17T23:52:12.50Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1209845,
  "total_fees" : 120985,
  "total_fee" : 120985,
  "net_amount" : 1088860,
  "destination" : "PIcgLj6AecVH1XbMpZpCF4Td",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=debit"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

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
      "id" : "SThZK4ge46CJV27dV3LDbyF4",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "currency" : "USD",
      "created_at" : "2017-04-17T23:52:11.58Z",
      "updated_at" : "2017-04-17T23:52:12.50Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 1209845,
      "total_fees" : 120985,
      "total_fee" : 120985,
      "net_amount" : 1088860,
      "destination" : "PIcgLj6AecVH1XbMpZpCF4Td",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java
Settlement settlement = client.settlementsClient().fetch("SThZK4ge46CJV27dV3LDbyF4");
  settlement.fundingTransfersClient().<Resources<Transfer>>resourcesIterator()
    .forEachRemaining(page -> {
      Collection<Transfer> transfers = page.getContent();
      transfers.forEach(transfer ->
     // do something
      );
    });
}
```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('SThZK4ge46CJV27dV3LDbyF4');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"SThZK4ge46CJV27dV3LDbyF4")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR4frQcc6rtZgTptRrX2UZUZ",
      "amount" : 1088860,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "c0b97e8f-74d1-435e-95af-949486d8abe5",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIcgLj6AecVH1XbMpZpCF4Td",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:12.17Z",
      "updated_at" : "2017-04-17T23:52:12.45Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR4frQcc6rtZgTptRrX2UZUZ"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR4frQcc6rtZgTptRrX2UZUZ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR4frQcc6rtZgTptRrX2UZUZ/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR4frQcc6rtZgTptRrX2UZUZ/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR4frQcc6rtZgTptRrX2UZUZ/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcgLj6AecVH1XbMpZpCF4Td"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java
Settlement settlement = client.settlementsClient().fetch("SThZK4ge46CJV27dV3LDbyF4");
    settlement.transfersClient().<Resources<Transfer>>resourcesIterator()
      .forEachRemaining(page -> {
        Collection<Transfer> transfers = page.getContent();
        transfers.forEach(transfer ->
       // do something
        );
      });
  }



```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('SThZK4ge46CJV27dV3LDbyF4');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"SThZK4ge46CJV27dV3LDbyF4")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRJS1gvU2xmnuThdKyfquWY",
      "amount" : 81375,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "24d1af38-d608-4db6-807b-6e9a1e5f7e4a",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIczY73VrpaCScZmSptbYXLX",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:10.95Z",
      "updated_at" : "2017-04-17T23:52:11.18Z",
      "merchant_identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRJS1gvU2xmnuThdKyfquWY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRJS1gvU2xmnuThdKyfquWY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRJS1gvU2xmnuThdKyfquWY/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRJS1gvU2xmnuThdKyfquWY/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRJS1gvU2xmnuThdKyfquWY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX"
        }
      }
    }, {
      "id" : "TRjFNM2N3pn4USKZKGxFCucz",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "ac16ff80-a953-48b7-b91d-3b6467185eb4",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIi4aybz3MGpEaVzqboRr5vT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:10.49Z",
      "updated_at" : "2017-04-17T23:52:10.92Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRjFNM2N3pn4USKZKGxFCucz"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRjFNM2N3pn4USKZKGxFCucz/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRjFNM2N3pn4USKZKGxFCucz/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRjFNM2N3pn4USKZKGxFCucz/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRjFNM2N3pn4USKZKGxFCucz/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT"
        }
      }
    }, {
      "id" : "TRv5Mavqbo4oYFvBXpAKmMDB",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "0b63cbb5-e0a8-481d-9686-65dcde79a869",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIi4aybz3MGpEaVzqboRr5vT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:10.06Z",
      "updated_at" : "2017-04-17T23:52:10.43Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRv5Mavqbo4oYFvBXpAKmMDB"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRv5Mavqbo4oYFvBXpAKmMDB/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRv5Mavqbo4oYFvBXpAKmMDB/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRv5Mavqbo4oYFvBXpAKmMDB/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRv5Mavqbo4oYFvBXpAKmMDB/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT"
        }
      }
    }, {
      "id" : "TRreWBwU9EEmaynjpsnKpcKF",
      "amount" : 39577,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "71474ce2-2be0-4f25-846f-624a7d910c23",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIczY73VrpaCScZmSptbYXLX",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:09.73Z",
      "updated_at" : "2017-04-17T23:52:10.01Z",
      "merchant_identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRreWBwU9EEmaynjpsnKpcKF"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRreWBwU9EEmaynjpsnKpcKF/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDgXEWuvWEtpM9J8W1U9vSzf"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRreWBwU9EEmaynjpsnKpcKF/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRreWBwU9EEmaynjpsnKpcKF/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRreWBwU9EEmaynjpsnKpcKF/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIczY73VrpaCScZmSptbYXLX"
        }
      }
    }, {
      "id" : "TRiz4XnNnkXF4FuuEJqSxE26",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "904237e9-6064-4fb6-98b8-2de35cda7817",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIi4aybz3MGpEaVzqboRr5vT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:09.37Z",
      "updated_at" : "2017-04-17T23:52:09.69Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRiz4XnNnkXF4FuuEJqSxE26"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRiz4XnNnkXF4FuuEJqSxE26/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRiz4XnNnkXF4FuuEJqSxE26/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRiz4XnNnkXF4FuuEJqSxE26/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRiz4XnNnkXF4FuuEJqSxE26/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIi4aybz3MGpEaVzqboRr5vT"
        }
      }
    }, {
      "id" : "TR7hEkZRcxzuCSiAAV6WCcUh",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 10,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:51.41Z",
      "updated_at" : "2017-04-17T23:49:17.24Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    }, {
      "id" : "TRojYTyiuZP7axuAPpxxLRHw",
      "amount" : 813861,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "56e041b9-65a4-4b51-b35a-364520672bbe",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIh6qmthgVJNXaYCG5ahB5wN",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 81386,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:46.36Z",
      "updated_at" : "2017-04-17T23:49:20.13Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    }, {
      "id" : "TRo78WokKsW3L3pAz5gZxrmD",
      "amount" : 395884,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "3d2a2076-bf44-4be0-b1b9-4ef0397e92bf",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : "2017-04-17T23:52:09.27Z",
      "fee" : 39588,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:45.70Z",
      "updated_at" : "2017-04-17T23:49:13.94Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/SThZK4ge46CJV27dV3LDbyF4/transfers?offset=0&limit=20&sort=created_at,desc"
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

`Transfers` can have four possible states values: PENDING, SUCCEEDED, FAILED, or CANCELED.

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
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92


```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRo78WokKsW3L3pAz5gZxrmD");

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRo78WokKsW3L3pAz5gZxrmD');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TRo78WokKsW3L3pAz5gZxrmD")

```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRo78WokKsW3L3pAz5gZxrmD")

```
> Example Response:

```json
{
  "id" : "TRo78WokKsW3L3pAz5gZxrmD",
  "amount" : 395884,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "3d2a2076-bf44-4be0-b1b9-4ef0397e92bf",
  "currency" : "USD",
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
  "ready_to_settle_at" : null,
  "fee" : 39588,
  "statement_descriptor" : "FIN*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:45.70Z",
  "updated_at" : "2017-04-17T23:48:45.83Z",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
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

curl https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

$debit = Transfer::retrieve('TRo78WokKsW3L3pAz5gZxrmD');
$refund = $debit->reverse(11);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TRo78WokKsW3L3pAz5gZxrmD")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRo78WokKsW3L3pAz5gZxrmD")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TRkDpewtG1XbRBCuAEpboJRP",
  "amount" : 666736,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "9f1678d4-c5f2-4822-bc4b-c91cd7ac7121",
  "currency" : "USD",
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
  "destination" : "PIw9KSQJAEiBMCdkeiYHm4kx",
  "ready_to_settle_at" : null,
  "fee" : 66674,
  "statement_descriptor" : "FIN*BOBS BURGERS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:49.55Z",
  "updated_at" : "2017-04-17T23:48:49.61Z",
  "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRkDpewtG1XbRBCuAEpboJRP"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRkDpewtG1XbRBCuAEpboJRP/payment_instruments"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

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
      "id" : "TR7hEkZRcxzuCSiAAV6WCcUh",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "aabe5af9-a702-4874-9efb-85e7cc104967",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:51.41Z",
      "updated_at" : "2017-04-17T23:48:51.52Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7hEkZRcxzuCSiAAV6WCcUh/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    }, {
      "id" : "TRkDpewtG1XbRBCuAEpboJRP",
      "amount" : 666736,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "36f4706c-d0ec-4497-a335-dccdfcc8270b",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "destination" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "ready_to_settle_at" : null,
      "fee" : 66674,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:49.43Z",
      "updated_at" : "2017-04-17T23:48:49.61Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRkDpewtG1XbRBCuAEpboJRP"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRkDpewtG1XbRBCuAEpboJRP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        }
      }
    }, {
      "id" : "TRmU9NKTM9K9UHZFuYXC3i9y",
      "amount" : 666736,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "3a73abb5-e278-4fdd-9e0f-f84620baf528",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : null,
      "fee" : 66674,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:48.74Z",
      "updated_at" : "2017-04-17T23:48:49.52Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRmU9NKTM9K9UHZFuYXC3i9y/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    }, {
      "id" : "TRojYTyiuZP7axuAPpxxLRHw",
      "amount" : 813861,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "56e041b9-65a4-4b51-b35a-364520672bbe",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIh6qmthgVJNXaYCG5ahB5wN",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : null,
      "fee" : 81386,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:46.36Z",
      "updated_at" : "2017-04-17T23:48:46.47Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRojYTyiuZP7axuAPpxxLRHw/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh6qmthgVJNXaYCG5ahB5wN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
        }
      }
    }, {
      "id" : "TRo78WokKsW3L3pAz5gZxrmD",
      "amount" : 395884,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "3d2a2076-bf44-4be0-b1b9-4ef0397e92bf",
      "currency" : "USD",
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "source" : "PIw9KSQJAEiBMCdkeiYHm4kx",
      "destination" : "PI6Yyo98eaCRwgLuhFK4TtzT",
      "ready_to_settle_at" : null,
      "fee" : 39588,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:45.70Z",
      "updated_at" : "2017-04-17T23:48:45.83Z",
      "merchant_identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRo78WokKsW3L3pAz5gZxrmD/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIw9KSQJAEiBMCdkeiYHm4kx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6Yyo98eaCRwgLuhFK4TtzT"
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


## Create ROLE_PARTNER User
```shell
curl https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'

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
  "id" : "USuT2XqryENsxHKtrQrBK5n2",
  "password" : "097c33df-7ca5-4cdb-9db9-537951084929",
  "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:36.90Z",
  "updated_at" : "2017-04-17T23:48:36.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USuT2XqryENsxHKtrQrBK5n2"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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

## Create ROLE_MERCHANT User
```shell
curl https://api-staging.finix.io/identities/IDfNKgun2WNruSqAPBFYXaXz/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
    -d '{}'

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
  "id" : "US2p6VAPg3zRdgQyrGVAAjNA",
  "password" : "5c972764-c0a8-4882-9632-7efcdf1a2626",
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:46.92Z",
  "updated_at" : "2017-04-17T23:48:46.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US2p6VAPg3zRdgQyrGVAAjNA"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/users/TRo78WokKsW3L3pAz5gZxrmD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php

```
```python


from finix.resources import User
user = User.get(id="UShascJpYqtfe9fxa9KSUHTP")

```
```ruby

```
> Example Response:

```json
{
  "id" : "UShascJpYqtfe9fxa9KSUHTP",
  "password" : null,
  "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:34.63Z",
  "updated_at" : "2017-04-17T23:48:35.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UShascJpYqtfe9fxa9KSUHTP"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
curl https://api-staging.finix.io/users/US2p6VAPg3zRdgQyrGVAAjNA \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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

```
```python



```
```ruby

```
> Example Response:

```json
{
  "id" : "US2p6VAPg3zRdgQyrGVAAjNA",
  "password" : null,
  "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:48:46.89Z",
  "updated_at" : "2017-04-17T23:48:47.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US2p6VAPg3zRdgQyrGVAAjNA"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

```
```java

```
```php
<?php

```
```python


from finix.resources import User
users = User.get()

```
```ruby

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "US2p6VAPg3zRdgQyrGVAAjNA",
      "password" : null,
      "identity" : "IDfNKgun2WNruSqAPBFYXaXz",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-04-17T23:48:46.89Z",
      "updated_at" : "2017-04-17T23:48:48.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US2p6VAPg3zRdgQyrGVAAjNA"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "USuT2XqryENsxHKtrQrBK5n2",
      "password" : null,
      "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:48:36.88Z",
      "updated_at" : "2017-04-17T23:48:36.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USuT2XqryENsxHKtrQrBK5n2"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
        }
      }
    }, {
      "id" : "UShascJpYqtfe9fxa9KSUHTP",
      "password" : null,
      "identity" : "IDgXEWuvWEtpM9J8W1U9vSzf",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:48:34.63Z",
      "updated_at" : "2017-04-17T23:48:35.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/UShascJpYqtfe9fxa9KSUHTP"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92 \
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
  "id" : "WHwyKC1keZZtnMM22nh5e3k",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "created_at" : "2017-04-17T23:48:38.51Z",
  "updated_at" : "2017-04-17T23:48:38.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHwyKC1keZZtnMM22nh5e3k"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request (max 120 characters)


## Retrieve a Webhook

```shell



curl https://api-staging.finix.io/webhooks/WHwyKC1keZZtnMM22nh5e3k \
    -H "Content-Type: application/vnd.json+api" \
    -u US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92


```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHwyKC1keZZtnMM22nh5e3k");

```
```php
<?php
use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHwyKC1keZZtnMM22nh5e3k');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WHwyKC1keZZtnMM22nh5e3k")

```
```ruby
webhook = Finix::Webhook.retrieve(:id=> "WHwyKC1keZZtnMM22nh5e3k")


```
> Example Response:

```json
{
  "id" : "WHwyKC1keZZtnMM22nh5e3k",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP22AGPHEqD1fwgycz9DaTYk",
  "created_at" : "2017-04-17T23:48:38.51Z",
  "updated_at" : "2017-04-17T23:48:38.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHwyKC1keZZtnMM22nh5e3k"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
    -u  US7WwPZ8N8nGwt48GdeCmqoG:09539f06-cdc1-43d2-beb6-4d58c9a0fc92

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
      "id" : "WHwyKC1keZZtnMM22nh5e3k",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "AP22AGPHEqD1fwgycz9DaTYk",
      "created_at" : "2017-04-17T23:48:38.51Z",
      "updated_at" : "2017-04-17T23:48:38.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHwyKC1keZZtnMM22nh5e3k"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP22AGPHEqD1fwgycz9DaTYk"
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
