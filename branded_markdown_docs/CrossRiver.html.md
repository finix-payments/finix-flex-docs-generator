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

4. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USoDReh5TNALwVGL3Xzu6SbA", "089536c0-4dd2-4205-a207-1ed0dc9909af"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USoDReh5TNALwVGL3Xzu6SbA`

- Password: `089536c0-4dd2-4205-a207-1ed0dc9909af`

- Application ID: `APgD91hb3sYVdLTC7BQSM5i3`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** https://api-staging.finix.io

- **Production API:** https://api.finix.io

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "Prestige World Wide", 
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
	        "doing_business_as": "Prestige World Wide", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Prestige World Wide", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PrestigeWorldWide.com", 
	        "annual_card_volume": 12000000
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 120000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Prestige World Wide", 
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
	        "doing_business_as"=> "Prestige World Wide", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Prestige World Wide", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PrestigeWorldWide.com", 
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
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Prestige World Wide", 
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
	        "doing_business_as": "Prestige World Wide", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Prestige World Wide", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PrestigeWorldWide.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "IDwpfuevovRvifZXEPgY4VSD",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Prestige World Wide",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "max_transaction_amount" : 120000,
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Prestige World Wide"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:35:44.40Z",
  "updated_at" : "2016-11-15T04:35:44.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}'


```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
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
	    "identity"=> "IDwpfuevovRvifZXEPgY4VSD"
	));
$bank_account = $bank_account->save();

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
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIb6yzdWhdE6QbsgveR8AwHN",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T04:35:52.24Z",
  "updated_at" : "2016-11-15T04:35:52.24Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDwpfuevovRvifZXEPgY4VSD');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDwpfuevovRvifZXEPgY4VSD")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "verification" : "VIt843BNigBmyeAP1rhxyavc",
  "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T04:35:53.62Z",
  "updated_at" : "2016-11-15T04:35:53.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIt843BNigBmyeAP1rhxyavc"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
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
	)
);
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
	        "first_name": "Step", 
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
  "id" : "ID3c7RSVDDGUKLDiQcoGYN68",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:35:54.79Z",
  "updated_at" : "2016-11-15T04:35:54.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "name": "Step Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
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
	    "identity": "ID3c7RSVDDGUKLDiQcoGYN68"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Step Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
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
	    "identity"=> "ID3c7RSVDDGUKLDiQcoGYN68"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Step Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
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
	    "identity": "ID3c7RSVDDGUKLDiQcoGYN68"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIh3yRBquQ7EXdXab9cURoFg",
  "fingerprint" : "FPR-2142146072",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Lopez",
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
  "created_at" : "2016-11-15T04:35:55.35Z",
  "updated_at" : "2016-11-15T04:35:55.35Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3c7RSVDDGUKLDiQcoGYN68",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/updates"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "merchant_identity": "IDwpfuevovRvifZXEPgY4VSD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh3yRBquQ7EXdXab9cURoFg", 
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
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDwpfuevovRvifZXEPgY4VSD", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIh3yRBquQ7EXdXab9cURoFg", 
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
	    "merchant_identity": "IDwpfuevovRvifZXEPgY4VSD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh3yRBquQ7EXdXab9cURoFg", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AU8G7A9ZCxApvonT4oEJCdNF",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T04:36:01.27Z",
  "updated_at" : "2016-11-15T04:36:01.28Z",
  "trace_id" : "548e2f65-78bf-491e-9c3f-9a072283afb0",
  "source" : "PIh3yRBquQ7EXdXab9cURoFg",
  "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "is_void" : false,
  "expires_at" : "2016-11-22T04:36:01.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8G7A9ZCxApvonT4oEJCdNF"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
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
curl https://api-staging.finix.io/authorizations/AU8G7A9ZCxApvonT4oEJCdNF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8G7A9ZCxApvonT4oEJCdNF");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AU8G7A9ZCxApvonT4oEJCdNF');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8G7A9ZCxApvonT4oEJCdNF")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AU8G7A9ZCxApvonT4oEJCdNF",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRxhkUeCCNTg9csnd3Ub6rKr",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T04:36:01.12Z",
  "updated_at" : "2016-11-15T04:36:02.15Z",
  "trace_id" : "548e2f65-78bf-491e-9c3f-9a072283afb0",
  "source" : "PIh3yRBquQ7EXdXab9cURoFg",
  "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "is_void" : false,
  "expires_at" : "2016-11-22T04:36:01.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8G7A9ZCxApvonT4oEJCdNF"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
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
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "ID6rLTvQd55QT9KzDFr6Xjm9",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:36:13.93Z",
  "updated_at" : "2016-11-15T04:36:13.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "name": "Maggie Curry", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
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
	    "identity": "ID6rLTvQd55QT9KzDFr6Xjm9"
	}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Venmo"
	    ), 
	    "user"=> "USoDReh5TNALwVGL3Xzu6SbA", 
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
	        "max_transaction_amount"=> 12000, 
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
> Example Response:

```json
{
  "id" : "PI9MMWTSAuUmaiNKHvybEfk",
  "fingerprint" : "FPR-1892162936",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Curry",
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
  "created_at" : "2016-11-15T04:36:15.86Z",
  "updated_at" : "2016-11-15T04:36:15.86Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID6rLTvQd55QT9KzDFr6Xjm9",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/updates"
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
curl https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUx5SvNyCCh88oJBbdZghZYT",
  "identity" : "ID6rLTvQd55QT9KzDFr6Xjm9",
  "verification" : "VIgw9qkA2eQcEwtg4K7LwVXY",
  "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T04:36:15.12Z",
  "updated_at" : "2016-11-15T04:36:15.12Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUx5SvNyCCh88oJBbdZghZYT"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUx5SvNyCCh88oJBbdZghZYT/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIgw9qkA2eQcEwtg4K7LwVXY"
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
    -u USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID6rLTvQd55QT9KzDFr6Xjm9", 
	    "destination": "PI9MMWTSAuUmaiNKHvybEfk", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Venmo"
	    ), 
	    "user"=> "USoDReh5TNALwVGL3Xzu6SbA", 
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
	        "max_transaction_amount"=> 12000, 
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
> Example Response:

```json
{
  "id" : "TR7DzfatzTWJHEpPy3H6XfgF",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "91654",
  "currency" : "USD",
  "application" : "APgD91hb3sYVdLTC7BQSM5i3",
  "source" : "PIsiAAErbLL1shTUaqYLRTii",
  "destination" : "PI9MMWTSAuUmaiNKHvybEfk",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T04:36:16.72Z",
  "updated_at" : "2016-11-15T04:36:19.68Z",
  "merchant_identity" : "IDbkxrnFVUn1KSFKUvABEzai",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk"
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
          applicationId: 'APgD91hb3sYVdLTC7BQSM5i3',
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
  "id" : "TKosc17aDp76Rv4j4Dtkm69g",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T04:36:04.33Z",
  "updated_at" : "2016-11-15T04:36:04.33Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T04:36:04.33Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIosc17aDp76Rv4j4Dtkm69g",
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
  "created_at" : "2016-11-15T04:36:06.27Z",
  "updated_at" : "2016-11-15T04:36:06.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/updates"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
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
	)
);
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
	        "first_name": "Step", 
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
  "id" : "ID3c7RSVDDGUKLDiQcoGYN68",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:35:54.79Z",
  "updated_at" : "2016-11-15T04:35:54.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "Prestige World Wide", 
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
	        "doing_business_as": "Prestige World Wide", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Prestige World Wide", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PrestigeWorldWide.com", 
	        "annual_card_volume": 12000000
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "amex_mid"=> "12345678910", 
	        "max_transaction_amount"=> 120000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Prestige World Wide", 
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
	        "doing_business_as"=> "Prestige World Wide", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Prestige World Wide", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PrestigeWorldWide.com", 
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
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Prestige World Wide", 
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
	        "doing_business_as": "Prestige World Wide", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Prestige World Wide", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PrestigeWorldWide.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "IDwpfuevovRvifZXEPgY4VSD",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Prestige World Wide",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "max_transaction_amount" : 120000,
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Prestige World Wide"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:35:44.40Z",
  "updated_at" : "2016-11-15T04:35:44.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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

curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDwpfuevovRvifZXEPgY4VSD");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDwpfuevovRvifZXEPgY4VSD');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDwpfuevovRvifZXEPgY4VSD")

```
> Example Response:

```json
{
  "id" : "IDwpfuevovRvifZXEPgY4VSD",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Prestige World Wide",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "max_transaction_amount" : 120000,
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Prestige World Wide"
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T04:35:44.34Z",
  "updated_at" : "2016-11-15T04:35:44.34Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af


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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "ID6rLTvQd55QT9KzDFr6Xjm9",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:36:13.87Z",
      "updated_at" : "2016-11-15T04:36:13.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID3c7RSVDDGUKLDiQcoGYN68",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:54.73Z",
      "updated_at" : "2016-11-15T04:35:54.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDmNj2hMoCx77j32Q5mhsncU",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:51.60Z",
      "updated_at" : "2016-11-15T04:35:51.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDwuMjPN3hdp9XB6oSAw5yzy",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:51.06Z",
      "updated_at" : "2016-11-15T04:35:51.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDqXh3KmKpm3yhFZDXc6TWZ",
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
        "max_transaction_amount" : 120000,
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
      },
      "created_at" : "2016-11-15T04:35:50.14Z",
      "updated_at" : "2016-11-15T04:35:50.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6VguEKa1m1Nf33iptGWAHz",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:49.61Z",
      "updated_at" : "2016-11-15T04:35:49.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDkrhkdemFcVJoQcsrdpXgkX",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:49.07Z",
      "updated_at" : "2016-11-15T04:35:49.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDhnWsWvV6HTq3bZ9Vw4gufr",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:48.09Z",
      "updated_at" : "2016-11-15T04:35:48.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6ArFWMFadHjKRY2dcu3oKb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:46.36Z",
      "updated_at" : "2016-11-15T04:35:46.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID3AM3gVZzpT1g2w2a2A9wwT",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:45.81Z",
      "updated_at" : "2016-11-15T04:35:45.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6dYU7uGu85R2wgxqCbeLsE",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:45.25Z",
      "updated_at" : "2016-11-15T04:35:45.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDwpfuevovRvifZXEPgY4VSD",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:44.34Z",
      "updated_at" : "2016-11-15T04:35:44.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDbkxrnFVUn1KSFKUvABEzai",
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
        "max_transaction_amount" : 12000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-11-15T04:35:40.85Z",
      "updated_at" : "2016-11-15T04:35:40.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Ricardo", 
	        "last_name": "Curry", 
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
	        "max_transaction_amount": 120000, 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDwpfuevovRvifZXEPgY4VSD",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Ricardo",
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
    "mcc" : 742,
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 120000,
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Dunder Mifflin"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2016-11-15T04:35:44.34Z",
  "updated_at" : "2016-11-15T04:36:27.43Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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

curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '


```
```java

import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDwpfuevovRvifZXEPgY4VSD');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );
```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDwpfuevovRvifZXEPgY4VSD")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "verification" : "VIt843BNigBmyeAP1rhxyavc",
  "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T04:35:53.62Z",
  "updated_at" : "2016-11-15T04:35:53.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIt843BNigBmyeAP1rhxyavc"
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
curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDwpfuevovRvifZXEPgY4VSD');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDwpfuevovRvifZXEPgY4VSD")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "verification" : "VIt843BNigBmyeAP1rhxyavc",
  "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T04:35:53.62Z",
  "updated_at" : "2016-11-15T04:35:53.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIt843BNigBmyeAP1rhxyavc"
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
curl https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUeCdyVBSamNJFkrrWHhU6Fr");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUeCdyVBSamNJFkrrWHhU6Fr');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUeCdyVBSamNJFkrrWHhU6Fr")

```
> Example Response:

```json
{
  "id" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "verification" : null,
  "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-15T04:35:53.52Z",
  "updated_at" : "2016-11-15T04:35:53.74Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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

## Create a Merchant User
```shell
curl https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "US6xmjLpX5crd6Hf6AeBynPL",
  "password" : "a02c0ed5-8ffd-43da-9d73-0c1bf2739d68",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-15T04:35:57.44Z",
  "updated_at" : "2016-11-15T04:35:57.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US6xmjLpX5crd6Hf6AeBynPL"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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


## Reattempt Merchant Provisioning
```shell
curl https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIupfhVd4PjTfXprCMssfsHP",
  "external_trace_id" : "db1bbe26-b9e9-44fd-8d52-bc0b6012823f",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T04:36:28.79Z",
  "updated_at" : "2016-11-15T04:36:28.81Z",
  "payment_instrument" : null,
  "merchant" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIupfhVd4PjTfXprCMssfsHP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
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
curl https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIupfhVd4PjTfXprCMssfsHP",
  "external_trace_id" : "db1bbe26-b9e9-44fd-8d52-bc0b6012823f",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T04:36:28.79Z",
  "updated_at" : "2016-11-15T04:36:28.81Z",
  "payment_instrument" : null,
  "merchant" : "MUeCdyVBSamNJFkrrWHhU6Fr",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIupfhVd4PjTfXprCMssfsHP"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "MUx5SvNyCCh88oJBbdZghZYT",
      "identity" : "ID6rLTvQd55QT9KzDFr6Xjm9",
      "verification" : null,
      "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-15T04:36:15.04Z",
      "updated_at" : "2016-11-15T04:36:15.04Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUx5SvNyCCh88oJBbdZghZYT"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUx5SvNyCCh88oJBbdZghZYT/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "MUeCdyVBSamNJFkrrWHhU6Fr",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "verification" : null,
      "merchant_profile" : "MPi1Y6GyretDoxVQyj8Dbgi9",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-15T04:35:53.52Z",
      "updated_at" : "2016-11-15T04:35:53.74Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPi1Y6GyretDoxVQyj8Dbgi9"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
curl https://api-staging.finix.io/merchants/MUeCdyVBSamNJFkrrWHhU6Fr/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID6rLTvQd55QT9KzDFr6Xjm9",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:36:13.87Z",
      "updated_at" : "2016-11-15T04:36:13.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID3c7RSVDDGUKLDiQcoGYN68",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:54.73Z",
      "updated_at" : "2016-11-15T04:35:54.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDmNj2hMoCx77j32Q5mhsncU",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:51.60Z",
      "updated_at" : "2016-11-15T04:35:51.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmNj2hMoCx77j32Q5mhsncU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDwuMjPN3hdp9XB6oSAw5yzy",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:51.06Z",
      "updated_at" : "2016-11-15T04:35:51.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwuMjPN3hdp9XB6oSAw5yzy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDqXh3KmKpm3yhFZDXc6TWZ",
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
        "max_transaction_amount" : 120000,
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
      },
      "created_at" : "2016-11-15T04:35:50.14Z",
      "updated_at" : "2016-11-15T04:35:50.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqXh3KmKpm3yhFZDXc6TWZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6VguEKa1m1Nf33iptGWAHz",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:49.61Z",
      "updated_at" : "2016-11-15T04:35:49.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6VguEKa1m1Nf33iptGWAHz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDkrhkdemFcVJoQcsrdpXgkX",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:49.07Z",
      "updated_at" : "2016-11-15T04:35:49.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkrhkdemFcVJoQcsrdpXgkX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDhnWsWvV6HTq3bZ9Vw4gufr",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:48.09Z",
      "updated_at" : "2016-11-15T04:35:48.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhnWsWvV6HTq3bZ9Vw4gufr/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6ArFWMFadHjKRY2dcu3oKb",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:46.36Z",
      "updated_at" : "2016-11-15T04:35:46.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6ArFWMFadHjKRY2dcu3oKb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID3AM3gVZzpT1g2w2a2A9wwT",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:45.81Z",
      "updated_at" : "2016-11-15T04:35:45.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3AM3gVZzpT1g2w2a2A9wwT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "ID6dYU7uGu85R2wgxqCbeLsE",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "CORPORATION",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:45.25Z",
      "updated_at" : "2016-11-15T04:35:45.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6dYU7uGu85R2wgxqCbeLsE/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDwpfuevovRvifZXEPgY4VSD",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T04:35:44.34Z",
      "updated_at" : "2016-11-15T04:35:44.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "IDbkxrnFVUn1KSFKUvABEzai",
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
        "max_transaction_amount" : 12000,
        "amex_mid" : null,
        "discover_mid" : null,
        "url" : null,
        "annual_card_volume" : 0,
        "has_accepted_credit_cards_previously" : false,
        "incorporation_date" : null,
        "principal_percentage_ownership" : null,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Venmo"
      },
      "created_at" : "2016-11-15T04:35:40.85Z",
      "updated_at" : "2016-11-15T04:35:40.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "name": "Step Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
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
	    "identity": "ID3c7RSVDDGUKLDiQcoGYN68"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Step Lopez", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
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
	    "identity"=> "ID3c7RSVDDGUKLDiQcoGYN68"
	));
$card = $card->save();


```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Step Lopez", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
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
	    "identity": "ID3c7RSVDDGUKLDiQcoGYN68"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIh3yRBquQ7EXdXab9cURoFg",
  "fingerprint" : "FPR-2142146072",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Lopez",
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
  "created_at" : "2016-11-15T04:35:55.35Z",
  "updated_at" : "2016-11-15T04:35:55.35Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3c7RSVDDGUKLDiQcoGYN68",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/updates"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}'


```
```java

import io.crossriver.payments.processing.client.model.BankAccount;

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
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
	    "identity"=> "IDwpfuevovRvifZXEPgY4VSD"
	));
$bank_account = $bank_account->save();


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
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIb6yzdWhdE6QbsgveR8AwHN",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T04:35:52.24Z",
  "updated_at" : "2016-11-15T04:35:52.24Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
## Tokenize Card with Embedded Iframe

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
          applicationId: 'APgD91hb3sYVdLTC7BQSM5i3',
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
  "id" : "TKosc17aDp76Rv4j4Dtkm69g",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T04:36:04.33Z",
  "updated_at" : "2016-11-15T04:36:04.33Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T04:36:04.33Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}'

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIosc17aDp76Rv4j4Dtkm69g",
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
  "created_at" : "2016-11-15T04:36:06.27Z",
  "updated_at" : "2016-11-15T04:36:06.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/updates"
    }
  }
}
```

Before you can use the newly tokenized card you will need to associate it with
an `Identity`. To do this you must make an authenticated `POST` request to the
`/payment_instruments` endpoint with the relevant token and the buyer's
`Identity` information.

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

## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
    -d '
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .token("TKkvwumxCgq5E8uTKyq96dta")
    .type("TOKEN")
    .identity("IDrfDP7Mty3CL7hj3UaGWUih")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	});
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKosc17aDp76Rv4j4Dtkm69g", 
	    "type": "TOKEN", 
	    "identity": "IDwpfuevovRvifZXEPgY4VSD"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIosc17aDp76Rv4j4Dtkm69g",
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
  "created_at" : "2016-11-15T04:36:06.27Z",
  "updated_at" : "2016-11-15T04:36:06.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/updates"
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


curl https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIb6yzdWhdE6QbsgveR8AwHN")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIb6yzdWhdE6QbsgveR8AwHN');

```
```python



```
> Example Response:

```json
{
  "id" : "PIb6yzdWhdE6QbsgveR8AwHN",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T04:35:52.15Z",
  "updated_at" : "2016-11-15T04:35:52.88Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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

## Update a Payment Instrument
```shell
curl https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PIb6yzdWhdE6QbsgveR8AwHN",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T04:35:52.15Z",
  "updated_at" : "2016-11-15T04:35:52.88Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI9MMWTSAuUmaiNKHvybEfk",
      "fingerprint" : "FPR-1892162936",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Maggie Curry",
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
      "created_at" : "2016-11-15T04:36:15.78Z",
      "updated_at" : "2016-11-15T04:36:15.78Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID6rLTvQd55QT9KzDFr6Xjm9",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID6rLTvQd55QT9KzDFr6Xjm9"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk/updates"
        }
      }
    }, {
      "id" : "PIsiAAErbLL1shTUaqYLRTii",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:36:12.60Z",
      "updated_at" : "2016-11-15T04:36:12.60Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIhgDG9NXfNMZuVnEx6H1WnY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:36:12.60Z",
      "updated_at" : "2016-11-15T04:36:12.60Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhgDG9NXfNMZuVnEx6H1WnY"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhgDG9NXfNMZuVnEx6H1WnY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhgDG9NXfNMZuVnEx6H1WnY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhgDG9NXfNMZuVnEx6H1WnY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PI8MsCjcVVHED4Zgw9Hdecqg",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:36:12.60Z",
      "updated_at" : "2016-11-15T04:36:12.60Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8MsCjcVVHED4Zgw9Hdecqg"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8MsCjcVVHED4Zgw9Hdecqg/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8MsCjcVVHED4Zgw9Hdecqg/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8MsCjcVVHED4Zgw9Hdecqg/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PI57gAvuoz6s2RnvpgFuCqqm",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:36:12.60Z",
      "updated_at" : "2016-11-15T04:36:12.60Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI57gAvuoz6s2RnvpgFuCqqm"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI57gAvuoz6s2RnvpgFuCqqm/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI57gAvuoz6s2RnvpgFuCqqm/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI57gAvuoz6s2RnvpgFuCqqm/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIosc17aDp76Rv4j4Dtkm69g",
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
      "created_at" : "2016-11-15T04:36:06.13Z",
      "updated_at" : "2016-11-15T04:36:06.13Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIosc17aDp76Rv4j4Dtkm69g/updates"
        }
      }
    }, {
      "id" : "PI4LgNWY7DS18M7iFWW2K9R3",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T04:35:55.81Z",
      "updated_at" : "2016-11-15T04:35:55.81Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID3c7RSVDDGUKLDiQcoGYN68",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4LgNWY7DS18M7iFWW2K9R3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4LgNWY7DS18M7iFWW2K9R3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4LgNWY7DS18M7iFWW2K9R3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4LgNWY7DS18M7iFWW2K9R3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIh3yRBquQ7EXdXab9cURoFg",
      "fingerprint" : "FPR-2142146072",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Step Lopez",
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
      "created_at" : "2016-11-15T04:35:55.27Z",
      "updated_at" : "2016-11-15T04:36:01.28Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID3c7RSVDDGUKLDiQcoGYN68",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID3c7RSVDDGUKLDiQcoGYN68"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg/updates"
        }
      }
    }, {
      "id" : "PI3pie7WhQUZRTYrZNotwbtP",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:53.52Z",
      "updated_at" : "2016-11-15T04:35:53.52Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3pie7WhQUZRTYrZNotwbtP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3pie7WhQUZRTYrZNotwbtP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3pie7WhQUZRTYrZNotwbtP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3pie7WhQUZRTYrZNotwbtP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIuHk7ja8iP3V3AEf4dxXGye",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:53.52Z",
      "updated_at" : "2016-11-15T04:35:53.52Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuHk7ja8iP3V3AEf4dxXGye"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuHk7ja8iP3V3AEf4dxXGye/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuHk7ja8iP3V3AEf4dxXGye/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuHk7ja8iP3V3AEf4dxXGye/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PI6hLTWquFArQehngU5YJrka",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:53.52Z",
      "updated_at" : "2016-11-15T04:35:53.52Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIb6yzdWhdE6QbsgveR8AwHN",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T04:35:52.15Z",
      "updated_at" : "2016-11-15T04:35:52.88Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIb6yzdWhdE6QbsgveR8AwHN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIheebkn8vkdygNpAAaYQ75L",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:41.48Z",
      "updated_at" : "2016-11-15T04:35:41.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIheebkn8vkdygNpAAaYQ75L"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIheebkn8vkdygNpAAaYQ75L/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIheebkn8vkdygNpAAaYQ75L/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIheebkn8vkdygNpAAaYQ75L/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIp8ksS2LGUTWk6ZhUQKk7Qx",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:41.48Z",
      "updated_at" : "2016-11-15T04:35:41.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8ksS2LGUTWk6ZhUQKk7Qx"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8ksS2LGUTWk6ZhUQKk7Qx/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8ksS2LGUTWk6ZhUQKk7Qx/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp8ksS2LGUTWk6ZhUQKk7Qx/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PI7JvcMjkdvF78Csn16uFCCm",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:41.48Z",
      "updated_at" : "2016-11-15T04:35:41.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7JvcMjkdvF78Csn16uFCCm"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7JvcMjkdvF78Csn16uFCCm/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7JvcMjkdvF78Csn16uFCCm/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7JvcMjkdvF78Csn16uFCCm/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        }
      }
    }, {
      "id" : "PIs5rwoSesDMtQwe89Jr7fxh",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T04:35:41.48Z",
      "updated_at" : "2016-11-15T04:35:41.48Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIs5rwoSesDMtQwe89Jr7fxh"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIs5rwoSesDMtQwe89Jr7fxh/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIs5rwoSesDMtQwe89Jr7fxh/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIs5rwoSesDMtQwe89Jr7fxh/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    "count" : 16
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

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRaFEHTBXRaYqXdFTuJjgpQE");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRaFEHTBXRaYqXdFTuJjgpQE');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRaFEHTBXRaYqXdFTuJjgpQE")

```
> Example Response:

```json
{
  "id" : "TRaFEHTBXRaYqXdFTuJjgpQE",
  "amount" : 275655,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "ae15c58c-321d-4643-baee-62474508c6f8",
  "currency" : "USD",
  "application" : "APgD91hb3sYVdLTC7BQSM5i3",
  "source" : "PIh3yRBquQ7EXdXab9cURoFg",
  "destination" : "PI6hLTWquFArQehngU5YJrka",
  "ready_to_settle_at" : null,
  "fee" : 27566,
  "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T04:35:56.51Z",
  "updated_at" : "2016-11-15T04:36:00.15Z",
  "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka"
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

curl https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRaFEHTBXRaYqXdFTuJjgpQE');
$refund = $debit->reverse(50);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRaFEHTBXRaYqXdFTuJjgpQE")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRvSAH5kzUqtvLwqH9CXQRF7",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "f1e9996c-fd0f-48a1-8f94-8d092793f9b0",
  "currency" : "USD",
  "application" : "APgD91hb3sYVdLTC7BQSM5i3",
  "source" : "PI6hLTWquFArQehngU5YJrka",
  "destination" : "PIh3yRBquQ7EXdXab9cURoFg",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T04:36:00.21Z",
  "updated_at" : "2016-11-15T04:36:00.30Z",
  "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRvSAH5kzUqtvLwqH9CXQRF7"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRvSAH5kzUqtvLwqH9CXQRF7/payment_instruments"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "TR7DzfatzTWJHEpPy3H6XfgF",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "91654",
      "currency" : "USD",
      "application" : "APgD91hb3sYVdLTC7BQSM5i3",
      "source" : "PIsiAAErbLL1shTUaqYLRTii",
      "destination" : "PI9MMWTSAuUmaiNKHvybEfk",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T04:36:16.51Z",
      "updated_at" : "2016-11-15T04:36:19.68Z",
      "merchant_identity" : "IDbkxrnFVUn1KSFKUvABEzai",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbkxrnFVUn1KSFKUvABEzai"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7DzfatzTWJHEpPy3H6XfgF/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsiAAErbLL1shTUaqYLRTii"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9MMWTSAuUmaiNKHvybEfk"
        }
      }
    }, {
      "id" : "TRxhkUeCCNTg9csnd3Ub6rKr",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "548e2f65-78bf-491e-9c3f-9a072283afb0",
      "currency" : "USD",
      "application" : "APgD91hb3sYVdLTC7BQSM5i3",
      "source" : "PIh3yRBquQ7EXdXab9cURoFg",
      "destination" : "PI6hLTWquFArQehngU5YJrka",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T04:36:01.91Z",
      "updated_at" : "2016-11-15T04:36:02.15Z",
      "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRxhkUeCCNTg9csnd3Ub6rKr/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka"
        }
      }
    }, {
      "id" : "TRvSAH5kzUqtvLwqH9CXQRF7",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c45f0ed0-2484-43f5-9bfb-5208bc81daff",
      "currency" : "USD",
      "application" : "APgD91hb3sYVdLTC7BQSM5i3",
      "source" : "PI6hLTWquFArQehngU5YJrka",
      "destination" : "PIh3yRBquQ7EXdXab9cURoFg",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T04:35:59.94Z",
      "updated_at" : "2016-11-15T04:36:00.30Z",
      "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRvSAH5kzUqtvLwqH9CXQRF7"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRvSAH5kzUqtvLwqH9CXQRF7/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
        }
      }
    }, {
      "id" : "TRaFEHTBXRaYqXdFTuJjgpQE",
      "amount" : 275655,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "ae15c58c-321d-4643-baee-62474508c6f8",
      "currency" : "USD",
      "application" : "APgD91hb3sYVdLTC7BQSM5i3",
      "source" : "PIh3yRBquQ7EXdXab9cURoFg",
      "destination" : "PI6hLTWquFArQehngU5YJrka",
      "ready_to_settle_at" : null,
      "fee" : 27566,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T04:35:56.51Z",
      "updated_at" : "2016-11-15T04:36:00.15Z",
      "merchant_identity" : "IDwpfuevovRvifZXEPgY4VSD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwpfuevovRvifZXEPgY4VSD"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRaFEHTBXRaYqXdFTuJjgpQE/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIh3yRBquQ7EXdXab9cURoFg"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6hLTWquFArQehngU5YJrka"
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
    "count" : 4
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
    -u USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
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
  "id" : "WHosScQxNpHetjkruykcrCUE",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgD91hb3sYVdLTC7BQSM5i3",
  "created_at" : "2016-11-15T04:35:43.98Z",
  "updated_at" : "2016-11-15T04:35:43.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHosScQxNpHetjkruykcrCUE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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



curl https://api-staging.finix.io/webhooks/WHosScQxNpHetjkruykcrCUE \
    -H "Content-Type: application/vnd.json+api" \
    -u USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHosScQxNpHetjkruykcrCUE");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHosScQxNpHetjkruykcrCUE');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHosScQxNpHetjkruykcrCUE")

```
> Example Response:

```json
{
  "id" : "WHosScQxNpHetjkruykcrCUE",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APgD91hb3sYVdLTC7BQSM5i3",
  "created_at" : "2016-11-15T04:35:43.98Z",
  "updated_at" : "2016-11-15T04:35:43.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHosScQxNpHetjkruykcrCUE"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
    -u  USoDReh5TNALwVGL3Xzu6SbA:089536c0-4dd2-4205-a207-1ed0dc9909af

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "WHosScQxNpHetjkruykcrCUE",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APgD91hb3sYVdLTC7BQSM5i3",
      "created_at" : "2016-11-15T04:35:43.98Z",
      "updated_at" : "2016-11-15T04:35:43.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHosScQxNpHetjkruykcrCUE"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APgD91hb3sYVdLTC7BQSM5i3"
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'USoDReh5TNALwVGL3Xzu6SbA', '089536c0-4dd2-4205-a207-1ed0dc9909af');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

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
