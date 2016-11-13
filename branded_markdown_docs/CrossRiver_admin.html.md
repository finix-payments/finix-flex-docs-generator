---
title: CrossRiver API Reference

language_tabs:
- python: Python
- shell: cURL
- php: PHP
- java: Java



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

3. [Embedded Tokenization](#embedded-tokenization-using-iframe): This guide
explains how to properly tokenize cards in production via our embedded iframe.

4. [Push-to-Card Private](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("US6QXZKCQCyKsUpVFa4oVKVM", "2d175c9b-8c5d-4ac6-81cc-92784bedf45d"))

```
```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```java

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US6QXZKCQCyKsUpVFa4oVKVM`

- Password: `2d175c9b-8c5d-4ac6-81cc-92784bedf45d`

- Application ID: `APiTy2556zrehQRKMp1U3AJa`

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
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
> Example Response:

```json
{
  "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
  "created_at" : "2016-11-13T04:13:48.55Z",
  "updated_at" : "2016-11-13T04:13:48.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	    "identity"=> "IDuhir41t9t7rDmuN1YKxsab"
	));
$bank_account = $bank_account->save();

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
> Example Response:

```json
{
  "id" : "PIwi59THzZyNGfVpHsCbDQbf",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T04:14:00.64Z",
  "updated_at" : "2016-11-13T04:14:00.64Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuhir41t9t7rDmuN1YKxsab")
merchant = identity.provision_merchant_on(Merchant())
```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuhir41t9t7rDmuN1YKxsab');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : "VIxopJhcbsrHnXA3WdzRmUFK",
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.76Z",
  "updated_at" : "2016-11-13T04:14:04.76Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIxopJhcbsrHnXA3WdzRmUFK"
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
	}).save()

```
```shell

curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	        "first_name"=> "Collen", 
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
	)
);
$identity = $identity->save();

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
> Example Response:

```json
{
  "id" : "IDtxktd3rNQ6mv28scRkQqcD",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-13T04:14:05.74Z",
  "updated_at" : "2016-11-13T04:14:05.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Ricardo Curry", 
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
	    "identity"=> "IDtxktd3rNQ6mv28scRkQqcD"
	));
$card = $card->save();


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
> Example Response:

```json
{
  "id" : "PIuYR9ZPv5a61duQV5KahKtK",
  "fingerprint" : "FPR1356102392",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ricardo Curry",
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
  "created_at" : "2016-11-13T04:14:06.37Z",
  "updated_at" : "2016-11-13T04:14:06.37Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtxktd3rNQ6mv28scRkQqcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/updates"
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
```python


from crossriver.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

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
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.36Z",
  "updated_at" : "2016-11-13T04:14:16.37Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8SumuaWjQqfyFKiH48Jeze")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AU8SumuaWjQqfyFKiH48Jeze');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8SumuaWjQqfyFKiH48Jeze");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRbPQhUC2T7w1N73FYwBoBYH",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.21Z",
  "updated_at" : "2016-11-13T04:14:17.94Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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

## Embedded Tokenization Using Iframe

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
          applicationId: 'APiTy2556zrehQRKMp1U3AJa',
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
  "id" : "TKbVAQScUSTjP2Dw9Bp4fNPs",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T04:14:19.16Z",
  "updated_at" : "2016-11-13T04:14:19.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T04:14:19.16Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    }
  }
}
```

### Step 4: Associate the Token
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	});
$card = $card->save();

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
> Example Response:

```json
{
  "id" : "PIbVAQScUSTjP2Dw9Bp4fNPs",
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
  "created_at" : "2016-11-13T04:14:25.16Z",
  "updated_at" : "2016-11-13T04:14:25.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/updates"
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
```python



```
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Alex", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDwYLHKFoemdS77UjWpFTYmo",
  "entity" : {
    "title" : null,
    "first_name" : "Alex",
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
  "created_at" : "2016-11-13T04:14:35.65Z",
  "updated_at" : "2016-11-13T04:14:35.65Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "name": "Marshall Wade", 
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
	    "identity": "IDwYLHKFoemdS77UjWpFTYmo"
	}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```java

```
> Example Response:

```json
{
  "id" : "PI5esTm8WyorpUqKkATwV6e5",
  "fingerprint" : "FPR-729537692",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marshall Wade",
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
  "created_at" : "2016-11-13T04:14:36.14Z",
  "updated_at" : "2016-11-13T04:14:36.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwYLHKFoemdS77UjWpFTYmo",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/updates"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MUeYChwgdRwdDMUkbAyNnLro",
  "identity" : "IDwYLHKFoemdS77UjWpFTYmo",
  "verification" : "VIoxr37AJsxRrKnKMHFy1Hnw",
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:40.25Z",
  "updated_at" : "2016-11-13T04:14:40.25Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeYChwgdRwdDMUkbAyNnLro"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeYChwgdRwdDMUkbAyNnLro/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIoxr37AJsxRrKnKMHFy1Hnw"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Nmae of Processor


### Step 4: Send Payout

Once you have tokenized the payment card as above you can send funds to it at any time by simply calling the API


```python



```
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDwYLHKFoemdS77UjWpFTYmo", 
	    "destination": "PI5esTm8WyorpUqKkATwV6e5", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```java

```
> Example Response:

```json
{
  "id" : "TRheA8TELjX9qom2GXsebemJ",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "87941",
  "currency" : "USD",
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "source" : "PIort5m4abcCmrgx9QdtHrDb",
  "destination" : "PI5esTm8WyorpUqKkATwV6e5",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:38.11Z",
  "updated_at" : "2016-11-13T04:14:39.53Z",
  "merchant_identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5"
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
merchant_identity | *string*, **required** | `Identity` ID of the recipient of whom you're sending the money to
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Getting Started
### Step 1: Create an Identity for a Merchant

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
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
> Example Response:

```json
{
  "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
  "created_at" : "2016-11-13T04:13:48.55Z",
  "updated_at" : "2016-11-13T04:13:48.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	    "identity"=> "IDuhir41t9t7rDmuN1YKxsab"
	));
$bank_account = $bank_account->save();

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
> Example Response:

```json
{
  "id" : "PIwi59THzZyNGfVpHsCbDQbf",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T04:14:00.64Z",
  "updated_at" : "2016-11-13T04:14:00.64Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuhir41t9t7rDmuN1YKxsab")
merchant = identity.provision_merchant_on(Merchant())
```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuhir41t9t7rDmuN1YKxsab');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : "VIxopJhcbsrHnXA3WdzRmUFK",
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.76Z",
  "updated_at" : "2016-11-13T04:14:04.76Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIxopJhcbsrHnXA3WdzRmUFK"
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
	}).save()

```
```shell

curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	        "first_name"=> "Collen", 
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
	)
);
$identity = $identity->save();

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
> Example Response:

```json
{
  "id" : "IDtxktd3rNQ6mv28scRkQqcD",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-13T04:14:05.74Z",
  "updated_at" : "2016-11-13T04:14:05.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Ricardo Curry", 
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
	    "identity"=> "IDtxktd3rNQ6mv28scRkQqcD"
	));
$card = $card->save();


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
> Example Response:

```json
{
  "id" : "PIuYR9ZPv5a61duQV5KahKtK",
  "fingerprint" : "FPR1356102392",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ricardo Curry",
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
  "created_at" : "2016-11-13T04:14:06.37Z",
  "updated_at" : "2016-11-13T04:14:06.37Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtxktd3rNQ6mv28scRkQqcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/updates"
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
```python


from crossriver.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

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
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.36Z",
  "updated_at" : "2016-11-13T04:14:16.37Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8SumuaWjQqfyFKiH48Jeze")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AU8SumuaWjQqfyFKiH48Jeze');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8SumuaWjQqfyFKiH48Jeze");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRbPQhUC2T7w1N73FYwBoBYH",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.21Z",
  "updated_at" : "2016-11-13T04:14:17.94Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python



```
```shell
curl https://api-staging.finix.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "role": "ROLE_PARTNER"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US6QXZKCQCyKsUpVFa4oVKVM",
  "password" : "2d175c9b-8c5d-4ac6-81cc-92784bedf45d",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T04:13:43.42Z",
  "updated_at" : "2016-11-13T04:13:43.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US6QXZKCQCyKsUpVFa4oVKVM"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "max_transaction_amount": 12000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T04:13:43.87Z",
  "updated_at" : "2016-11-13T04:13:43.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PRjvAknN2nyB1QuiaxxoabRD",
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "default_merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "created_at" : "2016-11-13T04:13:45.03Z",
  "updated_at" : "2016-11-13T04:13:45.03Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors/PRjvAknN2nyB1QuiaxxoabRD"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T04:13:43.82Z",
  "updated_at" : "2016-11-13T04:14:56.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
### Step 4: Enable Settlement Functionality
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T04:13:43.82Z",
  "updated_at" : "2016-11-13T04:14:57.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
    applicationId: "APiTy2556zrehQRKMp1U3AJa",
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
  "id" : "TKbVAQScUSTjP2Dw9Bp4fNPs",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T04:14:19.16Z",
  "updated_at" : "2016-11-13T04:14:19.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T04:14:19.16Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()

```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	});
$card = $card->save();

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
> Example Response:

```json
{
  "id" : "PIbVAQScUSTjP2Dw9Bp4fNPs",
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
  "created_at" : "2016-11-13T04:14:25.16Z",
  "updated_at" : "2016-11-13T04:14:25.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/updates"
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


# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).
## [ADMIN] Create a New Application

## Fetch an Application
```python


from crossriver.resources import Application

application = Application.get(id="APiTy2556zrehQRKMp1U3AJa")
```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = Application::retrieve('APiTy2556zrehQRKMp1U3AJa');

```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T04:13:43.82Z",
  "updated_at" : "2016-11-13T04:13:47.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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


```python


from crossriver.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "max_transaction_amount": 12000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}).save()
```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "max_transaction_amount": 12000, 
	        "phone": "1234567890", 
	        "doing_business_as": "WePay", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "WePay", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "WePay"
	    ), 
	    "user"=> "US6QXZKCQCyKsUpVFa4oVKVM", 
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
	        "doing_business_as"=> "WePay", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "WePay", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();

```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T04:13:43.87Z",
  "updated_at" : "2016-11-13T04:13:43.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
## Disable Processing Functionality
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-11-13T04:13:43.82Z",
  "updated_at" : "2016-11-13T04:14:53.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
## Disable Settlement Functionality
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "APiTy2556zrehQRKMp1U3AJa",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-13T04:13:43.82Z",
  "updated_at" : "2016-11-13T04:14:53.89Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USfNcfG9tyUv93uokD9bYWmk",
  "password" : "665f8339-ec96-4669-a58d-9b10e75dedd0",
  "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T04:13:45.59Z",
  "updated_at" : "2016-11-13T04:13:45.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USfNcfG9tyUv93uokD9bYWmk"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PRjvAknN2nyB1QuiaxxoabRD",
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "default_merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "created_at" : "2016-11-13T04:13:45.03Z",
  "updated_at" : "2016-11-13T04:13:45.03Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors/PRjvAknN2nyB1QuiaxxoabRD"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Application

application = Application.get()
```
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APiTy2556zrehQRKMp1U3AJa",
      "enabled" : true,
      "tags" : {
        "application_name" : "WePay"
      },
      "owner" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-11-13T04:13:43.82Z",
      "updated_at" : "2016-11-13T04:13:47.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/reversals"
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


```python


from crossriver.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```shell
curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "merchant_identity": "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDuhir41t9t7rDmuN1YKxsab", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIuYR9ZPv5a61duQV5KahKtK", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


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
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.36Z",
  "updated_at" : "2016-11-13T04:14:16.37Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.36Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8SumuaWjQqfyFKiH48Jeze")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```shell
curl https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AU8SumuaWjQqfyFKiH48Jeze');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8SumuaWjQqfyFKiH48Jeze");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRbPQhUC2T7w1N73FYwBoBYH",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.21Z",
  "updated_at" : "2016-11-13T04:14:17.94Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8SumuaWjQqfyFKiH48Jeze")
authorization.void()

```
```shell

curl https://api-staging.finix.io/authorizations/AUp81hoDnUJiornaxcNTmBC7 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUp81hoDnUJiornaxcNTmBC7",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:25.80Z",
  "updated_at" : "2016-11-13T04:14:27.45Z",
  "trace_id" : "84922ca7-9cdf-4423-a392-99f0d5ab7589",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : true,
  "expires_at" : "2016-11-20T04:14:25.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUp81hoDnUJiornaxcNTmBC7"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AU8SumuaWjQqfyFKiH48Jeze")
```
```shell

curl https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AU8SumuaWjQqfyFKiH48Jeze');

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU8SumuaWjQqfyFKiH48Jeze");

```
> Example Response:

```json
{
  "id" : "AU8SumuaWjQqfyFKiH48Jeze",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRbPQhUC2T7w1N73FYwBoBYH",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:16.21Z",
  "updated_at" : "2016-11-13T04:14:17.94Z",
  "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "is_void" : false,
  "expires_at" : "2016-11-20T04:14:16.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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
```python


from crossriver.resources import Authorization

authorization = Authorization.get()
```
```shell
curl https://api-staging.finix.io/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


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
      "id" : "AUp81hoDnUJiornaxcNTmBC7",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:25.80Z",
      "updated_at" : "2016-11-13T04:14:27.45Z",
      "trace_id" : "84922ca7-9cdf-4423-a392-99f0d5ab7589",
      "source" : "PIuYR9ZPv5a61duQV5KahKtK",
      "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "is_void" : true,
      "expires_at" : "2016-11-20T04:14:25.80Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUp81hoDnUJiornaxcNTmBC7"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        }
      }
    }, {
      "id" : "AU8SumuaWjQqfyFKiH48Jeze",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRbPQhUC2T7w1N73FYwBoBYH",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:16.21Z",
      "updated_at" : "2016-11-13T04:14:17.94Z",
      "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
      "source" : "PIuYR9ZPv5a61duQV5KahKtK",
      "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "is_void" : false,
      "expires_at" : "2016-11-20T04:14:16.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU8SumuaWjQqfyFKiH48Jeze"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
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


```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
	}).save()
```
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Collen", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	        "first_name"=> "Collen", 
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
	)
);
$identity = $identity->save();

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
> Example Response:

```json
{
  "id" : "IDtxktd3rNQ6mv28scRkQqcD",
  "entity" : {
    "title" : null,
    "first_name" : "Collen",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-11-13T04:14:05.74Z",
  "updated_at" : "2016-11-13T04:14:05.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
> Example Response:

```json
{
  "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
  "created_at" : "2016-11-13T04:13:48.55Z",
  "updated_at" : "2016-11-13T04:13:48.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDuhir41t9t7rDmuN1YKxsab")

```
```shell

curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuhir41t9t7rDmuN1YKxsab');
```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDuhir41t9t7rDmuN1YKxsab");

```
> Example Response:

```json
{
  "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
  "created_at" : "2016-11-13T04:13:48.49Z",
  "updated_at" : "2016-11-13T04:13:48.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Sean", 
	        "last_name": "Kline", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDuhir41t9t7rDmuN1YKxsab",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Sean",
    "last_name" : "Kline",
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
  "created_at" : "2016-11-13T04:13:48.49Z",
  "updated_at" : "2016-11-13T04:14:49.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Identity
identity = Identity.get()

```
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Identity;

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
      "id" : "IDwYLHKFoemdS77UjWpFTYmo",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-13T04:14:35.59Z",
      "updated_at" : "2016-11-13T04:14:35.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDtxktd3rNQ6mv28scRkQqcD",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-13T04:14:05.68Z",
      "updated_at" : "2016-11-13T04:14:05.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID2ZijHbYounPvDimeKbaRwA",
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
      "created_at" : "2016-11-13T04:13:59.83Z",
      "updated_at" : "2016-11-13T04:13:59.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDoBJhPBeazM3FdXsE677HyK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T04:13:59.14Z",
      "updated_at" : "2016-11-13T04:13:59.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID9HFEYkYXvuM41i7Ly7dmHn",
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
      "created_at" : "2016-11-13T04:13:58.52Z",
      "updated_at" : "2016-11-13T04:13:58.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDdwXLxH6TmNDpeLFJWLXiLt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-13T04:13:57.75Z",
      "updated_at" : "2016-11-13T04:13:57.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDpmDpd71hxagDw3B84R2aiF",
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
      "created_at" : "2016-11-13T04:13:55.56Z",
      "updated_at" : "2016-11-13T04:13:55.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDw6GxsiMg1z7vKpNoRCJvLS",
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
      "created_at" : "2016-11-13T04:13:55.01Z",
      "updated_at" : "2016-11-13T04:13:55.01Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDrCrZgXFjZgQXkQxWp7Z9JQ",
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
      "created_at" : "2016-11-13T04:13:53.18Z",
      "updated_at" : "2016-11-13T04:13:53.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDjGrpVR17TP3US1XvWrbxkF",
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
      "created_at" : "2016-11-13T04:13:49.50Z",
      "updated_at" : "2016-11-13T04:13:49.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDiDBDTPYRFEpwkbvPjvJJE6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T04:13:48.99Z",
      "updated_at" : "2016-11-13T04:13:48.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
      "created_at" : "2016-11-13T04:13:48.49Z",
      "updated_at" : "2016-11-13T04:13:48.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDmwRcg2jYkvXkRAqmdvWZgC",
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
      "created_at" : "2016-11-13T04:13:43.82Z",
      "updated_at" : "2016-11-13T04:13:43.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDuhir41t9t7rDmuN1YKxsab")
merchant = identity.provision_merchant_on(Merchant())

```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDuhir41t9t7rDmuN1YKxsab');

$merchant = $identity->provisionMerchantOn(
          array(
            "tags"=> array(
              "key_2"=> "value_2"
            )
          )
        );

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build())

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : "VIxopJhcbsrHnXA3WdzRmUFK",
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.76Z",
  "updated_at" : "2016-11-13T04:14:04.76Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIxopJhcbsrHnXA3WdzRmUFK"
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
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUmGvHP7jFbacidqvEC1GnUJ")

```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUmGvHP7jFbacidqvEC1GnUJ');

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUmGvHP7jFbacidqvEC1GnUJ");

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : null,
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.66Z",
  "updated_at" : "2016-11-13T04:14:04.85Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VI9pzHgDeacb2xkz33vv3pvW",
  "external_trace_id" : "d181b5ef-d919-4cff-b7e0-6f00ad38bfd9",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T04:14:50.33Z",
  "updated_at" : "2016-11-13T04:14:50.35Z",
  "payment_instrument" : null,
  "merchant" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9pzHgDeacb2xkz33vv3pvW"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "VI9pzHgDeacb2xkz33vv3pvW",
  "external_trace_id" : "d181b5ef-d919-4cff-b7e0-6f00ad38bfd9",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-13T04:14:50.33Z",
  "updated_at" : "2016-11-13T04:14:50.35Z",
  "payment_instrument" : null,
  "merchant" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9pzHgDeacb2xkz33vv3pvW"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : null,
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.66Z",
  "updated_at" : "2016-11-13T04:14:51.14Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "verification" : null,
  "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-13T04:14:04.66Z",
  "updated_at" : "2016-11-13T04:14:51.83Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Merchant
merchant = Merchant.get()

```
```shell
curl https://api-staging.finix.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUeYChwgdRwdDMUkbAyNnLro",
      "identity" : "IDwYLHKFoemdS77UjWpFTYmo",
      "verification" : null,
      "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-13T04:14:40.18Z",
      "updated_at" : "2016-11-13T04:14:40.18Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUeYChwgdRwdDMUkbAyNnLro"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUeYChwgdRwdDMUkbAyNnLro/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "MUmGvHP7jFbacidqvEC1GnUJ",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "verification" : null,
      "merchant_profile" : "MPpcWshPDdwJ11eHgdyuytqZ",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-13T04:14:04.66Z",
      "updated_at" : "2016-11-13T04:14:04.85Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPpcWshPDdwJ11eHgdyuytqZ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDwYLHKFoemdS77UjWpFTYmo",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-13T04:14:35.59Z",
      "updated_at" : "2016-11-13T04:14:35.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDtxktd3rNQ6mv28scRkQqcD",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-13T04:14:05.68Z",
      "updated_at" : "2016-11-13T04:14:05.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID2ZijHbYounPvDimeKbaRwA",
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
      "created_at" : "2016-11-13T04:13:59.83Z",
      "updated_at" : "2016-11-13T04:13:59.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDoBJhPBeazM3FdXsE677HyK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T04:13:59.14Z",
      "updated_at" : "2016-11-13T04:13:59.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID9HFEYkYXvuM41i7Ly7dmHn",
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
      "created_at" : "2016-11-13T04:13:58.52Z",
      "updated_at" : "2016-11-13T04:13:58.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDdwXLxH6TmNDpeLFJWLXiLt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-13T04:13:57.75Z",
      "updated_at" : "2016-11-13T04:13:57.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDpmDpd71hxagDw3B84R2aiF",
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
      "created_at" : "2016-11-13T04:13:55.56Z",
      "updated_at" : "2016-11-13T04:13:55.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDw6GxsiMg1z7vKpNoRCJvLS",
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
      "created_at" : "2016-11-13T04:13:55.01Z",
      "updated_at" : "2016-11-13T04:13:55.01Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDrCrZgXFjZgQXkQxWp7Z9JQ",
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
      "created_at" : "2016-11-13T04:13:53.18Z",
      "updated_at" : "2016-11-13T04:13:53.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDjGrpVR17TP3US1XvWrbxkF",
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
      "created_at" : "2016-11-13T04:13:49.50Z",
      "updated_at" : "2016-11-13T04:13:49.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDiDBDTPYRFEpwkbvPjvJJE6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T04:13:48.99Z",
      "updated_at" : "2016-11-13T04:13:48.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
      "created_at" : "2016-11-13T04:13:48.49Z",
      "updated_at" : "2016-11-13T04:13:48.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDmwRcg2jYkvXkRAqmdvWZgC",
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
      "created_at" : "2016-11-13T04:13:43.82Z",
      "updated_at" : "2016-11-13T04:13:43.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/merchants/MUmGvHP7jFbacidqvEC1GnUJ/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDwYLHKFoemdS77UjWpFTYmo",
      "entity" : {
        "title" : null,
        "first_name" : "Alex",
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
      "created_at" : "2016-11-13T04:14:35.59Z",
      "updated_at" : "2016-11-13T04:14:35.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDtxktd3rNQ6mv28scRkQqcD",
      "entity" : {
        "title" : null,
        "first_name" : "Collen",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-11-13T04:14:05.68Z",
      "updated_at" : "2016-11-13T04:14:05.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID2ZijHbYounPvDimeKbaRwA",
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
      "created_at" : "2016-11-13T04:13:59.83Z",
      "updated_at" : "2016-11-13T04:13:59.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2ZijHbYounPvDimeKbaRwA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDoBJhPBeazM3FdXsE677HyK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-11-13T04:13:59.14Z",
      "updated_at" : "2016-11-13T04:13:59.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoBJhPBeazM3FdXsE677HyK/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "ID9HFEYkYXvuM41i7Ly7dmHn",
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
      "created_at" : "2016-11-13T04:13:58.52Z",
      "updated_at" : "2016-11-13T04:13:58.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID9HFEYkYXvuM41i7Ly7dmHn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDdwXLxH6TmNDpeLFJWLXiLt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-11-13T04:13:57.75Z",
      "updated_at" : "2016-11-13T04:13:57.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdwXLxH6TmNDpeLFJWLXiLt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDpmDpd71hxagDw3B84R2aiF",
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
      "created_at" : "2016-11-13T04:13:55.56Z",
      "updated_at" : "2016-11-13T04:13:55.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpmDpd71hxagDw3B84R2aiF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDw6GxsiMg1z7vKpNoRCJvLS",
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
      "created_at" : "2016-11-13T04:13:55.01Z",
      "updated_at" : "2016-11-13T04:13:55.01Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw6GxsiMg1z7vKpNoRCJvLS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDrCrZgXFjZgQXkQxWp7Z9JQ",
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
      "created_at" : "2016-11-13T04:13:53.18Z",
      "updated_at" : "2016-11-13T04:13:53.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrCrZgXFjZgQXkQxWp7Z9JQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDjGrpVR17TP3US1XvWrbxkF",
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
      "created_at" : "2016-11-13T04:13:49.50Z",
      "updated_at" : "2016-11-13T04:13:49.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDjGrpVR17TP3US1XvWrbxkF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDiDBDTPYRFEpwkbvPjvJJE6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-11-13T04:13:48.99Z",
      "updated_at" : "2016-11-13T04:13:48.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDiDBDTPYRFEpwkbvPjvJJE6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDuhir41t9t7rDmuN1YKxsab",
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
      "created_at" : "2016-11-13T04:13:48.49Z",
      "updated_at" : "2016-11-13T04:13:48.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "IDmwRcg2jYkvXkRAqmdvWZgC",
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
      "created_at" : "2016-11-13T04:13:43.82Z",
      "updated_at" : "2016-11-13T04:13:43.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US83bU2kWJiWDn2TDqGJ6AUw",
  "password" : "55e6ad27-9654-484c-8bdd-f1d6f81a79ee",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T04:14:09.35Z",
  "updated_at" : "2016-11-13T04:14:09.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US83bU2kWJiWDn2TDqGJ6AUw"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
          applicationId: 'APiTy2556zrehQRKMp1U3AJa',
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
  "id" : "TKbVAQScUSTjP2Dw9Bp4fNPs",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-13T04:14:19.16Z",
  "updated_at" : "2016-11-13T04:14:19.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-14T04:14:19.16Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    }
  }
}
```

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	});
$card = $card->save();

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
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIbVAQScUSTjP2Dw9Bp4fNPs",
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
  "created_at" : "2016-11-13T04:14:25.16Z",
  "updated_at" : "2016-11-13T04:14:25.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/updates"
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
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()
```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKbVAQScUSTjP2Dw9Bp4fNPs", 
	    "type": "TOKEN", 
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	});
$card = $card->save();

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
> Example Response:

```json
{
  "id" : "PIbVAQScUSTjP2Dw9Bp4fNPs",
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
  "created_at" : "2016-11-13T04:14:25.16Z",
  "updated_at" : "2016-11-13T04:14:25.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/updates"
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
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}).save()
```
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
	{
	    "name": "Ricardo Curry", 
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
	    "identity": "IDtxktd3rNQ6mv28scRkQqcD"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Ricardo Curry", 
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
	    "identity"=> "IDtxktd3rNQ6mv28scRkQqcD"
	));
$card = $card->save();


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
> Example Response:

```json
{
  "id" : "PIuYR9ZPv5a61duQV5KahKtK",
  "fingerprint" : "FPR1356102392",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Ricardo Curry",
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
  "created_at" : "2016-11-13T04:14:06.37Z",
  "updated_at" : "2016-11-13T04:14:06.37Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtxktd3rNQ6mv28scRkQqcD",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/updates"
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}).save()
```
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
	    "identity": "IDuhir41t9t7rDmuN1YKxsab"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
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
	    "identity"=> "IDuhir41t9t7rDmuN1YKxsab"
	));
$bank_account = $bank_account->save();


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
> Example Response:

```json
{
  "id" : "PIwi59THzZyNGfVpHsCbDQbf",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T04:14:00.64Z",
  "updated_at" : "2016-11-13T04:14:00.64Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python



```
```shell


curl https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIwi59THzZyNGfVpHsCbDQbf');

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIwi59THzZyNGfVpHsCbDQbf")

```
> Example Response:

```json
{
  "id" : "PIwi59THzZyNGfVpHsCbDQbf",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T04:14:00.54Z",
  "updated_at" : "2016-11-13T04:14:02.46Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
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
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PIwi59THzZyNGfVpHsCbDQbf",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-13T04:14:00.54Z",
  "updated_at" : "2016-11-13T04:14:02.46Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python



```
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

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
      "id" : "PI5esTm8WyorpUqKkATwV6e5",
      "fingerprint" : "FPR-729537692",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marshall Wade",
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
      "created_at" : "2016-11-13T04:14:36.06Z",
      "updated_at" : "2016-11-13T04:14:36.06Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDwYLHKFoemdS77UjWpFTYmo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDwYLHKFoemdS77UjWpFTYmo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5/updates"
        }
      }
    }, {
      "id" : "PIort5m4abcCmrgx9QdtHrDb",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:34.49Z",
      "updated_at" : "2016-11-13T04:14:34.49Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PI6rbfH4SifnbAPasP8PwUhh",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:34.49Z",
      "updated_at" : "2016-11-13T04:14:34.49Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6rbfH4SifnbAPasP8PwUhh"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6rbfH4SifnbAPasP8PwUhh/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6rbfH4SifnbAPasP8PwUhh/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6rbfH4SifnbAPasP8PwUhh/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIbAT83ksVphQUH4SFT2q37f",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:34.49Z",
      "updated_at" : "2016-11-13T04:14:34.49Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbAT83ksVphQUH4SFT2q37f"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbAT83ksVphQUH4SFT2q37f/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbAT83ksVphQUH4SFT2q37f/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbAT83ksVphQUH4SFT2q37f/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PI5DEdhTM5ciykjwTGgVZ5J2",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:34.49Z",
      "updated_at" : "2016-11-13T04:14:34.49Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5DEdhTM5ciykjwTGgVZ5J2"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5DEdhTM5ciykjwTGgVZ5J2/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5DEdhTM5ciykjwTGgVZ5J2/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5DEdhTM5ciykjwTGgVZ5J2/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIbVAQScUSTjP2Dw9Bp4fNPs",
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
      "created_at" : "2016-11-13T04:14:25.03Z",
      "updated_at" : "2016-11-13T04:14:25.03Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbVAQScUSTjP2Dw9Bp4fNPs/updates"
        }
      }
    }, {
      "id" : "PI8EXrsfCoxD5uMdo2JNuA5W",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T04:14:07.55Z",
      "updated_at" : "2016-11-13T04:14:07.55Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDtxktd3rNQ6mv28scRkQqcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8EXrsfCoxD5uMdo2JNuA5W"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8EXrsfCoxD5uMdo2JNuA5W/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8EXrsfCoxD5uMdo2JNuA5W/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8EXrsfCoxD5uMdo2JNuA5W/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIuYR9ZPv5a61duQV5KahKtK",
      "fingerprint" : "FPR1356102392",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Ricardo Curry",
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
      "created_at" : "2016-11-13T04:14:06.28Z",
      "updated_at" : "2016-11-13T04:14:16.37Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDtxktd3rNQ6mv28scRkQqcD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDtxktd3rNQ6mv28scRkQqcD"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK/updates"
        }
      }
    }, {
      "id" : "PItUsuFNcBZEE29UqJp9mgGh",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:04.66Z",
      "updated_at" : "2016-11-13T04:14:04.66Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItUsuFNcBZEE29UqJp9mgGh"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItUsuFNcBZEE29UqJp9mgGh/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItUsuFNcBZEE29UqJp9mgGh/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItUsuFNcBZEE29UqJp9mgGh/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIhse9iP6T1DvGk4j73f8pYH",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:04.66Z",
      "updated_at" : "2016-11-13T04:14:04.66Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PI6ckPVC9dqusUvvcg9Qk6Qd",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:14:04.66Z",
      "updated_at" : "2016-11-13T04:14:04.66Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ckPVC9dqusUvvcg9Qk6Qd"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ckPVC9dqusUvvcg9Qk6Qd/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ckPVC9dqusUvvcg9Qk6Qd/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ckPVC9dqusUvvcg9Qk6Qd/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIwi59THzZyNGfVpHsCbDQbf",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-13T04:14:00.54Z",
      "updated_at" : "2016-11-13T04:14:02.46Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwi59THzZyNGfVpHsCbDQbf/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PI7548NHRwqMeFkJjhH8B7ym",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:13:44.94Z",
      "updated_at" : "2016-11-13T04:13:44.94Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7548NHRwqMeFkJjhH8B7ym"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7548NHRwqMeFkJjhH8B7ym/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7548NHRwqMeFkJjhH8B7ym/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7548NHRwqMeFkJjhH8B7ym/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PI73Eh7P8vNuNTo3sUQ1ovmL",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:13:44.94Z",
      "updated_at" : "2016-11-13T04:13:44.94Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI73Eh7P8vNuNTo3sUQ1ovmL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI73Eh7P8vNuNTo3sUQ1ovmL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI73Eh7P8vNuNTo3sUQ1ovmL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI73Eh7P8vNuNTo3sUQ1ovmL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIrowCTEoP7hgYnqmoAms2mw",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:13:44.94Z",
      "updated_at" : "2016-11-13T04:13:44.94Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrowCTEoP7hgYnqmoAms2mw"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrowCTEoP7hgYnqmoAms2mw/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrowCTEoP7hgYnqmoAms2mw/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrowCTEoP7hgYnqmoAms2mw/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "PIhR2sCYMN3vupoKrkYmxkE7",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-13T04:13:44.94Z",
      "updated_at" : "2016-11-13T04:13:44.94Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhR2sCYMN3vupoKrkYmxkE7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhR2sCYMN3vupoKrkYmxkE7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhR2sCYMN3vupoKrkYmxkE7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhR2sCYMN3vupoKrkYmxkE7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRty6KLkYCqAjgZJKXTc8fw3")

```
```shell

curl https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRty6KLkYCqAjgZJKXTc8fw3');



```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRty6KLkYCqAjgZJKXTc8fw3");

```
> Example Response:

```json
{
  "id" : "TRty6KLkYCqAjgZJKXTc8fw3",
  "amount" : 306243,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "4bd4e9b0-5aaf-4b0c-a664-c75e3b3b0a6a",
  "currency" : "USD",
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "source" : "PIuYR9ZPv5a61duQV5KahKtK",
  "destination" : "PIhse9iP6T1DvGk4j73f8pYH",
  "ready_to_settle_at" : null,
  "fee" : 30624,
  "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:08.66Z",
  "updated_at" : "2016-11-13T04:14:15.17Z",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH"
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
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRty6KLkYCqAjgZJKXTc8fw3")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
```shell

curl https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRty6KLkYCqAjgZJKXTc8fw3');
$refund = $debit->reverse(50);
```
```java

import io.crossriver.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRgp5oDnVhVDq55FZd4dR1Nj",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "7cb1e46d-fbc9-4383-9d8b-cc1e4eed1a46",
  "currency" : "USD",
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "source" : "PIhse9iP6T1DvGk4j73f8pYH",
  "destination" : "PIuYR9ZPv5a61duQV5KahKtK",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-13T04:14:15.19Z",
  "updated_at" : "2016-11-13T04:14:15.25Z",
  "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRgp5oDnVhVDq55FZd4dR1Nj"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRgp5oDnVhVDq55FZd4dR1Nj/payment_instruments"
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
```python


from crossriver.resources import Transfer
transfer = Transfer.get()

```
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Transfer;

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
      "id" : "TRheA8TELjX9qom2GXsebemJ",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "87941",
      "currency" : "USD",
      "application" : "APiTy2556zrehQRKMp1U3AJa",
      "source" : "PIort5m4abcCmrgx9QdtHrDb",
      "destination" : "PI5esTm8WyorpUqKkATwV6e5",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:37.91Z",
      "updated_at" : "2016-11-13T04:14:39.53Z",
      "merchant_identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDmwRcg2jYkvXkRAqmdvWZgC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRheA8TELjX9qom2GXsebemJ/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIort5m4abcCmrgx9QdtHrDb"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5esTm8WyorpUqKkATwV6e5"
        }
      }
    }, {
      "id" : "TRbPQhUC2T7w1N73FYwBoBYH",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "72de848f-31dc-4ff3-9bdf-2ee5d5e50ce9",
      "currency" : "USD",
      "application" : "APiTy2556zrehQRKMp1U3AJa",
      "source" : "PIuYR9ZPv5a61duQV5KahKtK",
      "destination" : "PIhse9iP6T1DvGk4j73f8pYH",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:17.76Z",
      "updated_at" : "2016-11-13T04:14:26.50Z",
      "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRbPQhUC2T7w1N73FYwBoBYH/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH"
        }
      }
    }, {
      "id" : "TRgp5oDnVhVDq55FZd4dR1Nj",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "7fa78125-8e0d-45d9-a26b-1132507b999e",
      "currency" : "USD",
      "application" : "APiTy2556zrehQRKMp1U3AJa",
      "source" : "PIhse9iP6T1DvGk4j73f8pYH",
      "destination" : "PIuYR9ZPv5a61duQV5KahKtK",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:15.01Z",
      "updated_at" : "2016-11-13T04:14:15.25Z",
      "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRgp5oDnVhVDq55FZd4dR1Nj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRgp5oDnVhVDq55FZd4dR1Nj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
        }
      }
    }, {
      "id" : "TRty6KLkYCqAjgZJKXTc8fw3",
      "amount" : 306243,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "4bd4e9b0-5aaf-4b0c-a664-c75e3b3b0a6a",
      "currency" : "USD",
      "application" : "APiTy2556zrehQRKMp1U3AJa",
      "source" : "PIuYR9ZPv5a61duQV5KahKtK",
      "destination" : "PIhse9iP6T1DvGk4j73f8pYH",
      "ready_to_settle_at" : null,
      "fee" : 30624,
      "statement_descriptor" : "FNX*PRESTIGE WORLD WI",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-13T04:14:08.66Z",
      "updated_at" : "2016-11-13T04:14:15.17Z",
      "merchant_identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRty6KLkYCqAjgZJKXTc8fw3/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuYR9ZPv5a61duQV5KahKtK"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhse9iP6T1DvGk4j73f8pYH"
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
```python



```
```shell
curl https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "USfNcfG9tyUv93uokD9bYWmk",
  "password" : "665f8339-ec96-4669-a58d-9b10e75dedd0",
  "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T04:13:45.59Z",
  "updated_at" : "2016-11-13T04:13:45.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USfNcfG9tyUv93uokD9bYWmk"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python



```
```shell
curl https://api-staging.finix.io/identities/IDuhir41t9t7rDmuN1YKxsab/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '{}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US83bU2kWJiWDn2TDqGJ6AUw",
  "password" : "55e6ad27-9654-484c-8bdd-f1d6f81a79ee",
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T04:14:09.35Z",
  "updated_at" : "2016-11-13T04:14:09.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US83bU2kWJiWDn2TDqGJ6AUw"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import User
user = User.get(id="US6QXZKCQCyKsUpVFa4oVKVM")

```
```shell
curl https://api-staging.finix.io/users/TRty6KLkYCqAjgZJKXTc8fw3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US6QXZKCQCyKsUpVFa4oVKVM",
  "password" : null,
  "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-13T04:13:43.42Z",
  "updated_at" : "2016-11-13T04:13:43.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US6QXZKCQCyKsUpVFa4oVKVM"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python



```
```shell
curl https://api-staging.finix.io/users/US83bU2kWJiWDn2TDqGJ6AUw \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "US83bU2kWJiWDn2TDqGJ6AUw",
  "password" : null,
  "identity" : "IDuhir41t9t7rDmuN1YKxsab",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-13T04:14:09.25Z",
  "updated_at" : "2016-11-13T04:14:09.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US83bU2kWJiWDn2TDqGJ6AUw"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import User
users = User.get()

```
```shell
curl https://api-staging.finix.io/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "US83bU2kWJiWDn2TDqGJ6AUw",
      "password" : null,
      "identity" : "IDuhir41t9t7rDmuN1YKxsab",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-11-13T04:14:09.25Z",
      "updated_at" : "2016-11-13T04:14:11.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US83bU2kWJiWDn2TDqGJ6AUw"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "USfNcfG9tyUv93uokD9bYWmk",
      "password" : null,
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-13T04:13:45.53Z",
      "updated_at" : "2016-11-13T04:13:45.53Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USfNcfG9tyUv93uokD9bYWmk"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
        }
      }
    }, {
      "id" : "US6QXZKCQCyKsUpVFa4oVKVM",
      "password" : null,
      "identity" : "IDmwRcg2jYkvXkRAqmdvWZgC",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-13T04:13:43.42Z",
      "updated_at" : "2016-11-13T04:13:43.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US6QXZKCQCyKsUpVFa4oVKVM"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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
```python


from crossriver.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
> Example Response:

```json
{
  "id" : "WHxzn8K5LRb23CHJ4wahrVJk",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "created_at" : "2016-11-13T04:13:48.14Z",
  "updated_at" : "2016-11-13T04:13:48.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHxzn8K5LRb23CHJ4wahrVJk"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHxzn8K5LRb23CHJ4wahrVJk")

```
```shell



curl https://api-staging.finix.io/webhooks/WHxzn8K5LRb23CHJ4wahrVJk \
    -H "Content-Type: application/vnd.json+api" \
    -u US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHxzn8K5LRb23CHJ4wahrVJk');



```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHxzn8K5LRb23CHJ4wahrVJk");

```
> Example Response:

```json
{
  "id" : "WHxzn8K5LRb23CHJ4wahrVJk",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APiTy2556zrehQRKMp1U3AJa",
  "created_at" : "2016-11-13T04:13:48.14Z",
  "updated_at" : "2016-11-13T04:13:48.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHxzn8K5LRb23CHJ4wahrVJk"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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

```python


from crossriver.resources import Webhook
webhooks = Webhook.get()

```
```shell
curl https://api-staging.finix.io/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US6QXZKCQCyKsUpVFa4oVKVM:2d175c9b-8c5d-4ac6-81cc-92784bedf45d

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();


```
```java
import io.crossriver.payments.processing.client.model.Webhook;

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
      "id" : "WHxzn8K5LRb23CHJ4wahrVJk",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APiTy2556zrehQRKMp1U3AJa",
      "created_at" : "2016-11-13T04:13:48.14Z",
      "updated_at" : "2016-11-13T04:13:48.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHxzn8K5LRb23CHJ4wahrVJk"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APiTy2556zrehQRKMp1U3AJa"
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


```python


```
```shell
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');
CrossRiver\Settings::configure('https://api-staging.finix.io', 'US6QXZKCQCyKsUpVFa4oVKVM', '2d175c9b-8c5d-4ac6-81cc-92784bedf45d');
require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

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
