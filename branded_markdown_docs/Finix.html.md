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

4. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
  client.setupUserIdAndPassword("UScrRBEbdXh6eXUnME9c1MYF", "dfee4bb1-595c-40b8-888b-7efae106f0ce");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');

Finix\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'UScrRBEbdXh6eXUnME9c1MYF',
	"password" => 'dfee4bb1-595c-40b8-888b-7efae106f0ce']
	);

require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("UScrRBEbdXh6eXUnME9c1MYF", "dfee4bb1-595c-40b8-888b-7efae106f0ce"))

```
```ruby
# To download the Ruby gem:
# gem install finix

require 'finix'

Finix.configure(
    :root_url => 'https://api-staging.finix.io',
    :user=>'UScrRBEbdXh6eXUnME9c1MYF',
    :password => 'dfee4bb1-595c-40b8-888b-7efae106f0ce'
)
```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `UScrRBEbdXh6eXUnME9c1MYF`

- Password: `dfee4bb1-595c-40b8-888b-7efae106f0ce`

- Application ID: `AP4GcWbztqRvJnJ9TydudDAF`

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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "ownership_type": "PRIVATE", 
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
	        "ownership_type"=> "PRIVATE", 
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
  "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T18:55:23.49Z",
  "updated_at" : "2017-03-28T18:55:23.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "ID6HTbvJWaQb7TUVSR2KpiqX"
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
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
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
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
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
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
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save
```
> Example Response:

```json
{
  "id" : "PIgtzh7EvFDiSnynkwnsgr3z",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T18:55:27.69Z",
  "updated_at" : "2017-03-28T18:55:27.69Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "verification" : "VIqsxrFKTjNTiyMEtpkfJPGS",
  "merchant_profile" : "MPg32sgckPhfindCMvLFCpP1",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T18:55:28.62Z",
  "updated_at" : "2017-03-28T18:55:28.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPg32sgckPhfindCMvLFCpP1"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqsxrFKTjNTiyMEtpkfJPGS"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "White", 
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
	        "first_name": "Bob", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "White", 
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
  "id" : "ID2YRE5PQEHtBTqoAAhJo2T3",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-03-28T18:55:29.37Z",
  "updated_at" : "2017-03-28T18:55:29.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "name": "Jessie Sterling", 
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
	    "identity": "ID2YRE5PQEHtBTqoAAhJo2T3"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
$card = new PaymentCard(
	array(
	    "name"=> "Jessie Sterling", 
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
	    "identity"=> "ID2YRE5PQEHtBTqoAAhJo2T3"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Jessie Sterling", 
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
	    "identity": "ID2YRE5PQEHtBTqoAAhJo2T3"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Jessie Sterling", 
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
	    "identity"=> "ID2YRE5PQEHtBTqoAAhJo2T3"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7jjWoR9uGsiXetvjLnavUY",
  "fingerprint" : "FPR1412414468",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Sterling",
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
  "created_at" : "2017-03-28T18:55:29.91Z",
  "updated_at" : "2017-03-28T18:55:29.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2YRE5PQEHtBTqoAAhJo2T3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/updates"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "merchant_identity": "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI7jjWoR9uGsiXetvjLnavUY", 
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
    .merchantIdentity("ID6HTbvJWaQb7TUVSR2KpiqX")
    .source("PI7jjWoR9uGsiXetvjLnavUY")
    .build()
);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI7jjWoR9uGsiXetvjLnavUY", 
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
	    "merchant_identity": "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI7jjWoR9uGsiXetvjLnavUY", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI7jjWoR9uGsiXetvjLnavUY", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.79Z",
  "updated_at" : "2017-03-28T18:55:34.84Z",
  "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : false,
  "expires_at" : "2017-04-04T18:55:34.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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
source | *string*, **required** | The buyer's `Payment Instrument` ID that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Capture the Authorization
```shell
curl https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU4VUHqAeFV46K9b1nrC9c1U");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU4VUHqAeFV46K9b1nrC9c1U');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU4VUHqAeFV46K9b1nrC9c1U")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AU4VUHqAeFV46K9b1nrC9c1U")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRtE4ScbPV8nMnAQKLoZuy9F",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.73Z",
  "updated_at" : "2017-03-28T18:55:35.33Z",
  "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : false,
  "expires_at" : "2017-04-04T18:55:34.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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
curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
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

identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")
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
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")
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
  "id" : "STrXDzTso6jYd83jvQS9yoVL",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "currency" : "USD",
  "created_at" : "2017-03-28T18:58:11.14Z",
  "updated_at" : "2017-03-28T18:58:11.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1389672,
  "total_fees" : 138969,
  "total_fee" : 138969,
  "net_amount" : 1250703,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=debit"
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
### Step 1: Create a Recipient Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Daphne", 
	        "last_name": "Curry", 
	        "email": "Daphne@gmail.com", 
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

$identity = new Identity(ID9gNYGtmx8XqF4NuAqK1oyn);
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
	        "phone"=> "7145677612", 
	        "first_name"=> "Daphne", 
	        "last_name"=> "Curry", 
	        "email"=> "Daphne@gmail.com", 
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
  "id" : "ID9gNYGtmx8XqF4NuAqK1oyn",
  "entity" : {
    "title" : null,
    "first_name" : "Daphne",
    "last_name" : "Curry",
    "email" : "Daphne@gmail.com",
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
  "created_at" : "2017-03-28T18:58:20.06Z",
  "updated_at" : "2017-03-28T18:58:20.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP8RsF6wsQ8iYkXccfaSRkjV"
    }
  }
}
```

Use the resulting ID of the newly created Recipient Identity to associate any payouts or payment instruments that are used. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds.

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

### Step 2:  Add a Payment Instrument for the Recipient 

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "name": "Jessie Henderson", 
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
	    "identity": "ID9gNYGtmx8XqF4NuAqK1oyn"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
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

$identity = Identity::retrieve('ID9gNYGtmx8XqF4NuAqK1oyn');
$card = new PaymentCard(
	array(
	    "name"=> "Jessie Henderson", 
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
	    "identity"=> "ID9gNYGtmx8XqF4NuAqK1oyn"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Jessie Henderson", 
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
	    "identity"=> "ID9gNYGtmx8XqF4NuAqK1oyn"
	}).save
```
> Example Response:

```json
{
  "id" : "PIiHLAm5NxMBbm9bubHb9N7q",
  "fingerprint" : "FPR767043592",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Henderson",
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
  "created_at" : "2017-03-28T18:58:20.41Z",
  "updated_at" : "2017-03-28T18:58:20.41Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID9gNYGtmx8XqF4NuAqK1oyn",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP8RsF6wsQ8iYkXccfaSRkjV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q/updates"
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

### Step 3: Provision Sender Account
```shell
curl https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
Identity identity = client.identitiesClient().fetchResource("ID9gNYGtmx8XqF4NuAqK1oyn");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('ID9gNYGtmx8XqF4NuAqK1oyn');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID9gNYGtmx8XqF4NuAqK1oyn")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUgsnd2xbvgVBEDHuNSgqjVe",
  "identity" : "ID9gNYGtmx8XqF4NuAqK1oyn",
  "verification" : "VIktfjWVDALWfPcesBcHe9Pq",
  "merchant_profile" : "MPwjEoRqbDHKUsNFCu7UF7pq",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T18:58:21.05Z",
  "updated_at" : "2017-03-28T18:58:21.05Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgsnd2xbvgVBEDHuNSgqjVe"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgsnd2xbvgVBEDHuNSgqjVe/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwjEoRqbDHKUsNFCu7UF7pq"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP8RsF6wsQ8iYkXccfaSRkjV"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIktfjWVDALWfPcesBcHe9Pq"
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
    -u UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIiHLAm5NxMBbm9bubHb9N7q", 
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
	    "destination"=> "PIiHLAm5NxMBbm9bubHb9N7q", 
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
	    "destination"=> "PIiHLAm5NxMBbm9bubHb9N7q", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "TR3AhfeF7z7rNvcr9gshsy6Q",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190767",
  "currency" : "USD",
  "application" : "AP8RsF6wsQ8iYkXccfaSRkjV",
  "source" : "PId6XFWo33YhbFH1FtKAUsuK",
  "destination" : "PIiHLAm5NxMBbm9bubHb9N7q",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:58:22.03Z",
  "updated_at" : "2017-03-28T18:58:23.58Z",
  "merchant_identity" : "ID9gNYGtmx8XqF4NuAqK1oyn",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP8RsF6wsQ8iYkXccfaSRkjV"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR3AhfeF7z7rNvcr9gshsy6Q"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR3AhfeF7z7rNvcr9gshsy6Q/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID9gNYGtmx8XqF4NuAqK1oyn"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR3AhfeF7z7rNvcr9gshsy6Q/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR3AhfeF7z7rNvcr9gshsy6Q/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR3AhfeF7z7rNvcr9gshsy6Q/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PId6XFWo33YhbFH1FtKAUsuK"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiHLAm5NxMBbm9bubHb9N7q"
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
          applicationId: 'AP4GcWbztqRvJnJ9TydudDAF',
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
  "id" : "TKgNmLTEk6oCcDERZqCX7w2m",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-28T18:55:36.28Z",
  "updated_at" : "2017-03-28T18:55:36.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-29T18:55:36.28Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKgNmLTEk6oCcDERZqCX7w2m")
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save
```
> Example Response:

```json
{
  "id" : "PIgNmLTEk6oCcDERZqCX7w2m",
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
  "created_at" : "2017-03-28T18:55:36.64Z",
  "updated_at" : "2017-03-28T18:55:36.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/updates"
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
    server: "https://api-staging.finix.io",
    applicationId: "AP4GcWbztqRvJnJ9TydudDAF",
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
  "id" : "TKgNmLTEk6oCcDERZqCX7w2m",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-28T18:55:36.28Z",
  "updated_at" : "2017-03-28T18:55:36.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-29T18:55:36.28Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}'

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKgNmLTEk6oCcDERZqCX7w2m")
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save
```
> Example Response:

```json
{
  "id" : "PIgNmLTEk6oCcDERZqCX7w2m",
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
  "created_at" : "2017-03-28T18:55:36.64Z",
  "updated_at" : "2017-03-28T18:55:36.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/updates"
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
# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "merchant_identity": "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI7jjWoR9uGsiXetvjLnavUY", 
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
    .merchantIdentity("ID6HTbvJWaQb7TUVSR2KpiqX")
    .source("PI7jjWoR9uGsiXetvjLnavUY")
    .build()
);


```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI7jjWoR9uGsiXetvjLnavUY", 
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
	    "merchant_identity": "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI7jjWoR9uGsiXetvjLnavUY", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI7jjWoR9uGsiXetvjLnavUY", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.79Z",
  "updated_at" : "2017-03-28T18:55:34.84Z",
  "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : false,
  "expires_at" : "2017-04-04T18:55:34.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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
curl https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU4VUHqAeFV46K9b1nrC9c1U");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU4VUHqAeFV46K9b1nrC9c1U');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU4VUHqAeFV46K9b1nrC9c1U")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AU4VUHqAeFV46K9b1nrC9c1U")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRtE4ScbPV8nMnAQKLoZuy9F",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.73Z",
  "updated_at" : "2017-03-28T18:55:35.33Z",
  "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : false,
  "expires_at" : "2017-04-04T18:55:34.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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

curl https://api-staging.finix.io/authorizations/AU9JYUSVPv3Za8jyqLA54MMx \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$authorization = Authorization::retrieve('AU4VUHqAeFV46K9b1nrC9c1U');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU4VUHqAeFV46K9b1nrC9c1U")
authorization.void()

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AU4VUHqAeFV46K9b1nrC9c1U")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AU9JYUSVPv3Za8jyqLA54MMx",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:37.17Z",
  "updated_at" : "2017-03-28T18:55:38.10Z",
  "trace_id" : "998d1f17-8532-48d4-a8b5-5aa1c2871557",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : true,
  "expires_at" : "2017-04-04T18:55:37.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU9JYUSVPv3Za8jyqLA54MMx"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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

curl https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU4VUHqAeFV46K9b1nrC9c1U");

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AU4VUHqAeFV46K9b1nrC9c1U');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AU4VUHqAeFV46K9b1nrC9c1U")
```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AU4VUHqAeFV46K9b1nrC9c1U")


```
> Example Response:

```json
{
  "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRtE4ScbPV8nMnAQKLoZuy9F",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.73Z",
  "updated_at" : "2017-03-28T18:55:35.33Z",
  "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "is_void" : false,
  "expires_at" : "2017-04-04T18:55:34.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
      "id" : "AU9JYUSVPv3Za8jyqLA54MMx",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:37.17Z",
      "updated_at" : "2017-03-28T18:55:38.10Z",
      "trace_id" : "998d1f17-8532-48d4-a8b5-5aa1c2871557",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "is_void" : true,
      "expires_at" : "2017-04-04T18:55:37.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU9JYUSVPv3Za8jyqLA54MMx"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        }
      }
    }, {
      "id" : "AU4VUHqAeFV46K9b1nrC9c1U",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRtE4ScbPV8nMnAQKLoZuy9F",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:34.73Z",
      "updated_at" : "2017-03-28T18:55:35.33Z",
      "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "is_void" : false,
      "expires_at" : "2017-04-04T18:55:34.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU4VUHqAeFV46K9b1nrC9c1U"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "White", 
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
	        "first_name": "Bob", 
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
	        "first_name"=> "Bob", 
	        "last_name"=> "White", 
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
  "id" : "ID2YRE5PQEHtBTqoAAhJo2T3",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-03-28T18:55:29.37Z",
  "updated_at" : "2017-03-28T18:55:29.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
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
	        "ownership_type"=> "PRIVATE", 
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
	        "ownership_type": "PRIVATE", 
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
	        "ownership_type"=> "PRIVATE", 
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
  "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T18:55:23.49Z",
  "updated_at" : "2017-03-28T18:55:23.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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

curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID6HTbvJWaQb7TUVSR2KpiqX");

```
```php
<?php
use Finix\Resources\Identity;

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
```
```python


from finix.resources import Identity
identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")

```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")


```
> Example Response:

```json
{
  "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-28T18:55:23.47Z",
  "updated_at" : "2017-03-28T18:55:23.47Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce


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
      "id" : "ID2YRE5PQEHtBTqoAAhJo2T3",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
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
        "ownership_type" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2017-03-28T18:55:29.36Z",
      "updated_at" : "2017-03-28T18:55:29.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDf8ppQpPnhuscMRrzBvions",
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
      "created_at" : "2017-03-28T18:55:27.30Z",
      "updated_at" : "2017-03-28T18:55:27.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID69Zgg9iiRNYKSr2AHj6vdb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:26.94Z",
      "updated_at" : "2017-03-28T18:55:26.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID96ASpo53x7KRhGPmTR5hTi",
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
      "created_at" : "2017-03-28T18:55:26.29Z",
      "updated_at" : "2017-03-28T18:55:26.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID26rb9jU6WZrHKwrVp2kNtz",
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
      "created_at" : "2017-03-28T18:55:25.91Z",
      "updated_at" : "2017-03-28T18:55:25.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID4d2yXxTHo1p25G5yiTQnEd",
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
      "created_at" : "2017-03-28T18:55:25.53Z",
      "updated_at" : "2017-03-28T18:55:25.53Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDkdK7Td1cSVwzdLqtzTZ87C",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:25.18Z",
      "updated_at" : "2017-03-28T18:55:25.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDpP8ScaAHxrsF4EAhTebdVt",
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
      "created_at" : "2017-03-28T18:55:24.81Z",
      "updated_at" : "2017-03-28T18:55:24.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDrt8ZVtJZyoUbBxDtRhF4Av",
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
      "created_at" : "2017-03-28T18:55:24.41Z",
      "updated_at" : "2017-03-28T18:55:24.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDts5Jx2YdP5wMdFGhhrdbbQ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "CORPORATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:23.87Z",
      "updated_at" : "2017-03-28T18:55:23.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:23.47Z",
      "updated_at" : "2017-03-28T18:55:23.47Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "HyperWallet",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "HyperWallet",
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
        "application_name" : "HyperWallet"
      },
      "created_at" : "2017-03-28T18:55:19.60Z",
      "updated_at" : "2017-03-28T18:55:19.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    "count" : 12
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/identities/`


## Update an Identity
```shell
curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Sterling", 
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
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Sterling",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
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
    "key" : "value_2"
  },
  "created_at" : "2017-03-28T18:55:23.47Z",
  "updated_at" : "2017-03-28T18:55:46.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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

curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")

merchant = identity.provision_merchant
```

> Example Response:

```json
{
  "id" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "verification" : "VIqsxrFKTjNTiyMEtpkfJPGS",
  "merchant_profile" : "MPg32sgckPhfindCMvLFCpP1",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T18:55:28.62Z",
  "updated_at" : "2017-03-28T18:55:28.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPg32sgckPhfindCMvLFCpP1"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqsxrFKTjNTiyMEtpkfJPGS"
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
curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id => "MUzL5f3UkAwvK79iZGa8UhQ")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "verification" : "VIqsxrFKTjNTiyMEtpkfJPGS",
  "merchant_profile" : "MPg32sgckPhfindCMvLFCpP1",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-28T18:55:28.62Z",
  "updated_at" : "2017-03-28T18:55:28.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPg32sgckPhfindCMvLFCpP1"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqsxrFKTjNTiyMEtpkfJPGS"
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
curl https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUzL5f3UkAwvK79iZGa8UhQ");

```
```php
<?php
use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUzL5f3UkAwvK79iZGa8UhQ');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MUzL5f3UkAwvK79iZGa8UhQ")

```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUzL5f3UkAwvK79iZGa8UhQ")

```
> Example Response:

```json
{
  "id" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "verification" : null,
  "merchant_profile" : "MPg32sgckPhfindCMvLFCpP1",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-03-28T18:55:28.58Z",
  "updated_at" : "2017-03-28T18:55:28.69Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPg32sgckPhfindCMvLFCpP1"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
curl https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUzL5f3UkAwvK79iZGa8UhQ");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUzL5f3UkAwvK79iZGa8UhQ');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUzL5f3UkAwvK79iZGa8UhQ")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VI8ALocEuZZ1abgNUV68DXfG",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-28T18:55:46.93Z",
  "updated_at" : "2017-03-28T18:55:46.96Z",
  "trace_id" : "8138ab09-bcdb-4f54-a835-20dfe02ff697",
  "payment_instrument" : null,
  "merchant" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI8ALocEuZZ1abgNUV68DXfG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
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
curl https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '{}'

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUzL5f3UkAwvK79iZGa8UhQ');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUzL5f3UkAwvK79iZGa8UhQ")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VI8ALocEuZZ1abgNUV68DXfG",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-28T18:55:46.93Z",
  "updated_at" : "2017-03-28T18:55:46.96Z",
  "trace_id" : "8138ab09-bcdb-4f54-a835-20dfe02ff697",
  "payment_instrument" : null,
  "merchant" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI8ALocEuZZ1abgNUV68DXfG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
      "id" : "MUzL5f3UkAwvK79iZGa8UhQ",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "verification" : null,
      "merchant_profile" : "MPg32sgckPhfindCMvLFCpP1",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-03-28T18:55:28.58Z",
      "updated_at" : "2017-03-28T18:55:28.69Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPg32sgckPhfindCMvLFCpP1"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
curl https://api-staging.finix.io/merchants/MUzL5f3UkAwvK79iZGa8UhQ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUzL5f3UkAwvK79iZGa8UhQ');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUzL5f3UkAwvK79iZGa8UhQ")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID2YRE5PQEHtBTqoAAhJo2T3",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
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
        "ownership_type" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2017-03-28T18:55:29.36Z",
      "updated_at" : "2017-03-28T18:55:29.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDf8ppQpPnhuscMRrzBvions",
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
      "created_at" : "2017-03-28T18:55:27.30Z",
      "updated_at" : "2017-03-28T18:55:27.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDf8ppQpPnhuscMRrzBvions/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID69Zgg9iiRNYKSr2AHj6vdb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:26.94Z",
      "updated_at" : "2017-03-28T18:55:26.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID69Zgg9iiRNYKSr2AHj6vdb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID96ASpo53x7KRhGPmTR5hTi",
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
      "created_at" : "2017-03-28T18:55:26.29Z",
      "updated_at" : "2017-03-28T18:55:26.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID96ASpo53x7KRhGPmTR5hTi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID26rb9jU6WZrHKwrVp2kNtz",
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
      "created_at" : "2017-03-28T18:55:25.91Z",
      "updated_at" : "2017-03-28T18:55:25.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID26rb9jU6WZrHKwrVp2kNtz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID4d2yXxTHo1p25G5yiTQnEd",
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
      "created_at" : "2017-03-28T18:55:25.53Z",
      "updated_at" : "2017-03-28T18:55:25.53Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4d2yXxTHo1p25G5yiTQnEd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDkdK7Td1cSVwzdLqtzTZ87C",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:25.18Z",
      "updated_at" : "2017-03-28T18:55:25.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkdK7Td1cSVwzdLqtzTZ87C/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDpP8ScaAHxrsF4EAhTebdVt",
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
      "created_at" : "2017-03-28T18:55:24.81Z",
      "updated_at" : "2017-03-28T18:55:24.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpP8ScaAHxrsF4EAhTebdVt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDrt8ZVtJZyoUbBxDtRhF4Av",
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
      "created_at" : "2017-03-28T18:55:24.41Z",
      "updated_at" : "2017-03-28T18:55:24.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrt8ZVtJZyoUbBxDtRhF4Av/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDts5Jx2YdP5wMdFGhhrdbbQ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "CORPORATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:23.87Z",
      "updated_at" : "2017-03-28T18:55:23.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDts5Jx2YdP5wMdFGhhrdbbQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "ID6HTbvJWaQb7TUVSR2KpiqX",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-28T18:55:23.47Z",
      "updated_at" : "2017-03-28T18:55:23.47Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "HyperWallet",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "HyperWallet",
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
        "application_name" : "HyperWallet"
      },
      "created_at" : "2017-03-28T18:55:19.60Z",
      "updated_at" : "2017-03-28T18:55:19.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    "count" : 12
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "name": "Jessie Sterling", 
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
	    "identity": "ID2YRE5PQEHtBTqoAAhJo2T3"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
$card = new PaymentCard(
	array(
	    "name"=> "Jessie Sterling", 
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
	    "identity"=> "ID2YRE5PQEHtBTqoAAhJo2T3"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Jessie Sterling", 
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
	    "identity": "ID2YRE5PQEHtBTqoAAhJo2T3"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Jessie Sterling", 
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
	    "identity"=> "ID2YRE5PQEHtBTqoAAhJo2T3"
	}).save
```
> Example Response:

```json
{
  "id" : "PI7jjWoR9uGsiXetvjLnavUY",
  "fingerprint" : "FPR1412414468",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Sterling",
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
  "created_at" : "2017-03-28T18:55:29.91Z",
  "updated_at" : "2017-03-28T18:55:29.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2YRE5PQEHtBTqoAAhJo2T3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/updates"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
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
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
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
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
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
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save
```
> Example Response:

```json
{
  "id" : "PIgtzh7EvFDiSnynkwnsgr3z",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T18:55:27.69Z",
  "updated_at" : "2017-03-28T18:55:27.69Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;
import io.finix.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TKgNmLTEk6oCcDERZqCX7w2m")
    .identity("ID6HTbvJWaQb7TUVSR2KpiqX")
    .build()
);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type": "TOKEN", 
	    "identity": "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save()
```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKgNmLTEk6oCcDERZqCX7w2m", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID6HTbvJWaQb7TUVSR2KpiqX"
	}).save
```
> Example Response:

```json
{
  "id" : "PIgNmLTEk6oCcDERZqCX7w2m",
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
  "created_at" : "2017-03-28T18:55:36.64Z",
  "updated_at" : "2017-03-28T18:55:36.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/updates"
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


## Fetch a Bank Account

```shell
curl https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIgtzh7EvFDiSnynkwnsgr3z")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIgtzh7EvFDiSnynkwnsgr3z');

```
```python



```
```ruby
bank_account = Finix::BankAccount.retrieve(:id=> "PIgtzh7EvFDiSnynkwnsgr3z")

```
> Example Response:

```json
{
  "id" : "PIgtzh7EvFDiSnynkwnsgr3z",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-28T18:55:27.67Z",
  "updated_at" : "2017-03-28T18:55:28.12Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
curl https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI7jjWoR9uGsiXetvjLnavUY")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI7jjWoR9uGsiXetvjLnavUY');

```
```python



```
```ruby
card = Finix::PaymentCard.retrieve(:id=> "PI7jjWoR9uGsiXetvjLnavUY")


```
> Example Response:

```json
{
  "id" : "PI7jjWoR9uGsiXetvjLnavUY",
  "fingerprint" : "FPR1412414468",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Sterling",
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
  "created_at" : "2017-03-28T18:55:29.88Z",
  "updated_at" : "2017-03-28T18:55:34.81Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2YRE5PQEHtBTqoAAhJo2T3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/updates"
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
curl https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
    -d '
	{
	    "merchant": "MUzL5f3UkAwvK79iZGa8UhQ"
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
  "id" : "IUov1Gm81yCSwQ1eJeFKvyfa",
  "application" : "AP4GcWbztqRvJnJ9TydudDAF",
  "merchant" : "MUzL5f3UkAwvK79iZGa8UhQ",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-03-28T18:55:38.57Z",
  "updated_at" : "2017-03-28T18:55:38.59Z",
  "payment_instrument" : "PI7jjWoR9uGsiXetvjLnavUY",
  "trace_id" : "272c22fd-7cbd-4801-a0a7-e5382336cea8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/updates/IUov1Gm81yCSwQ1eJeFKvyfa"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce
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
      "id" : "PIgNmLTEk6oCcDERZqCX7w2m",
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
      "created_at" : "2017-03-28T18:55:36.60Z",
      "updated_at" : "2017-03-28T18:55:36.60Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNmLTEk6oCcDERZqCX7w2m/updates"
        }
      }
    }, {
      "id" : "PI93aEoSgVtXt6jzHnvLEJhA",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-28T18:55:30.33Z",
      "updated_at" : "2017-03-28T18:55:30.33Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID2YRE5PQEHtBTqoAAhJo2T3",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PI7jjWoR9uGsiXetvjLnavUY",
      "fingerprint" : "FPR1412414468",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jessie Sterling",
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
      "created_at" : "2017-03-28T18:55:29.88Z",
      "updated_at" : "2017-03-28T18:55:34.81Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2YRE5PQEHtBTqoAAhJo2T3",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2YRE5PQEHtBTqoAAhJo2T3"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY/updates"
        }
      }
    }, {
      "id" : "PI4a7VHiEJpsxY7C5G3kph16",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:28.58Z",
      "updated_at" : "2017-03-28T18:55:28.58Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4a7VHiEJpsxY7C5G3kph16"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4a7VHiEJpsxY7C5G3kph16/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4a7VHiEJpsxY7C5G3kph16/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4a7VHiEJpsxY7C5G3kph16/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIFWaMJsxLZ2qgw12rMAqQ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:28.58Z",
      "updated_at" : "2017-03-28T18:55:28.58Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIFWaMJsxLZ2qgw12rMAqQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIFWaMJsxLZ2qgw12rMAqQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIFWaMJsxLZ2qgw12rMAqQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIFWaMJsxLZ2qgw12rMAqQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PI4WcsKv49EfdUPgP6ymYP46",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:28.58Z",
      "updated_at" : "2017-03-28T18:55:28.58Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIgtzh7EvFDiSnynkwnsgr3z",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-28T18:55:27.67Z",
      "updated_at" : "2017-03-28T18:55:28.12Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIm4BdpEHQ2LvwNhzSPaTpVA",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:20.66Z",
      "updated_at" : "2017-03-28T18:55:20.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIxiiGwwFR3hBrsibXbed4Pb",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:20.66Z",
      "updated_at" : "2017-03-28T18:55:20.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIvBvDPG1kATDw1nJAhcFDY2",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:20.66Z",
      "updated_at" : "2017-03-28T18:55:20.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBvDPG1kATDw1nJAhcFDY2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBvDPG1kATDw1nJAhcFDY2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBvDPG1kATDw1nJAhcFDY2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBvDPG1kATDw1nJAhcFDY2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        }
      }
    }, {
      "id" : "PIroFj7KSRoK2TE3FmkMMonU",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-28T18:55:20.66Z",
      "updated_at" : "2017-03-28T18:55:20.66Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIroFj7KSRoK2TE3FmkMMonU"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIroFj7KSRoK2TE3FmkMMonU/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIroFj7KSRoK2TE3FmkMMonU/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIroFj7KSRoK2TE3FmkMMonU/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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

curl https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$identity = Identity::retrieve('ID6HTbvJWaQb7TUVSR2KpiqX');
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

identity = Identity.get(id="ID6HTbvJWaQb7TUVSR2KpiqX")
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
identity = Finix::Identity.retrieve(:id=>"ID6HTbvJWaQb7TUVSR2KpiqX")
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
  "id" : "STrXDzTso6jYd83jvQS9yoVL",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "currency" : "USD",
  "created_at" : "2017-03-28T18:58:11.14Z",
  "updated_at" : "2017-03-28T18:58:11.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1389672,
  "total_fees" : 138969,
  "total_fee" : 138969,
  "net_amount" : 1250703,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STrXDzTso6jYd83jvQS9yoVL");

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STrXDzTso6jYd83jvQS9yoVL');

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STrXDzTso6jYd83jvQS9yoVL")

```
> Example Response:

```json
{
  "id" : "STrXDzTso6jYd83jvQS9yoVL",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "currency" : "USD",
  "created_at" : "2017-03-28T18:58:11.10Z",
  "updated_at" : "2017-03-28T18:58:11.90Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 1389672,
  "total_fees" : 138969,
  "total_fee" : 138969,
  "net_amount" : 1250703,
  "destination" : "PIgtzh7EvFDiSnynkwnsgr3z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=debit"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
      "id" : "STrXDzTso6jYd83jvQS9yoVL",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "currency" : "USD",
      "created_at" : "2017-03-28T18:58:11.10Z",
      "updated_at" : "2017-03-28T18:58:11.90Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 1389672,
      "total_fees" : 138969,
      "total_fee" : 138969,
      "net_amount" : 1250703,
      "destination" : "PIgtzh7EvFDiSnynkwnsgr3z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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

$settlement = Settlement::retrieve('STrXDzTso6jYd83jvQS9yoVL');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STrXDzTso6jYd83jvQS9yoVL")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRb6HfADjA2e73bQv5RJh4tj",
      "amount" : 1250703,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "43bac67e-614d-4da5-82c9-897441be0769",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIgtzh7EvFDiSnynkwnsgr3z",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:11.59Z",
      "updated_at" : "2017-03-28T18:58:11.85Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRb6HfADjA2e73bQv5RJh4tj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRb6HfADjA2e73bQv5RJh4tj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRb6HfADjA2e73bQv5RJh4tj/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRb6HfADjA2e73bQv5RJh4tj/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRb6HfADjA2e73bQv5RJh4tj/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgtzh7EvFDiSnynkwnsgr3z"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

```
```java

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STrXDzTso6jYd83jvQS9yoVL');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STrXDzTso6jYd83jvQS9yoVL")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR2aDSXd99E2ogmBvreNv2kj",
      "amount" : 66994,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "87022e1b-9c25-40ff-aa9b-b93360a4de9f",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIxiiGwwFR3hBrsibXbed4Pb",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:10.49Z",
      "updated_at" : "2017-03-28T18:58:10.71Z",
      "merchant_identity" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR2aDSXd99E2ogmBvreNv2kj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR2aDSXd99E2ogmBvreNv2kj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR2aDSXd99E2ogmBvreNv2kj/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR2aDSXd99E2ogmBvreNv2kj/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR2aDSXd99E2ogmBvreNv2kj/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb"
        }
      }
    }, {
      "id" : "TRsEY1eR5wd9aHywi8WoDQSh",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "97605277-8890-4ef6-9695-eb5d29630e94",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIm4BdpEHQ2LvwNhzSPaTpVA",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:10.25Z",
      "updated_at" : "2017-03-28T18:58:10.47Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsEY1eR5wd9aHywi8WoDQSh"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsEY1eR5wd9aHywi8WoDQSh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsEY1eR5wd9aHywi8WoDQSh/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsEY1eR5wd9aHywi8WoDQSh/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsEY1eR5wd9aHywi8WoDQSh/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA"
        }
      }
    }, {
      "id" : "TRoEy7SfKR7GQc2eEHUHmi2P",
      "amount" : 71942,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "ef7aa4c7-f5e7-4c58-92af-76eaa83731de",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIxiiGwwFR3hBrsibXbed4Pb",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:09.96Z",
      "updated_at" : "2017-03-28T18:58:10.19Z",
      "merchant_identity" : "IDwKf7z2Xb5u4XNZwo36XA8",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRoEy7SfKR7GQc2eEHUHmi2P"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRoEy7SfKR7GQc2eEHUHmi2P/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwKf7z2Xb5u4XNZwo36XA8"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRoEy7SfKR7GQc2eEHUHmi2P/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRoEy7SfKR7GQc2eEHUHmi2P/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRoEy7SfKR7GQc2eEHUHmi2P/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxiiGwwFR3hBrsibXbed4Pb"
        }
      }
    }, {
      "id" : "TR7a6SKc5XLgR6mhob5bgAuf",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "402e7873-d2ac-4339-a4b3-b79c8f9e00a7",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIm4BdpEHQ2LvwNhzSPaTpVA",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:09.71Z",
      "updated_at" : "2017-03-28T18:58:09.94Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7a6SKc5XLgR6mhob5bgAuf"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7a6SKc5XLgR6mhob5bgAuf/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7a6SKc5XLgR6mhob5bgAuf/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7a6SKc5XLgR6mhob5bgAuf/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7a6SKc5XLgR6mhob5bgAuf/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA"
        }
      }
    }, {
      "id" : "TRe9pctiCVPuuiSMF2NpnXJv",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "814dbfa7-4ce9-4403-9121-2481645486bb",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PIm4BdpEHQ2LvwNhzSPaTpVA",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:58:09.39Z",
      "updated_at" : "2017-03-28T18:58:09.66Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRe9pctiCVPuuiSMF2NpnXJv"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRe9pctiCVPuuiSMF2NpnXJv/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRe9pctiCVPuuiSMF2NpnXJv/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRe9pctiCVPuuiSMF2NpnXJv/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRe9pctiCVPuuiSMF2NpnXJv/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4BdpEHQ2LvwNhzSPaTpVA"
        }
      }
    }, {
      "id" : "TRtE4ScbPV8nMnAQKLoZuy9F",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 10,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:35.23Z",
      "updated_at" : "2017-03-28T18:56:04.43Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    }, {
      "id" : "TRmLZcYKowxnXStMFXnek5Bf",
      "amount" : 670046,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "db3e6872-c0b5-4b30-834c-7fa86237de3d",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI93aEoSgVtXt6jzHnvLEJhA",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 67005,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:31.25Z",
      "updated_at" : "2017-03-28T18:56:13.35Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    }, {
      "id" : "TRhfnbG4E6jMS7wHHanXFpjg",
      "amount" : 719526,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "b6956c8f-99ec-4dee-8bf8-0dc4eccca5bc",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : "2017-03-28T18:58:09.30Z",
      "fee" : 71953,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:30.75Z",
      "updated_at" : "2017-03-28T18:56:07.71Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STrXDzTso6jYd83jvQS9yoVL/transfers?offset=0&limit=20&sort=created_at,desc"
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
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce


```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRhfnbG4E6jMS7wHHanXFpjg");

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRhfnbG4E6jMS7wHHanXFpjg');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TRhfnbG4E6jMS7wHHanXFpjg")

```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRhfnbG4E6jMS7wHHanXFpjg")

```
> Example Response:

```json
{
  "id" : "TRhfnbG4E6jMS7wHHanXFpjg",
  "amount" : 719526,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "b6956c8f-99ec-4dee-8bf8-0dc4eccca5bc",
  "currency" : "USD",
  "application" : "AP4GcWbztqRvJnJ9TydudDAF",
  "source" : "PI7jjWoR9uGsiXetvjLnavUY",
  "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
  "ready_to_settle_at" : null,
  "fee" : 71953,
  "statement_descriptor" : "FIN*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:30.75Z",
  "updated_at" : "2017-03-28T18:55:30.87Z",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
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

curl https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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

$debit = Transfer::retrieve('TRhfnbG4E6jMS7wHHanXFpjg');
$refund = $debit->reverse(11);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TRhfnbG4E6jMS7wHHanXFpjg")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRhfnbG4E6jMS7wHHanXFpjg")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TR9Jinm2wDTDJV4tYVeL2fH2",
  "amount" : 81938,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "46b10d11-354d-4fe7-a810-e1db9d77c78b",
  "currency" : "USD",
  "application" : "AP4GcWbztqRvJnJ9TydudDAF",
  "source" : "PI4WcsKv49EfdUPgP6ymYP46",
  "destination" : "PI7jjWoR9uGsiXetvjLnavUY",
  "ready_to_settle_at" : null,
  "fee" : 8194,
  "statement_descriptor" : "FIN*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-28T18:55:34.04Z",
  "updated_at" : "2017-03-28T18:55:34.11Z",
  "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR9Jinm2wDTDJV4tYVeL2fH2"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR9Jinm2wDTDJV4tYVeL2fH2/payment_instruments"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
      "id" : "TRtE4ScbPV8nMnAQKLoZuy9F",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "79225bf1-e422-490b-874e-ddfb05e1b271",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:35.23Z",
      "updated_at" : "2017-03-28T18:55:35.33Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtE4ScbPV8nMnAQKLoZuy9F/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    }, {
      "id" : "TR9Jinm2wDTDJV4tYVeL2fH2",
      "amount" : 81938,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "d8e633fa-7e57-4ba8-8c7d-0542c96bb65f",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI4WcsKv49EfdUPgP6ymYP46",
      "destination" : "PI7jjWoR9uGsiXetvjLnavUY",
      "ready_to_settle_at" : null,
      "fee" : 8194,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:33.93Z",
      "updated_at" : "2017-03-28T18:55:34.11Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR9Jinm2wDTDJV4tYVeL2fH2"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR9Jinm2wDTDJV4tYVeL2fH2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        }
      }
    }, {
      "id" : "TRqPCTNuS81r5mPHi192ixqD",
      "amount" : 81938,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "7d0642b2-6ede-469c-aa61-1df9d20be346",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : null,
      "fee" : 8194,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:33.24Z",
      "updated_at" : "2017-03-28T18:55:34.01Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqPCTNuS81r5mPHi192ixqD/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    }, {
      "id" : "TRmLZcYKowxnXStMFXnek5Bf",
      "amount" : 670046,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "db3e6872-c0b5-4b30-834c-7fa86237de3d",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI93aEoSgVtXt6jzHnvLEJhA",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : null,
      "fee" : 67005,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:31.25Z",
      "updated_at" : "2017-03-28T18:55:31.36Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRmLZcYKowxnXStMFXnek5Bf/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI93aEoSgVtXt6jzHnvLEJhA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
        }
      }
    }, {
      "id" : "TRhfnbG4E6jMS7wHHanXFpjg",
      "amount" : 719526,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "b6956c8f-99ec-4dee-8bf8-0dc4eccca5bc",
      "currency" : "USD",
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "source" : "PI7jjWoR9uGsiXetvjLnavUY",
      "destination" : "PI4WcsKv49EfdUPgP6ymYP46",
      "ready_to_settle_at" : null,
      "fee" : 71953,
      "statement_descriptor" : "FIN*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-28T18:55:30.75Z",
      "updated_at" : "2017-03-28T18:55:30.87Z",
      "merchant_identity" : "ID6HTbvJWaQb7TUVSR2KpiqX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6HTbvJWaQb7TUVSR2KpiqX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRhfnbG4E6jMS7wHHanXFpjg/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7jjWoR9uGsiXetvjLnavUY"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4WcsKv49EfdUPgP6ymYP46"
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
    -u UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce \
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
  "id" : "WHdrWvr5eWHMHe3kSABBBM6t",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP4GcWbztqRvJnJ9TydudDAF",
  "created_at" : "2017-03-28T18:55:23.14Z",
  "updated_at" : "2017-03-28T18:55:23.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHdrWvr5eWHMHe3kSABBBM6t"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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



curl https://api-staging.finix.io/webhooks/WHdrWvr5eWHMHe3kSABBBM6t \
    -H "Content-Type: application/vnd.json+api" \
    -u UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce


```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHdrWvr5eWHMHe3kSABBBM6t");

```
```php
<?php
use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHdrWvr5eWHMHe3kSABBBM6t');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WHdrWvr5eWHMHe3kSABBBM6t")

```
```ruby
webhook = Finix::Webhook.retrieve(:id=> "WHdrWvr5eWHMHe3kSABBBM6t")


```
> Example Response:

```json
{
  "id" : "WHdrWvr5eWHMHe3kSABBBM6t",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP4GcWbztqRvJnJ9TydudDAF",
  "created_at" : "2017-03-28T18:55:23.14Z",
  "updated_at" : "2017-03-28T18:55:23.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHdrWvr5eWHMHe3kSABBBM6t"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
    -u  UScrRBEbdXh6eXUnME9c1MYF:dfee4bb1-595c-40b8-888b-7efae106f0ce

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
      "id" : "WHdrWvr5eWHMHe3kSABBBM6t",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "AP4GcWbztqRvJnJ9TydudDAF",
      "created_at" : "2017-03-28T18:55:23.14Z",
      "updated_at" : "2017-03-28T18:55:23.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHdrWvr5eWHMHe3kSABBBM6t"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4GcWbztqRvJnJ9TydudDAF"
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
