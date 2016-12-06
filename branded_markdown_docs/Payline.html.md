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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```php
<?php

// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);

require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("USmAQ8t77QraWU17YWM6jjjQ", "a41df9e6-2dce-4ad9-87ce-1da2d794db44"))

```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USmAQ8t77QraWU17YWM6jjjQ`

- Password: `a41df9e6-2dce-4ad9-87ce-1da2d794db44`

- Application ID: `APmE1ycLBmsgMx4gXoToVnLL`

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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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
	        "default_statement_descriptor": "Petes Coffee", 
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
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PetesCoffee.com", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
	        "default_statement_descriptor"=> "Petes Coffee", 
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
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PetesCoffee.com", 
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
	        "default_statement_descriptor": "Petes Coffee", 
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
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PetesCoffee.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-29T22:56:05.17Z",
  "updated_at" : "2016-11-29T22:56:05.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
	    "identity"=> "IDci9dFHHcUcfUCs4Gn72cRN"
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
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI7oLHdpoK2U6bvoU5BRu761",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T22:56:16.98Z",
  "updated_at" : "2016-11-29T22:56:16.98Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDci9dFHHcUcfUCs4Gn72cRN');

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

identity = Identity.get(id="IDci9dFHHcUcfUCs4Gn72cRN")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "verification" : "VInbqsrBcJbWC1sxsxHMPVyo",
  "merchant_profile" : "MPbT7hyqtvS5CiWhC2NmkpzY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T22:56:30.98Z",
  "updated_at" : "2016-11-29T22:56:30.98Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPbT7hyqtvS5CiWhC2NmkpzY"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VInbqsrBcJbWC1sxsxHMPVyo"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
> Example Response:

```json
{
  "id" : "IDvBmWTYJSrWDKwZuPnUFV2j",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-29T22:56:35.28Z",
  "updated_at" : "2016-11-29T22:56:35.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "name": "Walter Sterling", 
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
	    "identity": "IDvBmWTYJSrWDKwZuPnUFV2j"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Walter Sterling", 
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
	    "identity"=> "IDvBmWTYJSrWDKwZuPnUFV2j"
	));
$card = $card->save();


```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Sterling", 
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
	    "identity": "IDvBmWTYJSrWDKwZuPnUFV2j"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "fingerprint" : "FPR1798353012",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Sterling",
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
  "created_at" : "2016-11-29T22:56:36.14Z",
  "updated_at" : "2016-11-29T22:56:36.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDvBmWTYJSrWDKwZuPnUFV2j",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/updates"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "merchant_identity": "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh1Y21TC9DY7fG1t2juRL2x", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIh1Y21TC9DY7fG1t2juRL2x", 
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
	    "merchant_identity": "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh1Y21TC9DY7fG1t2juRL2x", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUfaL57h9QgPrgZvNhscNHpD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:47.36Z",
  "updated_at" : "2016-11-29T22:56:47.55Z",
  "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : false,
  "expires_at" : "2016-12-06T22:56:47.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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
curl https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUfaL57h9QgPrgZvNhscNHpD");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUfaL57h9QgPrgZvNhscNHpD');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUfaL57h9QgPrgZvNhscNHpD")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUfaL57h9QgPrgZvNhscNHpD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR28iRVdxQhvvhWPHT1qfUJN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:47.28Z",
  "updated_at" : "2016-11-29T22:56:49.70Z",
  "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : false,
  "expires_at" : "2016-12-06T22:56:47.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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
          applicationId: 'APmE1ycLBmsgMx4gXoToVnLL',
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
  "id" : "TK8vDGkdBrAnc6LnZcwP7KJp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-29T22:56:53.72Z",
  "updated_at" : "2016-11-29T22:56:53.72Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-30T22:56:53.72Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI8vDGkdBrAnc6LnZcwP7KJp",
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
  "created_at" : "2016-11-29T22:56:54.39Z",
  "updated_at" : "2016-11-29T22:56:54.39Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/updates"
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
    applicationId: "APmE1ycLBmsgMx4gXoToVnLL",
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
  "id" : "TK8vDGkdBrAnc6LnZcwP7KJp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-29T22:56:53.72Z",
  "updated_at" : "2016-11-29T22:56:53.72Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-30T22:56:53.72Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI8vDGkdBrAnc6LnZcwP7KJp",
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
  "created_at" : "2016-11-29T22:56:54.39Z",
  "updated_at" : "2016-11-29T22:56:54.39Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/updates"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "merchant_identity": "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh1Y21TC9DY7fG1t2juRL2x", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIh1Y21TC9DY7fG1t2juRL2x", 
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
	    "merchant_identity": "IDci9dFHHcUcfUCs4Gn72cRN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIh1Y21TC9DY7fG1t2juRL2x", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUfaL57h9QgPrgZvNhscNHpD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:47.36Z",
  "updated_at" : "2016-11-29T22:56:47.55Z",
  "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : false,
  "expires_at" : "2016-12-06T22:56:47.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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
curl https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUfaL57h9QgPrgZvNhscNHpD");
authorization = authorization.capture(50L);

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUfaL57h9QgPrgZvNhscNHpD');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUfaL57h9QgPrgZvNhscNHpD")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUfaL57h9QgPrgZvNhscNHpD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR28iRVdxQhvvhWPHT1qfUJN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:47.28Z",
  "updated_at" : "2016-11-29T22:56:49.70Z",
  "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : false,
  "expires_at" : "2016-12-06T22:56:47.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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

curl https://api-test.payline.io/authorizations/AU68aiydDJXfcMsG32GbvQzQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUfaL57h9QgPrgZvNhscNHpD")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AU68aiydDJXfcMsG32GbvQzQ",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:56.50Z",
  "updated_at" : "2016-11-29T22:56:58.19Z",
  "trace_id" : "54ec4b9f-7563-4fe1-a83b-542f2530b83e",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : true,
  "expires_at" : "2016-12-06T22:56:56.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU68aiydDJXfcMsG32GbvQzQ"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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

curl https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUfaL57h9QgPrgZvNhscNHpD");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUfaL57h9QgPrgZvNhscNHpD');

```
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AUfaL57h9QgPrgZvNhscNHpD")
```
> Example Response:

```json
{
  "id" : "AUfaL57h9QgPrgZvNhscNHpD",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR28iRVdxQhvvhWPHT1qfUJN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:47.28Z",
  "updated_at" : "2016-11-29T22:56:49.70Z",
  "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "is_void" : false,
  "expires_at" : "2016-12-06T22:56:47.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "AU68aiydDJXfcMsG32GbvQzQ",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T22:56:56.50Z",
      "updated_at" : "2016-11-29T22:56:58.19Z",
      "trace_id" : "54ec4b9f-7563-4fe1-a83b-542f2530b83e",
      "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "is_void" : true,
      "expires_at" : "2016-12-06T22:56:56.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AU68aiydDJXfcMsG32GbvQzQ"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        }
      }
    }, {
      "id" : "AUfaL57h9QgPrgZvNhscNHpD",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR28iRVdxQhvvhWPHT1qfUJN",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T22:56:47.28Z",
      "updated_at" : "2016-11-29T22:56:49.70Z",
      "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
      "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "is_void" : false,
      "expires_at" : "2016-12-06T22:56:47.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUfaL57h9QgPrgZvNhscNHpD"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
> Example Response:

```json
{
  "id" : "IDvBmWTYJSrWDKwZuPnUFV2j",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-29T22:56:35.28Z",
  "updated_at" : "2016-11-29T22:56:35.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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
	        "default_statement_descriptor": "Petes Coffee", 
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
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PetesCoffee.com", 
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
	        "default_statement_descriptor"=> "Petes Coffee", 
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
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PetesCoffee.com", 
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
	        "default_statement_descriptor": "Petes Coffee", 
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
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PetesCoffee.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-29T22:56:05.17Z",
  "updated_at" : "2016-11-29T22:56:05.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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

curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDci9dFHHcUcfUCs4Gn72cRN");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDci9dFHHcUcfUCs4Gn72cRN');
```
```python


from payline.resources import Identity
identity = Identity.get(id="IDci9dFHHcUcfUCs4Gn72cRN")

```
> Example Response:

```json
{
  "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-11-29T22:56:05.16Z",
  "updated_at" : "2016-11-29T22:56:05.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44


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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "IDvBmWTYJSrWDKwZuPnUFV2j",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-29T22:56:35.25Z",
      "updated_at" : "2016-11-29T22:56:35.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDqF6bUM8pziC6SLPXnUNqqV",
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
      "created_at" : "2016-11-29T22:56:15.35Z",
      "updated_at" : "2016-11-29T22:56:15.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDpj2iEJ1UiSXrwjBCmkVby6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-29T22:56:14.39Z",
      "updated_at" : "2016-11-29T22:56:14.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDbkwPTHMQmmNuufe2adCu6L",
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
      "created_at" : "2016-11-29T22:56:13.51Z",
      "updated_at" : "2016-11-29T22:56:13.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDqq2DMWfrdjVdbT7CmgGZZc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-29T22:56:11.55Z",
      "updated_at" : "2016-11-29T22:56:11.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDhoQ8znpRhLsMtbQyd6BKAB",
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
      "created_at" : "2016-11-29T22:56:10.71Z",
      "updated_at" : "2016-11-29T22:56:10.71Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDhnmpJQpUFV6QiTcNcWNjCv",
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
      "created_at" : "2016-11-29T22:56:09.78Z",
      "updated_at" : "2016-11-29T22:56:09.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDpzgQpQanAXpJzaLzkyfZUr",
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
      "created_at" : "2016-11-29T22:56:08.80Z",
      "updated_at" : "2016-11-29T22:56:08.80Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "ID7d8hhUfV9XCAAEmZd5Sekp",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-11-29T22:56:07.29Z",
      "updated_at" : "2016-11-29T22:56:07.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "ID8AH94icAePiPQnBxxn7LMF",
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
      "created_at" : "2016-11-29T22:56:06.23Z",
      "updated_at" : "2016-11-29T22:56:06.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-29T22:56:05.16Z",
      "updated_at" : "2016-11-29T22:56:05.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDiEqfWMGveafDrekHKiuxPo",
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
      "created_at" : "2016-11-29T22:55:58.41Z",
      "updated_at" : "2016-11-29T22:55:58.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Walter", 
	        "last_name": "Jones", 
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
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Walter",
    "last_name" : "Jones",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-29T22:56:05.16Z",
  "updated_at" : "2016-11-29T22:57:17.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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

curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDci9dFHHcUcfUCs4Gn72cRN');

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

identity = Identity.get(id="IDci9dFHHcUcfUCs4Gn72cRN")
merchant = identity.provision_merchant_on(Merchant())

```

> Example Response:

```json
{
  "id" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "verification" : "VInbqsrBcJbWC1sxsxHMPVyo",
  "merchant_profile" : "MPbT7hyqtvS5CiWhC2NmkpzY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T22:56:30.98Z",
  "updated_at" : "2016-11-29T22:56:30.98Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPbT7hyqtvS5CiWhC2NmkpzY"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VInbqsrBcJbWC1sxsxHMPVyo"
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
curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDci9dFHHcUcfUCs4Gn72cRN');

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

identity = Identity.get(id="IDci9dFHHcUcfUCs4Gn72cRN")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "verification" : "VInbqsrBcJbWC1sxsxHMPVyo",
  "merchant_profile" : "MPbT7hyqtvS5CiWhC2NmkpzY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-29T22:56:30.98Z",
  "updated_at" : "2016-11-29T22:56:30.98Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPbT7hyqtvS5CiWhC2NmkpzY"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VInbqsrBcJbWC1sxsxHMPVyo"
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
curl https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUnes7LTRELFtHq3a4JC21Ao");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUnes7LTRELFtHq3a4JC21Ao');

```
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUnes7LTRELFtHq3a4JC21Ao")

```
> Example Response:

```json
{
  "id" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "verification" : null,
  "merchant_profile" : "MPbT7hyqtvS5CiWhC2NmkpzY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-29T22:56:30.89Z",
  "updated_at" : "2016-11-29T22:56:31.53Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPbT7hyqtvS5CiWhC2NmkpzY"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "USdmayET4q4W5qUKPqARDFox",
  "password" : "7ac94379-eacc-4d39-8c61-f89b40fe2427",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-29T22:56:40.64Z",
  "updated_at" : "2016-11-29T22:56:40.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/USdmayET4q4W5qUKPqARDFox"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '{}'
```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIjHkgXvgSLVZ1AsQkp7sLov",
  "external_trace_id" : "f0cf7b68-e058-4146-9df7-ef1a8edfd49e",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-29T22:57:19.20Z",
  "updated_at" : "2016-11-29T22:57:19.22Z",
  "trace_id" : "f0cf7b68-e058-4146-9df7-ef1a8edfd49e",
  "payment_instrument" : null,
  "merchant" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIjHkgXvgSLVZ1AsQkp7sLov"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
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
curl https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '{}'

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "VIjHkgXvgSLVZ1AsQkp7sLov",
  "external_trace_id" : "f0cf7b68-e058-4146-9df7-ef1a8edfd49e",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-29T22:57:19.20Z",
  "updated_at" : "2016-11-29T22:57:19.22Z",
  "trace_id" : "f0cf7b68-e058-4146-9df7-ef1a8edfd49e",
  "payment_instrument" : null,
  "merchant" : "MUnes7LTRELFtHq3a4JC21Ao",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIjHkgXvgSLVZ1AsQkp7sLov"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "MUnes7LTRELFtHq3a4JC21Ao",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "verification" : null,
      "merchant_profile" : "MPbT7hyqtvS5CiWhC2NmkpzY",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-29T22:56:30.89Z",
      "updated_at" : "2016-11-29T22:56:31.53Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPbT7hyqtvS5CiWhC2NmkpzY"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/merchants/MUnes7LTRELFtHq3a4JC21Ao/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

```
```java

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "IDvBmWTYJSrWDKwZuPnUFV2j",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-29T22:56:35.25Z",
      "updated_at" : "2016-11-29T22:56:35.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDqF6bUM8pziC6SLPXnUNqqV",
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
      "created_at" : "2016-11-29T22:56:15.35Z",
      "updated_at" : "2016-11-29T22:56:15.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqF6bUM8pziC6SLPXnUNqqV/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDpj2iEJ1UiSXrwjBCmkVby6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-29T22:56:14.39Z",
      "updated_at" : "2016-11-29T22:56:14.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpj2iEJ1UiSXrwjBCmkVby6/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDbkwPTHMQmmNuufe2adCu6L",
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
      "created_at" : "2016-11-29T22:56:13.51Z",
      "updated_at" : "2016-11-29T22:56:13.51Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDbkwPTHMQmmNuufe2adCu6L/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDqq2DMWfrdjVdbT7CmgGZZc",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-29T22:56:11.55Z",
      "updated_at" : "2016-11-29T22:56:11.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqq2DMWfrdjVdbT7CmgGZZc/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDhoQ8znpRhLsMtbQyd6BKAB",
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
      "created_at" : "2016-11-29T22:56:10.71Z",
      "updated_at" : "2016-11-29T22:56:10.71Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhoQ8znpRhLsMtbQyd6BKAB/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDhnmpJQpUFV6QiTcNcWNjCv",
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
      "created_at" : "2016-11-29T22:56:09.78Z",
      "updated_at" : "2016-11-29T22:56:09.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhnmpJQpUFV6QiTcNcWNjCv/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDpzgQpQanAXpJzaLzkyfZUr",
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
      "created_at" : "2016-11-29T22:56:08.80Z",
      "updated_at" : "2016-11-29T22:56:08.80Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpzgQpQanAXpJzaLzkyfZUr/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "ID7d8hhUfV9XCAAEmZd5Sekp",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-11-29T22:56:07.29Z",
      "updated_at" : "2016-11-29T22:56:07.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID7d8hhUfV9XCAAEmZd5Sekp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "ID8AH94icAePiPQnBxxn7LMF",
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
      "created_at" : "2016-11-29T22:56:06.23Z",
      "updated_at" : "2016-11-29T22:56:06.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID8AH94icAePiPQnBxxn7LMF/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-11-29T22:56:05.16Z",
      "updated_at" : "2016-11-29T22:56:05.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "IDiEqfWMGveafDrekHKiuxPo",
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
      "created_at" : "2016-11-29T22:55:58.41Z",
      "updated_at" : "2016-11-29T22:55:58.46Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "name": "Walter Sterling", 
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
	    "identity": "IDvBmWTYJSrWDKwZuPnUFV2j"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Walter Sterling", 
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
	    "identity"=> "IDvBmWTYJSrWDKwZuPnUFV2j"
	));
$card = $card->save();


```
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Sterling", 
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
	    "identity": "IDvBmWTYJSrWDKwZuPnUFV2j"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "fingerprint" : "FPR1798353012",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Sterling",
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
  "created_at" : "2016-11-29T22:56:36.14Z",
  "updated_at" : "2016-11-29T22:56:36.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDvBmWTYJSrWDKwZuPnUFV2j",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/updates"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
	    "identity"=> "IDci9dFHHcUcfUCs4Gn72cRN"
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
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI7oLHdpoK2U6bvoU5BRu761",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T22:56:16.98Z",
  "updated_at" : "2016-11-29T22:56:16.98Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
          applicationId: 'APmE1ycLBmsgMx4gXoToVnLL',
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
  "id" : "TK8vDGkdBrAnc6LnZcwP7KJp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-29T22:56:53.72Z",
  "updated_at" : "2016-11-29T22:56:53.72Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-30T22:56:53.72Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    }
  }
}
```

```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	});
$card = $card->save();

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PI8vDGkdBrAnc6LnZcwP7KJp",
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
  "created_at" : "2016-11-29T22:56:54.39Z",
  "updated_at" : "2016-11-29T22:56:54.39Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/updates"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
    -d '
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	});
$card = $card->save();

```
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK8vDGkdBrAnc6LnZcwP7KJp", 
	    "type": "TOKEN", 
	    "identity": "IDci9dFHHcUcfUCs4Gn72cRN"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI8vDGkdBrAnc6LnZcwP7KJp",
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
  "created_at" : "2016-11-29T22:56:54.39Z",
  "updated_at" : "2016-11-29T22:56:54.39Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/updates"
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


curl https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PI7oLHdpoK2U6bvoU5BRu761")

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI7oLHdpoK2U6bvoU5BRu761');

```
```python



```
> Example Response:

```json
{
  "id" : "PI7oLHdpoK2U6bvoU5BRu761",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T22:56:16.92Z",
  "updated_at" : "2016-11-29T22:56:17.90Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
curl https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```python



```
> Example Response:

```json
{
  "id" : "PI7oLHdpoK2U6bvoU5BRu761",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-29T22:56:16.92Z",
  "updated_at" : "2016-11-29T22:56:17.90Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "PI8vDGkdBrAnc6LnZcwP7KJp",
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
      "created_at" : "2016-11-29T22:56:54.30Z",
      "updated_at" : "2016-11-29T22:56:54.30Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8vDGkdBrAnc6LnZcwP7KJp/updates"
        }
      }
    }, {
      "id" : "PI8dKi6KgUmd5EcxdUEEwZad",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-29T22:56:37.07Z",
      "updated_at" : "2016-11-29T22:56:37.07Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDvBmWTYJSrWDKwZuPnUFV2j",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8dKi6KgUmd5EcxdUEEwZad"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8dKi6KgUmd5EcxdUEEwZad/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8dKi6KgUmd5EcxdUEEwZad/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI8dKi6KgUmd5EcxdUEEwZad/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "fingerprint" : "FPR1798353012",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Walter Sterling",
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
      "created_at" : "2016-11-29T22:56:36.09Z",
      "updated_at" : "2016-11-29T22:56:47.46Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDvBmWTYJSrWDKwZuPnUFV2j",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDvBmWTYJSrWDKwZuPnUFV2j"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x/updates"
        }
      }
    }, {
      "id" : "PIfyxirv1pPN7yNr91o7ScRf",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:56:30.89Z",
      "updated_at" : "2016-11-29T22:56:30.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfyxirv1pPN7yNr91o7ScRf"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfyxirv1pPN7yNr91o7ScRf/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfyxirv1pPN7yNr91o7ScRf/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfyxirv1pPN7yNr91o7ScRf/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIjS4d6Az8v9yRFHgpQ6Pbje",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:56:30.89Z",
      "updated_at" : "2016-11-29T22:56:30.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjS4d6Az8v9yRFHgpQ6Pbje"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjS4d6Az8v9yRFHgpQ6Pbje/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjS4d6Az8v9yRFHgpQ6Pbje/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjS4d6Az8v9yRFHgpQ6Pbje/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIjX6hxC7gzBAED2qqMw1m1U",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:56:30.89Z",
      "updated_at" : "2016-11-29T22:56:30.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PI7oLHdpoK2U6bvoU5BRu761",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-29T22:56:16.92Z",
      "updated_at" : "2016-11-29T22:56:17.90Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI7oLHdpoK2U6bvoU5BRu761/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIxwnTLsyfurCvTjYDDKFkLC",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:55:59.89Z",
      "updated_at" : "2016-11-29T22:55:59.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiEqfWMGveafDrekHKiuxPo",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxwnTLsyfurCvTjYDDKFkLC"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxwnTLsyfurCvTjYDDKFkLC/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxwnTLsyfurCvTjYDDKFkLC/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIxwnTLsyfurCvTjYDDKFkLC/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIoNQ73RG79nuzQQHcv3fuFD",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:55:59.89Z",
      "updated_at" : "2016-11-29T22:55:59.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiEqfWMGveafDrekHKiuxPo",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIoNQ73RG79nuzQQHcv3fuFD"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIoNQ73RG79nuzQQHcv3fuFD/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIoNQ73RG79nuzQQHcv3fuFD/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIoNQ73RG79nuzQQHcv3fuFD/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIx1PaKMab1AzFM7zvihAA4V",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:55:59.89Z",
      "updated_at" : "2016-11-29T22:55:59.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIx1PaKMab1AzFM7zvihAA4V"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIx1PaKMab1AzFM7zvihAA4V/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIx1PaKMab1AzFM7zvihAA4V/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIx1PaKMab1AzFM7zvihAA4V/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        }
      }
    }, {
      "id" : "PIuJsfRcQLqGvCR2byRhsNLQ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-29T22:55:59.89Z",
      "updated_at" : "2016-11-29T22:55:59.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDiEqfWMGveafDrekHKiuxPo",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuJsfRcQLqGvCR2byRhsNLQ"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuJsfRcQLqGvCR2byRhsNLQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDiEqfWMGveafDrekHKiuxPo"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuJsfRcQLqGvCR2byRhsNLQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIuJsfRcQLqGvCR2byRhsNLQ/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
</puthon 
## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44


```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR6HE8ayfENdtk6qqnbWqLfA");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TR6HE8ayfENdtk6qqnbWqLfA');



```
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TR6HE8ayfENdtk6qqnbWqLfA")

```
> Example Response:

```json
{
  "id" : "TR6HE8ayfENdtk6qqnbWqLfA",
  "amount" : 182430,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "6f8a36ad-8ef4-4358-92e2-3fe9c7f442f4",
  "currency" : "USD",
  "application" : "APmE1ycLBmsgMx4gXoToVnLL",
  "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "destination" : "PIjX6hxC7gzBAED2qqMw1m1U",
  "ready_to_settle_at" : null,
  "fee" : 18243,
  "statement_descriptor" : "PLD*PETES COFFEE",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:38.05Z",
  "updated_at" : "2016-11-29T22:56:43.68Z",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U"
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

curl https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TR6HE8ayfENdtk6qqnbWqLfA');
$refund = $debit->reverse(50);
```
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TR6HE8ayfENdtk6qqnbWqLfA")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TR3jjomfs3gcRvwNBq8qb9VJ",
  "amount" : 182430,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "12c0fedb-d6d4-47ab-8258-2c5d49bcd73c",
  "currency" : "USD",
  "application" : "APmE1ycLBmsgMx4gXoToVnLL",
  "source" : "PIjX6hxC7gzBAED2qqMw1m1U",
  "destination" : "PIh1Y21TC9DY7fG1t2juRL2x",
  "ready_to_settle_at" : null,
  "fee" : 18243,
  "statement_descriptor" : "PLD*PETES COFFEE",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-29T22:56:44.40Z",
  "updated_at" : "2016-11-29T22:56:45.00Z",
  "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR3jjomfs3gcRvwNBq8qb9VJ"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR3jjomfs3gcRvwNBq8qb9VJ/payment_instruments"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "TR28iRVdxQhvvhWPHT1qfUJN",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "8a3dc180-7a1a-47b3-9076-a750067efc4a",
      "currency" : "USD",
      "application" : "APmE1ycLBmsgMx4gXoToVnLL",
      "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "destination" : "PIjX6hxC7gzBAED2qqMw1m1U",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T22:56:48.90Z",
      "updated_at" : "2016-11-29T22:56:49.70Z",
      "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR28iRVdxQhvvhWPHT1qfUJN/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U"
        }
      }
    }, {
      "id" : "TR3jjomfs3gcRvwNBq8qb9VJ",
      "amount" : 182430,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6bd09e09-f9a4-4e92-bdb6-304ca06eefeb",
      "currency" : "USD",
      "application" : "APmE1ycLBmsgMx4gXoToVnLL",
      "source" : "PIjX6hxC7gzBAED2qqMw1m1U",
      "destination" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "ready_to_settle_at" : null,
      "fee" : 18243,
      "statement_descriptor" : "PLD*PETES COFFEE",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T22:56:43.14Z",
      "updated_at" : "2016-11-29T22:56:45.00Z",
      "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR3jjomfs3gcRvwNBq8qb9VJ"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR3jjomfs3gcRvwNBq8qb9VJ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
        }
      }
    }, {
      "id" : "TR6HE8ayfENdtk6qqnbWqLfA",
      "amount" : 182430,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "6f8a36ad-8ef4-4358-92e2-3fe9c7f442f4",
      "currency" : "USD",
      "application" : "APmE1ycLBmsgMx4gXoToVnLL",
      "source" : "PIh1Y21TC9DY7fG1t2juRL2x",
      "destination" : "PIjX6hxC7gzBAED2qqMw1m1U",
      "ready_to_settle_at" : null,
      "fee" : 18243,
      "statement_descriptor" : "PLD*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-29T22:56:38.05Z",
      "updated_at" : "2016-11-29T22:56:43.68Z",
      "merchant_identity" : "IDci9dFHHcUcfUCs4Gn72cRN",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDci9dFHHcUcfUCs4Gn72cRN"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR6HE8ayfENdtk6qqnbWqLfA/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIh1Y21TC9DY7fG1t2juRL2x"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIjX6hxC7gzBAED2qqMw1m1U"
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
    -u USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44 \
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
  "id" : "WH8K7uvtQnBSq3k7AJcisxJW",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APmE1ycLBmsgMx4gXoToVnLL",
  "created_at" : "2016-11-29T22:56:04.66Z",
  "updated_at" : "2016-11-29T22:56:04.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WH8K7uvtQnBSq3k7AJcisxJW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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



curl https://api-test.payline.io/webhooks/WH8K7uvtQnBSq3k7AJcisxJW \
    -H "Content-Type: application/vnd.json+api" \
    -u USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44


```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WH8K7uvtQnBSq3k7AJcisxJW");

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WH8K7uvtQnBSq3k7AJcisxJW');



```
```python


from payline.resources import Webhook
webhook = Webhook.get(id="WH8K7uvtQnBSq3k7AJcisxJW")

```
> Example Response:

```json
{
  "id" : "WH8K7uvtQnBSq3k7AJcisxJW",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APmE1ycLBmsgMx4gXoToVnLL",
  "created_at" : "2016-11-29T22:56:04.68Z",
  "updated_at" : "2016-11-29T22:56:04.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WH8K7uvtQnBSq3k7AJcisxJW"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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
    -u  USmAQ8t77QraWU17YWM6jjjQ:a41df9e6-2dce-4ad9-87ce-1da2d794db44

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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
      "id" : "WH8K7uvtQnBSq3k7AJcisxJW",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APmE1ycLBmsgMx4gXoToVnLL",
      "created_at" : "2016-11-29T22:56:04.68Z",
      "updated_at" : "2016-11-29T22:56:04.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WH8K7uvtQnBSq3k7AJcisxJW"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APmE1ycLBmsgMx4gXoToVnLL"
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

Payline\Settings::configure([
	"root_url" => 'https://api-test.payline.io',
	"username" => 'USmAQ8t77QraWU17YWM6jjjQ',
	"password" => 'a41df9e6-2dce-4ad9-87ce-1da2d794db44']
	);


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
