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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
  client.setupUserIdAndPassword("USjHdX7bDkJbuypYXRnou9Yo", "ef77a904-9caf-47e9-a27e-df9a9bc199bb");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');

Finix\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USjHdX7bDkJbuypYXRnou9Yo',
	"password" => 'ef77a904-9caf-47e9-a27e-df9a9bc199bb']
	);

require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USjHdX7bDkJbuypYXRnou9Yo", "ef77a904-9caf-47e9-a27e-df9a9bc199bb"))

```
```ruby
# To download the Ruby gem:
# gem install finix

require 'finix'

Finix.configure(
    :root_url => 'https://api-staging.finix.io',
    :user=>'USjHdX7bDkJbuypYXRnou9Yo',
    :password => 'ef77a904-9caf-47e9-a27e-df9a9bc199bb'
)
```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USjHdX7bDkJbuypYXRnou9Yo`

- Password: `ef77a904-9caf-47e9-a27e-df9a9bc199bb`

- Application ID: `AP7BtUzQvgjfaARjZcREoqh9`

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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
	        "default_statement_descriptor": "ACME Anchors", 
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
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
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
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "ACME Anchors", 
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
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.ACMEAnchors.com", 
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
	        "default_statement_descriptor": "ACME Anchors", 
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
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
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
	        "default_statement_descriptor"=> "ACME Anchors", 
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
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.ACMEAnchors.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:51.52Z",
  "updated_at" : "2017-01-27T18:52:51.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDkWDHzBfY3NwnyuvkgNWXeZ"
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
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
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
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
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
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
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save
```
> Example Response:

```json
{
  "id" : "PIcSo1AS5P35ZAJrdq8FNefy",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:55.51Z",
  "updated_at" : "2017-01-27T18:52:55.51Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDkWDHzBfY3NwnyuvkgNWXeZ")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDkWDHzBfY3NwnyuvkgNWXeZ")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUgccutHtouqSEntragrmzWb",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "verification" : "VIjJooW2ir6oaf9EhPzksLmD",
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:56.32Z",
  "updated_at" : "2017-01-27T18:52:56.32Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIjJooW2ir6oaf9EhPzksLmD"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Michae", 
	        "last_name": "Sterling", 
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
	        "first_name"=> "Michae", 
	        "last_name"=> "Sterling", 
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
	        "first_name": "Michae", 
	        "last_name": "Sterling", 
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
	        "first_name"=> "Michae", 
	        "last_name"=> "Sterling", 
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
  "id" : "IDo6U9BcM7amTBPDn42cGPD3",
  "entity" : {
    "title" : null,
    "first_name" : "Michae",
    "last_name" : "Sterling",
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
  "created_at" : "2017-01-27T18:52:57.16Z",
  "updated_at" : "2017-01-27T18:52:57.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "name": "Laura Serna", 
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
	    "identity": "IDo6U9BcM7amTBPDn42cGPD3"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Serna", 
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
	    "identity"=> "IDo6U9BcM7amTBPDn42cGPD3"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Serna", 
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
	    "identity": "IDo6U9BcM7amTBPDn42cGPD3"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Laura Serna", 
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
	    "identity"=> "IDo6U9BcM7amTBPDn42cGPD3"
	}).save
```
> Example Response:

```json
{
  "id" : "PIp6LKtF1imZBtmKZWFYrk56",
  "fingerprint" : "FPR1682317982",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Serna",
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
  "created_at" : "2017-01-27T18:52:57.62Z",
  "updated_at" : "2017-01-27T18:52:57.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDo6U9BcM7amTBPDn42cGPD3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/updates"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "merchant_identity": "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIp6LKtF1imZBtmKZWFYrk56", 
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
    .merchantIdentity("IDkWDHzBfY3NwnyuvkgNWXeZ")
    .source("PIp6LKtF1imZBtmKZWFYrk56")
    .build()
);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIp6LKtF1imZBtmKZWFYrk56", 
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
	    "merchant_identity": "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIp6LKtF1imZBtmKZWFYrk56", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIp6LKtF1imZBtmKZWFYrk56", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:02.13Z",
  "updated_at" : "2017-01-27T18:53:02.19Z",
  "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:53:02.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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
curl https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUcnDT4fZSE3MvMBMe1pbQcj");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUcnDT4fZSE3MvMBMe1pbQcj');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUcnDT4fZSE3MvMBMe1pbQcj")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUcnDT4fZSE3MvMBMe1pbQcj")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRdh2sn5V8TnXJAvQZyMJ9FR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:02.08Z",
  "updated_at" : "2017-01-27T18:53:02.69Z",
  "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:53:02.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
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

identity = Identity.get(id="IDkWDHzBfY3NwnyuvkgNWXeZ")
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
identity = Finix::Identity.retrieve(:id=>"IDkWDHzBfY3NwnyuvkgNWXeZ")
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
  "id" : "STYYBiBaZJqvjKczp5hosUb",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:54:11.18Z",
  "updated_at" : "2017-01-27T18:54:11.25Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 817581,
  "total_fees" : 81758,
  "total_fee" : 81758,
  "net_amount" : 735823,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=debit"
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
    -u USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Walter", 
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

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Walter", 
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



```
```ruby
identity = Finix::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Walter", 
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
  "id" : "ID2WdZ6gu28sXNMVJdypfqEX",
  "entity" : {
    "title" : null,
    "first_name" : "Walter",
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
  "created_at" : "2017-01-27T18:53:09.64Z",
  "updated_at" : "2017-01-27T18:53:09.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "name": "Alex Chang", 
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
	    "identity": "ID2WdZ6gu28sXNMVJdypfqEX"
	}'
```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
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

$identity = Identity::retrieve('ID2WdZ6gu28sXNMVJdypfqEX');
$card = new PaymentCard(
	array(
	    "name"=> "Alex Chang", 
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
	    "identity"=> "ID2WdZ6gu28sXNMVJdypfqEX"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Alex Chang", 
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
	    "identity"=> "ID2WdZ6gu28sXNMVJdypfqEX"
	}).save
```
> Example Response:

```json
{
  "id" : "PImDZPf7MFrUUmZ5njWqLStG",
  "fingerprint" : "FPR2120714632",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Alex Chang",
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
  "created_at" : "2017-01-27T18:53:10.01Z",
  "updated_at" : "2017-01-27T18:53:10.01Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/updates"
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
curl https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
Identity identity = client.identitiesClient().fetchResource("PImDZPf7MFrUUmZ5njWqLStG");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('ID2WdZ6gu28sXNMVJdypfqEX');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"PImDZPf7MFrUUmZ5njWqLStG")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUjf82x1MwySDgpfve2epZyh",
  "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
  "verification" : "VI2VQ3143xeQXMBbyDLgd4kz",
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:53:10.41Z",
  "updated_at" : "2017-01-27T18:53:10.41Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUjf82x1MwySDgpfve2epZyh"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUjf82x1MwySDgpfve2epZyh/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI2VQ3143xeQXMBbyDLgd4kz"
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
    -u USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PImDZPf7MFrUUmZ5njWqLStG", 
	    "processor": "VISA_V1", 
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
	    "destination"=> "PImDZPf7MFrUUmZ5njWqLStG", 
	    "processor"=> "VISA_V1", 
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
	    "destination"=> "PImDZPf7MFrUUmZ5njWqLStG", 
	    "processor"=> "VISA_V1", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "TRpexjDp3rXwmKpq4N3kvZHK",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190066",
  "currency" : "USD",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "source" : "PIbMC54VgQ3UEMgNS5FCZbMa",
  "destination" : "PImDZPf7MFrUUmZ5njWqLStG",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:11.62Z",
  "updated_at" : "2017-01-27T18:53:12.57Z",
  "merchant_identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG"
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
          applicationId: 'AP7BtUzQvgjfaARjZcREoqh9',
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
  "id" : "TKH5FBrtgZowSzFZ9sw5oxT",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-27T18:53:03.73Z",
  "updated_at" : "2017-01-27T18:53:03.73Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-28T18:53:03.73Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKH5FBrtgZowSzFZ9sw5oxT")
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save
```
> Example Response:

```json
{
  "id" : "PIH5FBrtgZowSzFZ9sw5oxT",
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
  "created_at" : "2017-01-27T18:53:04.08Z",
  "updated_at" : "2017-01-27T18:53:04.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/updates"
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
    applicationId: "AP7BtUzQvgjfaARjZcREoqh9",
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
  "id" : "TKH5FBrtgZowSzFZ9sw5oxT",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-27T18:53:03.73Z",
  "updated_at" : "2017-01-27T18:53:03.73Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-28T18:53:03.73Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}'

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKH5FBrtgZowSzFZ9sw5oxT")
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save
```
> Example Response:

```json
{
  "id" : "PIH5FBrtgZowSzFZ9sw5oxT",
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
  "created_at" : "2017-01-27T18:53:04.08Z",
  "updated_at" : "2017-01-27T18:53:04.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/updates"
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
  "id" : "USjHdX7bDkJbuypYXRnou9Yo",
  "password" : "ef77a904-9caf-47e9-a27e-df9a9bc199bb",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:48.47Z",
  "updated_at" : "2017-01-27T18:52:48.47Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjHdX7bDkJbuypYXRnou9Yo"
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
	        "application_name": "Paypal"
	    }, 
	    "user": "USjHdX7bDkJbuypYXRnou9Yo", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
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
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "USjHdX7bDkJbuypYXRnou9Yo", 
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
```ruby

```
> Example Response:

```json
{
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:52:48.88Z",
  "updated_at" : "2017-01-27T18:52:48.88Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors \
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
  "id" : "PR7tXsVWmh2muaQ2Yj5cuq7T",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "default_merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "created_at" : "2017-01-27T18:52:49.37Z",
  "updated_at" : "2017-01-27T18:52:49.37Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors/PR7tXsVWmh2muaQ2Yj5cuq7T"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/ \
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
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:52:48.87Z",
  "updated_at" : "2017-01-27T18:54:18.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/ \
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
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:52:48.87Z",
  "updated_at" : "2017-01-27T18:54:19.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use Finix\Resources\Application;

$application = Application::retrieve('AP7BtUzQvgjfaARjZcREoqh9');

```
```python


from finix.resources import Application

application = Application.get(id="AP7BtUzQvgjfaARjZcREoqh9")
```
```ruby

```
> Example Response:

```json
{
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:52:48.87Z",
  "updated_at" : "2017-01-27T18:52:50.85Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "US5ds9NWLiEvEcqhYsCGgGa6",
  "password" : "d227131b-cc16-43c1-ac69-c7abc248a6f5",
  "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:50.00Z",
  "updated_at" : "2017-01-27T18:52:50.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US5ds9NWLiEvEcqhYsCGgGa6"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
	        "application_name": "Paypal"
	    }, 
	    "user": "USjHdX7bDkJbuypYXRnou9Yo", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
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
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "USjHdX7bDkJbuypYXRnou9Yo", 
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


from finix.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "USjHdX7bDkJbuypYXRnou9Yo", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
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
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:52:48.88Z",
  "updated_at" : "2017-01-27T18:52:48.88Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
## [ADMIN] Disable Processing Functionality
```shell
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/ \
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
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-01-27T18:52:48.87Z",
  "updated_at" : "2017-01-27T18:54:17.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/ \
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
  "id" : "AP7BtUzQvgjfaARjZcREoqh9",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-27T18:52:48.87Z",
  "updated_at" : "2017-01-27T18:54:17.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors \
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
  "id" : "PR7tXsVWmh2muaQ2Yj5cuq7T",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "default_merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "created_at" : "2017-01-27T18:52:49.37Z",
  "updated_at" : "2017-01-27T18:52:49.37Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors/PR7tXsVWmh2muaQ2Yj5cuq7T"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "AP7BtUzQvgjfaARjZcREoqh9",
      "enabled" : true,
      "tags" : {
        "application_name" : "Paypal"
      },
      "owner" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-01-27T18:52:48.87Z",
      "updated_at" : "2017-01-27T18:52:50.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/application_profile"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "merchant_identity": "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIp6LKtF1imZBtmKZWFYrk56", 
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
    .merchantIdentity("IDkWDHzBfY3NwnyuvkgNWXeZ")
    .source("PIp6LKtF1imZBtmKZWFYrk56")
    .build()
);


```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIp6LKtF1imZBtmKZWFYrk56", 
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
	    "merchant_identity": "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIp6LKtF1imZBtmKZWFYrk56", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIp6LKtF1imZBtmKZWFYrk56", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:02.13Z",
  "updated_at" : "2017-01-27T18:53:02.19Z",
  "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:53:02.13Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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
curl https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUcnDT4fZSE3MvMBMe1pbQcj");
authorization = authorization.capture(50L);

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUcnDT4fZSE3MvMBMe1pbQcj');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUcnDT4fZSE3MvMBMe1pbQcj")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUcnDT4fZSE3MvMBMe1pbQcj")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRdh2sn5V8TnXJAvQZyMJ9FR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:02.08Z",
  "updated_at" : "2017-01-27T18:53:02.69Z",
  "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:53:02.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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

curl https://api-staging.finix.io/authorizations/AUsLRWgv3x4ZAwY5t1vboPks \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$authorization = Authorization::retrieve('AUcnDT4fZSE3MvMBMe1pbQcj');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUcnDT4fZSE3MvMBMe1pbQcj")
authorization.void()

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUcnDT4fZSE3MvMBMe1pbQcj")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AUsLRWgv3x4ZAwY5t1vboPks",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:04.51Z",
  "updated_at" : "2017-01-27T18:53:05.25Z",
  "trace_id" : "27f0d8b5-233a-4e93-91a1-3e308edc0d16",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : true,
  "expires_at" : "2017-02-03T18:53:04.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUsLRWgv3x4ZAwY5t1vboPks"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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

curl https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUcnDT4fZSE3MvMBMe1pbQcj");

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUcnDT4fZSE3MvMBMe1pbQcj');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUcnDT4fZSE3MvMBMe1pbQcj")
```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUcnDT4fZSE3MvMBMe1pbQcj")


```
> Example Response:

```json
{
  "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRdh2sn5V8TnXJAvQZyMJ9FR",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:02.08Z",
  "updated_at" : "2017-01-27T18:53:02.69Z",
  "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:53:02.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "AUsLRWgv3x4ZAwY5t1vboPks",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:04.51Z",
      "updated_at" : "2017-01-27T18:53:05.25Z",
      "trace_id" : "27f0d8b5-233a-4e93-91a1-3e308edc0d16",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "is_void" : true,
      "expires_at" : "2017-02-03T18:53:04.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUsLRWgv3x4ZAwY5t1vboPks"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        }
      }
    }, {
      "id" : "AUcnDT4fZSE3MvMBMe1pbQcj",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRdh2sn5V8TnXJAvQZyMJ9FR",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:02.08Z",
      "updated_at" : "2017-01-27T18:53:02.69Z",
      "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "is_void" : false,
      "expires_at" : "2017-02-03T18:53:02.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUcnDT4fZSE3MvMBMe1pbQcj"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Michae", 
	        "last_name": "Sterling", 
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
	        "first_name"=> "Michae", 
	        "last_name"=> "Sterling", 
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
	        "first_name": "Michae", 
	        "last_name": "Sterling", 
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
	        "first_name"=> "Michae", 
	        "last_name"=> "Sterling", 
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
  "id" : "IDo6U9BcM7amTBPDn42cGPD3",
  "entity" : {
    "title" : null,
    "first_name" : "Michae",
    "last_name" : "Sterling",
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
  "created_at" : "2017-01-27T18:52:57.16Z",
  "updated_at" : "2017-01-27T18:52:57.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
	        "default_statement_descriptor": "ACME Anchors", 
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
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
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
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "ACME Anchors", 
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
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.ACMEAnchors.com", 
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
	        "default_statement_descriptor": "ACME Anchors", 
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
	        "doing_business_as": "ACME Anchors", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "ACME Anchors", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.ACMEAnchors.com", 
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
	        "default_statement_descriptor"=> "ACME Anchors", 
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
	        "doing_business_as"=> "ACME Anchors", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "ACME Anchors", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.ACMEAnchors.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:51.52Z",
  "updated_at" : "2017-01-27T18:52:51.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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

curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDkWDHzBfY3NwnyuvkgNWXeZ");

```
```php
<?php
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
```
```python


from finix.resources import Identity
identity = Identity.get(id="IDkWDHzBfY3NwnyuvkgNWXeZ")

```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDkWDHzBfY3NwnyuvkgNWXeZ")


```
> Example Response:

```json
{
  "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:51.50Z",
  "updated_at" : "2017-01-27T18:52:51.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Kline", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Pollos Hermanos", 
	        "url": "www.PollosHermanos.com", 
	        "business_name": "Pollos Hermanos", 
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
identity = Finix::Identity.retrieve(:id=>"IDkWDHzBfY3NwnyuvkgNWXeZ")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Kline",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Pollos Hermanos",
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
    "key" : "value_2"
  },
  "created_at" : "2017-01-27T18:52:51.50Z",
  "updated_at" : "2017-01-27T18:53:17.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
## List all Identities
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb


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
      "id" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "entity" : {
        "title" : null,
        "first_name" : "Walter",
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
      "created_at" : "2017-01-27T18:53:09.63Z",
      "updated_at" : "2017-01-27T18:53:09.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDo6U9BcM7amTBPDn42cGPD3",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Sterling",
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
      "created_at" : "2017-01-27T18:52:57.15Z",
      "updated_at" : "2017-01-27T18:52:57.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID9nssdEPkNxHQhn2hgBFWaT",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:55.12Z",
      "updated_at" : "2017-01-27T18:52:55.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID5vHFGMt7ujxChSHy4N9BHU",
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
      "created_at" : "2017-01-27T18:52:54.77Z",
      "updated_at" : "2017-01-27T18:52:54.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeogB7uEhiL8trL64MQwCMc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:54.40Z",
      "updated_at" : "2017-01-27T18:52:54.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDsU5fPQGJMvJYsw37kwMFMp",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.93Z",
      "updated_at" : "2017-01-27T18:52:53.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDaVCZPihgvncvsoNfWm8EkH",
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
      "created_at" : "2017-01-27T18:52:53.56Z",
      "updated_at" : "2017-01-27T18:52:53.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeTJAW1mVcHXU5pBjQ3ZJ9",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.21Z",
      "updated_at" : "2017-01-27T18:52:53.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDoQEcNxtDgeFPgLiHaLvJi3",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2017-01-27T18:52:52.85Z",
      "updated_at" : "2017-01-27T18:52:52.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDnGdzrpQusXwTeG69PnwtVm",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2017-01-27T18:52:52.44Z",
      "updated_at" : "2017-01-27T18:52:52.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID3Y3aUxuvXLE3UkijhcpdUU",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:52.03Z",
      "updated_at" : "2017-01-27T18:52:52.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:51.50Z",
      "updated_at" : "2017-01-27T18:52:51.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDxcRYizGuk3SPJXrHkvvRqF",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2017-01-27T18:52:48.87Z",
      "updated_at" : "2017-01-27T18:52:48.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
```shell
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="IDkWDHzBfY3NwnyuvkgNWXeZ")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id => "MUgccutHtouqSEntragrmzWb")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUgccutHtouqSEntragrmzWb",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "verification" : "VIjJooW2ir6oaf9EhPzksLmD",
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:56.32Z",
  "updated_at" : "2017-01-27T18:52:56.32Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIjJooW2ir6oaf9EhPzksLmD"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUgccutHtouqSEntragrmzWb");

```
```php
<?php
use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUgccutHtouqSEntragrmzWb');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MUgccutHtouqSEntragrmzWb")

```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUgccutHtouqSEntragrmzWb")

```
> Example Response:

```json
{
  "id" : "MUgccutHtouqSEntragrmzWb",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "verification" : null,
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:56.28Z",
  "updated_at" : "2017-01-27T18:52:56.40Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '{}'

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUgccutHtouqSEntragrmzWb');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUgccutHtouqSEntragrmzWb")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIxowqCk3BriZT5N4qevojeV",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:53:18.60Z",
  "updated_at" : "2017-01-27T18:53:18.62Z",
  "trace_id" : "6d65b1a2-c02c-40bf-98c5-515d45eabeb2",
  "payment_instrument" : null,
  "merchant" : "MUgccutHtouqSEntragrmzWb",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIxowqCk3BriZT5N4qevojeV"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUgccutHtouqSEntragrmzWb");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUgccutHtouqSEntragrmzWb');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUgccutHtouqSEntragrmzWb")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIxowqCk3BriZT5N4qevojeV",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:53:18.60Z",
  "updated_at" : "2017-01-27T18:53:18.62Z",
  "trace_id" : "6d65b1a2-c02c-40bf-98c5-515d45eabeb2",
  "payment_instrument" : null,
  "merchant" : "MUgccutHtouqSEntragrmzWb",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIxowqCk3BriZT5N4qevojeV"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/ \
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
  "id" : "MUgccutHtouqSEntragrmzWb",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "verification" : null,
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:56.28Z",
  "updated_at" : "2017-01-27T18:54:16.07Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/ \
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
  "id" : "MUgccutHtouqSEntragrmzWb",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "verification" : null,
  "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:56.28Z",
  "updated_at" : "2017-01-27T18:54:16.84Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "MUjf82x1MwySDgpfve2epZyh",
      "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "verification" : null,
      "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
      "processor" : "VISA_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-27T18:53:10.36Z",
      "updated_at" : "2017-01-27T18:53:10.80Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUjf82x1MwySDgpfve2epZyh"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUjf82x1MwySDgpfve2epZyh/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "MUgccutHtouqSEntragrmzWb",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "verification" : null,
      "merchant_profile" : "MPwm9NrVoKLh2ErFs4aFQhev",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-27T18:52:56.28Z",
      "updated_at" : "2017-01-27T18:52:56.40Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPwm9NrVoKLh2ErFs4aFQhev"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUgccutHtouqSEntragrmzWb');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUgccutHtouqSEntragrmzWb")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "entity" : {
        "title" : null,
        "first_name" : "Walter",
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
      "created_at" : "2017-01-27T18:53:09.63Z",
      "updated_at" : "2017-01-27T18:53:09.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDo6U9BcM7amTBPDn42cGPD3",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Sterling",
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
      "created_at" : "2017-01-27T18:52:57.15Z",
      "updated_at" : "2017-01-27T18:52:57.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID9nssdEPkNxHQhn2hgBFWaT",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:55.12Z",
      "updated_at" : "2017-01-27T18:52:55.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID5vHFGMt7ujxChSHy4N9BHU",
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
      "created_at" : "2017-01-27T18:52:54.77Z",
      "updated_at" : "2017-01-27T18:52:54.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeogB7uEhiL8trL64MQwCMc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:54.40Z",
      "updated_at" : "2017-01-27T18:52:54.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDsU5fPQGJMvJYsw37kwMFMp",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.93Z",
      "updated_at" : "2017-01-27T18:52:53.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDaVCZPihgvncvsoNfWm8EkH",
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
      "created_at" : "2017-01-27T18:52:53.56Z",
      "updated_at" : "2017-01-27T18:52:53.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeTJAW1mVcHXU5pBjQ3ZJ9",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.21Z",
      "updated_at" : "2017-01-27T18:52:53.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDoQEcNxtDgeFPgLiHaLvJi3",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2017-01-27T18:52:52.85Z",
      "updated_at" : "2017-01-27T18:52:52.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDnGdzrpQusXwTeG69PnwtVm",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2017-01-27T18:52:52.44Z",
      "updated_at" : "2017-01-27T18:52:52.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID3Y3aUxuvXLE3UkijhcpdUU",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:52.03Z",
      "updated_at" : "2017-01-27T18:52:52.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:51.50Z",
      "updated_at" : "2017-01-27T18:52:51.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDxcRYizGuk3SPJXrHkvvRqF",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2017-01-27T18:52:48.87Z",
      "updated_at" : "2017-01-27T18:52:48.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
```shell
curl https://api-staging.finix.io/merchants/MUgccutHtouqSEntragrmzWb/verifications \
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
      "id" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "entity" : {
        "title" : null,
        "first_name" : "Walter",
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
      "created_at" : "2017-01-27T18:53:09.63Z",
      "updated_at" : "2017-01-27T18:53:09.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDo6U9BcM7amTBPDn42cGPD3",
      "entity" : {
        "title" : null,
        "first_name" : "Michae",
        "last_name" : "Sterling",
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
      "created_at" : "2017-01-27T18:52:57.15Z",
      "updated_at" : "2017-01-27T18:52:57.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID9nssdEPkNxHQhn2hgBFWaT",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:55.12Z",
      "updated_at" : "2017-01-27T18:52:55.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9nssdEPkNxHQhn2hgBFWaT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID5vHFGMt7ujxChSHy4N9BHU",
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
      "created_at" : "2017-01-27T18:52:54.77Z",
      "updated_at" : "2017-01-27T18:52:54.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5vHFGMt7ujxChSHy4N9BHU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeogB7uEhiL8trL64MQwCMc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:54.40Z",
      "updated_at" : "2017-01-27T18:52:54.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeogB7uEhiL8trL64MQwCMc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDsU5fPQGJMvJYsw37kwMFMp",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.93Z",
      "updated_at" : "2017-01-27T18:52:53.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsU5fPQGJMvJYsw37kwMFMp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDaVCZPihgvncvsoNfWm8EkH",
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
      "created_at" : "2017-01-27T18:52:53.56Z",
      "updated_at" : "2017-01-27T18:52:53.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaVCZPihgvncvsoNfWm8EkH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDeTJAW1mVcHXU5pBjQ3ZJ9",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:53.21Z",
      "updated_at" : "2017-01-27T18:52:53.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeTJAW1mVcHXU5pBjQ3ZJ9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDoQEcNxtDgeFPgLiHaLvJi3",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2017-01-27T18:52:52.85Z",
      "updated_at" : "2017-01-27T18:52:52.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoQEcNxtDgeFPgLiHaLvJi3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDnGdzrpQusXwTeG69PnwtVm",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2017-01-27T18:52:52.44Z",
      "updated_at" : "2017-01-27T18:52:52.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnGdzrpQusXwTeG69PnwtVm/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "ID3Y3aUxuvXLE3UkijhcpdUU",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:52.03Z",
      "updated_at" : "2017-01-27T18:52:52.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3Y3aUxuvXLE3UkijhcpdUU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:51.50Z",
      "updated_at" : "2017-01-27T18:52:51.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "IDxcRYizGuk3SPJXrHkvvRqF",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2017-01-27T18:52:48.87Z",
      "updated_at" : "2017-01-27T18:52:48.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
```shell
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "USmyiv7tNfTzyj6iqX99Pu1H",
  "password" : "e65cbeda-602e-417f-be38-d584505a354a",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:59.53Z",
  "updated_at" : "2017-01-27T18:52:59.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USmyiv7tNfTzyj6iqX99Pu1H"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;
import io.finix.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TKH5FBrtgZowSzFZ9sw5oxT")
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
    .build()
);

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type": "TOKEN", 
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save()
```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKH5FBrtgZowSzFZ9sw5oxT", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save
```
> Example Response:

```json
{
  "id" : "PIH5FBrtgZowSzFZ9sw5oxT",
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
  "created_at" : "2017-01-27T18:53:04.08Z",
  "updated_at" : "2017-01-27T18:53:04.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/updates"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "name": "Laura Serna", 
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
	    "identity": "IDo6U9BcM7amTBPDn42cGPD3"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Serna", 
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
	    "identity"=> "IDo6U9BcM7amTBPDn42cGPD3"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura Serna", 
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
	    "identity": "IDo6U9BcM7amTBPDn42cGPD3"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Laura Serna", 
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
	    "identity"=> "IDo6U9BcM7amTBPDn42cGPD3"
	}).save
```
> Example Response:

```json
{
  "id" : "PIp6LKtF1imZBtmKZWFYrk56",
  "fingerprint" : "FPR1682317982",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Serna",
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
  "created_at" : "2017-01-27T18:52:57.62Z",
  "updated_at" : "2017-01-27T18:52:57.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDo6U9BcM7amTBPDn42cGPD3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/updates"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;
import io.finix.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDkWDHzBfY3NwnyuvkgNWXeZ")
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
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
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
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
	    "identity": "IDkWDHzBfY3NwnyuvkgNWXeZ"
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
	    "identity"=> "IDkWDHzBfY3NwnyuvkgNWXeZ"
	}).save
```
> Example Response:

```json
{
  "id" : "PIcSo1AS5P35ZAJrdq8FNefy",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:55.51Z",
  "updated_at" : "2017-01-27T18:52:55.51Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
## Fetch a Bank Account

```shell
curl https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIcSo1AS5P35ZAJrdq8FNefy")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIcSo1AS5P35ZAJrdq8FNefy');

```
```python



```
```ruby
bank_account = Finix::BankAccount.retrieve(:id=> "PIcSo1AS5P35ZAJrdq8FNefy")

```
> Example Response:

```json
{
  "id" : "PIcSo1AS5P35ZAJrdq8FNefy",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:55.48Z",
  "updated_at" : "2017-01-27T18:52:55.88Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIp6LKtF1imZBtmKZWFYrk56")

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIp6LKtF1imZBtmKZWFYrk56');

```
```python



```
```ruby
card = Finix::PaymentCard.retrieve(:id=> "PIp6LKtF1imZBtmKZWFYrk56")


```
> Example Response:

```json
{
  "id" : "PIp6LKtF1imZBtmKZWFYrk56",
  "fingerprint" : "FPR1682317982",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Serna",
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
  "created_at" : "2017-01-27T18:52:57.57Z",
  "updated_at" : "2017-01-27T18:53:02.17Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDo6U9BcM7amTBPDn42cGPD3",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/updates"
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
curl https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
    -d '
	{
	    "merchant": "MUgccutHtouqSEntragrmzWb"
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
  "id" : "IUiZr5mV82wwNPWY79eduFfi",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "merchant" : "MUgccutHtouqSEntragrmzWb",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-01-27T18:53:05.70Z",
  "updated_at" : "2017-01-27T18:53:05.72Z",
  "payment_instrument" : "PIp6LKtF1imZBtmKZWFYrk56",
  "trace_id" : "8649a57b-3019-4284-8aaf-aaa0bed7df86",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/updates/IUiZr5mV82wwNPWY79eduFfi"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb
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
      "id" : "PIbMC54VgQ3UEMgNS5FCZbMa",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:10.36Z",
      "updated_at" : "2017-01-27T18:53:10.36Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIeQXdboN7sp3WbkZFLvXYCL",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:10.36Z",
      "updated_at" : "2017-01-27T18:53:10.36Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeQXdboN7sp3WbkZFLvXYCL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeQXdboN7sp3WbkZFLvXYCL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeQXdboN7sp3WbkZFLvXYCL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeQXdboN7sp3WbkZFLvXYCL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIkAg3ak1wDAfCKNjxijCLgA",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:10.36Z",
      "updated_at" : "2017-01-27T18:53:10.36Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAg3ak1wDAfCKNjxijCLgA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAg3ak1wDAfCKNjxijCLgA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAg3ak1wDAfCKNjxijCLgA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAg3ak1wDAfCKNjxijCLgA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PImDZPf7MFrUUmZ5njWqLStG",
      "fingerprint" : "FPR2120714632",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Alex Chang",
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
      "created_at" : "2017-01-27T18:53:09.98Z",
      "updated_at" : "2017-01-27T18:53:09.98Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG/updates"
        }
      }
    }, {
      "id" : "PI5K3byJUjhMtqZkUwcow7n2",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:08.74Z",
      "updated_at" : "2017-01-27T18:53:08.74Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5K3byJUjhMtqZkUwcow7n2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5K3byJUjhMtqZkUwcow7n2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5K3byJUjhMtqZkUwcow7n2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5K3byJUjhMtqZkUwcow7n2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIgQJ4wFjU2nXw3cts1LZoMZ",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:08.74Z",
      "updated_at" : "2017-01-27T18:53:08.74Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQJ4wFjU2nXw3cts1LZoMZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQJ4wFjU2nXw3cts1LZoMZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQJ4wFjU2nXw3cts1LZoMZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQJ4wFjU2nXw3cts1LZoMZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIoMiqXL3nMu6LdBW1fSRpxG",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:08.74Z",
      "updated_at" : "2017-01-27T18:53:08.74Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoMiqXL3nMu6LdBW1fSRpxG"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoMiqXL3nMu6LdBW1fSRpxG/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoMiqXL3nMu6LdBW1fSRpxG/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoMiqXL3nMu6LdBW1fSRpxG/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PI2bWUWpbUP8mm6RRPYodEBc",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:53:08.74Z",
      "updated_at" : "2017-01-27T18:53:08.74Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2bWUWpbUP8mm6RRPYodEBc"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2bWUWpbUP8mm6RRPYodEBc/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2bWUWpbUP8mm6RRPYodEBc/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2bWUWpbUP8mm6RRPYodEBc/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIH5FBrtgZowSzFZ9sw5oxT",
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
      "created_at" : "2017-01-27T18:53:04.04Z",
      "updated_at" : "2017-01-27T18:53:04.04Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIH5FBrtgZowSzFZ9sw5oxT/updates"
        }
      }
    }, {
      "id" : "PIscDJ5CbW94UhauCkWZ737m",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:52:57.96Z",
      "updated_at" : "2017-01-27T18:52:57.96Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDo6U9BcM7amTBPDn42cGPD3",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIp6LKtF1imZBtmKZWFYrk56",
      "fingerprint" : "FPR1682317982",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Laura Serna",
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
      "created_at" : "2017-01-27T18:52:57.57Z",
      "updated_at" : "2017-01-27T18:53:02.17Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDo6U9BcM7amTBPDn42cGPD3",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDo6U9BcM7amTBPDn42cGPD3"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56/updates"
        }
      }
    }, {
      "id" : "PIcyvT6taGGjofzRa9N9MFSe",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:56.28Z",
      "updated_at" : "2017-01-27T18:52:56.28Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcyvT6taGGjofzRa9N9MFSe"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcyvT6taGGjofzRa9N9MFSe/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcyvT6taGGjofzRa9N9MFSe/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcyvT6taGGjofzRa9N9MFSe/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PI35Zao76FL3RnpestCH7yAH",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:56.28Z",
      "updated_at" : "2017-01-27T18:52:56.28Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI35Zao76FL3RnpestCH7yAH"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI35Zao76FL3RnpestCH7yAH/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI35Zao76FL3RnpestCH7yAH/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI35Zao76FL3RnpestCH7yAH/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:56.28Z",
      "updated_at" : "2017-01-27T18:52:56.28Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIcSo1AS5P35ZAJrdq8FNefy",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:52:55.48Z",
      "updated_at" : "2017-01-27T18:52:55.88Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PI6qcpeDc32wQyvTYVQH1q2h",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:49.34Z",
      "updated_at" : "2017-01-27T18:52:49.34Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIoavkt9CDW4PVUQ3bNxx91V",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:49.34Z",
      "updated_at" : "2017-01-27T18:52:49.34Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIwzjKDrmeVyVJ1XAQ9SDMMb",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:49.34Z",
      "updated_at" : "2017-01-27T18:52:49.34Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwzjKDrmeVyVJ1XAQ9SDMMb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwzjKDrmeVyVJ1XAQ9SDMMb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwzjKDrmeVyVJ1XAQ9SDMMb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwzjKDrmeVyVJ1XAQ9SDMMb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "PIwe5qxFxAzCXvQEjKCEbhMN",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:49.34Z",
      "updated_at" : "2017-01-27T18:52:49.34Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwe5qxFxAzCXvQEjKCEbhMN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwe5qxFxAzCXvQEjKCEbhMN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwe5qxFxAzCXvQEjKCEbhMN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwe5qxFxAzCXvQEjKCEbhMN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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

curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$identity = Identity::retrieve('IDkWDHzBfY3NwnyuvkgNWXeZ');
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

identity = Identity.get(id="IDkWDHzBfY3NwnyuvkgNWXeZ")
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
identity = Finix::Identity.retrieve(:id=>"IDkWDHzBfY3NwnyuvkgNWXeZ")
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
  "id" : "STYYBiBaZJqvjKczp5hosUb",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:54:11.18Z",
  "updated_at" : "2017-01-27T18:54:11.25Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 817581,
  "total_fees" : 81758,
  "total_fee" : 81758,
  "net_amount" : 735823,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STYYBiBaZJqvjKczp5hosUb");

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STYYBiBaZJqvjKczp5hosUb');

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STYYBiBaZJqvjKczp5hosUb")

```
> Example Response:

```json
{
  "id" : "STYYBiBaZJqvjKczp5hosUb",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "currency" : "USD",
  "created_at" : "2017-01-27T18:54:11.11Z",
  "updated_at" : "2017-01-27T18:54:12.40Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 817581,
  "total_fees" : 81758,
  "total_fee" : 81758,
  "net_amount" : 735823,
  "destination" : "PIcSo1AS5P35ZAJrdq8FNefy",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=debit"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "STYYBiBaZJqvjKczp5hosUb",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "currency" : "USD",
      "created_at" : "2017-01-27T18:54:11.11Z",
      "updated_at" : "2017-01-27T18:54:12.40Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 817581,
      "total_fees" : 81758,
      "total_fee" : 81758,
      "net_amount" : 735823,
      "destination" : "PIcSo1AS5P35ZAJrdq8FNefy",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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

$settlement = Settlement::retrieve('STYYBiBaZJqvjKczp5hosUb');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STYYBiBaZJqvjKczp5hosUb")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRekyBmbZXPShVwv27kh4tm",
      "amount" : 735823,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "e47844dc-e051-43c6-8232-bc11cdb663fe",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PIcSo1AS5P35ZAJrdq8FNefy",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:12.04Z",
      "updated_at" : "2017-01-27T18:54:12.34Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRekyBmbZXPShVwv27kh4tm"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRekyBmbZXPShVwv27kh4tm/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRekyBmbZXPShVwv27kh4tm/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRekyBmbZXPShVwv27kh4tm/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRekyBmbZXPShVwv27kh4tm/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcSo1AS5P35ZAJrdq8FNefy"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

```
```java

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STYYBiBaZJqvjKczp5hosUb');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"STYYBiBaZJqvjKczp5hosUb")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRsad2i4TWSE5oedwcrkjdNu",
      "amount" : 59026,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "dfbef09b-bb31-4780-9fe8-f12b8520fe63",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PIoavkt9CDW4PVUQ3bNxx91V",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:10.42Z",
      "updated_at" : "2017-01-27T18:54:10.66Z",
      "merchant_identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsad2i4TWSE5oedwcrkjdNu"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsad2i4TWSE5oedwcrkjdNu/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsad2i4TWSE5oedwcrkjdNu/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsad2i4TWSE5oedwcrkjdNu/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsad2i4TWSE5oedwcrkjdNu/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V"
        }
      }
    }, {
      "id" : "TRqRPJwf1bYsEVgK4dHoC2H",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "d3e4ace4-d5d9-4dd3-866b-01805961994c",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PI6qcpeDc32wQyvTYVQH1q2h",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:10.18Z",
      "updated_at" : "2017-01-27T18:54:10.41Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqRPJwf1bYsEVgK4dHoC2H"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqRPJwf1bYsEVgK4dHoC2H/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqRPJwf1bYsEVgK4dHoC2H/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqRPJwf1bYsEVgK4dHoC2H/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqRPJwf1bYsEVgK4dHoC2H/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h"
        }
      }
    }, {
      "id" : "TRwCRgUNbhJkg1JpXPVTTRrN",
      "amount" : 22710,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "a93e6570-9e0e-4dab-abd0-f011db7db547",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PIoavkt9CDW4PVUQ3bNxx91V",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:09.83Z",
      "updated_at" : "2017-01-27T18:54:10.13Z",
      "merchant_identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRwCRgUNbhJkg1JpXPVTTRrN"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRwCRgUNbhJkg1JpXPVTTRrN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDxcRYizGuk3SPJXrHkvvRqF"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRwCRgUNbhJkg1JpXPVTTRrN/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRwCRgUNbhJkg1JpXPVTTRrN/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRwCRgUNbhJkg1JpXPVTTRrN/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoavkt9CDW4PVUQ3bNxx91V"
        }
      }
    }, {
      "id" : "TRr795qeWLH9UYSZ66zavdWS",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "8c2908cf-91be-43bc-a69f-e19ef05600e1",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PI6qcpeDc32wQyvTYVQH1q2h",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:54:09.49Z",
      "updated_at" : "2017-01-27T18:54:09.81Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRr795qeWLH9UYSZ66zavdWS"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRr795qeWLH9UYSZ66zavdWS/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRr795qeWLH9UYSZ66zavdWS/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRr795qeWLH9UYSZ66zavdWS/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRr795qeWLH9UYSZ66zavdWS/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6qcpeDc32wQyvTYVQH1q2h"
        }
      }
    }, {
      "id" : "TReiHyn742MuwZ1VJfbxpHKA",
      "amount" : 227207,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "79fa7024-0374-4090-b7dd-a1cc40bb8315",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIscDJ5CbW94UhauCkWZ737m",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 22721,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:59.05Z",
      "updated_at" : "2017-01-27T18:53:13.44Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        }
      }
    }, {
      "id" : "TRjSYkyvxPNKhgVRC9tXMQcF",
      "amount" : 590374,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "d0ae0384-fab2-4c89-85cb-f3140f218f3f",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : "2017-01-27T18:54:09.41Z",
      "fee" : 59037,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:58.40Z",
      "updated_at" : "2017-01-27T18:53:07.96Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STYYBiBaZJqvjKczp5hosUb/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 6
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

curl https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb


```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRjSYkyvxPNKhgVRC9tXMQcF");

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRjSYkyvxPNKhgVRC9tXMQcF');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TRjSYkyvxPNKhgVRC9tXMQcF")

```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRjSYkyvxPNKhgVRC9tXMQcF")

```
> Example Response:

```json
{
  "id" : "TRjSYkyvxPNKhgVRC9tXMQcF",
  "amount" : 590374,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "d0ae0384-fab2-4c89-85cb-f3140f218f3f",
  "currency" : "USD",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "source" : "PIp6LKtF1imZBtmKZWFYrk56",
  "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
  "ready_to_settle_at" : null,
  "fee" : 59037,
  "statement_descriptor" : "FNX*ACME ANCHORS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:58.40Z",
  "updated_at" : "2017-01-27T18:53:07.96Z",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
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

curl https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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

$debit = Transfer::retrieve('TRjSYkyvxPNKhgVRC9tXMQcF');
$refund = $debit->reverse(11);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TRjSYkyvxPNKhgVRC9tXMQcF")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TRjSYkyvxPNKhgVRC9tXMQcF")

refund = Finix::Transfer.reverse(
          {
          "refund_amount" => 100
        }
        ).save
```
> Example Response:

```json
{
  "id" : "TRuzXYR9Ny4dkSFQ5pe3kqMY",
  "amount" : 357336,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "e77ded05-c995-4812-aac2-842ec63669c2",
  "currency" : "USD",
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
  "destination" : "PIp6LKtF1imZBtmKZWFYrk56",
  "ready_to_settle_at" : null,
  "fee" : 35734,
  "statement_descriptor" : "FNX*ACME ANCHORS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:53:01.37Z",
  "updated_at" : "2017-01-27T18:53:01.45Z",
  "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRuzXYR9Ny4dkSFQ5pe3kqMY"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRuzXYR9Ny4dkSFQ5pe3kqMY/payment_instruments"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "TRpexjDp3rXwmKpq4N3kvZHK",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "190066",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIbMC54VgQ3UEMgNS5FCZbMa",
      "destination" : "PImDZPf7MFrUUmZ5njWqLStG",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:11.52Z",
      "updated_at" : "2017-01-27T18:53:12.57Z",
      "merchant_identity" : "ID2WdZ6gu28sXNMVJdypfqEX",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2WdZ6gu28sXNMVJdypfqEX"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRpexjDp3rXwmKpq4N3kvZHK/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbMC54VgQ3UEMgNS5FCZbMa"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImDZPf7MFrUUmZ5njWqLStG"
        }
      }
    }, {
      "id" : "TRdh2sn5V8TnXJAvQZyMJ9FR",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "87cfead9-a220-405a-ab35-df788bec1029",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:02.56Z",
      "updated_at" : "2017-01-27T18:53:02.69Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRdh2sn5V8TnXJAvQZyMJ9FR/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        }
      }
    }, {
      "id" : "TRuzXYR9Ny4dkSFQ5pe3kqMY",
      "amount" : 357336,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "bfc1f4d5-2df5-40c2-bcf7-b06ec278a167",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "destination" : "PIp6LKtF1imZBtmKZWFYrk56",
      "ready_to_settle_at" : null,
      "fee" : 35734,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:01.26Z",
      "updated_at" : "2017-01-27T18:53:01.45Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuzXYR9Ny4dkSFQ5pe3kqMY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuzXYR9Ny4dkSFQ5pe3kqMY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        }
      }
    }, {
      "id" : "TRchG218pjnTHBF8dkv3YJvM",
      "amount" : 357336,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "e96eab7b-61fd-4250-a2ad-bb78755eef96",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : null,
      "fee" : 35734,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:53:00.64Z",
      "updated_at" : "2017-01-27T18:53:01.33Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRchG218pjnTHBF8dkv3YJvM/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        }
      }
    }, {
      "id" : "TReiHyn742MuwZ1VJfbxpHKA",
      "amount" : 227207,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "79fa7024-0374-4090-b7dd-a1cc40bb8315",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIscDJ5CbW94UhauCkWZ737m",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : null,
      "fee" : 22721,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:59.05Z",
      "updated_at" : "2017-01-27T18:53:13.44Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TReiHyn742MuwZ1VJfbxpHKA/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIscDJ5CbW94UhauCkWZ737m"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
        }
      }
    }, {
      "id" : "TRjSYkyvxPNKhgVRC9tXMQcF",
      "amount" : 590374,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "d0ae0384-fab2-4c89-85cb-f3140f218f3f",
      "currency" : "USD",
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "source" : "PIp6LKtF1imZBtmKZWFYrk56",
      "destination" : "PIwYRKz5HeNKhuyKdG4ay3DD",
      "ready_to_settle_at" : null,
      "fee" : 59037,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:58.40Z",
      "updated_at" : "2017-01-27T18:53:07.96Z",
      "merchant_identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRjSYkyvxPNKhgVRC9tXMQcF/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp6LKtF1imZBtmKZWFYrk56"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwYRKz5HeNKhuyKdG4ay3DD"
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
    "count" : 6
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
```shell
curl https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "US5ds9NWLiEvEcqhYsCGgGa6",
  "password" : "d227131b-cc16-43c1-ac69-c7abc248a6f5",
  "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:50.00Z",
  "updated_at" : "2017-01-27T18:52:50.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US5ds9NWLiEvEcqhYsCGgGa6"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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

```shell
curl https://api-staging.finix.io/identities/IDkWDHzBfY3NwnyuvkgNWXeZ/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "USmyiv7tNfTzyj6iqX99Pu1H",
  "password" : "e65cbeda-602e-417f-be38-d584505a354a",
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:59.53Z",
  "updated_at" : "2017-01-27T18:52:59.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USmyiv7tNfTzyj6iqX99Pu1H"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/users/TRjSYkyvxPNKhgVRC9tXMQcF \
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
user = User.get(id="USjHdX7bDkJbuypYXRnou9Yo")

```
```ruby

```
> Example Response:

```json
{
  "id" : "USjHdX7bDkJbuypYXRnou9Yo",
  "password" : null,
  "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:48.47Z",
  "updated_at" : "2017-01-27T18:52:48.88Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjHdX7bDkJbuypYXRnou9Yo"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
curl https://api-staging.finix.io/users/USmyiv7tNfTzyj6iqX99Pu1H \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "USmyiv7tNfTzyj6iqX99Pu1H",
  "password" : null,
  "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-27T18:52:59.50Z",
  "updated_at" : "2017-01-27T18:52:59.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USmyiv7tNfTzyj6iqX99Pu1H"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "USmyiv7tNfTzyj6iqX99Pu1H",
      "password" : null,
      "identity" : "IDkWDHzBfY3NwnyuvkgNWXeZ",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-01-27T18:52:59.50Z",
      "updated_at" : "2017-01-27T18:53:00.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USmyiv7tNfTzyj6iqX99Pu1H"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "US5ds9NWLiEvEcqhYsCGgGa6",
      "password" : null,
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-27T18:52:49.98Z",
      "updated_at" : "2017-01-27T18:52:49.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US5ds9NWLiEvEcqhYsCGgGa6"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
        }
      }
    }, {
      "id" : "USjHdX7bDkJbuypYXRnou9Yo",
      "password" : null,
      "identity" : "IDxcRYizGuk3SPJXrHkvvRqF",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-27T18:52:48.47Z",
      "updated_at" : "2017-01-27T18:52:48.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USjHdX7bDkJbuypYXRnou9Yo"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb \
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
  "id" : "WHWke3frQU8ii7SSKWfn999",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "created_at" : "2017-01-27T18:52:51.19Z",
  "updated_at" : "2017-01-27T18:52:51.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHWke3frQU8ii7SSKWfn999"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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



curl https://api-staging.finix.io/webhooks/WHWke3frQU8ii7SSKWfn999 \
    -H "Content-Type: application/vnd.json+api" \
    -u USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb


```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHWke3frQU8ii7SSKWfn999");

```
```php
<?php
use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHWke3frQU8ii7SSKWfn999');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WHWke3frQU8ii7SSKWfn999")

```
```ruby
webhook = Finix::Webhook.retrieve(:id=> "WHWke3frQU8ii7SSKWfn999")


```
> Example Response:

```json
{
  "id" : "WHWke3frQU8ii7SSKWfn999",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP7BtUzQvgjfaARjZcREoqh9",
  "created_at" : "2017-01-27T18:52:51.19Z",
  "updated_at" : "2017-01-27T18:52:51.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHWke3frQU8ii7SSKWfn999"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
    -u  USjHdX7bDkJbuypYXRnou9Yo:ef77a904-9caf-47e9-a27e-df9a9bc199bb

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
      "id" : "WHWke3frQU8ii7SSKWfn999",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "AP7BtUzQvgjfaARjZcREoqh9",
      "created_at" : "2017-01-27T18:52:51.19Z",
      "updated_at" : "2017-01-27T18:52:51.19Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHWke3frQU8ii7SSKWfn999"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP7BtUzQvgjfaARjZcREoqh9"
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
