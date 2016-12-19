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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'USjeUio4zHU9eEsLqnE6d7Wu',
	"password" => 'cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1']
	);

require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("USjeUio4zHU9eEsLqnE6d7Wu", "cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USjeUio4zHU9eEsLqnE6d7Wu`

- Password: `cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1`

- Application ID: `APnGK9w9wFhyeFxfZnFvKwSh`

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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
> Example Response:

```json
{
  "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:23:45.70Z",
  "updated_at" : "2016-12-19T22:23:45.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
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
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\BankAccount;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
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
	    "identity"=> "IDb8q27oRPi4NgXidKK8qbcD"
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
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIapqJzWaZN3QN1aPeqz5fHY",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:23:50.95Z",
  "updated_at" : "2016-12-19T22:23:50.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDb8q27oRPi4NgXidKK8qbcD")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "verification" : "VIp1fzGcQ7ZfBGmYcJzsmqNm",
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:23:51.87Z",
  "updated_at" : "2016-12-19T22:23:51.87Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIp1fzGcQ7ZfBGmYcJzsmqNm"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
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
	        "first_name"=> "Amy", 
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


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
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
> Example Response:

```json
{
  "id" : "IDbEcrf3hoD61riaKNtoKh9S",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
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
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:23:52.55Z",
  "updated_at" : "2016-12-19T22:23:52.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "name": "Ayisha Serna", 
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
	    "identity": "IDbEcrf3hoD61riaKNtoKh9S"
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
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
$card = new PaymentCard(
	array(
	    "name"=> "Ayisha Serna", 
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
	    "identity"=> "IDbEcrf3hoD61riaKNtoKh9S"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Ayisha Serna", 
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
	    "identity": "IDbEcrf3hoD61riaKNtoKh9S"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "fingerprint" : "FPR-921925016",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ayisha Serna",
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
  "created_at" : "2016-12-19T22:23:52.96Z",
  "updated_at" : "2016-12-19T22:23:52.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbEcrf3hoD61riaKNtoKh9S",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/updates"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "merchant_identity": "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIhspXZ5VJWgrXwEA4xeMq9J", 
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
use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIhspXZ5VJWgrXwEA4xeMq9J", 
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
	    "merchant_identity": "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIhspXZ5VJWgrXwEA4xeMq9J", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:58.27Z",
  "updated_at" : "2016-12-19T22:23:58.30Z",
  "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:23:58.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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
curl https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh8jqpVV6ERp4rDfvZm1RgK");
authorization = authorization.capture(50L);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUh8jqpVV6ERp4rDfvZm1RgK');
$authorization = $authorization->capture(50, 10);

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUh8jqpVV6ERp4rDfvZm1RgK")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfDAHgqDUk423PyTf6uAUbY",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:58.22Z",
  "updated_at" : "2016-12-19T22:23:58.94Z",
  "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:23:58.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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
### Step 1: Create an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Step", 
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



```
> Example Response:

```json
{
  "id" : "IDcN2K7fZNas88DgJ5YAkQky",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:24:06.69Z",
  "updated_at" : "2016-12-19T22:24:06.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "name": "Marshall Lopez", 
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
	    "identity": "IDcN2K7fZNas88DgJ5YAkQky"
	}'
```
```java

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDcN2K7fZNas88DgJ5YAkQky');
$card = new PaymentCard(
	array(
	    "name"=> "Marshall Lopez", 
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
	    "identity"=> "IDcN2K7fZNas88DgJ5YAkQky"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PIxnxLTU7SS7WYyptRQvoc7X",
  "fingerprint" : "FPR-1479379416",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marshall Lopez",
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
  "created_at" : "2016-12-19T22:24:08.44Z",
  "updated_at" : "2016-12-19T22:24:08.44Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/updates"
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
curl https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDcN2K7fZNas88DgJ5YAkQky');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MU3px7YZdnfATwStXFkSRdUV",
  "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
  "verification" : "VIorrCcwoKpVDhawVK7WH74p",
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:24:07.12Z",
  "updated_at" : "2016-12-19T22:24:07.12Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU3px7YZdnfATwStXFkSRdUV"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU3px7YZdnfATwStXFkSRdUV/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIorrCcwoKpVDhawVK7WH74p"
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
    -u USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDcN2K7fZNas88DgJ5YAkQky", 
	    "destination": "PIxnxLTU7SS7WYyptRQvoc7X", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```java

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "merchant_identity"=> "IDcN2K7fZNas88DgJ5YAkQky", 
	    "destination"=> "PIxnxLTU7SS7WYyptRQvoc7X", 
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "processor"=> "VISA_V1"
	));
$transfer = $transfer->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRsuTiE6Z8jAnerJKPdqYh41",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "184730",
  "currency" : "USD",
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "source" : "PIffqfWcHApxKEPf7UtjNLHN",
  "destination" : "PIxnxLTU7SS7WYyptRQvoc7X",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:09.24Z",
  "updated_at" : "2016-12-19T22:24:10.35Z",
  "merchant_identity" : "IDcN2K7fZNas88DgJ5YAkQky",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X"
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
          applicationId: 'APnGK9w9wFhyeFxfZnFvKwSh',
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
  "id" : "TK8dJruN5u4Vu2xF9QSjKhVC",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-19T22:24:00.28Z",
  "updated_at" : "2016-12-19T22:24:00.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-20T22:24:00.28Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
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
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDb8q27oRPi4NgXidKK8qbcD"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI8dJruN5u4Vu2xF9QSjKhVC",
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
  "created_at" : "2016-12-19T22:24:00.67Z",
  "updated_at" : "2016-12-19T22:24:00.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/updates"
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

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to CrossRiver.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/2hxnjL0q/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the CrossRiver API.
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
    applicationId: "APnGK9w9wFhyeFxfZnFvKwSh",
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
server | *string*, **required** |  The base url for the CrossRiver API
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
  "id" : "TK8dJruN5u4Vu2xF9QSjKhVC",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2016-12-19T22:24:00.28Z",
  "updated_at" : "2016-12-19T22:24:00.28Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-12-20T22:24:00.28Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
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
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDb8q27oRPi4NgXidKK8qbcD"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI8dJruN5u4Vu2xF9QSjKhVC",
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
  "created_at" : "2016-12-19T22:24:00.67Z",
  "updated_at" : "2016-12-19T22:24:00.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/updates"
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
> Example Response:

```json
{
  "id" : "USjeUio4zHU9eEsLqnE6d7Wu",
  "password" : "cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:42.05Z",
  "updated_at" : "2016-12-19T22:23:42.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjeUio4zHU9eEsLqnE6d7Wu"
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
	        "application_name": "Square"
	    }, 
	    "user": "USjeUio4zHU9eEsLqnE6d7Wu", 
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
use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USjeUio4zHU9eEsLqnE6d7Wu", 
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:23:42.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
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
> Example Response:

```json
{
  "id" : "PRcMiAYPjn4sVws1wWCXng76",
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "default_merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "created_at" : "2016-12-19T22:23:43.19Z",
  "updated_at" : "2016-12-19T22:23:43.19Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors/PRcMiAYPjn4sVws1wWCXng76"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    }
  }
}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The CrossRiver Payment Platform is processor agnostic allowing for processing transactions
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/ \
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:24:21.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/ \
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:24:22.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use CrossRiver\Resources\Application;

$application = Application::retrieve('APnGK9w9wFhyeFxfZnFvKwSh');

```
```python


from crossriver.resources import Application

application = Application.get(id="APnGK9w9wFhyeFxfZnFvKwSh")
```
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:23:44.94Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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

## Create an Application
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -d '
	{
	    "tags": {
	        "application_name": "Square"
	    }, 
	    "user": "USjeUio4zHU9eEsLqnE6d7Wu", 
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
use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Square"
	    ), 
	    "user"=> "USjeUio4zHU9eEsLqnE6d7Wu", 
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


from crossriver.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Square"
	    }, 
	    "user": "USjeUio4zHU9eEsLqnE6d7Wu", 
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:23:42.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/ \
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:24:19.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/ \
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
> Example Response:

```json
{
  "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-12-19T22:23:42.55Z",
  "updated_at" : "2016-12-19T22:24:19.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
## Create an Application User
```shell
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'

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
  "id" : "USfvn7Qihw1V6XygqQY3PwRi",
  "password" : "4392cc9c-07f1-4eac-91df-79ade2337e2c",
  "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:44.02Z",
  "updated_at" : "2016-12-19T22:23:44.02Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USfvn7Qihw1V6XygqQY3PwRi"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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

## [ADMIN] Enable the Dummy Processor (i.e. Sandbox)
```shell
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
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
> Example Response:

```json
{
  "id" : "PRcMiAYPjn4sVws1wWCXng76",
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "default_merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "created_at" : "2016-12-19T22:23:43.19Z",
  "updated_at" : "2016-12-19T22:23:43.19Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors/PRcMiAYPjn4sVws1wWCXng76"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

```
```php
<?php

```
```python


from crossriver.resources import Application

application = Application.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "enabled" : true,
      "tags" : {
        "application_name" : "Square"
      },
      "owner" : "IDd8xfHisExXe2KQx3e7rhwH",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-12-19T22:23:42.55Z",
      "updated_at" : "2016-12-19T22:23:44.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/tokens"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "merchant_identity": "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIhspXZ5VJWgrXwEA4xeMq9J", 
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
use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIhspXZ5VJWgrXwEA4xeMq9J", 
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
	    "merchant_identity": "IDb8q27oRPi4NgXidKK8qbcD", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIhspXZ5VJWgrXwEA4xeMq9J", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:58.27Z",
  "updated_at" : "2016-12-19T22:23:58.30Z",
  "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:23:58.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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
curl https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh8jqpVV6ERp4rDfvZm1RgK");
authorization = authorization.capture(50L);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUh8jqpVV6ERp4rDfvZm1RgK');
$authorization = $authorization->capture(50, 10);

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUh8jqpVV6ERp4rDfvZm1RgK")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfDAHgqDUk423PyTf6uAUbY",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:58.22Z",
  "updated_at" : "2016-12-19T22:23:58.94Z",
  "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:23:58.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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

curl https://api-staging.finix.io/authorizations/AU9X1eHSoZYkrADXnXvahCji \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUh8jqpVV6ERp4rDfvZm1RgK');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUh8jqpVV6ERp4rDfvZm1RgK")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AU9X1eHSoZYkrADXnXvahCji",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:24:01.44Z",
  "updated_at" : "2016-12-19T22:24:02.06Z",
  "trace_id" : "76d39f76-b638-4daf-a670-10137d5c4ab1",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : true,
  "expires_at" : "2016-12-26T22:24:01.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU9X1eHSoZYkrADXnXvahCji"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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

curl https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUh8jqpVV6ERp4rDfvZm1RgK");

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUh8jqpVV6ERp4rDfvZm1RgK');

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUh8jqpVV6ERp4rDfvZm1RgK")
```
> Example Response:

```json
{
  "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfDAHgqDUk423PyTf6uAUbY",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:58.22Z",
  "updated_at" : "2016-12-19T22:23:58.94Z",
  "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "is_void" : false,
  "expires_at" : "2016-12-26T22:23:58.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

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
use CrossRiver\Resources\Authorization;

$authorizations = Authorization::getPagination("/authorizations");


```
```python


from crossriver.resources import Authorization

authorization = Authorization.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU9X1eHSoZYkrADXnXvahCji",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:01.44Z",
      "updated_at" : "2016-12-19T22:24:02.06Z",
      "trace_id" : "76d39f76-b638-4daf-a670-10137d5c4ab1",
      "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "is_void" : true,
      "expires_at" : "2016-12-26T22:24:01.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU9X1eHSoZYkrADXnXvahCji"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        }
      }
    }, {
      "id" : "AUh8jqpVV6ERp4rDfvZm1RgK",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRfDAHgqDUk423PyTf6uAUbY",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:23:58.22Z",
      "updated_at" : "2016-12-19T22:23:58.94Z",
      "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
      "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "is_void" : false,
      "expires_at" : "2016-12-26T22:23:58.22Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUh8jqpVV6ERp4rDfvZm1RgK"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
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
	        "first_name"=> "Amy", 
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


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
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
> Example Response:

```json
{
  "id" : "IDbEcrf3hoD61riaKNtoKh9S",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
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
    "stake_percent" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-12-19T22:23:52.55Z",
  "updated_at" : "2016-12-19T22:23:52.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
> Example Response:

```json
{
  "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:23:45.70Z",
  "updated_at" : "2016-12-19T22:23:45.70Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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

curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDb8q27oRPi4NgXidKK8qbcD");

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDb8q27oRPi4NgXidKK8qbcD")

```
> Example Response:

```json
{
  "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
    "ownership_type" : null,
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2016-12-19T22:23:45.68Z",
  "updated_at" : "2016-12-19T22:23:45.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
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
	        "max_transaction_amount": 1200000, 
	        "principal_percentage_ownership": 50, 
	        "doing_business_as": "ACME Anchors", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "ACME Anchors", 
	        "url": "www.ACMEAnchors.com", 
	        "business_name": "ACME Anchors", 
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
  "id" : "IDb8q27oRPi4NgXidKK8qbcD",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Diaz",
    "email" : "user@example.org",
    "business_name" : "ACME Anchors",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "ACME Anchors",
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
    "stake_percent" : null,
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "ACME Anchors"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2016-12-19T22:23:45.68Z",
  "updated_at" : "2016-12-19T22:24:16.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
## List all Identities
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1


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
      "id" : "IDcN2K7fZNas88DgJ5YAkQky",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:06.68Z",
      "updated_at" : "2016-12-19T22:24:06.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDbEcrf3hoD61riaKNtoKh9S",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
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
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:23:52.54Z",
      "updated_at" : "2016-12-19T22:23:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDm2MKE3Tk4N8yRYuy6BVaYN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.41Z",
      "updated_at" : "2016-12-19T22:23:50.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDeFZ9i5zGGzZ16NtGW1yDwY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.00Z",
      "updated_at" : "2016-12-19T22:23:50.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDi7z79f7BQsqi3mhJ9WQ8yA",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:49.51Z",
      "updated_at" : "2016-12-19T22:23:49.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDnR6598Ku8gVHxyiEuM8RS4",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:48.61Z",
      "updated_at" : "2016-12-19T22:23:48.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "ID7mbqpqnfunGyVvhLD9YddS",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.85Z",
      "updated_at" : "2016-12-19T22:23:47.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDhE6Fh8xUdyV8TxzRD1ePB6",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.48Z",
      "updated_at" : "2016-12-19T22:23:47.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDtG7N3bixCDBio5ESJSpkY9",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.88Z",
      "updated_at" : "2016-12-19T22:23:46.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDJXcaXGCmNUpSw6EaKnEfY",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.45Z",
      "updated_at" : "2016-12-19T22:23:46.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDfzmeyhP4vR34XujnoenLT9",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.09Z",
      "updated_at" : "2016-12-19T22:23:46.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:45.68Z",
      "updated_at" : "2016-12-19T22:23:45.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDd8xfHisExXe2KQx3e7rhwH",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Square"
      },
      "created_at" : "2016-12-19T22:23:42.55Z",
      "updated_at" : "2016-12-19T22:23:42.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDb8q27oRPi4NgXidKK8qbcD")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "verification" : "VIp1fzGcQ7ZfBGmYcJzsmqNm",
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:23:51.87Z",
  "updated_at" : "2016-12-19T22:23:51.87Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIp1fzGcQ7ZfBGmYcJzsmqNm"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MU2hS9F1xJm42YHHVPcmHYjH");

```
```php
<?php
use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MU2hS9F1xJm42YHHVPcmHYjH');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MU2hS9F1xJm42YHHVPcmHYjH")

```
> Example Response:

```json
{
  "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "verification" : null,
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-12-19T22:23:51.82Z",
  "updated_at" : "2016-12-19T22:23:51.93Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MU2hS9F1xJm42YHHVPcmHYjH');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VIisg1X6daXZ3xNWdUZNhPkp",
  "external_trace_id" : "655c3533-4d49-4714-afbe-1aec0900bb7c",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-19T22:24:17.34Z",
  "updated_at" : "2016-12-19T22:24:17.36Z",
  "trace_id" : "655c3533-4d49-4714-afbe-1aec0900bb7c",
  "payment_instrument" : null,
  "merchant" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIisg1X6daXZ3xNWdUZNhPkp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'
```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MU2hS9F1xJm42YHHVPcmHYjH');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VIisg1X6daXZ3xNWdUZNhPkp",
  "external_trace_id" : "655c3533-4d49-4714-afbe-1aec0900bb7c",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-12-19T22:24:17.34Z",
  "updated_at" : "2016-12-19T22:24:17.36Z",
  "trace_id" : "655c3533-4d49-4714-afbe-1aec0900bb7c",
  "payment_instrument" : null,
  "merchant" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VIisg1X6daXZ3xNWdUZNhPkp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/ \
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
> Example Response:

```json
{
  "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "verification" : null,
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-12-19T22:23:51.82Z",
  "updated_at" : "2016-12-19T22:24:17.91Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/ \
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
> Example Response:

```json
{
  "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "verification" : null,
  "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-12-19T22:23:51.82Z",
  "updated_at" : "2016-12-19T22:24:18.47Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

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
      "id" : "MU3px7YZdnfATwStXFkSRdUV",
      "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "verification" : null,
      "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
      "processor" : "VISA_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-12-19T22:24:07.04Z",
      "updated_at" : "2016-12-19T22:24:07.75Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU3px7YZdnfATwStXFkSRdUV"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU3px7YZdnfATwStXFkSRdUV/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "MU2hS9F1xJm42YHHVPcmHYjH",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "verification" : null,
      "merchant_profile" : "MP8T4LzQTsdjkqo5wy21c13v",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-12-19T22:23:51.82Z",
      "updated_at" : "2016-12-19T22:23:51.93Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MP8T4LzQTsdjkqo5wy21c13v"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MU2hS9F1xJm42YHHVPcmHYjH');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcN2K7fZNas88DgJ5YAkQky",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:06.68Z",
      "updated_at" : "2016-12-19T22:24:06.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDbEcrf3hoD61riaKNtoKh9S",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
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
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:23:52.54Z",
      "updated_at" : "2016-12-19T22:23:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDm2MKE3Tk4N8yRYuy6BVaYN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.41Z",
      "updated_at" : "2016-12-19T22:23:50.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDeFZ9i5zGGzZ16NtGW1yDwY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.00Z",
      "updated_at" : "2016-12-19T22:23:50.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDi7z79f7BQsqi3mhJ9WQ8yA",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:49.51Z",
      "updated_at" : "2016-12-19T22:23:49.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDnR6598Ku8gVHxyiEuM8RS4",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:48.61Z",
      "updated_at" : "2016-12-19T22:23:48.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "ID7mbqpqnfunGyVvhLD9YddS",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.85Z",
      "updated_at" : "2016-12-19T22:23:47.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDhE6Fh8xUdyV8TxzRD1ePB6",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.48Z",
      "updated_at" : "2016-12-19T22:23:47.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDtG7N3bixCDBio5ESJSpkY9",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.88Z",
      "updated_at" : "2016-12-19T22:23:46.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDJXcaXGCmNUpSw6EaKnEfY",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.45Z",
      "updated_at" : "2016-12-19T22:23:46.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDfzmeyhP4vR34XujnoenLT9",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.09Z",
      "updated_at" : "2016-12-19T22:23:46.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:45.68Z",
      "updated_at" : "2016-12-19T22:23:45.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDd8xfHisExXe2KQx3e7rhwH",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Square"
      },
      "created_at" : "2016-12-19T22:23:42.55Z",
      "updated_at" : "2016-12-19T22:23:42.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/merchants/MU2hS9F1xJm42YHHVPcmHYjH/verifications \
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
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDcN2K7fZNas88DgJ5YAkQky",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:24:06.68Z",
      "updated_at" : "2016-12-19T22:24:06.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDbEcrf3hoD61riaKNtoKh9S",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
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
        "stake_percent" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-12-19T22:23:52.54Z",
      "updated_at" : "2016-12-19T22:23:52.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDm2MKE3Tk4N8yRYuy6BVaYN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.41Z",
      "updated_at" : "2016-12-19T22:23:50.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDm2MKE3Tk4N8yRYuy6BVaYN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDeFZ9i5zGGzZ16NtGW1yDwY",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:50.00Z",
      "updated_at" : "2016-12-19T22:23:50.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeFZ9i5zGGzZ16NtGW1yDwY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDi7z79f7BQsqi3mhJ9WQ8yA",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:49.51Z",
      "updated_at" : "2016-12-19T22:23:49.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDi7z79f7BQsqi3mhJ9WQ8yA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDnR6598Ku8gVHxyiEuM8RS4",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:48.61Z",
      "updated_at" : "2016-12-19T22:23:48.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDnR6598Ku8gVHxyiEuM8RS4/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "ID7mbqpqnfunGyVvhLD9YddS",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.85Z",
      "updated_at" : "2016-12-19T22:23:47.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7mbqpqnfunGyVvhLD9YddS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDhE6Fh8xUdyV8TxzRD1ePB6",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:47.48Z",
      "updated_at" : "2016-12-19T22:23:47.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhE6Fh8xUdyV8TxzRD1ePB6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDtG7N3bixCDBio5ESJSpkY9",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.88Z",
      "updated_at" : "2016-12-19T22:23:46.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtG7N3bixCDBio5ESJSpkY9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDJXcaXGCmNUpSw6EaKnEfY",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.45Z",
      "updated_at" : "2016-12-19T22:23:46.45Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDJXcaXGCmNUpSw6EaKnEfY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDfzmeyhP4vR34XujnoenLT9",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:46.09Z",
      "updated_at" : "2016-12-19T22:23:46.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfzmeyhP4vR34XujnoenLT9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDb8q27oRPi4NgXidKK8qbcD",
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
        "ownership_type" : null,
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2016-12-19T22:23:45.68Z",
      "updated_at" : "2016-12-19T22:23:45.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "IDd8xfHisExXe2KQx3e7rhwH",
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
        "stake_percent" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Square"
      },
      "created_at" : "2016-12-19T22:23:42.55Z",
      "updated_at" : "2016-12-19T22:23:42.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'

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
  "id" : "USonEP8vBQ5kXUMJn2vH7c1v",
  "password" : "b81f1d76-35a4-426c-8772-bbac79406cd7",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:55.01Z",
  "updated_at" : "2016-12-19T22:23:55.01Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USonEP8vBQ5kXUMJn2vH7c1v"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
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
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDb8q27oRPi4NgXidKK8qbcD"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8dJruN5u4Vu2xF9QSjKhVC", 
	    "type": "TOKEN", 
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI8dJruN5u4Vu2xF9QSjKhVC",
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
  "created_at" : "2016-12-19T22:24:00.67Z",
  "updated_at" : "2016-12-19T22:24:00.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/updates"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '
	{
	    "name": "Ayisha Serna", 
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
	    "identity": "IDbEcrf3hoD61riaKNtoKh9S"
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
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
$card = new PaymentCard(
	array(
	    "name"=> "Ayisha Serna", 
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
	    "identity"=> "IDbEcrf3hoD61riaKNtoKh9S"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Ayisha Serna", 
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
	    "identity": "IDbEcrf3hoD61riaKNtoKh9S"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "fingerprint" : "FPR-921925016",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ayisha Serna",
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
  "created_at" : "2016-12-19T22:23:52.96Z",
  "updated_at" : "2016-12-19T22:23:52.96Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbEcrf3hoD61riaKNtoKh9S",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/updates"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
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
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\BankAccount;

$identity = Identity::retrieve('IDb8q27oRPi4NgXidKK8qbcD');
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
	    "identity"=> "IDb8q27oRPi4NgXidKK8qbcD"
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
	    "identity": "IDb8q27oRPi4NgXidKK8qbcD"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIapqJzWaZN3QN1aPeqz5fHY",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:23:50.95Z",
  "updated_at" : "2016-12-19T22:23:50.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
## Fetch a Payment Instrument

```shell


curl https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIapqJzWaZN3QN1aPeqz5fHY")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIapqJzWaZN3QN1aPeqz5fHY');

```
```python



```
> Example Response:

```json
{
  "id" : "PIapqJzWaZN3QN1aPeqz5fHY",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:23:50.93Z",
  "updated_at" : "2016-12-19T22:23:51.44Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
  "id" : "PIapqJzWaZN3QN1aPeqz5fHY",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2016-12-19T22:23:50.93Z",
  "updated_at" : "2016-12-19T22:23:51.44Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1
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
      "id" : "PIxnxLTU7SS7WYyptRQvoc7X",
      "fingerprint" : "FPR-1479379416",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marshall Lopez",
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
      "created_at" : "2016-12-19T22:24:08.41Z",
      "updated_at" : "2016-12-19T22:24:08.41Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X/updates"
        }
      }
    }, {
      "id" : "PI2vfrk6Cpv4C3HR55twjcM3",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:07.04Z",
      "updated_at" : "2016-12-19T22:24:07.04Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2vfrk6Cpv4C3HR55twjcM3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2vfrk6Cpv4C3HR55twjcM3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2vfrk6Cpv4C3HR55twjcM3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI2vfrk6Cpv4C3HR55twjcM3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIffqfWcHApxKEPf7UtjNLHN",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:07.04Z",
      "updated_at" : "2016-12-19T22:24:07.04Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIgnVs9FgCEvjxTDrNgnJFyj",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:07.04Z",
      "updated_at" : "2016-12-19T22:24:07.04Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnVs9FgCEvjxTDrNgnJFyj"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnVs9FgCEvjxTDrNgnJFyj/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnVs9FgCEvjxTDrNgnJFyj/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgnVs9FgCEvjxTDrNgnJFyj/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIen8tmn6V1BKXJG8NwHQb5k",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:05.55Z",
      "updated_at" : "2016-12-19T22:24:05.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIen8tmn6V1BKXJG8NwHQb5k"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIen8tmn6V1BKXJG8NwHQb5k/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIen8tmn6V1BKXJG8NwHQb5k/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIen8tmn6V1BKXJG8NwHQb5k/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIrVgAxnAKKs5qXYbdY7Nich",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:05.55Z",
      "updated_at" : "2016-12-19T22:24:05.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrVgAxnAKKs5qXYbdY7Nich"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrVgAxnAKKs5qXYbdY7Nich/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrVgAxnAKKs5qXYbdY7Nich/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrVgAxnAKKs5qXYbdY7Nich/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PI7f7QKxPKQEUWDas5QgDvRR",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:05.55Z",
      "updated_at" : "2016-12-19T22:24:05.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7f7QKxPKQEUWDas5QgDvRR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7f7QKxPKQEUWDas5QgDvRR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7f7QKxPKQEUWDas5QgDvRR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7f7QKxPKQEUWDas5QgDvRR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIbDGJGm7VzzardXpnVRStMm",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:24:05.55Z",
      "updated_at" : "2016-12-19T22:24:05.55Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbDGJGm7VzzardXpnVRStMm"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbDGJGm7VzzardXpnVRStMm/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbDGJGm7VzzardXpnVRStMm/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbDGJGm7VzzardXpnVRStMm/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PI8dJruN5u4Vu2xF9QSjKhVC",
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
      "created_at" : "2016-12-19T22:24:00.63Z",
      "updated_at" : "2016-12-19T22:24:00.63Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8dJruN5u4Vu2xF9QSjKhVC/updates"
        }
      }
    }, {
      "id" : "PITQrb3Bu4GprWsbMhYe52R",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2016-12-19T22:23:53.78Z",
      "updated_at" : "2016-12-19T22:23:53.78Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDbEcrf3hoD61riaKNtoKh9S",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PITQrb3Bu4GprWsbMhYe52R"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PITQrb3Bu4GprWsbMhYe52R/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PITQrb3Bu4GprWsbMhYe52R/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PITQrb3Bu4GprWsbMhYe52R/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "fingerprint" : "FPR-921925016",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Ayisha Serna",
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
      "created_at" : "2016-12-19T22:23:52.93Z",
      "updated_at" : "2016-12-19T22:23:58.28Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDbEcrf3hoD61riaKNtoKh9S",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbEcrf3hoD61riaKNtoKh9S"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J/updates"
        }
      }
    }, {
      "id" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:51.82Z",
      "updated_at" : "2016-12-19T22:23:51.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIobZhY2EtpFSYHkCxGC6yG4",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:51.82Z",
      "updated_at" : "2016-12-19T22:23:51.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIobZhY2EtpFSYHkCxGC6yG4"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIobZhY2EtpFSYHkCxGC6yG4/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIobZhY2EtpFSYHkCxGC6yG4/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIobZhY2EtpFSYHkCxGC6yG4/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PI4hGevivgE3WQT8z6bjcbBz",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:51.82Z",
      "updated_at" : "2016-12-19T22:23:51.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4hGevivgE3WQT8z6bjcbBz"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4hGevivgE3WQT8z6bjcbBz/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4hGevivgE3WQT8z6bjcbBz/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4hGevivgE3WQT8z6bjcbBz/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIapqJzWaZN3QN1aPeqz5fHY",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2016-12-19T22:23:50.93Z",
      "updated_at" : "2016-12-19T22:23:51.44Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIapqJzWaZN3QN1aPeqz5fHY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PI8SeUyWCEu3cHYAqztj5uKN",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:43.17Z",
      "updated_at" : "2016-12-19T22:23:43.17Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PI3rZvQfnRGNC9GGzYKxcxQr",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:43.17Z",
      "updated_at" : "2016-12-19T22:23:43.17Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3rZvQfnRGNC9GGzYKxcxQr"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3rZvQfnRGNC9GGzYKxcxQr/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3rZvQfnRGNC9GGzYKxcxQr/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3rZvQfnRGNC9GGzYKxcxQr/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PIfzt2GqggdT7AZ6PJYWNV8W",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:43.17Z",
      "updated_at" : "2016-12-19T22:23:43.17Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfzt2GqggdT7AZ6PJYWNV8W"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfzt2GqggdT7AZ6PJYWNV8W/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfzt2GqggdT7AZ6PJYWNV8W/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfzt2GqggdT7AZ6PJYWNV8W/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "PImMSYqbLzkVcJugXdt4MX84",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-12-19T22:23:43.17Z",
      "updated_at" : "2016-12-19T22:23:43.17Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImMSYqbLzkVcJugXdt4MX84"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImMSYqbLzkVcJugXdt4MX84/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImMSYqbLzkVcJugXdt4MX84/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImMSYqbLzkVcJugXdt4MX84/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRt1DHe1BPvvPfS99ZSiagEC");

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRt1DHe1BPvvPfS99ZSiagEC');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRt1DHe1BPvvPfS99ZSiagEC")

```
> Example Response:

```json
{
  "id" : "TRt1DHe1BPvvPfS99ZSiagEC",
  "amount" : 336569,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "4895dab2-dbcf-43b8-89e1-f02d96ea9170",
  "currency" : "USD",
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "destination" : "PI8XfT6wpdQn2PV9b14ueiVd",
  "ready_to_settle_at" : null,
  "fee" : 33657,
  "statement_descriptor" : "FNX*ACME ANCHORS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:54.31Z",
  "updated_at" : "2016-12-19T22:23:54.42Z",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
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

curl https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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

$debit = Transfer::retrieve('TRt1DHe1BPvvPfS99ZSiagEC');
$refund = $debit->reverse(11);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRt1DHe1BPvvPfS99ZSiagEC")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRrwGgftC1Hh3KsT6CTDZSz4",
  "amount" : 59694,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "cebd97ae-9eb1-41c0-bf5f-c0625b6fa61d",
  "currency" : "USD",
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "source" : "PI8XfT6wpdQn2PV9b14ueiVd",
  "destination" : "PIhspXZ5VJWgrXwEA4xeMq9J",
  "ready_to_settle_at" : null,
  "fee" : 5969,
  "statement_descriptor" : "FNX*ACME ANCHORS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-12-19T22:23:57.57Z",
  "updated_at" : "2016-12-19T22:23:57.63Z",
  "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRrwGgftC1Hh3KsT6CTDZSz4"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRrwGgftC1Hh3KsT6CTDZSz4/payment_instruments"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

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
      "id" : "TR8dHtovLMAzH1bZo6iPvi7H",
      "amount" : 33646,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "aa4adf17-e457-46f8-a5b3-aef010018a29",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "destination" : "PI3rZvQfnRGNC9GGzYKxcxQr",
      "ready_to_settle_at" : "2016-12-19T22:24:07.43Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:09.93Z",
      "updated_at" : "2016-12-19T22:24:11.51Z",
      "merchant_identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR8dHtovLMAzH1bZo6iPvi7H"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR8dHtovLMAzH1bZo6iPvi7H/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDd8xfHisExXe2KQx3e7rhwH"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR8dHtovLMAzH1bZo6iPvi7H/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR8dHtovLMAzH1bZo6iPvi7H/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR8dHtovLMAzH1bZo6iPvi7H/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3rZvQfnRGNC9GGzYKxcxQr"
        }
      }
    }, {
      "id" : "TRsuTiE6Z8jAnerJKPdqYh41",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "184730",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PIffqfWcHApxKEPf7UtjNLHN",
      "destination" : "PIxnxLTU7SS7WYyptRQvoc7X",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:09.10Z",
      "updated_at" : "2016-12-19T22:24:10.35Z",
      "merchant_identity" : "IDcN2K7fZNas88DgJ5YAkQky",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcN2K7fZNas88DgJ5YAkQky"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsuTiE6Z8jAnerJKPdqYh41/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIffqfWcHApxKEPf7UtjNLHN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIxnxLTU7SS7WYyptRQvoc7X"
        }
      }
    }, {
      "id" : "TRoG4N2g4REVMPSaNyHc4Fot",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "219ef079-0b1b-4e6c-bf63-451d680bcfa8",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "destination" : "PI8SeUyWCEu3cHYAqztj5uKN",
      "ready_to_settle_at" : "2016-12-19T22:24:07.43Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:08.30Z",
      "updated_at" : "2016-12-19T22:24:09.73Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRoG4N2g4REVMPSaNyHc4Fot"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRoG4N2g4REVMPSaNyHc4Fot/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRoG4N2g4REVMPSaNyHc4Fot/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRoG4N2g4REVMPSaNyHc4Fot/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRoG4N2g4REVMPSaNyHc4Fot/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN"
        }
      }
    }, {
      "id" : "TRhroxaDFdjj4ySoGyqAeYfN",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "79fae952-f1e9-434b-88ce-5f236bd90796",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "destination" : "PI8SeUyWCEu3cHYAqztj5uKN",
      "ready_to_settle_at" : "2016-12-19T22:24:03.26Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:24:04.16Z",
      "updated_at" : "2016-12-19T22:24:06.51Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRhroxaDFdjj4ySoGyqAeYfN"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRhroxaDFdjj4ySoGyqAeYfN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRhroxaDFdjj4ySoGyqAeYfN/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRhroxaDFdjj4ySoGyqAeYfN/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRhroxaDFdjj4ySoGyqAeYfN/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8SeUyWCEu3cHYAqztj5uKN"
        }
      }
    }, {
      "id" : "TRfDAHgqDUk423PyTf6uAUbY",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c3b6aaff-178f-4da9-8149-33eecaadc1c9",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "destination" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "ready_to_settle_at" : "2016-12-19T22:24:03.33Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:23:58.84Z",
      "updated_at" : "2016-12-19T22:24:02.77Z",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRfDAHgqDUk423PyTf6uAUbY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        }
      }
    }, {
      "id" : "TRrwGgftC1Hh3KsT6CTDZSz4",
      "amount" : 59694,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "49290c87-f49b-4c53-9307-4366dc15660d",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "destination" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "ready_to_settle_at" : null,
      "fee" : 5969,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:23:57.47Z",
      "updated_at" : "2016-12-19T22:23:57.63Z",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRrwGgftC1Hh3KsT6CTDZSz4"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRrwGgftC1Hh3KsT6CTDZSz4/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
        }
      }
    }, {
      "id" : "TRuAdw3CUQQh1hoCpRiLmSRq",
      "amount" : 59694,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "9d659ddd-c14f-4244-97ba-6d7f6fc69b0e",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "destination" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "ready_to_settle_at" : null,
      "fee" : 5969,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:23:57.00Z",
      "updated_at" : "2016-12-19T22:23:57.54Z",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRuAdw3CUQQh1hoCpRiLmSRq/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
        }
      }
    }, {
      "id" : "TRt1DHe1BPvvPfS99ZSiagEC",
      "amount" : 336569,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "4895dab2-dbcf-43b8-89e1-f02d96ea9170",
      "currency" : "USD",
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "source" : "PIhspXZ5VJWgrXwEA4xeMq9J",
      "destination" : "PI8XfT6wpdQn2PV9b14ueiVd",
      "ready_to_settle_at" : "2016-12-19T22:24:08.56Z",
      "fee" : 33657,
      "statement_descriptor" : "FNX*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-12-19T22:23:54.31Z",
      "updated_at" : "2016-12-19T22:24:05.87Z",
      "merchant_identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRt1DHe1BPvvPfS99ZSiagEC/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhspXZ5VJWgrXwEA4xeMq9J"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8XfT6wpdQn2PV9b14ueiVd"
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
    "count" : 8
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers`
# Users (API Keys)

A `User` resource represents a pair of API keys which are used to perform
authenticated requests against the CrossRiver API. When making authenticated
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
curl https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'

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
  "id" : "USfvn7Qihw1V6XygqQY3PwRi",
  "password" : "4392cc9c-07f1-4eac-91df-79ade2337e2c",
  "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:44.02Z",
  "updated_at" : "2016-12-19T22:23:44.02Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USfvn7Qihw1V6XygqQY3PwRi"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/identities/IDb8q27oRPi4NgXidKK8qbcD/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
    -d '{}'

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
  "id" : "USonEP8vBQ5kXUMJn2vH7c1v",
  "password" : "b81f1d76-35a4-426c-8772-bbac79406cd7",
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:55.01Z",
  "updated_at" : "2016-12-19T22:23:55.01Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USonEP8vBQ5kXUMJn2vH7c1v"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/users/TRt1DHe1BPvvPfS99ZSiagEC \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php

```
```python


from crossriver.resources import User
user = User.get(id="USjeUio4zHU9eEsLqnE6d7Wu")

```
> Example Response:

```json
{
  "id" : "USjeUio4zHU9eEsLqnE6d7Wu",
  "password" : null,
  "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:42.05Z",
  "updated_at" : "2016-12-19T22:23:42.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjeUio4zHU9eEsLqnE6d7Wu"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
curl https://api-staging.finix.io/users/USonEP8vBQ5kXUMJn2vH7c1v \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
> Example Response:

```json
{
  "id" : "USonEP8vBQ5kXUMJn2vH7c1v",
  "password" : null,
  "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-12-19T22:23:54.98Z",
  "updated_at" : "2016-12-19T22:23:55.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USonEP8vBQ5kXUMJn2vH7c1v"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

```
```java

```
```php
<?php

```
```python


from crossriver.resources import User
users = User.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USonEP8vBQ5kXUMJn2vH7c1v",
      "password" : null,
      "identity" : "IDb8q27oRPi4NgXidKK8qbcD",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-12-19T22:23:54.98Z",
      "updated_at" : "2016-12-19T22:23:56.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USonEP8vBQ5kXUMJn2vH7c1v"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "USfvn7Qihw1V6XygqQY3PwRi",
      "password" : null,
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-12-19T22:23:44.01Z",
      "updated_at" : "2016-12-19T22:23:44.01Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USfvn7Qihw1V6XygqQY3PwRi"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
        }
      }
    }, {
      "id" : "USjeUio4zHU9eEsLqnE6d7Wu",
      "password" : null,
      "identity" : "IDd8xfHisExXe2KQx3e7rhwH",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-12-19T22:23:42.05Z",
      "updated_at" : "2016-12-19T22:23:42.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USjeUio4zHU9eEsLqnE6d7Wu"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1 \
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
  "id" : "WH6bDJRhaL69Yb8gyNWqN6Ns",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "created_at" : "2016-12-19T22:23:45.36Z",
  "updated_at" : "2016-12-19T22:23:45.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH6bDJRhaL69Yb8gyNWqN6Ns"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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



curl https://api-staging.finix.io/webhooks/WH6bDJRhaL69Yb8gyNWqN6Ns \
    -H "Content-Type: application/vnd.json+api" \
    -u USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH6bDJRhaL69Yb8gyNWqN6Ns");

```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WH6bDJRhaL69Yb8gyNWqN6Ns');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WH6bDJRhaL69Yb8gyNWqN6Ns")

```
> Example Response:

```json
{
  "id" : "WH6bDJRhaL69Yb8gyNWqN6Ns",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
  "created_at" : "2016-12-19T22:23:45.36Z",
  "updated_at" : "2016-12-19T22:23:45.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WH6bDJRhaL69Yb8gyNWqN6Ns"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
    -u  USjeUio4zHU9eEsLqnE6d7Wu:cba316d5-c3ef-41ca-8733-d4e3fbaaa7b1

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
      "id" : "WH6bDJRhaL69Yb8gyNWqN6Ns",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APnGK9w9wFhyeFxfZnFvKwSh",
      "created_at" : "2016-12-19T22:23:45.36Z",
      "updated_at" : "2016-12-19T22:23:45.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WH6bDJRhaL69Yb8gyNWqN6Ns"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnGK9w9wFhyeFxfZnFvKwSh"
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
