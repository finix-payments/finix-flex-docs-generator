---
title: Finix API Reference

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

4. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install finix

import finix

from finix.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USdFDtpR8HojqbBcrfzdyyy", "714d9c23-3113-4b78-8782-9bdc50564048"))

```
To communicate with the Finix API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USdFDtpR8HojqbBcrfzdyyy`

- Password: `714d9c23-3113-4b78-8782-9bdc50564048`

- Application ID: `APvD23kEHLoWkekhUPL4oqFz`

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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
	        "default_statement_descriptor": "Golds Gym", 
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
	        "doing_business_as": "Golds Gym", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Golds Gym", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.GoldsGym.com", 
	        "annual_card_volume": 12000000
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

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
	        "default_statement_descriptor"=> "Golds Gym", 
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
	        "doing_business_as"=> "Golds Gym", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Golds Gym", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.GoldsGym.com", 
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
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Golds Gym", 
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
	        "doing_business_as": "Golds Gym", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Golds Gym", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.GoldsGym.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Golds Gym",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-15T03:32:36.05Z",
  "updated_at" : "2016-11-15T03:32:36.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'


```
```java
import io.finix.payments.processing.client.model.BankAccount;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

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
	    "identity"=> "ID4FwZq4RPYdv2Uj983BDGUu"
	));
$bank_account = $bank_account->save();

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
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIo4V49KZE94HfNMYyrp2BQj",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:32:46.26Z",
  "updated_at" : "2016-11-15T03:32:46.26Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "verification" : "VInaCK7wdgvP56p62WuHd3vo",
  "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:32:49.01Z",
  "updated_at" : "2016-11-15T03:32:49.01Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VInaCK7wdgvP56p62WuHd3vo"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Daphne", 
	        "last_name": "Henderson", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Daphne", 
	        "last_name"=> "Henderson", 
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


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Daphne", 
	        "last_name": "Henderson", 
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
  "id" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
  "entity" : {
    "title" : null,
    "first_name" : "Daphne",
    "last_name" : "Henderson",
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
  "created_at" : "2016-11-15T03:32:50.26Z",
  "updated_at" : "2016-11-15T03:32:50.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "name": "Jim Chang", 
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
	    "identity": "IDuDG3Y5sAKsNmVZyKhYvHzi"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Jim Chang", 
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
	    "identity"=> "IDuDG3Y5sAKsNmVZyKhYvHzi"
	));
$card = $card->save();


```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Jim Chang", 
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
	    "identity": "IDuDG3Y5sAKsNmVZyKhYvHzi"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "fingerprint" : "FPR-1839138016",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jim Chang",
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
  "created_at" : "2016-11-15T03:32:50.89Z",
  "updated_at" : "2016-11-15T03:32:50.89Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/updates"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "merchant_identity": "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIxdcx2opRkRL6gazhg7ZGrF", 
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
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIxdcx2opRkRL6gazhg7ZGrF", 
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
	    "merchant_identity": "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIxdcx2opRkRL6gazhg7ZGrF", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUh6oGFxxDuQAskzbgLueKbz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:57.31Z",
  "updated_at" : "2016-11-15T03:32:57.32Z",
  "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:32:57.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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
curl https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh6oGFxxDuQAskzbgLueKbz");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUh6oGFxxDuQAskzbgLueKbz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUh6oGFxxDuQAskzbgLueKbz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUh6oGFxxDuQAskzbgLueKbz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRkQdH8ZruyJ894WAHBamFsE",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:57.17Z",
  "updated_at" : "2016-11-15T03:32:59.15Z",
  "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:32:57.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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
curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
)

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```python


from finix.resources import Identity
from finix.resources import Settlement

identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
> Example Response:

```json
{
  "id" : "STvMaxeJTVYhcnS4bztuRQUn",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:40:07.17Z",
  "updated_at" : "2016-11-15T03:40:07.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=debit"
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

## Embedded Tokenization Using Iframe

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
          applicationId: 'APvD23kEHLoWkekhUPL4oqFz',
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
  "id" : "TKa3i5yps3ZUXc7QZrWLaKoL",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:33:00.78Z",
  "updated_at" : "2016-11-15T03:33:00.78Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:33:00.78Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	});
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIa3i5yps3ZUXc7QZrWLaKoL",
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
  "created_at" : "2016-11-15T03:33:01.47Z",
  "updated_at" : "2016-11-15T03:33:01.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/updates"
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


## Push-to-Card
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDcfXcf85H91nALSFa4Zw6y9",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-15T03:33:10.87Z",
  "updated_at" : "2016-11-15T03:33:10.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "name": "Fran Curry", 
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
	    "identity": "IDcfXcf85H91nALSFa4Zw6y9"
	}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USdFDtpR8HojqbBcrfzdyyy", 
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
> Example Response:

```json
{
  "id" : "PIpoQpP7oPnYpMrBtDoJBQ6C",
  "fingerprint" : "FPR-285253272",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Curry",
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
  "created_at" : "2016-11-15T03:33:11.38Z",
  "updated_at" : "2016-11-15T03:33:11.38Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcfXcf85H91nALSFa4Zw6y9",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/updates"
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
curl https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "MUr4Won7TG2uZH17CprqhsMw",
  "identity" : "IDcfXcf85H91nALSFa4Zw6y9",
  "verification" : "VInMn2M3EQH32EMs5AJhT85Z",
  "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:33:14.29Z",
  "updated_at" : "2016-11-15T03:33:14.29Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUr4Won7TG2uZH17CprqhsMw"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUr4Won7TG2uZH17CprqhsMw/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VInMn2M3EQH32EMs5AJhT85Z"
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
    -u USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDcfXcf85H91nALSFa4Zw6y9", 
	    "destination": "PIpoQpP7oPnYpMrBtDoJBQ6C", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USdFDtpR8HojqbBcrfzdyyy", 
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
> Example Response:

```json
{
  "id" : "TR6PiL7K5ER9WUHTc4ma3zqX",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "91532",
  "currency" : "USD",
  "application" : "APvD23kEHLoWkekhUPL4oqFz",
  "source" : "PI5je4yCukwQvMwpesrmjC83",
  "destination" : "PIpoQpP7oPnYpMrBtDoJBQ6C",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:33:12.52Z",
  "updated_at" : "2016-11-15T03:33:13.57Z",
  "merchant_identity" : "IDhVY95jK59jzykWDTFnFjRn",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C"
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
    server: "https://api-staging.finix.io",
    applicationId: "APvD23kEHLoWkekhUPL4oqFz",
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
  "id" : "TKa3i5yps3ZUXc7QZrWLaKoL",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:33:00.78Z",
  "updated_at" : "2016-11-15T03:33:00.78Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:33:00.78Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	});
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIa3i5yps3ZUXc7QZrWLaKoL",
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
  "created_at" : "2016-11-15T03:33:01.47Z",
  "updated_at" : "2016-11-15T03:33:01.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/updates"
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


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "merchant_identity": "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIxdcx2opRkRL6gazhg7ZGrF", 
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
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIxdcx2opRkRL6gazhg7ZGrF", 
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
	    "merchant_identity": "ID4FwZq4RPYdv2Uj983BDGUu", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIxdcx2opRkRL6gazhg7ZGrF", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUh6oGFxxDuQAskzbgLueKbz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:57.31Z",
  "updated_at" : "2016-11-15T03:32:57.32Z",
  "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:32:57.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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
curl https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh6oGFxxDuQAskzbgLueKbz");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUh6oGFxxDuQAskzbgLueKbz');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUh6oGFxxDuQAskzbgLueKbz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUh6oGFxxDuQAskzbgLueKbz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRkQdH8ZruyJ894WAHBamFsE",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:57.17Z",
  "updated_at" : "2016-11-15T03:32:59.15Z",
  "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:32:57.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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

curl https://api-staging.finix.io/authorizations/AUie4nS1BMyDRKeA2xk5irA5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUh6oGFxxDuQAskzbgLueKbz")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AUie4nS1BMyDRKeA2xk5irA5",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:33:02.20Z",
  "updated_at" : "2016-11-15T03:33:03.09Z",
  "trace_id" : "e4f962cc-12b5-457e-bf13-9fb1dee364b0",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : true,
  "expires_at" : "2016-11-22T03:33:02.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUie4nS1BMyDRKeA2xk5irA5"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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

curl https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh6oGFxxDuQAskzbgLueKbz");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUh6oGFxxDuQAskzbgLueKbz');

```
```python


from finix.resources import Authorization

authorization = Authorization.get(id="AUh6oGFxxDuQAskzbgLueKbz")
```
> Example Response:

```json
{
  "id" : "AUh6oGFxxDuQAskzbgLueKbz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRkQdH8ZruyJ894WAHBamFsE",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:57.17Z",
  "updated_at" : "2016-11-15T03:32:59.15Z",
  "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:32:57.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Authorization

authorization = Authorization.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUie4nS1BMyDRKeA2xk5irA5",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:33:02.20Z",
      "updated_at" : "2016-11-15T03:33:03.09Z",
      "trace_id" : "e4f962cc-12b5-457e-bf13-9fb1dee364b0",
      "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "is_void" : true,
      "expires_at" : "2016-11-22T03:33:02.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUie4nS1BMyDRKeA2xk5irA5"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        }
      }
    }, {
      "id" : "AUh6oGFxxDuQAskzbgLueKbz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRkQdH8ZruyJ894WAHBamFsE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:32:57.17Z",
      "updated_at" : "2016-11-15T03:32:59.15Z",
      "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
      "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "is_void" : false,
      "expires_at" : "2016-11-22T03:32:57.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUh6oGFxxDuQAskzbgLueKbz"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Daphne", 
	        "last_name": "Henderson", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Daphne", 
	        "last_name"=> "Henderson", 
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


from finix.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Daphne", 
	        "last_name": "Henderson", 
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
  "id" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
  "entity" : {
    "title" : null,
    "first_name" : "Daphne",
    "last_name" : "Henderson",
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
  "created_at" : "2016-11-15T03:32:50.26Z",
  "updated_at" : "2016-11-15T03:32:50.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
	        "default_statement_descriptor": "Golds Gym", 
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
	        "doing_business_as": "Golds Gym", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Golds Gym", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.GoldsGym.com", 
	        "annual_card_volume": 12000000
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

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
	        "default_statement_descriptor"=> "Golds Gym", 
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
	        "doing_business_as"=> "Golds Gym", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Golds Gym", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.GoldsGym.com", 
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
	        "key": "value"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "amex_mid": "12345678910", 
	        "max_transaction_amount": 120000, 
	        "has_accepted_credit_cards_previously": True, 
	        "default_statement_descriptor": "Golds Gym", 
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
	        "doing_business_as": "Golds Gym", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Golds Gym", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.GoldsGym.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Golds Gym",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-15T03:32:36.05Z",
  "updated_at" : "2016-11-15T03:32:36.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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

curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID4FwZq4RPYdv2Uj983BDGUu");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');
```
```python


from finix.resources import Identity
identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")

```
> Example Response:

```json
{
  "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Golds Gym",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-15T03:32:35.99Z",
  "updated_at" : "2016-11-15T03:32:35.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048


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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Identity
identity = Identity.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcfXcf85H91nALSFa4Zw6y9",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:33:10.81Z",
      "updated_at" : "2016-11-15T03:33:10.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
      "entity" : {
        "title" : null,
        "first_name" : "Daphne",
        "last_name" : "Henderson",
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
      "created_at" : "2016-11-15T03:32:50.20Z",
      "updated_at" : "2016-11-15T03:32:50.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDeTaGF1qdRY6abteyN1b6Jx",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:45.60Z",
      "updated_at" : "2016-11-15T03:32:45.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID9jMRoBKEANyJnBersYgBq9",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-15T03:32:44.90Z",
      "updated_at" : "2016-11-15T03:32:44.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDfkMnmTY1dfXCvR2Lf4TTtb",
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
      "created_at" : "2016-11-15T03:32:43.20Z",
      "updated_at" : "2016-11-15T03:32:43.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID4tzTuoAtY7fLau4ge6M5jg",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-15T03:32:42.65Z",
      "updated_at" : "2016-11-15T03:32:42.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDiiRqmszUSn3vbv3SNc4Hbz",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:41.26Z",
      "updated_at" : "2016-11-15T03:32:41.26Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDn1P5c4Vi4rj73vyMgWVE2W",
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
      "created_at" : "2016-11-15T03:32:38.89Z",
      "updated_at" : "2016-11-15T03:32:38.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDcpcbeRcMLex54deFmszPjx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:32:38.07Z",
      "updated_at" : "2016-11-15T03:32:38.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDsKde6jRDtQ2TJrQxM2cKp8",
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
      "created_at" : "2016-11-15T03:32:37.36Z",
      "updated_at" : "2016-11-15T03:32:37.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDsRbLLfVAhH1Zvc4BXsw4v1",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:36.54Z",
      "updated_at" : "2016-11-15T03:32:36.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-15T03:32:35.99Z",
      "updated_at" : "2016-11-15T03:32:35.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDhVY95jK59jzykWDTFnFjRn",
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
        "application_name" : "Square"
      },
      "created_at" : "2016-11-15T03:32:32.29Z",
      "updated_at" : "2016-11-15T03:32:32.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Jessie", 
	        "last_name": "Diaz", 
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Jessie",
    "last_name" : "Diaz",
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
  "created_at" : "2016-11-15T03:32:35.99Z",
  "updated_at" : "2016-11-15T03:33:24.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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

curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '


```
```java

import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );
```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "verification" : "VInaCK7wdgvP56p62WuHd3vo",
  "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:32:49.01Z",
  "updated_at" : "2016-11-15T03:32:49.01Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VInaCK7wdgvP56p62WuHd3vo"
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
curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from finix.resources import Identity
from finix.resources import Merchant

identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "verification" : "VInaCK7wdgvP56p62WuHd3vo",
  "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:32:49.01Z",
  "updated_at" : "2016-11-15T03:32:49.01Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VInaCK7wdgvP56p62WuHd3vo"
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
curl https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java
import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU5L7BCaffkMJiVKNf557UF7");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Merchant;

$merchant = Merchant::retrieve('MU5L7BCaffkMJiVKNf557UF7');

```
```python


from finix.resources import Merchant
merchant = Merchant.get(id="MU5L7BCaffkMJiVKNf557UF7")

```
> Example Response:

```json
{
  "id" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "verification" : null,
  "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-15T03:32:48.80Z",
  "updated_at" : "2016-11-15T03:32:49.15Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USefJX6hHsvShke35XSTs478",
  "password" : "d5e2727a-164f-4976-913f-8355fc6460e3",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-15T03:32:54.05Z",
  "updated_at" : "2016-11-15T03:32:54.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USefJX6hHsvShke35XSTs478"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VImVvxTd5L3jopX1icLTapqz",
  "external_trace_id" : "b7775132-b18f-445d-a74d-1424d70a7c0b",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T03:33:26.24Z",
  "updated_at" : "2016-11-15T03:33:26.29Z",
  "payment_instrument" : null,
  "merchant" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImVvxTd5L3jopX1icLTapqz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
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
curl https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VImVvxTd5L3jopX1icLTapqz",
  "external_trace_id" : "b7775132-b18f-445d-a74d-1424d70a7c0b",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T03:33:26.24Z",
  "updated_at" : "2016-11-15T03:33:26.29Z",
  "payment_instrument" : null,
  "merchant" : "MU5L7BCaffkMJiVKNf557UF7",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImVvxTd5L3jopX1icLTapqz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Merchant
merchant = Merchant.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUr4Won7TG2uZH17CprqhsMw",
      "identity" : "IDcfXcf85H91nALSFa4Zw6y9",
      "verification" : null,
      "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-15T03:33:14.21Z",
      "updated_at" : "2016-11-15T03:33:14.21Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUr4Won7TG2uZH17CprqhsMw"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUr4Won7TG2uZH17CprqhsMw/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "MU5L7BCaffkMJiVKNf557UF7",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "verification" : null,
      "merchant_profile" : "MPqpGiKdoPjGZr9MiERnNZqn",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-15T03:32:48.80Z",
      "updated_at" : "2016-11-15T03:32:49.15Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPqpGiKdoPjGZr9MiERnNZqn"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/merchants/MU5L7BCaffkMJiVKNf557UF7/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcfXcf85H91nALSFa4Zw6y9",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:33:10.81Z",
      "updated_at" : "2016-11-15T03:33:10.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
      "entity" : {
        "title" : null,
        "first_name" : "Daphne",
        "last_name" : "Henderson",
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
      "created_at" : "2016-11-15T03:32:50.20Z",
      "updated_at" : "2016-11-15T03:32:50.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDeTaGF1qdRY6abteyN1b6Jx",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:45.60Z",
      "updated_at" : "2016-11-15T03:32:45.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeTaGF1qdRY6abteyN1b6Jx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID9jMRoBKEANyJnBersYgBq9",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-15T03:32:44.90Z",
      "updated_at" : "2016-11-15T03:32:44.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9jMRoBKEANyJnBersYgBq9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDfkMnmTY1dfXCvR2Lf4TTtb",
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
      "created_at" : "2016-11-15T03:32:43.20Z",
      "updated_at" : "2016-11-15T03:32:43.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfkMnmTY1dfXCvR2Lf4TTtb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID4tzTuoAtY7fLau4ge6M5jg",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-15T03:32:42.65Z",
      "updated_at" : "2016-11-15T03:32:42.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4tzTuoAtY7fLau4ge6M5jg/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDiiRqmszUSn3vbv3SNc4Hbz",
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
        "mcc" : 742,
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:41.26Z",
      "updated_at" : "2016-11-15T03:32:41.26Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiiRqmszUSn3vbv3SNc4Hbz/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDn1P5c4Vi4rj73vyMgWVE2W",
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
      "created_at" : "2016-11-15T03:32:38.89Z",
      "updated_at" : "2016-11-15T03:32:38.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDn1P5c4Vi4rj73vyMgWVE2W/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDcpcbeRcMLex54deFmszPjx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:32:38.07Z",
      "updated_at" : "2016-11-15T03:32:38.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcpcbeRcMLex54deFmszPjx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDsKde6jRDtQ2TJrQxM2cKp8",
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
      "created_at" : "2016-11-15T03:32:37.36Z",
      "updated_at" : "2016-11-15T03:32:37.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsKde6jRDtQ2TJrQxM2cKp8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDsRbLLfVAhH1Zvc4BXsw4v1",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:32:36.54Z",
      "updated_at" : "2016-11-15T03:32:36.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsRbLLfVAhH1Zvc4BXsw4v1/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-15T03:32:35.99Z",
      "updated_at" : "2016-11-15T03:32:35.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "IDhVY95jK59jzykWDTFnFjRn",
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
        "application_name" : "Square"
      },
      "created_at" : "2016-11-15T03:32:32.29Z",
      "updated_at" : "2016-11-15T03:32:32.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "name": "Jim Chang", 
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
	    "identity": "IDuDG3Y5sAKsNmVZyKhYvHzi"
	}'


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Jim Chang", 
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
	    "identity"=> "IDuDG3Y5sAKsNmVZyKhYvHzi"
	));
$card = $card->save();


```
```python


from finix.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Jim Chang", 
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
	    "identity": "IDuDG3Y5sAKsNmVZyKhYvHzi"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "fingerprint" : "FPR-1839138016",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Jim Chang",
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
  "created_at" : "2016-11-15T03:32:50.89Z",
  "updated_at" : "2016-11-15T03:32:50.89Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/updates"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'


```
```java

import io.finix.payments.processing.client.model.BankAccount;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

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
	    "identity"=> "ID4FwZq4RPYdv2Uj983BDGUu"
	));
$bank_account = $bank_account->save();


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
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIo4V49KZE94HfNMYyrp2BQj",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:32:46.26Z",
  "updated_at" : "2016-11-15T03:32:46.26Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
          applicationId: 'APvD23kEHLoWkekhUPL4oqFz',
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
  "id" : "TKa3i5yps3ZUXc7QZrWLaKoL",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:33:00.78Z",
  "updated_at" : "2016-11-15T03:33:00.78Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:33:00.78Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'

```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIa3i5yps3ZUXc7QZrWLaKoL",
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
  "created_at" : "2016-11-15T03:33:01.47Z",
  "updated_at" : "2016-11-15T03:33:01.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/updates"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
    -d '
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}'


```
```java
import io.finix.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	});
$card = $card->save();

```
```python


from finix.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKa3i5yps3ZUXc7QZrWLaKoL", 
	    "type": "TOKEN", 
	    "identity": "ID4FwZq4RPYdv2Uj983BDGUu"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIa3i5yps3ZUXc7QZrWLaKoL",
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
  "created_at" : "2016-11-15T03:33:01.47Z",
  "updated_at" : "2016-11-15T03:33:01.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/updates"
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


curl https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \

```
```java

import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIo4V49KZE94HfNMYyrp2BQj")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIo4V49KZE94HfNMYyrp2BQj');

```
```python



```
> Example Response:

```json
{
  "id" : "PIo4V49KZE94HfNMYyrp2BQj",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:32:46.16Z",
  "updated_at" : "2016-11-15T03:32:46.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
curl https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PIo4V49KZE94HfNMYyrp2BQj",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:32:46.16Z",
  "updated_at" : "2016-11-15T03:32:46.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIpoQpP7oPnYpMrBtDoJBQ6C",
      "fingerprint" : "FPR-285253272",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Fran Curry",
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
      "created_at" : "2016-11-15T03:33:11.31Z",
      "updated_at" : "2016-11-15T03:33:11.31Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDcfXcf85H91nALSFa4Zw6y9",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcfXcf85H91nALSFa4Zw6y9"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C/updates"
        }
      }
    }, {
      "id" : "PIfFDV7wH7aWWUBPdo7MEkMT",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:33:09.27Z",
      "updated_at" : "2016-11-15T03:33:09.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfFDV7wH7aWWUBPdo7MEkMT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfFDV7wH7aWWUBPdo7MEkMT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfFDV7wH7aWWUBPdo7MEkMT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfFDV7wH7aWWUBPdo7MEkMT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PI5je4yCukwQvMwpesrmjC83",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:33:09.27Z",
      "updated_at" : "2016-11-15T03:33:09.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIeCWMmsKe6JEGLpwPRZTbwZ",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:33:09.27Z",
      "updated_at" : "2016-11-15T03:33:09.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeCWMmsKe6JEGLpwPRZTbwZ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeCWMmsKe6JEGLpwPRZTbwZ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeCWMmsKe6JEGLpwPRZTbwZ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeCWMmsKe6JEGLpwPRZTbwZ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PI4ifCkhv5W4Zh3Uo2XfXzo6",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:33:09.27Z",
      "updated_at" : "2016-11-15T03:33:09.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4ifCkhv5W4Zh3Uo2XfXzo6"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4ifCkhv5W4Zh3Uo2XfXzo6/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4ifCkhv5W4Zh3Uo2XfXzo6/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4ifCkhv5W4Zh3Uo2XfXzo6/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIa3i5yps3ZUXc7QZrWLaKoL",
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
      "created_at" : "2016-11-15T03:33:01.30Z",
      "updated_at" : "2016-11-15T03:33:01.30Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIa3i5yps3ZUXc7QZrWLaKoL/updates"
        }
      }
    }, {
      "id" : "PI4GCsAMRrGyfxabHs5sNRzP",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T03:32:52.35Z",
      "updated_at" : "2016-11-15T03:32:52.35Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4GCsAMRrGyfxabHs5sNRzP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4GCsAMRrGyfxabHs5sNRzP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4GCsAMRrGyfxabHs5sNRzP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4GCsAMRrGyfxabHs5sNRzP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "fingerprint" : "FPR-1839138016",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Jim Chang",
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
      "created_at" : "2016-11-15T03:32:50.81Z",
      "updated_at" : "2016-11-15T03:32:57.32Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDuDG3Y5sAKsNmVZyKhYvHzi",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuDG3Y5sAKsNmVZyKhYvHzi"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF/updates"
        }
      }
    }, {
      "id" : "PIryhJBzwEXVwczHHu1tyW1a",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:48.80Z",
      "updated_at" : "2016-11-15T03:32:48.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIryhJBzwEXVwczHHu1tyW1a"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIryhJBzwEXVwczHHu1tyW1a/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIryhJBzwEXVwczHHu1tyW1a/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIryhJBzwEXVwczHHu1tyW1a/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIig16Lt6UPYehW2Urr53UcP",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:48.80Z",
      "updated_at" : "2016-11-15T03:32:48.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIig16Lt6UPYehW2Urr53UcP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIig16Lt6UPYehW2Urr53UcP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIig16Lt6UPYehW2Urr53UcP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIig16Lt6UPYehW2Urr53UcP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PI3MDS634myBVwHD8iSRy1CP",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:48.80Z",
      "updated_at" : "2016-11-15T03:32:48.80Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIo4V49KZE94HfNMYyrp2BQj",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T03:32:46.16Z",
      "updated_at" : "2016-11-15T03:32:46.95Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIbZAZUxG9ybHuYSvU7aBkNA",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:32.87Z",
      "updated_at" : "2016-11-15T03:32:32.87Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbZAZUxG9ybHuYSvU7aBkNA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbZAZUxG9ybHuYSvU7aBkNA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbZAZUxG9ybHuYSvU7aBkNA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbZAZUxG9ybHuYSvU7aBkNA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIwncyaDxrWY2mRN8vzAGyfX",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:32.87Z",
      "updated_at" : "2016-11-15T03:32:32.87Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwncyaDxrWY2mRN8vzAGyfX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwncyaDxrWY2mRN8vzAGyfX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwncyaDxrWY2mRN8vzAGyfX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwncyaDxrWY2mRN8vzAGyfX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PI4vQ1YBuWADRkXVCty62ThX",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:32.87Z",
      "updated_at" : "2016-11-15T03:32:32.87Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4vQ1YBuWADRkXVCty62ThX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4vQ1YBuWADRkXVCty62ThX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4vQ1YBuWADRkXVCty62ThX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4vQ1YBuWADRkXVCty62ThX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        }
      }
    }, {
      "id" : "PIrr3VADYCwkLWTTYrAs5DcV",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:32:32.87Z",
      "updated_at" : "2016-11-15T03:32:32.87Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrr3VADYCwkLWTTYrAs5DcV"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrr3VADYCwkLWTTYrAs5DcV/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrr3VADYCwkLWTTYrAs5DcV/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrr3VADYCwkLWTTYrAs5DcV/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
)

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('ID4FwZq4RPYdv2Uj983BDGUu');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```python


from finix.resources import Identity
from finix.resources import Settlement

identity = Identity.get(id="ID4FwZq4RPYdv2Uj983BDGUu")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
> Example Response:

```json
{
  "id" : "STvMaxeJTVYhcnS4bztuRQUn",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:40:07.17Z",
  "updated_at" : "2016-11-15T03:40:07.18Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STvMaxeJTVYhcnS4bztuRQUn");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STvMaxeJTVYhcnS4bztuRQUn');

```
```python



```
> Example Response:

```json
{
  "id" : "STvMaxeJTVYhcnS4bztuRQUn",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:40:07.06Z",
  "updated_at" : "2016-11-15T03:40:08.36Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PIo4V49KZE94HfNMYyrp2BQj",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=debit"
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


## Fund a Settlement
```shell
curl https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "destination": "PIo4V49KZE94HfNMYyrp2BQj"
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "STvMaxeJTVYhcnS4bztuRQUn",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:40:07.06Z",
  "updated_at" : "2016-11-15T03:40:08.36Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PIo4V49KZE94HfNMYyrp2BQj",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=debit"
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

`PUT https://api-staging.finix.io/settlements/:SETTLEMENT_ID`

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
curl https://api-staging.finix.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Settlement
settlements = Settlement.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STvMaxeJTVYhcnS4bztuRQUn",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "currency" : "USD",
      "created_at" : "2016-11-15T03:40:07.06Z",
      "updated_at" : "2016-11-15T03:40:08.36Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 100,
      "total_fees" : 11,
      "total_fee" : 11,
      "net_amount" : 89,
      "destination" : "PIo4V49KZE94HfNMYyrp2BQj",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRapVLp4aYAMZ7tNna99v8ri",
      "amount" : 89,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "b8d9e6bc-4080-4598-80f3-38e80c0d99b8",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PI3MDS634myBVwHD8iSRy1CP",
      "destination" : "PIo4V49KZE94HfNMYyrp2BQj",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "SETTLEMENT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:08.07Z",
      "updated_at" : "2016-11-15T03:40:08.26Z",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRapVLp4aYAMZ7tNna99v8ri"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRapVLp4aYAMZ7tNna99v8ri/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRapVLp4aYAMZ7tNna99v8ri/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRapVLp4aYAMZ7tNna99v8ri/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRapVLp4aYAMZ7tNna99v8ri/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIo4V49KZE94HfNMYyrp2BQj"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR7YjHSmwqdYof68F5zenyjY",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "bb9f28ce-df52-4105-86ef-1f530d26c26f",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PI3MDS634myBVwHD8iSRy1CP",
      "destination" : "PI4vQ1YBuWADRkXVCty62ThX",
      "ready_to_settle_at" : "2016-11-15T03:35:14.63Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:36:05.50Z",
      "updated_at" : "2016-11-15T03:36:07.58Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR7YjHSmwqdYof68F5zenyjY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR7YjHSmwqdYof68F5zenyjY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR7YjHSmwqdYof68F5zenyjY/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR7YjHSmwqdYof68F5zenyjY/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR7YjHSmwqdYof68F5zenyjY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4vQ1YBuWADRkXVCty62ThX"
        }
      }
    }, {
      "id" : "TRkQdH8ZruyJ894WAHBamFsE",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "destination" : "PI3MDS634myBVwHD8iSRy1CP",
      "ready_to_settle_at" : "2016-11-15T03:35:14.63Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:32:58.92Z",
      "updated_at" : "2016-11-15T03:33:53.76Z",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STvMaxeJTVYhcnS4bztuRQUn/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 2
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

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048


```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRdic84Ms2URRb9mzRquSoJg");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRdic84Ms2URRb9mzRquSoJg');



```
```python


from finix.resources import Transfer
transfer = Transfer.get(id="TRdic84Ms2URRb9mzRquSoJg")

```
> Example Response:

```json
{
  "id" : "TRdic84Ms2URRb9mzRquSoJg",
  "amount" : 13363,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "ec680343-3b5b-4fb1-87df-9fbe06727160",
  "currency" : "USD",
  "application" : "APvD23kEHLoWkekhUPL4oqFz",
  "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "destination" : "PI3MDS634myBVwHD8iSRy1CP",
  "ready_to_settle_at" : null,
  "fee" : 1336,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:53.15Z",
  "updated_at" : "2016-11-15T03:32:56.16Z",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
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

curl https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TRdic84Ms2URRb9mzRquSoJg');
$refund = $debit->reverse(50);
```
```python


from finix.resources import Transfer

transfer = Transfer.get(id="TRdic84Ms2URRb9mzRquSoJg")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TR9g7taHAAABNfAGZeLEMs8J",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "42e5408b-5efe-48cb-be01-860c9ed89410",
  "currency" : "USD",
  "application" : "APvD23kEHLoWkekhUPL4oqFz",
  "source" : "PI3MDS634myBVwHD8iSRy1CP",
  "destination" : "PIxdcx2opRkRL6gazhg7ZGrF",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:32:56.21Z",
  "updated_at" : "2016-11-15T03:32:56.30Z",
  "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR9g7taHAAABNfAGZeLEMs8J"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR9g7taHAAABNfAGZeLEMs8J/payment_instruments"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Transfer
transfer = Transfer.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR6PiL7K5ER9WUHTc4ma3zqX",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "91532",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PI5je4yCukwQvMwpesrmjC83",
      "destination" : "PIpoQpP7oPnYpMrBtDoJBQ6C",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:33:12.31Z",
      "updated_at" : "2016-11-15T03:33:13.57Z",
      "merchant_identity" : "IDhVY95jK59jzykWDTFnFjRn",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDhVY95jK59jzykWDTFnFjRn"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR6PiL7K5ER9WUHTc4ma3zqX/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5je4yCukwQvMwpesrmjC83"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpoQpP7oPnYpMrBtDoJBQ6C"
        }
      }
    }, {
      "id" : "TRkQdH8ZruyJ894WAHBamFsE",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "03741424-922b-4b49-a04b-c72ce725e53e",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "destination" : "PI3MDS634myBVwHD8iSRy1CP",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:32:58.92Z",
      "updated_at" : "2016-11-15T03:32:59.15Z",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRkQdH8ZruyJ894WAHBamFsE/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
        }
      }
    }, {
      "id" : "TR9g7taHAAABNfAGZeLEMs8J",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "29dd0e3b-8c43-410d-bf04-cf2ff68fb63e",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PI3MDS634myBVwHD8iSRy1CP",
      "destination" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:32:55.95Z",
      "updated_at" : "2016-11-15T03:32:56.30Z",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR9g7taHAAABNfAGZeLEMs8J"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR9g7taHAAABNfAGZeLEMs8J/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
        }
      }
    }, {
      "id" : "TRdic84Ms2URRb9mzRquSoJg",
      "amount" : 13363,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "ec680343-3b5b-4fb1-87df-9fbe06727160",
      "currency" : "USD",
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "source" : "PIxdcx2opRkRL6gazhg7ZGrF",
      "destination" : "PI3MDS634myBVwHD8iSRy1CP",
      "ready_to_settle_at" : null,
      "fee" : 1336,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:32:53.15Z",
      "updated_at" : "2016-11-15T03:32:56.16Z",
      "merchant_identity" : "ID4FwZq4RPYdv2Uj983BDGUu",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID4FwZq4RPYdv2Uj983BDGUu"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRdic84Ms2URRb9mzRquSoJg/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxdcx2opRkRL6gazhg7ZGrF"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3MDS634myBVwHD8iSRy1CP"
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
    -u USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048 \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
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
> Example Response:

```json
{
  "id" : "WH8fYXYdXhjnamjzQDWAr3W",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvD23kEHLoWkekhUPL4oqFz",
  "created_at" : "2016-11-15T03:32:35.64Z",
  "updated_at" : "2016-11-15T03:32:35.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH8fYXYdXhjnamjzQDWAr3W"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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



curl https://api-staging.finix.io/webhooks/WH8fYXYdXhjnamjzQDWAr3W \
    -H "Content-Type: application/vnd.json+api" \
    -u USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048


```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH8fYXYdXhjnamjzQDWAr3W");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WH8fYXYdXhjnamjzQDWAr3W');



```
```python


from finix.resources import Webhook
webhook = Webhook.get(id="WH8fYXYdXhjnamjzQDWAr3W")

```
> Example Response:

```json
{
  "id" : "WH8fYXYdXhjnamjzQDWAr3W",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvD23kEHLoWkekhUPL4oqFz",
  "created_at" : "2016-11-15T03:32:35.64Z",
  "updated_at" : "2016-11-15T03:32:35.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH8fYXYdXhjnamjzQDWAr3W"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
    -u  USdFDtpR8HojqbBcrfzdyyy:714d9c23-3113-4b78-8782-9bdc50564048

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```python


from finix.resources import Webhook
webhooks = Webhook.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WH8fYXYdXhjnamjzQDWAr3W",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APvD23kEHLoWkekhUPL4oqFz",
      "created_at" : "2016-11-15T03:32:35.64Z",
      "updated_at" : "2016-11-15T03:32:35.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WH8fYXYdXhjnamjzQDWAr3W"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APvD23kEHLoWkekhUPL4oqFz"
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USdFDtpR8HojqbBcrfzdyyy', '714d9c23-3113-4b78-8782-9bdc50564048');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

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
