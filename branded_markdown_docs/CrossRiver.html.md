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

4. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.crossriver.payments.processing.client</groupId>
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

import io.crossriver.payments.processing.client.ProcessingClient;
import io.crossriver.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("https://api-staging.finix.io");
  client.setupUserIdAndPassword("USbBaUzyrgmSyFeRipRUZG1F", "aec11417-7423-4e34-a6d1-a09c8b76509e");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USbBaUzyrgmSyFeRipRUZG1F',
	"password" => 'aec11417-7423-4e34-a6d1-a09c8b76509e']
	);

require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USbBaUzyrgmSyFeRipRUZG1F", "aec11417-7423-4e34-a6d1-a09c8b76509e"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USbBaUzyrgmSyFeRipRUZG1F`

- Password: `aec11417-7423-4e34-a6d1-a09c8b76509e`

- Application ID: `APo33Betu7pEGtdw63VA8tFV`

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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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

import io.crossriver.payments.processing.client.model.Address;
import io.crossriver.payments.processing.client.model.BankAccountType;
import io.crossriver.payments.processing.client.model.BusinessType;
import io.crossriver.payments.processing.client.model.Date;
import io.crossriver.payments.processing.client.model.Entity;
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
use CrossRiver\Resources\Identity;

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


from crossriver.resources import Identity

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
> Example Response:

```json
{
  "id" : "IDsQsVMwtkQzGRzBRhRZq25u",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:16.68Z",
  "updated_at" : "2017-01-27T18:52:16.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}'


```
```java

import io.crossriver.payments.processing.client.model.BankAccount;
import io.crossriver.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "IDsQsVMwtkQzGRzBRhRZq25u"
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
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\BankAccount;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
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
	    "identity"=> "IDsQsVMwtkQzGRzBRhRZq25u"
	));
$bank_account = $identity->createBankAccount($bank_account);
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
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI76MpurcgyKzQMixwVDXVTP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:21.34Z",
  "updated_at" : "2017-01-27T18:52:21.34Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
curl https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDsQsVMwtkQzGRzBRhRZq25u")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "verification" : "VIzbNTXHbAtRY9EmcaQWDWB",
  "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:22.18Z",
  "updated_at" : "2017-01-27T18:52:22.18Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIzbNTXHbAtRY9EmcaQWDWB"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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

import io.crossriver.payments.processing.client.model.Identity;

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
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Alex", 
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


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
> Example Response:

```json
{
  "id" : "IDs96tgaLNJv7rvA23J3zYe5",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2017-01-27T18:52:23.16Z",
  "updated_at" : "2017-01-27T18:52:23.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "name": "Maggie Green", 
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
	    "identity": "IDs96tgaLNJv7rvA23J3zYe5"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
$card = new PaymentCard(
	array(
	    "name"=> "Maggie Green", 
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
	    "identity"=> "IDs96tgaLNJv7rvA23J3zYe5"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Maggie Green", 
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
	    "identity": "IDs96tgaLNJv7rvA23J3zYe5"
	}).save()
```
> Example Response:

```json
{
  "id" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "fingerprint" : "FPR-952338680",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Green",
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
  "created_at" : "2017-01-27T18:52:23.55Z",
  "updated_at" : "2017-01-27T18:52:23.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs96tgaLNJv7rvA23J3zYe5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/updates"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "merchant_identity": "IDsQsVMwtkQzGRzBRhRZq25u", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PImJU78Vq5ub2xiGaQrCmhtL", 
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
    .merchantIdentity("IDsQsVMwtkQzGRzBRhRZq25u")
    .source("PImJU78Vq5ub2xiGaQrCmhtL")
    .build()
);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDsQsVMwtkQzGRzBRhRZq25u", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PImJU78Vq5ub2xiGaQrCmhtL", 
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
	    "merchant_identity": "IDsQsVMwtkQzGRzBRhRZq25u", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PImJU78Vq5ub2xiGaQrCmhtL", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUibbngBfJFGdRs6nQJ8d3hP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:28.26Z",
  "updated_at" : "2017-01-27T18:52:28.32Z",
  "trace_id" : "66d10c43-f580-4720-b4c7-1b4226517186",
  "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:52:28.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUibbngBfJFGdRs6nQJ8d3hP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
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
curl https://api-staging.finix.io/authorizations/AUibbngBfJFGdRs6nQJ8d3hP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUibbngBfJFGdRs6nQJ8d3hP");
authorization = authorization.capture(50L);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUibbngBfJFGdRs6nQJ8d3hP');
$authorization = $authorization->capture(50, 10);

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUibbngBfJFGdRs6nQJ8d3hP")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUibbngBfJFGdRs6nQJ8d3hP",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRbeAS1qH2wSnegGcs4dCedf",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:28.19Z",
  "updated_at" : "2017-01-27T18:52:29.10Z",
  "trace_id" : "66d10c43-f580-4720-b4c7-1b4226517186",
  "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "is_void" : false,
  "expires_at" : "2017-02-03T18:52:28.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUibbngBfJFGdRs6nQJ8d3hP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
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
### Step 1: Create a Recipient Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Curry", 
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

import io.crossriver.payments.processing.client.model.Address;
import io.crossriver.payments.processing.client.model.BankAccountType;
import io.crossriver.payments.processing.client.model.BusinessType;
import io.crossriver.payments.processing.client.model.Date;
import io.crossriver.payments.processing.client.model.Entity;
import io.crossriver.payments.processing.client.model.Identity;;

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
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
	        "last_name"=> "Curry", 
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
> Example Response:

```json
{
  "id" : "IDaTJa8KoZgnPDdA5gkTmz7N",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
    "last_name" : "Curry",
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
  "created_at" : "2017-01-27T18:52:36.11Z",
  "updated_at" : "2017-01-27T18:52:36.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "name": "Jessie Chang", 
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
	    "identity": "IDaTJa8KoZgnPDdA5gkTmz7N"
	}'
```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDaTJa8KoZgnPDdA5gkTmz7N');
$card = new PaymentCard(
	array(
	    "name"=> "Jessie Chang", 
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
	    "identity"=> "IDaTJa8KoZgnPDdA5gkTmz7N"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PI3AMzHBb6xo4uaTTUGT2sE6",
  "fingerprint" : "FPR1234127784",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jessie Chang",
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
  "created_at" : "2017-01-27T18:52:36.47Z",
  "updated_at" : "2017-01-27T18:52:36.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/updates"
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
curl https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
Identity identity = client.identitiesClient().fetchResource("PI3AMzHBb6xo4uaTTUGT2sE6");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDaTJa8KoZgnPDdA5gkTmz7N');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MU5wRYGJSmeG1rdHe95voX1N",
  "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
  "verification" : "VIo8Cw8xwKQyTFUMfWd6pjon",
  "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:36.86Z",
  "updated_at" : "2017-01-27T18:52:36.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5wRYGJSmeG1rdHe95voX1N"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5wRYGJSmeG1rdHe95voX1N/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIo8Cw8xwKQyTFUMfWd6pjon"
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
    -u USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PI3AMzHBb6xo4uaTTUGT2sE6", 
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
use CrossRiver\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI3AMzHBb6xo4uaTTUGT2sE6", 
	    "processor"=> "VISA_V1", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$transfer = $transfer->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRftrKKryX7gBSHcBmnD6hTH",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190064",
  "currency" : "USD",
  "application" : "APo33Betu7pEGtdw63VA8tFV",
  "source" : "PI4xNZKYDWWM5WkdaZQEjipW",
  "destination" : "PI3AMzHBb6xo4uaTTUGT2sE6",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:38.05Z",
  "updated_at" : "2017-01-27T18:52:39.28Z",
  "merchant_identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6"
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
          applicationId: 'APo33Betu7pEGtdw63VA8tFV',
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
  "id" : "TKo8efS9cGmS73HbUod5FRTo",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-27T18:52:30.35Z",
  "updated_at" : "2017-01-27T18:52:30.35Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-28T18:52:30.35Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "token": "TKo8efS9cGmS73HbUod5FRTo", 
	    "type": "TOKEN", 
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKo8efS9cGmS73HbUod5FRTo")
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKo8efS9cGmS73HbUod5FRTo", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDsQsVMwtkQzGRzBRhRZq25u"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKo8efS9cGmS73HbUod5FRTo", 
	    "type": "TOKEN", 
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIo8efS9cGmS73HbUod5FRTo",
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
  "created_at" : "2017-01-27T18:52:30.71Z",
  "updated_at" : "2017-01-27T18:52:30.71Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/updates"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Alex", 
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


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
> Example Response:

```json
{
  "id" : "IDs96tgaLNJv7rvA23J3zYe5",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2017-01-27T18:52:23.16Z",
  "updated_at" : "2017-01-27T18:52:23.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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

import io.crossriver.payments.processing.client.model.Address;
import io.crossriver.payments.processing.client.model.BankAccountType;
import io.crossriver.payments.processing.client.model.BusinessType;
import io.crossriver.payments.processing.client.model.Date;
import io.crossriver.payments.processing.client.model.Entity;
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
use CrossRiver\Resources\Identity;

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


from crossriver.resources import Identity

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
> Example Response:

```json
{
  "id" : "IDsQsVMwtkQzGRzBRhRZq25u",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:16.68Z",
  "updated_at" : "2017-01-27T18:52:16.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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

curl https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDsQsVMwtkQzGRzBRhRZq25u");

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDsQsVMwtkQzGRzBRhRZq25u")

```
> Example Response:

```json
{
  "id" : "IDsQsVMwtkQzGRzBRhRZq25u",
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Lees Sandwiches"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-27T18:52:16.66Z",
  "updated_at" : "2017-01-27T18:52:16.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e


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
      "id" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
        "last_name" : "Curry",
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
      "created_at" : "2017-01-27T18:52:36.09Z",
      "updated_at" : "2017-01-27T18:52:36.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDs96tgaLNJv7rvA23J3zYe5",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2017-01-27T18:52:23.14Z",
      "updated_at" : "2017-01-27T18:52:23.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "ID9AQdcP6HRSK43h63GTUE7L",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:20.93Z",
      "updated_at" : "2017-01-27T18:52:20.93Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9AQdcP6HRSK43h63GTUE7L/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "ID2Fm9jkKZjDEeRDDFnHAGus",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:20.51Z",
      "updated_at" : "2017-01-27T18:52:20.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2Fm9jkKZjDEeRDDFnHAGus/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDeVYhZLuUZp1w1qfLjsdjNd",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:20.09Z",
      "updated_at" : "2017-01-27T18:52:20.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeVYhZLuUZp1w1qfLjsdjNd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDdNckjB4FDBVQmxmRgN59VM",
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
      "created_at" : "2017-01-27T18:52:19.53Z",
      "updated_at" : "2017-01-27T18:52:19.53Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdNckjB4FDBVQmxmRgN59VM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "ID4h38XWTzw3uDj1Pokpb9GC",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "GENERAL_PARTNERSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:19.05Z",
      "updated_at" : "2017-01-27T18:52:19.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4h38XWTzw3uDj1Pokpb9GC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDfD9X6HcCqAo16vGGo2sgwJ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:18.46Z",
      "updated_at" : "2017-01-27T18:52:18.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfD9X6HcCqAo16vGGo2sgwJ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDx2DMfSfckPqJMD416dH9pr",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:18.04Z",
      "updated_at" : "2017-01-27T18:52:18.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDx2DMfSfckPqJMD416dH9pr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDdGvPJLVFZxW2Wbs3YN2RYH",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:17.51Z",
      "updated_at" : "2017-01-27T18:52:17.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGvPJLVFZxW2Wbs3YN2RYH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDv3jn1mQoDgt28YdEPSMCUt",
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
      "created_at" : "2017-01-27T18:52:17.09Z",
      "updated_at" : "2017-01-27T18:52:17.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDv3jn1mQoDgt28YdEPSMCUt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDsQsVMwtkQzGRzBRhRZq25u",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-27T18:52:16.66Z",
      "updated_at" : "2017-01-27T18:52:16.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "IDmAMuExV6VpixDj8NLsa9bV",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2017-01-27T18:52:13.97Z",
      "updated_at" : "2017-01-27T18:52:13.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
curl https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "White", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Lees Sandwiches", 
	        "url": "www.LeesSandwiches.com", 
	        "business_name": "Lees Sandwiches", 
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
> Example Response:

```json
{
  "id" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "White",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Lees Sandwiches",
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
    "key" : "value_2"
  },
  "created_at" : "2017-01-27T18:52:16.66Z",
  "updated_at" : "2017-01-27T18:52:44.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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

curl https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java

import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDsQsVMwtkQzGRzBRhRZq25u")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "verification" : "VIzbNTXHbAtRY9EmcaQWDWB",
  "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:22.18Z",
  "updated_at" : "2017-01-27T18:52:22.18Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIzbNTXHbAtRY9EmcaQWDWB"
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
curl https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDsQsVMwtkQzGRzBRhRZq25u")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "verification" : "VIzbNTXHbAtRY9EmcaQWDWB",
  "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:22.18Z",
  "updated_at" : "2017-01-27T18:52:22.18Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIzbNTXHbAtRY9EmcaQWDWB"
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
curl https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUvdjEe9bqZBhj7ZvgbMz1tF");

```
```php
<?php
use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUvdjEe9bqZBhj7ZvgbMz1tF');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUvdjEe9bqZBhj7ZvgbMz1tF")

```
> Example Response:

```json
{
  "id" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "verification" : null,
  "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-27T18:52:22.15Z",
  "updated_at" : "2017-01-27T18:52:22.30Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
curl https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUvdjEe9bqZBhj7ZvgbMz1tF");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUvdjEe9bqZBhj7ZvgbMz1tF');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VI9sgoMezkXzjur7DdDosGiw",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:52:44.64Z",
  "updated_at" : "2017-01-27T18:52:44.66Z",
  "trace_id" : "00776ec9-e129-48f0-a3f1-baac22eb31ab",
  "payment_instrument" : null,
  "merchant" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9sgoMezkXzjur7DdDosGiw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
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
curl https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '{}'

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUvdjEe9bqZBhj7ZvgbMz1tF');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VI9sgoMezkXzjur7DdDosGiw",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-27T18:52:44.64Z",
  "updated_at" : "2017-01-27T18:52:44.66Z",
  "trace_id" : "00776ec9-e129-48f0-a3f1-baac22eb31ab",
  "payment_instrument" : null,
  "merchant" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9sgoMezkXzjur7DdDosGiw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

```
```java

```
```php
<?php
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
      "id" : "MU5wRYGJSmeG1rdHe95voX1N",
      "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "verification" : null,
      "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
      "processor" : "VISA_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-27T18:52:36.81Z",
      "updated_at" : "2017-01-27T18:52:37.26Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU5wRYGJSmeG1rdHe95voX1N"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU5wRYGJSmeG1rdHe95voX1N/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "verification" : null,
      "merchant_profile" : "MPnhCLbDVY25TAkG8EGfQPp8",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-27T18:52:22.15Z",
      "updated_at" : "2017-01-27T18:52:22.30Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPnhCLbDVY25TAkG8EGfQPp8"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
curl https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUvdjEe9bqZBhj7ZvgbMz1tF');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIzbNTXHbAtRY9EmcaQWDWB",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-27T18:52:22.15Z",
      "updated_at" : "2017-01-27T18:52:22.37Z",
      "trace_id" : "85bc28d9-7acb-4b44-8441-d6eb53988c2f",
      "payment_instrument" : null,
      "merchant" : "MUvdjEe9bqZBhj7ZvgbMz1tF",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/verifications/VIzbNTXHbAtRY9EmcaQWDWB"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "merchant" : {
          "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUvdjEe9bqZBhj7ZvgbMz1tF/verifications?offset=0&limit=20&sort=created_at,desc"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "name": "Maggie Green", 
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
	    "identity": "IDs96tgaLNJv7rvA23J3zYe5"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
$card = new PaymentCard(
	array(
	    "name"=> "Maggie Green", 
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
	    "identity"=> "IDs96tgaLNJv7rvA23J3zYe5"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Maggie Green", 
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
	    "identity": "IDs96tgaLNJv7rvA23J3zYe5"
	}).save()
```
> Example Response:

```json
{
  "id" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "fingerprint" : "FPR-952338680",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Green",
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
  "created_at" : "2017-01-27T18:52:23.55Z",
  "updated_at" : "2017-01-27T18:52:23.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs96tgaLNJv7rvA23J3zYe5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/updates"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}'


```
```java

import io.crossriver.payments.processing.client.model.BankAccount;
import io.crossriver.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
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
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\BankAccount;

$identity = Identity::retrieve('IDsQsVMwtkQzGRzBRhRZq25u');
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
	    "identity"=> "IDsQsVMwtkQzGRzBRhRZq25u"
	));
$bank_account = $identity->createBankAccount($bank_account);
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
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI76MpurcgyKzQMixwVDXVTP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:21.34Z",
  "updated_at" : "2017-01-27T18:52:21.34Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
    -d '
	{
	    "token": "TKo8efS9cGmS73HbUod5FRTo", 
	    "type": "TOKEN", 
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;
import io.crossriver.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TKo8efS9cGmS73HbUod5FRTo")
    .identity("IDsQsVMwtkQzGRzBRhRZq25u")
    .build()
);

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKo8efS9cGmS73HbUod5FRTo", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDsQsVMwtkQzGRzBRhRZq25u"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKo8efS9cGmS73HbUod5FRTo", 
	    "type": "TOKEN", 
	    "identity": "IDsQsVMwtkQzGRzBRhRZq25u"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIo8efS9cGmS73HbUod5FRTo",
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
  "created_at" : "2017-01-27T18:52:30.71Z",
  "updated_at" : "2017-01-27T18:52:30.71Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/updates"
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
curl https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PI76MpurcgyKzQMixwVDXVTP")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PI76MpurcgyKzQMixwVDXVTP');

```
```python



```
> Example Response:

```json
{
  "id" : "PI76MpurcgyKzQMixwVDXVTP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:21.31Z",
  "updated_at" : "2017-01-27T18:52:21.73Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
curl https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PImJU78Vq5ub2xiGaQrCmhtL")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PImJU78Vq5ub2xiGaQrCmhtL');

```
```python



```
> Example Response:

```json
{
  "id" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "fingerprint" : "FPR-952338680",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Green",
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
  "created_at" : "2017-01-27T18:52:23.52Z",
  "updated_at" : "2017-01-27T18:52:28.29Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDs96tgaLNJv7rvA23J3zYe5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/updates"
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

## Update a Payment Instrument
```shell
curl https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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

```
```python



```
> Example Response:

```json
{
  "id" : "PI76MpurcgyKzQMixwVDXVTP",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-27T18:52:21.31Z",
  "updated_at" : "2017-01-27T18:52:21.73Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e
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
      "id" : "PImhCpXvdBxfhbb1R9VVSC9H",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:36.81Z",
      "updated_at" : "2017-01-27T18:52:36.81Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImhCpXvdBxfhbb1R9VVSC9H"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImhCpXvdBxfhbb1R9VVSC9H/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImhCpXvdBxfhbb1R9VVSC9H/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImhCpXvdBxfhbb1R9VVSC9H/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI4xNZKYDWWM5WkdaZQEjipW",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:36.81Z",
      "updated_at" : "2017-01-27T18:52:36.81Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI2PThnerzbPj3fZvdvPVuG4",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:36.81Z",
      "updated_at" : "2017-01-27T18:52:36.81Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2PThnerzbPj3fZvdvPVuG4"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2PThnerzbPj3fZvdvPVuG4/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2PThnerzbPj3fZvdvPVuG4/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2PThnerzbPj3fZvdvPVuG4/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI3AMzHBb6xo4uaTTUGT2sE6",
      "fingerprint" : "FPR1234127784",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jessie Chang",
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
      "created_at" : "2017-01-27T18:52:36.44Z",
      "updated_at" : "2017-01-27T18:52:36.44Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6/updates"
        }
      }
    }, {
      "id" : "PIu4PUMxJRjvKehqxk8qMJmd",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:35.32Z",
      "updated_at" : "2017-01-27T18:52:35.32Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu4PUMxJRjvKehqxk8qMJmd"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu4PUMxJRjvKehqxk8qMJmd/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu4PUMxJRjvKehqxk8qMJmd/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIu4PUMxJRjvKehqxk8qMJmd/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIePpDhHBWMEA9EULX9iuukU",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:35.32Z",
      "updated_at" : "2017-01-27T18:52:35.32Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIePpDhHBWMEA9EULX9iuukU"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIePpDhHBWMEA9EULX9iuukU/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIePpDhHBWMEA9EULX9iuukU/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIePpDhHBWMEA9EULX9iuukU/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIwpKsyie4zE9C9i7NoixPXv",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:35.32Z",
      "updated_at" : "2017-01-27T18:52:35.32Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwpKsyie4zE9C9i7NoixPXv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwpKsyie4zE9C9i7NoixPXv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwpKsyie4zE9C9i7NoixPXv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwpKsyie4zE9C9i7NoixPXv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIgQGEUqL7EKpDXx655bd5D7",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:35.32Z",
      "updated_at" : "2017-01-27T18:52:35.32Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQGEUqL7EKpDXx655bd5D7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQGEUqL7EKpDXx655bd5D7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQGEUqL7EKpDXx655bd5D7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgQGEUqL7EKpDXx655bd5D7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIo8efS9cGmS73HbUod5FRTo",
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
      "created_at" : "2017-01-27T18:52:30.66Z",
      "updated_at" : "2017-01-27T18:52:30.66Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo8efS9cGmS73HbUod5FRTo/updates"
        }
      }
    }, {
      "id" : "PIvV4BXBXqyq1gQHkUkP8iq1",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:52:23.98Z",
      "updated_at" : "2017-01-27T18:52:23.98Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDs96tgaLNJv7rvA23J3zYe5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvV4BXBXqyq1gQHkUkP8iq1"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvV4BXBXqyq1gQHkUkP8iq1/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvV4BXBXqyq1gQHkUkP8iq1/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvV4BXBXqyq1gQHkUkP8iq1/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PImJU78Vq5ub2xiGaQrCmhtL",
      "fingerprint" : "FPR-952338680",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Maggie Green",
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
      "created_at" : "2017-01-27T18:52:23.52Z",
      "updated_at" : "2017-01-27T18:52:28.29Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDs96tgaLNJv7rvA23J3zYe5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDs96tgaLNJv7rvA23J3zYe5"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL/updates"
        }
      }
    }, {
      "id" : "PIeGfUFvUeE2d6yn8ThWsyC2",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:22.15Z",
      "updated_at" : "2017-01-27T18:52:22.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeGfUFvUeE2d6yn8ThWsyC2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeGfUFvUeE2d6yn8ThWsyC2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeGfUFvUeE2d6yn8ThWsyC2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeGfUFvUeE2d6yn8ThWsyC2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI6417csAhXRsmFuTRH5NLmr",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:22.15Z",
      "updated_at" : "2017-01-27T18:52:22.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6417csAhXRsmFuTRH5NLmr"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6417csAhXRsmFuTRH5NLmr/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6417csAhXRsmFuTRH5NLmr/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6417csAhXRsmFuTRH5NLmr/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIsdrFuu1caqjcqmKi5VNUSx",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:22.15Z",
      "updated_at" : "2017-01-27T18:52:22.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI76MpurcgyKzQMixwVDXVTP",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-27T18:52:21.31Z",
      "updated_at" : "2017-01-27T18:52:21.73Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI76MpurcgyKzQMixwVDXVTP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIvkHxR5PrbwGxPdvX9SC7GG",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:14.55Z",
      "updated_at" : "2017-01-27T18:52:14.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvkHxR5PrbwGxPdvX9SC7GG"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvkHxR5PrbwGxPdvX9SC7GG/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvkHxR5PrbwGxPdvX9SC7GG/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvkHxR5PrbwGxPdvX9SC7GG/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIpXSfzStA4HEZEUokxnfZYs",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:14.55Z",
      "updated_at" : "2017-01-27T18:52:14.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpXSfzStA4HEZEUokxnfZYs"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpXSfzStA4HEZEUokxnfZYs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpXSfzStA4HEZEUokxnfZYs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpXSfzStA4HEZEUokxnfZYs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PI2U8Hav1D2pJAvEXSKVKE41",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:14.55Z",
      "updated_at" : "2017-01-27T18:52:14.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2U8Hav1D2pJAvEXSKVKE41"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2U8Hav1D2pJAvEXSKVKE41/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2U8Hav1D2pJAvEXSKVKE41/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2U8Hav1D2pJAvEXSKVKE41/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        }
      }
    }, {
      "id" : "PIxf5UWE6gkdcELv9ZwQjUn4",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-27T18:52:14.55Z",
      "updated_at" : "2017-01-27T18:52:14.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmAMuExV6VpixDj8NLsa9bV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxf5UWE6gkdcELv9ZwQjUn4"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxf5UWE6gkdcELv9ZwQjUn4/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmAMuExV6VpixDj8NLsa9bV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxf5UWE6gkdcELv9ZwQjUn4/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxf5UWE6gkdcELv9ZwQjUn4/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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

`ready_to_settle_at` field can have 2 possible values:

1. `null`: Funds have been captured, but are not yet ready to be paid out
2. `TIMESTAMP`: A UTC timestamp that specifies when the funds will be available to be payout out. Once in the past, the Transfer will be eligible for inclusion in a batch Settlement.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRfm9dgyjRhji5rRWzbQbD7G");

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRfm9dgyjRhji5rRWzbQbD7G');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRfm9dgyjRhji5rRWzbQbD7G")

```
> Example Response:

```json
{
  "id" : "TRfm9dgyjRhji5rRWzbQbD7G",
  "amount" : 39716,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "ba0b85a7-5819-41d6-972d-92ef676d4c6c",
  "currency" : "USD",
  "application" : "APo33Betu7pEGtdw63VA8tFV",
  "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "destination" : "PIsdrFuu1caqjcqmKi5VNUSx",
  "ready_to_settle_at" : null,
  "fee" : 3972,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:24.51Z",
  "updated_at" : "2017-01-27T18:52:24.64Z",
  "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx"
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

curl https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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
use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRfm9dgyjRhji5rRWzbQbD7G');
$refund = $debit->reverse(11);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRfm9dgyjRhji5rRWzbQbD7G")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRk7HXz4mqChfMK4Bj8TJPjN",
  "amount" : 26581,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "9acdf46b-1c4f-4940-98ed-534f240f4efe",
  "currency" : "USD",
  "application" : "APo33Betu7pEGtdw63VA8tFV",
  "source" : "PIsdrFuu1caqjcqmKi5VNUSx",
  "destination" : "PImJU78Vq5ub2xiGaQrCmhtL",
  "ready_to_settle_at" : null,
  "fee" : 2658,
  "statement_descriptor" : "FNX*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-27T18:52:27.44Z",
  "updated_at" : "2017-01-27T18:52:27.52Z",
  "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRk7HXz4mqChfMK4Bj8TJPjN"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRk7HXz4mqChfMK4Bj8TJPjN/payment_instruments"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

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
      "id" : "TRftrKKryX7gBSHcBmnD6hTH",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "190064",
      "currency" : "USD",
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "source" : "PI4xNZKYDWWM5WkdaZQEjipW",
      "destination" : "PI3AMzHBb6xo4uaTTUGT2sE6",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:37.95Z",
      "updated_at" : "2017-01-27T18:52:39.28Z",
      "merchant_identity" : "IDaTJa8KoZgnPDdA5gkTmz7N",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaTJa8KoZgnPDdA5gkTmz7N"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRftrKKryX7gBSHcBmnD6hTH/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4xNZKYDWWM5WkdaZQEjipW"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3AMzHBb6xo4uaTTUGT2sE6"
        }
      }
    }, {
      "id" : "TRbeAS1qH2wSnegGcs4dCedf",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "66d10c43-f580-4720-b4c7-1b4226517186",
      "currency" : "USD",
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
      "destination" : "PIsdrFuu1caqjcqmKi5VNUSx",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:28.95Z",
      "updated_at" : "2017-01-27T18:52:29.10Z",
      "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRbeAS1qH2wSnegGcs4dCedf/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx"
        }
      }
    }, {
      "id" : "TRk7HXz4mqChfMK4Bj8TJPjN",
      "amount" : 26581,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "7c553247-378c-4bf4-b68c-bb204faa5465",
      "currency" : "USD",
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "source" : "PIsdrFuu1caqjcqmKi5VNUSx",
      "destination" : "PImJU78Vq5ub2xiGaQrCmhtL",
      "ready_to_settle_at" : null,
      "fee" : 2658,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:27.27Z",
      "updated_at" : "2017-01-27T18:52:27.52Z",
      "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRk7HXz4mqChfMK4Bj8TJPjN"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRk7HXz4mqChfMK4Bj8TJPjN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
        }
      }
    }, {
      "id" : "TRqXPrRknwzdtRGE24bAGZHW",
      "amount" : 26581,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "080fec38-a2c8-451a-bf9f-0702c1621c5d",
      "currency" : "USD",
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
      "destination" : "PIsdrFuu1caqjcqmKi5VNUSx",
      "ready_to_settle_at" : null,
      "fee" : 2658,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:26.49Z",
      "updated_at" : "2017-01-27T18:52:27.36Z",
      "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqXPrRknwzdtRGE24bAGZHW/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx"
        }
      }
    }, {
      "id" : "TRfm9dgyjRhji5rRWzbQbD7G",
      "amount" : 39716,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "ba0b85a7-5819-41d6-972d-92ef676d4c6c",
      "currency" : "USD",
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "source" : "PImJU78Vq5ub2xiGaQrCmhtL",
      "destination" : "PIsdrFuu1caqjcqmKi5VNUSx",
      "ready_to_settle_at" : null,
      "fee" : 3972,
      "statement_descriptor" : "FNX*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-27T18:52:24.51Z",
      "updated_at" : "2017-01-27T18:52:24.64Z",
      "merchant_identity" : "IDsQsVMwtkQzGRzBRhRZq25u",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDsQsVMwtkQzGRzBRhRZq25u"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRfm9dgyjRhji5rRWzbQbD7G/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImJU78Vq5ub2xiGaQrCmhtL"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsdrFuu1caqjcqmKi5VNUSx"
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
    -u USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e \
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
use CrossRiver\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
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
  "id" : "WH8V1NtJiviRLVEMUgonNcfn",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APo33Betu7pEGtdw63VA8tFV",
  "created_at" : "2017-01-27T18:52:16.36Z",
  "updated_at" : "2017-01-27T18:52:16.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH8V1NtJiviRLVEMUgonNcfn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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



curl https://api-staging.finix.io/webhooks/WH8V1NtJiviRLVEMUgonNcfn \
    -H "Content-Type: application/vnd.json+api" \
    -u USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH8V1NtJiviRLVEMUgonNcfn");

```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WH8V1NtJiviRLVEMUgonNcfn');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WH8V1NtJiviRLVEMUgonNcfn")

```
> Example Response:

```json
{
  "id" : "WH8V1NtJiviRLVEMUgonNcfn",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APo33Betu7pEGtdw63VA8tFV",
  "created_at" : "2017-01-27T18:52:16.36Z",
  "updated_at" : "2017-01-27T18:52:16.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH8V1NtJiviRLVEMUgonNcfn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
    -u  USbBaUzyrgmSyFeRipRUZG1F:aec11417-7423-4e34-a6d1-a09c8b76509e

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
      "id" : "WH8V1NtJiviRLVEMUgonNcfn",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APo33Betu7pEGtdw63VA8tFV",
      "created_at" : "2017-01-27T18:52:16.36Z",
      "updated_at" : "2017-01-27T18:52:16.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WH8V1NtJiviRLVEMUgonNcfn"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APo33Betu7pEGtdw63VA8tFV"
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
