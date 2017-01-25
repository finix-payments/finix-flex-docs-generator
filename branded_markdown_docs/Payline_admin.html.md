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

3. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 

4. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
  client.setupUserIdAndPassword("USbcCcbSwtbPuUPamvW57Jw7", "81b4087d-2b77-4400-a3fd-4c96da6c38d4");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USbcCcbSwtbPuUPamvW57Jw7',
	"password" => '81b4087d-2b77-4400-a3fd-4c96da6c38d4']
	);

require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("USbcCcbSwtbPuUPamvW57Jw7", "81b4087d-2b77-4400-a3fd-4c96da6c38d4"))

```
```ruby
# To download the Ruby gem:
# gem install payline-data

require 'payline'

Payline.configure(
    :root_url => 'https://api-test.payline.io',
    :user=>'USbcCcbSwtbPuUPamvW57Jw7',
    :password => '81b4087d-2b77-4400-a3fd-4c96da6c38d4'
)
```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USbcCcbSwtbPuUPamvW57Jw7`

- Password: `81b4087d-2b77-4400-a3fd-4c96da6c38d4`

- Application ID: `APwYzjqMp6o4vzg3emDNrRXp`

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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
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
```python


from payline.resources import Identity

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
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PollosHermanos.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "ID33X2HZb1QNCQMtngS8UeEi",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pollos Hermanos"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-25T01:49:00.92Z",
  "updated_at" : "2017-01-25T01:49:00.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "ID33X2HZb1QNCQMtngS8UeEi"
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
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
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
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
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
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
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	}).save
```
> Example Response:

```json
{
  "id" : "PIt6PPUyJA2zUrPM9girYQH2",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-25T01:49:05.64Z",
  "updated_at" : "2017-01-25T01:49:05.64Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="ID33X2HZb1QNCQMtngS8UeEi")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Payline::Identity.retrieve(:id=>"ID33X2HZb1QNCQMtngS8UeEi")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "verification" : "VIhTgCSTTMm5dKpKi3HRWG4J",
  "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-25T01:49:06.51Z",
  "updated_at" : "2017-01-25T01:49:06.51Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIhTgCSTTMm5dKpKi3HRWG4J"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
	        "last_name": "Chang", 
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
	        "first_name"=> "Jessie", 
	        "last_name"=> "Chang", 
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
	        "first_name": "Jessie", 
	        "last_name": "Chang", 
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
	        "first_name"=> "Jessie", 
	        "last_name"=> "Chang", 
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
  "id" : "IDvxbQ9S38ifm85JKJXP8SMa",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
    "last_name" : "Chang",
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
  "created_at" : "2017-01-25T01:49:07.53Z",
  "updated_at" : "2017-01-25T01:49:07.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "name": "Marcie Le", 
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
	    "identity": "IDvxbQ9S38ifm85JKJXP8SMa"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Le", 
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
	    "identity"=> "IDvxbQ9S38ifm85JKJXP8SMa"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Le", 
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
	    "identity": "IDvxbQ9S38ifm85JKJXP8SMa"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Marcie Le", 
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
	    "identity"=> "IDvxbQ9S38ifm85JKJXP8SMa"
	}).save
```
> Example Response:

```json
{
  "id" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "fingerprint" : "FPR1011272346",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Le",
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
  "created_at" : "2017-01-25T01:49:07.91Z",
  "updated_at" : "2017-01-25T01:49:07.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDvxbQ9S38ifm85JKJXP8SMa",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/updates"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "merchant_identity": "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItLLqh4JbeWNB82nrwHPpWQ", 
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
    .merchantIdentity("MUvAifQNAeQNxHidVdWQoCKq")
    .source("PItLLqh4JbeWNB82nrwHPpWQ")
    .build()
);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
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
	    "merchant_identity": "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUv1xFr5XTXGaTqPs77xftcp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:12.61Z",
  "updated_at" : "2017-01-25T01:49:12.66Z",
  "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : false,
  "expires_at" : "2017-02-01T01:49:12.61Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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
curl https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUv1xFr5XTXGaTqPs77xftcp");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUv1xFr5XTXGaTqPs77xftcp');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUv1xFr5XTXGaTqPs77xftcp")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUv1xFr5XTXGaTqPs77xftcp")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUv1xFr5XTXGaTqPs77xftcp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRhR7QhLTismoSeW7LisRa9m",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:12.54Z",
  "updated_at" : "2017-01-25T01:49:13.29Z",
  "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : false,
  "expires_at" : "2017-02-01T01:49:12.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
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

identity = Identity.get(id="ID33X2HZb1QNCQMtngS8UeEi")
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
identity = Payline::Identity.retrieve(:id=>"ID33X2HZb1QNCQMtngS8UeEi")
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
  "id" : "SThgTHuusMWHNb5WehH82cuw",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "currency" : "USD",
  "created_at" : "2017-01-25T01:51:33.14Z",
  "updated_at" : "2017-01-25T01:51:33.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1139180,
  "total_fees" : 113919,
  "total_fee" : 113919,
  "net_amount" : 1025261,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=debit"
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
          applicationId: 'APwYzjqMp6o4vzg3emDNrRXp',
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
  "id" : "TKt4RX2p8rFpDnxj5uKWSCXe",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-25T01:49:14.22Z",
  "updated_at" : "2017-01-25T01:49:14.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-26T01:49:14.22Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("PIt4RX2p8rFpDnxj5uKWSCXe")
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	}).save
```
> Example Response:

```json
{
  "id" : "PIt4RX2p8rFpDnxj5uKWSCXe",
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
  "created_at" : "2017-01-25T01:49:14.59Z",
  "updated_at" : "2017-01-25T01:49:14.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/updates"
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
  "id" : "USbcCcbSwtbPuUPamvW57Jw7",
  "password" : "81b4087d-2b77-4400-a3fd-4c96da6c38d4",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-25T01:48:57.71Z",
  "updated_at" : "2017-01-25T01:48:57.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USbcCcbSwtbPuUPamvW57Jw7"
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
	        "application_name": "Venmo"
	    }, 
	    "user": "USbcCcbSwtbPuUPamvW57Jw7", 
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
	        "doing_business_as": "Venmo", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Venmo", 
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
	        "application_name"=> "Venmo"
	    ), 
	    "user"=> "USbcCcbSwtbPuUPamvW57Jw7", 
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
	        "doing_business_as"=> "Venmo", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Venmo", 
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-25T01:48:58.13Z",
  "updated_at" : "2017-01-25T01:48:58.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors \
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
  "id" : "PRm8HVwMD6P2Za1CxfmXJAQx",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "default_merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "created_at" : "2017-01-25T01:48:58.87Z",
  "updated_at" : "2017-01-25T01:48:58.87Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors/PRm8HVwMD6P2Za1CxfmXJAQx"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/ \
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-01-25T01:48:58.12Z",
  "updated_at" : "2017-01-25T01:51:39.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/ \
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-25T01:48:58.12Z",
  "updated_at" : "2017-01-25T01:51:40.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
    applicationId: "APwYzjqMp6o4vzg3emDNrRXp",
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
  "id" : "TKt4RX2p8rFpDnxj5uKWSCXe",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-25T01:49:14.22Z",
  "updated_at" : "2017-01-25T01:49:14.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-26T01:49:14.22Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("PIt4RX2p8rFpDnxj5uKWSCXe")
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	}).save
```
> Example Response:

```json
{
  "id" : "PIt4RX2p8rFpDnxj5uKWSCXe",
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
  "created_at" : "2017-01-25T01:49:14.59Z",
  "updated_at" : "2017-01-25T01:49:14.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/updates"
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

## Fetch an Application
```shell
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```java

```
```php
<?php
use Payline\Resources\Application;

$application = Application::retrieve('APwYzjqMp6o4vzg3emDNrRXp');

```
```python


from payline.resources import Application

application = Application.get(id="APwYzjqMp6o4vzg3emDNrRXp")
```
```ruby

```
> Example Response:

```json
{
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-25T01:48:58.12Z",
  "updated_at" : "2017-01-25T01:49:00.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
	        "application_name": "Venmo"
	    }, 
	    "user": "USbcCcbSwtbPuUPamvW57Jw7", 
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
	        "doing_business_as": "Venmo", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Venmo", 
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
	        "application_name"=> "Venmo"
	    ), 
	    "user"=> "USbcCcbSwtbPuUPamvW57Jw7", 
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
	        "doing_business_as"=> "Venmo", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Venmo", 
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
	        "application_name": "Venmo"
	    }, 
	    "user": "USbcCcbSwtbPuUPamvW57Jw7", 
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
	        "doing_business_as": "Venmo", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Venmo", 
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-25T01:48:58.13Z",
  "updated_at" : "2017-01-25T01:48:58.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
## [ADMIN] Disable Processing Functionality
```shell
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/ \
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-01-25T01:48:58.12Z",
  "updated_at" : "2017-01-25T01:51:38.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/ \
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
  "id" : "APwYzjqMp6o4vzg3emDNrRXp",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-25T01:48:58.12Z",
  "updated_at" : "2017-01-25T01:51:38.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "USuJmB3Pan8avbScDU4Xr6ar",
  "password" : "6643ff75-dc07-4f55-b52f-b7942861bf92",
  "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-25T01:48:59.42Z",
  "updated_at" : "2017-01-25T01:48:59.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USuJmB3Pan8avbScDU4Xr6ar"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors \
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
  "id" : "PRm8HVwMD6P2Za1CxfmXJAQx",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "default_merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "created_at" : "2017-01-25T01:48:58.87Z",
  "updated_at" : "2017-01-25T01:48:58.87Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors/PRm8HVwMD6P2Za1CxfmXJAQx"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "APwYzjqMp6o4vzg3emDNrRXp",
      "enabled" : true,
      "tags" : {
        "application_name" : "Venmo"
      },
      "owner" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-01-25T01:48:58.12Z",
      "updated_at" : "2017-01-25T01:49:00.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "processors" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/processors"
        },
        "users" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users"
        },
        "owner_identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/transfers"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/disputes"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/authorizations"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/settlements"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/merchants"
        },
        "identities" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/identities"
        },
        "webhooks" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/webhooks"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/reversals"
        },
        "tokens" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/tokens"
        },
        "application_profile" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/application_profile"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "merchant_identity": "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItLLqh4JbeWNB82nrwHPpWQ", 
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
    .merchantIdentity("MUvAifQNAeQNxHidVdWQoCKq")
    .source("PItLLqh4JbeWNB82nrwHPpWQ")
    .build()
);


```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
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
	    "merchant_identity": "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUv1xFr5XTXGaTqPs77xftcp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:12.61Z",
  "updated_at" : "2017-01-25T01:49:12.66Z",
  "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : false,
  "expires_at" : "2017-02-01T01:49:12.61Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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
curl https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUv1xFr5XTXGaTqPs77xftcp");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUv1xFr5XTXGaTqPs77xftcp');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUv1xFr5XTXGaTqPs77xftcp")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUv1xFr5XTXGaTqPs77xftcp")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUv1xFr5XTXGaTqPs77xftcp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRhR7QhLTismoSeW7LisRa9m",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:12.54Z",
  "updated_at" : "2017-01-25T01:49:13.29Z",
  "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : false,
  "expires_at" : "2017-02-01T01:49:12.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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

curl https://api-test.payline.io/authorizations/AUeXAkcx8q972kPM6rnpNQWz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$authorization = Authorization::retrieve('AUv1xFr5XTXGaTqPs77xftcp');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUv1xFr5XTXGaTqPs77xftcp")
authorization.void()

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUv1xFr5XTXGaTqPs77xftcp")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AUeXAkcx8q972kPM6rnpNQWz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:15.11Z",
  "updated_at" : "2017-01-25T01:49:15.65Z",
  "trace_id" : "ddbbe086-30ed-435f-956c-1a313b5ab65a",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : true,
  "expires_at" : "2017-02-01T01:49:15.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUeXAkcx8q972kPM6rnpNQWz"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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

curl https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUv1xFr5XTXGaTqPs77xftcp");

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUv1xFr5XTXGaTqPs77xftcp');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUv1xFr5XTXGaTqPs77xftcp")
```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUv1xFr5XTXGaTqPs77xftcp")


```
> Example Response:

```json
{
  "id" : "AUv1xFr5XTXGaTqPs77xftcp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRhR7QhLTismoSeW7LisRa9m",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:12.54Z",
  "updated_at" : "2017-01-25T01:49:13.29Z",
  "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "is_void" : false,
  "expires_at" : "2017-02-01T01:49:12.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "AUeXAkcx8q972kPM6rnpNQWz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:15.11Z",
      "updated_at" : "2017-01-25T01:49:15.65Z",
      "trace_id" : "ddbbe086-30ed-435f-956c-1a313b5ab65a",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "is_void" : true,
      "expires_at" : "2017-02-01T01:49:15.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUeXAkcx8q972kPM6rnpNQWz"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        }
      }
    }, {
      "id" : "AUv1xFr5XTXGaTqPs77xftcp",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRhR7QhLTismoSeW7LisRa9m",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:12.54Z",
      "updated_at" : "2017-01-25T01:49:13.29Z",
      "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "is_void" : false,
      "expires_at" : "2017-02-01T01:49:12.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUv1xFr5XTXGaTqPs77xftcp"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
	        "last_name": "Chang", 
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
	        "first_name"=> "Jessie", 
	        "last_name"=> "Chang", 
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
	        "first_name": "Jessie", 
	        "last_name": "Chang", 
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
	        "first_name"=> "Jessie", 
	        "last_name"=> "Chang", 
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
  "id" : "IDvxbQ9S38ifm85JKJXP8SMa",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
    "last_name" : "Chang",
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
  "created_at" : "2017-01-25T01:49:07.53Z",
  "updated_at" : "2017-01-25T01:49:07.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
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
```python


from payline.resources import Identity

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
```ruby
identity = Payline::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PollosHermanos.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "ID33X2HZb1QNCQMtngS8UeEi",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pollos Hermanos"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-25T01:49:00.92Z",
  "updated_at" : "2017-01-25T01:49:00.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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

curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID33X2HZb1QNCQMtngS8UeEi");

```
```php
<?php
use Payline\Resources\Identity;

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
```
```python


from payline.resources import Identity
identity = Identity.get(id="ID33X2HZb1QNCQMtngS8UeEi")

```
```ruby
identity = Payline::Identity.retrieve(:id=>"ID33X2HZb1QNCQMtngS8UeEi")


```
> Example Response:

```json
{
  "id" : "ID33X2HZb1QNCQMtngS8UeEi",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pollos Hermanos"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-25T01:49:00.90Z",
  "updated_at" : "2017-01-25T01:49:00.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
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
identity = Payline::Identity.retrieve(:id=>"ID33X2HZb1QNCQMtngS8UeEi")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "ID33X2HZb1QNCQMtngS8UeEi",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Lopez",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-01-25T01:49:00.90Z",
  "updated_at" : "2017-01-25T01:49:23.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4


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
      "id" : "IDvxbQ9S38ifm85JKJXP8SMa",
      "entity" : {
        "title" : null,
        "first_name" : "Jessie",
        "last_name" : "Chang",
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
      "created_at" : "2017-01-25T01:49:07.51Z",
      "updated_at" : "2017-01-25T01:49:07.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDqT12rbDU3odGW974QdKQ7a",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:05.13Z",
      "updated_at" : "2017-01-25T01:49:05.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqT12rbDU3odGW974QdKQ7a/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "ID6Q71gdydDHsHXgEyGhDouo",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:04.59Z",
      "updated_at" : "2017-01-25T01:49:04.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID6Q71gdydDHsHXgEyGhDouo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDgQLMXJASyvjcgX7pvG79bY",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:03.83Z",
      "updated_at" : "2017-01-25T01:49:03.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDgQLMXJASyvjcgX7pvG79bY/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDi733TvnTFYjqVFPKjofVAx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:03.36Z",
      "updated_at" : "2017-01-25T01:49:03.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDi733TvnTFYjqVFPKjofVAx/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDhDDyowYxDkPeJZkiF5aBr4",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:02.95Z",
      "updated_at" : "2017-01-25T01:49:02.95Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhDDyowYxDkPeJZkiF5aBr4/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDwqB89Ftni8QPkUQgms88Sm",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:02.48Z",
      "updated_at" : "2017-01-25T01:49:02.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwqB89Ftni8QPkUQgms88Sm/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDch8SUZt9rmqTLrVuHX6DTZ",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:02.11Z",
      "updated_at" : "2017-01-25T01:49:02.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDch8SUZt9rmqTLrVuHX6DTZ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDfEn7dGDJMD4CorTZ5LKvEy",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:01.72Z",
      "updated_at" : "2017-01-25T01:49:01.72Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfEn7dGDJMD4CorTZ5LKvEy/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "ID4UwmnKtUpkDcCjPGurPCCF",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:01.35Z",
      "updated_at" : "2017-01-25T01:49:01.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID4UwmnKtUpkDcCjPGurPCCF/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "ID33X2HZb1QNCQMtngS8UeEi",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-25T01:49:00.90Z",
      "updated_at" : "2017-01-25T01:49:00.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "IDdfvsBUNTcEtPP9o4VuDw3b",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2017-01-25T01:48:58.12Z",
      "updated_at" : "2017-01-25T01:48:58.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="ID33X2HZb1QNCQMtngS8UeEi")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Payline::Identity.retrieve(:id => "MUvAifQNAeQNxHidVdWQoCKq")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "verification" : "VIhTgCSTTMm5dKpKi3HRWG4J",
  "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-25T01:49:06.51Z",
  "updated_at" : "2017-01-25T01:49:06.51Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIhTgCSTTMm5dKpKi3HRWG4J"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUvAifQNAeQNxHidVdWQoCKq");

```
```php
<?php
use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUvAifQNAeQNxHidVdWQoCKq');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUvAifQNAeQNxHidVdWQoCKq")

```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUvAifQNAeQNxHidVdWQoCKq")

```
> Example Response:

```json
{
  "id" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "verification" : null,
  "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-25T01:49:06.47Z",
  "updated_at" : "2017-01-25T01:49:06.64Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '{}'

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUvAifQNAeQNxHidVdWQoCKq');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUvAifQNAeQNxHidVdWQoCKq")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIpCYjBkK4riKZryYdnKYCBS",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-25T01:49:24.35Z",
  "updated_at" : "2017-01-25T01:49:24.37Z",
  "trace_id" : "8a629953-4aa5-40ea-a6b4-0ef10c40c6ab",
  "payment_instrument" : null,
  "merchant" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIpCYjBkK4riKZryYdnKYCBS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUvAifQNAeQNxHidVdWQoCKq");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUvAifQNAeQNxHidVdWQoCKq');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUvAifQNAeQNxHidVdWQoCKq")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIpCYjBkK4riKZryYdnKYCBS",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-25T01:49:24.35Z",
  "updated_at" : "2017-01-25T01:49:24.37Z",
  "trace_id" : "8a629953-4aa5-40ea-a6b4-0ef10c40c6ab",
  "payment_instrument" : null,
  "merchant" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIpCYjBkK4riKZryYdnKYCBS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/ \
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
  "id" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "verification" : null,
  "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-25T01:49:06.47Z",
  "updated_at" : "2017-01-25T01:51:37.32Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/ \
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
  "id" : "MUvAifQNAeQNxHidVdWQoCKq",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "verification" : null,
  "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-25T01:49:06.47Z",
  "updated_at" : "2017-01-25T01:51:37.80Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "MUvAifQNAeQNxHidVdWQoCKq",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "verification" : null,
      "merchant_profile" : "MP98whdVQFZdsj3isgDXFpXo",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.64Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MP98whdVQFZdsj3isgDXFpXo"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MUvAifQNAeQNxHidVdWQoCKq');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MUvAifQNAeQNxHidVdWQoCKq")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIhTgCSTTMm5dKpKi3HRWG4J",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.73Z",
      "trace_id" : "b34699f7-92bd-45df-a67f-227d9629910f",
      "payment_instrument" : null,
      "merchant" : "MUvAifQNAeQNxHidVdWQoCKq",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/verifications/VIhTgCSTTMm5dKpKi3HRWG4J"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications \
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
      "id" : "VIhTgCSTTMm5dKpKi3HRWG4J",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.73Z",
      "trace_id" : "b34699f7-92bd-45df-a67f-227d9629910f",
      "payment_instrument" : null,
      "merchant" : "MUvAifQNAeQNxHidVdWQoCKq",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/verifications/VIhTgCSTTMm5dKpKi3HRWG4J"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUvAifQNAeQNxHidVdWQoCKq/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "UStjcEyyBoPVN1ojYo2FzeZJ",
  "password" : "a191d9e9-ed28-4ebf-ac28-a9e2c8a5ab31",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-25T01:49:09.82Z",
  "updated_at" : "2017-01-25T01:49:09.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UStjcEyyBoPVN1ojYo2FzeZJ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("PIt4RX2p8rFpDnxj5uKWSCXe")
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
    .build();
);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type": "TOKEN", 
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}).save()
```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TKt4RX2p8rFpDnxj5uKWSCXe", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	}).save
```
> Example Response:

```json
{
  "id" : "PIt4RX2p8rFpDnxj5uKWSCXe",
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
  "created_at" : "2017-01-25T01:49:14.59Z",
  "updated_at" : "2017-01-25T01:49:14.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/updates"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "name": "Marcie Le", 
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
	    "identity": "IDvxbQ9S38ifm85JKJXP8SMa"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Le", 
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
	    "identity"=> "IDvxbQ9S38ifm85JKJXP8SMa"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Le", 
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
	    "identity": "IDvxbQ9S38ifm85JKJXP8SMa"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Marcie Le", 
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
	    "identity"=> "IDvxbQ9S38ifm85JKJXP8SMa"
	}).save
```
> Example Response:

```json
{
  "id" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "fingerprint" : "FPR1011272346",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Le",
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
  "created_at" : "2017-01-25T01:49:07.91Z",
  "updated_at" : "2017-01-25T01:49:07.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDvxbQ9S38ifm85JKJXP8SMa",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/updates"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("ID33X2HZb1QNCQMtngS8UeEi")
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
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
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
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
	    "identity": "ID33X2HZb1QNCQMtngS8UeEi"
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
	    "identity"=> "ID33X2HZb1QNCQMtngS8UeEi"
	}).save
```
> Example Response:

```json
{
  "id" : "PIt6PPUyJA2zUrPM9girYQH2",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-25T01:49:05.64Z",
  "updated_at" : "2017-01-25T01:49:05.64Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
## Fetch a Bank Account

```shell
curl https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIt6PPUyJA2zUrPM9girYQH2")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIt6PPUyJA2zUrPM9girYQH2');

```
```python



```
```ruby
bank_account = Payline::BankAccount.retrieve(:id=> "PIt6PPUyJA2zUrPM9girYQH2")

```
> Example Response:

```json
{
  "id" : "PIt6PPUyJA2zUrPM9girYQH2",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-25T01:49:05.61Z",
  "updated_at" : "2017-01-25T01:49:06.04Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PItLLqh4JbeWNB82nrwHPpWQ")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PItLLqh4JbeWNB82nrwHPpWQ');

```
```python



```
```ruby
card = Payline::PaymentCard.retrieve(:id=> "PItLLqh4JbeWNB82nrwHPpWQ")


```
> Example Response:

```json
{
  "id" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "fingerprint" : "FPR1011272346",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Le",
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
  "created_at" : "2017-01-25T01:49:07.86Z",
  "updated_at" : "2017-01-25T01:49:12.63Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDvxbQ9S38ifm85JKJXP8SMa",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/updates"
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
curl https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "merchant": "MUvAifQNAeQNxHidVdWQoCKq"
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
  "id" : "IUx1xihDeV9XftjQtXrGpS4t",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "merchant" : "MUvAifQNAeQNxHidVdWQoCKq",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-01-25T01:49:16.31Z",
  "updated_at" : "2017-01-25T01:49:16.33Z",
  "payment_instrument" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "trace_id" : "7ce26abb-d383-4097-9558-6715b098ebf7",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/updates/IUx1xihDeV9XftjQtXrGpS4t"
    },
    "payment_instrument" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4
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
      "id" : "PIt4RX2p8rFpDnxj5uKWSCXe",
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
      "created_at" : "2017-01-25T01:49:14.55Z",
      "updated_at" : "2017-01-25T01:49:14.55Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt4RX2p8rFpDnxj5uKWSCXe/updates"
        }
      }
    }, {
      "id" : "PIbR3KsEWZeyTf5puvaQorDb",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-25T01:49:08.26Z",
      "updated_at" : "2017-01-25T01:49:08.26Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDvxbQ9S38ifm85JKJXP8SMa",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbR3KsEWZeyTf5puvaQorDb"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbR3KsEWZeyTf5puvaQorDb/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbR3KsEWZeyTf5puvaQorDb/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbR3KsEWZeyTf5puvaQorDb/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "fingerprint" : "FPR1011272346",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marcie Le",
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
      "created_at" : "2017-01-25T01:49:07.86Z",
      "updated_at" : "2017-01-25T01:49:12.63Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDvxbQ9S38ifm85JKJXP8SMa",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDvxbQ9S38ifm85JKJXP8SMa"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ/updates"
        }
      }
    }, {
      "id" : "PIvnVdMuMz75tB4frDkDDYof",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.47Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvnVdMuMz75tB4frDkDDYof"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvnVdMuMz75tB4frDkDDYof/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvnVdMuMz75tB4frDkDDYof/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvnVdMuMz75tB4frDkDDYof/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.47Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PI4HXHcaxXNJ6CoKHULZPnmb",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:49:06.47Z",
      "updated_at" : "2017-01-25T01:49:06.47Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4HXHcaxXNJ6CoKHULZPnmb"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4HXHcaxXNJ6CoKHULZPnmb/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4HXHcaxXNJ6CoKHULZPnmb/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4HXHcaxXNJ6CoKHULZPnmb/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PIt6PPUyJA2zUrPM9girYQH2",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-25T01:49:05.61Z",
      "updated_at" : "2017-01-25T01:49:06.04Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PIkZy8oTT8Ddsg9bBvLjwrQt",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:48:58.83Z",
      "updated_at" : "2017-01-25T01:48:58.83Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIkZy8oTT8Ddsg9bBvLjwrQt"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIkZy8oTT8Ddsg9bBvLjwrQt/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIkZy8oTT8Ddsg9bBvLjwrQt/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIkZy8oTT8Ddsg9bBvLjwrQt/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PIcmUYRcB91eTFRGqvMeiD9m",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:48:58.83Z",
      "updated_at" : "2017-01-25T01:48:58.83Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcmUYRcB91eTFRGqvMeiD9m"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcmUYRcB91eTFRGqvMeiD9m/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcmUYRcB91eTFRGqvMeiD9m/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcmUYRcB91eTFRGqvMeiD9m/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PIgKiL7QBybo8zvwiVkXjD1N",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:48:58.83Z",
      "updated_at" : "2017-01-25T01:48:58.83Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "PIxsHypBGxpjpvmdm1zicmTR",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-25T01:48:58.83Z",
      "updated_at" : "2017-01-25T01:48:58.83Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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

curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$identity = Identity::retrieve('ID33X2HZb1QNCQMtngS8UeEi');
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

identity = Identity.get(id="ID33X2HZb1QNCQMtngS8UeEi")
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
identity = Payline::Identity.retrieve(:id=>"ID33X2HZb1QNCQMtngS8UeEi")
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
  "id" : "SThgTHuusMWHNb5WehH82cuw",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "currency" : "USD",
  "created_at" : "2017-01-25T01:51:33.14Z",
  "updated_at" : "2017-01-25T01:51:33.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1139180,
  "total_fees" : 113919,
  "total_fee" : 113919,
  "net_amount" : 1025261,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=debit"
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


curl https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("SThgTHuusMWHNb5WehH82cuw");

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('SThgTHuusMWHNb5WehH82cuw');

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"SThgTHuusMWHNb5WehH82cuw")

```
> Example Response:

```json
{
  "id" : "SThgTHuusMWHNb5WehH82cuw",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "currency" : "USD",
  "created_at" : "2017-01-25T01:51:33.10Z",
  "updated_at" : "2017-01-25T01:51:34.09Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1139180,
  "total_fees" : 113919,
  "total_fee" : 113919,
  "net_amount" : 1025261,
  "destination" : "PIt6PPUyJA2zUrPM9girYQH2",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PIt6PPUyJA2zUrPM9girYQH2"
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
  "id" : "SThgTHuusMWHNb5WehH82cuw",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "currency" : "USD",
  "created_at" : "2017-01-25T01:51:33.10Z",
  "updated_at" : "2017-01-25T01:51:34.09Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1139180,
  "total_fees" : 113919,
  "total_fee" : 113919,
  "net_amount" : 1025261,
  "destination" : "PIt6PPUyJA2zUrPM9girYQH2",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=debit"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "SThgTHuusMWHNb5WehH82cuw",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "currency" : "USD",
      "created_at" : "2017-01-25T01:51:33.10Z",
      "updated_at" : "2017-01-25T01:51:34.09Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 1139180,
      "total_fees" : 113919,
      "total_fee" : 113919,
      "net_amount" : 1025261,
      "destination" : "PIt6PPUyJA2zUrPM9girYQH2",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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

$settlement = Settlement::retrieve('SThgTHuusMWHNb5WehH82cuw');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"SThgTHuusMWHNb5WehH82cuw")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRmRaX6Xy5PCrSu6FxHFuJsP",
      "amount" : 1025261,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "5a287ef2-a649-4fd7-b2a8-b3977cd5b8e4",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIt6PPUyJA2zUrPM9girYQH2",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:33.74Z",
      "updated_at" : "2017-01-25T01:51:34.03Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRmRaX6Xy5PCrSu6FxHFuJsP"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRmRaX6Xy5PCrSu6FxHFuJsP/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRmRaX6Xy5PCrSu6FxHFuJsP/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRmRaX6Xy5PCrSu6FxHFuJsP/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRmRaX6Xy5PCrSu6FxHFuJsP/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIt6PPUyJA2zUrPM9girYQH2"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

```
```java

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('SThgTHuusMWHNb5WehH82cuw');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"SThgTHuusMWHNb5WehH82cuw")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRnGsVsGfDZwi5kERWfKZqQX",
      "amount" : 44598,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "07c42666-09c7-4756-a391-7081df0323ab",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIgKiL7QBybo8zvwiVkXjD1N",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:32.50Z",
      "updated_at" : "2017-01-25T01:51:32.72Z",
      "merchant_identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRnGsVsGfDZwi5kERWfKZqQX"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRnGsVsGfDZwi5kERWfKZqQX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRnGsVsGfDZwi5kERWfKZqQX/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRnGsVsGfDZwi5kERWfKZqQX/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRnGsVsGfDZwi5kERWfKZqQX/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N"
        }
      }
    }, {
      "id" : "TRifBJnegVmHsrz9bfXBiz44",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c42bc8f3-0fea-400a-b911-f0c940940012",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIxsHypBGxpjpvmdm1zicmTR",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:32.27Z",
      "updated_at" : "2017-01-25T01:51:32.48Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRifBJnegVmHsrz9bfXBiz44"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRifBJnegVmHsrz9bfXBiz44/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRifBJnegVmHsrz9bfXBiz44/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRifBJnegVmHsrz9bfXBiz44/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRifBJnegVmHsrz9bfXBiz44/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR"
        }
      }
    }, {
      "id" : "TRq7SP23wWE28r9V9tASTTMt",
      "amount" : 69288,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "660f5b65-dcf7-4902-b52c-384a4de0bdfa",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIgKiL7QBybo8zvwiVkXjD1N",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:31.85Z",
      "updated_at" : "2017-01-25T01:51:32.22Z",
      "merchant_identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRq7SP23wWE28r9V9tASTTMt"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRq7SP23wWE28r9V9tASTTMt/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDdfvsBUNTcEtPP9o4VuDw3b"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRq7SP23wWE28r9V9tASTTMt/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRq7SP23wWE28r9V9tASTTMt/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRq7SP23wWE28r9V9tASTTMt/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgKiL7QBybo8zvwiVkXjD1N"
        }
      }
    }, {
      "id" : "TReQEYXEoH9ZriyGGz7xmABR",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "0fca4e5d-9cbf-42aa-9eae-05cb843b2b02",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIxsHypBGxpjpvmdm1zicmTR",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:31.62Z",
      "updated_at" : "2017-01-25T01:51:31.83Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TReQEYXEoH9ZriyGGz7xmABR"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TReQEYXEoH9ZriyGGz7xmABR/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TReQEYXEoH9ZriyGGz7xmABR/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TReQEYXEoH9ZriyGGz7xmABR/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TReQEYXEoH9ZriyGGz7xmABR/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR"
        }
      }
    }, {
      "id" : "TR7xUCfNY2fMduPfFCQr3w9J",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c1d49201-3239-44ca-8642-53b59ca2f66a",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PIxsHypBGxpjpvmdm1zicmTR",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:51:31.28Z",
      "updated_at" : "2017-01-25T01:51:31.57Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR7xUCfNY2fMduPfFCQr3w9J"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR7xUCfNY2fMduPfFCQr3w9J/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR7xUCfNY2fMduPfFCQr3w9J/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR7xUCfNY2fMduPfFCQr3w9J/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR7xUCfNY2fMduPfFCQr3w9J/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxsHypBGxpjpvmdm1zicmTR"
        }
      }
    }, {
      "id" : "TRhR7QhLTismoSeW7LisRa9m",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:13.15Z",
      "updated_at" : "2017-01-25T01:50:05.18Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    }, {
      "id" : "TRshxxCUSsxqcYwAZ8H5Q9E9",
      "amount" : 446087,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "e354e2fe-c2d5-4480-8ec9-6f4eac16ddbf",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 44609,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:09.29Z",
      "updated_at" : "2017-01-25T01:50:07.60Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    }, {
      "id" : "TRexW2GvnxirWZqk6JtXnCRg",
      "amount" : 692993,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "44992b49-1e6d-4904-b5d3-a6936d6d2270",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : "2017-01-25T01:51:31.20Z",
      "fee" : 69299,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:08.69Z",
      "updated_at" : "2017-01-25T01:50:07.75Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/SThgTHuusMWHNb5WehH82cuw/transfers?offset=0&limit=20&sort=created_at,desc"
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

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
    -d '
	{
	    "fee": 44609, 
	    "source": "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "merchant_identity": "ID33X2HZb1QNCQMtngS8UeEi", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 446087
	}'


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
```php
<?php
use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 69299, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 692993
	));
$debit = $debit->save();
```
```python



```
```ruby
Payline::Transfer.new(
	{
	    "fee"=> 44609, 
	    "source"=> "PItLLqh4JbeWNB82nrwHPpWQ", 
	    "merchant_identity"=> "ID33X2HZb1QNCQMtngS8UeEi", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "currency"=> "USD", 
	    "amount"=> 446087
	}}).save
```


> Example Response:

```json
{
  "id" : "TRshxxCUSsxqcYwAZ8H5Q9E9",
  "amount" : 446087,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "e354e2fe-c2d5-4480-8ec9-6f4eac16ddbf",
  "currency" : "USD",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
  "ready_to_settle_at" : null,
  "fee" : 44609,
  "statement_descriptor" : "PLD*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:09.35Z",
  "updated_at" : "2017-01-25T01:49:09.43Z",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
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

curl https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRexW2GvnxirWZqk6JtXnCRg");

```
```php
<?php
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRexW2GvnxirWZqk6JtXnCRg');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRexW2GvnxirWZqk6JtXnCRg")

```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRexW2GvnxirWZqk6JtXnCRg")

```
> Example Response:

```json
{
  "id" : "TRexW2GvnxirWZqk6JtXnCRg",
  "amount" : 692993,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "44992b49-1e6d-4904-b5d3-a6936d6d2270",
  "currency" : "USD",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
  "ready_to_settle_at" : null,
  "fee" : 69299,
  "statement_descriptor" : "PLD*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:08.69Z",
  "updated_at" : "2017-01-25T01:49:08.87Z",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
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

curl https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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

$debit = Transfer::retrieve('TRexW2GvnxirWZqk6JtXnCRg');
$refund = $debit->reverse(11);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TRexW2GvnxirWZqk6JtXnCRg")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRexW2GvnxirWZqk6JtXnCRg")

refund = Payline::Transfer.reverse(
          {
          "refund_amount" => 100
        }
        ).save
```
> Example Response:

```json
{
  "id" : "TR7zgAEXiJyBfhbCedUDkuwv",
  "amount" : 264428,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "353bfd25-19a5-4181-a6b1-094258656b21",
  "currency" : "USD",
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
  "destination" : "PItLLqh4JbeWNB82nrwHPpWQ",
  "ready_to_settle_at" : null,
  "fee" : 26443,
  "statement_descriptor" : "PLD*POLLOS HERMANOS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-25T01:49:11.70Z",
  "updated_at" : "2017-01-25T01:49:11.80Z",
  "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR7zgAEXiJyBfhbCedUDkuwv"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR7zgAEXiJyBfhbCedUDkuwv/payment_instruments"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "TRhR7QhLTismoSeW7LisRa9m",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "3aea4c4e-3e65-4707-9120-3d4acd9bd485",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:13.15Z",
      "updated_at" : "2017-01-25T01:49:13.29Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRhR7QhLTismoSeW7LisRa9m/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    }, {
      "id" : "TR7zgAEXiJyBfhbCedUDkuwv",
      "amount" : 264428,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "dbf20f78-d26b-4eb3-b297-da8d808f94ec",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "destination" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "ready_to_settle_at" : null,
      "fee" : 26443,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:11.53Z",
      "updated_at" : "2017-01-25T01:49:11.80Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR7zgAEXiJyBfhbCedUDkuwv"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR7zgAEXiJyBfhbCedUDkuwv/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        }
      }
    }, {
      "id" : "TR8pjN1obyshWnbDXuMFRZrK",
      "amount" : 264428,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "6985b6f6-ddae-4650-bc89-9633d7389aa8",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : null,
      "fee" : 26443,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:10.98Z",
      "updated_at" : "2017-01-25T01:49:11.65Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR8pjN1obyshWnbDXuMFRZrK/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    }, {
      "id" : "TRshxxCUSsxqcYwAZ8H5Q9E9",
      "amount" : 446087,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "e354e2fe-c2d5-4480-8ec9-6f4eac16ddbf",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : null,
      "fee" : 44609,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:09.29Z",
      "updated_at" : "2017-01-25T01:49:09.43Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRshxxCUSsxqcYwAZ8H5Q9E9/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
        }
      }
    }, {
      "id" : "TRexW2GvnxirWZqk6JtXnCRg",
      "amount" : 692993,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "44992b49-1e6d-4904-b5d3-a6936d6d2270",
      "currency" : "USD",
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "source" : "PItLLqh4JbeWNB82nrwHPpWQ",
      "destination" : "PI2y1DcZxhWcMdxgPbueKzFY",
      "ready_to_settle_at" : null,
      "fee" : 69299,
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-25T01:49:08.69Z",
      "updated_at" : "2017-01-25T01:49:08.87Z",
      "merchant_identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRexW2GvnxirWZqk6JtXnCRg/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItLLqh4JbeWNB82nrwHPpWQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2y1DcZxhWcMdxgPbueKzFY"
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


## Create an Application User
```shell
curl https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "USuJmB3Pan8avbScDU4Xr6ar",
  "password" : "6643ff75-dc07-4f55-b52f-b7942861bf92",
  "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-25T01:48:59.42Z",
  "updated_at" : "2017-01-25T01:48:59.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USuJmB3Pan8avbScDU4Xr6ar"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/identities/ID33X2HZb1QNCQMtngS8UeEi/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "UStjcEyyBoPVN1ojYo2FzeZJ",
  "password" : "a191d9e9-ed28-4ebf-ac28-a9e2c8a5ab31",
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-25T01:49:09.82Z",
  "updated_at" : "2017-01-25T01:49:09.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UStjcEyyBoPVN1ojYo2FzeZJ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/users/TRexW2GvnxirWZqk6JtXnCRg \
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
user = User.get(id="USbcCcbSwtbPuUPamvW57Jw7")

```
```ruby

```
> Example Response:

```json
{
  "id" : "USbcCcbSwtbPuUPamvW57Jw7",
  "password" : null,
  "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-25T01:48:57.70Z",
  "updated_at" : "2017-01-25T01:48:58.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USbcCcbSwtbPuUPamvW57Jw7"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
curl https://api-test.payline.io/users/UStjcEyyBoPVN1ojYo2FzeZJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "UStjcEyyBoPVN1ojYo2FzeZJ",
  "password" : null,
  "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-25T01:49:09.79Z",
  "updated_at" : "2017-01-25T01:49:10.25Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UStjcEyyBoPVN1ojYo2FzeZJ"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "UStjcEyyBoPVN1ojYo2FzeZJ",
      "password" : null,
      "identity" : "ID33X2HZb1QNCQMtngS8UeEi",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-01-25T01:49:09.79Z",
      "updated_at" : "2017-01-25T01:49:10.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/UStjcEyyBoPVN1ojYo2FzeZJ"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "USuJmB3Pan8avbScDU4Xr6ar",
      "password" : null,
      "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-25T01:48:59.40Z",
      "updated_at" : "2017-01-25T01:48:59.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USuJmB3Pan8avbScDU4Xr6ar"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
        }
      }
    }, {
      "id" : "USbcCcbSwtbPuUPamvW57Jw7",
      "password" : null,
      "identity" : "IDdfvsBUNTcEtPP9o4VuDw3b",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-25T01:48:57.70Z",
      "updated_at" : "2017-01-25T01:48:58.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USbcCcbSwtbPuUPamvW57Jw7"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4 \
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
  "id" : "WHbKeScbK9bKf6sqvAtERx2o",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "created_at" : "2017-01-25T01:49:00.59Z",
  "updated_at" : "2017-01-25T01:49:00.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHbKeScbK9bKf6sqvAtERx2o"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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



curl https://api-test.payline.io/webhooks/WHbKeScbK9bKf6sqvAtERx2o \
    -H "Content-Type: application/vnd.json+api" \
    -u USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHbKeScbK9bKf6sqvAtERx2o");

```
```php
<?php
use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHbKeScbK9bKf6sqvAtERx2o');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WHbKeScbK9bKf6sqvAtERx2o")

```
```ruby
webhook = Payline::Webhook.retrieve(:id=> "WHbKeScbK9bKf6sqvAtERx2o")


```
> Example Response:

```json
{
  "id" : "WHbKeScbK9bKf6sqvAtERx2o",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APwYzjqMp6o4vzg3emDNrRXp",
  "created_at" : "2017-01-25T01:49:00.60Z",
  "updated_at" : "2017-01-25T01:49:00.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHbKeScbK9bKf6sqvAtERx2o"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
    -u  USbcCcbSwtbPuUPamvW57Jw7:81b4087d-2b77-4400-a3fd-4c96da6c38d4

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
      "id" : "WHbKeScbK9bKf6sqvAtERx2o",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APwYzjqMp6o4vzg3emDNrRXp",
      "created_at" : "2017-01-25T01:49:00.60Z",
      "updated_at" : "2017-01-25T01:49:00.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHbKeScbK9bKf6sqvAtERx2o"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APwYzjqMp6o4vzg3emDNrRXp"
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
