---
title: Payline API Reference

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

4. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("USfQ9LCUotNchB31PKbXdqir", "30141a9e-5338-4848-a24a-3ad12085e3dd"))

```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USfQ9LCUotNchB31PKbXdqir`

- Password: `30141a9e-5338-4848-a24a-3ad12085e3dd`

- Application ID: `APvFU1J7hgZjmewU9fkeUh8i`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** https://api-test.payline.io

- **Production API:** https://api.payline.io

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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


from payline.resources import Identity

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
  "id" : "IDaotf83HNxER4mu5gXAxJPV",
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
  "created_at" : "2016-11-15T03:40:22.38Z",
  "updated_at" : "2016-11-15T03:40:22.38Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'


```
```java
import io.payline.payments.processing.client.model.BankAccount;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "IDaotf83HNxER4mu5gXAxJPV"
	));
$bank_account = $bank_account->save();

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
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI485mr7uuJWRyTMVS8qpnBL",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:40:31.74Z",
  "updated_at" : "2016-11-15T03:40:31.74Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "verification" : "VIjap1EF2Kao7zYjd8wJybvg",
  "merchant_profile" : "MPsW9zxb7VANE2N1pF5kNPUX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:40:33.10Z",
  "updated_at" : "2016-11-15T03:40:33.10Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsW9zxb7VANE2N1pF5kNPUX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIjap1EF2Kao7zYjd8wJybvg"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Green", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
	        "last_name"=> "Green", 
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


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Green", 
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
  "id" : "ID9n1NEjjjCeurMoqLgwF8Nv",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
    "last_name" : "Green",
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
  "created_at" : "2016-11-15T03:40:34.51Z",
  "updated_at" : "2016-11-15T03:40:34.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "name": "Bob Henderson", 
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
	    "identity": "ID9n1NEjjjCeurMoqLgwF8Nv"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Bob Henderson", 
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
	    "identity"=> "ID9n1NEjjjCeurMoqLgwF8Nv"
	));
$card = $card->save();


```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Henderson", 
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
	    "identity": "ID9n1NEjjjCeurMoqLgwF8Nv"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIrNo8zuHEZoatYMcCPvkypT",
  "fingerprint" : "FPR-1778475544",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Henderson",
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
  "created_at" : "2016-11-15T03:40:35.02Z",
  "updated_at" : "2016-11-15T03:40:35.02Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID9n1NEjjjCeurMoqLgwF8Nv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/updates"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "merchant_identity": "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIrNo8zuHEZoatYMcCPvkypT", 
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
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIrNo8zuHEZoatYMcCPvkypT", 
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
	    "merchant_identity": "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIrNo8zuHEZoatYMcCPvkypT", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUtK245svn13rbnyQG2oYWQq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:40.60Z",
  "updated_at" : "2016-11-15T03:40:40.61Z",
  "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:40:40.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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
curl https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUtK245svn13rbnyQG2oYWQq");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUtK245svn13rbnyQG2oYWQq');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUtK245svn13rbnyQG2oYWQq")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUtK245svn13rbnyQG2oYWQq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR9STEP4F5uZeQJrXFUnwPjw",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:40.45Z",
  "updated_at" : "2016-11-15T03:40:41.42Z",
  "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:40:40.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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
curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
)

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```python


from payline.resources import Identity
from payline.resources import Settlement

identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")
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
  "id" : "STjT9iJhUzeJjjABXHPc9WB3",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:47:41.34Z",
  "updated_at" : "2016-11-15T03:47:41.35Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=debit"
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

## Embedded Tokenization Using Iframe

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
          applicationId: 'APvFU1J7hgZjmewU9fkeUh8i',
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
  "id" : "TK9E43itbiWv7TyGX3PFbvKc",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:40:42.77Z",
  "updated_at" : "2016-11-15T03:40:42.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:40:42.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI9E43itbiWv7TyGX3PFbvKc",
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
  "created_at" : "2016-11-15T03:40:43.28Z",
  "updated_at" : "2016-11-15T03:40:43.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/updates"
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
    applicationId: "APvFU1J7hgZjmewU9fkeUh8i",
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
  "id" : "TK9E43itbiWv7TyGX3PFbvKc",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:40:42.77Z",
  "updated_at" : "2016-11-15T03:40:42.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:40:42.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI9E43itbiWv7TyGX3PFbvKc",
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
  "created_at" : "2016-11-15T03:40:43.28Z",
  "updated_at" : "2016-11-15T03:40:43.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/updates"
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


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "merchant_identity": "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIrNo8zuHEZoatYMcCPvkypT", 
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
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIrNo8zuHEZoatYMcCPvkypT", 
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
	    "merchant_identity": "IDaotf83HNxER4mu5gXAxJPV", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIrNo8zuHEZoatYMcCPvkypT", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUtK245svn13rbnyQG2oYWQq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:40.60Z",
  "updated_at" : "2016-11-15T03:40:40.61Z",
  "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:40:40.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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
curl https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUtK245svn13rbnyQG2oYWQq");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUtK245svn13rbnyQG2oYWQq');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUtK245svn13rbnyQG2oYWQq")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUtK245svn13rbnyQG2oYWQq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR9STEP4F5uZeQJrXFUnwPjw",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:40.45Z",
  "updated_at" : "2016-11-15T03:40:41.42Z",
  "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:40:40.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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

curl https://api-test.payline.io/authorizations/AUn75LL2B6KbTcqX8HrByWNj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUtK245svn13rbnyQG2oYWQq")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AUn75LL2B6KbTcqX8HrByWNj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:45.26Z",
  "updated_at" : "2016-11-15T03:40:46.04Z",
  "trace_id" : "eb55947e-968e-4b20-a76d-a84e22053235",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : true,
  "expires_at" : "2016-11-22T03:40:45.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUn75LL2B6KbTcqX8HrByWNj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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

curl https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUtK245svn13rbnyQG2oYWQq");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUtK245svn13rbnyQG2oYWQq');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUtK245svn13rbnyQG2oYWQq")
```
> Example Response:

```json
{
  "id" : "AUtK245svn13rbnyQG2oYWQq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR9STEP4F5uZeQJrXFUnwPjw",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:40.45Z",
  "updated_at" : "2016-11-15T03:40:41.42Z",
  "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "is_void" : false,
  "expires_at" : "2016-11-22T03:40:40.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Authorization

authorization = Authorization.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUn75LL2B6KbTcqX8HrByWNj",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:45.26Z",
      "updated_at" : "2016-11-15T03:40:46.04Z",
      "trace_id" : "eb55947e-968e-4b20-a76d-a84e22053235",
      "source" : "PIrNo8zuHEZoatYMcCPvkypT",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "is_void" : true,
      "expires_at" : "2016-11-22T03:40:45.26Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUn75LL2B6KbTcqX8HrByWNj"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        }
      }
    }, {
      "id" : "AUtK245svn13rbnyQG2oYWQq",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR9STEP4F5uZeQJrXFUnwPjw",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:40.45Z",
      "updated_at" : "2016-11-15T03:40:41.42Z",
      "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
      "source" : "PIrNo8zuHEZoatYMcCPvkypT",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "is_void" : false,
      "expires_at" : "2016-11-22T03:40:40.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUtK245svn13rbnyQG2oYWQq"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Green", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
	        "last_name"=> "Green", 
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


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
	        "last_name": "Green", 
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
  "id" : "ID9n1NEjjjCeurMoqLgwF8Nv",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
    "last_name" : "Green",
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
  "created_at" : "2016-11-15T03:40:34.51Z",
  "updated_at" : "2016-11-15T03:40:34.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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


from payline.resources import Identity

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
  "id" : "IDaotf83HNxER4mu5gXAxJPV",
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
  "created_at" : "2016-11-15T03:40:22.38Z",
  "updated_at" : "2016-11-15T03:40:22.38Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDaotf83HNxER4mu5gXAxJPV");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');
```
```python


from payline.resources import Identity
identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")

```
> Example Response:

```json
{
  "id" : "IDaotf83HNxER4mu5gXAxJPV",
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
  "created_at" : "2016-11-15T03:40:22.32Z",
  "updated_at" : "2016-11-15T03:40:22.32Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

## List all Identities
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd


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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Identity
identity = Identity.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID9n1NEjjjCeurMoqLgwF8Nv",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
        "last_name" : "Green",
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
      "created_at" : "2016-11-15T03:40:34.45Z",
      "updated_at" : "2016-11-15T03:40:34.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDkgfS8dSwZnTyXYG9FHzeQZ",
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
      "created_at" : "2016-11-15T03:40:31.03Z",
      "updated_at" : "2016-11-15T03:40:31.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID25hwCpAsx5DGEAXapSscKw",
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
      "created_at" : "2016-11-15T03:40:30.10Z",
      "updated_at" : "2016-11-15T03:40:30.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDAtrxVDLvpxHEBvjRBDRRo",
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
      "created_at" : "2016-11-15T03:40:29.55Z",
      "updated_at" : "2016-11-15T03:40:29.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID2VQxr4AoEDY4BN5yZp2Mk2",
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
      "created_at" : "2016-11-15T03:40:27.96Z",
      "updated_at" : "2016-11-15T03:40:27.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDuk1qbkqjrmJihXfur6L4WE",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:40:27.28Z",
      "updated_at" : "2016-11-15T03:40:27.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDhS7v5XG48WfBW5FyeC5eqM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:40:26.72Z",
      "updated_at" : "2016-11-15T03:40:26.72Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDmBajumGWviwd3iWrwgq3G7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:40:25.96Z",
      "updated_at" : "2016-11-15T03:40:25.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID9NU6Mg3T2EuqNS2FzdV11m",
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
      "created_at" : "2016-11-15T03:40:23.95Z",
      "updated_at" : "2016-11-15T03:40:23.95Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID9U9pWN6iKJbmnb2Uu9n8A9",
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
      "created_at" : "2016-11-15T03:40:23.35Z",
      "updated_at" : "2016-11-15T03:40:23.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDaotf83HNxER4mu5gXAxJPV",
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
      "created_at" : "2016-11-15T03:40:22.32Z",
      "updated_at" : "2016-11-15T03:40:22.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDiWXJgvQmEiiEqEvJgG4xgB",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Facebook",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Facebook",
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
        "application_name" : "Facebook"
      },
      "created_at" : "2016-11-15T03:40:19.15Z",
      "updated_at" : "2016-11-15T03:40:19.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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


## Update an Identity
```shell
curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Step", 
	        "last_name": "Le", 
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
	        "doing_business_as": "Golds Gym", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Golds Gym", 
	        "url": "www.GoldsGym.com", 
	        "business_name": "Golds Gym", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDaotf83HNxER4mu5gXAxJPV",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Step",
    "last_name" : "Le",
    "email" : "user@example.org",
    "business_name" : "Golds Gym",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Golds Gym",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-15T03:40:22.32Z",
  "updated_at" : "2016-11-15T03:40:59.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
## Provision a Merchant

```shell

curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '


```
```java

import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );
```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "verification" : "VIjap1EF2Kao7zYjd8wJybvg",
  "merchant_profile" : "MPsW9zxb7VANE2N1pF5kNPUX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:40:33.10Z",
  "updated_at" : "2016-11-15T03:40:33.10Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsW9zxb7VANE2N1pF5kNPUX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIjap1EF2Kao7zYjd8wJybvg"
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

`POST https://api-test.payline.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "verification" : "VIjap1EF2Kao7zYjd8wJybvg",
  "merchant_profile" : "MPsW9zxb7VANE2N1pF5kNPUX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-15T03:40:33.10Z",
  "updated_at" : "2016-11-15T03:40:33.10Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsW9zxb7VANE2N1pF5kNPUX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIjap1EF2Kao7zYjd8wJybvg"
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
curl https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUmkS68nR9tbaksv35SYMkQs");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUmkS68nR9tbaksv35SYMkQs');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUmkS68nR9tbaksv35SYMkQs")

```
> Example Response:

```json
{
  "id" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "verification" : null,
  "merchant_profile" : "MPsW9zxb7VANE2N1pF5kNPUX",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-15T03:40:32.99Z",
  "updated_at" : "2016-11-15T03:40:33.22Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPsW9zxb7VANE2N1pF5kNPUX"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

## Create a Merchant User
```shell
curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USbFvxAoWyFT2C821tBSuLWw",
  "password" : "6cb5575f-8067-467b-bad3-e1dce2c542db",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-15T03:40:37.68Z",
  "updated_at" : "2016-11-15T03:40:37.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USbFvxAoWyFT2C821tBSuLWw"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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


## Reattempt Merchant Provisioning
```shell
curl https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VI35Fo212j4cFYKAi13nAW6w",
  "external_trace_id" : "b2c01a92-b6e6-49d2-bb97-2df2863d66c2",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T03:41:00.61Z",
  "updated_at" : "2016-11-15T03:41:00.63Z",
  "payment_instrument" : null,
  "merchant" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VI35Fo212j4cFYKAi13nAW6w"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
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

## Update Info on Processor
```shell
curl https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VI35Fo212j4cFYKAi13nAW6w",
  "external_trace_id" : "b2c01a92-b6e6-49d2-bb97-2df2863d66c2",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-15T03:41:00.61Z",
  "updated_at" : "2016-11-15T03:41:00.63Z",
  "payment_instrument" : null,
  "merchant" : "MUmkS68nR9tbaksv35SYMkQs",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VI35Fo212j4cFYKAi13nAW6w"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
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

## List all Merchants
```shell
curl https://api-test.payline.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Merchant
merchant = Merchant.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUmkS68nR9tbaksv35SYMkQs",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "verification" : null,
      "merchant_profile" : "MPsW9zxb7VANE2N1pF5kNPUX",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-15T03:40:32.99Z",
      "updated_at" : "2016-11-15T03:40:33.22Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPsW9zxb7VANE2N1pF5kNPUX"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
curl https://api-test.payline.io/merchants/MUmkS68nR9tbaksv35SYMkQs/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID9n1NEjjjCeurMoqLgwF8Nv",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
        "last_name" : "Green",
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
      "created_at" : "2016-11-15T03:40:34.45Z",
      "updated_at" : "2016-11-15T03:40:34.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDkgfS8dSwZnTyXYG9FHzeQZ",
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
      "created_at" : "2016-11-15T03:40:31.03Z",
      "updated_at" : "2016-11-15T03:40:31.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDkgfS8dSwZnTyXYG9FHzeQZ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID25hwCpAsx5DGEAXapSscKw",
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
      "created_at" : "2016-11-15T03:40:30.10Z",
      "updated_at" : "2016-11-15T03:40:30.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID25hwCpAsx5DGEAXapSscKw/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDAtrxVDLvpxHEBvjRBDRRo",
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
      "created_at" : "2016-11-15T03:40:29.55Z",
      "updated_at" : "2016-11-15T03:40:29.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDAtrxVDLvpxHEBvjRBDRRo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID2VQxr4AoEDY4BN5yZp2Mk2",
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
      "created_at" : "2016-11-15T03:40:27.96Z",
      "updated_at" : "2016-11-15T03:40:27.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2VQxr4AoEDY4BN5yZp2Mk2/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDuk1qbkqjrmJihXfur6L4WE",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:40:27.28Z",
      "updated_at" : "2016-11-15T03:40:27.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuk1qbkqjrmJihXfur6L4WE/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDhS7v5XG48WfBW5FyeC5eqM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-15T03:40:26.72Z",
      "updated_at" : "2016-11-15T03:40:26.72Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhS7v5XG48WfBW5FyeC5eqM/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDmBajumGWviwd3iWrwgq3G7",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "PARTNERSHIP",
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
        "max_transaction_amount" : 120000,
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-15T03:40:25.96Z",
      "updated_at" : "2016-11-15T03:40:25.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDmBajumGWviwd3iWrwgq3G7/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID9NU6Mg3T2EuqNS2FzdV11m",
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
      "created_at" : "2016-11-15T03:40:23.95Z",
      "updated_at" : "2016-11-15T03:40:23.95Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9NU6Mg3T2EuqNS2FzdV11m/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "ID9U9pWN6iKJbmnb2Uu9n8A9",
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
      "created_at" : "2016-11-15T03:40:23.35Z",
      "updated_at" : "2016-11-15T03:40:23.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID9U9pWN6iKJbmnb2Uu9n8A9/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDaotf83HNxER4mu5gXAxJPV",
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
      "created_at" : "2016-11-15T03:40:22.32Z",
      "updated_at" : "2016-11-15T03:40:22.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "IDiWXJgvQmEiiEqEvJgG4xgB",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Facebook",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Facebook",
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
        "application_name" : "Facebook"
      },
      "created_at" : "2016-11-15T03:40:19.15Z",
      "updated_at" : "2016-11-15T03:40:19.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

Retrieve all attempts to onboard (i.e. provision) a merchant onto a processor.

#### HTTP Request

`GET https://api-test.payline.io/merchants/:MERCHANT_ID/verifications`

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


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "name": "Bob Henderson", 
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
	    "identity": "ID9n1NEjjjCeurMoqLgwF8Nv"
	}'


```
```java

import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Bob Henderson", 
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
	    "identity"=> "ID9n1NEjjjCeurMoqLgwF8Nv"
	));
$card = $card->save();


```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Henderson", 
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
	    "identity": "ID9n1NEjjjCeurMoqLgwF8Nv"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIrNo8zuHEZoatYMcCPvkypT",
  "fingerprint" : "FPR-1778475544",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Henderson",
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
  "created_at" : "2016-11-15T03:40:35.02Z",
  "updated_at" : "2016-11-15T03:40:35.02Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID9n1NEjjjCeurMoqLgwF8Nv",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/updates"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'


```
```java

import io.payline.payments.processing.client.model.BankAccount;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "IDaotf83HNxER4mu5gXAxJPV"
	));
$bank_account = $bank_account->save();


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
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI485mr7uuJWRyTMVS8qpnBL",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:40:31.74Z",
  "updated_at" : "2016-11-15T03:40:31.74Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
## Tokenize Card with Embedded Iframe

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
          applicationId: 'APvFU1J7hgZjmewU9fkeUh8i',
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
  "id" : "TK9E43itbiWv7TyGX3PFbvKc",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-15T03:40:42.77Z",
  "updated_at" : "2016-11-15T03:40:42.77Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-16T03:40:42.77Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    }
  }
}
```

```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'

```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PI9E43itbiWv7TyGX3PFbvKc",
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
  "created_at" : "2016-11-15T03:40:43.28Z",
  "updated_at" : "2016-11-15T03:40:43.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/updates"
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

`POST https://api-test.payline.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated

## Associate a Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
    -d '
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}'


```
```java
import io.payline.payments.processing.client.model.PaymentCard;

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK9E43itbiWv7TyGX3PFbvKc", 
	    "type": "TOKEN", 
	    "identity": "IDaotf83HNxER4mu5gXAxJPV"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI9E43itbiWv7TyGX3PFbvKc",
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
  "created_at" : "2016-11-15T03:40:43.28Z",
  "updated_at" : "2016-11-15T03:40:43.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/updates"
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


## Fetch a Payment Instrument

```shell


curl https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI485mr7uuJWRyTMVS8qpnBL")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI485mr7uuJWRyTMVS8qpnBL');

```
```python



```
> Example Response:

```json
{
  "id" : "PI485mr7uuJWRyTMVS8qpnBL",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:40:31.65Z",
  "updated_at" : "2016-11-15T03:40:32.37Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    }
  }
}
```

Fetch a previously created `Payment Instrument`

#### HTTP Request

`GET https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PI485mr7uuJWRyTMVS8qpnBL",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-15T03:40:31.65Z",
  "updated_at" : "2016-11-15T03:40:32.37Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

`PUT https://api-test.payline.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


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
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PI9E43itbiWv7TyGX3PFbvKc",
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
      "created_at" : "2016-11-15T03:40:43.15Z",
      "updated_at" : "2016-11-15T03:40:43.15Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9E43itbiWv7TyGX3PFbvKc/updates"
        }
      }
    }, {
      "id" : "PI3fSDf8RY5H2Hm7Sxuq65km",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T03:40:35.62Z",
      "updated_at" : "2016-11-15T03:40:35.62Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID9n1NEjjjCeurMoqLgwF8Nv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3fSDf8RY5H2Hm7Sxuq65km"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3fSDf8RY5H2Hm7Sxuq65km/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3fSDf8RY5H2Hm7Sxuq65km/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI3fSDf8RY5H2Hm7Sxuq65km/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIrNo8zuHEZoatYMcCPvkypT",
      "fingerprint" : "FPR-1778475544",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Bob Henderson",
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
      "created_at" : "2016-11-15T03:40:34.94Z",
      "updated_at" : "2016-11-15T03:40:40.61Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID9n1NEjjjCeurMoqLgwF8Nv",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID9n1NEjjjCeurMoqLgwF8Nv"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT/updates"
        }
      }
    }, {
      "id" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:32.99Z",
      "updated_at" : "2016-11-15T03:40:32.99Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PI2tvvUTfN9aphBRjNxJLS7R",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:32.99Z",
      "updated_at" : "2016-11-15T03:40:32.99Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2tvvUTfN9aphBRjNxJLS7R"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2tvvUTfN9aphBRjNxJLS7R/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2tvvUTfN9aphBRjNxJLS7R/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI2tvvUTfN9aphBRjNxJLS7R/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIDMZjyb6nLswUXy2o51aj4",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:32.99Z",
      "updated_at" : "2016-11-15T03:40:32.99Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIDMZjyb6nLswUXy2o51aj4"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIDMZjyb6nLswUXy2o51aj4/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIDMZjyb6nLswUXy2o51aj4/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIDMZjyb6nLswUXy2o51aj4/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PI485mr7uuJWRyTMVS8qpnBL",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-15T03:40:31.65Z",
      "updated_at" : "2016-11-15T03:40:32.37Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIbg6nJazoE73h8fwcHPaAzm",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:19.90Z",
      "updated_at" : "2016-11-15T03:40:19.90Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiWXJgvQmEiiEqEvJgG4xgB",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbg6nJazoE73h8fwcHPaAzm"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbg6nJazoE73h8fwcHPaAzm/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbg6nJazoE73h8fwcHPaAzm/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIbg6nJazoE73h8fwcHPaAzm/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIp3MQD1bkT2r1vvXjwzKphN",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:19.90Z",
      "updated_at" : "2016-11-15T03:40:19.90Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiWXJgvQmEiiEqEvJgG4xgB",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIp3MQD1bkT2r1vvXjwzKphN"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIp3MQD1bkT2r1vvXjwzKphN/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIp3MQD1bkT2r1vvXjwzKphN/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIp3MQD1bkT2r1vvXjwzKphN/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIcfre4PYgX7Bz7u1ha6PxMn",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:19.90Z",
      "updated_at" : "2016-11-15T03:40:19.90Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcfre4PYgX7Bz7u1ha6PxMn"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcfre4PYgX7Bz7u1ha6PxMn/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcfre4PYgX7Bz7u1ha6PxMn/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcfre4PYgX7Bz7u1ha6PxMn/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        }
      }
    }, {
      "id" : "PIiu6oRpry65d5xTo3DyZ3Xb",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-15T03:40:19.90Z",
      "updated_at" : "2016-11-15T03:40:19.90Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiWXJgvQmEiiEqEvJgG4xgB",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiu6oRpry65d5xTo3DyZ3Xb"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiu6oRpry65d5xTo3DyZ3Xb/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiWXJgvQmEiiEqEvJgG4xgB"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiu6oRpry65d5xTo3DyZ3Xb/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiu6oRpry65d5xTo3DyZ3Xb/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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

curl https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
)

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDaotf83HNxER4mu5gXAxJPV');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));

```
```python


from payline.resources import Identity
from payline.resources import Settlement

identity = Identity.get(id="IDaotf83HNxER4mu5gXAxJPV")
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
  "id" : "STjT9iJhUzeJjjABXHPc9WB3",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:47:41.34Z",
  "updated_at" : "2016-11-15T03:47:41.35Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=debit"
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


curl https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STjT9iJhUzeJjjABXHPc9WB3");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STjT9iJhUzeJjjABXHPc9WB3');

```
```python



```
> Example Response:

```json
{
  "id" : "STjT9iJhUzeJjjABXHPc9WB3",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:47:41.23Z",
  "updated_at" : "2016-11-15T03:47:42.86Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PI485mr7uuJWRyTMVS8qpnBL",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PI485mr7uuJWRyTMVS8qpnBL"
	}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "STjT9iJhUzeJjjABXHPc9WB3",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "currency" : "USD",
  "created_at" : "2016-11-15T03:47:41.23Z",
  "updated_at" : "2016-11-15T03:47:42.86Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PI485mr7uuJWRyTMVS8qpnBL",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=debit"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Settlement
settlements = Settlement.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STjT9iJhUzeJjjABXHPc9WB3",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "currency" : "USD",
      "created_at" : "2016-11-15T03:47:41.23Z",
      "updated_at" : "2016-11-15T03:47:42.86Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 100,
      "total_fees" : 11,
      "total_fee" : 11,
      "net_amount" : 89,
      "destination" : "PI485mr7uuJWRyTMVS8qpnBL",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?type=debit"
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
curl https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRtHL2VTs5CRjfeTSeY8ojJt",
      "amount" : 89,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "83c52155-74a0-4392-8adb-812075bd6d5b",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "destination" : "PI485mr7uuJWRyTMVS8qpnBL",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:47:42.56Z",
      "updated_at" : "2016-11-15T03:47:42.74Z",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRtHL2VTs5CRjfeTSeY8ojJt"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRtHL2VTs5CRjfeTSeY8ojJt/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRtHL2VTs5CRjfeTSeY8ojJt/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRtHL2VTs5CRjfeTSeY8ojJt/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRtHL2VTs5CRjfeTSeY8ojJt/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI485mr7uuJWRyTMVS8qpnBL"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRsbUZh2TTv3AqcmzWWrsXNc",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "b84d0129-c5db-4ce8-ae47-d2d37ba3f4ff",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "destination" : "PIcfre4PYgX7Bz7u1ha6PxMn",
      "ready_to_settle_at" : "2016-11-15T03:42:30.93Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:42:31.10Z",
      "updated_at" : "2016-11-15T03:42:31.44Z",
      "merchant_identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRsbUZh2TTv3AqcmzWWrsXNc"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRsbUZh2TTv3AqcmzWWrsXNc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRsbUZh2TTv3AqcmzWWrsXNc/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRsbUZh2TTv3AqcmzWWrsXNc/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRsbUZh2TTv3AqcmzWWrsXNc/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcfre4PYgX7Bz7u1ha6PxMn"
        }
      }
    }, {
      "id" : "TR9STEP4F5uZeQJrXFUnwPjw",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PIrNo8zuHEZoatYMcCPvkypT",
      "destination" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "ready_to_settle_at" : "2016-11-15T03:42:30.93Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:41.20Z",
      "updated_at" : "2016-11-15T03:41:01.30Z",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STjT9iJhUzeJjjABXHPc9WB3/transfers?offset=0&limit=20&sort=created_at,desc"
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

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRnyz63K5sRmDax8AiHdsBLc");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRnyz63K5sRmDax8AiHdsBLc');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRnyz63K5sRmDax8AiHdsBLc")

```
> Example Response:

```json
{
  "id" : "TRnyz63K5sRmDax8AiHdsBLc",
  "amount" : 229829,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "1438c674-9f49-4895-9133-1aacac2df139",
  "currency" : "USD",
  "application" : "APvFU1J7hgZjmewU9fkeUh8i",
  "source" : "PIrNo8zuHEZoatYMcCPvkypT",
  "destination" : "PI4MZrhJo5pYthKZP8XZb1G2",
  "ready_to_settle_at" : null,
  "fee" : 22983,
  "statement_descriptor" : "PLD*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:36.41Z",
  "updated_at" : "2016-11-15T03:40:39.50Z",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
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

curl https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRnyz63K5sRmDax8AiHdsBLc');
$refund = $debit->reverse(50);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TRnyz63K5sRmDax8AiHdsBLc")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRwfk4NmFPTaJi18LyodtADh",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "f4f25276-1395-4ae8-a8ff-2b1ef33182f2",
  "currency" : "USD",
  "application" : "APvFU1J7hgZjmewU9fkeUh8i",
  "source" : "PI4MZrhJo5pYthKZP8XZb1G2",
  "destination" : "PIrNo8zuHEZoatYMcCPvkypT",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "PLD*GOLDS GYM",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-15T03:40:39.55Z",
  "updated_at" : "2016-11-15T03:40:39.63Z",
  "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRwfk4NmFPTaJi18LyodtADh"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRwfk4NmFPTaJi18LyodtADh/payment_instruments"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Transfer
transfer = Transfer.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR9STEP4F5uZeQJrXFUnwPjw",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "63eaf2c9-c57c-4f86-8966-eb5e4481620f",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PIrNo8zuHEZoatYMcCPvkypT",
      "destination" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:41.20Z",
      "updated_at" : "2016-11-15T03:40:41.42Z",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR9STEP4F5uZeQJrXFUnwPjw/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
        }
      }
    }, {
      "id" : "TRwfk4NmFPTaJi18LyodtADh",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6d5fb97b-c66c-4692-b9be-6d96e8bcc771",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "destination" : "PIrNo8zuHEZoatYMcCPvkypT",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "PLD*GOLDS GYM",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:39.31Z",
      "updated_at" : "2016-11-15T03:40:39.63Z",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRwfk4NmFPTaJi18LyodtADh"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRwfk4NmFPTaJi18LyodtADh/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
        }
      }
    }, {
      "id" : "TRnyz63K5sRmDax8AiHdsBLc",
      "amount" : 229829,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "1438c674-9f49-4895-9133-1aacac2df139",
      "currency" : "USD",
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "source" : "PIrNo8zuHEZoatYMcCPvkypT",
      "destination" : "PI4MZrhJo5pYthKZP8XZb1G2",
      "ready_to_settle_at" : null,
      "fee" : 22983,
      "statement_descriptor" : "PLD*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-15T03:40:36.41Z",
      "updated_at" : "2016-11-15T03:40:39.50Z",
      "merchant_identity" : "IDaotf83HNxER4mu5gXAxJPV",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDaotf83HNxER4mu5gXAxJPV"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRnyz63K5sRmDax8AiHdsBLc/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrNo8zuHEZoatYMcCPvkypT"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI4MZrhJo5pYthKZP8XZb1G2"
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
    "count" : 3
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/transfers`
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
    -u USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd \
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
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
> Example Response:

```json
{
  "id" : "WHrPWX4WQ2WR6tar1SDQvovM",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvFU1J7hgZjmewU9fkeUh8i",
  "created_at" : "2016-11-15T03:40:21.97Z",
  "updated_at" : "2016-11-15T03:40:21.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHrPWX4WQ2WR6tar1SDQvovM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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



curl https://api-test.payline.io/webhooks/WHrPWX4WQ2WR6tar1SDQvovM \
    -H "Content-Type: application/vnd.json+api" \
    -u USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHrPWX4WQ2WR6tar1SDQvovM");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHrPWX4WQ2WR6tar1SDQvovM');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WHrPWX4WQ2WR6tar1SDQvovM")

```
> Example Response:

```json
{
  "id" : "WHrPWX4WQ2WR6tar1SDQvovM",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APvFU1J7hgZjmewU9fkeUh8i",
  "created_at" : "2016-11-15T03:40:21.97Z",
  "updated_at" : "2016-11-15T03:40:21.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHrPWX4WQ2WR6tar1SDQvovM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
    -u  USfQ9LCUotNchB31PKbXdqir:30141a9e-5338-4848-a24a-3ad12085e3dd

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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Webhook
webhooks = Webhook.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHrPWX4WQ2WR6tar1SDQvovM",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APvFU1J7hgZjmewU9fkeUh8i",
      "created_at" : "2016-11-15T03:40:21.97Z",
      "updated_at" : "2016-11-15T03:40:21.97Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHrPWX4WQ2WR6tar1SDQvovM"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APvFU1J7hgZjmewU9fkeUh8i"
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USfQ9LCUotNchB31PKbXdqir', '30141a9e-5338-4848-a24a-3ad12085e3dd');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

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
