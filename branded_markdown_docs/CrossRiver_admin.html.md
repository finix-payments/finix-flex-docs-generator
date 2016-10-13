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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US5Dhrc7Huw1wUEVdKyeXgPA`

- Password: `2bf7bec1-13b6-4fa2-a0af-da9622f6f288`

- Application ID: `APnM61tzbMZkQm8p2sG16gXN`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
> Example Response:

```json
{
  "id" : "IDqietesXCGedRHgyuWbLCNp",
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
  "created_at" : "2016-10-12T02:29:18.87Z",
  "updated_at" : "2016-10-12T02:29:18.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'


```
> Example Response:

```json
{
  "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-12T02:29:29.95Z",
  "updated_at" : "2016-10-12T02:29:29.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : "VIkXmkjPpXNZf5BGWFBH7EjU",
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.86Z",
  "updated_at" : "2016-10-12T02:29:32.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIkXmkjPpXNZf5BGWFBH7EjU"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
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
> Example Response:

```json
{
  "id" : "IDdujtL5uQeX235f8dw6xeRR",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
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
  "created_at" : "2016-10-12T02:29:34.31Z",
  "updated_at" : "2016-10-12T02:29:34.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "name": "Collen James", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4242424242424242", 
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
	    "identity": "IDdujtL5uQeX235f8dw6xeRR"
	}'


```
> Example Response:

```json
{
  "id" : "PIkjfszxEcAfECT4wgwKhSwM",
  "fingerprint" : "FPR-1338723162",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Collen James",
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
  "created_at" : "2016-10-12T02:29:35.52Z",
  "updated_at" : "2016-10-12T02:29:35.52Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDdujtL5uQeX235f8dw6xeRR",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/updates"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "merchant_identity": "IDqietesXCGedRHgyuWbLCNp", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIkjfszxEcAfECT4wgwKhSwM", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.42Z",
  "updated_at" : "2016-10-12T02:29:44.43Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahxbnGQfsZBomHwH1DQeRK",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.29Z",
  "updated_at" : "2016-10-12T02:29:45.72Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "STspzY2wR5obj6GHEPpsUyXQ",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "currency" : "USD",
  "created_at" : "2016-10-12T02:37:00.39Z",
  "updated_at" : "2016-10-12T02:37:00.40Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 431685,
  "total_fee" : 43170,
  "net_amount" : 388515,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
          applicationId: 'APnM61tzbMZkQm8p2sG16gXN',
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
  "id" : "TK7u6vTKXaeV6up6arwht7w3",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-12T02:29:48.21Z",
  "updated_at" : "2016-10-12T02:29:48.21Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-13T02:29:48.21Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "token": "TK7u6vTKXaeV6up6arwht7w3", 
	    "type": "TOKEN", 
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'


```
> Example Response:

```json
{
  "id" : "PI7u6vTKXaeV6up6arwht7w3",
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
  "created_at" : "2016-10-12T02:29:49.04Z",
  "updated_at" : "2016-10-12T02:29:49.04Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/updates"
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


## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
> Example Response:

```json
{
  "id" : "IDqietesXCGedRHgyuWbLCNp",
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
  "created_at" : "2016-10-12T02:29:18.87Z",
  "updated_at" : "2016-10-12T02:29:18.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'


```
> Example Response:

```json
{
  "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-12T02:29:29.95Z",
  "updated_at" : "2016-10-12T02:29:29.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : "VIkXmkjPpXNZf5BGWFBH7EjU",
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.86Z",
  "updated_at" : "2016-10-12T02:29:32.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIkXmkjPpXNZf5BGWFBH7EjU"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
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
> Example Response:

```json
{
  "id" : "IDdujtL5uQeX235f8dw6xeRR",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
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
  "created_at" : "2016-10-12T02:29:34.31Z",
  "updated_at" : "2016-10-12T02:29:34.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "name": "Collen James", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4242424242424242", 
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
	    "identity": "IDdujtL5uQeX235f8dw6xeRR"
	}'


```
> Example Response:

```json
{
  "id" : "PIkjfszxEcAfECT4wgwKhSwM",
  "fingerprint" : "FPR-1338723162",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Collen James",
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
  "created_at" : "2016-10-12T02:29:35.52Z",
  "updated_at" : "2016-10-12T02:29:35.52Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDdujtL5uQeX235f8dw6xeRR",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/updates"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "merchant_identity": "IDqietesXCGedRHgyuWbLCNp", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIkjfszxEcAfECT4wgwKhSwM", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.42Z",
  "updated_at" : "2016-10-12T02:29:44.43Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahxbnGQfsZBomHwH1DQeRK",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.29Z",
  "updated_at" : "2016-10-12T02:29:45.72Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "STspzY2wR5obj6GHEPpsUyXQ",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "currency" : "USD",
  "created_at" : "2016-10-12T02:37:00.39Z",
  "updated_at" : "2016-10-12T02:37:00.40Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 431685,
  "total_fee" : 43170,
  "net_amount" : 388515,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
  "id" : "US5Dhrc7Huw1wUEVdKyeXgPA",
  "password" : "2bf7bec1-13b6-4fa2-a0af-da9622f6f288",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:11.37Z",
  "updated_at" : "2016-10-12T02:29:11.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US5Dhrc7Huw1wUEVdKyeXgPA"
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
	        "application_name": "Venmo"
	    }, 
	    "user": "US5Dhrc7Huw1wUEVdKyeXgPA", 
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
	        "doing_business_as": "Venmo", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Venmo", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-12T02:29:12.77Z",
  "updated_at" : "2016-10-12T02:29:12.77Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors \
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
  "id" : "PRtZtUaxLaia1WoVm4mCq8dT",
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "default_merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "created_at" : "2016-10-12T02:29:14.47Z",
  "updated_at" : "2016-10-12T02:29:14.47Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors/PRtZtUaxLaia1WoVm4mCq8dT"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/ \
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
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2016-10-12T02:29:12.69Z",
  "updated_at" : "2016-10-12T02:37:15.38Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/ \
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
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-10-12T02:29:12.69Z",
  "updated_at" : "2016-10-12T02:37:15.91Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
    applicationId: "APnM61tzbMZkQm8p2sG16gXN",
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
  "id" : "TK7u6vTKXaeV6up6arwht7w3",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-12T02:29:48.21Z",
  "updated_at" : "2016-10-12T02:29:48.21Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-13T02:29:48.21Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "token": "TK7u6vTKXaeV6up6arwht7w3", 
	    "type": "TOKEN", 
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'

```
> Example Response:

```json
{
  "id" : "PI7u6vTKXaeV6up6arwht7w3",
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
  "created_at" : "2016-10-12T02:29:49.04Z",
  "updated_at" : "2016-10-12T02:29:49.04Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/updates"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2016-10-12T02:29:12.69Z",
  "updated_at" : "2016-10-12T02:29:17.20Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
	        "application_name": "Venmo"
	    }, 
	    "user": "US5Dhrc7Huw1wUEVdKyeXgPA", 
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
	        "doing_business_as": "Venmo", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Venmo", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-12T02:29:12.77Z",
  "updated_at" : "2016-10-12T02:29:12.77Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/ \
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
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2016-10-12T02:29:12.69Z",
  "updated_at" : "2016-10-12T02:37:12.96Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/ \
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
  "id" : "APnM61tzbMZkQm8p2sG16gXN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Venmo"
  },
  "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2016-10-12T02:29:12.69Z",
  "updated_at" : "2016-10-12T02:37:13.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USjMhAWiobiGB4macvn4hs4T",
  "password" : "f88c931c-5caf-4261-a974-ef77d2a59e90",
  "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:16.22Z",
  "updated_at" : "2016-10-12T02:29:16.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjMhAWiobiGB4macvn4hs4T"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors \
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
  "id" : "PRtZtUaxLaia1WoVm4mCq8dT",
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "default_merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "created_at" : "2016-10-12T02:29:14.47Z",
  "updated_at" : "2016-10-12T02:29:14.47Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "key1" : "value-1",
    "key2" : "value-2"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors/PRtZtUaxLaia1WoVm4mCq8dT"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APnM61tzbMZkQm8p2sG16gXN",
      "enabled" : true,
      "tags" : {
        "application_name" : "Venmo"
      },
      "owner" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2016-10-12T02:29:12.69Z",
      "updated_at" : "2016-10-12T02:29:17.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/reversals"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "merchant_identity": "IDqietesXCGedRHgyuWbLCNp", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIkjfszxEcAfECT4wgwKhSwM", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.42Z",
  "updated_at" : "2016-10-12T02:29:44.43Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.42Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahxbnGQfsZBomHwH1DQeRK",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.29Z",
  "updated_at" : "2016-10-12T02:29:45.72Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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

curl https://api-staging.finix.io/authorizations/AUf3eDuL2nRucfBPmCiTXoqT \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
> Example Response:

```json
{
  "id" : "AUf3eDuL2nRucfBPmCiTXoqT",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:50.44Z",
  "updated_at" : "2016-10-12T02:29:51.63Z",
  "trace_id" : "8b85272f-fb49-4933-ad3b-e04c85f3dce2",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : true,
  "expires_at" : "2016-10-19T02:29:50.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUf3eDuL2nRucfBPmCiTXoqT"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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

curl https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRahxbnGQfsZBomHwH1DQeRK",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:44.29Z",
  "updated_at" : "2016-10-12T02:29:45.72Z",
  "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "is_void" : false,
  "expires_at" : "2016-10-19T02:29:44.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUf3eDuL2nRucfBPmCiTXoqT",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:50.44Z",
      "updated_at" : "2016-10-12T02:30:02.18Z",
      "trace_id" : "8b85272f-fb49-4933-ad3b-e04c85f3dce2",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "is_void" : true,
      "expires_at" : "2016-10-19T02:29:50.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUf3eDuL2nRucfBPmCiTXoqT"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        }
      }
    }, {
      "id" : "AUq97yjgFBbtKFpLuGPn7Xof",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRahxbnGQfsZBomHwH1DQeRK",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:44.29Z",
      "updated_at" : "2016-10-12T02:29:45.72Z",
      "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "is_void" : false,
      "expires_at" : "2016-10-19T02:29:44.29Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/authorizations/AUq97yjgFBbtKFpLuGPn7Xof"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "transfer" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Laura", 
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
> Example Response:

```json
{
  "id" : "IDdujtL5uQeX235f8dw6xeRR",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
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
  "created_at" : "2016-10-12T02:29:34.31Z",
  "updated_at" : "2016-10-12T02:29:34.31Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
> Example Response:

```json
{
  "id" : "IDqietesXCGedRHgyuWbLCNp",
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
  "created_at" : "2016-10-12T02:29:18.87Z",
  "updated_at" : "2016-10-12T02:29:18.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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

curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "id" : "IDqietesXCGedRHgyuWbLCNp",
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
  "created_at" : "2016-10-12T02:29:18.81Z",
  "updated_at" : "2016-10-12T02:29:18.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Marcie", 
	        "last_name": "Serna", 
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
	        "doing_business_as": "Petes Coffee", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Petes Coffee", 
	        "url": "www.PetesCoffee.com", 
	        "business_name": "Petes Coffee", 
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
  "id" : "IDqietesXCGedRHgyuWbLCNp",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Marcie",
    "last_name" : "Serna",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Petes Coffee",
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
    "key" : "value_2"
  },
  "created_at" : "2016-10-12T02:29:18.81Z",
  "updated_at" : "2016-10-12T02:30:17.51Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDthNkZn3hdmrscTd3UGkn4u",
      "entity" : {
        "title" : null,
        "first_name" : "Daphne",
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
      "created_at" : "2016-10-12T02:30:01.11Z",
      "updated_at" : "2016-10-12T02:30:01.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDdujtL5uQeX235f8dw6xeRR",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
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
      "created_at" : "2016-10-12T02:29:34.25Z",
      "updated_at" : "2016-10-12T02:29:34.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDttFmorAkBDy29nvBWwfhc",
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
      "created_at" : "2016-10-12T02:29:29.02Z",
      "updated_at" : "2016-10-12T02:29:29.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8MWUsbzAHFjN2UCb3vBKAA",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:28.11Z",
      "updated_at" : "2016-10-12T02:29:28.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvSxA16mwHdG3zWZB99Ktqw",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:27.16Z",
      "updated_at" : "2016-10-12T02:29:27.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqpR5xVXJEzoBZufpMxQaiQ",
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
      "created_at" : "2016-10-12T02:29:26.27Z",
      "updated_at" : "2016-10-12T02:29:26.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvLSYyaJXnApLhhEWAfH2ra",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:25.05Z",
      "updated_at" : "2016-10-12T02:29:25.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDpVUkg1yfMCbCFn7vbCBz4P",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:23.90Z",
      "updated_at" : "2016-10-12T02:29:23.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDoSTqhZJGDdjDWRuySvgzb",
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
      "created_at" : "2016-10-12T02:29:22.99Z",
      "updated_at" : "2016-10-12T02:29:22.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8q3tvDuPwnffVDsNEcisX8",
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
      "created_at" : "2016-10-12T02:29:21.57Z",
      "updated_at" : "2016-10-12T02:29:21.57Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDmdtHkLjV4TnJ2YCvNpqT4D",
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
      "created_at" : "2016-10-12T02:29:20.40Z",
      "updated_at" : "2016-10-12T02:29:20.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqietesXCGedRHgyuWbLCNp",
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
      "created_at" : "2016-10-12T02:29:18.81Z",
      "updated_at" : "2016-10-12T02:29:18.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDcTwYTXKGtrCtKsdpbPvUx2",
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
      "created_at" : "2016-10-12T02:29:12.69Z",
      "updated_at" : "2016-10-12T02:29:12.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : "VIkXmkjPpXNZf5BGWFBH7EjU",
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.86Z",
  "updated_at" : "2016-10-12T02:29:32.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIkXmkjPpXNZf5BGWFBH7EjU"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : null,
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.76Z",
  "updated_at" : "2016-10-12T02:29:32.98Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "VI3vmaS8A5xA6LRCi24fbsHf",
  "external_trace_id" : "a9c2578a-a87b-430c-986d-ad6052327324",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-12T02:30:18.74Z",
  "updated_at" : "2016-10-12T02:30:18.76Z",
  "payment_instrument" : null,
  "merchant" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI3vmaS8A5xA6LRCi24fbsHf"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'
```
> Example Response:

```json
{
  "id" : "VI3vmaS8A5xA6LRCi24fbsHf",
  "external_trace_id" : "a9c2578a-a87b-430c-986d-ad6052327324",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-10-12T02:30:18.74Z",
  "updated_at" : "2016-10-12T02:30:18.76Z",
  "payment_instrument" : null,
  "merchant" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VI3vmaS8A5xA6LRCi24fbsHf"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/ \
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
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : null,
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.76Z",
  "updated_at" : "2016-10-12T02:37:11.30Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/ \
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
  "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "verification" : null,
  "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-10-12T02:29:32.76Z",
  "updated_at" : "2016-10-12T02:37:11.96Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MU5L2EzWyXNmPpnb2hyXzrg6",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "verification" : null,
      "merchant_profile" : "MP79mtd4Asqzni2AQLfyyakY",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-10-12T02:29:32.76Z",
      "updated_at" : "2016-10-12T02:29:32.98Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MP79mtd4Asqzni2AQLfyyakY"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    "count" : 1
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/merchants/`

## List Merchant Verifications
```shell
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDthNkZn3hdmrscTd3UGkn4u",
      "entity" : {
        "title" : null,
        "first_name" : "Daphne",
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
      "created_at" : "2016-10-12T02:30:01.11Z",
      "updated_at" : "2016-10-12T02:30:01.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDdujtL5uQeX235f8dw6xeRR",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
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
      "created_at" : "2016-10-12T02:29:34.25Z",
      "updated_at" : "2016-10-12T02:29:34.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDttFmorAkBDy29nvBWwfhc",
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
      "created_at" : "2016-10-12T02:29:29.02Z",
      "updated_at" : "2016-10-12T02:29:29.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8MWUsbzAHFjN2UCb3vBKAA",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:28.11Z",
      "updated_at" : "2016-10-12T02:29:28.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvSxA16mwHdG3zWZB99Ktqw",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:27.16Z",
      "updated_at" : "2016-10-12T02:29:27.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqpR5xVXJEzoBZufpMxQaiQ",
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
      "created_at" : "2016-10-12T02:29:26.27Z",
      "updated_at" : "2016-10-12T02:29:26.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvLSYyaJXnApLhhEWAfH2ra",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:25.05Z",
      "updated_at" : "2016-10-12T02:29:25.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDpVUkg1yfMCbCFn7vbCBz4P",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:23.90Z",
      "updated_at" : "2016-10-12T02:29:23.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDoSTqhZJGDdjDWRuySvgzb",
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
      "created_at" : "2016-10-12T02:29:22.99Z",
      "updated_at" : "2016-10-12T02:29:22.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8q3tvDuPwnffVDsNEcisX8",
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
      "created_at" : "2016-10-12T02:29:21.57Z",
      "updated_at" : "2016-10-12T02:29:21.57Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDmdtHkLjV4TnJ2YCvNpqT4D",
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
      "created_at" : "2016-10-12T02:29:20.40Z",
      "updated_at" : "2016-10-12T02:29:20.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqietesXCGedRHgyuWbLCNp",
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
      "created_at" : "2016-10-12T02:29:18.81Z",
      "updated_at" : "2016-10-12T02:29:18.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDcTwYTXKGtrCtKsdpbPvUx2",
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
      "created_at" : "2016-10-12T02:29:12.69Z",
      "updated_at" : "2016-10-12T02:29:12.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/merchants/MU5L2EzWyXNmPpnb2hyXzrg6/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDthNkZn3hdmrscTd3UGkn4u",
      "entity" : {
        "title" : null,
        "first_name" : "Daphne",
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
      "created_at" : "2016-10-12T02:30:01.11Z",
      "updated_at" : "2016-10-12T02:30:01.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDdujtL5uQeX235f8dw6xeRR",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
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
      "created_at" : "2016-10-12T02:29:34.25Z",
      "updated_at" : "2016-10-12T02:29:34.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDttFmorAkBDy29nvBWwfhc",
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
      "created_at" : "2016-10-12T02:29:29.02Z",
      "updated_at" : "2016-10-12T02:29:29.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDttFmorAkBDy29nvBWwfhc/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8MWUsbzAHFjN2UCb3vBKAA",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:28.11Z",
      "updated_at" : "2016-10-12T02:29:28.11Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8MWUsbzAHFjN2UCb3vBKAA/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvSxA16mwHdG3zWZB99Ktqw",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2016-10-12T02:29:27.16Z",
      "updated_at" : "2016-10-12T02:29:27.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvSxA16mwHdG3zWZB99Ktqw/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqpR5xVXJEzoBZufpMxQaiQ",
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
      "created_at" : "2016-10-12T02:29:26.27Z",
      "updated_at" : "2016-10-12T02:29:26.27Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqpR5xVXJEzoBZufpMxQaiQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDvLSYyaJXnApLhhEWAfH2ra",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:25.05Z",
      "updated_at" : "2016-10-12T02:29:25.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvLSYyaJXnApLhhEWAfH2ra/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDpVUkg1yfMCbCFn7vbCBz4P",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-10-12T02:29:23.90Z",
      "updated_at" : "2016-10-12T02:29:23.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpVUkg1yfMCbCFn7vbCBz4P/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDoSTqhZJGDdjDWRuySvgzb",
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
      "created_at" : "2016-10-12T02:29:22.99Z",
      "updated_at" : "2016-10-12T02:29:22.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoSTqhZJGDdjDWRuySvgzb/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "ID8q3tvDuPwnffVDsNEcisX8",
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
      "created_at" : "2016-10-12T02:29:21.57Z",
      "updated_at" : "2016-10-12T02:29:21.57Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8q3tvDuPwnffVDsNEcisX8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDmdtHkLjV4TnJ2YCvNpqT4D",
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
      "created_at" : "2016-10-12T02:29:20.40Z",
      "updated_at" : "2016-10-12T02:29:20.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmdtHkLjV4TnJ2YCvNpqT4D/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDqietesXCGedRHgyuWbLCNp",
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
      "created_at" : "2016-10-12T02:29:18.81Z",
      "updated_at" : "2016-10-12T02:29:18.81Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "IDcTwYTXKGtrCtKsdpbPvUx2",
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
      "created_at" : "2016-10-12T02:29:12.69Z",
      "updated_at" : "2016-10-12T02:29:12.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USbtBGmpGwdYPpTx7aV4iKs",
  "password" : "10a4f702-5113-4050-961c-b58437639af4",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:40.62Z",
  "updated_at" : "2016-10-12T02:29:40.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USbtBGmpGwdYPpTx7aV4iKs"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
          applicationId: 'APnM61tzbMZkQm8p2sG16gXN',
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
  "id" : "TK7u6vTKXaeV6up6arwht7w3",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-10-12T02:29:48.21Z",
  "updated_at" : "2016-10-12T02:29:48.21Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-10-13T02:29:48.21Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "token": "TK7u6vTKXaeV6up6arwht7w3", 
	    "type": "TOKEN", 
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'

```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PI7u6vTKXaeV6up6arwht7w3",
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
  "created_at" : "2016-10-12T02:29:49.04Z",
  "updated_at" : "2016-10-12T02:29:49.04Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/updates"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "token": "TK7u6vTKXaeV6up6arwht7w3", 
	    "type": "TOKEN", 
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'


```
> Example Response:

```json
{
  "id" : "PI7u6vTKXaeV6up6arwht7w3",
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
  "created_at" : "2016-10-12T02:29:49.04Z",
  "updated_at" : "2016-10-12T02:29:49.04Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/updates"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "name": "Collen James", 
	    "expiration_year": 2020, 
	    "tags": {
	        "card name": "Business Card"
	    }, 
	    "number": "4242424242424242", 
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
	    "identity": "IDdujtL5uQeX235f8dw6xeRR"
	}'


```
> Example Response:

```json
{
  "id" : "PIkjfszxEcAfECT4wgwKhSwM",
  "fingerprint" : "FPR-1338723162",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Collen James",
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
  "created_at" : "2016-10-12T02:29:35.52Z",
  "updated_at" : "2016-10-12T02:29:35.52Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDdujtL5uQeX235f8dw6xeRR",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/updates"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
	    "identity": "IDqietesXCGedRHgyuWbLCNp"
	}'


```
> Example Response:

```json
{
  "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-12T02:29:29.95Z",
  "updated_at" : "2016-10-12T02:29:29.95Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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


curl https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \

```
> Example Response:

```json
{
  "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-12T02:29:29.85Z",
  "updated_at" : "2016-10-12T02:29:31.69Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-10-12T02:29:29.85Z",
  "updated_at" : "2016-10-12T02:29:31.69Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIkNgYBksSNoBnPZW3PHCZEP",
      "fingerprint" : "FPR-363220090",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Michae Chang",
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
      "created_at" : "2016-10-12T02:30:01.93Z",
      "updated_at" : "2016-10-12T02:30:01.93Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDthNkZn3hdmrscTd3UGkn4u",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDthNkZn3hdmrscTd3UGkn4u"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP/updates"
        }
      }
    }, {
      "id" : "PI6BTgbHMyQUxmKURaAeJRMB",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:59.34Z",
      "updated_at" : "2016-10-12T02:29:59.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6BTgbHMyQUxmKURaAeJRMB"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6BTgbHMyQUxmKURaAeJRMB/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6BTgbHMyQUxmKURaAeJRMB/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6BTgbHMyQUxmKURaAeJRMB/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIqPSfUcx2tuZKPE9vVYWd7p",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:59.34Z",
      "updated_at" : "2016-10-12T02:29:59.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPSfUcx2tuZKPE9vVYWd7p"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPSfUcx2tuZKPE9vVYWd7p/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPSfUcx2tuZKPE9vVYWd7p/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPSfUcx2tuZKPE9vVYWd7p/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PI8NAAYdDSN18CKm9kYXctV1",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:59.34Z",
      "updated_at" : "2016-10-12T02:29:59.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8NAAYdDSN18CKm9kYXctV1"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8NAAYdDSN18CKm9kYXctV1/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8NAAYdDSN18CKm9kYXctV1/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8NAAYdDSN18CKm9kYXctV1/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIuaMkVEV8kRJ9KS4ZSJfGq9",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:59.34Z",
      "updated_at" : "2016-10-12T02:29:59.34Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuaMkVEV8kRJ9KS4ZSJfGq9"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuaMkVEV8kRJ9KS4ZSJfGq9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuaMkVEV8kRJ9KS4ZSJfGq9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuaMkVEV8kRJ9KS4ZSJfGq9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PI7u6vTKXaeV6up6arwht7w3",
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
      "created_at" : "2016-10-12T02:29:48.91Z",
      "updated_at" : "2016-10-12T02:29:48.91Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7u6vTKXaeV6up6arwht7w3/updates"
        }
      }
    }, {
      "id" : "PIdb5M6SuPeeoNG3fGzzdRNJ",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-12T02:29:36.47Z",
      "updated_at" : "2016-10-12T02:29:36.47Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDdujtL5uQeX235f8dw6xeRR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIkjfszxEcAfECT4wgwKhSwM",
      "fingerprint" : "FPR-1338723162",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Collen James",
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
      "created_at" : "2016-10-12T02:29:35.43Z",
      "updated_at" : "2016-10-12T02:29:44.43Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDdujtL5uQeX235f8dw6xeRR",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDdujtL5uQeX235f8dw6xeRR"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM/updates"
        }
      }
    }, {
      "id" : "PIsT7M4U8eWh56ae7nowmxWp",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:32.76Z",
      "updated_at" : "2016-10-12T02:29:32.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsT7M4U8eWh56ae7nowmxWp"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsT7M4U8eWh56ae7nowmxWp/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsT7M4U8eWh56ae7nowmxWp/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsT7M4U8eWh56ae7nowmxWp/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PInXP1mwyVYgWMQtfQF4eApw",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:32.76Z",
      "updated_at" : "2016-10-12T02:29:32.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInXP1mwyVYgWMQtfQF4eApw"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInXP1mwyVYgWMQtfQF4eApw/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInXP1mwyVYgWMQtfQF4eApw/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInXP1mwyVYgWMQtfQF4eApw/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:32.76Z",
      "updated_at" : "2016-10-12T02:29:32.76Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIfomB1mZx8yDXQ9xCy7qXEW",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-10-12T02:29:29.85Z",
      "updated_at" : "2016-10-12T02:29:31.69Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIadN4gn21A4x5px37TqMeFk",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:14.38Z",
      "updated_at" : "2016-10-12T02:29:14.38Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIadN4gn21A4x5px37TqMeFk"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIadN4gn21A4x5px37TqMeFk/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIadN4gn21A4x5px37TqMeFk/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIadN4gn21A4x5px37TqMeFk/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PI84CHPA4UkVpLxWtFES2xsa",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:14.38Z",
      "updated_at" : "2016-10-12T02:29:14.38Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84CHPA4UkVpLxWtFES2xsa"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84CHPA4UkVpLxWtFES2xsa/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84CHPA4UkVpLxWtFES2xsa/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI84CHPA4UkVpLxWtFES2xsa/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIikLPySjMnqEVV91QNtyUds",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:14.38Z",
      "updated_at" : "2016-10-12T02:29:14.38Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIikLPySjMnqEVV91QNtyUds"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIikLPySjMnqEVV91QNtyUds/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIikLPySjMnqEVV91QNtyUds/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIikLPySjMnqEVV91QNtyUds/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "PIpEPwvJHPiXSgsEtiJLpetA",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-10-12T02:29:14.38Z",
      "updated_at" : "2016-10-12T02:29:14.38Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpEPwvJHPiXSgsEtiJLpetA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpEPwvJHPiXSgsEtiJLpetA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpEPwvJHPiXSgsEtiJLpetA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIpEPwvJHPiXSgsEtiJLpetA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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

curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
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
  "id" : "STspzY2wR5obj6GHEPpsUyXQ",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "currency" : "USD",
  "created_at" : "2016-10-12T02:37:00.39Z",
  "updated_at" : "2016-10-12T02:37:00.40Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 431685,
  "total_fee" : 43170,
  "net_amount" : 388515,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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


curl https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \

```
> Example Response:

```json
{
  "id" : "STspzY2wR5obj6GHEPpsUyXQ",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "currency" : "USD",
  "created_at" : "2016-10-12T02:37:00.28Z",
  "updated_at" : "2016-10-12T02:37:01.52Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 431685,
  "total_fee" : 43170,
  "net_amount" : 388515,
  "destination" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -X PUT \
    -d '
	{
	    "destination": "PIfomB1mZx8yDXQ9xCy7qXEW"
	}'

```
> Example Response:

```json
{
  "id" : "STspzY2wR5obj6GHEPpsUyXQ",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "currency" : "USD",
  "created_at" : "2016-10-12T02:37:00.28Z",
  "updated_at" : "2016-10-12T02:37:01.52Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 431685,
  "total_fee" : 43170,
  "net_amount" : 388515,
  "destination" : "PIfomB1mZx8yDXQ9xCy7qXEW",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STspzY2wR5obj6GHEPpsUyXQ",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "currency" : "USD",
      "created_at" : "2016-10-12T02:37:00.28Z",
      "updated_at" : "2016-10-12T02:37:01.52Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 431685,
      "total_fee" : 43170,
      "net_amount" : 388515,
      "destination" : "PIfomB1mZx8yDXQ9xCy7qXEW",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
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
curl https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRnkCvNVjMj8HRdt8keMh8co",
      "amount" : 89,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "bc634861-9ced-45fb-8bec-d04320068b82",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "destination" : "PIfomB1mZx8yDXQ9xCy7qXEW",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:37:01.26Z",
      "updated_at" : "2016-10-12T02:37:01.68Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRnkCvNVjMj8HRdt8keMh8co"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRnkCvNVjMj8HRdt8keMh8co/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRnkCvNVjMj8HRdt8keMh8co/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRnkCvNVjMj8HRdt8keMh8co/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
        }
      }
    }, {
      "id" : "TRrWwJQbiQ3cQHAhc27W5xMj",
      "amount" : 388426,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "97ee482e-56d3-47de-9730-fcf75e95a89d",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "destination" : "PIfomB1mZx8yDXQ9xCy7qXEW",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:37:01.26Z",
      "updated_at" : "2016-10-12T02:37:01.60Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRrWwJQbiQ3cQHAhc27W5xMj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRrWwJQbiQ3cQHAhc27W5xMj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRrWwJQbiQ3cQHAhc27W5xMj/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRrWwJQbiQ3cQHAhc27W5xMj/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfomB1mZx8yDXQ9xCy7qXEW"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/funding_transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 2
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

curl https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRahxbnGQfsZBomHwH1DQeRK",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "ready_to_settle_at" : "2016-10-12T02:31:09.26Z",
      "fee" : 10,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:45.44Z",
      "updated_at" : "2016-10-12T02:30:08.24Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        }
      }
    }, {
      "id" : "TR4DaWNVD1kB27z6K8bpAUYx",
      "amount" : 431585,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "e8060214-32bc-4948-b0e6-cd6f640273d5",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "ready_to_settle_at" : "2016-10-12T02:31:09.26Z",
      "fee" : 43159,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:37.79Z",
      "updated_at" : "2016-10-12T02:30:05.07Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/settlements/STspzY2wR5obj6GHEPpsUyXQ/transfers?offset=0&limit=20&sort=created_at,desc"
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
## Debit a Bank Account (ie eCheck) 

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	{
	    "fee": 9803, 
	    "source": "PIdb5M6SuPeeoNG3fGzzdRNJ", 
	    "merchant_identity": "IDqietesXCGedRHgyuWbLCNp", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 98027
	}'


```


> Example Response:

```json
{
  "id" : "TRrbV8WcghyZTnqKxjK8XSo9",
  "amount" : 98027,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "283846d0-bba8-486e-bc20-45d68571013c",
  "currency" : "USD",
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "source" : "PIdb5M6SuPeeoNG3fGzzdRNJ",
  "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
  "ready_to_settle_at" : null,
  "fee" : 9803,
  "statement_descriptor" : "FNX*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:39.46Z",
  "updated_at" : "2016-10-12T02:29:39.58Z",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
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

curl https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288


```
> Example Response:

```json
{
  "id" : "TR4DaWNVD1kB27z6K8bpAUYx",
  "amount" : 431585,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "e8060214-32bc-4948-b0e6-cd6f640273d5",
  "currency" : "USD",
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "source" : "PIkjfszxEcAfECT4wgwKhSwM",
  "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
  "ready_to_settle_at" : null,
  "fee" : 43159,
  "statement_descriptor" : "FNX*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:37.79Z",
  "updated_at" : "2016-10-12T02:29:38.05Z",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/reversals"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
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

curl https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
> Example Response:

```json
{
  "id" : "TRbjNLVpSVUNLXVPdBQ9yttj",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "7939f18a-7ba7-4bcb-beaf-d5eaf5bc2870",
  "currency" : "USD",
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "source" : "PI8eoiEDix8JVJ1p5o3aCTAv",
  "destination" : "PIkjfszxEcAfECT4wgwKhSwM",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*POLLOS HERMANOS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-10-12T02:29:42.99Z",
  "updated_at" : "2016-10-12T02:29:43.10Z",
  "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRbjNLVpSVUNLXVPdBQ9yttj"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRbjNLVpSVUNLXVPdBQ9yttj/payment_instruments"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR5PS2HkQpnVgthCmkjKdWXo",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "FAILED",
      "trace_id" : "1208",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIuaMkVEV8kRJ9KS4ZSJfGq9",
      "destination" : "PIkNgYBksSNoBnPZW3PHCZEP",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:30:04.05Z",
      "updated_at" : "2016-10-12T02:30:05.14Z",
      "merchant_identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PS2HkQpnVgthCmkjKdWXo"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PS2HkQpnVgthCmkjKdWXo/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDcTwYTXKGtrCtKsdpbPvUx2"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PS2HkQpnVgthCmkjKdWXo/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR5PS2HkQpnVgthCmkjKdWXo/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIuaMkVEV8kRJ9KS4ZSJfGq9"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkNgYBksSNoBnPZW3PHCZEP"
        }
      }
    }, {
      "id" : "TRahxbnGQfsZBomHwH1DQeRK",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "1bf2c4ad-aaaf-4d62-9de9-3eb33204f6b8",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:45.44Z",
      "updated_at" : "2016-10-12T02:30:08.24Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRahxbnGQfsZBomHwH1DQeRK/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        }
      }
    }, {
      "id" : "TRbjNLVpSVUNLXVPdBQ9yttj",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "7939f18a-7ba7-4bcb-beaf-d5eaf5bc2870",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "destination" : "PIkjfszxEcAfECT4wgwKhSwM",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:42.82Z",
      "updated_at" : "2016-10-12T02:30:04.39Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRbjNLVpSVUNLXVPdBQ9yttj"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRbjNLVpSVUNLXVPdBQ9yttj/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        }
      }
    }, {
      "id" : "TRrbV8WcghyZTnqKxjK8XSo9",
      "amount" : 98027,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "283846d0-bba8-486e-bc20-45d68571013c",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIdb5M6SuPeeoNG3fGzzdRNJ",
      "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "ready_to_settle_at" : null,
      "fee" : 9803,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:39.32Z",
      "updated_at" : "2016-10-12T02:30:04.76Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRrbV8WcghyZTnqKxjK8XSo9/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdb5M6SuPeeoNG3fGzzdRNJ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
        }
      }
    }, {
      "id" : "TR4DaWNVD1kB27z6K8bpAUYx",
      "amount" : 431585,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "e8060214-32bc-4948-b0e6-cd6f640273d5",
      "currency" : "USD",
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "source" : "PIkjfszxEcAfECT4wgwKhSwM",
      "destination" : "PI8eoiEDix8JVJ1p5o3aCTAv",
      "ready_to_settle_at" : null,
      "fee" : 43159,
      "statement_descriptor" : "FNX*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-10-12T02:29:37.79Z",
      "updated_at" : "2016-10-12T02:30:05.07Z",
      "merchant_identity" : "IDqietesXCGedRHgyuWbLCNp",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/reversals"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR4DaWNVD1kB27z6K8bpAUYx/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkjfszxEcAfECT4wgwKhSwM"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI8eoiEDix8JVJ1p5o3aCTAv"
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
curl https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USjMhAWiobiGB4macvn4hs4T",
  "password" : "f88c931c-5caf-4261-a974-ef77d2a59e90",
  "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:16.22Z",
  "updated_at" : "2016-10-12T02:29:16.22Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjMhAWiobiGB4macvn4hs4T"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/identities/IDqietesXCGedRHgyuWbLCNp/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USbtBGmpGwdYPpTx7aV4iKs",
  "password" : "10a4f702-5113-4050-961c-b58437639af4",
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:40.62Z",
  "updated_at" : "2016-10-12T02:29:40.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USbtBGmpGwdYPpTx7aV4iKs"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/users/TR4DaWNVD1kB27z6K8bpAUYx \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
> Example Response:

```json
{
  "id" : "US5Dhrc7Huw1wUEVdKyeXgPA",
  "password" : null,
  "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:11.31Z",
  "updated_at" : "2016-10-12T02:29:12.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US5Dhrc7Huw1wUEVdKyeXgPA"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
curl https://api-staging.finix.io/users/USbtBGmpGwdYPpTx7aV4iKs \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "USbtBGmpGwdYPpTx7aV4iKs",
  "password" : null,
  "identity" : "IDqietesXCGedRHgyuWbLCNp",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-10-12T02:29:40.52Z",
  "updated_at" : "2016-10-12T02:29:41.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USbtBGmpGwdYPpTx7aV4iKs"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "USbtBGmpGwdYPpTx7aV4iKs",
      "password" : null,
      "identity" : "IDqietesXCGedRHgyuWbLCNp",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2016-10-12T02:29:40.52Z",
      "updated_at" : "2016-10-12T02:29:41.99Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USbtBGmpGwdYPpTx7aV4iKs"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "USjMhAWiobiGB4macvn4hs4T",
      "password" : null,
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-10-12T02:29:16.14Z",
      "updated_at" : "2016-10-12T02:29:16.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USjMhAWiobiGB4macvn4hs4T"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
        }
      }
    }, {
      "id" : "US5Dhrc7Huw1wUEVdKyeXgPA",
      "password" : null,
      "identity" : "IDcTwYTXKGtrCtKsdpbPvUx2",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2016-10-12T02:29:11.31Z",
      "updated_at" : "2016-10-12T02:29:12.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US5Dhrc7Huw1wUEVdKyeXgPA"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288 \
    -d '
	            {
	            "url" : "http://requestb.in/1jb5zu11"
	            }
	        '

```
> Example Response:

```json
{
  "id" : "WHsdPBfeZu3vhQJtMz4x9w5T",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "created_at" : "2016-10-12T02:29:18.09Z",
  "updated_at" : "2016-10-12T02:29:18.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHsdPBfeZu3vhQJtMz4x9w5T"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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



curl https://api-staging.finix.io/webhooks/WHsdPBfeZu3vhQJtMz4x9w5T \
    -H "Content-Type: application/vnd.json+api" \
    -u US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288


```
> Example Response:

```json
{
  "id" : "WHsdPBfeZu3vhQJtMz4x9w5T",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APnM61tzbMZkQm8p2sG16gXN",
  "created_at" : "2016-10-12T02:29:18.09Z",
  "updated_at" : "2016-10-12T02:29:18.09Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHsdPBfeZu3vhQJtMz4x9w5T"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
    -u  US5Dhrc7Huw1wUEVdKyeXgPA:2bf7bec1-13b6-4fa2-a0af-da9622f6f288

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHsdPBfeZu3vhQJtMz4x9w5T",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APnM61tzbMZkQm8p2sG16gXN",
      "created_at" : "2016-10-12T02:29:18.09Z",
      "updated_at" : "2016-10-12T02:29:18.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHsdPBfeZu3vhQJtMz4x9w5T"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APnM61tzbMZkQm8p2sG16gXN"
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
