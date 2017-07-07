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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

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

import io.finix.payments.ApiClient;
import io.finix.payments.views.*;
import io.finix.payments.forms.*;

//...

public static void main(String[] args) {

  ApiClient api = ApiClient.builder()
                  .url("https://api-staging.finix.io")
                  .user("USvcFQjk8nYtixh3REG9Httu")
                  .password("6587d480-073a-4dd9-86f1-591ae8924a02")
                  .build();
//...



```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');

Finix\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USvcFQjk8nYtixh3REG9Httu',
	"password" => '6587d480-073a-4dd9-86f1-591ae8924a02']
	);

require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USvcFQjk8nYtixh3REG9Httu", "6587d480-073a-4dd9-86f1-591ae8924a02"))

```
```ruby
# To download the Ruby gem:
# gem install finix

require 'finix'

Finix.configure(
    :root_url => 'https://api-staging.finix.io',
    :user=>'USvcFQjk8nYtixh3REG9Httu',
    :password => '6587d480-073a-4dd9-86f1-591ae8924a02'
)
```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USvcFQjk8nYtixh3REG9Httu`

- Password: `6587d480-073a-4dd9-86f1-591ae8924a02`

- Application ID: `AP4pi6CF3PS3eES7zpw6TxKb`

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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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
import io.finix.payments.ApiClient;
import io.finix.payments.enums.BusinessType;
import io.finix.payments.forms.Address;
import io.finix.payments.forms.Date;
import io.finix.payments.forms.IdentityEntityForm;
import io.finix.payments.forms.IdentityForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Identity;


IdentityForm form = IdentityForm.builder()
  .entity(IdentityEntityForm.builder()
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
  .personalAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .businessAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .dob(Date.builder().day(Integer.valueOf(27)).month(Integer.valueOf(5)).year(Integer.valueOf(1978)).build())
  .maxTransactionAmount(Long.valueOf(1000L))
  .mcc("7399").url("http://sample-entity.com")
  .annualCardVolume(Long.valueOf(100L))
  .defaultStatementDescriptor("Business Inc")
  .incorporationDate(Date.builder().day(Integer.valueOf(1)).month(Integer.valueOf(12)).year(Integer.valueOf(2012)).build())
  .principalPercentageOwnership(Integer.valueOf(51)).build()).build();

Maybe<Identity> response = api.identities.post(form);
if(! response.succeeded().booleanValue()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}
    Identity identity = (Identity)response.view();
    identity.getId();

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
  "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
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
  "created_at" : "2017-07-06T05:18:33.33Z",
  "updated_at" : "2017-07-06T05:18:33.33Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}'


```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.enums.BankAccountType;
import io.finix.payments.forms.BankAccountForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.BankAccount;
import io.finix.payments.views.Identity;
import java.util.Currency;

BankAccountForm form = BankAccountForm.builder()
        .name("Joe Doe")
        .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
        .accountNumber("84012312415")
        .bankCode("840123124")
        .accountType(BankAccountType.SAVINGS)
        .companyName("company name")
        .country("USA")
        .currency(Currency.getInstance("USD"))
        .build();

Maybe<BankAccount> request = api.instruments.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create bank account");
}
BankAccount bankAccount = request.view();

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\BankAccount;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
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
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
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
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
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
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save
```
> Example Response:

```json
{
  "id" : "PImyPYpY3eZ4m8C4ejLemqs9",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-07-06T05:18:36.93Z",
  "updated_at" : "2017-07-06T05:18:36.93Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "verification" : "VIceuSG3a4UpfRcurdxP8YUD",
  "merchant_profile" : "MPrUQXj4izWybTdxxsWLmH8B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-07-06T05:18:37.88Z",
  "updated_at" : "2017-07-06T05:18:37.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrUQXj4izWybTdxxsWLmH8B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIceuSG3a4UpfRcurdxP8YUD"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
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
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.forms.Date;


IdentityForm form = IdentityForm.builder()
    .entity(
    IdentityEntityForm.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
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
        .build())
    .build();

Maybe<Identity> response = api.identities.post(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}

Identity identity = response.view();

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
	        "first_name"=> "Laura", 
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
	        "first_name": "Laura", 
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
	        "first_name"=> "Laura", 
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
  "id" : "IDc4aXrHuVxefQwz3xbeeHpe",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
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
  "created_at" : "2017-07-06T05:18:38.74Z",
  "updated_at" : "2017-07-06T05:18:38.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "name": "Joe Le", 
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
	    "identity": "IDc4aXrHuVxefQwz3xbeeHpe"
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
        if (! response.succeeded()) {
            ApiError error = response .error();
            System.out.println(error.getCode());
            throw new RuntimeException("API error attempting to create Payment Card");
        }
PaymentCard card = response.view();

```
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
$card = new PaymentCard(
	array(
	    "name"=> "Joe Le", 
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
	    "identity"=> "IDc4aXrHuVxefQwz3xbeeHpe"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Le", 
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
	    "identity": "IDc4aXrHuVxefQwz3xbeeHpe"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Joe Le", 
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
	    "identity"=> "IDc4aXrHuVxefQwz3xbeeHpe"
	}).save
```
> Example Response:

```json
{
  "id" : "PI3koNPTGqRjLrsakKERqdmA",
  "fingerprint" : "FPR-955625032",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Le",
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
  "created_at" : "2017-07-06T05:18:39.21Z",
  "updated_at" : "2017-07-06T05:18:39.21Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDc4aXrHuVxefQwz3xbeeHpe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/updates"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "merchant_identity": "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

AuthorizationCreateForm formCreateAuthorization = AuthorizationCreateForm.builder()
                .amount(10000L)
                .merchantIdentity("ID5Ebo6ErBV71hpkDgHzhGVS")
                .source("PI3koNPTGqRjLrsakKERqdmA")
                .build();

Maybe<Authorization> response = api.authorizations.post(formCreateAuthorization);

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getMessage());
  throw new RuntimeException("API error attempting to creating Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3koNPTGqRjLrsakKERqdmA", 
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
	    "merchant_identity": "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:44.03Z",
  "updated_at" : "2017-07-06T05:18:44.12Z",
  "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : false,
  "expires_at" : "2017-07-13T05:18:44.03Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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
curl https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

AuthorizationUpdateForm form = AuthorizationUpdateForm.builder()
        .captureAmount(100L)
        .fee(10L)
        .statementDescriptor("Order 123")
        .build();

Maybe<Authorization> response = api.authorizations.id("AUogt3PgskE2ahBFmTpn2EGJ").put(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getMessage());
    throw new RuntimeException("API error attempting to capture authorization");
}
Authorization capturedAuthorization = response.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUogt3PgskE2ahBFmTpn2EGJ');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUogt3PgskE2ahBFmTpn2EGJ")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUogt3PgskE2ahBFmTpn2EGJ")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxuza9aGaxBEPnWTsJTXjQ9",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:43.96Z",
  "updated_at" : "2017-07-06T05:18:44.66Z",
  "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : false,
  "expires_at" : "2017-07-13T05:18:43.96Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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
curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.SettlementForm;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.*;
import java.util.Currency;


Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

SettlementForm formSettlement = SettlementForm.builder()
        .currency(Currency.getInstance("USD"))
        .build();

Transfer transfer = api.transfers.id("AUogt3PgskE2ahBFmTpn2EGJ").get().view();

Maybe<Settlement> response = api.identities.id("ID5Ebo6ErBV71hpkDgHzhGVS").settlements.post(formSettlement);

if (! response.succeeded()) {
    throw new RuntimeException("API error attempting to create batch settlement");
}

Settlement settlementBatch = response.view();

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
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

identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")
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
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")
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
  "id" : "ST6qzrxSqbLnUKpS2EZiLUu",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "currency" : "USD",
  "created_at" : "2017-07-06T05:32:14.70Z",
  "updated_at" : "2017-07-06T05:32:14.73Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 721549,
  "total_fees" : 72156,
  "total_fee" : 72156,
  "net_amount" : 649393,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=debit"
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
The `total_amount` minus the `total_fee` equals the `net_amount` (the amount in cents
that will be deposited into your merchant's bank account).

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
    -u USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Daphne", 
	        "last_name": "Chang", 
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
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.forms.Date;


IdentityForm form = IdentityForm.builder()
    .entity(
    IdentityEntityForm.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
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
        .build())
    .build();

Maybe<Identity> response = api.identities.post(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}

Identity identity = response.view();
```
```php
<?php
use Finix\Resources\Identity;

$identity = new Identity(IDgBubuAG69dusHgB6JMMX8p);
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
	        "first_name": "Daphne", 
	        "last_name": "Chang", 
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
	        "first_name"=> "Daphne", 
	        "last_name"=> "Chang", 
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
  "id" : "IDgBubuAG69dusHgB6JMMX8p",
  "entity" : {
    "title" : null,
    "first_name" : "Daphne",
    "last_name" : "Chang",
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
  "created_at" : "2017-07-06T05:32:25.84Z",
  "updated_at" : "2017-07-06T05:32:25.84Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
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
    -u USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "name": "Collen Curry", 
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
	    "identity": "IDgBubuAG69dusHgB6JMMX8p"
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
if (! response.succeeded()) {
    ApiError error = response .error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard card = response.view();

```
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('IDgBubuAG69dusHgB6JMMX8p');
$card = new PaymentCard(
	array(
	    "name"=> "Collen Curry", 
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
	    "identity"=> "IDgBubuAG69dusHgB6JMMX8p"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Le", 
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
	    "identity": "IDc4aXrHuVxefQwz3xbeeHpe"
	}).save()

```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Collen Curry", 
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
	    "identity"=> "IDgBubuAG69dusHgB6JMMX8p"
	}).save
```
> Example Response:

```json
{
  "id" : "PIfUSipeoSdppGB3qBLv8EVr",
  "fingerprint" : "FPR2085799720",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Collen Curry",
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
  "created_at" : "2017-07-06T05:32:26.24Z",
  "updated_at" : "2017-07-06T05:32:26.24Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDgBubuAG69dusHgB6JMMX8p",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr/updates"
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

### Step 3: Verify card is eligible to receive push-to-card disbursements

Now that we've associated a payment instrument to a recipient, we'll need to verify whether or not the card is eligible to receive push-to-card disbursements. How? By making a request to the `Verifications` endpoint. The returned `Verification` resource returns a set of general attributes and details about the card in question (e.g. card type, issuer information). For example, the `inquiry_details` object will contain a `push_funds_block_indicator` attribute that indicates if it is eligible for push-to-card disbursements. Below you'll see a number of fields and the potential responses.

```shell
curl https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "processor": "VISA_V1"
	}'

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;


 VerificationForm verificationForm = VerificationForm.builder()
    .processor("VISA_V1")
    .build();

Maybe<Verification> verificationResponse = api.instruments.id("PIfUSipeoSdppGB3qBLv8EVr").verifications.post(verificationForm);
if (! verificationResponse.succeeded()) {
    ApiError error = verificationResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create a Verification");
}
Verification verification = verificationResponse.view();

```
```php
<?php

```
```python


from finix.resources import PaymentInstrument
from finix.resources import Verification


payment_card = PaymentInstrument.get(id="PI3koNPTGqRjLrsakKERqdmA")

verify = payment_card.verify_on(Verification(**
	{
	    "processor": "VISA_V1"
	}))

```
```ruby

```
> Example Response:

```json
{
  "id" : "VI5DhWvuqz7gABvcma431Pbr",
  "tags" : { },
  "messages" : [ ],
  "raw" : {
    "validation_details" : {
      "systems_trace_audit_number" : "191677",
      "transaction_identifier" : "1234",
      "action_code" : "N7",
      "response_code" : "5",
      "address_verification_results" : "N",
      "cvv2_result_code" : "N"
    },
    "inquiry_details" : {
      "systems_trace_audit_number" : "191677",
      "card_type_code" : "C",
      "billing_currency_code" : 986,
      "billing_currency_minor_digits" : 2,
      "issuer_name" : "Visa Test Bank",
      "card_issuer_country_code" : 76,
      "fast_funds_indicator" : "N",
      "push_funds_block_indicator" : "N",
      "online_gambing_block_indicator" : "Y"
    },
    "general_inquiry_details" : {
      "systems_trace_audit_number" : "191677",
      "status" : {
        "status_code" : "CDI000",
        "status_description" : "Success"
      }
    }
  },
  "processor" : "VISA_V1",
  "state" : "SUCCEEDED",
  "created_at" : "2017-07-06T05:32:30.26Z",
  "updated_at" : "2017-07-06T05:32:31.32Z",
  "trace_id" : "191677",
  "payment_instrument" : "PIfUSipeoSdppGB3qBLv8EVr",
  "merchant" : null,
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI5DhWvuqz7gABvcma431Pbr"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | The name of the processor, which needs to be: `VISA_V1`

#### Address Verification Results (address_verification_results)
Letter | Description
------ | -------------------------------------------------------------------
D, F, M | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Verification 2 Results (cvv2_result_code)
Letter | Description
------ | -------------------------------------------------------------------
M | CVV  verified
N, P, S | CVV not verified
U | Issuer does not participate in CVV2 service

#### Card Type (card_type_code)

This one-character code indicates whether the account is credit, debit, prepaid, deferred debit, or charge.

Letter | Description
------ | -------------------------------------------------------------------
C | Credit  
D | Debit  
H | Charge Card    
P | Prepaid  
R | Deferred Debit  

#### Fasts Funds Indicator (fast_funds_indicator)

Indicates whether or not the card is Fast Funds eligible (i.e. if the funds will settle in 30 mins or less). If not eligible, typically funds will settle within 2 days.

Letter | Description
------ | -------------------------------------------------------------------
B, D | Fast Funds eligible
N | Not eligible for Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

This code indicates if the associated card can receive push-to-card disbursements.

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push-to-card payments
N | Does not accept push-to-card payments

#### Online Gambling Block Indicator (online_gambing_block_indicator)

Indicates if the card can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y | Blocked for online gambling payouts
N | Not blocked for online gambling payouts

#### Card Product ID (card_product_id)

A combination of card brand, platform, class and scheme.

Letter | Description
------ | -------------------------------------------------------------------
A | Visa Traditional
AX | American Express
B | Visa Traditional Rewards
C | Visa Signature
D | Visa Signature Preferred
DI | Discover
DN | Diners
E | Proprietary ATM
F | Visa Classic
G | Visa Business
G1 | Visa Signature Business
G2 | Visa Business Check Card
G3 | Visa Business Enhanced
G4 | Visa Infinite Business
G5 | Visa Business Rewards
I | Visa Infinite
I1 | Visa Infinite Privilege
I2 | Visa UHNW
J3 | Visa Healthcare
JC | JCB
K | Visa Corporate T&E
K1 | Visa Government Corporate T&E
L | Visa Electron
M | MasterCard
N | Visa Platinum
N1 | Visa Rewards
N2 | Visa Select
P | Visa Gold
Q | Private Label
Q1 | Private Label Prepaid
Q2 | Private Label Basic
Q3 | Private Label Standard
Q4 | Private Label Enhanced
Q5 | Private Label Specialized
Q6 | Private Label Premium
R | Proprietary
S | Visa Purchasing
S1 | Visa Purchasing with Fleet
S2 | Visa Government Purchasing
S3 | Visa Government Purchasing with Fleet
S4 | Visa Commercial Agriculture
S5 | Visa Commercial Transport
S6 | Visa Commercial Marketplace
U | Visa Travel Money
V | Visa V PAY

#### Product Sub-Type (card_product_subtype)

Description of product subtype.

Letter | Description
------ | -------------------------------------------------------------------
AC | Agriculture Maintenance Account
AE | Agriculture Debit Account/Electron
AG | Agriculture
AI | Agriculture Investment Loan
CG | Brazil Cargo
CS | Construction
DS | Distribution
HC | Healthcare
LP | Visa Large Purchase Advantage
MA | Visa Mobile Agent
MB | Interoperable Mobile Branchless Banking
MG | Visa Mobile General
VA | Visa Vale - Supermarket
VF | Visa Vale - Fuel
VR | Visa Vale - Restaurant

#### Card Sub-Type (card_subtype_code)

The code for account funding source subtype, such as reloadable and non-reloadable.

Letter | Description
------ | -------------------------------------------------------------------
N | Non-Reloadable
R | Reloadable

### Step 4: Provision Recipient Account

```shell
curl https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDgBubuAG69dusHgB6JMMX8p").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> merchantResponse = api.identities.id(identity.id).merchants.post(form);

if (! merchantResponse.succeeded()) {
            ApiError error = merchantResponse.error();
            System.out.println(error.getCode());
            throw new RuntimeException("API error attempting to provision Merchant");
        }
Merchant merchant = merchantResponse.view();
```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('IDgBubuAG69dusHgB6JMMX8p');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="PIfUSipeoSdppGB3qBLv8EVr")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id=>"IDgBubuAG69dusHgB6JMMX8p")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MU8nGPUtta7zgrJdGfLwyQPG",
  "identity" : "IDgBubuAG69dusHgB6JMMX8p",
  "verification" : "VIaEg7LSY2u79gayuEGrWcfL",
  "merchant_profile" : "MPcR8X8tMUVv15vnReupsAwt",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-07-06T05:32:26.65Z",
  "updated_at" : "2017-07-06T05:32:26.65Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU8nGPUtta7zgrJdGfLwyQPG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU8nGPUtta7zgrJdGfLwyQPG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPcR8X8tMUVv15vnReupsAwt"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIaEg7LSY2u79gayuEGrWcfL"
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


### Step 5: Send Payout

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIfUSipeoSdppGB3qBLv8EVr", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .amount(100L)
        .currency(Currency.getInstance("USD"))
        .idempotencyId("Idsfk23jnasdfkjf")
        .destination("PIfUSipeoSdppGB3qBLv8EVr")
        .tags(ImmutableMap.of("order_number", "21DFASJSAKAS"))
.build();

Maybe<Transfer> response = api.transfers.post(form);
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Transfer");
}
Transfer transfer = response.view();
```
```php
<?php
use Finix\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PIfUSipeoSdppGB3qBLv8EVr", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$transfer = $transfer->save();
```
```python


from finix.resources import Transfer

payout = Transfer(**
	{
	    "name": "Collen Curry", 
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
	    "identity": "IDgBubuAG69dusHgB6JMMX8p"
	}).save()

```
```ruby
transfer = Finix::Transfer.new(
	{
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PIfUSipeoSdppGB3qBLv8EVr", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "TRxxnkai4979bFtwvhUTMJHE",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "191676",
  "currency" : "USD",
  "application" : "AP7VLVh3dm3yoz156UqWDm8U",
  "source" : "PIjVciYinDXZPaLxk6KPx5iH",
  "destination" : "PIfUSipeoSdppGB3qBLv8EVr",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:32:27.74Z",
  "updated_at" : "2017-07-06T05:32:29.29Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDgBubuAG69dusHgB6JMMX8p",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRxxnkai4979bFtwvhUTMJHE"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRxxnkai4979bFtwvhUTMJHE/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDgBubuAG69dusHgB6JMMX8p"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRxxnkai4979bFtwvhUTMJHE/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRxxnkai4979bFtwvhUTMJHE/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRxxnkai4979bFtwvhUTMJHE/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIjVciYinDXZPaLxk6KPx5iH"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr"
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
          applicationId: 'AP4pi6CF3PS3eES7zpw6TxKb',
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
  "id" : "TKxg7igRL3iHeXrUk947UqbR",
  "fingerprint" : "FPR405642276",
  "created_at" : "2017-07-06T05:18:45.68Z",
  "updated_at" : "2017-07-06T05:18:45.68Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-07-07T05:18:45.68Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKxg7igRL3iHeXrUk947UqbR")
    .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save
```
> Example Response:

```json
{
  "id" : "PIxg7igRL3iHeXrUk947UqbR",
  "fingerprint" : "FPR405642276",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-07-06T05:18:46.10Z",
  "updated_at" : "2017-07-06T05:18:46.10Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/updates"
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
    secureForm.submit('/applications/AP4pi6CF3PS3eES7zpw6TxKb/tokens', {
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
  "id" : "TKxg7igRL3iHeXrUk947UqbR",
  "fingerprint" : "FPR405642276",
  "created_at" : "2017-07-06T05:18:45.68Z",
  "updated_at" : "2017-07-06T05:18:45.68Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-07-07T05:18:45.68Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}'

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKxg7igRL3iHeXrUk947UqbR")
    .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save()

```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save
```
> Example Response:

```json
{
  "id" : "PIxg7igRL3iHeXrUk947UqbR",
  "fingerprint" : "FPR405642276",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-07-06T05:18:46.10Z",
  "updated_at" : "2017-07-06T05:18:46.10Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/updates"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "merchant_identity": "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

AuthorizationCreateForm formCreateAuthorization = AuthorizationCreateForm.builder()
                .amount(10000L)
                .merchantIdentity("ID5Ebo6ErBV71hpkDgHzhGVS")
                .source("PI3koNPTGqRjLrsakKERqdmA")
                .build();

Maybe<Authorization> response = api.authorizations.post(formCreateAuthorization);

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getMessage());
  throw new RuntimeException("API error attempting to creating Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3koNPTGqRjLrsakKERqdmA", 
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
	    "merchant_identity": "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Finix::Authorization.new(
	{
	    "merchant_identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PI3koNPTGqRjLrsakKERqdmA", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:44.03Z",
  "updated_at" : "2017-07-06T05:18:44.12Z",
  "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : false,
  "expires_at" : "2017-07-13T05:18:44.03Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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
curl https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

AuthorizationUpdateForm form = AuthorizationUpdateForm.builder()
        .captureAmount(100L)
        .fee(10L)
        .statementDescriptor("Order 123")
        .build();

Maybe<Authorization> responseAuthorization = api.authorizations.id("AUogt3PgskE2ahBFmTpn2EGJ").put(form);

if (! responseAuthorization.succeeded()) {
    ApiError error = responseAuthorization.error();
    System.out.println(error.getMessage());
    throw new RuntimeException("API error attempting to capture authorization");
}
Authorization capturedAuth = responseAuthorization.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUogt3PgskE2ahBFmTpn2EGJ');
$authorization = $authorization->capture(50, 10);

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUogt3PgskE2ahBFmTpn2EGJ")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUogt3PgskE2ahBFmTpn2EGJ")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxuza9aGaxBEPnWTsJTXjQ9",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:43.96Z",
  "updated_at" : "2017-07-06T05:18:44.66Z",
  "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : false,
  "expires_at" : "2017-07-13T05:18:43.96Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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

curl https://api-staging.finix.io/authorizations/AU3Ai99bJYUJr4GptzsP7Di7 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.AuthorizationUpdateForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.*;

AuthorizationUpdateForm formVoid = AuthorizationUpdateForm.builder()
        .voidMe(true)
        .build();

Maybe<Authorization> response = api.authorizations.id("AUogt3PgskE2ahBFmTpn2EGJ").put(formVoid);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to void authorization");
}
Authorization voidAuthorization = response.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUogt3PgskE2ahBFmTpn2EGJ');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUogt3PgskE2ahBFmTpn2EGJ")
authorization.void()

```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUogt3PgskE2ahBFmTpn2EGJ")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AU3Ai99bJYUJr4GptzsP7Di7",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:46.59Z",
  "updated_at" : "2017-07-06T05:18:47.13Z",
  "trace_id" : "c77c42ef-3106-4220-b120-7c2f8c324a9d",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : true,
  "expires_at" : "2017-07-13T05:18:46.59Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU3Ai99bJYUJr4GptzsP7Di7"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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

## Fetch an Authorization

```shell

curl https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.ApiClient;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Authorization;

Maybe <Authorization> response =  api.authorizations
    .id("AUogt3PgskE2ahBFmTpn2EGJ")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    throw new RuntimeException("API error in attempting to fetch Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUogt3PgskE2ahBFmTpn2EGJ');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUogt3PgskE2ahBFmTpn2EGJ")
```
```ruby
authorization = Finix::Authorization.retrieve(:id=>"AUogt3PgskE2ahBFmTpn2EGJ")


```
> Example Response:

```json
{
  "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxuza9aGaxBEPnWTsJTXjQ9",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:43.96Z",
  "updated_at" : "2017-07-06T05:18:44.66Z",
  "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "is_void" : false,
  "expires_at" : "2017-07-13T05:18:43.96Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.*;

Maybe<Page<Authorization>> response = api.authorizations.get();

if (! response.succeeded()) {
   ApiError error = response.error();
   System.out.println(error.getCode());
   System.out.println(error.getMessage());
   System.out.println(error.getDetails());
   throw new RuntimeException("API error attempting to list all Authorizations");
}

 Page<Authorization> page = response.view();
 Page<Authorization> page2 = page.getNext();

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
      "id" : "AU3Ai99bJYUJr4GptzsP7Di7",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:46.59Z",
      "updated_at" : "2017-07-06T05:18:47.13Z",
      "trace_id" : "c77c42ef-3106-4220-b120-7c2f8c324a9d",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "is_void" : true,
      "expires_at" : "2017-07-13T05:18:46.59Z",
      "idempotency_id" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU3Ai99bJYUJr4GptzsP7Di7"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        }
      }
    }, {
      "id" : "AUogt3PgskE2ahBFmTpn2EGJ",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRxuza9aGaxBEPnWTsJTXjQ9",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:43.96Z",
      "updated_at" : "2017-07-06T05:18:44.66Z",
      "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "is_void" : false,
      "expires_at" : "2017-07-13T05:18:43.96Z",
      "idempotency_id" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUogt3PgskE2ahBFmTpn2EGJ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
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
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.forms.Date;


IdentityForm form = IdentityForm.builder()
    .entity(
    IdentityEntityForm.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
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
        .build())
    .build();

Maybe<Identity> response = api.identities.post(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}

Identity identity = response.view();
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
	        "first_name"=> "Laura", 
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
	        "first_name": "Laura", 
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
	        "first_name"=> "Laura", 
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
  "id" : "IDc4aXrHuVxefQwz3xbeeHpe",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
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
  "created_at" : "2017-07-06T05:18:38.74Z",
  "updated_at" : "2017-07-06T05:18:38.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a `business_type` field should not be passed. Passing a `business_type` indicates that the Identity should be treated as a merchant.

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

## Create an Identity for a Merchant
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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
import io.finix.payments.ApiClient;
import io.finix.payments.enums.BusinessType;
import io.finix.payments.forms.Address;
import io.finix.payments.forms.Date;
import io.finix.payments.forms.IdentityEntityForm;
import io.finix.payments.forms.IdentityForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Identity;


IdentityForm form = IdentityForm.builder()
  .entity(IdentityEntityForm.builder()
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
  .personalAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .businessAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .dob(Date.builder().day(Integer.valueOf(27)).month(Integer.valueOf(5)).year(Integer.valueOf(1978)).build())
  .maxTransactionAmount(Long.valueOf(1000L))
  .mcc("7399").url("http://sample-entity.com")
  .annualCardVolume(Long.valueOf(100L))
  .defaultStatementDescriptor("Business Inc")
  .incorporationDate(Date.builder().day(Integer.valueOf(1)).month(Integer.valueOf(12)).year(Integer.valueOf(2012)).build())
  .principalPercentageOwnership(Integer.valueOf(51)).build()).build();

Maybe<Identity> response = api.identities.post(form);
if(! response.succeeded().booleanValue()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}
    Identity identity = (Identity)response.view();
    

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
  "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
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
  "created_at" : "2017-07-06T05:18:33.33Z",
  "updated_at" : "2017-07-06T05:18:33.33Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    }
  }
}
```
Create an `Identity` resource with the merchant's underwriting information.

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

## Fetch a Identity

```shell

curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("ID5Ebo6ErBV71hpkDgHzhGVS").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

```
```php
<?php
use Finix\Resources\Identity;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
```
```python


from finix.resources import Identity
identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")

```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")


```
> Example Response:

```json
{
  "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
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
  "created_at" : "2017-07-06T05:18:33.31Z",
  "updated_at" : "2017-07-06T05:18:33.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02


```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;

Maybe<Page<Identity>> response = api.identities.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Identities");
}

Page<Identity> page = response.view();

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
      "id" : "IDc4aXrHuVxefQwz3xbeeHpe",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
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
      "created_at" : "2017-07-06T05:18:38.73Z",
      "updated_at" : "2017-07-06T05:18:38.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDp5YB3BGv93PqrsHUqjrzat",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-07-06T05:18:36.50Z",
      "updated_at" : "2017-07-06T05:18:36.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDfiXfe2bi3UjaS7gjY8uheu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-07-06T05:18:36.08Z",
      "updated_at" : "2017-07-06T05:18:36.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID7cggLgcHovUoqq2bWENMZo",
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
      "created_at" : "2017-07-06T05:18:35.63Z",
      "updated_at" : "2017-07-06T05:18:35.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID3LmcyrgandVUzBQRhCS15o",
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
      "created_at" : "2017-07-06T05:18:35.15Z",
      "updated_at" : "2017-07-06T05:18:35.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDrng8ahCGREL6crHQSpnGQb",
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
      "created_at" : "2017-07-06T05:18:34.73Z",
      "updated_at" : "2017-07-06T05:18:34.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID77mCzusQVpFBUo9bR5QLaN",
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
      "created_at" : "2017-07-06T05:18:34.27Z",
      "updated_at" : "2017-07-06T05:18:34.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID9uCQbeV8ZMEnR8VNyBjqYu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
      "created_at" : "2017-07-06T05:18:33.78Z",
      "updated_at" : "2017-07-06T05:18:33.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
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
      "created_at" : "2017-07-06T05:18:33.31Z",
      "updated_at" : "2017-07-06T05:18:33.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDeaonR2ZnzvUDspyDVTgPDP",
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
      "created_at" : "2017-07-06T05:18:30.18Z",
      "updated_at" : "2017-07-06T05:18:30.19Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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


## Update an Identity
```shell
curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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
	        "doing_business_as": "Bobs Burgers", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Bobs Burgers", 
	        "url": "www.BobsBurgers.com", 
	        "business_name": "Bobs Burgers", 
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
import io.finix.payments.ApiClient;
import io.finix.payments.enums.BusinessType;
import io.finix.payments.forms.*;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Identity;

IdentityForm form = IdentityForm.builder()
                .entity(
                  IdentityEntityForm.builder()
                      .firstName("dwayne")
                      .email("self@newdomain.com")
                      .businessPhone("+1 (408) 756-4497")
                      .build())
                .build();

Maybe<Identity> response = api.identities.id("ID5Ebo6ErBV71hpkDgHzhGVS").put(form);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to update identity");
}

Identity updatedIdentity = response.view();

```
```php
<?php

```
```python



```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Kline",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Bobs Burgers",
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
    "key" : "value_2"
  },
  "created_at" : "2017-07-06T05:18:33.31Z",
  "updated_at" : "2017-07-06T05:18:55.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
## Provision a Merchant

```shell

curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDgBubuAG69dusHgB6JMMX8p").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> merchantResponse = api.identities.id(identity.id).merchants.post(form);

if (! merchantResponse.succeeded()) {
            ApiError error = merchantResponse.error();
            System.out.println(error.getCode());
            throw new RuntimeException("API error attempting to provision Merchant");
        }
Merchant merchant = merchantResponse.view();
```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")

merchant = identity.provision_merchant
```

> Example Response:

```json
{
  "id" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "verification" : "VIceuSG3a4UpfRcurdxP8YUD",
  "merchant_profile" : "MPrUQXj4izWybTdxxsWLmH8B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-07-06T05:18:37.88Z",
  "updated_at" : "2017-07-06T05:18:37.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrUQXj4izWybTdxxsWLmH8B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIceuSG3a4UpfRcurdxP8YUD"
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
curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```java
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.*;
import io.finix.payments.forms.*;

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .processor(null)
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> underwriteMerchant = api.identities.id("ID5Ebo6ErBV71hpkDgHzhGVS").merchants.post(form);

if(! underwriteMerchant.succeeded()){
   System.out.println(underwriteMerchant.error());
}

Merchant provisionMerchant = underwriteMerchant.view();

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Merchant;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Finix::Identity.retrieve(:id => "MUk4ByEEmSgKwJwMLWH9dRPx")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "verification" : "VIceuSG3a4UpfRcurdxP8YUD",
  "merchant_profile" : "MPrUQXj4izWybTdxxsWLmH8B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-07-06T05:18:37.88Z",
  "updated_at" : "2017-07-06T05:18:37.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrUQXj4izWybTdxxsWLmH8B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIceuSG3a4UpfRcurdxP8YUD"
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

## Fetch a Merchant

```shell
curl https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Merchant;

Maybe<Merchant> response = api.merchants
    .id(merchant.id)
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Merchant");
}

Merchant merchantView = response.view();

```
```php
<?php
use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MUk4ByEEmSgKwJwMLWH9dRPx');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MUk4ByEEmSgKwJwMLWH9dRPx")

```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUk4ByEEmSgKwJwMLWH9dRPx")

```
> Example Response:

```json
{
  "id" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "verification" : null,
  "merchant_profile" : "MPiyCemrhTcQQ7q9MYJ3j9NG",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-07-06T05:18:37.85Z",
  "updated_at" : "2017-07-06T05:18:38.00Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPiyCemrhTcQQ7q9MYJ3j9NG"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
curl https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUk4ByEEmSgKwJwMLWH9dRPx");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUk4ByEEmSgKwJwMLWH9dRPx');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUk4ByEEmSgKwJwMLWH9dRPx")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIhMDvy7cqmCFUfrCZFbf2wv",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-07-06T05:18:56.24Z",
  "updated_at" : "2017-07-06T05:18:56.26Z",
  "trace_id" : "6092036a-6357-4e04-ae59-ef3b1bd7a789",
  "payment_instrument" : null,
  "merchant" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIhMDvy7cqmCFUfrCZFbf2wv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
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
curl https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '{}'

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUk4ByEEmSgKwJwMLWH9dRPx');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUk4ByEEmSgKwJwMLWH9dRPx")

verification = merchant.entity["default_statement_descriptor"] = "Prestige World Wide"

```
> Example Response:

```json
{
  "id" : "VIhMDvy7cqmCFUfrCZFbf2wv",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-07-06T05:18:56.24Z",
  "updated_at" : "2017-07-06T05:18:56.26Z",
  "trace_id" : "6092036a-6357-4e04-ae59-ef3b1bd7a789",
  "payment_instrument" : null,
  "merchant" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIhMDvy7cqmCFUfrCZFbf2wv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.Merchant;

Maybe<Page<Merchant>> response = api.merchants.get();

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getCode());
  System.out.println(error.getMessage());
  System.out.println(error.getDetails());
  throw new RuntimeException("API error attempting to list all Merchants");
}

Page<Merchant> page = response.view();

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
      "id" : "MUk4ByEEmSgKwJwMLWH9dRPx",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "verification" : null,
      "merchant_profile" : "MPiyCemrhTcQQ7q9MYJ3j9NG",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-07-06T05:18:37.85Z",
      "updated_at" : "2017-07-06T05:18:38.00Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPiyCemrhTcQQ7q9MYJ3j9NG"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
curl https://api-staging.finix.io/merchants/MUk4ByEEmSgKwJwMLWH9dRPx/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java

```
```php
<?php
use Finix\Resources\Merchant;
use Finix\Resources\Verification;

$merchant = Merchant::retrieve('MUk4ByEEmSgKwJwMLWH9dRPx');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
```ruby
merchant = Finix::Merchant.retrieve(:id => "MUk4ByEEmSgKwJwMLWH9dRPx")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDc4aXrHuVxefQwz3xbeeHpe",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
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
      "created_at" : "2017-07-06T05:18:38.73Z",
      "updated_at" : "2017-07-06T05:18:38.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDp5YB3BGv93PqrsHUqjrzat",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-07-06T05:18:36.50Z",
      "updated_at" : "2017-07-06T05:18:36.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDp5YB3BGv93PqrsHUqjrzat/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDfiXfe2bi3UjaS7gjY8uheu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-07-06T05:18:36.08Z",
      "updated_at" : "2017-07-06T05:18:36.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfiXfe2bi3UjaS7gjY8uheu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID7cggLgcHovUoqq2bWENMZo",
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
      "created_at" : "2017-07-06T05:18:35.63Z",
      "updated_at" : "2017-07-06T05:18:35.63Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7cggLgcHovUoqq2bWENMZo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID3LmcyrgandVUzBQRhCS15o",
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
      "created_at" : "2017-07-06T05:18:35.15Z",
      "updated_at" : "2017-07-06T05:18:35.15Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3LmcyrgandVUzBQRhCS15o/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDrng8ahCGREL6crHQSpnGQb",
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
      "created_at" : "2017-07-06T05:18:34.73Z",
      "updated_at" : "2017-07-06T05:18:34.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrng8ahCGREL6crHQSpnGQb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID77mCzusQVpFBUo9bR5QLaN",
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
      "created_at" : "2017-07-06T05:18:34.27Z",
      "updated_at" : "2017-07-06T05:18:34.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID77mCzusQVpFBUo9bR5QLaN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID9uCQbeV8ZMEnR8VNyBjqYu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
      "created_at" : "2017-07-06T05:18:33.78Z",
      "updated_at" : "2017-07-06T05:18:33.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9uCQbeV8ZMEnR8VNyBjqYu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "ID5Ebo6ErBV71hpkDgHzhGVS",
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
      "created_at" : "2017-07-06T05:18:33.31Z",
      "updated_at" : "2017-07-06T05:18:33.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "IDeaonR2ZnzvUDspyDVTgPDP",
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
      "created_at" : "2017-07-06T05:18:30.18Z",
      "updated_at" : "2017-07-06T05:18:30.19Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "name": "Joe Le", 
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
	    "identity": "IDc4aXrHuVxefQwz3xbeeHpe"
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.forms.Address;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
        if (! response.succeeded()) {
            ApiError error = response .error();
            System.out.println(error.getCode());
            throw new RuntimeException("API error attempting to create Payment Card");
        }
PaymentCard card = response.view();

```
```php
<?php
use Finix\Resources\PaymentCard;
use Finix\Resources\Identity;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
$card = new PaymentCard(
	array(
	    "name"=> "Joe Le", 
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
	    "identity"=> "IDc4aXrHuVxefQwz3xbeeHpe"
	));
$card = $identity->createPaymentCard($card);

```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Joe Le", 
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
	    "identity": "IDc4aXrHuVxefQwz3xbeeHpe"
	}).save()
```
```ruby
card = Finix::PaymentCard.new(
	{
	    "name"=> "Joe Le", 
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
	    "identity"=> "IDc4aXrHuVxefQwz3xbeeHpe"
	}).save
```
> Example Response:

```json
{
  "id" : "PI3koNPTGqRjLrsakKERqdmA",
  "fingerprint" : "FPR-955625032",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Le",
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
  "created_at" : "2017-07-06T05:18:39.21Z",
  "updated_at" : "2017-07-06T05:18:39.21Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDc4aXrHuVxefQwz3xbeeHpe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/updates"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}'


```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.enums.BankAccountType;
import io.finix.payments.forms.BankAccountForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.BankAccount;
import io.finix.payments.views.Identity;
import java.util.Currency;

BankAccountForm form = BankAccountForm.builder()
        .name("Joe Doe")
        .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
        .accountNumber("84012312415")
        .bankCode("840123124")
        .accountType(BankAccountType.SAVINGS)
        .companyName("company name")
        .country("USA")
        .currency(Currency.getInstance("USD"))
        .build();

Maybe<BankAccount> request = api.instruments.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create bank account");
}
BankAccount bankAccount = request.view();

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\BankAccount;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
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
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
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
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
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
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save
```
> Example Response:

```json
{
  "id" : "PImyPYpY3eZ4m8C4ejLemqs9",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-07-06T05:18:36.93Z",
  "updated_at" : "2017-07-06T05:18:36.93Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}'


```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKxg7igRL3iHeXrUk947UqbR")
    .identity("ID5Ebo6ErBV71hpkDgHzhGVS")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	));
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKxg7igRL3iHeXrUk947UqbR", 
	    "type": "TOKEN", 
	    "identity": "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save()
```
```ruby
card = Finix::PaymentInstrument.new(
	{
	    "token"=> "TKxg7igRL3iHeXrUk947UqbR", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID5Ebo6ErBV71hpkDgHzhGVS"
	}).save
```
> Example Response:

```json
{
  "id" : "PIxg7igRL3iHeXrUk947UqbR",
  "fingerprint" : "FPR405642276",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-07-06T05:18:46.10Z",
  "updated_at" : "2017-07-06T05:18:46.10Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/updates"
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
curl https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.views.Instrument;
import io.finix.payments.interfaces.Maybe;

Maybe<Instrument> response = api.paymentInstruments
    .id("PImyPYpY3eZ4m8C4ejLemqs9")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Bank Account");
}

Instrument bankAccountView = response.view();

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PImyPYpY3eZ4m8C4ejLemqs9');

```
```python



```
```ruby
bank_account = Finix::BankAccount.retrieve(:id=> "PImyPYpY3eZ4m8C4ejLemqs9")

```
> Example Response:

```json
{
  "id" : "PImyPYpY3eZ4m8C4ejLemqs9",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-07-06T05:18:36.91Z",
  "updated_at" : "2017-07-06T05:18:37.39Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
curl https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;

Maybe<PaymentCard> response = api.instruments
  .id("PI3koNPTGqRjLrsakKERqdmA")
  .get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Payment Card");
}
PaymentCard card = response.view();

```
```php
<?php
use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI3koNPTGqRjLrsakKERqdmA');

```
```python



```
```ruby
card = Finix::PaymentCard.retrieve(:id=> "PI3koNPTGqRjLrsakKERqdmA")


```
> Example Response:

```json
{
  "id" : "PI3koNPTGqRjLrsakKERqdmA",
  "fingerprint" : "FPR-955625032",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Joe Le",
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
  "created_at" : "2017-07-06T05:18:39.18Z",
  "updated_at" : "2017-07-06T05:18:44.05Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDc4aXrHuVxefQwz3xbeeHpe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/updates"
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
curl https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "merchant": "MUk4ByEEmSgKwJwMLWH9dRPx"
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
  "id" : "IUhs6HWUjUUyfge2WpccFxLB",
  "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
  "merchant" : "MUk4ByEEmSgKwJwMLWH9dRPx",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-07-06T05:18:47.64Z",
  "updated_at" : "2017-07-06T05:18:47.66Z",
  "payment_instrument" : "PI3koNPTGqRjLrsakKERqdmA",
  "trace_id" : "fd99008d-702d-412f-bfd7-ea854db6b9f6",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/updates/IUhs6HWUjUUyfge2WpccFxLB"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02
```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.Instrument;

Maybe<Page<Instrument>> response = api.instruments.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Payment Instruments");
}

Page<Instrument> page = response.view();

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
      "id" : "PIxg7igRL3iHeXrUk947UqbR",
      "fingerprint" : "FPR405642276",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
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
      "created_at" : "2017-07-06T05:18:46.05Z",
      "updated_at" : "2017-07-06T05:18:46.05Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxg7igRL3iHeXrUk947UqbR/updates"
        }
      }
    }, {
      "id" : "PIciCQVaejDSQen4gfVFZmDu",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-07-06T05:18:39.62Z",
      "updated_at" : "2017-07-06T05:18:39.62Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDc4aXrHuVxefQwz3xbeeHpe",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PI3koNPTGqRjLrsakKERqdmA",
      "fingerprint" : "FPR-955625032",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Joe Le",
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
      "created_at" : "2017-07-06T05:18:39.18Z",
      "updated_at" : "2017-07-06T05:18:44.05Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDc4aXrHuVxefQwz3xbeeHpe",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDc4aXrHuVxefQwz3xbeeHpe"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/updates"
        }
      }
    }, {
      "id" : "PIaTm4nGBpyinkmq5dyA2oA2",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:37.85Z",
      "updated_at" : "2017-07-06T05:18:37.85Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaTm4nGBpyinkmq5dyA2oA2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaTm4nGBpyinkmq5dyA2oA2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaTm4nGBpyinkmq5dyA2oA2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaTm4nGBpyinkmq5dyA2oA2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PI5ws5iMZ6bVTa63pcNREcHR",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:37.85Z",
      "updated_at" : "2017-07-06T05:18:37.85Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5ws5iMZ6bVTa63pcNREcHR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5ws5iMZ6bVTa63pcNREcHR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5ws5iMZ6bVTa63pcNREcHR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5ws5iMZ6bVTa63pcNREcHR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PIrbMrwkyMvofyPasPXjUbMA",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:37.85Z",
      "updated_at" : "2017-07-06T05:18:37.85Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PImyPYpY3eZ4m8C4ejLemqs9",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-07-06T05:18:36.91Z",
      "updated_at" : "2017-07-06T05:18:37.39Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PIgEUxW3hdJUNaqZkouXB1XE",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:31.09Z",
      "updated_at" : "2017-07-06T05:18:31.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PIfRRsUbnDAGTVucidfQTVev",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:31.09Z",
      "updated_at" : "2017-07-06T05:18:31.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeaonR2ZnzvUDspyDVTgPDP",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PIkR5dey86VQuNwo4tDQa44h",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:31.09Z",
      "updated_at" : "2017-07-06T05:18:31.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeaonR2ZnzvUDspyDVTgPDP",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkR5dey86VQuNwo4tDQa44h"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkR5dey86VQuNwo4tDQa44h/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkR5dey86VQuNwo4tDQa44h/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkR5dey86VQuNwo4tDQa44h/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        }
      }
    }, {
      "id" : "PIr96efDhgAGbBimC2hYKdAu",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-07-06T05:18:31.09Z",
      "updated_at" : "2017-07-06T05:18:31.09Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeaonR2ZnzvUDspyDVTgPDP",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr96efDhgAGbBimC2hYKdAu"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr96efDhgAGbBimC2hYKdAu/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr96efDhgAGbBimC2hYKdAu/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIr96efDhgAGbBimC2hYKdAu/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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

## Payment Instrument Verification

```shell
curl https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "processor": "VISA_V1"
	}'

```
```java
import io.finix.payments.forms.*;
import io.finix.payments.views.*;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;


 VerificationForm verificationForm = VerificationForm.builder()
    .processor("VISA_V1")
    .build();

Maybe<Verification> verificationResponse = api.instruments.id("PIfUSipeoSdppGB3qBLv8EVr").verifications.post(verificationForm);
if (! verificationResponse.succeeded()) {
    ApiError error = verificationResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create a Verification");
}
Verification verification = verificationResponse.view();

```
```php
<?php

```
```python


from finix.resources import PaymentInstrument
from finix.resources import Verification


payment_card = PaymentInstrument.get(id="PI3koNPTGqRjLrsakKERqdmA")

verify = payment_card.verify_on(Verification(**
	{
	    "processor": "VISA_V1"
	}))

```
```ruby

```
> Example Response:

```json
{
  "id" : "VI5DhWvuqz7gABvcma431Pbr",
  "tags" : { },
  "messages" : [ ],
  "raw" : {
    "validation_details" : {
      "systems_trace_audit_number" : "191677",
      "transaction_identifier" : "1234",
      "action_code" : "N7",
      "response_code" : "5",
      "address_verification_results" : "N",
      "cvv2_result_code" : "N"
    },
    "inquiry_details" : {
      "systems_trace_audit_number" : "191677",
      "card_type_code" : "C",
      "billing_currency_code" : 986,
      "billing_currency_minor_digits" : 2,
      "issuer_name" : "Visa Test Bank",
      "card_issuer_country_code" : 76,
      "fast_funds_indicator" : "N",
      "push_funds_block_indicator" : "N",
      "online_gambing_block_indicator" : "Y"
    },
    "general_inquiry_details" : {
      "systems_trace_audit_number" : "191677",
      "status" : {
        "status_code" : "CDI000",
        "status_description" : "Success"
      }
    }
  },
  "processor" : "VISA_V1",
  "state" : "SUCCEEDED",
  "created_at" : "2017-07-06T05:32:30.26Z",
  "updated_at" : "2017-07-06T05:32:31.32Z",
  "trace_id" : "191677",
  "payment_instrument" : "PIfUSipeoSdppGB3qBLv8EVr",
  "merchant" : null,
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI5DhWvuqz7gABvcma431Pbr"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP7VLVh3dm3yoz156UqWDm8U"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfUSipeoSdppGB3qBLv8EVr"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | The name of the processor, which needs to be: `VISA_V1`

#### Address Verification Results (address_verification_results)
Letter | Description
------ | -------------------------------------------------------------------
D, F, M | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Verification 2 Results (cvv2_result_code)
Letter | Description
------ | -------------------------------------------------------------------
M | CVV  verified
N, P, S | CVV not verified
U | Issuer does not participate in CVV2 service

#### Card Type (card_type_code)

This one-character code indicates whether the account is credit, debit, prepaid, deferred debit, or charge.

Letter | Description
------ | -------------------------------------------------------------------
C | Credit  
D | Debit  
H | Charge Card    
P | Prepaid  
R | Deferred Debit  

#### Fasts Funds Indicator (fast_funds_indicator)

Indicates whether or not the card is Fast Funds eligible (i.e. if the funds will settle in 30 mins or less). If not eligible, typically funds will settle within 2 days.

Letter | Description
------ | -------------------------------------------------------------------
B, D | Fast Funds eligible
N | Not eligible for Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

This code indicates if the associated card can receive push-to-card disbursements.

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push-to-card payments
N | Does not accept push-to-card payments

#### Online Gambling Block Indicator (online_gambing_block_indicator)

Indicates if the card can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y | Blocked for online gambling payouts
N | Not blocked for online gambling payouts

#### Card Product ID (card_product_id)

A combination of card brand, platform, class and scheme.

Letter | Description
------ | -------------------------------------------------------------------
A | Visa Traditional
AX | American Express
B | Visa Traditional Rewards
C | Visa Signature
D | Visa Signature Preferred
DI | Discover
DN | Diners
E | Proprietary ATM
F | Visa Classic
G | Visa Business
G1 | Visa Signature Business
G2 | Visa Business Check Card
G3 | Visa Business Enhanced
G4 | Visa Infinite Business
G5 | Visa Business Rewards
I | Visa Infinite
I1 | Visa Infinite Privilege
I2 | Visa UHNW
J3 | Visa Healthcare
JC | JCB
K | Visa Corporate T&E
K1 | Visa Government Corporate T&E
L | Visa Electron
M | MasterCard
N | Visa Platinum
N1 | Visa Rewards
N2 | Visa Select
P | Visa Gold
Q | Private Label
Q1 | Private Label Prepaid
Q2 | Private Label Basic
Q3 | Private Label Standard
Q4 | Private Label Enhanced
Q5 | Private Label Specialized
Q6 | Private Label Premium
R | Proprietary
S | Visa Purchasing
S1 | Visa Purchasing with Fleet
S2 | Visa Government Purchasing
S3 | Visa Government Purchasing with Fleet
S4 | Visa Commercial Agriculture
S5 | Visa Commercial Transport
S6 | Visa Commercial Marketplace
U | Visa Travel Money
V | Visa V PAY

#### Product Sub-Type (card_product_subtype)

Description of product subtype.

Letter | Description
------ | -------------------------------------------------------------------
AC | Agriculture Maintenance Account
AE | Agriculture Debit Account/Electron
AG | Agriculture
AI | Agriculture Investment Loan
CG | Brazil Cargo
CS | Construction
DS | Distribution
HC | Healthcare
LP | Visa Large Purchase Advantage
MA | Visa Mobile Agent
MB | Interoperable Mobile Branchless Banking
MG | Visa Mobile General
VA | Visa Vale - Supermarket
VF | Visa Vale - Fuel
VR | Visa Vale - Restaurant

#### Card Sub-Type (card_subtype_code)

The code for account funding source subtype, such as reloadable and non-reloadable.

Letter | Description
------ | -------------------------------------------------------------------
N | Non-Reloadable
R | Reloadable

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Batch Settlement

```shell

curl https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.SettlementForm;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.*;
import java.util.Currency;


Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

SettlementForm formSettlement = SettlementForm.builder()
        .currency(Currency.getInstance("USD"))
        .build();

Transfer transfer = api.transfers.id("AUogt3PgskE2ahBFmTpn2EGJ").get().view();

Maybe<Settlement> response = api.identities.id("ID5Ebo6ErBV71hpkDgHzhGVS").settlements.post(formSettlement);

if (! response.succeeded()) {
    throw new RuntimeException("API error attempting to create batch settlement");
}

Settlement settlementBatch = response.view();

```
```php
<?php
use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('ID5Ebo6ErBV71hpkDgHzhGVS');
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

identity = Identity.get(id="ID5Ebo6ErBV71hpkDgHzhGVS")
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
identity = Finix::Identity.retrieve(:id=>"ID5Ebo6ErBV71hpkDgHzhGVS")
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
  "id" : "ST6qzrxSqbLnUKpS2EZiLUu",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "currency" : "USD",
  "created_at" : "2017-07-06T05:32:14.70Z",
  "updated_at" : "2017-07-06T05:32:14.73Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 721549,
  "total_fees" : 72156,
  "total_fee" : 72156,
  "net_amount" : 649393,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=debit"
    }
  }
}
```
Each settlement is comprised of all the `Transfers` that have a SUCCEEDED state and
that have not been previously settled out. In other words, if a merchant has a
`Transfer` in the PENDING state it will not be included in the batch settlement.
In addition, `Settlements` will include any refunded Transfers as a deduction.
The `total_amount` minus the `total_fee` equals the `net_amount` (the amount in cents
that will be deposited into your merchant's bank account).

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

## Fetch a Settlement

```shell


curl https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Settlement;

Maybe<Settlement> response = api.settlements
  .id("ST6qzrxSqbLnUKpS2EZiLUu")
  .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch settlement");
}

Settlement settlementView = response.view();

```
```php
<?php
use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('ST6qzrxSqbLnUKpS2EZiLUu');

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"ST6qzrxSqbLnUKpS2EZiLUu")

```
> Example Response:

```json
{
  "id" : "ST6qzrxSqbLnUKpS2EZiLUu",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "currency" : "USD",
  "created_at" : "2017-07-06T05:32:14.66Z",
  "updated_at" : "2017-07-06T05:32:15.75Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 721549,
  "total_fees" : 72156,
  "total_fee" : 72156,
  "net_amount" : 649393,
  "destination" : "PImyPYpY3eZ4m8C4ejLemqs9",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=debit"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.Settlement;

Maybe<Page<Settlement>> request = api.settlements.get();

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Settlements");
}

Page<Settlement> page = request.view();

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
      "id" : "ST6qzrxSqbLnUKpS2EZiLUu",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "currency" : "USD",
      "created_at" : "2017-07-06T05:32:14.66Z",
      "updated_at" : "2017-07-06T05:32:15.75Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 721549,
      "total_fees" : 72156,
      "total_fee" : 72156,
      "net_amount" : 649393,
      "destination" : "PImyPYpY3eZ4m8C4ejLemqs9",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
Settlement settlement = client.settlementsClient().fetch("ST6qzrxSqbLnUKpS2EZiLUu");
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

$settlement = Settlement::retrieve('ST6qzrxSqbLnUKpS2EZiLUu');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"ST6qzrxSqbLnUKpS2EZiLUu")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRuuY1qECRvzmCer7D9MDuvz",
      "amount" : 649393,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "a01071f6-e1f9-4d1b-b5e0-4f2420a470d2",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PImyPYpY3eZ4m8C4ejLemqs9",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:15.38Z",
      "updated_at" : "2017-07-06T05:32:15.68Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuuY1qECRvzmCer7D9MDuvz"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuuY1qECRvzmCer7D9MDuvz/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRuuY1qECRvzmCer7D9MDuvz/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRuuY1qECRvzmCer7D9MDuvz/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRuuY1qECRvzmCer7D9MDuvz/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImyPYpY3eZ4m8C4ejLemqs9"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
Settlement settlement = client.settlementsClient().fetch("ST6qzrxSqbLnUKpS2EZiLUu");
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

$settlement = Settlement::retrieve('ST6qzrxSqbLnUKpS2EZiLUu');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Finix::Settlement.retrieve(:id=>"ST6qzrxSqbLnUKpS2EZiLUu")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRgYc4JjkWoctfZqiWg4rDPT",
      "amount" : 44641,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "f5e4ece9-1d3a-417b-8f3f-c3b035d89841",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PIfRRsUbnDAGTVucidfQTVev",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:13.59Z",
      "updated_at" : "2017-07-06T05:32:13.97Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDeaonR2ZnzvUDspyDVTgPDP",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRgYc4JjkWoctfZqiWg4rDPT"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRgYc4JjkWoctfZqiWg4rDPT/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRgYc4JjkWoctfZqiWg4rDPT/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRgYc4JjkWoctfZqiWg4rDPT/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRgYc4JjkWoctfZqiWg4rDPT/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev"
        }
      }
    }, {
      "id" : "TR3SZ1huALtE5z47HEFYNdJG",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "d3e1fe31-e25f-4972-bc54-93fb40ee7d68",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PIgEUxW3hdJUNaqZkouXB1XE",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:13.20Z",
      "updated_at" : "2017-07-06T05:32:13.56Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SZ1huALtE5z47HEFYNdJG"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SZ1huALtE5z47HEFYNdJG/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SZ1huALtE5z47HEFYNdJG/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SZ1huALtE5z47HEFYNdJG/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR3SZ1huALtE5z47HEFYNdJG/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE"
        }
      }
    }, {
      "id" : "TRo9ZycdL55WizJWhn1y6Tc",
      "amount" : 27482,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "a28cf1d9-874a-4908-ac55-4272d631e13d",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PIfRRsUbnDAGTVucidfQTVev",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:12.75Z",
      "updated_at" : "2017-07-06T05:32:13.12Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDeaonR2ZnzvUDspyDVTgPDP",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRo9ZycdL55WizJWhn1y6Tc"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRo9ZycdL55WizJWhn1y6Tc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeaonR2ZnzvUDspyDVTgPDP"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRo9ZycdL55WizJWhn1y6Tc/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRo9ZycdL55WizJWhn1y6Tc/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRo9ZycdL55WizJWhn1y6Tc/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfRRsUbnDAGTVucidfQTVev"
        }
      }
    }, {
      "id" : "TRqQGFdbtNHr5ELJfLszHyB3",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "2bec2b30-900a-4169-92c7-c84dc2e8eab0",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PIgEUxW3hdJUNaqZkouXB1XE",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:12.36Z",
      "updated_at" : "2017-07-06T05:32:12.72Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqQGFdbtNHr5ELJfLszHyB3"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqQGFdbtNHr5ELJfLszHyB3/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqQGFdbtNHr5ELJfLszHyB3/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqQGFdbtNHr5ELJfLszHyB3/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqQGFdbtNHr5ELJfLszHyB3/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE"
        }
      }
    }, {
      "id" : "TRdExapWFV6QiFseEJDUeZc6",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "acde2c9d-20b2-4e26-8fcd-cb8d1d163117",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PIgEUxW3hdJUNaqZkouXB1XE",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:11.71Z",
      "updated_at" : "2017-07-06T05:32:12.28Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRdExapWFV6QiFseEJDUeZc6"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRdExapWFV6QiFseEJDUeZc6/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRdExapWFV6QiFseEJDUeZc6/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRdExapWFV6QiFseEJDUeZc6/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRdExapWFV6QiFseEJDUeZc6/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgEUxW3hdJUNaqZkouXB1XE"
        }
      }
    }, {
      "id" : "TRxuza9aGaxBEPnWTsJTXjQ9",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 10,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:44.54Z",
      "updated_at" : "2017-07-06T05:19:13.88Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    }, {
      "id" : "TRi3naf49mYGLug9AFap1a8F",
      "amount" : 446519,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "16224230-f866-4b0c-a802-faae42c22493",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIciCQVaejDSQen4gfVFZmDu",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 44652,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:40.72Z",
      "updated_at" : "2017-07-06T05:19:23.05Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    }, {
      "id" : "TR5ESiT8FjcDWbaNFYkBTxih",
      "amount" : 274930,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "66abac44-a16d-4e29-bdfa-79b1b46d64ce",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : "2017-07-06T05:32:11.58Z",
      "fee" : 27493,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:40.07Z",
      "updated_at" : "2017-07-06T05:19:17.19Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/ST6qzrxSqbLnUKpS2EZiLUu/transfers?offset=0&limit=20&sort=created_at,desc"
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
## Fetch a Transfer

```shell

curl https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02


```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Transfer;

Maybe<Transfer> response = api.transfers
    .id("TR5ESiT8FjcDWbaNFYkBTxih")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Transfer");
}

Transfer transferView = response.view();

```
```php
<?php
use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TR5ESiT8FjcDWbaNFYkBTxih');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TR5ESiT8FjcDWbaNFYkBTxih")

```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TR5ESiT8FjcDWbaNFYkBTxih")

```
> Example Response:

```json
{
  "id" : "TR5ESiT8FjcDWbaNFYkBTxih",
  "amount" : 274930,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "66abac44-a16d-4e29-bdfa-79b1b46d64ce",
  "currency" : "USD",
  "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
  "source" : "PI3koNPTGqRjLrsakKERqdmA",
  "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
  "ready_to_settle_at" : null,
  "fee" : 27493,
  "statement_descriptor" : "FIN*BOBS BURGERS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:40.07Z",
  "updated_at" : "2017-07-06T05:18:40.25Z",
  "idempotency_id" : null,
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
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

curl https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
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

$debit = Transfer::retrieve('TR5ESiT8FjcDWbaNFYkBTxih');
$refund = $debit->reverse(11);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TR5ESiT8FjcDWbaNFYkBTxih")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```ruby
transfer = Finix::Transfer.retrieve(:id=> "TR5ESiT8FjcDWbaNFYkBTxih")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TRd2HgNzn577vXDLcfW1DBq4",
  "amount" : 96017,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "616ad7be-8272-41e0-b9b7-71e524fa65e7",
  "currency" : "USD",
  "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
  "source" : "PIrbMrwkyMvofyPasPXjUbMA",
  "destination" : "PI3koNPTGqRjLrsakKERqdmA",
  "ready_to_settle_at" : null,
  "fee" : 9602,
  "statement_descriptor" : "FIN*BOBS BURGERS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:18:43.30Z",
  "updated_at" : "2017-07-06T05:18:43.37Z",
  "idempotency_id" : null,
  "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRd2HgNzn577vXDLcfW1DBq4"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRd2HgNzn577vXDLcfW1DBq4/payment_instruments"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.Transfer;

Maybe<Page<Transfer>> request = api.transfers.get();

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Transfers");
}

Page<Transfer> page = request.view();

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
      "id" : "TRxuza9aGaxBEPnWTsJTXjQ9",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "78654fd0-cf8c-485b-a540-19b7ac72b372",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:44.54Z",
      "updated_at" : "2017-07-06T05:18:44.66Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRxuza9aGaxBEPnWTsJTXjQ9/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    }, {
      "id" : "TRd2HgNzn577vXDLcfW1DBq4",
      "amount" : 96017,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "a54440ae-42f9-4456-a0f1-5087ee016226",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIrbMrwkyMvofyPasPXjUbMA",
      "destination" : "PI3koNPTGqRjLrsakKERqdmA",
      "ready_to_settle_at" : null,
      "fee" : 9602,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:43.13Z",
      "updated_at" : "2017-07-06T05:18:43.37Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRd2HgNzn577vXDLcfW1DBq4"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRd2HgNzn577vXDLcfW1DBq4/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        }
      }
    }, {
      "id" : "TR3ux7WUW9DnFXJmw176KcU4",
      "amount" : 96017,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "b66b4723-c635-44c9-917e-8dce0f04d977",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : null,
      "fee" : 9602,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:42.63Z",
      "updated_at" : "2017-07-06T05:18:43.24Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR3ux7WUW9DnFXJmw176KcU4/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    }, {
      "id" : "TRi3naf49mYGLug9AFap1a8F",
      "amount" : 446519,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "16224230-f866-4b0c-a802-faae42c22493",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PIciCQVaejDSQen4gfVFZmDu",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : null,
      "fee" : 44652,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:40.72Z",
      "updated_at" : "2017-07-06T05:18:40.85Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRi3naf49mYGLug9AFap1a8F/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIciCQVaejDSQen4gfVFZmDu"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
        }
      }
    }, {
      "id" : "TR5ESiT8FjcDWbaNFYkBTxih",
      "amount" : 274930,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "66abac44-a16d-4e29-bdfa-79b1b46d64ce",
      "currency" : "USD",
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "source" : "PI3koNPTGqRjLrsakKERqdmA",
      "destination" : "PIrbMrwkyMvofyPasPXjUbMA",
      "ready_to_settle_at" : null,
      "fee" : 27493,
      "statement_descriptor" : "FIN*BOBS BURGERS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:18:40.07Z",
      "updated_at" : "2017-07-06T05:18:40.25Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID5Ebo6ErBV71hpkDgHzhGVS",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID5Ebo6ErBV71hpkDgHzhGVS"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5ESiT8FjcDWbaNFYkBTxih/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3koNPTGqRjLrsakKERqdmA"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrbMrwkyMvofyPasPXjUbMA"
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
    -u USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.forms.WebhookForm;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Webhook;

WebhookForm form = WebhookForm.builder()
    .url("http://requestb.in/1jb5zu11")
    .build();

Maybe<Webhook> request = api.webhooks.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create Webhook");
}
Webhook webhookView = request.view();

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
  "id" : "WH7hVFyUEQrZ3XyuPcLaFEA6",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
  "created_at" : "2017-07-06T05:18:32.95Z",
  "updated_at" : "2017-07-06T05:18:32.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH7hVFyUEQrZ3XyuPcLaFEA6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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


## Fetch a Webhook

```shell



curl https://api-staging.finix.io/webhooks/WH7hVFyUEQrZ3XyuPcLaFEA6 \
    -H "Content-Type: application/vnd.json+api" \
    -u USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02


```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.views.Webhook;

Maybe<Webhook> response = api.webhooks
        .id("WH7hVFyUEQrZ3XyuPcLaFEA6")
        .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Webhook");
}
Webhook webhookView = response.view();

```
```php
<?php
use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WH7hVFyUEQrZ3XyuPcLaFEA6');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WH7hVFyUEQrZ3XyuPcLaFEA6")

```
```ruby
webhook = Finix::Webhook.retrieve(:id=> "WH7hVFyUEQrZ3XyuPcLaFEA6")


```
> Example Response:

```json
{
  "id" : "WH7hVFyUEQrZ3XyuPcLaFEA6",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
  "created_at" : "2017-07-06T05:18:32.95Z",
  "updated_at" : "2017-07-06T05:18:32.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH7hVFyUEQrZ3XyuPcLaFEA6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
    -u  USvcFQjk8nYtixh3REG9Httu:6587d480-073a-4dd9-86f1-591ae8924a02

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.Webhook;

Maybe<Page<Webhook>> response = api.webhooks.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Webhooks");
}

Page<Webhook> page = response.view();

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
      "id" : "WH7hVFyUEQrZ3XyuPcLaFEA6",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "AP4pi6CF3PS3eES7zpw6TxKb",
      "created_at" : "2017-07-06T05:18:32.95Z",
      "updated_at" : "2017-07-06T05:18:32.95Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WH7hVFyUEQrZ3XyuPcLaFEA6"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP4pi6CF3PS3eES7zpw6TxKb"
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
# FAQs

Below are GIFs of some of the common actions that you will be performing when using the dashboard.

## Sign Up
If you haven't signed up yet, please create a user account.
![sign up gif] (https://finix-payments.github.io/customer-logos/assets/sign_up.gif)

## Create Production Account
Once you've played with a sandbox account, you're ready to create a production `Application.`
![create production account] (https://finix-payments.github.io/customer-logos/assets/create_production_account.gif)

## Create an Identity for a Merchant
Simply select `Identity` on the sidebar, click "Create new identity", and fill out the form with the `Merchant's` underwriting information.
![Create an Identity for a Merchant]
(https://finix-payments.github.io/customer-logos/assets/create_identity_merchant.gif)

## View KYC Identity Verification
You are able to view important KYC information for `Merchants` by first selecting `Merchants`, then clicking your desired `Merchant`. This will take you the summary view of the `Merchant` you selected. Now just click the Processor tab and scroll down to the Verification container.
![view kyc identity verification]     (https://finix-payments.github.io/customer-logos/assets/view_kyc_identity_verification.gif)

## Approve Merchant
Want to approve a `Merchant`? Under review queues in the sidebar, you'll see `Merchants`- a list of all pending `Merchants` under your `Application`. You have the ability to approve one by one, or approve an entire page.
![approve merchant] (https://finix-payments.github.io/customer-logos/assets/approve_merchant.gif)

## Enable or Disable Processing Functionality
Enable or disable `Merchant's` ability to create new `Transfers` and `Authorizations` by navigating to Merchants on the sidebar. Then select your desired `Merchant` and click the `Processors` tab. Finally, click the edit button and configure a `Merchant's` processing ability to your liking.
![enable processing merchant]
(https://finix-payments.github.io/customer-logos/assets/enable_processing_merchant.gif)

## Enable or Disable Settlement Functionality
Disable or disable `Merchant's` ability to create new `Settlements`by navigating to Merchants on the sidebar. Then select your desired `Merchant` and click the `Processors` tab. Finally, click the edit button and configure a `Merchant's` settlement ability to your liking.
![enable processing settlements] (https://finix-payments.github.io/customer-logos/assets/enable_processing_settlements.gif)

## Edit Fees & Interchange Plus
Want to edit an `Application's` fixed fee, basis points, ACH fee, or toggle interchange plus? First, click `Application` on the sidebar and then click the Processors tab. Once you pick which processor you want to configure, you'll be presented with a modal allowing you edit fees and interchange plus.  
![edit fees] (https://finix-payments.github.io/customer-logos/assets/edit_fees.gif)

## Enable CVV & AVS
Finix offers you the ability to configure Address Verification System (AVS) and CVV rules as part of our fraud risk system, to help you ensure that transactions are being made by only authorized users. How? Simply click `Application` on the sidebar, then click the Processors tab. Select the desired processor, and then click edit on the Security configuration.
![enable cvv and avs] (https://finix-payments.github.io/customer-logos/assets/enable_cvv_avs.gif)

## Approve a Settlement
Want to approve a `Settlement`? Under review queues in the sidebar, you'll see `Settlements`- a list of all pending `Settlements` under your `Application`. You have the ability to approve one by one, or approve an entire page.
![approve settlement] (https://finix-payments.github.io/customer-logos/assets/settlement_aprove.gif)

## Upload Dispute Evidence
Have evidence for your dispute? Click Disputes, select the desired dispute, then scroll down to the Evidence container, and click Upload File.
![upload dispute evidence] (https://finix-payments.github.io/customer-logos/assets/upload_dispute_evidence.gif)

