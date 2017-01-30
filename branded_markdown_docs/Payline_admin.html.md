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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
  client.setupUserIdAndPassword("US6Qjhi6PFP5pH7nrujts3Lu", "879a7227-1c51-4de5-91e4-32044cfc12e5");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'US6Qjhi6PFP5pH7nrujts3Lu',
	"password" => '879a7227-1c51-4de5-91e4-32044cfc12e5']
	);

require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("US6Qjhi6PFP5pH7nrujts3Lu", "879a7227-1c51-4de5-91e4-32044cfc12e5"))

```
```ruby
# To download the Ruby gem:
# gem install payline-data

require 'payline'

Payline.configure(
    :root_url => 'https://api-test.payline.io',
    :user=>'US6Qjhi6PFP5pH7nrujts3Lu',
    :password => '879a7227-1c51-4de5-91e4-32044cfc12e5'
)
```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US6Qjhi6PFP5pH7nrujts3Lu`

- Password: `879a7227-1c51-4de5-91e4-32044cfc12e5`

- Application ID: `APxisMF2hLsbZqe2q9cyRYUt`

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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
	        "amex_mid"=> "12345678910", 
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
	        "amex_mid": "12345678910", 
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
	        "amex_mid"=> "12345678910", 
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
  "id" : "IDwj12xXD4h5hewgMoxyPjUR",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:54:23.60Z",
  "updated_at" : "2017-01-27T18:54:23.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDwj12xXD4h5hewgMoxyPjUR"
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
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
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
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
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
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
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeYoYSpVci2YDsA7uV9uctN",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:54:27.57Z",
  "updated_at" : "2017-01-27T18:54:27.57Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDwj12xXD4h5hewgMoxyPjUR")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDwj12xXD4h5hewgMoxyPjUR")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "verification" : "VIsmg72dp61gWofHX9HeiBUU",
  "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:54:28.59Z",
  "updated_at" : "2017-01-27T18:54:28.59Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIsmg72dp61gWofHX9HeiBUU"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
	        "last_name": "James", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "James", 
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
	        "first_name": "Bob", 
	        "last_name": "James", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "James", 
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
  "id" : "IDi7TvzGiUFezC2HZ9CmGnyB",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
    "last_name" : "James",
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
  "created_at" : "2017-01-27T18:54:29.34Z",
  "updated_at" : "2017-01-27T18:54:29.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "name": "Fran Serna", 
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
	    "identity": "IDi7TvzGiUFezC2HZ9CmGnyB"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
$card = new PaymentCard(
	array(
	    "name"=> "Fran Serna", 
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
	    "identity"=> "IDi7TvzGiUFezC2HZ9CmGnyB"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Fran Serna", 
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
	    "identity": "IDi7TvzGiUFezC2HZ9CmGnyB"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Fran Serna", 
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
	    "identity"=> "IDi7TvzGiUFezC2HZ9CmGnyB"
	}).save
```
> Example Response:

```json
{
  "id" : "PIjPjRJd9qia891Wv3qw7qhp",
  "fingerprint" : "FPR-1970802456",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Serna",
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
  "created_at" : "2017-01-27T18:54:29.73Z",
  "updated_at" : "2017-01-27T18:54:29.73Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDi7TvzGiUFezC2HZ9CmGnyB",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/updates"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "merchant_identity": "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIjPjRJd9qia891Wv3qw7qhp", 
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
    .merchantIdentity("IDwj12xXD4h5hewgMoxyPjUR")
    .source("PIjPjRJd9qia891Wv3qw7qhp")
    .build()
);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIjPjRJd9qia891Wv3qw7qhp", 
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
	    "merchant_identity": "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIjPjRJd9qia891Wv3qw7qhp", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIjPjRJd9qia891Wv3qw7qhp", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:34.20Z",
  "updated_at" : "2017-01-27T18:54:34.25Z",
  "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:54:34.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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
curl https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUmMbKD8iEEV8LZHDFy6mXtE");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUmMbKD8iEEV8LZHDFy6mXtE');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUmMbKD8iEEV8LZHDFy6mXtE")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUmMbKD8iEEV8LZHDFy6mXtE")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6nqgvHhVKi59PCeLbedm63",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:34.16Z",
  "updated_at" : "2017-01-27T18:54:34.76Z",
  "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:54:34.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
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

identity = Identity.get(id="IDwj12xXD4h5hewgMoxyPjUR")
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
identity = Payline::Identity.retrieve(:id=>"IDwj12xXD4h5hewgMoxyPjUR")
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
  "id" : "ST2a4SPHbCSCTeWu8U3jzEVt",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:58:20.31Z",
  "updated_at" : "2017-01-27T18:58:20.35Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 558206,
  "total_fees" : 55822,
  "total_fee" : 55822,
  "net_amount" : 502384,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=debit"
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
          applicationId: 'APxisMF2hLsbZqe2q9cyRYUt',
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
  "id" : "TK7VLd7UbhmkJ3x64DLxkLi9",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-27T18:54:35.67Z",
  "updated_at" : "2017-01-27T18:54:35.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-28T18:54:35.67Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TK7VLd7UbhmkJ3x64DLxkLi9")
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7VLd7UbhmkJ3x64DLxkLi9",
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
  "created_at" : "2017-01-27T18:54:36.03Z",
  "updated_at" : "2017-01-27T18:54:36.03Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/updates"
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
  "id" : "US6Qjhi6PFP5pH7nrujts3Lu",
  "password" : "879a7227-1c51-4de5-91e4-32044cfc12e5",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:20.29Z",
  "updated_at" : "2017-01-27T18:54:20.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/US6Qjhi6PFP5pH7nrujts3Lu"
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
	        "application_name": "Square"
	    }, 
	    "user": "US6Qjhi6PFP5pH7nrujts3Lu", 
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
	    "user"=> "US6Qjhi6PFP5pH7nrujts3Lu", 
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:54:20.78Z",
  "updated_at" : "2017-01-27T18:54:20.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (If business type is INDIVIDUAL_SOLE_PROPRIETORSHIP, please input 100) 
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors \
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
  "id" : "PR43TF9wJF4rhQcwsrYHmoxF",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "default_merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "created_at" : "2017-01-27T18:54:21.58Z",
  "updated_at" : "2017-01-27T18:54:21.58Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors/PR43TF9wJF4rhQcwsrYHmoxF"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/ \
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:54:20.75Z",
  "updated_at" : "2017-01-27T18:58:26.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/ \
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:54:20.75Z",
  "updated_at" : "2017-01-27T18:58:27.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
    applicationId: "APxisMF2hLsbZqe2q9cyRYUt",
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
  "id" : "TK7VLd7UbhmkJ3x64DLxkLi9",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-27T18:54:35.67Z",
  "updated_at" : "2017-01-27T18:54:35.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-28T18:54:35.67Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TK7VLd7UbhmkJ3x64DLxkLi9")
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}).save()

```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7VLd7UbhmkJ3x64DLxkLi9",
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
  "created_at" : "2017-01-27T18:54:36.03Z",
  "updated_at" : "2017-01-27T18:54:36.03Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/updates"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110

```
```java

```
```php
<?php
use Payline\Resources\Application;

$application = Application::retrieve('APxisMF2hLsbZqe2q9cyRYUt');

```
```python


from payline.resources import Application

application = Application.get(id="APxisMF2hLsbZqe2q9cyRYUt")
```
```ruby

```
> Example Response:

```json
{
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:54:20.75Z",
  "updated_at" : "2017-01-27T18:54:22.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
	    "user": "US6Qjhi6PFP5pH7nrujts3Lu", 
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
	    "user"=> "US6Qjhi6PFP5pH7nrujts3Lu", 
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
	    "user": "US6Qjhi6PFP5pH7nrujts3Lu", 
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:54:20.78Z",
  "updated_at" : "2017-01-27T18:54:20.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/ \
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:54:20.75Z",
  "updated_at" : "2017-01-27T18:58:25.25Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/ \
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
  "id" : "APxisMF2hLsbZqe2q9cyRYUt",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:54:20.75Z",
  "updated_at" : "2017-01-27T18:58:25.72Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "processors" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
    },
    "users" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
    },
    "owner_identity" : {
      "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
    },
    "identities" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
    },
    "webhooks" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
    },
    "tokens" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
    },
    "application_profile" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "USiCW7rd5SRs7etzRE55Uwmw",
  "password" : "a36eca79-e236-4c18-bc86-bfc6d7e1b26c",
  "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:22.16Z",
  "updated_at" : "2017-01-27T18:54:22.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USiCW7rd5SRs7etzRE55Uwmw"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors \
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
  "id" : "PR43TF9wJF4rhQcwsrYHmoxF",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "default_merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "created_at" : "2017-01-27T18:54:21.58Z",
  "updated_at" : "2017-01-27T18:54:21.58Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors/PR43TF9wJF4rhQcwsrYHmoxF"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "APxisMF2hLsbZqe2q9cyRYUt",
      "enabled" : true,
      "tags" : {
        "application_name" : "Square"
      },
      "owner" : "IDeNEuHLfLjycaWNSdykVpTh",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-01-27T18:54:20.75Z",
      "updated_at" : "2017-01-27T18:54:22.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "processors" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/processors"
        },
        "users" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users"
        },
        "owner_identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/transfers"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/disputes"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/authorizations"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/settlements"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/merchants"
        },
        "identities" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/identities"
        },
        "webhooks" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/webhooks"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/reversals"
        },
        "tokens" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/tokens"
        },
        "application_profile" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/application_profile"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "merchant_identity": "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIjPjRJd9qia891Wv3qw7qhp", 
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
    .merchantIdentity("IDwj12xXD4h5hewgMoxyPjUR")
    .source("PIjPjRJd9qia891Wv3qw7qhp")
    .build()
);


```
```php
<?php
use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIjPjRJd9qia891Wv3qw7qhp", 
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
	    "merchant_identity": "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIjPjRJd9qia891Wv3qw7qhp", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Payline::Authorization.new(
	{
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIjPjRJd9qia891Wv3qw7qhp", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:34.20Z",
  "updated_at" : "2017-01-27T18:54:34.25Z",
  "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:54:34.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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
curl https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUmMbKD8iEEV8LZHDFy6mXtE");
authorization = authorization.capture(50L);

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUmMbKD8iEEV8LZHDFy6mXtE');
$authorization = $authorization->capture(50, 10);

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUmMbKD8iEEV8LZHDFy6mXtE")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUmMbKD8iEEV8LZHDFy6mXtE")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6nqgvHhVKi59PCeLbedm63",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:34.16Z",
  "updated_at" : "2017-01-27T18:54:34.76Z",
  "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:54:34.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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

curl https://api-test.payline.io/authorizations/AU8DVXrpzeQhMsFSW9YDMGHM \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$authorization = Authorization::retrieve('AUmMbKD8iEEV8LZHDFy6mXtE');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUmMbKD8iEEV8LZHDFy6mXtE")
authorization.void()

```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUmMbKD8iEEV8LZHDFy6mXtE")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AU8DVXrpzeQhMsFSW9YDMGHM",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:36.48Z",
  "updated_at" : "2017-01-27T18:54:36.99Z",
  "trace_id" : "d50335cd-0865-4d1c-9031-77fca90dc618",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : true,
  "expires_at" : "2017-02-03T18:54:36.48Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU8DVXrpzeQhMsFSW9YDMGHM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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

curl https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUmMbKD8iEEV8LZHDFy6mXtE");

```
```php
<?php
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUmMbKD8iEEV8LZHDFy6mXtE');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUmMbKD8iEEV8LZHDFy6mXtE")
```
```ruby
authorization = Payline::Authorization.retrieve(:id=>"AUmMbKD8iEEV8LZHDFy6mXtE")


```
> Example Response:

```json
{
  "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR6nqgvHhVKi59PCeLbedm63",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:34.16Z",
  "updated_at" : "2017-01-27T18:54:34.76Z",
  "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:54:34.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "AU8DVXrpzeQhMsFSW9YDMGHM",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:36.48Z",
      "updated_at" : "2017-01-27T18:54:36.99Z",
      "trace_id" : "d50335cd-0865-4d1c-9031-77fca90dc618",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "is_void" : true,
      "expires_at" : "2017-02-03T18:54:36.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AU8DVXrpzeQhMsFSW9YDMGHM"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        }
      }
    }, {
      "id" : "AUmMbKD8iEEV8LZHDFy6mXtE",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR6nqgvHhVKi59PCeLbedm63",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:34.16Z",
      "updated_at" : "2017-01-27T18:54:34.76Z",
      "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "is_void" : false,
      "expires_at" : "2017-02-03T18:54:34.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUmMbKD8iEEV8LZHDFy6mXtE"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
	        "last_name": "James", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "James", 
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
	        "first_name": "Bob", 
	        "last_name": "James", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "James", 
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
  "id" : "IDi7TvzGiUFezC2HZ9CmGnyB",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
    "last_name" : "James",
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
  "created_at" : "2017-01-27T18:54:29.34Z",
  "updated_at" : "2017-01-27T18:54:29.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
	        "amex_mid"=> "12345678910", 
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
	        "amex_mid": "12345678910", 
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
	        "amex_mid"=> "12345678910", 
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
  "id" : "IDwj12xXD4h5hewgMoxyPjUR",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:54:23.60Z",
  "updated_at" : "2017-01-27T18:54:23.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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

curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDwj12xXD4h5hewgMoxyPjUR");

```
```php
<?php
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
```
```python


from payline.resources import Identity
identity = Identity.get(id="IDwj12xXD4h5hewgMoxyPjUR")

```
```ruby
identity = Payline::Identity.retrieve(:id=>"IDwj12xXD4h5hewgMoxyPjUR")


```
> Example Response:

```json
{
  "id" : "IDwj12xXD4h5hewgMoxyPjUR",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Bobs Burgers"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:54:23.58Z",
  "updated_at" : "2017-01-27T18:54:23.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
	        "amex_mid": "12345678910", 
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
identity = Payline::Identity.retrieve(:id=>"IDwj12xXD4h5hewgMoxyPjUR")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDwj12xXD4h5hewgMoxyPjUR",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Curry",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-01-27T18:54:23.58Z",
  "updated_at" : "2017-01-27T18:54:44.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
## List all Identities
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5


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
      "id" : "IDi7TvzGiUFezC2HZ9CmGnyB",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
        "last_name" : "James",
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
      "created_at" : "2017-01-27T18:54:29.32Z",
      "updated_at" : "2017-01-27T18:54:29.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDs2PkMWrAX5odK2ixQxQ492",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:27.17Z",
      "updated_at" : "2017-01-27T18:54:27.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDs2PkMWrAX5odK2ixQxQ492/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "ID5i63nj7iaRA6emnVgECxFV",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:26.72Z",
      "updated_at" : "2017-01-27T18:54:26.72Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID5i63nj7iaRA6emnVgECxFV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDrzfA6mDLMAKv66g7SvWHks",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:26.34Z",
      "updated_at" : "2017-01-27T18:54:26.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDrzfA6mDLMAKv66g7SvWHks/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDv4a4MTxbB8HDhyppRpqAoU",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:25.94Z",
      "updated_at" : "2017-01-27T18:54:25.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDv4a4MTxbB8HDhyppRpqAoU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDcihD2BxdTF5Udg6sW5hH1D",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "GENERAL_PARTNERSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:25.58Z",
      "updated_at" : "2017-01-27T18:54:25.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDcihD2BxdTF5Udg6sW5hH1D/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "ID3Se1and4MurhDorwYRnMYW",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:25.14Z",
      "updated_at" : "2017-01-27T18:54:25.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID3Se1and4MurhDorwYRnMYW/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDgJWwBwYhyShWNqs7yVoRAN",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:24.70Z",
      "updated_at" : "2017-01-27T18:54:24.70Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDgJWwBwYhyShWNqs7yVoRAN/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "ID2MCrJHxeW9BGaaG2resegM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:24.34Z",
      "updated_at" : "2017-01-27T18:54:24.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2MCrJHxeW9BGaaG2resegM/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDecjRZV8eXx5mdd96qEnCvc",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:23.98Z",
      "updated_at" : "2017-01-27T18:54:23.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDecjRZV8eXx5mdd96qEnCvc/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDwj12xXD4h5hewgMoxyPjUR",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:54:23.58Z",
      "updated_at" : "2017-01-27T18:54:23.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "IDeNEuHLfLjycaWNSdykVpTh",
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
      "created_at" : "2017-01-27T18:54:20.75Z",
      "updated_at" : "2017-01-27T18:54:20.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDwj12xXD4h5hewgMoxyPjUR")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Payline::Identity.retrieve(:id => "MU7dskWucSx9qwz1S4fLWzkG")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "verification" : "VIsmg72dp61gWofHX9HeiBUU",
  "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:54:28.59Z",
  "updated_at" : "2017-01-27T18:54:28.59Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIsmg72dp61gWofHX9HeiBUU"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU7dskWucSx9qwz1S4fLWzkG");

```
```php
<?php
use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MU7dskWucSx9qwz1S4fLWzkG');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MU7dskWucSx9qwz1S4fLWzkG")

```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MU7dskWucSx9qwz1S4fLWzkG")

```
> Example Response:

```json
{
  "id" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "verification" : null,
  "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-27T18:54:28.54Z",
  "updated_at" : "2017-01-27T18:54:28.69Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '{}'

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MU7dskWucSx9qwz1S4fLWzkG');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MU7dskWucSx9qwz1S4fLWzkG")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIrzc8sG5BJ3ecGsLQ9bppEj",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:54:45.13Z",
  "updated_at" : "2017-01-27T18:54:45.16Z",
  "trace_id" : "d79a76b5-ec3f-43e3-9614-0473f6d8cd21",
  "payment_instrument" : null,
  "merchant" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIrzc8sG5BJ3ecGsLQ9bppEj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MU7dskWucSx9qwz1S4fLWzkG");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MU7dskWucSx9qwz1S4fLWzkG');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MU7dskWucSx9qwz1S4fLWzkG")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIrzc8sG5BJ3ecGsLQ9bppEj",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:54:45.13Z",
  "updated_at" : "2017-01-27T18:54:45.16Z",
  "trace_id" : "d79a76b5-ec3f-43e3-9614-0473f6d8cd21",
  "payment_instrument" : null,
  "merchant" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIrzc8sG5BJ3ecGsLQ9bppEj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/ \
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
  "id" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "verification" : null,
  "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-27T18:54:28.54Z",
  "updated_at" : "2017-01-27T18:58:24.45Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/ \
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
  "id" : "MU7dskWucSx9qwz1S4fLWzkG",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "verification" : null,
  "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:54:28.54Z",
  "updated_at" : "2017-01-27T18:58:24.82Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "MU7dskWucSx9qwz1S4fLWzkG",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "verification" : null,
      "merchant_profile" : "MPo4HRCVa3tHN6aLska6kfNN",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.69Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPo4HRCVa3tHN6aLska6kfNN"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

```
```java

```
```php
<?php
use Payline\Resources\Merchant;
use Payline\Resources\Verification;

$merchant = Merchant::retrieve('MU7dskWucSx9qwz1S4fLWzkG');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Payline::Merchant.retrieve(:id => "MU7dskWucSx9qwz1S4fLWzkG")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIsmg72dp61gWofHX9HeiBUU",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.73Z",
      "trace_id" : "afe089dd-0566-4873-abe9-8f5a925de0ca",
      "payment_instrument" : null,
      "merchant" : "MU7dskWucSx9qwz1S4fLWzkG",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/verifications/VIsmg72dp61gWofHX9HeiBUU"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications \
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
      "id" : "VIsmg72dp61gWofHX9HeiBUU",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.73Z",
      "trace_id" : "afe089dd-0566-4873-abe9-8f5a925de0ca",
      "payment_instrument" : null,
      "merchant" : "MU7dskWucSx9qwz1S4fLWzkG",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/verifications/VIsmg72dp61gWofHX9HeiBUU"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "merchant" : {
          "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU7dskWucSx9qwz1S4fLWzkG/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "USfuLueqKfmEyFDGZwVvK2Lj",
  "password" : "2f57d543-7a9f-41bb-83f8-9c1c3c8b5900",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:31.80Z",
  "updated_at" : "2017-01-27T18:54:31.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USfuLueqKfmEyFDGZwVvK2Lj"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;
import io.payline.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TK7VLd7UbhmkJ3x64DLxkLi9")
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
    .build()
);

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	));
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type": "TOKEN", 
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}).save()
```
```ruby
card = Payline::PaymentInstrument.new(
	{
	    "token"=> "TK7VLd7UbhmkJ3x64DLxkLi9", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7VLd7UbhmkJ3x64DLxkLi9",
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
  "created_at" : "2017-01-27T18:54:36.03Z",
  "updated_at" : "2017-01-27T18:54:36.03Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/updates"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "name": "Fran Serna", 
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
	    "identity": "IDi7TvzGiUFezC2HZ9CmGnyB"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
$card = new PaymentCard(
	array(
	    "name"=> "Fran Serna", 
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
	    "identity"=> "IDi7TvzGiUFezC2HZ9CmGnyB"
	));
$card = $identity->createPaymentCard($card);

```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Fran Serna", 
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
	    "identity": "IDi7TvzGiUFezC2HZ9CmGnyB"
	}).save()
```
```ruby
card = Payline::PaymentCard.new(
	{
	    "name"=> "Fran Serna", 
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
	    "identity"=> "IDi7TvzGiUFezC2HZ9CmGnyB"
	}).save
```
> Example Response:

```json
{
  "id" : "PIjPjRJd9qia891Wv3qw7qhp",
  "fingerprint" : "FPR-1970802456",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Serna",
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
  "created_at" : "2017-01-27T18:54:29.73Z",
  "updated_at" : "2017-01-27T18:54:29.73Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDi7TvzGiUFezC2HZ9CmGnyB",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/updates"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;
import io.payline.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDwj12xXD4h5hewgMoxyPjUR")
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
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
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
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
	    "identity": "IDwj12xXD4h5hewgMoxyPjUR"
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
	    "identity"=> "IDwj12xXD4h5hewgMoxyPjUR"
	}).save
```
> Example Response:

```json
{
  "id" : "PIeYoYSpVci2YDsA7uV9uctN",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:54:27.57Z",
  "updated_at" : "2017-01-27T18:54:27.57Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIeYoYSpVci2YDsA7uV9uctN")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIeYoYSpVci2YDsA7uV9uctN');

```
```python



```
```ruby
bank_account = Payline::BankAccount.retrieve(:id=> "PIeYoYSpVci2YDsA7uV9uctN")

```
> Example Response:

```json
{
  "id" : "PIeYoYSpVci2YDsA7uV9uctN",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:54:27.54Z",
  "updated_at" : "2017-01-27T18:54:27.94Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIjPjRJd9qia891Wv3qw7qhp")

```
```php
<?php
use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIjPjRJd9qia891Wv3qw7qhp');

```
```python



```
```ruby
card = Payline::PaymentCard.retrieve(:id=> "PIjPjRJd9qia891Wv3qw7qhp")


```
> Example Response:

```json
{
  "id" : "PIjPjRJd9qia891Wv3qw7qhp",
  "fingerprint" : "FPR-1970802456",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Serna",
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
  "created_at" : "2017-01-27T18:54:29.70Z",
  "updated_at" : "2017-01-27T18:54:34.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDi7TvzGiUFezC2HZ9CmGnyB",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/updates"
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
curl https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "merchant": "MU7dskWucSx9qwz1S4fLWzkG"
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
  "id" : "IUdvhrZg8EoNpJgwZTMy2wf5",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "merchant" : "MU7dskWucSx9qwz1S4fLWzkG",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-01-27T18:54:37.56Z",
  "updated_at" : "2017-01-27T18:54:37.58Z",
  "payment_instrument" : "PIjPjRJd9qia891Wv3qw7qhp",
  "trace_id" : "ec5919ae-6555-437e-af81-f7ed221725d9",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/updates/IUdvhrZg8EoNpJgwZTMy2wf5"
    },
    "payment_instrument" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5
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
      "id" : "PI7VLd7UbhmkJ3x64DLxkLi9",
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
      "created_at" : "2017-01-27T18:54:35.99Z",
      "updated_at" : "2017-01-27T18:54:35.99Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7VLd7UbhmkJ3x64DLxkLi9/updates"
        }
      }
    }, {
      "id" : "PIqJczYWwk8xfzhTwJTUUgFv",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:54:30.08Z",
      "updated_at" : "2017-01-27T18:54:30.08Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDi7TvzGiUFezC2HZ9CmGnyB",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIjPjRJd9qia891Wv3qw7qhp",
      "fingerprint" : "FPR-1970802456",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Fran Serna",
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
      "created_at" : "2017-01-27T18:54:29.70Z",
      "updated_at" : "2017-01-27T18:54:34.22Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDi7TvzGiUFezC2HZ9CmGnyB",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDi7TvzGiUFezC2HZ9CmGnyB"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp/updates"
        }
      }
    }, {
      "id" : "PImHVMt6uAVX36mJkVqS4orV",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.54Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIsbRY98QnZxH9Fafei3fvj9",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.54Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsbRY98QnZxH9Fafei3fvj9"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsbRY98QnZxH9Fafei3fvj9/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsbRY98QnZxH9Fafei3fvj9/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsbRY98QnZxH9Fafei3fvj9/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIF3iCYGcxZiNsCyyvhkQzr",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:28.54Z",
      "updated_at" : "2017-01-27T18:54:28.54Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIF3iCYGcxZiNsCyyvhkQzr"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIF3iCYGcxZiNsCyyvhkQzr/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIF3iCYGcxZiNsCyyvhkQzr/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIF3iCYGcxZiNsCyyvhkQzr/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIeYoYSpVci2YDsA7uV9uctN",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:54:27.54Z",
      "updated_at" : "2017-01-27T18:54:27.94Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIcivZEn5Ji6gCzPDVqBVRoz",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:21.55Z",
      "updated_at" : "2017-01-27T18:54:21.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PIcMQ3h9VNe923ATmNjrRWMY",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:21.55Z",
      "updated_at" : "2017-01-27T18:54:21.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcMQ3h9VNe923ATmNjrRWMY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcMQ3h9VNe923ATmNjrRWMY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcMQ3h9VNe923ATmNjrRWMY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcMQ3h9VNe923ATmNjrRWMY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PI4EtwgF8vFV1A6bqdV4rZwy",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:21.55Z",
      "updated_at" : "2017-01-27T18:54:21.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "PImiMXYhVgD59sTLPD1pegyF",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:54:21.55Z",
      "updated_at" : "2017-01-27T18:54:21.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiMXYhVgD59sTLPD1pegyF"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiMXYhVgD59sTLPD1pegyF/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiMXYhVgD59sTLPD1pegyF/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiMXYhVgD59sTLPD1pegyF/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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

curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$identity = Identity::retrieve('IDwj12xXD4h5hewgMoxyPjUR');
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

identity = Identity.get(id="IDwj12xXD4h5hewgMoxyPjUR")
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
identity = Payline::Identity.retrieve(:id=>"IDwj12xXD4h5hewgMoxyPjUR")
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
  "id" : "ST2a4SPHbCSCTeWu8U3jzEVt",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:58:20.31Z",
  "updated_at" : "2017-01-27T18:58:20.35Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 558206,
  "total_fees" : 55822,
  "total_fee" : 55822,
  "net_amount" : 502384,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=debit"
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


curl https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("ST2a4SPHbCSCTeWu8U3jzEVt");

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('ST2a4SPHbCSCTeWu8U3jzEVt');

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"ST2a4SPHbCSCTeWu8U3jzEVt")

```
> Example Response:

```json
{
  "id" : "ST2a4SPHbCSCTeWu8U3jzEVt",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:58:20.28Z",
  "updated_at" : "2017-01-27T18:58:21.27Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 558206,
  "total_fees" : 55822,
  "total_fee" : 55822,
  "net_amount" : 502384,
  "destination" : "PIeYoYSpVci2YDsA7uV9uctN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PIeYoYSpVci2YDsA7uV9uctN"
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
  "id" : "ST2a4SPHbCSCTeWu8U3jzEVt",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:58:20.28Z",
  "updated_at" : "2017-01-27T18:58:21.27Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 558206,
  "total_fees" : 55822,
  "total_fee" : 55822,
  "net_amount" : 502384,
  "destination" : "PIeYoYSpVci2YDsA7uV9uctN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=debit"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "ST2a4SPHbCSCTeWu8U3jzEVt",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "currency" : "USD",
      "created_at" : "2017-01-27T18:58:20.28Z",
      "updated_at" : "2017-01-27T18:58:21.27Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 558206,
      "total_fees" : 55822,
      "total_fee" : 55822,
      "net_amount" : 502384,
      "destination" : "PIeYoYSpVci2YDsA7uV9uctN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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

$settlement = Settlement::retrieve('ST2a4SPHbCSCTeWu8U3jzEVt');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"ST2a4SPHbCSCTeWu8U3jzEVt")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR5eogt2o1G5BcTufFk42KCS",
      "amount" : 502384,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "409db8bb-0f65-4cb7-b9f4-3342fc4c0413",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PIeYoYSpVci2YDsA7uV9uctN",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:20.97Z",
      "updated_at" : "2017-01-27T18:58:21.23Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR5eogt2o1G5BcTufFk42KCS"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR5eogt2o1G5BcTufFk42KCS/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR5eogt2o1G5BcTufFk42KCS/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR5eogt2o1G5BcTufFk42KCS/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR5eogt2o1G5BcTufFk42KCS/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIeYoYSpVci2YDsA7uV9uctN"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

```
```java

```
```php
<?php
use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('ST2a4SPHbCSCTeWu8U3jzEVt');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Payline::Settlement.retrieve(:id=>"ST2a4SPHbCSCTeWu8U3jzEVt")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRp5UCFka2ipdUYTdfogfn6i",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "b9d6425c-5198-43e5-adc0-827dcafda8bd",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PI4EtwgF8vFV1A6bqdV4rZwy",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:19.13Z",
      "updated_at" : "2017-01-27T18:58:19.36Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRp5UCFka2ipdUYTdfogfn6i"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRp5UCFka2ipdUYTdfogfn6i/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRp5UCFka2ipdUYTdfogfn6i/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRp5UCFka2ipdUYTdfogfn6i/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRp5UCFka2ipdUYTdfogfn6i/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy"
        }
      }
    }, {
      "id" : "TRfwFoR9s7C4JCtgNw7kPZ2p",
      "amount" : 18215,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "aa01291e-7ba5-4444-8b6c-cb2695300611",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PIcivZEn5Ji6gCzPDVqBVRoz",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:18.71Z",
      "updated_at" : "2017-01-27T18:58:19.09Z",
      "merchant_identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRfwFoR9s7C4JCtgNw7kPZ2p"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRfwFoR9s7C4JCtgNw7kPZ2p/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRfwFoR9s7C4JCtgNw7kPZ2p/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRfwFoR9s7C4JCtgNw7kPZ2p/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRfwFoR9s7C4JCtgNw7kPZ2p/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz"
        }
      }
    }, {
      "id" : "TR8UjoTemBEHGLDdepGafCUi",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "d9811213-81e2-47df-9a4d-558019523682",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PI4EtwgF8vFV1A6bqdV4rZwy",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:18.46Z",
      "updated_at" : "2017-01-27T18:58:18.70Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR8UjoTemBEHGLDdepGafCUi"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR8UjoTemBEHGLDdepGafCUi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR8UjoTemBEHGLDdepGafCUi/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR8UjoTemBEHGLDdepGafCUi/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR8UjoTemBEHGLDdepGafCUi/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy"
        }
      }
    }, {
      "id" : "TRcSt93GoKUwCiURij6wD4Jw",
      "amount" : 37574,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "66fd1aff-6b32-4a90-8e67-6d9d4dde7ee8",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PIcivZEn5Ji6gCzPDVqBVRoz",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:18.14Z",
      "updated_at" : "2017-01-27T18:58:18.41Z",
      "merchant_identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRcSt93GoKUwCiURij6wD4Jw"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRcSt93GoKUwCiURij6wD4Jw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDeNEuHLfLjycaWNSdykVpTh"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRcSt93GoKUwCiURij6wD4Jw/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRcSt93GoKUwCiURij6wD4Jw/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRcSt93GoKUwCiURij6wD4Jw/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcivZEn5Ji6gCzPDVqBVRoz"
        }
      }
    }, {
      "id" : "TRi7Sn8tZsinN1MnQuCWdSuF",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "1350d974-bbf4-4dc9-82b6-6372f1a4e188",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PI4EtwgF8vFV1A6bqdV4rZwy",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:58:17.81Z",
      "updated_at" : "2017-01-27T18:58:18.11Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRi7Sn8tZsinN1MnQuCWdSuF"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRi7Sn8tZsinN1MnQuCWdSuF/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRi7Sn8tZsinN1MnQuCWdSuF/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRi7Sn8tZsinN1MnQuCWdSuF/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRi7Sn8tZsinN1MnQuCWdSuF/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4EtwgF8vFV1A6bqdV4rZwy"
        }
      }
    }, {
      "id" : "TR6nqgvHhVKi59PCeLbedm63",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:34.65Z",
      "updated_at" : "2017-01-27T18:55:09.04Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    }, {
      "id" : "TRgiiWou6LMru2mUHS4kVFZk",
      "amount" : 375848,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "194abda3-41b0-4bf1-8034-5067e162915e",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIqJczYWwk8xfzhTwJTUUgFv",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 37585,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:31.20Z",
      "updated_at" : "2017-01-27T18:55:12.90Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    }, {
      "id" : "TRxgqBbSqRn15DBPksNkjh3q",
      "amount" : 182258,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "86108465-613b-48e6-9603-b1f1f4c9786d",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : "2017-01-27T18:58:17.73Z",
      "fee" : 18226,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:30.49Z",
      "updated_at" : "2017-01-27T18:55:11.65Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/ST2a4SPHbCSCTeWu8U3jzEVt/transfers?offset=0&limit=20&sort=created_at,desc"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
    -d '
	{
	    "fee": 37585, 
	    "source": "PIqJczYWwk8xfzhTwJTUUgFv", 
	    "merchant_identity": "IDwj12xXD4h5hewgMoxyPjUR", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 375848
	}'


```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDwj12xXD4h5hewgMoxyPjUR")
      .source("PIjPjRJd9qia891Wv3qw7qhp")
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
	    "fee"=> 18226, 
	    "source"=> "PIjPjRJd9qia891Wv3qw7qhp", 
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 182258
	));
$debit = $debit->save();
```
```python



```
```ruby
Payline::Transfer.new(
	{
	    "fee"=> 37585, 
	    "source"=> "PIqJczYWwk8xfzhTwJTUUgFv", 
	    "merchant_identity"=> "IDwj12xXD4h5hewgMoxyPjUR", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "currency"=> "USD", 
	    "amount"=> 375848
	}}).save
```


> Example Response:

```json
{
  "id" : "TRgiiWou6LMru2mUHS4kVFZk",
  "amount" : 375848,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "194abda3-41b0-4bf1-8034-5067e162915e",
  "currency" : "USD",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "source" : "PIqJczYWwk8xfzhTwJTUUgFv",
  "destination" : "PImHVMt6uAVX36mJkVqS4orV",
  "ready_to_settle_at" : null,
  "fee" : 37585,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:31.25Z",
  "updated_at" : "2017-01-27T18:54:31.32Z",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
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

curl https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRxgqBbSqRn15DBPksNkjh3q");

```
```php
<?php
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRxgqBbSqRn15DBPksNkjh3q');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRxgqBbSqRn15DBPksNkjh3q")

```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRxgqBbSqRn15DBPksNkjh3q")

```
> Example Response:

```json
{
  "id" : "TRxgqBbSqRn15DBPksNkjh3q",
  "amount" : 182258,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "86108465-613b-48e6-9603-b1f1f4c9786d",
  "currency" : "USD",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "source" : "PIjPjRJd9qia891Wv3qw7qhp",
  "destination" : "PImHVMt6uAVX36mJkVqS4orV",
  "ready_to_settle_at" : null,
  "fee" : 18226,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:30.49Z",
  "updated_at" : "2017-01-27T18:54:30.64Z",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
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

curl https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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

$debit = Transfer::retrieve('TRxgqBbSqRn15DBPksNkjh3q');
$refund = $debit->reverse(11);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TRxgqBbSqRn15DBPksNkjh3q")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Payline::Transfer.retrieve(:id=> "TRxgqBbSqRn15DBPksNkjh3q")

refund = Payline::Transfer.reverse(
          {
          "refund_amount" => 100
        }
        ).save
```
> Example Response:

```json
{
  "id" : "TRtYaEAm7BUEW788ydCrfVEg",
  "amount" : 746522,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "e27e59f8-3066-494d-8d35-f4aeb250a05f",
  "currency" : "USD",
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "source" : "PImHVMt6uAVX36mJkVqS4orV",
  "destination" : "PIjPjRJd9qia891Wv3qw7qhp",
  "ready_to_settle_at" : null,
  "fee" : 74652,
  "statement_descriptor" : "PLD*BOBS BURGERS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:54:33.54Z",
  "updated_at" : "2017-01-27T18:54:33.61Z",
  "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRtYaEAm7BUEW788ydCrfVEg"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRtYaEAm7BUEW788ydCrfVEg/payment_instruments"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "TR6nqgvHhVKi59PCeLbedm63",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "bc96a3ce-873b-443b-9911-afebd38dd8f0",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:34.65Z",
      "updated_at" : "2017-01-27T18:54:34.76Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR6nqgvHhVKi59PCeLbedm63/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    }, {
      "id" : "TRtYaEAm7BUEW788ydCrfVEg",
      "amount" : 746522,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "bed04ea0-8084-4f94-9505-e4cec4075f1d",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PImHVMt6uAVX36mJkVqS4orV",
      "destination" : "PIjPjRJd9qia891Wv3qw7qhp",
      "ready_to_settle_at" : null,
      "fee" : 74652,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:33.41Z",
      "updated_at" : "2017-01-27T18:54:33.61Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRtYaEAm7BUEW788ydCrfVEg"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRtYaEAm7BUEW788ydCrfVEg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        }
      }
    }, {
      "id" : "TR7dSmywWdKWUjrYNwMCQ7xn",
      "amount" : 746522,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "1c70c784-4123-4557-aef5-dc930596b41f",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : null,
      "fee" : 74652,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:32.92Z",
      "updated_at" : "2017-01-27T18:54:33.51Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR7dSmywWdKWUjrYNwMCQ7xn/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    }, {
      "id" : "TRgiiWou6LMru2mUHS4kVFZk",
      "amount" : 375848,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "194abda3-41b0-4bf1-8034-5067e162915e",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIqJczYWwk8xfzhTwJTUUgFv",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : null,
      "fee" : 37585,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:31.20Z",
      "updated_at" : "2017-01-27T18:54:31.32Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRgiiWou6LMru2mUHS4kVFZk/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqJczYWwk8xfzhTwJTUUgFv"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
        }
      }
    }, {
      "id" : "TRxgqBbSqRn15DBPksNkjh3q",
      "amount" : 182258,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "86108465-613b-48e6-9603-b1f1f4c9786d",
      "currency" : "USD",
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "source" : "PIjPjRJd9qia891Wv3qw7qhp",
      "destination" : "PImHVMt6uAVX36mJkVqS4orV",
      "ready_to_settle_at" : null,
      "fee" : 18226,
      "statement_descriptor" : "PLD*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:30.49Z",
      "updated_at" : "2017-01-27T18:54:30.64Z",
      "merchant_identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRxgqBbSqRn15DBPksNkjh3q/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjPjRJd9qia891Wv3qw7qhp"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImHVMt6uAVX36mJkVqS4orV"
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
curl https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "USiCW7rd5SRs7etzRE55Uwmw",
  "password" : "a36eca79-e236-4c18-bc86-bfc6d7e1b26c",
  "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:22.16Z",
  "updated_at" : "2017-01-27T18:54:22.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USiCW7rd5SRs7etzRE55Uwmw"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/identities/IDwj12xXD4h5hewgMoxyPjUR/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "USfuLueqKfmEyFDGZwVvK2Lj",
  "password" : "2f57d543-7a9f-41bb-83f8-9c1c3c8b5900",
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:31.80Z",
  "updated_at" : "2017-01-27T18:54:31.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USfuLueqKfmEyFDGZwVvK2Lj"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/users/TRxgqBbSqRn15DBPksNkjh3q \
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
user = User.get(id="US6Qjhi6PFP5pH7nrujts3Lu")

```
```ruby

```
> Example Response:

```json
{
  "id" : "US6Qjhi6PFP5pH7nrujts3Lu",
  "password" : null,
  "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:20.28Z",
  "updated_at" : "2017-01-27T18:54:20.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/US6Qjhi6PFP5pH7nrujts3Lu"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
curl https://api-test.payline.io/users/USfuLueqKfmEyFDGZwVvK2Lj \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "USfuLueqKfmEyFDGZwVvK2Lj",
  "password" : null,
  "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:54:31.77Z",
  "updated_at" : "2017-01-27T18:54:32.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USfuLueqKfmEyFDGZwVvK2Lj"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "USfuLueqKfmEyFDGZwVvK2Lj",
      "password" : null,
      "identity" : "IDwj12xXD4h5hewgMoxyPjUR",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-01-27T18:54:31.77Z",
      "updated_at" : "2017-01-27T18:54:32.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USfuLueqKfmEyFDGZwVvK2Lj"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "USiCW7rd5SRs7etzRE55Uwmw",
      "password" : null,
      "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-27T18:54:22.14Z",
      "updated_at" : "2017-01-27T18:54:22.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/USiCW7rd5SRs7etzRE55Uwmw"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
        }
      }
    }, {
      "id" : "US6Qjhi6PFP5pH7nrujts3Lu",
      "password" : null,
      "identity" : "IDeNEuHLfLjycaWNSdykVpTh",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-27T18:54:20.28Z",
      "updated_at" : "2017-01-27T18:54:20.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/users/US6Qjhi6PFP5pH7nrujts3Lu"
        },
        "applications" : {
          "href" : "https://api-test.payline.io/applications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5 \
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
  "id" : "WHtXMXjJVVt7fZTLd7kCYNxB",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "created_at" : "2017-01-27T18:54:23.31Z",
  "updated_at" : "2017-01-27T18:54:23.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHtXMXjJVVt7fZTLd7kCYNxB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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



curl https://api-test.payline.io/webhooks/WHtXMXjJVVt7fZTLd7kCYNxB \
    -H "Content-Type: application/vnd.json+api" \
    -u US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHtXMXjJVVt7fZTLd7kCYNxB");

```
```php
<?php
use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHtXMXjJVVt7fZTLd7kCYNxB');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WHtXMXjJVVt7fZTLd7kCYNxB")

```
```ruby
webhook = Payline::Webhook.retrieve(:id=> "WHtXMXjJVVt7fZTLd7kCYNxB")


```
> Example Response:

```json
{
  "id" : "WHtXMXjJVVt7fZTLd7kCYNxB",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APxisMF2hLsbZqe2q9cyRYUt",
  "created_at" : "2017-01-27T18:54:23.30Z",
  "updated_at" : "2017-01-27T18:54:23.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHtXMXjJVVt7fZTLd7kCYNxB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
    -u  US6Qjhi6PFP5pH7nrujts3Lu:879a7227-1c51-4de5-91e4-32044cfc12e5

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
      "id" : "WHtXMXjJVVt7fZTLd7kCYNxB",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APxisMF2hLsbZqe2q9cyRYUt",
      "created_at" : "2017-01-27T18:54:23.30Z",
      "updated_at" : "2017-01-27T18:54:23.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHtXMXjJVVt7fZTLd7kCYNxB"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APxisMF2hLsbZqe2q9cyRYUt"
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
