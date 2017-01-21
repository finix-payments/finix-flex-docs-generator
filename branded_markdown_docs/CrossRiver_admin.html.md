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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
	"username" => 'UStrgQnqiv3CFUB8WJriTpj4',
	"password" => '5ec5bf78-40f5-48d0-84f4-146c754d685b']
	);

require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("UStrgQnqiv3CFUB8WJriTpj4", "5ec5bf78-40f5-48d0-84f4-146c754d685b"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `UStrgQnqiv3CFUB8WJriTpj4`

- Password: `5ec5bf78-40f5-48d0-84f4-146c754d685b`

- Application ID: `APpoubinhFL1cKJsa1YWtG6b`

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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "IDctyAqyAsm7aKMb8PTWovDx",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-12T06:22:06.40Z",
  "updated_at" : "2017-01-12T06:22:06.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
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
	    "identity"=> "IDctyAqyAsm7aKMb8PTWovDx"
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
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIexnDWTnYs4RJnfgTEawaiq",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-12T06:22:11.60Z",
  "updated_at" : "2017-01-12T06:22:11.60Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDctyAqyAsm7aKMb8PTWovDx")
merchant = identity.provision_merchant_on(Merchant())
```
> Example Response:

```json
{
  "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "verification" : "VIq1j7ViDNAWgMBcyREuqRQJ",
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:12.54Z",
  "updated_at" : "2017-01-12T06:22:12.54Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIq1j7ViDNAWgMBcyREuqRQJ"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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
	        "first_name"=> "Step", 
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
	        "first_name": "Step", 
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
  "id" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-01-12T06:22:13.40Z",
  "updated_at" : "2017-01-12T06:22:13.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "name": "Marcie Sterling", 
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
	    "identity": "IDaSMP6PuWRJNM8jbUxtWQ5k"
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Sterling", 
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
	    "identity"=> "IDaSMP6PuWRJNM8jbUxtWQ5k"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Sterling", 
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
	    "identity": "IDaSMP6PuWRJNM8jbUxtWQ5k"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIbpY1YQic3xKySTo8aG2eWb",
  "fingerprint" : "FPR391052208",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Sterling",
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
  "created_at" : "2017-01-12T06:22:13.84Z",
  "updated_at" : "2017-01-12T06:22:13.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/updates"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "merchant_identity": "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbpY1YQic3xKySTo8aG2eWb", 
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
	    "merchant_identity"=> "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbpY1YQic3xKySTo8aG2eWb", 
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
	    "merchant_identity": "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbpY1YQic3xKySTo8aG2eWb", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
> Example Response:

```json
{
  "id" : "AUny42y965e5YLp3ccjVqbKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:18.45Z",
  "updated_at" : "2017-01-12T06:22:18.51Z",
  "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : false,
  "expires_at" : "2017-01-19T06:22:18.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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
curl https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUny42y965e5YLp3ccjVqbKz");
authorization = authorization.capture(50L);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUny42y965e5YLp3ccjVqbKz');
$authorization = $authorization->capture(50, 10);

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUny42y965e5YLp3ccjVqbKz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUny42y965e5YLp3ccjVqbKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR8q7DnmgJYTgzSKG24c1BAC",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:18.41Z",
  "updated_at" : "2017-01-12T06:22:19.11Z",
  "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : false,
  "expires_at" : "2017-01-19T06:22:18.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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
    -u UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marcie", 
	        "last_name": "Lopez", 
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
	        "first_name"=> "Marcie", 
	        "last_name"=> "Lopez", 
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
  "id" : "IDeXvjnGD5EibiffYd3SVUWW",
  "entity" : {
    "title" : null,
    "first_name" : "Marcie",
    "last_name" : "Lopez",
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
  "created_at" : "2017-01-12T06:22:26.50Z",
  "updated_at" : "2017-01-12T06:22:26.50Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "name": "Collen Chang", 
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
	    "identity": "IDeXvjnGD5EibiffYd3SVUWW"
	}'
```
```java

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDeXvjnGD5EibiffYd3SVUWW');
$card = new PaymentCard(
	array(
	    "name"=> "Collen Chang", 
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
	    "identity"=> "IDeXvjnGD5EibiffYd3SVUWW"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PIdKd7MJtU9Do3XEpNXq6W39",
  "fingerprint" : "FPR-1454370968",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Collen Chang",
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
  "created_at" : "2017-01-12T06:22:28.27Z",
  "updated_at" : "2017-01-12T06:22:28.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/updates"
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
curl https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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

$identity = Identity::retrieve('IDeXvjnGD5EibiffYd3SVUWW');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MUkNQjPNwwmrgRETtRD3vXBX",
  "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
  "verification" : "VI2RfNqHmyVuY39haVsYYSTh",
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:26.97Z",
  "updated_at" : "2017-01-12T06:22:26.97Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUkNQjPNwwmrgRETtRD3vXBX"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUkNQjPNwwmrgRETtRD3vXBX/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI2RfNqHmyVuY39haVsYYSTh"
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
    -u UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "IDeXvjnGD5EibiffYd3SVUWW", 
	    "destination": "PIdKd7MJtU9Do3XEpNXq6W39", 
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
	    "merchant_identity"=> "IDeXvjnGD5EibiffYd3SVUWW", 
	    "destination"=> "PIdKd7MJtU9Do3XEpNXq6W39", 
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
  "id" : "TR3UCHmfBbqpa9nFeHnk9bfk",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "189048",
  "currency" : "USD",
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "source" : "PIrvJUktbZe3MD67njs3yhAX",
  "destination" : "PIdKd7MJtU9Do3XEpNXq6W39",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:28.88Z",
  "updated_at" : "2017-01-12T06:22:30.60Z",
  "merchant_identity" : "IDeXvjnGD5EibiffYd3SVUWW",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39"
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
          applicationId: 'APpoubinhFL1cKJsa1YWtG6b',
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
  "id" : "TKkYaAvTRLCAA3wn6ninHQD7",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-12T06:22:20.18Z",
  "updated_at" : "2017-01-12T06:22:20.18Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-13T06:22:20.18Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
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
	    "token"=> "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDctyAqyAsm7aKMb8PTWovDx"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIkYaAvTRLCAA3wn6ninHQD7",
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
  "created_at" : "2017-01-12T06:22:20.59Z",
  "updated_at" : "2017-01-12T06:22:20.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/updates"
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
    applicationId: "APpoubinhFL1cKJsa1YWtG6b",
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
  "id" : "TKkYaAvTRLCAA3wn6ninHQD7",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-01-12T06:22:20.18Z",
  "updated_at" : "2017-01-12T06:22:20.18Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-01-13T06:22:20.18Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
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
	    "token"=> "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDctyAqyAsm7aKMb8PTWovDx"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIkYaAvTRLCAA3wn6ninHQD7",
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
  "created_at" : "2017-01-12T06:22:20.59Z",
  "updated_at" : "2017-01-12T06:22:20.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/updates"
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
  "id" : "UStrgQnqiv3CFUB8WJriTpj4",
  "password" : "5ec5bf78-40f5-48d0-84f4-146c754d685b",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:03.09Z",
  "updated_at" : "2017-01-12T06:22:03.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UStrgQnqiv3CFUB8WJriTpj4"
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
	    "user": "UStrgQnqiv3CFUB8WJriTpj4", 
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
	    "user"=> "UStrgQnqiv3CFUB8WJriTpj4", 
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-12T06:22:03.55Z",
  "updated_at" : "2017-01-12T06:22:03.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors \
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
  "id" : "PRsdJgRaw9hxY5z9rNTfa3Ne",
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "default_merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "created_at" : "2017-01-12T06:22:04.24Z",
  "updated_at" : "2017-01-12T06:22:04.24Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors/PRsdJgRaw9hxY5z9rNTfa3Ne"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/ \
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-01-12T06:22:03.54Z",
  "updated_at" : "2017-01-12T06:22:39.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/ \
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-12T06:22:03.54Z",
  "updated_at" : "2017-01-12T06:22:40.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use CrossRiver\Resources\Application;

$application = Application::retrieve('APpoubinhFL1cKJsa1YWtG6b');

```
```python


from crossriver.resources import Application

application = Application.get(id="APpoubinhFL1cKJsa1YWtG6b")
```
> Example Response:

```json
{
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-01-12T06:22:03.54Z",
  "updated_at" : "2017-01-12T06:22:05.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
	    "user": "UStrgQnqiv3CFUB8WJriTpj4", 
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
	    "user"=> "UStrgQnqiv3CFUB8WJriTpj4", 
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
	    "user": "UStrgQnqiv3CFUB8WJriTpj4", 
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-12T06:22:03.55Z",
  "updated_at" : "2017-01-12T06:22:03.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/ \
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-01-12T06:22:03.54Z",
  "updated_at" : "2017-01-12T06:22:37.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/ \
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
  "id" : "APpoubinhFL1cKJsa1YWtG6b",
  "enabled" : true,
  "tags" : {
    "application_name" : "Square"
  },
  "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-01-12T06:22:03.54Z",
  "updated_at" : "2017-01-12T06:22:38.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "USu4hLkMMXAVEMwWkxCzu3ZD",
  "password" : "bbcf2faf-89c1-4096-81b3-35e75f35aaab",
  "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:04.81Z",
  "updated_at" : "2017-01-12T06:22:04.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USu4hLkMMXAVEMwWkxCzu3ZD"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors \
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
  "id" : "PRsdJgRaw9hxY5z9rNTfa3Ne",
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "default_merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "created_at" : "2017-01-12T06:22:04.24Z",
  "updated_at" : "2017-01-12T06:22:04.24Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors/PRsdJgRaw9hxY5z9rNTfa3Ne"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "APpoubinhFL1cKJsa1YWtG6b",
      "enabled" : true,
      "tags" : {
        "application_name" : "Square"
      },
      "owner" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-01-12T06:22:03.54Z",
      "updated_at" : "2017-01-12T06:22:05.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/application_profile"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "merchant_identity": "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbpY1YQic3xKySTo8aG2eWb", 
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
	    "merchant_identity"=> "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbpY1YQic3xKySTo8aG2eWb", 
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
	    "merchant_identity": "IDctyAqyAsm7aKMb8PTWovDx", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbpY1YQic3xKySTo8aG2eWb", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "AUny42y965e5YLp3ccjVqbKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:18.45Z",
  "updated_at" : "2017-01-12T06:22:18.51Z",
  "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : false,
  "expires_at" : "2017-01-19T06:22:18.45Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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
curl https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUny42y965e5YLp3ccjVqbKz");
authorization = authorization.capture(50L);

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUny42y965e5YLp3ccjVqbKz');
$authorization = $authorization->capture(50, 10);

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUny42y965e5YLp3ccjVqbKz")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
> Example Response:

```json
{
  "id" : "AUny42y965e5YLp3ccjVqbKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR8q7DnmgJYTgzSKG24c1BAC",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:18.41Z",
  "updated_at" : "2017-01-12T06:22:19.11Z",
  "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : false,
  "expires_at" : "2017-01-19T06:22:18.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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

curl https://api-staging.finix.io/authorizations/AU4dz3HyLoF6AAAFTfgvxk4M \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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

$authorization = Authorization::retrieve('AUny42y965e5YLp3ccjVqbKz');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUny42y965e5YLp3ccjVqbKz")
authorization.void()

```
> Example Response:

```json
{
  "id" : "AU4dz3HyLoF6AAAFTfgvxk4M",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:21.10Z",
  "updated_at" : "2017-01-12T06:22:21.69Z",
  "trace_id" : "7e5f859a-4fc1-4359-b878-f5aea2fb6141",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : true,
  "expires_at" : "2017-01-19T06:22:21.10Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU4dz3HyLoF6AAAFTfgvxk4M"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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

curl https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

```
```java

import io.crossriver.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUny42y965e5YLp3ccjVqbKz");

```
```php
<?php
use CrossRiver\Resources\Authorization;

$authorization = Authorization::retrieve('AUny42y965e5YLp3ccjVqbKz');

```
```python


from crossriver.resources import Authorization

authorization = Authorization.get(id="AUny42y965e5YLp3ccjVqbKz")
```
> Example Response:

```json
{
  "id" : "AUny42y965e5YLp3ccjVqbKz",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR8q7DnmgJYTgzSKG24c1BAC",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:18.41Z",
  "updated_at" : "2017-01-12T06:22:19.11Z",
  "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "is_void" : false,
  "expires_at" : "2017-01-19T06:22:18.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "AU4dz3HyLoF6AAAFTfgvxk4M",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:21.10Z",
      "updated_at" : "2017-01-12T06:22:21.69Z",
      "trace_id" : "7e5f859a-4fc1-4359-b878-f5aea2fb6141",
      "source" : "PIbpY1YQic3xKySTo8aG2eWb",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "is_void" : true,
      "expires_at" : "2017-01-19T06:22:21.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU4dz3HyLoF6AAAFTfgvxk4M"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        }
      }
    }, {
      "id" : "AUny42y965e5YLp3ccjVqbKz",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR8q7DnmgJYTgzSKG24c1BAC",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:18.41Z",
      "updated_at" : "2017-01-12T06:22:19.11Z",
      "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
      "source" : "PIbpY1YQic3xKySTo8aG2eWb",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "is_void" : false,
      "expires_at" : "2017-01-19T06:22:18.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUny42y965e5YLp3ccjVqbKz"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Step", 
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
	        "first_name"=> "Step", 
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
	        "first_name": "Step", 
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
  "id" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
  "entity" : {
    "title" : null,
    "first_name" : "Step",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-01-12T06:22:13.40Z",
  "updated_at" : "2017-01-12T06:22:13.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
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
	        "default_statement_descriptor"=> "Pawny City Hall", 
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
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
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
	        "default_statement_descriptor": "Pawny City Hall", 
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
	        "doing_business_as": "Pawny City Hall", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pawny City Hall", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PawnyCityHall.com", 
	        "annual_card_volume": 12000000
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "IDctyAqyAsm7aKMb8PTWovDx",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-12T06:22:06.40Z",
  "updated_at" : "2017-01-12T06:22:06.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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

curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDctyAqyAsm7aKMb8PTWovDx");

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDctyAqyAsm7aKMb8PTWovDx")

```
> Example Response:

```json
{
  "id" : "IDctyAqyAsm7aKMb8PTWovDx",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-01-12T06:22:06.39Z",
  "updated_at" : "2017-01-12T06:22:06.39Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
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
	        "max_transaction_amount": 1200000, 
	        "principal_percentage_ownership": 50, 
	        "doing_business_as": "Pawny City Hall", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Pawny City Hall", 
	        "url": "www.PawnyCityHall.com", 
	        "business_name": "Pawny City Hall", 
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
  "id" : "IDctyAqyAsm7aKMb8PTWovDx",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Le",
    "email" : "user@example.org",
    "business_name" : "Pawny City Hall",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Pawny City Hall",
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
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pawny City Hall"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-01-12T06:22:06.39Z",
  "updated_at" : "2017-01-12T06:22:35.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b


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
      "id" : "IDeXvjnGD5EibiffYd3SVUWW",
      "entity" : {
        "title" : null,
        "first_name" : "Marcie",
        "last_name" : "Lopez",
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
      "created_at" : "2017-01-12T06:22:26.49Z",
      "updated_at" : "2017-01-12T06:22:26.49Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
      "entity" : {
        "title" : null,
        "first_name" : "Step",
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
        "ownership_type" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2017-01-12T06:22:13.39Z",
      "updated_at" : "2017-01-12T06:22:13.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDvVkJ8EkeuBMt8aYjubJaVw",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:11.16Z",
      "updated_at" : "2017-01-12T06:22:11.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvVkJ8EkeuBMt8aYjubJaVw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDdtR55y8pHG25RWXZdW1MJS",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:10.72Z",
      "updated_at" : "2017-01-12T06:22:10.72Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdtR55y8pHG25RWXZdW1MJS/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDomj9XUhtUohvdn4jXMd1ax",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:10.29Z",
      "updated_at" : "2017-01-12T06:22:10.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDomj9XUhtUohvdn4jXMd1ax/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDcB1YeRHxQkjMGk2pM1dttH",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:09.86Z",
      "updated_at" : "2017-01-12T06:22:09.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcB1YeRHxQkjMGk2pM1dttH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "ID6pFQGFd2JXyaG3mmXFd6Fp",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:09.23Z",
      "updated_at" : "2017-01-12T06:22:09.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6pFQGFd2JXyaG3mmXFd6Fp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "ID5XbEaAQ7D6UUFJDor6xFkt",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "LIMITED_PARTNERSHIP",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:08.62Z",
      "updated_at" : "2017-01-12T06:22:08.62Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5XbEaAQ7D6UUFJDor6xFkt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDctF7eZcBwarfaAxL9VawWP",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:08.02Z",
      "updated_at" : "2017-01-12T06:22:08.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDctF7eZcBwarfaAxL9VawWP/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "ID5jPybETPfgDKE4xjxuMHRN",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:07.31Z",
      "updated_at" : "2017-01-12T06:22:07.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5jPybETPfgDKE4xjxuMHRN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDpZ9yrm5CwtM9bCSADoDj14",
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
        "ownership_type" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:06.86Z",
      "updated_at" : "2017-01-12T06:22:06.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpZ9yrm5CwtM9bCSADoDj14/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDctyAqyAsm7aKMb8PTWovDx",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-01-12T06:22:06.39Z",
      "updated_at" : "2017-01-12T06:22:06.39Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
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
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "application_name" : "Square"
      },
      "created_at" : "2017-01-12T06:22:03.54Z",
      "updated_at" : "2017-01-12T06:22:03.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="IDctyAqyAsm7aKMb8PTWovDx")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "verification" : "VIq1j7ViDNAWgMBcyREuqRQJ",
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:12.54Z",
  "updated_at" : "2017-01-12T06:22:12.54Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIq1j7ViDNAWgMBcyREuqRQJ"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

```
```java
import io.crossriver.payments.processing.client.model.Merchant;

Merchant merchant = client.merchantsClient().fetch("MUwzLJXqEbH3SYryNV8XzLsk");

```
```php
<?php
use CrossRiver\Resources\Merchant;

$merchant = Merchant::retrieve('MUwzLJXqEbH3SYryNV8XzLsk');

```
```python


from crossriver.resources import Merchant
merchant = Merchant.get(id="MUwzLJXqEbH3SYryNV8XzLsk")

```
> Example Response:

```json
{
  "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "verification" : null,
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:12.51Z",
  "updated_at" : "2017-01-12T06:22:12.66Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '{}'

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUwzLJXqEbH3SYryNV8XzLsk');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VI9wrWHt9oyZdgwtr5HwX2Aa",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-12T06:22:36.25Z",
  "updated_at" : "2017-01-12T06:22:36.27Z",
  "trace_id" : "9b773e83-3d92-4cc9-97ac-5a2e89b63b44",
  "payment_instrument" : null,
  "merchant" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9wrWHt9oyZdgwtr5HwX2Aa"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '{}'
```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUwzLJXqEbH3SYryNV8XzLsk');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python



```
> Example Response:

```json
{
  "id" : "VI9wrWHt9oyZdgwtr5HwX2Aa",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-01-12T06:22:36.25Z",
  "updated_at" : "2017-01-12T06:22:36.27Z",
  "trace_id" : "9b773e83-3d92-4cc9-97ac-5a2e89b63b44",
  "payment_instrument" : null,
  "merchant" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI9wrWHt9oyZdgwtr5HwX2Aa"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/ \
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
  "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "verification" : null,
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:12.51Z",
  "updated_at" : "2017-01-12T06:22:36.77Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/ \
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
  "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "verification" : null,
  "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-01-12T06:22:12.51Z",
  "updated_at" : "2017-01-12T06:22:37.22Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "MUkNQjPNwwmrgRETtRD3vXBX",
      "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "verification" : null,
      "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
      "processor" : "VISA_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-12T06:22:26.89Z",
      "updated_at" : "2017-01-12T06:22:27.62Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUkNQjPNwwmrgRETtRD3vXBX"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUkNQjPNwwmrgRETtRD3vXBX/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "MUwzLJXqEbH3SYryNV8XzLsk",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "verification" : null,
      "merchant_profile" : "MPtLVjcwTHA54Tnpvtanreef",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.66Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPtLVjcwTHA54Tnpvtanreef"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

```
```java

```
```php
<?php
use CrossRiver\Resources\Merchant;
use CrossRiver\Resources\Verification;

$merchant = Merchant::retrieve('MUwzLJXqEbH3SYryNV8XzLsk');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIq1j7ViDNAWgMBcyREuqRQJ",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.71Z",
      "trace_id" : "ef94b868-62ee-43bd-a1c7-d74232d8714f",
      "payment_instrument" : null,
      "merchant" : "MUwzLJXqEbH3SYryNV8XzLsk",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/verifications/VIq1j7ViDNAWgMBcyREuqRQJ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "merchant" : {
          "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications?offset=0&limit=20&sort=created_at,desc"
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




## [ADMIN] List Merchant Verifications
```shell
curl https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications \
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
    "verifications" : [ {
      "id" : "VIq1j7ViDNAWgMBcyREuqRQJ",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.71Z",
      "trace_id" : "ef94b868-62ee-43bd-a1c7-d74232d8714f",
      "payment_instrument" : null,
      "merchant" : "MUwzLJXqEbH3SYryNV8XzLsk",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/verifications/VIq1j7ViDNAWgMBcyREuqRQJ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "merchant" : {
          "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUwzLJXqEbH3SYryNV8XzLsk/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "UStFUPUyQR79TQYufGVy2yfB",
  "password" : "c3036e4e-fb77-4198-a394-aad3dcf3f9d2",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:15.44Z",
  "updated_at" : "2017-01-12T06:22:15.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UStFUPUyQR79TQYufGVy2yfB"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
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
	    "token"=> "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDctyAqyAsm7aKMb8PTWovDx"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKkYaAvTRLCAA3wn6ninHQD7", 
	    "type": "TOKEN", 
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIkYaAvTRLCAA3wn6ninHQD7",
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
  "created_at" : "2017-01-12T06:22:20.59Z",
  "updated_at" : "2017-01-12T06:22:20.59Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/updates"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
    -d '
	{
	    "name": "Marcie Sterling", 
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
	    "identity": "IDaSMP6PuWRJNM8jbUxtWQ5k"
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Sterling", 
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
	    "identity"=> "IDaSMP6PuWRJNM8jbUxtWQ5k"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Sterling", 
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
	    "identity": "IDaSMP6PuWRJNM8jbUxtWQ5k"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIbpY1YQic3xKySTo8aG2eWb",
  "fingerprint" : "FPR391052208",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Sterling",
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
  "created_at" : "2017-01-12T06:22:13.84Z",
  "updated_at" : "2017-01-12T06:22:13.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/updates"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
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

$identity = Identity::retrieve('IDctyAqyAsm7aKMb8PTWovDx');
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
	    "identity"=> "IDctyAqyAsm7aKMb8PTWovDx"
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
	    "identity": "IDctyAqyAsm7aKMb8PTWovDx"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIexnDWTnYs4RJnfgTEawaiq",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-12T06:22:11.60Z",
  "updated_at" : "2017-01-12T06:22:11.60Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIexnDWTnYs4RJnfgTEawaiq")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIexnDWTnYs4RJnfgTEawaiq');

```
```python



```
> Example Response:

```json
{
  "id" : "PIexnDWTnYs4RJnfgTEawaiq",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-12T06:22:11.58Z",
  "updated_at" : "2017-01-12T06:22:12.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIbpY1YQic3xKySTo8aG2eWb")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIbpY1YQic3xKySTo8aG2eWb');

```
```python



```
> Example Response:

```json
{
  "id" : "PIbpY1YQic3xKySTo8aG2eWb",
  "fingerprint" : "FPR391052208",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Sterling",
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
  "created_at" : "2017-01-12T06:22:13.79Z",
  "updated_at" : "2017-01-12T06:22:18.48Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/updates"
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
curl https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "PIexnDWTnYs4RJnfgTEawaiq",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-01-12T06:22:11.58Z",
  "updated_at" : "2017-01-12T06:22:12.07Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b
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
      "id" : "PIdKd7MJtU9Do3XEpNXq6W39",
      "fingerprint" : "FPR-1454370968",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Collen Chang",
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
      "created_at" : "2017-01-12T06:22:28.24Z",
      "updated_at" : "2017-01-12T06:22:28.24Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39/updates"
        }
      }
    }, {
      "id" : "PIC5hJQ83SzNHPYeEmEdBgs",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:26.89Z",
      "updated_at" : "2017-01-12T06:22:26.89Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIC5hJQ83SzNHPYeEmEdBgs"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIC5hJQ83SzNHPYeEmEdBgs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIC5hJQ83SzNHPYeEmEdBgs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIC5hJQ83SzNHPYeEmEdBgs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIrvJUktbZe3MD67njs3yhAX",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:26.89Z",
      "updated_at" : "2017-01-12T06:22:26.89Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PI7j3Tc2mjGF6rar3yyiGk8P",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:26.89Z",
      "updated_at" : "2017-01-12T06:22:26.89Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7j3Tc2mjGF6rar3yyiGk8P"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7j3Tc2mjGF6rar3yyiGk8P/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7j3Tc2mjGF6rar3yyiGk8P/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7j3Tc2mjGF6rar3yyiGk8P/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIvzMz9C5AUj41qzDHq7U4pM",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:25.60Z",
      "updated_at" : "2017-01-12T06:22:25.60Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvzMz9C5AUj41qzDHq7U4pM"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvzMz9C5AUj41qzDHq7U4pM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvzMz9C5AUj41qzDHq7U4pM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvzMz9C5AUj41qzDHq7U4pM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIm4oYGzL8mhPzCpMZ8qrbgk",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:25.60Z",
      "updated_at" : "2017-01-12T06:22:25.60Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4oYGzL8mhPzCpMZ8qrbgk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4oYGzL8mhPzCpMZ8qrbgk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4oYGzL8mhPzCpMZ8qrbgk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIm4oYGzL8mhPzCpMZ8qrbgk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIiu4b3rk8YtxXRJ4SuWiNpX",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:25.60Z",
      "updated_at" : "2017-01-12T06:22:25.60Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiu4b3rk8YtxXRJ4SuWiNpX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiu4b3rk8YtxXRJ4SuWiNpX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiu4b3rk8YtxXRJ4SuWiNpX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiu4b3rk8YtxXRJ4SuWiNpX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIcjD2io7c1nk8XSRe347X6J",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:25.60Z",
      "updated_at" : "2017-01-12T06:22:25.60Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcjD2io7c1nk8XSRe347X6J"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcjD2io7c1nk8XSRe347X6J/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcjD2io7c1nk8XSRe347X6J/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcjD2io7c1nk8XSRe347X6J/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIkYaAvTRLCAA3wn6ninHQD7",
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
      "created_at" : "2017-01-12T06:22:20.54Z",
      "updated_at" : "2017-01-12T06:22:20.54Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkYaAvTRLCAA3wn6ninHQD7/updates"
        }
      }
    }, {
      "id" : "PIoue15fZ6b6y9FokuowAqi",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-12T06:22:14.26Z",
      "updated_at" : "2017-01-12T06:22:14.26Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoue15fZ6b6y9FokuowAqi"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoue15fZ6b6y9FokuowAqi/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoue15fZ6b6y9FokuowAqi/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIoue15fZ6b6y9FokuowAqi/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIbpY1YQic3xKySTo8aG2eWb",
      "fingerprint" : "FPR391052208",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Marcie Sterling",
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
      "created_at" : "2017-01-12T06:22:13.79Z",
      "updated_at" : "2017-01-12T06:22:18.48Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDaSMP6PuWRJNM8jbUxtWQ5k",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaSMP6PuWRJNM8jbUxtWQ5k"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb/updates"
        }
      }
    }, {
      "id" : "PIaVzK8YZVKeMn2tpBbppD5x",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.51Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaVzK8YZVKeMn2tpBbppD5x"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaVzK8YZVKeMn2tpBbppD5x/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaVzK8YZVKeMn2tpBbppD5x/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIaVzK8YZVKeMn2tpBbppD5x/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PI8ThYHXtPcp9AKquDxR3a3q",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.51Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ThYHXtPcp9AKquDxR3a3q"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ThYHXtPcp9AKquDxR3a3q/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ThYHXtPcp9AKquDxR3a3q/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8ThYHXtPcp9AKquDxR3a3q/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIkHTWtAfrwPCuTFmKwvJecR",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:12.51Z",
      "updated_at" : "2017-01-12T06:22:12.51Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIexnDWTnYs4RJnfgTEawaiq",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-01-12T06:22:11.58Z",
      "updated_at" : "2017-01-12T06:22:12.07Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIexnDWTnYs4RJnfgTEawaiq/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PImxAShb8aU7hpf7GBHnSqru",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:04.21Z",
      "updated_at" : "2017-01-12T06:22:04.21Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImxAShb8aU7hpf7GBHnSqru"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImxAShb8aU7hpf7GBHnSqru/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImxAShb8aU7hpf7GBHnSqru/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PImxAShb8aU7hpf7GBHnSqru/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIvBcCVjaLKShNuWF7WeUWCv",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:04.21Z",
      "updated_at" : "2017-01-12T06:22:04.21Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBcCVjaLKShNuWF7WeUWCv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBcCVjaLKShNuWF7WeUWCv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBcCVjaLKShNuWF7WeUWCv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvBcCVjaLKShNuWF7WeUWCv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIrrsCbSqXypaaS6KULCVgkE",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:04.21Z",
      "updated_at" : "2017-01-12T06:22:04.21Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrrsCbSqXypaaS6KULCVgkE"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrrsCbSqXypaaS6KULCVgkE/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrrsCbSqXypaaS6KULCVgkE/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrrsCbSqXypaaS6KULCVgkE/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "PIfEaB9MaTBEAgmWCqja7un6",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-01-12T06:22:04.21Z",
      "updated_at" : "2017-01-12T06:22:04.21Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfEaB9MaTBEAgmWCqja7un6"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfEaB9MaTBEAgmWCqja7un6/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDaxDtjmTgcL5Jr4nmiUM2Xo"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfEaB9MaTBEAgmWCqja7un6/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfEaB9MaTBEAgmWCqja7un6/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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

curl https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRehrqoiWEqHCG2iNYqoZS4j");

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRehrqoiWEqHCG2iNYqoZS4j');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRehrqoiWEqHCG2iNYqoZS4j")

```
> Example Response:

```json
{
  "id" : "TRehrqoiWEqHCG2iNYqoZS4j",
  "amount" : 755480,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "ac0a9b00-a728-4b1b-9062-262eff021474",
  "currency" : "USD",
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "source" : "PIbpY1YQic3xKySTo8aG2eWb",
  "destination" : "PIkHTWtAfrwPCuTFmKwvJecR",
  "ready_to_settle_at" : null,
  "fee" : 75548,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:14.76Z",
  "updated_at" : "2017-01-12T06:22:14.92Z",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR"
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

curl https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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

$debit = Transfer::retrieve('TRehrqoiWEqHCG2iNYqoZS4j');
$refund = $debit->reverse(11);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRehrqoiWEqHCG2iNYqoZS4j")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRevhY1XM62QgjinEDVa35M8",
  "amount" : 497507,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "6d5dd3d4-417c-4bd0-a880-4c8ccb8ec809",
  "currency" : "USD",
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "source" : "PIkHTWtAfrwPCuTFmKwvJecR",
  "destination" : "PIbpY1YQic3xKySTo8aG2eWb",
  "ready_to_settle_at" : null,
  "fee" : 49751,
  "statement_descriptor" : "FNX*PAWNY CITY HALL",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-01-12T06:22:17.68Z",
  "updated_at" : "2017-01-12T06:22:17.77Z",
  "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRevhY1XM62QgjinEDVa35M8"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRevhY1XM62QgjinEDVa35M8/payment_instruments"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "TR3UCHmfBbqpa9nFeHnk9bfk",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "189048",
      "currency" : "USD",
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "source" : "PIrvJUktbZe3MD67njs3yhAX",
      "destination" : "PIdKd7MJtU9Do3XEpNXq6W39",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:28.74Z",
      "updated_at" : "2017-01-12T06:22:30.60Z",
      "merchant_identity" : "IDeXvjnGD5EibiffYd3SVUWW",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDeXvjnGD5EibiffYd3SVUWW"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR3UCHmfBbqpa9nFeHnk9bfk/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrvJUktbZe3MD67njs3yhAX"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdKd7MJtU9Do3XEpNXq6W39"
        }
      }
    }, {
      "id" : "TR8q7DnmgJYTgzSKG24c1BAC",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "bd1104f0-925b-46cb-982e-a030640cd028",
      "currency" : "USD",
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "source" : "PIbpY1YQic3xKySTo8aG2eWb",
      "destination" : "PIkHTWtAfrwPCuTFmKwvJecR",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:18.96Z",
      "updated_at" : "2017-01-12T06:22:19.11Z",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR8q7DnmgJYTgzSKG24c1BAC/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR"
        }
      }
    }, {
      "id" : "TRevhY1XM62QgjinEDVa35M8",
      "amount" : 497507,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "1627b5dd-b0f0-47d9-a4f1-ebd0445189da",
      "currency" : "USD",
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "source" : "PIkHTWtAfrwPCuTFmKwvJecR",
      "destination" : "PIbpY1YQic3xKySTo8aG2eWb",
      "ready_to_settle_at" : null,
      "fee" : 49751,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:17.52Z",
      "updated_at" : "2017-01-12T06:22:17.77Z",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRevhY1XM62QgjinEDVa35M8"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRevhY1XM62QgjinEDVa35M8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
        }
      }
    }, {
      "id" : "TRvTqTL8em5AFDtzx935nvLr",
      "amount" : 497507,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "26697d6a-e3aa-47a5-9fc9-0e433b9c4fdf",
      "currency" : "USD",
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "source" : "PIbpY1YQic3xKySTo8aG2eWb",
      "destination" : "PIkHTWtAfrwPCuTFmKwvJecR",
      "ready_to_settle_at" : null,
      "fee" : 49751,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:16.74Z",
      "updated_at" : "2017-01-12T06:22:17.61Z",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRvTqTL8em5AFDtzx935nvLr/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR"
        }
      }
    }, {
      "id" : "TRehrqoiWEqHCG2iNYqoZS4j",
      "amount" : 755480,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "ac0a9b00-a728-4b1b-9062-262eff021474",
      "currency" : "USD",
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "source" : "PIbpY1YQic3xKySTo8aG2eWb",
      "destination" : "PIkHTWtAfrwPCuTFmKwvJecR",
      "ready_to_settle_at" : null,
      "fee" : 75548,
      "statement_descriptor" : "FNX*PAWNY CITY HALL",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-01-12T06:22:14.76Z",
      "updated_at" : "2017-01-12T06:22:14.92Z",
      "merchant_identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRehrqoiWEqHCG2iNYqoZS4j/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbpY1YQic3xKySTo8aG2eWb"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkHTWtAfrwPCuTFmKwvJecR"
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
curl https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "USu4hLkMMXAVEMwWkxCzu3ZD",
  "password" : "bbcf2faf-89c1-4096-81b3-35e75f35aaab",
  "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:04.81Z",
  "updated_at" : "2017-01-12T06:22:04.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USu4hLkMMXAVEMwWkxCzu3ZD"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/identities/IDctyAqyAsm7aKMb8PTWovDx/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "UStFUPUyQR79TQYufGVy2yfB",
  "password" : "c3036e4e-fb77-4198-a394-aad3dcf3f9d2",
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:15.44Z",
  "updated_at" : "2017-01-12T06:22:15.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UStFUPUyQR79TQYufGVy2yfB"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/users/TRehrqoiWEqHCG2iNYqoZS4j \
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
user = User.get(id="UStrgQnqiv3CFUB8WJriTpj4")

```
> Example Response:

```json
{
  "id" : "UStrgQnqiv3CFUB8WJriTpj4",
  "password" : null,
  "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:03.09Z",
  "updated_at" : "2017-01-12T06:22:03.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UStrgQnqiv3CFUB8WJriTpj4"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
curl https://api-staging.finix.io/users/UStFUPUyQR79TQYufGVy2yfB \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "UStFUPUyQR79TQYufGVy2yfB",
  "password" : null,
  "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-01-12T06:22:15.40Z",
  "updated_at" : "2017-01-12T06:22:15.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/UStFUPUyQR79TQYufGVy2yfB"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "UStFUPUyQR79TQYufGVy2yfB",
      "password" : null,
      "identity" : "IDctyAqyAsm7aKMb8PTWovDx",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-01-12T06:22:15.40Z",
      "updated_at" : "2017-01-12T06:22:16.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/UStFUPUyQR79TQYufGVy2yfB"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "USu4hLkMMXAVEMwWkxCzu3ZD",
      "password" : null,
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-12T06:22:04.79Z",
      "updated_at" : "2017-01-12T06:22:04.79Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USu4hLkMMXAVEMwWkxCzu3ZD"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
        }
      }
    }, {
      "id" : "UStrgQnqiv3CFUB8WJriTpj4",
      "password" : null,
      "identity" : "IDaxDtjmTgcL5Jr4nmiUM2Xo",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-01-12T06:22:03.09Z",
      "updated_at" : "2017-01-12T06:22:03.55Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/UStrgQnqiv3CFUB8WJriTpj4"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b \
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
  "id" : "WHwmMU1AMnLpD45rBCX5Rscg",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "created_at" : "2017-01-12T06:22:06.04Z",
  "updated_at" : "2017-01-12T06:22:06.04Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHwmMU1AMnLpD45rBCX5Rscg"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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



curl https://api-staging.finix.io/webhooks/WHwmMU1AMnLpD45rBCX5Rscg \
    -H "Content-Type: application/vnd.json+api" \
    -u UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHwmMU1AMnLpD45rBCX5Rscg");

```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHwmMU1AMnLpD45rBCX5Rscg');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHwmMU1AMnLpD45rBCX5Rscg")

```
> Example Response:

```json
{
  "id" : "WHwmMU1AMnLpD45rBCX5Rscg",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APpoubinhFL1cKJsa1YWtG6b",
  "created_at" : "2017-01-12T06:22:06.05Z",
  "updated_at" : "2017-01-12T06:22:06.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHwmMU1AMnLpD45rBCX5Rscg"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
    -u  UStrgQnqiv3CFUB8WJriTpj4:5ec5bf78-40f5-48d0-84f4-146c754d685b

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
      "id" : "WHwmMU1AMnLpD45rBCX5Rscg",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APpoubinhFL1cKJsa1YWtG6b",
      "created_at" : "2017-01-12T06:22:06.05Z",
      "updated_at" : "2017-01-12T06:22:06.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHwmMU1AMnLpD45rBCX5Rscg"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APpoubinhFL1cKJsa1YWtG6b"
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
