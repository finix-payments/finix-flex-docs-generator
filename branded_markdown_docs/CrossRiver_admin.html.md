---
title: CrossRiver API Reference

language_tabs:
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

4. [Push-to-Card Private [BETA]](#push-to-card-private-beta): This guide walks 
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 
## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USx5onyNMhKqfZkHsbqnwtvV`

- Password: `9f219a08-c7b2-4bbc-b47a-fb22d67f7bec`

- Application ID: `APxyejXYzodptF98WCsnhTWr`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
> Example Response:

```json
{
  "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
  "created_at" : "2016-11-01T22:17:07.71Z",
  "updated_at" : "2016-11-01T22:17:07.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'


```
> Example Response:

```json
{
  "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-01T22:17:13.36Z",
  "updated_at" : "2016-11-01T22:17:13.36Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'
```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : "VIqtbeo6DmYXfuoVkZoBk9DG",
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.12Z",
  "updated_at" : "2016-11-01T22:17:15.12Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqtbeo6DmYXfuoVkZoBk9DG"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
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
> Example Response:

```json
{
  "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Kline",
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
  "created_at" : "2016-11-01T22:17:16.11Z",
  "updated_at" : "2016-11-01T22:17:16.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "name": "Fran Diaz", 
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
	    "identity": "IDbAkawGUaLi8tpeDbdAhQK5"
	}'


```
> Example Response:

```json
{
  "id" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "fingerprint" : "FPR-492142476",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Diaz",
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
  "created_at" : "2016-11-01T22:17:16.76Z",
  "updated_at" : "2016-11-01T22:17:16.76Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/updates"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "merchant_identity": "IDpV9vLomC9EZhHnkAbdcqkN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfX16Y1YYhhaWGCXizLzU5v", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.69Z",
  "updated_at" : "2016-11-01T22:17:22.70Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
curl https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRsCgh57TmNQCtsQiWQxm4g",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.56Z",
  "updated_at" : "2016-11-01T22:17:23.46Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "STepUqw8W3E84vyh2DBhQQ7f",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "currency" : "USD",
  "created_at" : "2016-11-01T22:24:23.63Z",
  "updated_at" : "2016-11-01T22:24:23.64Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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
          applicationId: 'APxyejXYzodptF98WCsnhTWr',
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
  "id" : "TKbQuqHcmDnSPzFrLJwgZUDp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-01T22:17:25.11Z",
  "updated_at" : "2016-11-01T22:17:25.11Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-02T22:17:25.11Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "token": "TKbQuqHcmDnSPzFrLJwgZUDp", 
	    "type": "TOKEN", 
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'


```
> Example Response:

```json
{
  "id" : "PIbQuqHcmDnSPzFrLJwgZUDp",
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
  "created_at" : "2016-11-01T22:17:25.62Z",
  "updated_at" : "2016-11-01T22:17:25.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/updates"
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


## Push-to-Card [PRIVATE BETA]
### Step 1: Register an Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Fran", 
	        "last_name": "Jones", 
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
> Example Response:

```json
{
  "id" : "ID2912ngcbKTnWrCmitJZ8Lq",
  "entity" : {
    "title" : null,
    "first_name" : "Fran",
    "last_name" : "Jones",
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
  "created_at" : "2016-11-01T22:17:32.08Z",
  "updated_at" : "2016-11-01T22:17:32.08Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "name": "Michae Curry", 
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
	    "identity": "ID2912ngcbKTnWrCmitJZ8Lq"
	}'
```
> Example Response:

```json
{
  "id" : "PIeDbL7ChaTzcCbwub4BCC2n",
  "fingerprint" : "FPR1665880360",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Michae Curry",
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
  "created_at" : "2016-11-01T22:17:32.62Z",
  "updated_at" : "2016-11-01T22:17:32.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2912ngcbKTnWrCmitJZ8Lq",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/updates"
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
curl https://api-staging.finix.io/identities/'MU2xHsEfHWNCJ3CALGXPi7jx'/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'
```
> Example Response:

```json
{
  "id" : "TRucdVr9ukCDmg7KaUVrPJzT",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "83173",
  "currency" : "USD",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "source" : "PI3XsxPzsLnfwdtE6xULjsUk",
  "destination" : "PIeDbL7ChaTzcCbwub4BCC2n",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:33.43Z",
  "updated_at" : "2016-11-01T22:17:35.20Z",
  "merchant_identity" : "IDw8gA4byLPTJYeX18ozYU4j",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n"
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


```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID2912ngcbKTnWrCmitJZ8Lq", 
	    "destination": "PIeDbL7ChaTzcCbwub4BCC2n", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
> Example Response:

```json
{
  "id" : "TRucdVr9ukCDmg7KaUVrPJzT",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "83173",
  "currency" : "USD",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "source" : "PI3XsxPzsLnfwdtE6xULjsUk",
  "destination" : "PIeDbL7ChaTzcCbwub4BCC2n",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:33.43Z",
  "updated_at" : "2016-11-01T22:17:35.20Z",
  "merchant_identity" : "IDw8gA4byLPTJYeX18ozYU4j",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n"
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

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
> Example Response:

```json
{
  "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
  "created_at" : "2016-11-01T22:17:07.71Z",
  "updated_at" : "2016-11-01T22:17:07.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'


```
> Example Response:

```json
{
  "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-01T22:17:13.36Z",
  "updated_at" : "2016-11-01T22:17:13.36Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'
```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : "VIqtbeo6DmYXfuoVkZoBk9DG",
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.12Z",
  "updated_at" : "2016-11-01T22:17:15.12Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqtbeo6DmYXfuoVkZoBk9DG"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
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
> Example Response:

```json
{
  "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Kline",
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
  "created_at" : "2016-11-01T22:17:16.11Z",
  "updated_at" : "2016-11-01T22:17:16.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "name": "Fran Diaz", 
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
	    "identity": "IDbAkawGUaLi8tpeDbdAhQK5"
	}'


```
> Example Response:

```json
{
  "id" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "fingerprint" : "FPR-492142476",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Diaz",
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
  "created_at" : "2016-11-01T22:17:16.76Z",
  "updated_at" : "2016-11-01T22:17:16.76Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/updates"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "merchant_identity": "IDpV9vLomC9EZhHnkAbdcqkN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfX16Y1YYhhaWGCXizLzU5v", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.69Z",
  "updated_at" : "2016-11-01T22:17:22.70Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
curl https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRsCgh57TmNQCtsQiWQxm4g",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.56Z",
  "updated_at" : "2016-11-01T22:17:23.46Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "STepUqw8W3E84vyh2DBhQQ7f",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "currency" : "USD",
  "created_at" : "2016-11-01T22:24:23.63Z",
  "updated_at" : "2016-11-01T22:24:23.64Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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
> Example Response:

```json
{
  "id" : "USx5onyNMhKqfZkHsbqnwtvV",
  "password" : "9f219a08-c7b2-4bbc-b47a-fb22d67f7bec",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:04.23Z",
  "updated_at" : "2016-11-01T22:17:04.23Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USx5onyNMhKqfZkHsbqnwtvV"
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
	        "application_name": "WePay"
	    }, 
	    "user": "USx5onyNMhKqfZkHsbqnwtvV", 
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
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-01T22:17:04.74Z",
  "updated_at" : "2016-11-01T22:17:04.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors \
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
> Example Response:

```json
{
  "id" : "PR255KtG35spGj8JvdcAD9f4",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "default_merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "created_at" : "2016-11-01T22:17:05.33Z",
  "updated_at" : "2016-11-01T22:17:05.33Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors/PR255KtG35spGj8JvdcAD9f4"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-11-01T22:17:04.70Z",
  "updated_at" : "2016-11-01T22:24:33.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
```shell
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-01T22:17:04.70Z",
  "updated_at" : "2016-11-01T22:24:34.59Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
    applicationId: "APxyejXYzodptF98WCsnhTWr",
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
  "id" : "TKbQuqHcmDnSPzFrLJwgZUDp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-01T22:17:25.11Z",
  "updated_at" : "2016-11-01T22:17:25.11Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-02T22:17:25.11Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "token": "TKbQuqHcmDnSPzFrLJwgZUDp", 
	    "type": "TOKEN", 
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'

```
> Example Response:

```json
{
  "id" : "PIbQuqHcmDnSPzFrLJwgZUDp",
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
  "created_at" : "2016-11-01T22:17:25.62Z",
  "updated_at" : "2016-11-01T22:17:25.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/updates"
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
```shell
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-11-01T22:17:04.70Z",
  "updated_at" : "2016-11-01T22:17:06.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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


```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "tags": {
	        "application_name": "WePay"
	    }, 
	    "user": "USx5onyNMhKqfZkHsbqnwtvV", 
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
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-01T22:17:04.74Z",
  "updated_at" : "2016-11-01T22:17:04.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
```shell
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-11-01T22:17:04.70Z",
  "updated_at" : "2016-11-01T22:24:30.46Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
```shell
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "APxyejXYzodptF98WCsnhTWr",
  "enabled" : true,
  "tags" : {
    "application_name" : "WePay"
  },
  "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-11-01T22:17:04.70Z",
  "updated_at" : "2016-11-01T22:24:31.73Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USeSW5yPJ1rgqFMuSwa6x2D5",
  "password" : "ae542ee3-2ef0-4bba-b500-372101434d5c",
  "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:05.91Z",
  "updated_at" : "2016-11-01T22:17:05.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USeSW5yPJ1rgqFMuSwa6x2D5"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors \
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
> Example Response:

```json
{
  "id" : "PR255KtG35spGj8JvdcAD9f4",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "default_merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "created_at" : "2016-11-01T22:17:05.33Z",
  "updated_at" : "2016-11-01T22:17:05.33Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors/PR255KtG35spGj8JvdcAD9f4"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APxyejXYzodptF98WCsnhTWr",
      "enabled" : true,
      "tags" : {
        "application_name" : "WePay"
      },
      "owner" : "IDw8gA4byLPTJYeX18ozYU4j",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-11-01T22:17:04.70Z",
      "updated_at" : "2016-11-01T22:17:06.83Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/reversals"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "merchant_identity": "IDpV9vLomC9EZhHnkAbdcqkN", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIfX16Y1YYhhaWGCXizLzU5v", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.69Z",
  "updated_at" : "2016-11-01T22:17:22.70Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.69Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
curl https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRsCgh57TmNQCtsQiWQxm4g",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.56Z",
  "updated_at" : "2016-11-01T22:17:23.46Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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

curl https://api-staging.finix.io/authorizations/AU5HfcMhY78Vz3aMTpLW6p7n \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
> Example Response:

```json
{
  "id" : "AU5HfcMhY78Vz3aMTpLW6p7n",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:26.29Z",
  "updated_at" : "2016-11-01T22:17:27.04Z",
  "trace_id" : "a2181158-7106-4b43-9295-93f354523430",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : true,
  "expires_at" : "2016-11-08T22:17:26.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AU5HfcMhY78Vz3aMTpLW6p7n"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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

curl https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRsCgh57TmNQCtsQiWQxm4g",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:22.56Z",
  "updated_at" : "2016-11-01T22:17:23.46Z",
  "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "is_void" : false,
  "expires_at" : "2016-11-08T22:17:22.56Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU5HfcMhY78Vz3aMTpLW6p7n",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:26.29Z",
      "updated_at" : "2016-11-01T22:17:27.04Z",
      "trace_id" : "a2181158-7106-4b43-9295-93f354523430",
      "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "is_void" : true,
      "expires_at" : "2016-11-08T22:17:26.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AU5HfcMhY78Vz3aMTpLW6p7n"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        }
      }
    }, {
      "id" : "AUq2Z1hBcGtv7cAjGTCRR4k6",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRsCgh57TmNQCtsQiWQxm4g",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:22.56Z",
      "updated_at" : "2016-11-01T22:17:23.46Z",
      "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
      "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "is_void" : false,
      "expires_at" : "2016-11-08T22:17:22.56Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUq2Z1hBcGtv7cAjGTCRR4k6"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
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
> Example Response:

```json
{
  "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Kline",
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
  "created_at" : "2016-11-01T22:17:16.11Z",
  "updated_at" : "2016-11-01T22:17:16.11Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
> Example Response:

```json
{
  "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
  "created_at" : "2016-11-01T22:17:07.71Z",
  "updated_at" : "2016-11-01T22:17:07.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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

curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
  "created_at" : "2016-11-01T22:17:07.66Z",
  "updated_at" : "2016-11-01T22:17:07.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
	        "doing_business_as": "Bobs Burgers", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Bobs Burgers", 
	        "url": "www.BobsBurgers.com", 
	        "business_name": "Bobs Burgers", 
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
> Example Response:

```json
{
  "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Jessie",
    "last_name" : "Diaz",
    "email" : "user@example.org",
    "business_name" : "Bobs Burgers",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Bobs Burgers",
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
    "key" : "value_2"
  },
  "created_at" : "2016-11-01T22:17:07.66Z",
  "updated_at" : "2016-11-01T22:17:42.21Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID2912ngcbKTnWrCmitJZ8Lq",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Jones",
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
      "created_at" : "2016-11-01T22:17:32.03Z",
      "updated_at" : "2016-11-01T22:17:32.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
        "last_name" : "Kline",
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
      "created_at" : "2016-11-01T22:17:16.05Z",
      "updated_at" : "2016-11-01T22:17:16.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdMNVLUBgZNhYrBBK3C7sSH",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-01T22:17:12.77Z",
      "updated_at" : "2016-11-01T22:17:12.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID6BnribBMBHV7V7fgaubH8z",
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
      "created_at" : "2016-11-01T22:17:12.16Z",
      "updated_at" : "2016-11-01T22:17:12.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID3LMtXxUHJ6Qo1fooFXwdP8",
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
      "created_at" : "2016-11-01T22:17:11.61Z",
      "updated_at" : "2016-11-01T22:17:11.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDd55KwqbnPP62s85k3ff6eu",
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
      "created_at" : "2016-11-01T22:17:11.04Z",
      "updated_at" : "2016-11-01T22:17:11.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDwmQPnbBv7Pb1kjBfTAtrxs",
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
      "created_at" : "2016-11-01T22:17:10.52Z",
      "updated_at" : "2016-11-01T22:17:10.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdGcGmxx6hgT2JPhY5xZfmb",
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
      "created_at" : "2016-11-01T22:17:09.98Z",
      "updated_at" : "2016-11-01T22:17:09.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDaUmRe9TLqwMYvu7LMjQzpq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-01T22:17:09.43Z",
      "updated_at" : "2016-11-01T22:17:09.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDkUXf3ndX5TgbUuoyMHyFVf",
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
      "created_at" : "2016-11-01T22:17:08.91Z",
      "updated_at" : "2016-11-01T22:17:08.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID7T9SstRkbZt7QTJJqrL4TD",
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
      "created_at" : "2016-11-01T22:17:08.20Z",
      "updated_at" : "2016-11-01T22:17:08.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
      "created_at" : "2016-11-01T22:17:07.66Z",
      "updated_at" : "2016-11-01T22:17:07.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDw8gA4byLPTJYeX18ozYU4j",
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
      "created_at" : "2016-11-01T22:17:04.70Z",
      "updated_at" : "2016-11-01T22:17:04.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	'

```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : "VIqtbeo6DmYXfuoVkZoBk9DG",
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.12Z",
  "updated_at" : "2016-11-01T22:17:15.12Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIqtbeo6DmYXfuoVkZoBk9DG"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : null,
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.03Z",
  "updated_at" : "2016-11-01T22:17:15.21Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "VI6bfjKXNXsLkK3Fj3yWGXzm",
  "external_trace_id" : "c81a5a05-8a30-4c1a-954a-ad803f841eaf",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-01T22:17:42.97Z",
  "updated_at" : "2016-11-01T22:17:42.99Z",
  "payment_instrument" : null,
  "merchant" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI6bfjKXNXsLkK3Fj3yWGXzm"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'
```
> Example Response:

```json
{
  "id" : "VI6bfjKXNXsLkK3Fj3yWGXzm",
  "external_trace_id" : "c81a5a05-8a30-4c1a-954a-ad803f841eaf",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-01T22:17:42.97Z",
  "updated_at" : "2016-11-01T22:17:42.99Z",
  "payment_instrument" : null,
  "merchant" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI6bfjKXNXsLkK3Fj3yWGXzm"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : null,
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.03Z",
  "updated_at" : "2016-11-01T22:24:29.29Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "MUoxcspupMYhwDncYS3pKzEB",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "verification" : null,
  "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-01T22:17:15.03Z",
  "updated_at" : "2016-11-01T22:24:29.89Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU2xHsEfHWNCJ3CALGXPi7jx",
      "identity" : "ID2912ngcbKTnWrCmitJZ8Lq",
      "verification" : null,
      "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-01T22:17:35.64Z",
      "updated_at" : "2016-11-01T22:17:35.64Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU2xHsEfHWNCJ3CALGXPi7jx"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU2xHsEfHWNCJ3CALGXPi7jx/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "MUoxcspupMYhwDncYS3pKzEB",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "verification" : null,
      "merchant_profile" : "MPm4jXRqEuFxp3o1Dduvta4B",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-01T22:17:15.03Z",
      "updated_at" : "2016-11-01T22:17:15.21Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPm4jXRqEuFxp3o1Dduvta4B"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID2912ngcbKTnWrCmitJZ8Lq",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Jones",
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
      "created_at" : "2016-11-01T22:17:32.03Z",
      "updated_at" : "2016-11-01T22:17:32.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
        "last_name" : "Kline",
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
      "created_at" : "2016-11-01T22:17:16.05Z",
      "updated_at" : "2016-11-01T22:17:16.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdMNVLUBgZNhYrBBK3C7sSH",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-01T22:17:12.77Z",
      "updated_at" : "2016-11-01T22:17:12.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID6BnribBMBHV7V7fgaubH8z",
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
      "created_at" : "2016-11-01T22:17:12.16Z",
      "updated_at" : "2016-11-01T22:17:12.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID3LMtXxUHJ6Qo1fooFXwdP8",
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
      "created_at" : "2016-11-01T22:17:11.61Z",
      "updated_at" : "2016-11-01T22:17:11.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDd55KwqbnPP62s85k3ff6eu",
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
      "created_at" : "2016-11-01T22:17:11.04Z",
      "updated_at" : "2016-11-01T22:17:11.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDwmQPnbBv7Pb1kjBfTAtrxs",
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
      "created_at" : "2016-11-01T22:17:10.52Z",
      "updated_at" : "2016-11-01T22:17:10.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdGcGmxx6hgT2JPhY5xZfmb",
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
      "created_at" : "2016-11-01T22:17:09.98Z",
      "updated_at" : "2016-11-01T22:17:09.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDaUmRe9TLqwMYvu7LMjQzpq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-01T22:17:09.43Z",
      "updated_at" : "2016-11-01T22:17:09.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDkUXf3ndX5TgbUuoyMHyFVf",
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
      "created_at" : "2016-11-01T22:17:08.91Z",
      "updated_at" : "2016-11-01T22:17:08.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID7T9SstRkbZt7QTJJqrL4TD",
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
      "created_at" : "2016-11-01T22:17:08.20Z",
      "updated_at" : "2016-11-01T22:17:08.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
      "created_at" : "2016-11-01T22:17:07.66Z",
      "updated_at" : "2016-11-01T22:17:07.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDw8gA4byLPTJYeX18ozYU4j",
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
      "created_at" : "2016-11-01T22:17:04.70Z",
      "updated_at" : "2016-11-01T22:17:04.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/merchants/MUoxcspupMYhwDncYS3pKzEB/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID2912ngcbKTnWrCmitJZ8Lq",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Jones",
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
      "created_at" : "2016-11-01T22:17:32.03Z",
      "updated_at" : "2016-11-01T22:17:32.03Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDbAkawGUaLi8tpeDbdAhQK5",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
        "last_name" : "Kline",
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
      "created_at" : "2016-11-01T22:17:16.05Z",
      "updated_at" : "2016-11-01T22:17:16.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdMNVLUBgZNhYrBBK3C7sSH",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-11-01T22:17:12.77Z",
      "updated_at" : "2016-11-01T22:17:12.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdMNVLUBgZNhYrBBK3C7sSH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID6BnribBMBHV7V7fgaubH8z",
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
      "created_at" : "2016-11-01T22:17:12.16Z",
      "updated_at" : "2016-11-01T22:17:12.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6BnribBMBHV7V7fgaubH8z/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID3LMtXxUHJ6Qo1fooFXwdP8",
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
      "created_at" : "2016-11-01T22:17:11.61Z",
      "updated_at" : "2016-11-01T22:17:11.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3LMtXxUHJ6Qo1fooFXwdP8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDd55KwqbnPP62s85k3ff6eu",
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
      "created_at" : "2016-11-01T22:17:11.04Z",
      "updated_at" : "2016-11-01T22:17:11.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDd55KwqbnPP62s85k3ff6eu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDwmQPnbBv7Pb1kjBfTAtrxs",
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
      "created_at" : "2016-11-01T22:17:10.52Z",
      "updated_at" : "2016-11-01T22:17:10.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwmQPnbBv7Pb1kjBfTAtrxs/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDdGcGmxx6hgT2JPhY5xZfmb",
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
      "created_at" : "2016-11-01T22:17:09.98Z",
      "updated_at" : "2016-11-01T22:17:09.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdGcGmxx6hgT2JPhY5xZfmb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDaUmRe9TLqwMYvu7LMjQzpq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-11-01T22:17:09.43Z",
      "updated_at" : "2016-11-01T22:17:09.43Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDaUmRe9TLqwMYvu7LMjQzpq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDkUXf3ndX5TgbUuoyMHyFVf",
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
      "created_at" : "2016-11-01T22:17:08.91Z",
      "updated_at" : "2016-11-01T22:17:08.91Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDkUXf3ndX5TgbUuoyMHyFVf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "ID7T9SstRkbZt7QTJJqrL4TD",
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
      "created_at" : "2016-11-01T22:17:08.20Z",
      "updated_at" : "2016-11-01T22:17:08.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7T9SstRkbZt7QTJJqrL4TD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDpV9vLomC9EZhHnkAbdcqkN",
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
      "created_at" : "2016-11-01T22:17:07.66Z",
      "updated_at" : "2016-11-01T22:17:07.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "IDw8gA4byLPTJYeX18ozYU4j",
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
      "created_at" : "2016-11-01T22:17:04.70Z",
      "updated_at" : "2016-11-01T22:17:04.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USwvqeLj31Qj8LrBHhfSYr7D",
  "password" : "14302c6a-7e11-4699-8e87-9ea59af2fbc8",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:19.83Z",
  "updated_at" : "2016-11-01T22:17:19.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USwvqeLj31Qj8LrBHhfSYr7D"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
          applicationId: 'APxyejXYzodptF98WCsnhTWr',
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
  "id" : "TKbQuqHcmDnSPzFrLJwgZUDp",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-01T22:17:25.11Z",
  "updated_at" : "2016-11-01T22:17:25.11Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-02T22:17:25.11Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "token": "TKbQuqHcmDnSPzFrLJwgZUDp", 
	    "type": "TOKEN", 
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'

```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIbQuqHcmDnSPzFrLJwgZUDp",
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
  "created_at" : "2016-11-01T22:17:25.62Z",
  "updated_at" : "2016-11-01T22:17:25.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/updates"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "token": "TKbQuqHcmDnSPzFrLJwgZUDp", 
	    "type": "TOKEN", 
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'


```
> Example Response:

```json
{
  "id" : "PIbQuqHcmDnSPzFrLJwgZUDp",
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
  "created_at" : "2016-11-01T22:17:25.62Z",
  "updated_at" : "2016-11-01T22:17:25.62Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/updates"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "name": "Fran Diaz", 
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
	    "identity": "IDbAkawGUaLi8tpeDbdAhQK5"
	}'


```
> Example Response:

```json
{
  "id" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "fingerprint" : "FPR-492142476",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Fran Diaz",
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
  "created_at" : "2016-11-01T22:17:16.76Z",
  "updated_at" : "2016-11-01T22:17:16.76Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDbAkawGUaLi8tpeDbdAhQK5",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/updates"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
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
	    "identity": "IDpV9vLomC9EZhHnkAbdcqkN"
	}'


```
> Example Response:

```json
{
  "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-01T22:17:13.36Z",
  "updated_at" : "2016-11-01T22:17:13.36Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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


curl https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \

```
> Example Response:

```json
{
  "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-01T22:17:13.27Z",
  "updated_at" : "2016-11-01T22:17:14.35Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-01T22:17:13.27Z",
  "updated_at" : "2016-11-01T22:17:14.35Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIeDbL7ChaTzcCbwub4BCC2n",
      "fingerprint" : "FPR1665880360",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Michae Curry",
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
      "created_at" : "2016-11-01T22:17:32.55Z",
      "updated_at" : "2016-11-01T22:17:32.55Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2912ngcbKTnWrCmitJZ8Lq",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2912ngcbKTnWrCmitJZ8Lq"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n/updates"
        }
      }
    }, {
      "id" : "PI3H5QPxL98GiX9Gx9dRNrjA",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:30.79Z",
      "updated_at" : "2016-11-01T22:17:30.79Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3H5QPxL98GiX9Gx9dRNrjA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3H5QPxL98GiX9Gx9dRNrjA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3H5QPxL98GiX9Gx9dRNrjA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3H5QPxL98GiX9Gx9dRNrjA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIn5bPoW7CrwEbMagJxf96zt",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:30.79Z",
      "updated_at" : "2016-11-01T22:17:30.79Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIn5bPoW7CrwEbMagJxf96zt"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIn5bPoW7CrwEbMagJxf96zt/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIn5bPoW7CrwEbMagJxf96zt/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIn5bPoW7CrwEbMagJxf96zt/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIbcvBM4ELPbLw3mVXNEMMFp",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:30.79Z",
      "updated_at" : "2016-11-01T22:17:30.79Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbcvBM4ELPbLw3mVXNEMMFp"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbcvBM4ELPbLw3mVXNEMMFp/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbcvBM4ELPbLw3mVXNEMMFp/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbcvBM4ELPbLw3mVXNEMMFp/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PI3XsxPzsLnfwdtE6xULjsUk",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:30.79Z",
      "updated_at" : "2016-11-01T22:17:30.79Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIbQuqHcmDnSPzFrLJwgZUDp",
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
      "created_at" : "2016-11-01T22:17:25.50Z",
      "updated_at" : "2016-11-01T22:17:25.50Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIbQuqHcmDnSPzFrLJwgZUDp/updates"
        }
      }
    }, {
      "id" : "PI5dp9LSzdU8XLNcBCfP7DjM",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-01T22:17:17.30Z",
      "updated_at" : "2016-11-01T22:17:17.30Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDbAkawGUaLi8tpeDbdAhQK5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "fingerprint" : "FPR-492142476",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Fran Diaz",
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
      "created_at" : "2016-11-01T22:17:16.69Z",
      "updated_at" : "2016-11-01T22:17:22.70Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDbAkawGUaLi8tpeDbdAhQK5",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDbAkawGUaLi8tpeDbdAhQK5"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v/updates"
        }
      }
    }, {
      "id" : "PI39hJoTyhPNVyWzTT917Xcb",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:15.03Z",
      "updated_at" : "2016-11-01T22:17:15.03Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI39hJoTyhPNVyWzTT917Xcb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI39hJoTyhPNVyWzTT917Xcb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI39hJoTyhPNVyWzTT917Xcb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI39hJoTyhPNVyWzTT917Xcb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PI9q8SbgvRpt4frt9o5UEofk",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:15.03Z",
      "updated_at" : "2016-11-01T22:17:15.03Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9q8SbgvRpt4frt9o5UEofk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9q8SbgvRpt4frt9o5UEofk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9q8SbgvRpt4frt9o5UEofk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9q8SbgvRpt4frt9o5UEofk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIf2frRc22Hbixy1dEYTaP3k",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:15.03Z",
      "updated_at" : "2016-11-01T22:17:15.03Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIkAbBTFLS7UcLp5MynbqDFx",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-01T22:17:13.27Z",
      "updated_at" : "2016-11-01T22:17:14.35Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIhYWpMcrYtC1ckzRFyBxeMt",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:05.27Z",
      "updated_at" : "2016-11-01T22:17:05.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhYWpMcrYtC1ckzRFyBxeMt"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhYWpMcrYtC1ckzRFyBxeMt/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhYWpMcrYtC1ckzRFyBxeMt/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhYWpMcrYtC1ckzRFyBxeMt/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PI5RWAVE5D47WVkfDLb7BbtL",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:05.27Z",
      "updated_at" : "2016-11-01T22:17:05.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PIp5wAWp8ErJN6RR1xxM1eGC",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:05.27Z",
      "updated_at" : "2016-11-01T22:17:05.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp5wAWp8ErJN6RR1xxM1eGC"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp5wAWp8ErJN6RR1xxM1eGC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp5wAWp8ErJN6RR1xxM1eGC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp5wAWp8ErJN6RR1xxM1eGC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "PI4QFCpahHdL9vzUH3W2dPy9",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-01T22:17:05.27Z",
      "updated_at" : "2016-11-01T22:17:05.27Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4QFCpahHdL9vzUH3W2dPy9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4QFCpahHdL9vzUH3W2dPy9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4QFCpahHdL9vzUH3W2dPy9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4QFCpahHdL9vzUH3W2dPy9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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

curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "STepUqw8W3E84vyh2DBhQQ7f",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "currency" : "USD",
  "created_at" : "2016-11-01T22:24:23.63Z",
  "updated_at" : "2016-11-01T22:24:23.64Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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


curl https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \

```
> Example Response:

```json
{
  "id" : "STepUqw8W3E84vyh2DBhQQ7f",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "currency" : "USD",
  "created_at" : "2016-11-01T22:24:23.53Z",
  "updated_at" : "2016-11-01T22:24:24.44Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "destination": "PIkAbBTFLS7UcLp5MynbqDFx"
	}'

```
> Example Response:

```json
{
  "id" : "STepUqw8W3E84vyh2DBhQQ7f",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "currency" : "USD",
  "created_at" : "2016-11-01T22:24:23.53Z",
  "updated_at" : "2016-11-01T22:24:24.44Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 100,
  "total_fees" : 11,
  "total_fee" : 11,
  "net_amount" : 89,
  "destination" : "PIkAbBTFLS7UcLp5MynbqDFx",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STepUqw8W3E84vyh2DBhQQ7f",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "currency" : "USD",
      "created_at" : "2016-11-01T22:24:23.53Z",
      "updated_at" : "2016-11-01T22:24:24.44Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 100,
      "total_fees" : 11,
      "total_fee" : 11,
      "net_amount" : 89,
      "destination" : "PIkAbBTFLS7UcLp5MynbqDFx",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?type=debit"
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
curl https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRt9aG8dFkqGNED6EJN7Doj8",
      "amount" : 89,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "9ba6e110-dcd1-41f5-ab69-2c9ba4c6c481",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIf2frRc22Hbixy1dEYTaP3k",
      "destination" : "PIkAbBTFLS7UcLp5MynbqDFx",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:24:24.23Z",
      "updated_at" : "2016-11-01T22:24:24.60Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRt9aG8dFkqGNED6EJN7Doj8"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRt9aG8dFkqGNED6EJN7Doj8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRt9aG8dFkqGNED6EJN7Doj8/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRt9aG8dFkqGNED6EJN7Doj8/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRt9aG8dFkqGNED6EJN7Doj8/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkAbBTFLS7UcLp5MynbqDFx"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/funding_transfers?offset=0&limit=20&sort=created_at,desc"
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

curl https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRqBwZS9b7aAJtWpseKJfKeE",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "977289db-7b60-4509-b03b-3ac2e421aafc",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIf2frRc22Hbixy1dEYTaP3k",
      "destination" : "PI5RWAVE5D47WVkfDLb7BbtL",
      "ready_to_settle_at" : "2016-11-01T22:23:30.16Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:23:31.37Z",
      "updated_at" : "2016-11-01T22:23:31.84Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqBwZS9b7aAJtWpseKJfKeE"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqBwZS9b7aAJtWpseKJfKeE/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqBwZS9b7aAJtWpseKJfKeE/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqBwZS9b7aAJtWpseKJfKeE/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqBwZS9b7aAJtWpseKJfKeE/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL"
        }
      }
    }, {
      "id" : "TRvH7M4UcLWdSVYXodxSBLTY",
      "amount" : 23914,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "50661961-edf9-4879-9141-b4b6180848a4",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIf2frRc22Hbixy1dEYTaP3k",
      "destination" : "PIp5wAWp8ErJN6RR1xxM1eGC",
      "ready_to_settle_at" : "2016-11-01T22:23:30.16Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:23:30.85Z",
      "updated_at" : "2016-11-01T22:23:31.28Z",
      "merchant_identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRvH7M4UcLWdSVYXodxSBLTY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRvH7M4UcLWdSVYXodxSBLTY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRvH7M4UcLWdSVYXodxSBLTY/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRvH7M4UcLWdSVYXodxSBLTY/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRvH7M4UcLWdSVYXodxSBLTY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIp5wAWp8ErJN6RR1xxM1eGC"
        }
      }
    }, {
      "id" : "TRqNbtfafoRtjSii6vpGsCNW",
      "amount" : 11,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6ee4ddfe-639b-4670-a38e-4cca550ee14f",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIf2frRc22Hbixy1dEYTaP3k",
      "destination" : "PI5RWAVE5D47WVkfDLb7BbtL",
      "ready_to_settle_at" : "2016-11-01T22:23:30.16Z",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:23:30.35Z",
      "updated_at" : "2016-11-01T22:23:30.82Z",
      "merchant_identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqNbtfafoRtjSii6vpGsCNW"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqNbtfafoRtjSii6vpGsCNW/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqNbtfafoRtjSii6vpGsCNW/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqNbtfafoRtjSii6vpGsCNW/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqNbtfafoRtjSii6vpGsCNW/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5RWAVE5D47WVkfDLb7BbtL"
        }
      }
    }, {
      "id" : "TRsCgh57TmNQCtsQiWQxm4g",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
      "ready_to_settle_at" : "2016-11-01T22:23:30.16Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:23.28Z",
      "updated_at" : "2016-11-01T22:18:11.10Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STepUqw8W3E84vyh2DBhQQ7f/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 4
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
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	{
	    "fee": 23925, 
	    "source": "PI5dp9LSzdU8XLNcBCfP7DjM", 
	    "merchant_identity": "IDpV9vLomC9EZhHnkAbdcqkN", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 239247
	}'


```


> Example Response:

```json
{
  "id" : "TR9y2T9bn8GQ49qXykKoasME",
  "amount" : 239247,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "cbb134ed-280a-46f4-a4e0-5b9468acd2b4",
  "currency" : "USD",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "source" : "PI5dp9LSzdU8XLNcBCfP7DjM",
  "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
  "ready_to_settle_at" : null,
  "fee" : 23925,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:18.92Z",
  "updated_at" : "2016-11-01T22:17:18.99Z",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
    }
  }
}
```

A `Transfer` representing a customer payment where funds are obtained from a
bank account (i.e. ACH Debit, eCheck). These specific `Transfers` are
distinguished by their type which return DEBIT.

#### HTTP Request

`POST https://api-staging.finix.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec


```
> Example Response:

```json
{
  "id" : "TRoXp8MBdqYWtZDNgptKdzJc",
  "amount" : 194832,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "21c8e0e7-28a4-40c2-ae1a-8b8224dd489f",
  "currency" : "USD",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
  "ready_to_settle_at" : null,
  "fee" : 19483,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:17.97Z",
  "updated_at" : "2016-11-01T22:17:21.71Z",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
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

curl https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
> Example Response:

```json
{
  "id" : "TRxpuiJmqvA3qhT3z2oqD3i5",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "fe52d963-65a0-4c78-8910-2e7421976bee",
  "currency" : "USD",
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "source" : "PIf2frRc22Hbixy1dEYTaP3k",
  "destination" : "PIfX16Y1YYhhaWGCXizLzU5v",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-01T22:17:21.73Z",
  "updated_at" : "2016-11-01T22:17:21.79Z",
  "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRxpuiJmqvA3qhT3z2oqD3i5"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRxpuiJmqvA3qhT3z2oqD3i5/payment_instruments"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRucdVr9ukCDmg7KaUVrPJzT",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "83173",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PI3XsxPzsLnfwdtE6xULjsUk",
      "destination" : "PIeDbL7ChaTzcCbwub4BCC2n",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:33.24Z",
      "updated_at" : "2016-11-01T22:17:35.20Z",
      "merchant_identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDw8gA4byLPTJYeX18ozYU4j"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRucdVr9ukCDmg7KaUVrPJzT/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3XsxPzsLnfwdtE6xULjsUk"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIeDbL7ChaTzcCbwub4BCC2n"
        }
      }
    }, {
      "id" : "TRsCgh57TmNQCtsQiWQxm4g",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "c2b3ca5e-5003-46c7-90c6-bb3769273f56",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:23.28Z",
      "updated_at" : "2016-11-01T22:17:23.46Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRsCgh57TmNQCtsQiWQxm4g/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        }
      }
    }, {
      "id" : "TRxpuiJmqvA3qhT3z2oqD3i5",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "8ca0ee92-cfda-468c-bb99-06c32683277a",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIf2frRc22Hbixy1dEYTaP3k",
      "destination" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:21.54Z",
      "updated_at" : "2016-11-01T22:17:21.79Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRxpuiJmqvA3qhT3z2oqD3i5"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRxpuiJmqvA3qhT3z2oqD3i5/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
        }
      }
    }, {
      "id" : "TR9y2T9bn8GQ49qXykKoasME",
      "amount" : 239247,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "cbb134ed-280a-46f4-a4e0-5b9468acd2b4",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PI5dp9LSzdU8XLNcBCfP7DjM",
      "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
      "ready_to_settle_at" : null,
      "fee" : 23925,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:18.77Z",
      "updated_at" : "2016-11-01T22:17:18.99Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR9y2T9bn8GQ49qXykKoasME/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5dp9LSzdU8XLNcBCfP7DjM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
        }
      }
    }, {
      "id" : "TRoXp8MBdqYWtZDNgptKdzJc",
      "amount" : 194832,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "21c8e0e7-28a4-40c2-ae1a-8b8224dd489f",
      "currency" : "USD",
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "source" : "PIfX16Y1YYhhaWGCXizLzU5v",
      "destination" : "PIf2frRc22Hbixy1dEYTaP3k",
      "ready_to_settle_at" : null,
      "fee" : 19483,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-01T22:17:17.97Z",
      "updated_at" : "2016-11-01T22:17:21.71Z",
      "merchant_identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRoXp8MBdqYWtZDNgptKdzJc/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfX16Y1YYhhaWGCXizLzU5v"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIf2frRc22Hbixy1dEYTaP3k"
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
curl https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USeSW5yPJ1rgqFMuSwa6x2D5",
  "password" : "ae542ee3-2ef0-4bba-b500-372101434d5c",
  "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:05.91Z",
  "updated_at" : "2016-11-01T22:17:05.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USeSW5yPJ1rgqFMuSwa6x2D5"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/identities/IDpV9vLomC9EZhHnkAbdcqkN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USwvqeLj31Qj8LrBHhfSYr7D",
  "password" : "14302c6a-7e11-4699-8e87-9ea59af2fbc8",
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:19.83Z",
  "updated_at" : "2016-11-01T22:17:19.83Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USwvqeLj31Qj8LrBHhfSYr7D"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/users/TRoXp8MBdqYWtZDNgptKdzJc \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "id" : "USx5onyNMhKqfZkHsbqnwtvV",
  "password" : null,
  "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:04.23Z",
  "updated_at" : "2016-11-01T22:17:04.74Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USx5onyNMhKqfZkHsbqnwtvV"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
curl https://api-staging.finix.io/users/USwvqeLj31Qj8LrBHhfSYr7D \
    -H "Content-Type: application/vnd.json+api" \
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "USwvqeLj31Qj8LrBHhfSYr7D",
  "password" : null,
  "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-01T22:17:19.67Z",
  "updated_at" : "2016-11-01T22:17:20.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USwvqeLj31Qj8LrBHhfSYr7D"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USwvqeLj31Qj8LrBHhfSYr7D",
      "password" : null,
      "identity" : "IDpV9vLomC9EZhHnkAbdcqkN",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-11-01T22:17:19.67Z",
      "updated_at" : "2016-11-01T22:17:21.08Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USwvqeLj31Qj8LrBHhfSYr7D"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "USeSW5yPJ1rgqFMuSwa6x2D5",
      "password" : null,
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-01T22:17:05.85Z",
      "updated_at" : "2016-11-01T22:17:05.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USeSW5yPJ1rgqFMuSwa6x2D5"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
        }
      }
    }, {
      "id" : "USx5onyNMhKqfZkHsbqnwtvV",
      "password" : null,
      "identity" : "IDw8gA4byLPTJYeX18ozYU4j",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-11-01T22:17:04.23Z",
      "updated_at" : "2016-11-01T22:17:04.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USx5onyNMhKqfZkHsbqnwtvV"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
> Example Response:

```json
{
  "id" : "WHnUpwoVyzNPBfTTDXjvsEad",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "created_at" : "2016-11-01T22:17:07.26Z",
  "updated_at" : "2016-11-01T22:17:07.26Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHnUpwoVyzNPBfTTDXjvsEad"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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



curl https://api-staging.finix.io/webhooks/WHnUpwoVyzNPBfTTDXjvsEad \
    -H "Content-Type: application/vnd.json+api" \
    -u USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec


```
> Example Response:

```json
{
  "id" : "WHnUpwoVyzNPBfTTDXjvsEad",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APxyejXYzodptF98WCsnhTWr",
  "created_at" : "2016-11-01T22:17:07.27Z",
  "updated_at" : "2016-11-01T22:17:07.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHnUpwoVyzNPBfTTDXjvsEad"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
    -u  USx5onyNMhKqfZkHsbqnwtvV:9f219a08-c7b2-4bbc-b47a-fb22d67f7bec

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHnUpwoVyzNPBfTTDXjvsEad",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APxyejXYzodptF98WCsnhTWr",
      "created_at" : "2016-11-01T22:17:07.27Z",
      "updated_at" : "2016-11-01T22:17:07.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHnUpwoVyzNPBfTTDXjvsEad"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APxyejXYzodptF98WCsnhTWr"
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
