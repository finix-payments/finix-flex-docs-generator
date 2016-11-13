---
title: Payline API Reference

language_tabs:
- shell: cURL
- python: Python
- php: PHP
- java: Java



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

3. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.

4. [Push-to-Card Private](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```python


# To install the python client run the command below from your terminal:
# pip install payline

import payline

from payline.config import configure
configure(root_url="https://api-test.payline.io", auth=("US2WyUiuGyjYM2sKVMjXNmz7", "27338be5-b4b6-4202-96bf-33c6cf21545a"))

```
```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-test.payline.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```java

```
To communicate with the Payline API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US2WyUiuGyjYM2sKVMjXNmz7`

- Password: `27338be5-b4b6-4202-96bf-33c6cf21545a`

- Application ID: `APb1fv4toNckfdjxYxETsz8G`

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
```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
> Example Response:

```json
{
  "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
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
  "created_at" : "2016-11-13T20:49:44.04Z",
  "updated_at" : "2016-11-13T20:49:44.04Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}).save()

```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
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
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
	    "identity"=> "ID2NZkbqzm5VenxC1Gs3VyS8"
	));
$bank_account = $bank_account->save();

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
> Example Response:

```json
{
  "id" : "PIi9D4sJf9ip383BydeCnwMS",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:50.50Z",
  "updated_at" : "2016-11-13T20:49:50.50Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="ID2NZkbqzm5VenxC1Gs3VyS8")
merchant = identity.provision_merchant_on(Merchant())
```
```shell
curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID2NZkbqzm5VenxC1Gs3VyS8');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "verification" : "VIo3qfzFiTpTDyhgQpsFVK76",
  "merchant_profile" : "MPcHBWK3hQJLtssDUXzebHXB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:52.11Z",
  "updated_at" : "2016-11-13T20:49:52.11Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPcHBWK3hQJLtssDUXzebHXB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIo3qfzFiTpTDyhgQpsFVK76"
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
```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Maggie", 
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
```shell

curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Maggie", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
	        "first_name"=> "Maggie", 
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
> Example Response:

```json
{
  "id" : "IDrSTSwuUidruVb3TzVWvTTS",
  "entity" : {
    "title" : null,
    "first_name" : "Maggie",
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
  "created_at" : "2016-11-13T20:49:53.27Z",
  "updated_at" : "2016-11-13T20:49:53.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Jones", 
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
	    "identity": "IDrSTSwuUidruVb3TzVWvTTS"
	}).save()
```
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "name": "Bob Jones", 
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
	    "identity": "IDrSTSwuUidruVb3TzVWvTTS"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Bob Jones", 
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
	    "identity"=> "IDrSTSwuUidruVb3TzVWvTTS"
	));
$card = $card->save();


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
> Example Response:

```json
{
  "id" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "fingerprint" : "FPR1221569778",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Jones",
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
  "created_at" : "2016-11-13T20:49:53.91Z",
  "updated_at" : "2016-11-13T20:49:53.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDrSTSwuUidruVb3TzVWvTTS",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/updates"
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
```python


from payline.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "merchant_identity": "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

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
> Example Response:

```json
{
  "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:59.00Z",
  "updated_at" : "2016-11-13T20:49:59.02Z",
  "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:59.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU9H3Dzv9ntxM4rhLxafb6w6")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU9H3Dzv9ntxM4rhLxafb6w6');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU9H3Dzv9ntxM4rhLxafb6w6");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfXPtbdqywZ63oUuhXdugxN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:58.87Z",
  "updated_at" : "2016-11-13T20:49:59.94Z",
  "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:58.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
          applicationId: 'APb1fv4toNckfdjxYxETsz8G',
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
  "id" : "TKiNddjSuaYTdTYimxCFAtpW",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T20:50:01.48Z",
  "updated_at" : "2016-11-13T20:50:01.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T20:50:01.48Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    }
  }
}
```

### Step 4: Associate the Token
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}).save()

```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	});
$card = $card->save();

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
> Example Response:

```json
{
  "id" : "PIiNddjSuaYTdTYimxCFAtpW",
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
  "created_at" : "2016-11-13T20:50:02.50Z",
  "updated_at" : "2016-11-13T20:50:02.50Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/updates"
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


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```python


from payline.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "merchant_identity": "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID2NZkbqzm5VenxC1Gs3VyS8", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIfMEMPUp7AH1rqpHkwP2goi", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


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
> Example Response:

```json
{
  "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:59.00Z",
  "updated_at" : "2016-11-13T20:49:59.02Z",
  "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:59.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU9H3Dzv9ntxM4rhLxafb6w6")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU9H3Dzv9ntxM4rhLxafb6w6');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU9H3Dzv9ntxM4rhLxafb6w6");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfXPtbdqywZ63oUuhXdugxN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:58.87Z",
  "updated_at" : "2016-11-13T20:49:59.94Z",
  "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:58.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU9H3Dzv9ntxM4rhLxafb6w6")
authorization.void()

```
```shell

curl https://api-test.payline.io/authorizations/AU5bDaZddzG4TquT4BQNZT4h \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AU5bDaZddzG4TquT4BQNZT4h",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:50:03.25Z",
  "updated_at" : "2016-11-13T20:50:04.07Z",
  "trace_id" : "aa5b411e-e406-4fa5-8794-4ebb94bcf150",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : true,
  "expires_at" : "2016-11-20T20:50:03.25Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU5bDaZddzG4TquT4BQNZT4h"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
```python


from payline.resources import Authorization

authorization = Authorization.get(id="AU9H3Dzv9ntxM4rhLxafb6w6")
```
```shell

curl https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU9H3Dzv9ntxM4rhLxafb6w6');

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU9H3Dzv9ntxM4rhLxafb6w6");

```
> Example Response:

```json
{
  "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRfXPtbdqywZ63oUuhXdugxN",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:58.87Z",
  "updated_at" : "2016-11-13T20:49:59.94Z",
  "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "is_void" : false,
  "expires_at" : "2016-11-20T20:49:58.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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
```python


from payline.resources import Authorization

authorization = Authorization.get()
```
```shell
curl https://api-test.payline.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Authorization;

client.authorizationsClient().<Resources<Authorization>>resourcesIterator()
  .forEachRemaining(page-> {
    Collection<Authorization> authorizations = page.getContent();
    //do something
  });
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU5bDaZddzG4TquT4BQNZT4h",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:50:03.25Z",
      "updated_at" : "2016-11-13T20:50:04.07Z",
      "trace_id" : "aa5b411e-e406-4fa5-8794-4ebb94bcf150",
      "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "is_void" : true,
      "expires_at" : "2016-11-20T20:50:03.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AU5bDaZddzG4TquT4BQNZT4h"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        }
      }
    }, {
      "id" : "AU9H3Dzv9ntxM4rhLxafb6w6",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRfXPtbdqywZ63oUuhXdugxN",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:58.87Z",
      "updated_at" : "2016-11-13T20:49:59.94Z",
      "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
      "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "is_void" : false,
      "expires_at" : "2016-11-20T20:49:58.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AU9H3Dzv9ntxM4rhLxafb6w6"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
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


```python


from payline.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Maggie", 
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
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Maggie", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
	        "first_name"=> "Maggie", 
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
> Example Response:

```json
{
  "id" : "IDrSTSwuUidruVb3TzVWvTTS",
  "entity" : {
    "title" : null,
    "first_name" : "Maggie",
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
  "created_at" : "2016-11-13T20:49:53.27Z",
  "updated_at" : "2016-11-13T20:49:53.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
> Example Response:

```json
{
  "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
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
  "created_at" : "2016-11-13T20:49:44.04Z",
  "updated_at" : "2016-11-13T20:49:44.04Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python


from payline.resources import Identity
identity = Identity.get(id="ID2NZkbqzm5VenxC1Gs3VyS8")

```
```shell

curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID2NZkbqzm5VenxC1Gs3VyS8');
```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID2NZkbqzm5VenxC1Gs3VyS8");

```
> Example Response:

```json
{
  "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
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
  "created_at" : "2016-11-13T20:49:43.98Z",
  "updated_at" : "2016-11-13T20:49:43.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python


from payline.resources import Identity
identity = Identity.get()

```
```shell
curl https://api-test.payline.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDrSTSwuUidruVb3TzVWvTTS",
      "entity" : {
        "title" : null,
        "first_name" : "Maggie",
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
      "created_at" : "2016-11-13T20:49:53.21Z",
      "updated_at" : "2016-11-13T20:49:53.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID54hjjUm4xakSaVYfH1ocub",
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
      "created_at" : "2016-11-13T20:49:49.88Z",
      "updated_at" : "2016-11-13T20:49:49.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDpCdDj4fyTCTqSTtubKKaAj",
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
      "created_at" : "2016-11-13T20:49:49.30Z",
      "updated_at" : "2016-11-13T20:49:49.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDs68YU7RK8QUm7rBWNAhsDk",
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
      "created_at" : "2016-11-13T20:49:48.67Z",
      "updated_at" : "2016-11-13T20:49:48.67Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDffWGLkoe64AvNRNuY7GTmU",
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
      "created_at" : "2016-11-13T20:49:48.12Z",
      "updated_at" : "2016-11-13T20:49:48.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDsV3BRuQ3a8NhrBtcS7hhXQ",
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
      "created_at" : "2016-11-13T20:49:47.50Z",
      "updated_at" : "2016-11-13T20:49:47.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID2jRMDfAEih2YPokrXagHfp",
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
      "created_at" : "2016-11-13T20:49:46.92Z",
      "updated_at" : "2016-11-13T20:49:46.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDmVRnKWjbMxzWwDKWPXquxy",
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
      "created_at" : "2016-11-13T20:49:46.33Z",
      "updated_at" : "2016-11-13T20:49:46.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID5KVSqAbPq5CJqWiWz8nNAU",
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
      "created_at" : "2016-11-13T20:49:45.66Z",
      "updated_at" : "2016-11-13T20:49:45.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDa2En4ig9hW4NbdnrJpJUgb",
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
      "created_at" : "2016-11-13T20:49:44.84Z",
      "updated_at" : "2016-11-13T20:49:44.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
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
      "created_at" : "2016-11-13T20:49:43.98Z",
      "updated_at" : "2016-11-13T20:49:43.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDuTmvj15skGEgYhN8L5D6dm",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "application_name" : "WePay"
      },
      "created_at" : "2016-11-13T20:49:40.58Z",
      "updated_at" : "2016-11-13T20:49:40.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python



```
```shell
curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Collen", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Collen",
    "last_name" : "Diaz",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-13T20:49:43.98Z",
  "updated_at" : "2016-11-13T20:50:14.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="ID2NZkbqzm5VenxC1Gs3VyS8")
merchant = identity.provision_merchant_on(Merchant())

```
```shell

curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID2NZkbqzm5VenxC1Gs3VyS8');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );
```
```java

import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```

> Example Response:

```json
{
  "id" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "verification" : "VIo3qfzFiTpTDyhgQpsFVK76",
  "merchant_profile" : "MPcHBWK3hQJLtssDUXzebHXB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:52.11Z",
  "updated_at" : "2016-11-13T20:49:52.11Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPcHBWK3hQJLtssDUXzebHXB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIo3qfzFiTpTDyhgQpsFVK76"
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
```python


from payline.resources import Identity
from payline.resources import Merchant

identity = Identity.get(id="ID2NZkbqzm5VenxC1Gs3VyS8")
merchant = identity.provision_merchant_on(Merchant())

```
```shell
curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID2NZkbqzm5VenxC1Gs3VyS8');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "verification" : "VIo3qfzFiTpTDyhgQpsFVK76",
  "merchant_profile" : "MPcHBWK3hQJLtssDUXzebHXB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:52.11Z",
  "updated_at" : "2016-11-13T20:49:52.11Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPcHBWK3hQJLtssDUXzebHXB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIo3qfzFiTpTDyhgQpsFVK76"
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
```python


from payline.resources import Merchant
merchant = Merchant.get(id="MUoiJAXoU5xqJeiujXdDiJNm")

```
```shell
curl https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Merchant;

$merchant = Merchant::retrieve('MUoiJAXoU5xqJeiujXdDiJNm');

```
```java
import io.payline.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUoiJAXoU5xqJeiujXdDiJNm");

```
> Example Response:

```json
{
  "id" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "verification" : null,
  "merchant_profile" : "MPcHBWK3hQJLtssDUXzebHXB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-13T20:49:52.00Z",
  "updated_at" : "2016-11-13T20:49:52.28Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MPcHBWK3hQJLtssDUXzebHXB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python



```
```shell
curl https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "UScV93xXhFVgfy1BbCoevfxV",
  "password" : "38c60f6a-29a2-47ea-be2a-23f67d84780f",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T20:49:56.08Z",
  "updated_at" : "2016-11-13T20:49:56.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/users/UScV93xXhFVgfy1BbCoevfxV"
    },
    "applications" : {
      "href" : "https://api-test.payline.io/applications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIm7qHbCjXhkprqK5Ywb2dET",
  "external_trace_id" : "7917eec2-0695-4ae3-8b39-b2ddece1af65",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T20:50:15.76Z",
  "updated_at" : "2016-11-13T20:50:15.78Z",
  "payment_instrument" : null,
  "merchant" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIm7qHbCjXhkprqK5Ywb2dET"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VIm7qHbCjXhkprqK5Ywb2dET",
  "external_trace_id" : "7917eec2-0695-4ae3-8b39-b2ddece1af65",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T20:50:15.76Z",
  "updated_at" : "2016-11-13T20:50:15.78Z",
  "payment_instrument" : null,
  "merchant" : "MUoiJAXoU5xqJeiujXdDiJNm",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/verifications/VIm7qHbCjXhkprqK5Ywb2dET"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "merchant" : {
      "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
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
```python


from payline.resources import Merchant
merchant = Merchant.get()

```
```shell
curl https://api-test.payline.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUoiJAXoU5xqJeiujXdDiJNm",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "verification" : null,
      "merchant_profile" : "MPcHBWK3hQJLtssDUXzebHXB",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-13T20:49:52.00Z",
      "updated_at" : "2016-11-13T20:49:52.28Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-test.payline.io/merchant_profiles/MPcHBWK3hQJLtssDUXzebHXB"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python



```
```shell
curl https://api-test.payline.io/merchants/MUoiJAXoU5xqJeiujXdDiJNm/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDrSTSwuUidruVb3TzVWvTTS",
      "entity" : {
        "title" : null,
        "first_name" : "Maggie",
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
      "created_at" : "2016-11-13T20:49:53.21Z",
      "updated_at" : "2016-11-13T20:49:53.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID54hjjUm4xakSaVYfH1ocub",
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
      "created_at" : "2016-11-13T20:49:49.88Z",
      "updated_at" : "2016-11-13T20:49:49.88Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID54hjjUm4xakSaVYfH1ocub/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDpCdDj4fyTCTqSTtubKKaAj",
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
      "created_at" : "2016-11-13T20:49:49.30Z",
      "updated_at" : "2016-11-13T20:49:49.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDpCdDj4fyTCTqSTtubKKaAj/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDs68YU7RK8QUm7rBWNAhsDk",
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
      "created_at" : "2016-11-13T20:49:48.67Z",
      "updated_at" : "2016-11-13T20:49:48.67Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDs68YU7RK8QUm7rBWNAhsDk/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDffWGLkoe64AvNRNuY7GTmU",
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
      "created_at" : "2016-11-13T20:49:48.12Z",
      "updated_at" : "2016-11-13T20:49:48.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDffWGLkoe64AvNRNuY7GTmU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDsV3BRuQ3a8NhrBtcS7hhXQ",
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
      "created_at" : "2016-11-13T20:49:47.50Z",
      "updated_at" : "2016-11-13T20:49:47.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDsV3BRuQ3a8NhrBtcS7hhXQ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID2jRMDfAEih2YPokrXagHfp",
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
      "created_at" : "2016-11-13T20:49:46.92Z",
      "updated_at" : "2016-11-13T20:49:46.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2jRMDfAEih2YPokrXagHfp/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDmVRnKWjbMxzWwDKWPXquxy",
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
      "created_at" : "2016-11-13T20:49:46.33Z",
      "updated_at" : "2016-11-13T20:49:46.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDmVRnKWjbMxzWwDKWPXquxy/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID5KVSqAbPq5CJqWiWz8nNAU",
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
      "created_at" : "2016-11-13T20:49:45.66Z",
      "updated_at" : "2016-11-13T20:49:45.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID5KVSqAbPq5CJqWiWz8nNAU/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDa2En4ig9hW4NbdnrJpJUgb",
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
      "created_at" : "2016-11-13T20:49:44.84Z",
      "updated_at" : "2016-11-13T20:49:44.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDa2En4ig9hW4NbdnrJpJUgb/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "ID2NZkbqzm5VenxC1Gs3VyS8",
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
      "created_at" : "2016-11-13T20:49:43.98Z",
      "updated_at" : "2016-11-13T20:49:43.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "IDuTmvj15skGEgYhN8L5D6dm",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "application_name" : "WePay"
      },
      "created_at" : "2016-11-13T20:49:40.58Z",
      "updated_at" : "2016-11-13T20:49:40.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python


from payline.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Jones", 
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
	    "identity": "IDrSTSwuUidruVb3TzVWvTTS"
	}).save()
```
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "name": "Bob Jones", 
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
	    "identity": "IDrSTSwuUidruVb3TzVWvTTS"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Bob Jones", 
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
	    "identity"=> "IDrSTSwuUidruVb3TzVWvTTS"
	));
$card = $card->save();


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
> Example Response:

```json
{
  "id" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "fingerprint" : "FPR1221569778",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Jones",
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
  "created_at" : "2016-11-13T20:49:53.91Z",
  "updated_at" : "2016-11-13T20:49:53.91Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDrSTSwuUidruVb3TzVWvTTS",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/updates"
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
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}).save()
```
```shell

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
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
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
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
	    "identity"=> "ID2NZkbqzm5VenxC1Gs3VyS8"
	));
$bank_account = $bank_account->save();


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
> Example Response:

```json
{
  "id" : "PIi9D4sJf9ip383BydeCnwMS",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:50.50Z",
  "updated_at" : "2016-11-13T20:49:50.50Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
          applicationId: 'APb1fv4toNckfdjxYxETsz8G',
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
  "id" : "TKiNddjSuaYTdTYimxCFAtpW",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T20:50:01.48Z",
  "updated_at" : "2016-11-13T20:50:01.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T20:50:01.48Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    }
  }
}
```

```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	});
$card = $card->save();

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
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIiNddjSuaYTdTYimxCFAtpW",
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
  "created_at" : "2016-11-13T20:50:02.50Z",
  "updated_at" : "2016-11-13T20:50:02.50Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/updates"
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
```python


from payline.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}).save()
```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKiNddjSuaYTdTYimxCFAtpW", 
	    "type": "TOKEN", 
	    "identity": "ID2NZkbqzm5VenxC1Gs3VyS8"
	});
$card = $card->save();

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
> Example Response:

```json
{
  "id" : "PIiNddjSuaYTdTYimxCFAtpW",
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
  "created_at" : "2016-11-13T20:50:02.50Z",
  "updated_at" : "2016-11-13T20:50:02.50Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/updates"
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

```python



```
```shell


curl https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIi9D4sJf9ip383BydeCnwMS');

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIi9D4sJf9ip383BydeCnwMS")

```
> Example Response:

```json
{
  "id" : "PIi9D4sJf9ip383BydeCnwMS",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:50.41Z",
  "updated_at" : "2016-11-13T20:49:51.10Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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
```python



```
```shell
curl https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PIi9D4sJf9ip383BydeCnwMS",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T20:49:50.41Z",
  "updated_at" : "2016-11-13T20:49:51.10Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

```python



```
```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIiNddjSuaYTdTYimxCFAtpW",
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
      "created_at" : "2016-11-13T20:50:02.24Z",
      "updated_at" : "2016-11-13T20:50:02.24Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNddjSuaYTdTYimxCFAtpW/updates"
        }
      }
    }, {
      "id" : "PIrnoPUDFPaEzUJffZ3ekc7Q",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T20:49:54.48Z",
      "updated_at" : "2016-11-13T20:49:54.48Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDrSTSwuUidruVb3TzVWvTTS",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrnoPUDFPaEzUJffZ3ekc7Q"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrnoPUDFPaEzUJffZ3ekc7Q/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrnoPUDFPaEzUJffZ3ekc7Q/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIrnoPUDFPaEzUJffZ3ekc7Q/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "fingerprint" : "FPR1221569778",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Bob Jones",
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
      "created_at" : "2016-11-13T20:49:53.83Z",
      "updated_at" : "2016-11-13T20:49:59.02Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDrSTSwuUidruVb3TzVWvTTS",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDrSTSwuUidruVb3TzVWvTTS"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi/updates"
        }
      }
    }, {
      "id" : "PIwkygm6cxxULFs73gc8ooGP",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:52.00Z",
      "updated_at" : "2016-11-13T20:49:52.00Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PIvBsdcFAnKuvifuquMkSunk",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:52.00Z",
      "updated_at" : "2016-11-13T20:49:52.00Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvBsdcFAnKuvifuquMkSunk"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvBsdcFAnKuvifuquMkSunk/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvBsdcFAnKuvifuquMkSunk/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIvBsdcFAnKuvifuquMkSunk/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PIb8fTKx5q68s5kxFgNoCyfY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:52.00Z",
      "updated_at" : "2016-11-13T20:49:52.00Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIb8fTKx5q68s5kxFgNoCyfY"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIb8fTKx5q68s5kxFgNoCyfY/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIb8fTKx5q68s5kxFgNoCyfY/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIb8fTKx5q68s5kxFgNoCyfY/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PIi9D4sJf9ip383BydeCnwMS",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T20:49:50.41Z",
      "updated_at" : "2016-11-13T20:49:51.10Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIi9D4sJf9ip383BydeCnwMS/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PI9sMH5tgMyGxcPzMEP7474B",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:41.31Z",
      "updated_at" : "2016-11-13T20:49:41.31Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuTmvj15skGEgYhN8L5D6dm",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9sMH5tgMyGxcPzMEP7474B"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9sMH5tgMyGxcPzMEP7474B/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9sMH5tgMyGxcPzMEP7474B/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI9sMH5tgMyGxcPzMEP7474B/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PItie1WMA7CyBFVXjX2uxYGF",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:41.31Z",
      "updated_at" : "2016-11-13T20:49:41.31Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuTmvj15skGEgYhN8L5D6dm",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItie1WMA7CyBFVXjX2uxYGF"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItie1WMA7CyBFVXjX2uxYGF/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItie1WMA7CyBFVXjX2uxYGF/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PItie1WMA7CyBFVXjX2uxYGF/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PIc4YdVJPvXig59xKmTFriZy",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:41.31Z",
      "updated_at" : "2016-11-13T20:49:41.31Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIc4YdVJPvXig59xKmTFriZy"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIc4YdVJPvXig59xKmTFriZy/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIc4YdVJPvXig59xKmTFriZy/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIc4YdVJPvXig59xKmTFriZy/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        }
      }
    }, {
      "id" : "PI59N7NRRFNBVD6smtcmkK1V",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T20:49:41.31Z",
      "updated_at" : "2016-11-13T20:49:41.31Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuTmvj15skGEgYhN8L5D6dm",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI59N7NRRFNBVD6smtcmkK1V"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI59N7NRRFNBVD6smtcmkK1V/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDuTmvj15skGEgYhN8L5D6dm"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI59N7NRRFNBVD6smtcmkK1V/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI59N7NRRFNBVD6smtcmkK1V/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>
## Retrieve a Transfer
```python


from payline.resources import Transfer
transfer = Transfer.get(id="TRk2Ug7d7UQ6wAHV5iCpThsQ")

```
```shell

curl https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRk2Ug7d7UQ6wAHV5iCpThsQ');



```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRk2Ug7d7UQ6wAHV5iCpThsQ");

```
> Example Response:

```json
{
  "id" : "TRk2Ug7d7UQ6wAHV5iCpThsQ",
  "amount" : 215686,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "6b3687a3-87f3-44ed-809a-247b6299a9c1",
  "currency" : "USD",
  "application" : "APb1fv4toNckfdjxYxETsz8G",
  "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "destination" : "PIwkygm6cxxULFs73gc8ooGP",
  "ready_to_settle_at" : null,
  "fee" : 21569,
  "statement_descriptor" : "PLD*ACME ANCHORS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:55.18Z",
  "updated_at" : "2016-11-13T20:49:57.74Z",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/reversals"
    },
    "fees" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/fees"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP"
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
```python


from payline.resources import Transfer

transfer = Transfer.get(id="TRk2Ug7d7UQ6wAHV5iCpThsQ")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```shell

curl https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRk2Ug7d7UQ6wAHV5iCpThsQ');
$refund = $debit->reverse(50);
```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TR5cghopNkTg943Tpqj2LNKD",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "21f72780-333f-4c46-aba5-dd2093f3820b",
  "currency" : "USD",
  "application" : "APb1fv4toNckfdjxYxETsz8G",
  "source" : "PIwkygm6cxxULFs73gc8ooGP",
  "destination" : "PIfMEMPUp7AH1rqpHkwP2goi",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "PLD*ACME ANCHORS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T20:49:57.80Z",
  "updated_at" : "2016-11-13T20:49:57.90Z",
  "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TR5cghopNkTg943Tpqj2LNKD"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TR5cghopNkTg943Tpqj2LNKD/payment_instruments"
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
```python


from payline.resources import Transfer
transfer = Transfer.get()

```
```shell
curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRfXPtbdqywZ63oUuhXdugxN",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "b8304c51-93f6-43d2-86bc-1c9573af22c4",
      "currency" : "USD",
      "application" : "APb1fv4toNckfdjxYxETsz8G",
      "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "destination" : "PIwkygm6cxxULFs73gc8ooGP",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:59.71Z",
      "updated_at" : "2016-11-13T20:50:03.53Z",
      "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRfXPtbdqywZ63oUuhXdugxN/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP"
        }
      }
    }, {
      "id" : "TR5cghopNkTg943Tpqj2LNKD",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "0d8c577e-37c2-40c9-beac-703100461c8a",
      "currency" : "USD",
      "application" : "APb1fv4toNckfdjxYxETsz8G",
      "source" : "PIwkygm6cxxULFs73gc8ooGP",
      "destination" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "PLD*ACME ANCHORS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:57.52Z",
      "updated_at" : "2016-11-13T20:49:57.90Z",
      "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR5cghopNkTg943Tpqj2LNKD"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR5cghopNkTg943Tpqj2LNKD/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
        }
      }
    }, {
      "id" : "TRk2Ug7d7UQ6wAHV5iCpThsQ",
      "amount" : 215686,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "6b3687a3-87f3-44ed-809a-247b6299a9c1",
      "currency" : "USD",
      "application" : "APb1fv4toNckfdjxYxETsz8G",
      "source" : "PIfMEMPUp7AH1rqpHkwP2goi",
      "destination" : "PIwkygm6cxxULFs73gc8ooGP",
      "ready_to_settle_at" : null,
      "fee" : 21569,
      "statement_descriptor" : "PLD*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T20:49:55.18Z",
      "updated_at" : "2016-11-13T20:49:57.74Z",
      "merchant_identity" : "ID2NZkbqzm5VenxC1Gs3VyS8",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/ID2NZkbqzm5VenxC1Gs3VyS8"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/reversals"
        },
        "fees" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/fees"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRk2Ug7d7UQ6wAHV5iCpThsQ/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIfMEMPUp7AH1rqpHkwP2goi"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIwkygm6cxxULFs73gc8ooGP"
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
```python


from payline.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```shell

curl https://api-test.payline.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHeDsR4KPPhs2U7Reet5YbMT",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APb1fv4toNckfdjxYxETsz8G",
  "created_at" : "2016-11-13T20:49:43.57Z",
  "updated_at" : "2016-11-13T20:49:43.57Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHeDsR4KPPhs2U7Reet5YbMT"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

```python


from payline.resources import Webhook
webhook = Webhook.get(id="WHeDsR4KPPhs2U7Reet5YbMT")

```
```shell



curl https://api-test.payline.io/webhooks/WHeDsR4KPPhs2U7Reet5YbMT \
    -H "Content-Type: application/vnd.json+api" \
    -u US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHeDsR4KPPhs2U7Reet5YbMT');



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHeDsR4KPPhs2U7Reet5YbMT");

```
> Example Response:

```json
{
  "id" : "WHeDsR4KPPhs2U7Reet5YbMT",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APb1fv4toNckfdjxYxETsz8G",
  "created_at" : "2016-11-13T20:49:43.58Z",
  "updated_at" : "2016-11-13T20:49:43.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHeDsR4KPPhs2U7Reet5YbMT"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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

```python


from payline.resources import Webhook
webhooks = Webhook.get()

```
```shell
curl https://api-test.payline.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2WyUiuGyjYM2sKVMjXNmz7:27338be5-b4b6-4202-96bf-33c6cf21545a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHeDsR4KPPhs2U7Reet5YbMT",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APb1fv4toNckfdjxYxETsz8G",
      "created_at" : "2016-11-13T20:49:43.58Z",
      "updated_at" : "2016-11-13T20:49:43.58Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHeDsR4KPPhs2U7Reet5YbMT"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APb1fv4toNckfdjxYxETsz8G"
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


```python


```
```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US2WyUiuGyjYM2sKVMjXNmz7', '27338be5-b4b6-4202-96bf-33c6cf21545a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

```
```java
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
