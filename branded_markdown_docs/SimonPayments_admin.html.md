---
title: SimonPayments API Reference

language_tabs:
- shell: cURL
- php: PHP



includes:
  - errors

search: true
---

# Guides

## Overview

These guides provide a collection of resources for utilizing the SimonPayments
API and its client libraries. We offer a number of client libraries for
interfacing with the API, and you can view example code snippets for each in
the dark area to the right.

1. [Authentication](#authentication): A quick guide on how to properly
authenticate and interface with the API.

2. [Getting Started](#getting-started): A step-by-step guide demonstrating the basic workflow
of charging a card. This guide will walk you through provisioning merchant
accounts, tokenizing cards, charging those cards, and finally settling (i.e.
payout) those funds out to your merchants.

3. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.simonpayments.com/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Simon/Settings.php');

SimonPayments\Settings::configure([
	"root_url" => 'https://api-staging.simonpayments.com',
	"username" => 'USggcGLbiN1DzFmqVKz66f9W',
	"password" => 'de654913-27be-4121-a503-788edeaccc50']
	);

require(__DIR__ . '/src/Simon/Bootstrap.php');
Simon\Bootstrap::init();

```
To communicate with the SimonPayments API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USggcGLbiN1DzFmqVKz66f9W`

- Password: `de654913-27be-4121-a503-788edeaccc50`

- Application ID: `APFGbQvx9yVjdi79yUu2zCT`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://api-staging.simonpayments.com`

- **Production API:** `https://api.simonpayments.com`

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
use Simon\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PollosHermanos.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
> Example Response:

```json
{
  "id" : "IDtma3vCbxNkHUWAQYoWt22j",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-04-17T23:55:27.93Z",
  "updated_at" : "2017-04-17T23:55:27.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://api-staging.simonpayments.com/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://api-staging.simonpayments.com/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
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
	    "identity": "IDtma3vCbxNkHUWAQYoWt22j"
	}'


```
```php
<?php
use Simon\Resources\Identity;
use Simon\Resources\BankAccount;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
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
	    "identity"=> "IDtma3vCbxNkHUWAQYoWt22j"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
> Example Response:

```json
{
  "id" : "PIuhSrMRaD2vDD3dE1eq3Pdn",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:55:31.87Z",
  "updated_at" : "2017-04-17T23:55:31.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/payment_instruments`

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
curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```php
<?php
use Simon\Resources\Identity;
use Simon\Resources\Merchant;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
> Example Response:

```json
{
  "id" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "verification" : "VIwFBSMZBKuJqTdYs2NxpWmQ",
  "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:55:33.10Z",
  "updated_at" : "2017-04-17T23:55:33.10Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIwFBSMZBKuJqTdYs2NxpWmQ"
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Walter", 
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
```php
<?php
use Simon\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Walter", 
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
> Example Response:

```json
{
  "id" : "IDoa8hFzWBE64D6CF6z4uoTX",
  "entity" : {
    "title" : null,
    "first_name" : "Walter",
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
  "created_at" : "2017-04-17T23:55:34.14Z",
  "updated_at" : "2017-04-17T23:55:34.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/identities`

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


curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "name": "Michae Diaz", 
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
	    "identity": "IDoa8hFzWBE64D6CF6z4uoTX"
	}'


```
```php
<?php
use Simon\Resources\PaymentCard;
use Simon\Resources\Identity;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
$card = new PaymentCard(
	array(
	    "name"=> "Michae Diaz", 
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
	    "identity"=> "IDoa8hFzWBE64D6CF6z4uoTX"
	));
$card = $identity->createPaymentCard($card);

```
> Example Response:

```json
{
  "id" : "PInigLmfucovqz3CCsfYxcm5",
  "fingerprint" : "FPR439487516",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Michae Diaz",
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
  "created_at" : "2017-04-17T23:55:34.58Z",
  "updated_at" : "2017-04-17T23:55:34.58Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoa8hFzWBE64D6CF6z4uoTX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/updates"
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

`POST https://api-staging.simonpayments.com/payment_instruments`

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
curl https://api-staging.simonpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "merchant_identity": "IDtma3vCbxNkHUWAQYoWt22j", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PInigLmfucovqz3CCsfYxcm5", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
use Simon\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDtma3vCbxNkHUWAQYoWt22j", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PInigLmfucovqz3CCsfYxcm5", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
> Example Response:

```json
{
  "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:39.78Z",
  "updated_at" : "2017-04-17T23:55:39.84Z",
  "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:55:39.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
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

`POST https://api-staging.simonpayments.com/authorizations`

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
curl https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```php
<?php
use Simon\Resources\Authorization;

$authorization = Authorization::retrieve('AUo9RDTFsGZV7vDRHyTXtTEd');
$authorization = $authorization->capture(50, 10);

```
> Example Response:

```json
{
  "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2FgDQNE8QPEBH5mCvWuPgn",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:39.73Z",
  "updated_at" : "2017-04-17T23:55:40.59Z",
  "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:55:39.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
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

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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
of PCI scope by sending this info over SSL directly to SimonPayments. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/4urqd3tr/4/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the SimonPayments API.
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
<script type="text/javascript" src="https://js.paymentsfnx.com/simon-payments/tokenize.js"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: 'APFGbQvx9yVjdi79yUu2zCT',
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
  "id" : "TKtBQmgVMMyaYCxCBuaZMzDa",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:55:41.67Z",
  "updated_at" : "2017-04-17T23:55:41.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:55:41.67Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "token": "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type": "TOKEN", 
	    "identity": "IDtma3vCbxNkHUWAQYoWt22j"
	}'


```
```php
<?php
use Simon\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDtma3vCbxNkHUWAQYoWt22j"
	));
$card = $card->save();

```
> Example Response:

```json
{
  "id" : "PItBQmgVMMyaYCxCBuaZMzDa",
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
  "created_at" : "2017-04-17T23:55:42.08Z",
  "updated_at" : "2017-04-17T23:55:42.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/updates"
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

`POST https://api-staging.simonpayments.com/payment_instruments`


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
[jsFiddle example](https://jsfiddle.net/rserna2010/0ouyja68/).

### Step 1: Include library

```html
 <script type="text/javascript" src="https://js.verygoodvault.com/js-vgfield-2/simon-payments.js"></script>
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
    secureForm.submit('/applications/APFGbQvx9yVjdi79yUu2zCT/tokens', {
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
  "id" : "TKtBQmgVMMyaYCxCBuaZMzDa",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:55:41.67Z",
  "updated_at" : "2017-04-17T23:55:41.67Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:55:41.67Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "token": "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type": "TOKEN", 
	    "identity": "IDtma3vCbxNkHUWAQYoWt22j"
	}'

```
```php
<?php
use SimonPayments\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDtma3vCbxNkHUWAQYoWt22j"
	));
$card = $card->save();

```
> Example Response:

```json
{
  "id" : "PItBQmgVMMyaYCxCBuaZMzDa",
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
  "created_at" : "2017-04-17T23:55:42.08Z",
  "updated_at" : "2017-04-17T23:55:42.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/updates"
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

`POST https://api-staging.simonpayments.com/payment_instruments`


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

3. [Fees](#fees): A guide describing the four different pricing tiers

##Fees

You can find the live example of how fees are calculated in this [spreadsheet](https://docs.google.com/spreadsheets/d/1UFmKg7EvhlCduM31bQ3rOeslszOlO49rOw3frllBj9c/edit#gid=0)

### Case 1
- Fee profile not set
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.00 | $100.00 | $0.00 | $0.00 | $0.00 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.00 | $90.00 | $10.00 | $0.00 | $0.00 |

### Case 2
- Fee profile not set
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.11 | $90.00 | $9.89 | $0.11 | $0.11 |
| $100 | $0.10 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |

### Case 3
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.00 | $96.00 | $0.80 | $3.20 | $3.20 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.00 | $1.00 | $95.80 | $3.20 | $3.20 |

### Case 4
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.11 | $96.00 | $0.69 | $3.31 | $3.31 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.11 | $1.00 | $95.69 | $3.31 | $3.31 |

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
curl https://api-staging.simonpayments.com/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "role": "ROLE_PARTNER"
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USggcGLbiN1DzFmqVKz66f9W",
  "password" : "de654913-27be-4121-a503-788edeaccc50",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:24.68Z",
  "updated_at" : "2017-04-17T23:55:24.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USggcGLbiN1DzFmqVKz66f9W"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
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

`POST https://api-staging.simonpayments.com/users`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user (use ROLE_PARTNER when creating a new `Application`)

### Step 2: Create the Application
```shell
curl https://api-staging.simonpayments.com/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "tags": {
	        "application_name": "Dwolla"
	    }, 
	    "user": "USggcGLbiN1DzFmqVKz66f9W", 
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
	        "doing_business_as": "Dwolla", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Dwolla", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
use Simon\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Dwolla"
	    ), 
	    "user"=> "USggcGLbiN1DzFmqVKz66f9W", 
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
	        "doing_business_as"=> "Dwolla", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Dwolla", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:25.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
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

`POST https://api-staging.simonpayments.com/applications`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
user | *string*, **required** | User ID for the owner of the `Application`


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
### Step 3: Enable a Processor
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "canDebitBankAccount": true, 
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "PRaU67ANhpXpXkmH6bQEb8LT",
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "default_merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "created_at" : "2017-04-17T23:55:25.65Z",
  "updated_at" : "2017-04-17T23:55:25.65Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors/PRaU67ANhpXpXkmH6bQEb8LT"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Great! Now that we have an `Application`, let's enable a `Processor` for it to
transact on. A `Processor` represents the acquiring platform where `Merchants`
accounts are provisioned, and ultimately, where `Transfers` are processed.
The SimonPayments Payment Platform is processor agnostic allowing for processing transactions
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

`POST https://api-staging.simonpayments.com/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

### Step 4: Enable Processing Functionality
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:56.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
    }
  }
}
```

Now that we have a processor associated with an `Application` we'll want to
enable its ability to creaet new `Transfers` and `Authorizations`. This same
method can be used to shut off its ability to process transactions as a form of
risk management.

#### HTTP Request

`PUT https://api-staging.simonpayments.com/applications/:APPLICATION_ID`

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
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:56.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
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

`PUT https://api-staging.simonpayments.com/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `APPLICATION`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
settlement_enabled | *boolean*, **required** | True to enable
# Fees

 You can find the live example of how fees are calculated in this [spreadsheet](https://docs.google.com/spreadsheets/d/1UFmKg7EvhlCduM31bQ3rOeslszOlO49rOw3frllBj9c/edit#gid=0)

## Case 1 
- Fee profile not set
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.00 | $100.00 | $0.00 | $0.00 | $0.00 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.00 | $90.00 | $10.00 | $0.00 | $0.00 |

## Case 2
- Fee profile not set
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |
| $100 | $10.00 | 0c+0% ($0.00) | $0.11 | $90.00 | $9.89 | $0.11 | $0.11 |
| $100 | $0.10 | 0c+0% ($0.00) | $0.11 | $99.89 | $0.00 | $0.11 | $0.11 |

## Case 3 
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `FALSE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.00 | $96.80 | $0.00 | $3.20 | $3.20 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.00 | $96.00 | $0.80 | $3.20 | $3.20 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.00 | $1.00 | $95.80 | $3.20 | $3.20 |

## Case 4 
- Fee profile is set to `30c + 2.9%`
- Charge interchange fee is set to `TRUE`

| Transfer Amount | Transfer Fee | Platform Fee Profile (Fixed+BPS) | Interchange Fee | Merchant | Application | Platform | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $100 | $0.00 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $0.10 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $3.20 | 30c+2.9% ($3.20) | $0.11 | $96.69 | $0.00 | $3.31 | $3.31 |
| $100 | $4.00 | 30c+2.9% ($3.20) | $0.11 | $96.00 | $0.69 | $3.31 | $3.31 |
| $100 | $99.00 | 30c+2.9% ($3.20) | $0.11 | $1.00 | $95.69 | $3.31 | $3.31 |

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
# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
```php
<?php
use Simon\Resources\Application;

$application = Application::retrieve('APFGbQvx9yVjdi79yUu2zCT');

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:27.18Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## Create an Application
```shell
curl https://api-staging.simonpayments.com/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "tags": {
	        "application_name": "Dwolla"
	    }, 
	    "user": "USggcGLbiN1DzFmqVKz66f9W", 
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
	        "doing_business_as": "Dwolla", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Dwolla", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
use Simon\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Dwolla"
	    ), 
	    "user"=> "USggcGLbiN1DzFmqVKz66f9W", 
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
	        "doing_business_as"=> "Dwolla", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Dwolla", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:25.05Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
    }
  }
}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can create a new Application.
</aside>

#### HTTP Request

`POST https://api-staging.simonpayments.com/applications`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
user | *string*, **required** | User ID for the owner of the `Application`


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
## [ADMIN] Disable Processing Functionality
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:54.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
    }
  }
}
```

Disable an `Applications's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-staging.simonpayments.com/applications/:APPLICATION_ID`

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
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "APFGbQvx9yVjdi79yUu2zCT",
  "enabled" : true,
  "tags" : {
    "application_name" : "Dwolla"
  },
  "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-04-17T23:55:25.05Z",
  "updated_at" : "2017-04-17T23:55:54.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
    }
  }
}
```

Disable an `Applications's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-staging.simonpayments.com/applications/:APPLICATION_ID`

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
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USqPrkUJeqchBDQU3ycCEHUM",
  "password" : "3ac08302-f50f-4e6b-841c-c520f24c9b27",
  "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:26.52Z",
  "updated_at" : "2017-04-17T23:55:26.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USqPrkUJeqchBDQU3ycCEHUM"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## [ADMIN] Enable the Dummy Processor (i.e. Sandbox)
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "type": "DUMMY_V1", 
	    "config": {
	        "canDebitBankAccount": true, 
	        "key2": "value-2", 
	        "key1": "value-1"
	    }
	}

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "PRaU67ANhpXpXkmH6bQEb8LT",
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "default_merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "created_at" : "2017-04-17T23:55:25.65Z",
  "updated_at" : "2017-04-17T23:55:25.65Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors/PRaU67ANhpXpXkmH6bQEb8LT"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/applications/:APPLICATION_ID/processors`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## [ADMIN] List all Applications
```shell
curl https://api-staging.simonpayments.com/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APFGbQvx9yVjdi79yUu2zCT",
      "enabled" : true,
      "tags" : {
        "application_name" : "Dwolla"
      },
      "owner" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-04-17T23:55:25.05Z",
      "updated_at" : "2017-04-17T23:55:27.18Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "processors" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/processors"
        },
        "users" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/application_profile"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/applications/`


# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-staging.simonpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "merchant_identity": "IDtma3vCbxNkHUWAQYoWt22j", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PInigLmfucovqz3CCsfYxcm5", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
use Simon\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDtma3vCbxNkHUWAQYoWt22j", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PInigLmfucovqz3CCsfYxcm5", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
> Example Response:

```json
{
  "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:39.78Z",
  "updated_at" : "2017-04-17T23:55:39.84Z",
  "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:55:39.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
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

`POST https://api-staging.simonpayments.com/authorizations`

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
curl https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```php
<?php
use Simon\Resources\Authorization;

$authorization = Authorization::retrieve('AUo9RDTFsGZV7vDRHyTXtTEd');
$authorization = $authorization->capture(50, 10);

```
> Example Response:

```json
{
  "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2FgDQNE8QPEBH5mCvWuPgn",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:39.73Z",
  "updated_at" : "2017-04-17T23:55:40.59Z",
  "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:55:39.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
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

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.simonpayments.com/authorizations/AU3V9vkYbQxHCXNqAcJxwcnq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```php
<?php
use Simon\Resources\Authorization;

$authorization = Authorization::retrieve('AUo9RDTFsGZV7vDRHyTXtTEd');
$authorization->void(true);
$authorization = $authorization->save();


```
> Example Response:

```json
{
  "id" : "AU3V9vkYbQxHCXNqAcJxwcnq",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:42.65Z",
  "updated_at" : "2017-04-17T23:55:43.38Z",
  "trace_id" : "f9c2231c-eaa8-4c28-9f00-31a0d131daf4",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : true,
  "expires_at" : "2017-04-24T23:55:42.65Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU3V9vkYbQxHCXNqAcJxwcnq"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

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

curl https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Authorization;

$authorization = Authorization::retrieve('AUo9RDTFsGZV7vDRHyTXtTEd');

```
> Example Response:

```json
{
  "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR2FgDQNE8QPEBH5mCvWuPgn",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:39.73Z",
  "updated_at" : "2017-04-17T23:55:40.59Z",
  "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "is_void" : false,
  "expires_at" : "2017-04-24T23:55:39.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://api-staging.simonpayments.com/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Authorization;

$authorizations = Authorization::getPagination("/authorizations");


```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU3V9vkYbQxHCXNqAcJxwcnq",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:42.65Z",
      "updated_at" : "2017-04-17T23:55:43.38Z",
      "trace_id" : "f9c2231c-eaa8-4c28-9f00-31a0d131daf4",
      "source" : "PInigLmfucovqz3CCsfYxcm5",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "is_void" : true,
      "expires_at" : "2017-04-24T23:55:42.65Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AU3V9vkYbQxHCXNqAcJxwcnq"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        }
      }
    }, {
      "id" : "AUo9RDTFsGZV7vDRHyTXtTEd",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR2FgDQNE8QPEBH5mCvWuPgn",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:39.73Z",
      "updated_at" : "2017-04-17T23:55:40.59Z",
      "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
      "source" : "PInigLmfucovqz3CCsfYxcm5",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "is_void" : false,
      "expires_at" : "2017-04-24T23:55:39.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AUo9RDTFsGZV7vDRHyTXtTEd"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "transfer" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/authorizations/`

# Identities

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.

## Create an Identity for a Buyer


```shell


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Walter", 
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
```php
<?php
use Simon\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Walter", 
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
> Example Response:

```json
{
  "id" : "IDoa8hFzWBE64D6CF6z4uoTX",
  "entity" : {
    "title" : null,
    "first_name" : "Walter",
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
  "created_at" : "2017-04-17T23:55:34.14Z",
  "updated_at" : "2017-04-17T23:55:34.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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

## Create an Identity for a Sender
```shell


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": true, 
	        "default_statement_descriptor": "Pollos Hermanos", 
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
	        "doing_business_as": "Pollos Hermanos", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Pollos Hermanos", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.PollosHermanos.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
use Simon\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pollos Hermanos", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PollosHermanos.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
> Example Response:

```json
{
  "id" : "IDtma3vCbxNkHUWAQYoWt22j",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-04-17T23:55:27.93Z",
  "updated_at" : "2017-04-17T23:55:27.93Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account
for your seller. This requires 3-steps:

1. Create an `Identity` resource with the sender's underwriting and identity
verification information (API request to the right)


2. [Create a Payment Instrument](#create-a-card) representing the
sender's bank account where processed funds will be settled (i.e. deposited)



#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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
## Retrieve a Identity
```shell

curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Identity;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
```
> Example Response:

```json
{
  "id" : "IDtma3vCbxNkHUWAQYoWt22j",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-04-17T23:55:27.92Z",
  "updated_at" : "2017-04-17T23:55:27.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Update an Identity
```shell
curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Lopez", 
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
```php
<?php

```
> Example Response:

```json
{
  "id" : "IDtma3vCbxNkHUWAQYoWt22j",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Lopez",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
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
    "key" : "value_2"
  },
  "created_at" : "2017-04-17T23:55:27.92Z",
  "updated_at" : "2017-04-17T23:55:52.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/identities`

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
## List all Identities
```shell
curl https://api-staging.simonpayments.com/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50


```
```php
<?php
use Simon\Resources\Identity;

$identities= Identity::getPagination("/identities");


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDoa8hFzWBE64D6CF6z4uoTX",
      "entity" : {
        "title" : null,
        "first_name" : "Walter",
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
      "created_at" : "2017-04-17T23:55:34.13Z",
      "updated_at" : "2017-04-17T23:55:34.13Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDvF3GhAC1NyUtS1R5LBaqex",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Golds Gym"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:55:31.22Z",
      "updated_at" : "2017-04-17T23:55:31.22Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDvF3GhAC1NyUtS1R5LBaqex/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDtVtpVonen2QnrkZcquu8kJ",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:55:30.69Z",
      "updated_at" : "2017-04-17T23:55:30.69Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtVtpVonen2QnrkZcquu8kJ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDto1uWzn1PbVeadTWRE29kQ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-04-17T23:55:30.24Z",
      "updated_at" : "2017-04-17T23:55:30.24Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDto1uWzn1PbVeadTWRE29kQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDdLkGCxsqr4nbT8MKpTiMLb",
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
      "created_at" : "2017-04-17T23:55:29.78Z",
      "updated_at" : "2017-04-17T23:55:29.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDdLkGCxsqr4nbT8MKpTiMLb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "ID78PHZf1UQ5n7LUV3sZjK3W",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
      "created_at" : "2017-04-17T23:55:29.32Z",
      "updated_at" : "2017-04-17T23:55:29.32Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID78PHZf1UQ5n7LUV3sZjK3W/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "ID7q6BhYBbH2cyvv3q9eYNHL",
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
      "created_at" : "2017-04-17T23:55:28.91Z",
      "updated_at" : "2017-04-17T23:55:28.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7q6BhYBbH2cyvv3q9eYNHL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDhHDfQmEAS7VmRRud3fzCg8",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
      "created_at" : "2017-04-17T23:55:28.38Z",
      "updated_at" : "2017-04-17T23:55:28.38Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDhHDfQmEAS7VmRRud3fzCg8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDtma3vCbxNkHUWAQYoWt22j",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2017-04-17T23:55:27.92Z",
      "updated_at" : "2017-04-17T23:55:27.92Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dwolla",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Dwolla",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
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
        "application_name" : "Dwolla"
      },
      "created_at" : "2017-04-17T23:55:25.05Z",
      "updated_at" : "2017-04-17T23:55:25.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/identities/`


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```php
<?php
use Simon\Resources\Identity;
use Simon\Resources\Merchant;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
> Example Response:

```json
{
  "id" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "verification" : "VIwFBSMZBKuJqTdYs2NxpWmQ",
  "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:55:33.10Z",
  "updated_at" : "2017-04-17T23:55:33.10Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIwFBSMZBKuJqTdYs2NxpWmQ"
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Retrieve a Merchant
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Merchant;

$merchant = Merchant::retrieve('MUc1gfNsE961YtNQxVwHeKm2');

```
> Example Response:

```json
{
  "id" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "verification" : null,
  "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:55:33.07Z",
  "updated_at" : "2017-04-17T23:55:33.26Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'

```
```php
<?php
use Simon\Resources\Merchant;
use Simon\Resources\Verification;

$merchant = Merchant::retrieve('MUc1gfNsE961YtNQxVwHeKm2');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
> Example Response:

```json
{
  "id" : "VItvhf2pokNjtjMtYDK9HKzV",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:55:53.20Z",
  "updated_at" : "2017-04-17T23:55:53.23Z",
  "trace_id" : "6db59476-5d73-4897-aef3-e8540c84bc9b",
  "payment_instrument" : null,
  "merchant" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VItvhf2pokNjtjMtYDK9HKzV"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    }
  }
}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Reattempt Merchant Provisioning
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'
```
```php
<?php
use Simon\Resources\Merchant;
use Simon\Resources\Verification;

$merchant = Merchant::retrieve('MUc1gfNsE961YtNQxVwHeKm2');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
> Example Response:

```json
{
  "id" : "VItvhf2pokNjtjMtYDK9HKzV",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-04-17T23:55:53.20Z",
  "updated_at" : "2017-04-17T23:55:53.23Z",
  "trace_id" : "6db59476-5d73-4897-aef3-e8540c84bc9b",
  "payment_instrument" : null,
  "merchant" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VItvhf2pokNjtjMtYDK9HKzV"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    }
  }
}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Disable Processing Functionality
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "verification" : null,
  "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-04-17T23:55:33.07Z",
  "updated_at" : "2017-04-17T23:55:53.55Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Disable a `Merchant's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-staging.simonpayments.com/merchants/:MERCHANT_ID`

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
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "MUc1gfNsE961YtNQxVwHeKm2",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "verification" : null,
  "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:55:33.07Z",
  "updated_at" : "2017-04-17T23:55:53.89Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```
Disable a `Merchant's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-staging.simonpayments.com/merchants/:MERCHANT_ID`

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
curl https://api-staging.simonpayments.com/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Merchant;

$merchants = Merchant::getPagination("/merchants");


```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUc1gfNsE961YtNQxVwHeKm2",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "verification" : null,
      "merchant_profile" : "MP2Aagi3CMbpny1AMkBQtD7X",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.26Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP2Aagi3CMbpny1AMkBQtD7X"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/merchants/`

## List Merchant Verifications
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Merchant;
use Simon\Resources\Verification;

$merchant = Merchant::retrieve('MUc1gfNsE961YtNQxVwHeKm2');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIwFBSMZBKuJqTdYs2NxpWmQ",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.32Z",
      "trace_id" : "5a20c1f9-9b22-4043-adc9-2ba61c13c442",
      "payment_instrument" : null,
      "merchant" : "MUc1gfNsE961YtNQxVwHeKm2",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/verifications/VIwFBSMZBKuJqTdYs2NxpWmQ"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "merchant" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`




## [ADMIN] List Merchant Verifications
```shell
curl https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
```php
<?php

```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIwFBSMZBKuJqTdYs2NxpWmQ",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.32Z",
      "trace_id" : "5a20c1f9-9b22-4043-adc9-2ba61c13c442",
      "payment_instrument" : null,
      "merchant" : "MUc1gfNsE961YtNQxVwHeKm2",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/verifications/VIwFBSMZBKuJqTdYs2NxpWmQ"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "merchant" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUc1gfNsE961YtNQxVwHeKm2/verifications?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`


## Create a Merchant User
```shell
curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USFUyBJB9ZAKN6SrQkXrRyM",
  "password" : "1e052e66-6cdc-47cc-acfd-3b432063ca18",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:36.97Z",
  "updated_at" : "2017-04-17T23:55:36.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USFUyBJB9ZAKN6SrQkXrRyM"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/users`

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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "token": "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type": "TOKEN", 
	    "identity": "IDtma3vCbxNkHUWAQYoWt22j"
	}'


```
```php
<?php
use Simon\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKtBQmgVMMyaYCxCBuaZMzDa", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDtma3vCbxNkHUWAQYoWt22j"
	));
$card = $card->save();

```
> Example Response:

```json
{
  "id" : "PItBQmgVMMyaYCxCBuaZMzDa",
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
  "created_at" : "2017-04-17T23:55:42.08Z",
  "updated_at" : "2017-04-17T23:55:42.08Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/updates"
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

`POST https://api-staging.simonpayments.com/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Create a Card
```shell


curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
	{
	    "name": "Michae Diaz", 
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
	    "identity": "IDoa8hFzWBE64D6CF6z4uoTX"
	}'


```
```php
<?php
use Simon\Resources\PaymentCard;
use Simon\Resources\Identity;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
$card = new PaymentCard(
	array(
	    "name"=> "Michae Diaz", 
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
	    "identity"=> "IDoa8hFzWBE64D6CF6z4uoTX"
	));
$card = $identity->createPaymentCard($card);

```
> Example Response:

```json
{
  "id" : "PInigLmfucovqz3CCsfYxcm5",
  "fingerprint" : "FPR439487516",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Michae Diaz",
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
  "created_at" : "2017-04-17T23:55:34.58Z",
  "updated_at" : "2017-04-17T23:55:34.58Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoa8hFzWBE64D6CF6z4uoTX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/updates"
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

`POST https://api-staging.simonpayments.com/payment_instruments`

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

curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
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
	    "identity": "IDtma3vCbxNkHUWAQYoWt22j"
	}'


```
```php
<?php
use Simon\Resources\Identity;
use Simon\Resources\BankAccount;

$identity = Identity::retrieve('IDtma3vCbxNkHUWAQYoWt22j');
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
	    "identity"=> "IDtma3vCbxNkHUWAQYoWt22j"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
> Example Response:

```json
{
  "id" : "PIuhSrMRaD2vDD3dE1eq3Pdn",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:55:31.87Z",
  "updated_at" : "2017-04-17T23:55:31.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.simonpayments.com/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **required** | Account owner's full name (max 40 characters)
## Fetch a Bank Account

```shell
curl https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \

```
```php
<?php
use Simon\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PIuhSrMRaD2vDD3dE1eq3Pdn');

```
> Example Response:

```json
{
  "id" : "PIuhSrMRaD2vDD3dE1eq3Pdn",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-04-17T23:55:31.84Z",
  "updated_at" : "2017-04-17T23:55:32.48Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `BANK_ACCOUNT`

#### HTTP Request

`GET https://api-staging.simonpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Fetch a Credit Card
```shell
curl https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \

```
```php
<?php
use Simon\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PInigLmfucovqz3CCsfYxcm5');

```
> Example Response:

```json
{
  "id" : "PInigLmfucovqz3CCsfYxcm5",
  "fingerprint" : "FPR439487516",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Michae Diaz",
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
  "created_at" : "2017-04-17T23:55:34.55Z",
  "updated_at" : "2017-04-17T23:55:39.81Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDoa8hFzWBE64D6CF6z4uoTX",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://api-staging.simonpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## List all Payment Instruments

```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50
```
```php
<?php
use Simon\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PItBQmgVMMyaYCxCBuaZMzDa",
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
      "created_at" : "2017-04-17T23:55:42.04Z",
      "updated_at" : "2017-04-17T23:55:42.04Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PItBQmgVMMyaYCxCBuaZMzDa/updates"
        }
      }
    }, {
      "id" : "PInpunYcAnbEjjnAWR6HjnYf",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:55:35.00Z",
      "updated_at" : "2017-04-17T23:55:35.00Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDoa8hFzWBE64D6CF6z4uoTX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInpunYcAnbEjjnAWR6HjnYf"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInpunYcAnbEjjnAWR6HjnYf/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInpunYcAnbEjjnAWR6HjnYf/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInpunYcAnbEjjnAWR6HjnYf/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PInigLmfucovqz3CCsfYxcm5",
      "fingerprint" : "FPR439487516",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Michae Diaz",
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
      "created_at" : "2017-04-17T23:55:34.55Z",
      "updated_at" : "2017-04-17T23:55:39.81Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDoa8hFzWBE64D6CF6z4uoTX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDoa8hFzWBE64D6CF6z4uoTX"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5/updates"
        }
      }
    }, {
      "id" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.07Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PIw1exxcsXPGF2xXYRrT6Xog",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.07Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw1exxcsXPGF2xXYRrT6Xog"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw1exxcsXPGF2xXYRrT6Xog/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw1exxcsXPGF2xXYRrT6Xog/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw1exxcsXPGF2xXYRrT6Xog/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PIezeXg5ixi2iSDn6fqrt9eb",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:33.07Z",
      "updated_at" : "2017-04-17T23:55:33.07Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIezeXg5ixi2iSDn6fqrt9eb"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIezeXg5ixi2iSDn6fqrt9eb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIezeXg5ixi2iSDn6fqrt9eb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIezeXg5ixi2iSDn6fqrt9eb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PIuhSrMRaD2vDD3dE1eq3Pdn",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-04-17T23:55:31.84Z",
      "updated_at" : "2017-04-17T23:55:32.48Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIuhSrMRaD2vDD3dE1eq3Pdn/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PIbNsXAfgYLCSRJKq3WhmvQs",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:25.62Z",
      "updated_at" : "2017-04-17T23:55:25.62Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbNsXAfgYLCSRJKq3WhmvQs"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbNsXAfgYLCSRJKq3WhmvQs/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbNsXAfgYLCSRJKq3WhmvQs/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbNsXAfgYLCSRJKq3WhmvQs/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PI3mcukXSybPDECBN3VkbWMt",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:25.62Z",
      "updated_at" : "2017-04-17T23:55:25.62Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI3mcukXSybPDECBN3VkbWMt"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI3mcukXSybPDECBN3VkbWMt/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI3mcukXSybPDECBN3VkbWMt/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI3mcukXSybPDECBN3VkbWMt/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PIwiUUDNGbCtYq1XABiec4aM",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:25.62Z",
      "updated_at" : "2017-04-17T23:55:25.62Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2f67hZpBDEM1xBfKSp7LPD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwiUUDNGbCtYq1XABiec4aM"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwiUUDNGbCtYq1XABiec4aM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2f67hZpBDEM1xBfKSp7LPD"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwiUUDNGbCtYq1XABiec4aM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIwiUUDNGbCtYq1XABiec4aM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "PI4qdZnrzBuKUNhxWG8hpWEL",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-04-17T23:55:25.62Z",
      "updated_at" : "2017-04-17T23:55:25.62Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4qdZnrzBuKUNhxWG8hpWEL"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4qdZnrzBuKUNhxWG8hpWEL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDeh2Y4XZcVkqYzHZNQpD1w2"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4qdZnrzBuKUNhxWG8hpWEL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI4qdZnrzBuKUNhxWG8hpWEL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/payment_instruments`

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
## Retrieve a Transfer
```shell

curl https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50


```
```php
<?php
use Simon\Resources\Transfer;

$transfer = Transfer::retrieve('TR9xU2PXKwEnP5w5yMU7HLbE');



```
> Example Response:

```json
{
  "id" : "TR9xU2PXKwEnP5w5yMU7HLbE",
  "amount" : 583176,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "8f9ab6d4-95b9-4082-8a63-9f1f327af20b",
  "currency" : "USD",
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "source" : "PInigLmfucovqz3CCsfYxcm5",
  "destination" : "PIbV8rUY7NqrYJdZj1f1tCJN",
  "ready_to_settle_at" : null,
  "fee" : 58318,
  "statement_descriptor" : "SPN*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:35.49Z",
  "updated_at" : "2017-04-17T23:55:35.71Z",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/disputes"
    },
    "source" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```php
<?php
use Simon\Resources\Transfer;

$debit = Transfer::retrieve('TR9xU2PXKwEnP5w5yMU7HLbE');
$refund = $debit->reverse(11);
```
> Example Response:

```json
{
  "id" : "TRpoMUo9Tmdtybj3NSM3K4sd",
  "amount" : 308872,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "bd70d747-6455-4774-83d0-da020f8a02d4",
  "currency" : "USD",
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "source" : "PIbV8rUY7NqrYJdZj1f1tCJN",
  "destination" : "PInigLmfucovqz3CCsfYxcm5",
  "ready_to_settle_at" : null,
  "fee" : 30887,
  "statement_descriptor" : "SPN*POLLOS HERMANOS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:55:38.97Z",
  "updated_at" : "2017-04-17T23:55:39.08Z",
  "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRpoMUo9Tmdtybj3NSM3K4sd"
    },
    "parent" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRpoMUo9Tmdtybj3NSM3K4sd/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://api-staging.simonpayments.com/transfers/:TRANSFER_ID/reversals`

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
curl https://api-staging.simonpayments.com/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR2FgDQNE8QPEBH5mCvWuPgn",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "fc2d551c-5b45-4e7a-a046-713d43a35e73",
      "currency" : "USD",
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "source" : "PInigLmfucovqz3CCsfYxcm5",
      "destination" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "SPN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:40.42Z",
      "updated_at" : "2017-04-17T23:55:40.59Z",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR2FgDQNE8QPEBH5mCvWuPgn/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
        }
      }
    }, {
      "id" : "TRpoMUo9Tmdtybj3NSM3K4sd",
      "amount" : 308872,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "04257f99-578b-490f-bbe0-d9aefcb4434d",
      "currency" : "USD",
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "source" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "destination" : "PInigLmfucovqz3CCsfYxcm5",
      "ready_to_settle_at" : null,
      "fee" : 30887,
      "statement_descriptor" : "SPN*POLLOS HERMANOS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:38.81Z",
      "updated_at" : "2017-04-17T23:55:39.08Z",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRpoMUo9Tmdtybj3NSM3K4sd"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRpoMUo9Tmdtybj3NSM3K4sd/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "parent" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
        }
      }
    }, {
      "id" : "TRfqedrkG7ULDCdstBsh7fkH",
      "amount" : 308872,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "f11dc452-deb2-48a1-ab0a-f0e999a21562",
      "currency" : "USD",
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "source" : "PInigLmfucovqz3CCsfYxcm5",
      "destination" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "ready_to_settle_at" : null,
      "fee" : 30887,
      "statement_descriptor" : "SPN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:38.21Z",
      "updated_at" : "2017-04-17T23:55:38.92Z",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRfqedrkG7ULDCdstBsh7fkH/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
        }
      }
    }, {
      "id" : "TR6P22fZtBnA5E2u6SvMwSC1",
      "amount" : 170524,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "e15dbb53-541d-488f-9cc0-449aad83cf32",
      "currency" : "USD",
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "source" : "PInpunYcAnbEjjnAWR6HjnYf",
      "destination" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "ready_to_settle_at" : null,
      "fee" : 17052,
      "statement_descriptor" : "SPN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:36.20Z",
      "updated_at" : "2017-04-17T23:55:36.34Z",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6P22fZtBnA5E2u6SvMwSC1"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6P22fZtBnA5E2u6SvMwSC1/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6P22fZtBnA5E2u6SvMwSC1/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6P22fZtBnA5E2u6SvMwSC1/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6P22fZtBnA5E2u6SvMwSC1/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInpunYcAnbEjjnAWR6HjnYf"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
        }
      }
    }, {
      "id" : "TR9xU2PXKwEnP5w5yMU7HLbE",
      "amount" : 583176,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "8f9ab6d4-95b9-4082-8a63-9f1f327af20b",
      "currency" : "USD",
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "source" : "PInigLmfucovqz3CCsfYxcm5",
      "destination" : "PIbV8rUY7NqrYJdZj1f1tCJN",
      "ready_to_settle_at" : null,
      "fee" : 58318,
      "statement_descriptor" : "SPN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:55:35.49Z",
      "updated_at" : "2017-04-17T23:55:35.71Z",
      "merchant_identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR9xU2PXKwEnP5w5yMU7HLbE/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PInigLmfucovqz3CCsfYxcm5"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIbV8rUY7NqrYJdZj1f1tCJN"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/transfers`
# Users (API Keys)

A `User` resource represents a pair of API keys which are used to perform
authenticated requests against the SimonPayments API. When making authenticated
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


## Create ROLE_PARTNER User
```shell
curl https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USqPrkUJeqchBDQU3ycCEHUM",
  "password" : "3ac08302-f50f-4e6b-841c-c520f24c9b27",
  "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:26.52Z",
  "updated_at" : "2017-04-17T23:55:26.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USqPrkUJeqchBDQU3ycCEHUM"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## Create ROLE_MERCHANT User
```shell
curl https://api-staging.simonpayments.com/identities/IDtma3vCbxNkHUWAQYoWt22j/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '{}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USFUyBJB9ZAKN6SrQkXrRyM",
  "password" : "1e052e66-6cdc-47cc-acfd-3b432063ca18",
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:36.97Z",
  "updated_at" : "2017-04-17T23:55:36.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USFUyBJB9ZAKN6SrQkXrRyM"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
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

`POST https://api-staging.simonpayments.com/identities/:IDENTITY_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the merchant's `Identity`



## Retrieve a User
```shell
curl https://api-staging.simonpayments.com/users/TR9xU2PXKwEnP5w5yMU7HLbE \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USggcGLbiN1DzFmqVKz66f9W",
  "password" : null,
  "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:24.68Z",
  "updated_at" : "2017-04-17T23:55:25.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USggcGLbiN1DzFmqVKz66f9W"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User`

## Disable a User
```shell
curl https://api-staging.simonpayments.com/users/USFUyBJB9ZAKN6SrQkXrRyM \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
```php
<?php

```
> Example Response:

```json
{
  "id" : "USFUyBJB9ZAKN6SrQkXrRyM",
  "password" : null,
  "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-04-17T23:55:36.95Z",
  "updated_at" : "2017-04-17T23:55:37.48Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USFUyBJB9ZAKN6SrQkXrRyM"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

Disable API keys (i.e. credentials) for a previously created `User`

<aside class="notice">
Only Users with ROLE_PLATFORM can disable another user.
</aside>


#### HTTP Request


`PUT https://api-staging.simonpayments.com/users/user_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
user_id | ID of the `User` you would like to disable

## List all Users
```shell
curl https://api-staging.simonpayments.com/users/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USFUyBJB9ZAKN6SrQkXrRyM",
      "password" : null,
      "identity" : "IDtma3vCbxNkHUWAQYoWt22j",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-04-17T23:55:36.95Z",
      "updated_at" : "2017-04-17T23:55:37.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/USFUyBJB9ZAKN6SrQkXrRyM"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "USqPrkUJeqchBDQU3ycCEHUM",
      "password" : null,
      "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:55:26.50Z",
      "updated_at" : "2017-04-17T23:55:26.50Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/USqPrkUJeqchBDQU3ycCEHUM"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    }, {
      "id" : "USggcGLbiN1DzFmqVKz66f9W",
      "password" : null,
      "identity" : "IDeh2Y4XZcVkqYzHZNQpD1w2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-04-17T23:55:24.68Z",
      "updated_at" : "2017-04-17T23:55:25.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/USggcGLbiN1DzFmqVKz66f9W"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/users`

# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the SimonPayments API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://api-staging.simonpayments.com/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```php
<?php
use Simon\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
$webhook = $webhook->save();

```
> Example Response:

```json
{
  "id" : "WHhNHoVtmUfZGBvAqwNQ8yP4",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "created_at" : "2017-04-17T23:55:27.58Z",
  "updated_at" : "2017-04-17T23:55:27.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WHhNHoVtmUfZGBvAqwNQ8yP4"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.simonpayments.com/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request (max 120 characters)


## Retrieve a Webhook

```shell



curl https://api-staging.simonpayments.com/webhooks/WHhNHoVtmUfZGBvAqwNQ8yP4 \
    -H "Content-Type: application/vnd.json+api" \
    -u USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50


```
```php
<?php
use Simon\Resources\Webhook;

$webhook = Webhook::retrieve('WHhNHoVtmUfZGBvAqwNQ8yP4');



```
> Example Response:

```json
{
  "id" : "WHhNHoVtmUfZGBvAqwNQ8yP4",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APFGbQvx9yVjdi79yUu2zCT",
  "created_at" : "2017-04-17T23:55:27.59Z",
  "updated_at" : "2017-04-17T23:55:27.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WHhNHoVtmUfZGBvAqwNQ8yP4"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.simonpayments.com/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://api-staging.simonpayments.com/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USggcGLbiN1DzFmqVKz66f9W:de654913-27be-4121-a503-788edeaccc50

```
```php
<?php
use Simon\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHhNHoVtmUfZGBvAqwNQ8yP4",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APFGbQvx9yVjdi79yUu2zCT",
      "created_at" : "2017-04-17T23:55:27.59Z",
      "updated_at" : "2017-04-17T23:55:27.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/webhooks/WHhNHoVtmUfZGBvAqwNQ8yP4"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APFGbQvx9yVjdi79yUu2zCT"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.simonpayments.com/webhooks`
    

## Sample Payloads


```shell
```
```php
<?php
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
