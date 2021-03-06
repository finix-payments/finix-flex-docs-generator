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
of charging a card. This guide will walk you through provisioning merchant
accounts, tokenizing cards, charging those cards, and finally settling (i.e.
payout) those funds out to your merchants.

3. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
  client.setupUserIdAndPassword("US669rYWoQvFYqHV5kPE8L2E", "ea99d26c-80c8-4233-adda-fd9a3ee48cfd");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'US669rYWoQvFYqHV5kPE8L2E',
	"password" => 'ea99d26c-80c8-4233-adda-fd9a3ee48cfd']
	);

require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("US669rYWoQvFYqHV5kPE8L2E", "ea99d26c-80c8-4233-adda-fd9a3ee48cfd"))

```
```ruby
# To download the Ruby gem:
# gem install payline-data

require 'payline'

Payline.configure(
    :root_url => 'https://api-test.payline.io',
    :user=>'US669rYWoQvFYqHV5kPE8L2E',
    :password => 'ea99d26c-80c8-4233-adda-fd9a3ee48cfd'
)
```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US669rYWoQvFYqHV5kPE8L2E`

- Password: `ea99d26c-80c8-4233-adda-fd9a3ee48cfd`

- Application ID: `APn7hrntyq8KiHRQLi82dkS2`

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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "ownership_type": "PRIVATE", 
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PawnyCityHall.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDkfvquctsLXZszYmnzpe6pv",
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
  "created_at" : "2017-04-17T23:52:31.53Z",
  "updated_at" : "2017-04-17T23:52:31.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-test.payline.io/identities`

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
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDkfvquctsLXZszYmnzpe6pv"
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
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
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
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
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
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
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIxqhZfPQr66EZ82jXqDMoT",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:52:35.65Z",
  "updated_at" : "2017-04-17T23:52:35.65Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
name | *string*, **required** | Account owner's full name (max 40 characters)
### Step 3: Provision Merchant Account

```shell
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDkfvquctsLXZszYmnzpe6pv")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDkfvquctsLXZszYmnzpe6pv")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "verification" : "VIf2CTjYEzKVXH1SpqJagYDU",
  "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:36.71Z",
  "updated_at" : "2017-04-17T23:52:36.71Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "verification" : {
      "href" : "https://api-test.payline.io:443/verifications/VIf2CTjYEzKVXH1SpqJagYDU"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Jones", 
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
	        "first_name"=> "Step", 
	        "last_name"=> "Jones", 
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
	        "first_name": "Step", 
	        "last_name": "Jones", 
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
	        "first_name"=> "Step", 
	        "last_name"=> "Jones", 
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
  "id" : "IDcdWNLK7wa2trGRBcHfyKZo",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
    "last_name" : "Jones",
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
  "created_at" : "2017-04-17T23:52:37.43Z",
  "updated_at" : "2017-04-17T23:52:37.43Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 5: Tokenize a Card
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "name": "Walter Lopez", 
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
	    "identity": "IDcdWNLK7wa2trGRBcHfyKZo"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDkfvquctsLXZszYmnzpe6pv")
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Lopez", 
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
	    "identity"=> "IDcdWNLK7wa2trGRBcHfyKZo"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Lopez", 
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
	    "identity": "IDcdWNLK7wa2trGRBcHfyKZo"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Walter Lopez", 
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
	    "identity"=> "IDcdWNLK7wa2trGRBcHfyKZo"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "fingerprint" : "FPR178541064",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Lopez",
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
  "created_at" : "2017-04-17T23:52:37.91Z",
  "updated_at" : "2017-04-17T23:52:37.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcdWNLK7wa2trGRBcHfyKZo",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/updates"
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 6: Create an Authorization
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "merchant_identity": "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeDe5Vm6FoCT4qt43FwAk9A", 
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
    .merchantIdentity("IDkfvquctsLXZszYmnzpe6pv")
    .source("PIeDe5Vm6FoCT4qt43FwAk9A")
    .build()
);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeDe5Vm6FoCT4qt43FwAk9A", 
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
	    "merchant_identity": "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeDe5Vm6FoCT4qt43FwAk9A", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeDe5Vm6FoCT4qt43FwAk9A", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU8wVfEpFw7U3Kac5r784YRW",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:42.80Z",
  "updated_at" : "2017-04-17T23:52:42.85Z",
  "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:52:42.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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
curl https://api-test.payline.io/authorizations/AU8wVfEpFw7U3Kac5r784YRW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8wVfEpFw7U3Kac5r784YRW");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU8wVfEpFw7U3Kac5r784YRW');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU8wVfEpFw7U3Kac5r784YRW")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AU8wVfEpFw7U3Kac5r784YRW")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU8wVfEpFw7U3Kac5r784YRW",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRaA9kwVetidJqm7xjDzjghi",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:42.75Z",
  "updated_at" : "2017-04-17T23:52:43.62Z",
  "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:52:42.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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

### Step 8: Create a Batch Settlement
```shell
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
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

identity = Identity.get(id="IDkfvquctsLXZszYmnzpe6pv")
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
identity = Payline::Identity.retrieve(:id=>"IDkfvquctsLXZszYmnzpe6pv")
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
  "id" : "STcPmNe9qq5kkz3AJ6BSqdVp",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:55:15.90Z",
  "updated_at" : "2017-04-17T23:55:15.93Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 715233,
  "total_fees" : 71524,
  "total_fee" : 71524,
  "net_amount" : 643709,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=debit"
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
          applicationId: 'APn7hrntyq8KiHRQLi82dkS2',
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
  "id" : "TKvrwB3316K26LVCL4w5wrNN",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:52:44.77Z",
  "updated_at" : "2017-04-17T23:52:44.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:52:44.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKvrwB3316K26LVCL4w5wrNN")
            .identity("IDkfvquctsLXZszYmnzpe6pv")
    .build()
);
```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIvrwB3316K26LVCL4w5wrNN",
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
  "created_at" : "2017-04-17T23:52:45.56Z",
  "updated_at" : "2017-04-17T23:52:45.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/updates"
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
    secureForm.submit('/applications/APn7hrntyq8KiHRQLi82dkS2/tokens', {
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
  "id" : "TKvrwB3316K26LVCL4w5wrNN",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:52:44.77Z",
  "updated_at" : "2017-04-17T23:52:44.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:52:44.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKvrwB3316K26LVCL4w5wrNN")
            .identity("IDkfvquctsLXZszYmnzpe6pv")
    .build()
);
```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIvrwB3316K26LVCL4w5wrNN",
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
  "created_at" : "2017-04-17T23:52:45.56Z",
  "updated_at" : "2017-04-17T23:52:45.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/updates"
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
curl https://api-test.payline.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
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
  "id" : "US669rYWoQvFYqHV5kPE8L2E",
  "password" : "ea99d26c-80c8-4233-adda-fd9a3ee48cfd",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:27.97Z",
  "updated_at" : "2017-04-17T23:52:27.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/US669rYWoQvFYqHV5kPE8L2E"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
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
	        "application_name": "Square"
	    }, 
	    "user": "US669rYWoQvFYqHV5kPE8L2E", 
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
	        "doing_business_as": "Square", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Square", 
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
use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "US669rYWoQvFYqHV5kPE8L2E", 
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
```ruby

```
> Example Response:

```json
{
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:52:28.44Z",
  "updated_at" : "2017-04-17T23:52:28.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
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
  "id" : "PRrfYyjGYWvgL1Z99P9j1U9c",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "default_merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "created_at" : "2017-04-17T23:52:29.17Z",
  "updated_at" : "2017-04-17T23:52:29.17Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2",
    "canDebitBankAccount" : true
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors/PRrfYyjGYWvgL1Z99P9j1U9c"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
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
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:52:28.43Z",
  "updated_at" : "2017-04-17T23:55:23.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
### Step 5: Enable Settlement Functionality
```shell
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
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
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:52:28.43Z",
  "updated_at" : "2017-04-17T23:55:23.57Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
# Fees

 You can find the live example of how fees are calculated in this [spreadsheet](https://docs.google.com/spreadsheets/d/1UFmKg7EvhlCduM31bQ3rOeslszOlO49rOw3frllBj9c/edit#gid=0)

## Case 1 
- Fee profile not set
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.00 | $100.00 | $0.00 | $0.00 | $0.00 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.00 | $90.00 | $10.00 | $0.00 | $0.00 |

## Case 2
- Fee profile not set
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.11 | $90.00 | $9.89 | $0.11 | $0.11 |
| $100 | $0.10 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |

## Case 3 
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.00 | $96.00 | $0.80 | $3.20 | $3.20 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.00 | $1.00 | $95.80 | $3.20 | $3.20 |

## Case 4 
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.11 | $96.00 | $0.69 | $3.31 | $3.31 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.11 | $1.00 | $95.69 | $3.31 | $3.31 |

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
where you're hosting your form. Please include the script tag as demonstrated
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
    applicationId: "APn7hrntyq8KiHRQLi82dkS2",
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
name | *string*, **required** | Account owner's full name (max 40 characters)
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
  "id" : "TKvrwB3316K26LVCL4w5wrNN",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:52:44.77Z",
  "updated_at" : "2017-04-17T23:52:44.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:52:44.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
Great! Now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server, which you'll do by expanding on the callback that you created in the previous step.


### Step 6: Associate to an Identity
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKvrwB3316K26LVCL4w5wrNN")
            .identity("IDkfvquctsLXZszYmnzpe6pv")
    .build()
);
```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIvrwB3316K26LVCL4w5wrNN",
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
  "created_at" : "2017-04-17T23:52:45.56Z",
  "updated_at" : "2017-04-17T23:52:45.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/updates"
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
# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```java

```
```php
<?php
use Payline\Resources\Application;

$application = Application::retrieve('APn7hrntyq8KiHRQLi82dkS2');

```
```python


from payline.resources import Application

application = Application.get(id="APn7hrntyq8KiHRQLi82dkS2")
```
```ruby

```
> Example Response:

```json
{
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:52:28.43Z",
  "updated_at" : "2017-04-17T23:52:30.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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

## Create an Application
```shell
curl https://api-test.payline.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
    -d '
	{
	    "tags": {
	        "application_name": "Square"
	    }, 
	    "user": "US669rYWoQvFYqHV5kPE8L2E", 
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
	        "doing_business_as": "Square", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Square", 
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
use Payline\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "US669rYWoQvFYqHV5kPE8L2E", 
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


from payline.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Square"
	    }, 
	    "user": "US669rYWoQvFYqHV5kPE8L2E", 
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
	        "doing_business_as": "Square", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Square", 
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
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:52:28.44Z",
  "updated_at" : "2017-04-17T23:52:28.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
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
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:52:28.43Z",
  "updated_at" : "2017-04-17T23:55:21.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
## [ADMIN] Disable Settlement Functionality
```shell
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e \
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
  "id" : "APn7hrntyq8KiHRQLi82dkS2",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:52:28.43Z",
  "updated_at" : "2017-04-17T23:55:21.61Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "processors" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "USvsWqRmZMoTxsgKK5DFY4fe",
  "password" : "10b2747d-35e0-410a-adf5-176202f8b506",
  "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:29.70Z",
  "updated_at" : "2017-04-17T23:52:29.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/USvsWqRmZMoTxsgKK5DFY4fe"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
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
  "id" : "PRrfYyjGYWvgL1Z99P9j1U9c",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "default_merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "created_at" : "2017-04-17T23:52:29.17Z",
  "updated_at" : "2017-04-17T23:52:29.17Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2",
    "canDebitBankAccount" : true
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors/PRrfYyjGYWvgL1Z99P9j1U9c"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java

```
```php
<?php

```
```python


from payline.resources import Application

application = Application.get()
```
```ruby

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APn7hrntyq8KiHRQLi82dkS2",
      "enabled" : true,
      "tags" : {
        "application_name" : "Square"
      },
      "owner" : "IDsASSegMz9n8NUNJuzC77Y2",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-04-17T23:52:28.43Z",
      "updated_at" : "2017-04-17T23:52:30.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "processors" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/processors"
        },
        "users" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/users"
        },
        "owner_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/transfers"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/disputes"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/authorizations"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/settlements"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/merchants"
        },
        "identities" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/identities"
        },
        "webhooks" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/webhooks"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/reversals"
        },
        "tokens" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/tokens"
        },
        "application_profile" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2/application_profile"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "merchant_identity": "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeDe5Vm6FoCT4qt43FwAk9A", 
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
    .merchantIdentity("IDkfvquctsLXZszYmnzpe6pv")
    .source("PIeDe5Vm6FoCT4qt43FwAk9A")
    .build()
);


```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeDe5Vm6FoCT4qt43FwAk9A", 
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
	    "merchant_identity": "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIeDe5Vm6FoCT4qt43FwAk9A", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIeDe5Vm6FoCT4qt43FwAk9A", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU8wVfEpFw7U3Kac5r784YRW",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:42.80Z",
  "updated_at" : "2017-04-17T23:52:42.85Z",
  "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:52:42.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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
curl https://api-test.payline.io/authorizations/AU8wVfEpFw7U3Kac5r784YRW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8wVfEpFw7U3Kac5r784YRW");
Long captureAmount = 50L;
Long feeAmount = 10L;
authorization = authorization.capture(captureAmount, feeAmount);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU8wVfEpFw7U3Kac5r784YRW');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU8wVfEpFw7U3Kac5r784YRW")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AU8wVfEpFw7U3Kac5r784YRW")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU8wVfEpFw7U3Kac5r784YRW",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRaA9kwVetidJqm7xjDzjghi",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:42.75Z",
  "updated_at" : "2017-04-17T23:52:43.62Z",
  "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:52:42.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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

curl https://api-test.payline.io/authorizations/AUdB3VzV8v6kkHXrQ7ouTEXQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$authorization = Authorization::retrieve('AU8wVfEpFw7U3Kac5r784YRW');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU8wVfEpFw7U3Kac5r784YRW")
authorization.void()

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AU8wVfEpFw7U3Kac5r784YRW")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AUdB3VzV8v6kkHXrQ7ouTEXQ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:46.09Z",
  "updated_at" : "2017-04-17T23:52:46.68Z",
  "trace_id" : "d4f7abbe-4da3-4870-b153-a8fb6afe7d7e",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : true,
  "expires_at" : "2017-04-24T23:52:46.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AUdB3VzV8v6kkHXrQ7ouTEXQ"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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

curl https://api-test.payline.io/authorizations/AU8wVfEpFw7U3Kac5r784YRW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8wVfEpFw7U3Kac5r784YRW");

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU8wVfEpFw7U3Kac5r784YRW');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU8wVfEpFw7U3Kac5r784YRW")
```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AU8wVfEpFw7U3Kac5r784YRW")


```
> Example Response:

```json
{
  "id" : "AU8wVfEpFw7U3Kac5r784YRW",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRaA9kwVetidJqm7xjDzjghi",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:42.75Z",
  "updated_at" : "2017-04-17T23:52:43.62Z",
  "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:52:42.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
      "id" : "AUdB3VzV8v6kkHXrQ7ouTEXQ",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:46.09Z",
      "updated_at" : "2017-04-17T23:52:46.68Z",
      "trace_id" : "d4f7abbe-4da3-4870-b153-a8fb6afe7d7e",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "is_void" : true,
      "expires_at" : "2017-04-24T23:52:46.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/authorizations/AUdB3VzV8v6kkHXrQ7ouTEXQ"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        }
      }
    }, {
      "id" : "AU8wVfEpFw7U3Kac5r784YRW",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRaA9kwVetidJqm7xjDzjghi",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:42.75Z",
      "updated_at" : "2017-04-17T23:52:43.62Z",
      "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "is_void" : false,
      "expires_at" : "2017-04-24T23:52:42.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/authorizations/AU8wVfEpFw7U3Kac5r784YRW"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
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

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.

## Create an Identity for a Buyer


```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Jones", 
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
	        "first_name"=> "Step", 
	        "last_name"=> "Jones", 
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
	        "first_name": "Step", 
	        "last_name": "Jones", 
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
	        "first_name"=> "Step", 
	        "last_name"=> "Jones", 
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
  "id" : "IDcdWNLK7wa2trGRBcHfyKZo",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
    "last_name" : "Jones",
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
  "created_at" : "2017-04-17T23:52:37.43Z",
  "updated_at" : "2017-04-17T23:52:37.43Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Create an Identity for a Sender
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "ownership_type": "PRIVATE", 
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PawnyCityHall.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDkfvquctsLXZszYmnzpe6pv",
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
  "created_at" : "2017-04-17T23:52:31.53Z",
  "updated_at" : "2017-04-17T23:52:31.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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

`POST https://api-test.payline.io/identities`

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

curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDkfvquctsLXZszYmnzpe6pv");

```
```php
<?php
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
```
```python


from payline.resources import Identity
identity = Identity.get(id="IDkfvquctsLXZszYmnzpe6pv")

```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDkfvquctsLXZszYmnzpe6pv")


```
> Example Response:

```json
{
  "id" : "IDkfvquctsLXZszYmnzpe6pv",
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
  "created_at" : "2017-04-17T23:52:31.52Z",
  "updated_at" : "2017-04-17T23:52:31.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "James", 
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
	        "doing_business_as": "Petes Coffee", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Petes Coffee", 
	        "url": "www.PetesCoffee.com", 
	        "business_name": "Petes Coffee", 
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
identity = Payline::Identity.retrieve(:id=>"IDkfvquctsLXZszYmnzpe6pv")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDkfvquctsLXZszYmnzpe6pv",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "James",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Petes Coffee",
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
    "key" : "value_2"
  },
  "created_at" : "2017-04-17T23:52:31.52Z",
  "updated_at" : "2017-04-17T23:52:56.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd


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
      "id" : "IDcdWNLK7wa2trGRBcHfyKZo",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
        "last_name" : "Jones",
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
      "created_at" : "2017-04-17T23:52:37.42Z",
      "updated_at" : "2017-04-17T23:52:37.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDmBBQrRRSkc97SfqVkwC18g",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:52:35.18Z",
      "updated_at" : "2017-04-17T23:52:35.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDmBBQrRRSkc97SfqVkwC18g/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDkanjWCg1NsrKkViFxyZ9Sf",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:52:34.69Z",
      "updated_at" : "2017-04-17T23:52:34.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDkanjWCg1NsrKkViFxyZ9Sf/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDh7Qyb8GN5iRJGjqXsbsmMN",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:52:34.14Z",
      "updated_at" : "2017-04-17T23:52:34.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDh7Qyb8GN5iRJGjqXsbsmMN/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDad8W1KwKeoVvJispNcbgdr",
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
      "created_at" : "2017-04-17T23:52:33.70Z",
      "updated_at" : "2017-04-17T23:52:33.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDad8W1KwKeoVvJispNcbgdr/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDv2wB3zjt6z9eubkpcqBzTg",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2017-04-17T23:52:33.09Z",
      "updated_at" : "2017-04-17T23:52:33.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDv2wB3zjt6z9eubkpcqBzTg/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDp4xveUWeAZq4xMqz84g3o5",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:52:32.64Z",
      "updated_at" : "2017-04-17T23:52:32.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDp4xveUWeAZq4xMqz84g3o5/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDus9wnpRLpUoFmPGJboXxkV",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "CORPORATION",
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
      "created_at" : "2017-04-17T23:52:32.03Z",
      "updated_at" : "2017-04-17T23:52:32.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDus9wnpRLpUoFmPGJboXxkV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDkfvquctsLXZszYmnzpe6pv",
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
      "created_at" : "2017-04-17T23:52:31.52Z",
      "updated_at" : "2017-04-17T23:52:31.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "IDsASSegMz9n8NUNJuzC77Y2",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Square"
      },
      "created_at" : "2017-04-17T23:52:28.43Z",
      "updated_at" : "2017-04-17T23:52:28.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    "count" : 10
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
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDkfvquctsLXZszYmnzpe6pv")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Payline::Identity.retrieve(:id => "MUu8YQBvNnGb8kJ3eiLcXPkz")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "verification" : "VIf2CTjYEzKVXH1SpqJagYDU",
  "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:36.71Z",
  "updated_at" : "2017-04-17T23:52:36.71Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "verification" : {
      "href" : "https://api-test.payline.io:443/verifications/VIf2CTjYEzKVXH1SpqJagYDU"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUu8YQBvNnGb8kJ3eiLcXPkz");

```
```php
<?php
use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUu8YQBvNnGb8kJ3eiLcXPkz');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUu8YQBvNnGb8kJ3eiLcXPkz")

```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUu8YQBvNnGb8kJ3eiLcXPkz")

```
> Example Response:

```json
{
  "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "verification" : null,
  "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:36.68Z",
  "updated_at" : "2017-04-17T23:52:36.80Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '{}'

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUu8YQBvNnGb8kJ3eiLcXPkz');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUu8YQBvNnGb8kJ3eiLcXPkz")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIphTZP93UPHgKdRkdmEsugq",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:52:57.46Z",
  "updated_at" : "2017-04-17T23:52:57.48Z",
  "trace_id" : "8d792dbc-5e86-432d-8249-90fd06778715",
  "payment_instrument" : null,
  "merchant" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/verifications/VIphTZP93UPHgKdRkdmEsugq"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUu8YQBvNnGb8kJ3eiLcXPkz");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUu8YQBvNnGb8kJ3eiLcXPkz');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUu8YQBvNnGb8kJ3eiLcXPkz")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIphTZP93UPHgKdRkdmEsugq",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:52:57.46Z",
  "updated_at" : "2017-04-17T23:52:57.48Z",
  "trace_id" : "8d792dbc-5e86-432d-8249-90fd06778715",
  "payment_instrument" : null,
  "merchant" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/verifications/VIphTZP93UPHgKdRkdmEsugq"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
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
  "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "verification" : null,
  "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:36.68Z",
  "updated_at" : "2017-04-17T23:55:20.02Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
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
  "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "verification" : null,
  "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:52:36.68Z",
  "updated_at" : "2017-04-17T23:55:20.59Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
      "id" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "verification" : null,
      "merchant_profile" : "MP6T3zP6RiCgq3NrTyN7HFMn",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.80Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io:443/merchant_profiles/MP6T3zP6RiCgq3NrTyN7HFMn"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUu8YQBvNnGb8kJ3eiLcXPkz');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUu8YQBvNnGb8kJ3eiLcXPkz")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIf2CTjYEzKVXH1SpqJagYDU",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.84Z",
      "trace_id" : "7a494597-f93b-4f25-a838-c85afdf7f615",
      "payment_instrument" : null,
      "merchant" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/verifications/VIf2CTjYEzKVXH1SpqJagYDU"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications?offset=0&limit=20&sort=created_at,desc"
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




## [ADMIN] List Merchant Verifications
```shell
curl https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

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
    "verifications" : [ {
      "id" : "VIf2CTjYEzKVXH1SpqJagYDU",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.84Z",
      "trace_id" : "7a494597-f93b-4f25-a838-c85afdf7f615",
      "payment_instrument" : null,
      "merchant" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/verifications/VIf2CTjYEzKVXH1SpqJagYDU"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io:443/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUu8YQBvNnGb8kJ3eiLcXPkz/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "USj8YzBZdpSzQz717yGf5mHP",
  "password" : "8bc696c9-bbc5-409a-8a5c-9e73f7579f9b",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:39.98Z",
  "updated_at" : "2017-04-17T23:52:39.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/USj8YzBZdpSzQz717yGf5mHP"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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


## Associate a Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKvrwB3316K26LVCL4w5wrNN")
            .identity("IDkfvquctsLXZszYmnzpe6pv")
    .build()
);
```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKvrwB3316K26LVCL4w5wrNN", 
	    "type": "TOKEN", 
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}).save()
```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKvrwB3316K26LVCL4w5wrNN", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIvrwB3316K26LVCL4w5wrNN",
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
  "created_at" : "2017-04-17T23:52:45.56Z",
  "updated_at" : "2017-04-17T23:52:45.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/updates"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "name": "Walter Lopez", 
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
	    "identity": "IDcdWNLK7wa2trGRBcHfyKZo"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDkfvquctsLXZszYmnzpe6pv")
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Lopez", 
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
	    "identity"=> "IDcdWNLK7wa2trGRBcHfyKZo"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Lopez", 
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
	    "identity": "IDcdWNLK7wa2trGRBcHfyKZo"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Walter Lopez", 
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
	    "identity"=> "IDcdWNLK7wa2trGRBcHfyKZo"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "fingerprint" : "FPR178541064",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Lopez",
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
  "created_at" : "2017-04-17T23:52:37.91Z",
  "updated_at" : "2017-04-17T23:52:37.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcdWNLK7wa2trGRBcHfyKZo",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/updates"
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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
## Create a Bank Account
```shell

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDkfvquctsLXZszYmnzpe6pv")
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
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
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
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
	    "identity": "IDkfvquctsLXZszYmnzpe6pv"
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
	    "identity"=> "IDkfvquctsLXZszYmnzpe6pv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIxqhZfPQr66EZ82jXqDMoT",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:52:35.65Z",
  "updated_at" : "2017-04-17T23:52:35.65Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
name | *string*, **required** | Account owner's full name (max 40 characters)
## Fetch a Bank Account

```shell
curl https://api-test.payline.io/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIxqhZfPQr66EZ82jXqDMoT")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIxqhZfPQr66EZ82jXqDMoT');

```
```python



```
```ruby
bank_account = Payline::BankAccount.retrieve(:id=> "PIxqhZfPQr66EZ82jXqDMoT")

```
> Example Response:

```json
{
  "id" : "PIxqhZfPQr66EZ82jXqDMoT",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:52:35.62Z",
  "updated_at" : "2017-04-17T23:52:36.19Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIeDe5Vm6FoCT4qt43FwAk9A")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIeDe5Vm6FoCT4qt43FwAk9A');

```
```python



```
```ruby
card = Payline::PaymentCard.retrieve(:id=> "PIeDe5Vm6FoCT4qt43FwAk9A")


```
> Example Response:

```json
{
  "id" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "fingerprint" : "FPR178541064",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Lopez",
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
  "created_at" : "2017-04-17T23:52:37.88Z",
  "updated_at" : "2017-04-17T23:52:42.82Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcdWNLK7wa2trGRBcHfyKZo",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "updates" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/updates"
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
curl https://api-test.payline.io/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "merchant": "MUu8YQBvNnGb8kJ3eiLcXPkz"
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
  "id" : "IU2QiYhwmrFv12rbtjxH51eY",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "merchant" : "MUu8YQBvNnGb8kJ3eiLcXPkz",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-04-17T23:52:47.19Z",
  "updated_at" : "2017-04-17T23:52:47.21Z",
  "payment_instrument" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "trace_id" : "750d727a-0cad-4c6a-b84f-a2e5d9429ae1",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/updates/IU2QiYhwmrFv12rbtjxH51eY"
    },
    "payment_instrument" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd
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
      "id" : "PIvrwB3316K26LVCL4w5wrNN",
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
      "created_at" : "2017-04-17T23:52:45.52Z",
      "updated_at" : "2017-04-17T23:52:45.52Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "updates" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvrwB3316K26LVCL4w5wrNN/updates"
        }
      }
    }, {
      "id" : "PItMcq7JvXG3HR7nfWp9SQF8",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:52:38.35Z",
      "updated_at" : "2017-04-17T23:52:38.35Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDcdWNLK7wa2trGRBcHfyKZo",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "fingerprint" : "FPR178541064",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Walter Lopez",
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
      "created_at" : "2017-04-17T23:52:37.88Z",
      "updated_at" : "2017-04-17T23:52:42.82Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDcdWNLK7wa2trGRBcHfyKZo",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDcdWNLK7wa2trGRBcHfyKZo"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "updates" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A/updates"
        }
      }
    }, {
      "id" : "PIeH2AGbFaKJQxzo3QGYU3Qj",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.68Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeH2AGbFaKJQxzo3QGYU3Qj"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeH2AGbFaKJQxzo3QGYU3Qj/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeH2AGbFaKJQxzo3QGYU3Qj/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeH2AGbFaKJQxzo3QGYU3Qj/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PI9CxWL6Goj3ot427UdcCp4p",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.68Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PI9CxWL6Goj3ot427UdcCp4p"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PI9CxWL6Goj3ot427UdcCp4p/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PI9CxWL6Goj3ot427UdcCp4p/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PI9CxWL6Goj3ot427UdcCp4p/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:36.68Z",
      "updated_at" : "2017-04-17T23:52:36.68Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIxqhZfPQr66EZ82jXqDMoT",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:52:35.62Z",
      "updated_at" : "2017-04-17T23:52:36.19Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIhFHhNUh45AFmyFQQsbBc8L",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:29.14Z",
      "updated_at" : "2017-04-17T23:52:29.14Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PItnsWEXZQF3oFGptV4L9pXf",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:29.14Z",
      "updated_at" : "2017-04-17T23:52:29.14Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIvxfWp2uAivQqmNNqR2UojW",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:29.14Z",
      "updated_at" : "2017-04-17T23:52:29.14Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvxfWp2uAivQqmNNqR2UojW"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvxfWp2uAivQqmNNqR2UojW/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvxfWp2uAivQqmNNqR2UojW/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvxfWp2uAivQqmNNqR2UojW/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "PIvSAgLTCpbS9GdMapugH5Qw",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:52:29.14Z",
      "updated_at" : "2017-04-17T23:52:29.14Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvSAgLTCpbS9GdMapugH5Qw"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvSAgLTCpbS9GdMapugH5Qw/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvSAgLTCpbS9GdMapugH5Qw/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIvSAgLTCpbS9GdMapugH5Qw/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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

curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$identity = Identity::retrieve('IDkfvquctsLXZszYmnzpe6pv');
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

identity = Identity.get(id="IDkfvquctsLXZszYmnzpe6pv")
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
identity = Payline::Identity.retrieve(:id=>"IDkfvquctsLXZszYmnzpe6pv")
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
  "id" : "STcPmNe9qq5kkz3AJ6BSqdVp",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:55:15.90Z",
  "updated_at" : "2017-04-17T23:55:15.93Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 715233,
  "total_fees" : 71524,
  "total_fee" : 71524,
  "net_amount" : 643709,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=debit"
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


curl https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STcPmNe9qq5kkz3AJ6BSqdVp");

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STcPmNe9qq5kkz3AJ6BSqdVp');

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STcPmNe9qq5kkz3AJ6BSqdVp")

```
> Example Response:

```json
{
  "id" : "STcPmNe9qq5kkz3AJ6BSqdVp",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:55:15.86Z",
  "updated_at" : "2017-04-17T23:55:16.84Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 715233,
  "total_fees" : 71524,
  "total_fee" : 71524,
  "net_amount" : 643709,
  "destination" : "PIxqhZfPQr66EZ82jXqDMoT",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PIxqhZfPQr66EZ82jXqDMoT"
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
  "id" : "STcPmNe9qq5kkz3AJ6BSqdVp",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "currency" : "USD",
  "created_at" : "2017-04-17T23:55:15.86Z",
  "updated_at" : "2017-04-17T23:55:16.84Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 715233,
  "total_fees" : 71524,
  "total_fee" : 71524,
  "net_amount" : 643709,
  "destination" : "PIxqhZfPQr66EZ82jXqDMoT",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=debit"
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

`PUT https://api-test.payline.io/settlements/:SETTLEMENT_ID`

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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
      "id" : "STcPmNe9qq5kkz3AJ6BSqdVp",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "currency" : "USD",
      "created_at" : "2017-04-17T23:55:15.86Z",
      "updated_at" : "2017-04-17T23:55:16.84Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 715233,
      "total_fees" : 71524,
      "total_fee" : 71524,
      "net_amount" : 643709,
      "destination" : "PIxqhZfPQr66EZ82jXqDMoT",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-test.payline.io:443/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java
Settlement settlement = client.settlementsClient().fetch("STcPmNe9qq5kkz3AJ6BSqdVp");
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
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STcPmNe9qq5kkz3AJ6BSqdVp');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STcPmNe9qq5kkz3AJ6BSqdVp")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR5fxp9DxXwU2bPoEByAuSYE",
      "amount" : 643709,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "9c62250e-c9a0-42e5-8f60-80fb3dc710ee",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PIxqhZfPQr66EZ82jXqDMoT",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:16.53Z",
      "updated_at" : "2017-04-17T23:55:16.80Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TR5fxp9DxXwU2bPoEByAuSYE"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TR5fxp9DxXwU2bPoEByAuSYE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TR5fxp9DxXwU2bPoEByAuSYE/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TR5fxp9DxXwU2bPoEByAuSYE/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TR5fxp9DxXwU2bPoEByAuSYE/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIxqhZfPQr66EZ82jXqDMoT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java
Settlement settlement = client.settlementsClient().fetch("STcPmNe9qq5kkz3AJ6BSqdVp");
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
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STcPmNe9qq5kkz3AJ6BSqdVp');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"STcPmNe9qq5kkz3AJ6BSqdVp")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRq8TxBVkeuEVZntjvHPtSyd",
      "amount" : 34700,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6ddf3d78-88a3-4869-a0f7-17be04a995af",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PItnsWEXZQF3oFGptV4L9pXf",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:15.28Z",
      "updated_at" : "2017-04-17T23:55:15.50Z",
      "merchant_identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRq8TxBVkeuEVZntjvHPtSyd"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRq8TxBVkeuEVZntjvHPtSyd/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRq8TxBVkeuEVZntjvHPtSyd/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRq8TxBVkeuEVZntjvHPtSyd/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRq8TxBVkeuEVZntjvHPtSyd/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf"
        }
      }
    }, {
      "id" : "TRoJaH8yPT5ajBCPFrsZakSy",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "d482bff0-a530-4c59-b0ee-2a14e08bd94d",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PIhFHhNUh45AFmyFQQsbBc8L",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:15.03Z",
      "updated_at" : "2017-04-17T23:55:15.26Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoJaH8yPT5ajBCPFrsZakSy"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoJaH8yPT5ajBCPFrsZakSy/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoJaH8yPT5ajBCPFrsZakSy/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoJaH8yPT5ajBCPFrsZakSy/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoJaH8yPT5ajBCPFrsZakSy/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L"
        }
      }
    }, {
      "id" : "TRoFHUFEgpCYSsRHBdN7gYvp",
      "amount" : 36791,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "7937989f-c69a-4716-97e1-e2b3d4ebd326",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PItnsWEXZQF3oFGptV4L9pXf",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:14.73Z",
      "updated_at" : "2017-04-17T23:55:14.96Z",
      "merchant_identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoFHUFEgpCYSsRHBdN7gYvp"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoFHUFEgpCYSsRHBdN7gYvp/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDsASSegMz9n8NUNJuzC77Y2"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoFHUFEgpCYSsRHBdN7gYvp/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoFHUFEgpCYSsRHBdN7gYvp/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRoFHUFEgpCYSsRHBdN7gYvp/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItnsWEXZQF3oFGptV4L9pXf"
        }
      }
    }, {
      "id" : "TRi7bbfoJsueKrRn2iKcXHJ5",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c7705436-7032-4155-8a55-9214fe16161b",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PIhFHhNUh45AFmyFQQsbBc8L",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:14.46Z",
      "updated_at" : "2017-04-17T23:55:14.71Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRi7bbfoJsueKrRn2iKcXHJ5"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRi7bbfoJsueKrRn2iKcXHJ5/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRi7bbfoJsueKrRn2iKcXHJ5/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRi7bbfoJsueKrRn2iKcXHJ5/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRi7bbfoJsueKrRn2iKcXHJ5/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L"
        }
      }
    }, {
      "id" : "TR4R3DLdXKopE4JRo5CXhQRo",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "631bb118-8887-4199-86bd-7c42c874d85e",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PIhFHhNUh45AFmyFQQsbBc8L",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:14.13Z",
      "updated_at" : "2017-04-17T23:55:14.42Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TR4R3DLdXKopE4JRo5CXhQRo"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TR4R3DLdXKopE4JRo5CXhQRo/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TR4R3DLdXKopE4JRo5CXhQRo/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TR4R3DLdXKopE4JRo5CXhQRo/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TR4R3DLdXKopE4JRo5CXhQRo/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIhFHhNUh45AFmyFQQsbBc8L"
        }
      }
    }, {
      "id" : "TRaA9kwVetidJqm7xjDzjghi",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:43.51Z",
      "updated_at" : "2017-04-17T23:53:04.18Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    }, {
      "id" : "TRsXVc1jbxzJd67TLwsjTBwM",
      "amount" : 347111,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "da94127e-1522-4112-8c8f-b846ff295f1d",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PItMcq7JvXG3HR7nfWp9SQF8",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 34711,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:39.42Z",
      "updated_at" : "2017-04-17T23:53:05.51Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    }, {
      "id" : "TRubVkEVXLhohBc44a5GRMcP",
      "amount" : 368022,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "30c176a0-6cb7-489e-a198-9bd3af6a3371",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : "2017-04-17T23:55:14.04Z",
      "fee" : 36802,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:38.82Z",
      "updated_at" : "2017-04-17T23:53:03.73Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STcPmNe9qq5kkz3AJ6BSqdVp/transfers?offset=0&limit=20&sort=created_at,desc"
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
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
    -d '
	{
	    "fee": 34711, 
	    "source": "PItMcq7JvXG3HR7nfWp9SQF8", 
	    "merchant_identity": "IDkfvquctsLXZszYmnzpe6pv", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 347111
	}'


```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDkfvquctsLXZszYmnzpe6pv")
      .source("PIeDe5Vm6FoCT4qt43FwAk9A")
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
	    "fee"=> 36802, 
	    "source"=> "PIeDe5Vm6FoCT4qt43FwAk9A", 
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 368022
	));
$debit = $debit->save();
```
```python



```
```ruby
Payline::Transfer.new(
	{
	    "fee"=> 34711, 
	    "source"=> "PItMcq7JvXG3HR7nfWp9SQF8", 
	    "merchant_identity"=> "IDkfvquctsLXZszYmnzpe6pv", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "currency"=> "USD", 
	    "amount"=> 347111
	}}).save
```


> Example Response:

```json
{
  "id" : "TRsXVc1jbxzJd67TLwsjTBwM",
  "amount" : 347111,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "da94127e-1522-4112-8c8f-b846ff295f1d",
  "currency" : "USD",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "source" : "PItMcq7JvXG3HR7nfWp9SQF8",
  "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
  "ready_to_settle_at" : null,
  "fee" : 34711,
  "statement_descriptor" : "PLD*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:39.47Z",
  "updated_at" : "2017-04-17T23:52:39.53Z",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "self" : {
      "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8"
    },
    "destination" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
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

curl https://api-test.payline.io/transfers/TRubVkEVXLhohBc44a5GRMcP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRubVkEVXLhohBc44a5GRMcP");

```
```php
<?php
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRubVkEVXLhohBc44a5GRMcP');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRubVkEVXLhohBc44a5GRMcP")

```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRubVkEVXLhohBc44a5GRMcP")

```
> Example Response:

```json
{
  "id" : "TRubVkEVXLhohBc44a5GRMcP",
  "amount" : 368022,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "30c176a0-6cb7-489e-a198-9bd3af6a3371",
  "currency" : "USD",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
  "ready_to_settle_at" : null,
  "fee" : 36802,
  "statement_descriptor" : "PLD*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:38.82Z",
  "updated_at" : "2017-04-17T23:52:38.95Z",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "self" : {
      "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "destination" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
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

curl https://api-test.payline.io/transfers/TRubVkEVXLhohBc44a5GRMcP/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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

$debit = Transfer::retrieve('TRubVkEVXLhohBc44a5GRMcP');
$refund = $debit->reverse(11);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TRubVkEVXLhohBc44a5GRMcP")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRubVkEVXLhohBc44a5GRMcP")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TR9sp6qcRNRacaC8srWDvX24",
  "amount" : 356061,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "4478adda-7406-418d-921f-c43fbe75c4d1",
  "currency" : "USD",
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
  "destination" : "PIeDe5Vm6FoCT4qt43FwAk9A",
  "ready_to_settle_at" : null,
  "fee" : 35606,
  "statement_descriptor" : "PLD*PAWNY CITY HALL",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:52:41.94Z",
  "updated_at" : "2017-04-17T23:52:42.02Z",
  "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    },
    "self" : {
      "href" : "https://api-test.payline.io:443/transfers/TR9sp6qcRNRacaC8srWDvX24"
    },
    "parent" : {
      "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq"
    },
    "destination" : {
      "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io:443/transfers/TR9sp6qcRNRacaC8srWDvX24/payment_instruments"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
      "id" : "TRaA9kwVetidJqm7xjDzjghi",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "2e61bbb3-6966-42e8-abb9-e57e902ca6df",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:43.51Z",
      "updated_at" : "2017-04-17T23:52:43.62Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRaA9kwVetidJqm7xjDzjghi/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    }, {
      "id" : "TR9sp6qcRNRacaC8srWDvX24",
      "amount" : 356061,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "64456df8-120c-46a1-8346-775680edd1e7",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "destination" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "ready_to_settle_at" : null,
      "fee" : 35606,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:41.82Z",
      "updated_at" : "2017-04-17T23:52:42.02Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TR9sp6qcRNRacaC8srWDvX24"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TR9sp6qcRNRacaC8srWDvX24/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "parent" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        }
      }
    }, {
      "id" : "TRpf2QtVhY2zv3a4pVVkNhWq",
      "amount" : 356061,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "2d1ef62c-84a0-4f0e-affd-e477c83b643a",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : null,
      "fee" : 35606,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:41.27Z",
      "updated_at" : "2017-04-17T23:52:41.90Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRpf2QtVhY2zv3a4pVVkNhWq/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    }, {
      "id" : "TRsXVc1jbxzJd67TLwsjTBwM",
      "amount" : 347111,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "da94127e-1522-4112-8c8f-b846ff295f1d",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PItMcq7JvXG3HR7nfWp9SQF8",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : null,
      "fee" : 34711,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:39.42Z",
      "updated_at" : "2017-04-17T23:52:39.53Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRsXVc1jbxzJd67TLwsjTBwM/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PItMcq7JvXG3HR7nfWp9SQF8"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
        }
      }
    }, {
      "id" : "TRubVkEVXLhohBc44a5GRMcP",
      "amount" : 368022,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "30c176a0-6cb7-489e-a198-9bd3af6a3371",
      "currency" : "USD",
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "source" : "PIeDe5Vm6FoCT4qt43FwAk9A",
      "destination" : "PIwc2bXxnoZCaC2mSLACo5PY",
      "ready_to_settle_at" : null,
      "fee" : 36802,
      "statement_descriptor" : "PLD*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:52:38.82Z",
      "updated_at" : "2017-04-17T23:52:38.95Z",
      "merchant_identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        },
        "self" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io:443/identities/IDkfvquctsLXZszYmnzpe6pv"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io:443/transfers/TRubVkEVXLhohBc44a5GRMcP/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIeDe5Vm6FoCT4qt43FwAk9A"
        },
        "destination" : {
          "href" : "https://api-test.payline.io:443/payment_instruments/PIwc2bXxnoZCaC2mSLACo5PY"
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


## Create ROLE_PARTNER User
```shell
curl https://api-test.payline.io/applications/APn7hrntyq8KiHRQLi82dkS2/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "USvsWqRmZMoTxsgKK5DFY4fe",
  "password" : "10b2747d-35e0-410a-adf5-176202f8b506",
  "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:29.70Z",
  "updated_at" : "2017-04-17T23:52:29.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/USvsWqRmZMoTxsgKK5DFY4fe"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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

## Create ROLE_MERCHANT User
```shell
curl https://api-test.payline.io/identities/IDkfvquctsLXZszYmnzpe6pv/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "USj8YzBZdpSzQz717yGf5mHP",
  "password" : "8bc696c9-bbc5-409a-8a5c-9e73f7579f9b",
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:39.98Z",
  "updated_at" : "2017-04-17T23:52:39.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/USj8YzBZdpSzQz717yGf5mHP"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/users/TRubVkEVXLhohBc44a5GRMcP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```java

```
```php
<?php

```
```python


from payline.resources import User
user = User.get(id="US669rYWoQvFYqHV5kPE8L2E")

```
```ruby

```
> Example Response:

```json
{
  "id" : "US669rYWoQvFYqHV5kPE8L2E",
  "password" : null,
  "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:27.96Z",
  "updated_at" : "2017-04-17T23:52:28.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/US669rYWoQvFYqHV5kPE8L2E"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
curl https://api-test.payline.io/users/USj8YzBZdpSzQz717yGf5mHP \
    -H "Content-Type: application/vnd.json+api" \
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "USj8YzBZdpSzQz717yGf5mHP",
  "password" : null,
  "identity" : "IDkfvquctsLXZszYmnzpe6pv",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:52:39.95Z",
  "updated_at" : "2017-04-17T23:52:40.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/users/USj8YzBZdpSzQz717yGf5mHP"
    },
    "applications" : {
      "href" : "https://api-test.payline.io:443/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

```
```java

```
```php
<?php

```
```python


from payline.resources import User
users = User.get()

```
```ruby

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USj8YzBZdpSzQz717yGf5mHP",
      "password" : null,
      "identity" : "IDkfvquctsLXZszYmnzpe6pv",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-04-17T23:52:39.95Z",
      "updated_at" : "2017-04-17T23:52:40.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/users/USj8YzBZdpSzQz717yGf5mHP"
        },
        "applications" : {
          "href" : "https://api-test.payline.io:443/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "USvsWqRmZMoTxsgKK5DFY4fe",
      "password" : null,
      "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:52:29.68Z",
      "updated_at" : "2017-04-17T23:52:29.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/users/USvsWqRmZMoTxsgKK5DFY4fe"
        },
        "applications" : {
          "href" : "https://api-test.payline.io:443/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
        }
      }
    }, {
      "id" : "US669rYWoQvFYqHV5kPE8L2E",
      "password" : null,
      "identity" : "IDsASSegMz9n8NUNJuzC77Y2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:52:27.96Z",
      "updated_at" : "2017-04-17T23:52:28.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/users/US669rYWoQvFYqHV5kPE8L2E"
        },
        "applications" : {
          "href" : "https://api-test.payline.io:443/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd \
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
  "id" : "WH9MPftA7ee3QJjLgAkAS3T",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "created_at" : "2017-04-17T23:52:31.15Z",
  "updated_at" : "2017-04-17T23:52:31.15Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/webhooks/WH9MPftA7ee3QJjLgAkAS3T"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
    }
  }
}
```

#### HTTP Request

`POST https://api-test.payline.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request (max 120 characters)


## Retrieve a Webhook

```shell



curl https://api-test.payline.io/webhooks/WH9MPftA7ee3QJjLgAkAS3T \
    -H "Content-Type: application/vnd.json+api" \
    -u US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH9MPftA7ee3QJjLgAkAS3T");

```
```php
<?php
use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WH9MPftA7ee3QJjLgAkAS3T');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WH9MPftA7ee3QJjLgAkAS3T")

```
```ruby
webhook = Payline::Webhook.retrieve(:id=> "WH9MPftA7ee3QJjLgAkAS3T")


```
> Example Response:

```json
{
  "id" : "WH9MPftA7ee3QJjLgAkAS3T",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APn7hrntyq8KiHRQLi82dkS2",
  "created_at" : "2017-04-17T23:52:31.15Z",
  "updated_at" : "2017-04-17T23:52:31.15Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io:443/webhooks/WH9MPftA7ee3QJjLgAkAS3T"
    },
    "application" : {
      "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
    -u  US669rYWoQvFYqHV5kPE8L2E:ea99d26c-80c8-4233-adda-fd9a3ee48cfd

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
      "id" : "WH9MPftA7ee3QJjLgAkAS3T",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APn7hrntyq8KiHRQLi82dkS2",
      "created_at" : "2017-04-17T23:52:31.15Z",
      "updated_at" : "2017-04-17T23:52:31.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io:443/webhooks/WH9MPftA7ee3QJjLgAkAS3T"
        },
        "application" : {
          "href" : "https://api-test.payline.io:443/applications/APn7hrntyq8KiHRQLi82dkS2"
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
