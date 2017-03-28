---
title: SimonPayments API Reference

language_tabs:
- shell: cURL



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

curl https://api-staging.simonpayments.com/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
To communicate with the SimonPayments API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USdfmiYeT2zJARHvt91o98kN`

- Password: `aedaece9-f759-40dc-96f6-b641850f67f0`

- Application ID: `APpQYhFe2yxLyWvGb9cYprtY`

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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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
> Example Response:

```json
{
  "id" : "IDisW8wNJg3RvTDW3ieUGfJF",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
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
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-27T18:01:36.68Z",
  "updated_at" : "2017-03-27T18:01:36.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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

Let's start with the first step by creating an `Identity` resource. Each `Identity`
 represents either a `buyer` or a `merchant`. We use this resource to associate
 cards, bank accounts, and transactions. This structure makes it simple to
 manage and reconcile a merchant's associated bank accounts, transaction
 history, and payouts. Additionally, for merchants, the `Identity` resource is
 used to collect underwriting information for the business and its principal.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://api-staging.simonpayments.com/identities`

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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
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
	    "identity": "IDisW8wNJg3RvTDW3ieUGfJF"
	}'


```
> Example Response:

```json
{
  "id" : "PIsS69gq37muRhZwjbn5mzAg",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-27T18:01:40.87Z",
  "updated_at" : "2017-03-27T18:01:40.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
name | *string*, **optional** | Account owner's full name
### Step 3: Provision Merchant Account

```shell
curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
> Example Response:

```json
{
  "id" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "verification" : "VIsSjneM9AMGTveAAFuqm3nW",
  "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-27T18:01:41.86Z",
  "updated_at" : "2017-03-27T18:01:41.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIsSjneM9AMGTveAAFuqm3nW"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
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
  "id" : "IDosACaSXULGm37EAP7cNyjM",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
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
  "created_at" : "2017-03-27T18:01:42.76Z",
  "updated_at" : "2017-03-27T18:01:42.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
line1 | *string*, **required** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **required** | City
region | *string*, **required** | State
postal_code | *string*, **required** | Zip or Postal code
country | *string*, **required** | 3-Letter Country code

### Step 5: Tokenize a Card
```shell


curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "name": "Step Lopez", 
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
	    "identity": "IDosACaSXULGm37EAP7cNyjM"
	}'


```
> Example Response:

```json
{
  "id" : "PI8jksL2cPtP2RLn1udjWzw9",
  "fingerprint" : "FPR-2142146072",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Lopez",
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
  "created_at" : "2017-03-27T18:01:43.16Z",
  "updated_at" : "2017-03-27T18:01:43.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDosACaSXULGm37EAP7cNyjM",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/updates"
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
line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code
### Step 6: Create an Authorization
```shell
curl https://api-staging.simonpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "merchant_identity": "IDisW8wNJg3RvTDW3ieUGfJF", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI8jksL2cPtP2RLn1udjWzw9", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:49.24Z",
  "updated_at" : "2017-03-27T18:01:49.29Z",
  "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : false,
  "expires_at" : "2017-04-03T18:01:49.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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
curl https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
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
  "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR4F9Gqgnk8SJyaDgFG2S1xU",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:49.17Z",
  "updated_at" : "2017-03-27T18:01:49.89Z",
  "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : false,
  "expires_at" : "2017-04-03T18:01:49.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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
<script type="text/javascript" src="https://js.paymentsfnx.com/simon-payments/tokenize.js"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: 'APpQYhFe2yxLyWvGb9cYprtY',
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
  "id" : "TKgzk8ba3AQVY9dF1MfgMt8v",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-27T18:01:50.94Z",
  "updated_at" : "2017-03-27T18:01:50.94Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-28T18:01:50.94Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "token": "TKgzk8ba3AQVY9dF1MfgMt8v", 
	    "type": "TOKEN", 
	    "identity": "IDisW8wNJg3RvTDW3ieUGfJF"
	}'


```
> Example Response:

```json
{
  "id" : "PIgzk8ba3AQVY9dF1MfgMt8v",
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
  "created_at" : "2017-03-27T18:01:51.34Z",
  "updated_at" : "2017-03-27T18:01:51.34Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/updates"
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
> Example Response:

```json
{
  "id" : "USdfmiYeT2zJARHvt91o98kN",
  "password" : "aedaece9-f759-40dc-96f6-b641850f67f0",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:33.54Z",
  "updated_at" : "2017-03-27T18:01:33.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USdfmiYeT2zJARHvt91o98kN"
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
	        "application_name": "Google"
	    }, 
	    "user": "USdfmiYeT2zJARHvt91o98kN", 
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
	        "doing_business_as": "Google", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Google", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T18:01:33.87Z",
  "updated_at" : "2017-03-27T18:01:33.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (If business type is INDIVIDUAL_SOLE_PROPRIETORSHIP, please input 100) 
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors \
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
> Example Response:

```json
{
  "id" : "PR8fp3fwUgnCdis9oD7NRu2s",
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "default_merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "created_at" : "2017-03-27T18:01:34.49Z",
  "updated_at" : "2017-03-27T18:01:34.49Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors/PR8fp3fwUgnCdis9oD7NRu2s"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T18:01:33.86Z",
  "updated_at" : "2017-03-27T18:02:03.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T18:01:33.86Z",
  "updated_at" : "2017-03-27T18:02:04.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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

## Tokenization.js

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to SimonPayments.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/sab76Lne/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the SimonPayments API.
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
where you're hosting your form. Please include the script tag as demonstrated
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
    server: "https://api-staging.simonpayments.com",
    applicationId: "APpQYhFe2yxLyWvGb9cYprtY",
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
server | *string*, **required** |  The base url for the SimonPayments API
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
  "id" : "TKgzk8ba3AQVY9dF1MfgMt8v",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-27T18:01:50.94Z",
  "updated_at" : "2017-03-27T18:01:50.94Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-28T18:01:50.94Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "token": "TKgzk8ba3AQVY9dF1MfgMt8v", 
	    "type": "TOKEN", 
	    "identity": "IDisW8wNJg3RvTDW3ieUGfJF"
	}'

```
> Example Response:

```json
{
  "id" : "PIgzk8ba3AQVY9dF1MfgMt8v",
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
  "created_at" : "2017-03-27T18:01:51.34Z",
  "updated_at" : "2017-03-27T18:01:51.34Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/updates"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T18:01:33.86Z",
  "updated_at" : "2017-03-27T18:01:35.86Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
	        "application_name": "Google"
	    }, 
	    "user": "USdfmiYeT2zJARHvt91o98kN", 
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
	        "doing_business_as": "Google", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Google", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T18:01:33.87Z",
  "updated_at" : "2017-03-27T18:01:33.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T18:01:33.86Z",
  "updated_at" : "2017-03-27T18:02:02.53Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "APpQYhFe2yxLyWvGb9cYprtY",
  "enabled" : true,
  "tags" : {
    "application_name" : "Google"
  },
  "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T18:01:33.86Z",
  "updated_at" : "2017-03-27T18:02:02.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "processors" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
    },
    "users" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USkt2SSmL9hUmzz4ETgTvATE",
  "password" : "64ead5ec-8e2d-4048-a9ab-b0da17c201bb",
  "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:34.92Z",
  "updated_at" : "2017-03-27T18:01:34.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USkt2SSmL9hUmzz4ETgTvATE"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors \
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
> Example Response:

```json
{
  "id" : "PR8fp3fwUgnCdis9oD7NRu2s",
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "default_merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "created_at" : "2017-03-27T18:01:34.49Z",
  "updated_at" : "2017-03-27T18:01:34.49Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors/PR8fp3fwUgnCdis9oD7NRu2s"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APpQYhFe2yxLyWvGb9cYprtY",
      "enabled" : true,
      "tags" : {
        "application_name" : "Google"
      },
      "owner" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-03-27T18:01:33.86Z",
      "updated_at" : "2017-03-27T18:01:35.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "processors" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/processors"
        },
        "users" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/application_profile"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "merchant_identity": "IDisW8wNJg3RvTDW3ieUGfJF", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PI8jksL2cPtP2RLn1udjWzw9", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:49.24Z",
  "updated_at" : "2017-03-27T18:01:49.29Z",
  "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : false,
  "expires_at" : "2017-04-03T18:01:49.24Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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
curl https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
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
  "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR4F9Gqgnk8SJyaDgFG2S1xU",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:49.17Z",
  "updated_at" : "2017-03-27T18:01:49.89Z",
  "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : false,
  "expires_at" : "2017-04-03T18:01:49.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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

curl https://api-staging.simonpayments.com/authorizations/AUVGS4hgTwWWrbqj1oLnF4a \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
> Example Response:

```json
{
  "id" : "AUVGS4hgTwWWrbqj1oLnF4a",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:52.00Z",
  "updated_at" : "2017-03-27T18:01:52.81Z",
  "trace_id" : "75034a3d-82df-4c93-b48a-dadd7001da79",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : true,
  "expires_at" : "2017-04-03T18:01:52.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AUVGS4hgTwWWrbqj1oLnF4a"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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

curl https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TR4F9Gqgnk8SJyaDgFG2S1xU",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:49.17Z",
  "updated_at" : "2017-03-27T18:01:49.89Z",
  "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "is_void" : false,
  "expires_at" : "2017-04-03T18:01:49.17Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "transfer" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUVGS4hgTwWWrbqj1oLnF4a",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:52.00Z",
      "updated_at" : "2017-03-27T18:01:52.81Z",
      "trace_id" : "75034a3d-82df-4c93-b48a-dadd7001da79",
      "source" : "PI8jksL2cPtP2RLn1udjWzw9",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "is_void" : true,
      "expires_at" : "2017-04-03T18:01:52.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AUVGS4hgTwWWrbqj1oLnF4a"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        }
      }
    }, {
      "id" : "AU6JsxuNoFPuAKpqGti6jkw1",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TR4F9Gqgnk8SJyaDgFG2S1xU",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:49.17Z",
      "updated_at" : "2017-03-27T18:01:49.89Z",
      "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
      "source" : "PI8jksL2cPtP2RLn1udjWzw9",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "is_void" : false,
      "expires_at" : "2017-04-03T18:01:49.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/authorizations/AU6JsxuNoFPuAKpqGti6jkw1"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "transfer" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
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

An `Identity` resource represents either a buyer or a merchant and is in many
ways the centerpiece of the payment API's architecture. `Transfers` and
`Payment Instruments` must be associated with an `Identity`. For both buyers
and merchants this structure makes it easy to manage and reconcile their
associated bank accounts, transaction history, and payouts.

For merchants, the `Identity` resource is used to collect underwriting
information for the business and its principal.

## Create an Identity for a Buyer


```shell


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Bob", 
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
  "id" : "IDosACaSXULGm37EAP7cNyjM",
  "entity" : {
    "title" : null,
    "first_name" : "Bob",
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
  "created_at" : "2017-03-27T18:01:42.76Z",
  "updated_at" : "2017-03-27T18:01:42.76Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
line1 | *string*, **optional** | Street address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Postal code
country | *string*, **optional** | Country
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Create an Identity for a Merchant
```shell


curl https://api-staging.simonpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
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
	        "ownership_type": "PRIVATE", 
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
> Example Response:

```json
{
  "id" : "IDisW8wNJg3RvTDW3ieUGfJF",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
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
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-27T18:01:36.68Z",
  "updated_at" : "2017-03-27T18:01:36.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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

`POST https://api-staging.simonpayments.com/identities`

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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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

curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "id" : "IDisW8wNJg3RvTDW3ieUGfJF",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
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
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-27T18:01:36.66Z",
  "updated_at" : "2017-03-27T18:01:36.66Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "James", 
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
> Example Response:

```json
{
  "id" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "James",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
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
    "key" : "value_2"
  },
  "created_at" : "2017-03-27T18:01:36.66Z",
  "updated_at" : "2017-03-27T18:02:01.03Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/disputes"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
url | *string*, **required** | Merchant's publicly available website
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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
curl https://api-staging.simonpayments.com/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDosACaSXULGm37EAP7cNyjM",
      "entity" : {
        "title" : null,
        "first_name" : "Bob",
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
      "created_at" : "2017-03-27T18:01:42.75Z",
      "updated_at" : "2017-03-27T18:01:42.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDh425TBqpUwTvydxxvetsjt",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "ACME Anchors"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:40.48Z",
      "updated_at" : "2017-03-27T18:01:40.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDh425TBqpUwTvydxxvetsjt/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDjBZiNe4SZHSick5PAd2w2K",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:40.10Z",
      "updated_at" : "2017-03-27T18:01:40.10Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDjBZiNe4SZHSick5PAd2w2K/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDfpMAU8JRi1AZtkuNbG7u26",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:39.61Z",
      "updated_at" : "2017-03-27T18:01:39.61Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDfpMAU8JRi1AZtkuNbG7u26/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDpidFfKmYwddfFFPqkdPE3b",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Dunder Mifflin"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:39.21Z",
      "updated_at" : "2017-03-27T18:01:39.21Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDpidFfKmYwddfFFPqkdPE3b/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDiYnhfkFsV5G44nStBhCtU6",
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
      "created_at" : "2017-03-27T18:01:38.80Z",
      "updated_at" : "2017-03-27T18:01:38.80Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDiYnhfkFsV5G44nStBhCtU6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "ID7Vug3GRudZXN8ZigGHN1KL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2017-03-27T18:01:38.41Z",
      "updated_at" : "2017-03-27T18:01:38.41Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID7Vug3GRudZXN8ZigGHN1KL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "ID2gvYBfzZJTt2o6Fe4AqMt5",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
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
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:38.02Z",
      "updated_at" : "2017-03-27T18:01:38.02Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2gvYBfzZJTt2o6Fe4AqMt5/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "ID6DMdxj6wyN3NZWY9LRtMPY",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2017-03-27T18:01:37.64Z",
      "updated_at" : "2017-03-27T18:01:37.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID6DMdxj6wyN3NZWY9LRtMPY/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDsiXXmjbtyCWvheAc2cNxaU",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "CORPORATION",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
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
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:37.07Z",
      "updated_at" : "2017-03-27T18:01:37.07Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDsiXXmjbtyCWvheAc2cNxaU/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "IDisW8wNJg3RvTDW3ieUGfJF",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
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
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T18:01:36.66Z",
      "updated_at" : "2017-03-27T18:01:36.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Google",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "Google",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
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
        "application_name" : "Google"
      },
      "created_at" : "2017-03-27T18:01:33.86Z",
      "updated_at" : "2017-03-27T18:01:33.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    "count" : 12
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
curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
> Example Response:

```json
{
  "id" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "verification" : "VIsSjneM9AMGTveAAFuqm3nW",
  "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-27T18:01:41.86Z",
  "updated_at" : "2017-03-27T18:01:41.86Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "verification" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VIsSjneM9AMGTveAAFuqm3nW"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "id" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "verification" : null,
  "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-03-27T18:01:41.82Z",
  "updated_at" : "2017-03-27T18:01:41.97Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "VI4dasngH9e8duH8TqJ7AfBU",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-27T18:02:01.54Z",
  "updated_at" : "2017-03-27T18:02:01.56Z",
  "trace_id" : "af094320-504c-4009-8bde-f0049425cef9",
  "payment_instrument" : null,
  "merchant" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VI4dasngH9e8duH8TqJ7AfBU"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'
```
> Example Response:

```json
{
  "id" : "VI4dasngH9e8duH8TqJ7AfBU",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-03-27T18:02:01.54Z",
  "updated_at" : "2017-03-27T18:02:01.56Z",
  "trace_id" : "af094320-504c-4009-8bde-f0049425cef9",
  "payment_instrument" : null,
  "merchant" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/verifications/VI4dasngH9e8duH8TqJ7AfBU"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "merchant" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "verification" : null,
  "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-03-27T18:01:41.82Z",
  "updated_at" : "2017-03-27T18:02:01.92Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "MUUZQLfRS84rwWr95DrUx9C",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "verification" : null,
  "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-27T18:01:41.82Z",
  "updated_at" : "2017-03-27T18:02:02.24Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUUZQLfRS84rwWr95DrUx9C",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "verification" : null,
      "merchant_profile" : "MP9bp5i4W55mFRvZUaY4gaQB",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:41.97Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.simonpayments.com/merchant_profiles/MP9bp5i4W55mFRvZUaY4gaQB"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIsSjneM9AMGTveAAFuqm3nW",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:42.02Z",
      "trace_id" : "42f85fc5-6e4c-45b5-bcc3-2a251ef98dfa",
      "payment_instrument" : null,
      "merchant" : "MUUZQLfRS84rwWr95DrUx9C",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/verifications/VIsSjneM9AMGTveAAFuqm3nW"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "merchant" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIsSjneM9AMGTveAAFuqm3nW",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:42.02Z",
      "trace_id" : "42f85fc5-6e4c-45b5-bcc3-2a251ef98dfa",
      "payment_instrument" : null,
      "merchant" : "MUUZQLfRS84rwWr95DrUx9C",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/verifications/VIsSjneM9AMGTveAAFuqm3nW"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "merchant" : {
          "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/merchants/MUUZQLfRS84rwWr95DrUx9C/verifications?offset=0&limit=20&sort=created_at,desc"
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
curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "US9YGjjDeS6pzD1tnEpc33Hk",
  "password" : "f603b4c7-971d-440b-9e8f-f45e3ebb0c20",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:45.23Z",
  "updated_at" : "2017-03-27T18:01:45.23Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/US9YGjjDeS6pzD1tnEpc33Hk"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "token": "TKgzk8ba3AQVY9dF1MfgMt8v", 
	    "type": "TOKEN", 
	    "identity": "IDisW8wNJg3RvTDW3ieUGfJF"
	}'


```
> Example Response:

```json
{
  "id" : "PIgzk8ba3AQVY9dF1MfgMt8v",
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
  "created_at" : "2017-03-27T18:01:51.34Z",
  "updated_at" : "2017-03-27T18:01:51.34Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/updates"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
	{
	    "name": "Step Lopez", 
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
	    "identity": "IDosACaSXULGm37EAP7cNyjM"
	}'


```
> Example Response:

```json
{
  "id" : "PI8jksL2cPtP2RLn1udjWzw9",
  "fingerprint" : "FPR-2142146072",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Lopez",
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
  "created_at" : "2017-03-27T18:01:43.16Z",
  "updated_at" : "2017-03-27T18:01:43.16Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDosACaSXULGm37EAP7cNyjM",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/updates"
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
line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code

## Create a Bank Account
```shell

curl https://api-staging.simonpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
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
	    "identity": "IDisW8wNJg3RvTDW3ieUGfJF"
	}'


```
> Example Response:

```json
{
  "id" : "PIsS69gq37muRhZwjbn5mzAg",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-27T18:01:40.87Z",
  "updated_at" : "2017-03-27T18:01:40.87Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
name | *string*, **optional** | Account owner's full name
## Fetch a Bank Account

```shell
curl https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \

```
> Example Response:

```json
{
  "id" : "PIsS69gq37muRhZwjbn5mzAg",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-27T18:01:40.84Z",
  "updated_at" : "2017-03-27T18:01:41.36Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \

```
> Example Response:

```json
{
  "id" : "PI8jksL2cPtP2RLn1udjWzw9",
  "fingerprint" : "FPR-2142146072",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Step Lopez",
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
  "created_at" : "2017-03-27T18:01:43.13Z",
  "updated_at" : "2017-03-27T18:01:49.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDosACaSXULGm37EAP7cNyjM",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
    },
    "authorizations" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
    },
    "transfers" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/verifications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "updates" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/updates"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIgzk8ba3AQVY9dF1MfgMt8v",
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
      "created_at" : "2017-03-27T18:01:51.29Z",
      "updated_at" : "2017-03-27T18:01:51.29Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIgzk8ba3AQVY9dF1MfgMt8v/updates"
        }
      }
    }, {
      "id" : "PIiTtAugaYJ72vwGgBCZXPFJ",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-27T18:01:43.62Z",
      "updated_at" : "2017-03-27T18:01:43.62Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDosACaSXULGm37EAP7cNyjM",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIiTtAugaYJ72vwGgBCZXPFJ"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIiTtAugaYJ72vwGgBCZXPFJ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIiTtAugaYJ72vwGgBCZXPFJ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIiTtAugaYJ72vwGgBCZXPFJ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PI8jksL2cPtP2RLn1udjWzw9",
      "fingerprint" : "FPR-2142146072",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Step Lopez",
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
      "created_at" : "2017-03-27T18:01:43.13Z",
      "updated_at" : "2017-03-27T18:01:49.27Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDosACaSXULGm37EAP7cNyjM",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDosACaSXULGm37EAP7cNyjM"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "updates" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9/updates"
        }
      }
    }, {
      "id" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:41.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIdfB11cikFTJKWmN4igixB",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:41.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIdfB11cikFTJKWmN4igixB"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIdfB11cikFTJKWmN4igixB/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIdfB11cikFTJKWmN4igixB/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIdfB11cikFTJKWmN4igixB/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PI7GEnkizRvU4KU9ZQbbKAXJ",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:41.82Z",
      "updated_at" : "2017-03-27T18:01:41.82Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7GEnkizRvU4KU9ZQbbKAXJ"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7GEnkizRvU4KU9ZQbbKAXJ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7GEnkizRvU4KU9ZQbbKAXJ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7GEnkizRvU4KU9ZQbbKAXJ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIsS69gq37muRhZwjbn5mzAg",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-27T18:01:40.84Z",
      "updated_at" : "2017-03-27T18:01:41.36Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsS69gq37muRhZwjbn5mzAg/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIw7hUiao6KUCWk5XLDEvZFC",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:34.46Z",
      "updated_at" : "2017-03-27T18:01:34.46Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw7hUiao6KUCWk5XLDEvZFC"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw7hUiao6KUCWk5XLDEvZFC/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw7hUiao6KUCWk5XLDEvZFC/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIw7hUiao6KUCWk5XLDEvZFC/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIDuMyiu3yeGr55c1jYxa5n",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:34.46Z",
      "updated_at" : "2017-03-27T18:01:34.46Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIDuMyiu3yeGr55c1jYxa5n"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIDuMyiu3yeGr55c1jYxa5n/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIDuMyiu3yeGr55c1jYxa5n/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIDuMyiu3yeGr55c1jYxa5n/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIh2hwVzGKsJUFHHjqpPEgJY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:34.46Z",
      "updated_at" : "2017-03-27T18:01:34.46Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2f67hZpBDEM1xBfKSp7LPD",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIh2hwVzGKsJUFHHjqpPEgJY"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIh2hwVzGKsJUFHHjqpPEgJY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID2f67hZpBDEM1xBfKSp7LPD"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIh2hwVzGKsJUFHHjqpPEgJY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIh2hwVzGKsJUFHHjqpPEgJY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "PIsQfMg46t2Ao7toYv6kyQxE",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T18:01:34.46Z",
      "updated_at" : "2017-03-27T18:01:34.46Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsQfMg46t2Ao7toYv6kyQxE"
        },
        "authorizations" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsQfMg46t2Ao7toYv6kyQxE/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/ID3EeRyDn2cibtmhGBMZQAy6"
        },
        "transfers" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsQfMg46t2Ao7toYv6kyQxE/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIsQfMg46t2Ao7toYv6kyQxE/verifications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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

`ready_to_settle_at` field can have 2 possible values:

1. `null`: Funds have been captured, but are not yet ready to be paid out
2. `TIMESTAMP`: A UTC timestamp that specifies when the funds will be available to be payout out. Once in the past, the Transfer will be eligible for inclusion in a batch Settlement.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside> 
## Retrieve a Transfer
```shell

curl https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0


```
> Example Response:

```json
{
  "id" : "TR6wQHhXzrNANbQx5ENpdUci",
  "amount" : 501062,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "51327cd3-0a70-4f88-b82a-a37b7ae2b297",
  "currency" : "USD",
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "source" : "PI8jksL2cPtP2RLn1udjWzw9",
  "destination" : "PI7aNojAFGd8Vi9yvU3B4mod",
  "ready_to_settle_at" : null,
  "fee" : 50106,
  "statement_descriptor" : "SPN*ACME ANCHORS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:44.06Z",
  "updated_at" : "2017-03-27T18:01:44.24Z",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "reversals" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/disputes"
    },
    "source" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
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

curl https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
> Example Response:

```json
{
  "id" : "TRhLhkuqc1aPpLZGV77KQHAc",
  "amount" : 232035,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "87c1030a-73b3-4ddf-9001-61a68208b973",
  "currency" : "USD",
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "source" : "PI7aNojAFGd8Vi9yvU3B4mod",
  "destination" : "PI8jksL2cPtP2RLn1udjWzw9",
  "ready_to_settle_at" : null,
  "fee" : 23204,
  "statement_descriptor" : "SPN*ACME ANCHORS",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T18:01:48.45Z",
  "updated_at" : "2017-03-27T18:01:48.55Z",
  "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    },
    "self" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRhLhkuqc1aPpLZGV77KQHAc"
    },
    "parent" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY"
    },
    "destination" : {
      "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.simonpayments.com/transfers/TRhLhkuqc1aPpLZGV77KQHAc/payment_instruments"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR4F9Gqgnk8SJyaDgFG2S1xU",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "5a27cf78-39ed-4c65-b551-d46af58eab1a",
      "currency" : "USD",
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "source" : "PI8jksL2cPtP2RLn1udjWzw9",
      "destination" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:49.74Z",
      "updated_at" : "2017-03-27T18:01:49.89Z",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR4F9Gqgnk8SJyaDgFG2S1xU/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
        }
      }
    }, {
      "id" : "TRhLhkuqc1aPpLZGV77KQHAc",
      "amount" : 232035,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "93388f24-eb97-45e5-b5f4-fa9ee1fdd98c",
      "currency" : "USD",
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "source" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "destination" : "PI8jksL2cPtP2RLn1udjWzw9",
      "ready_to_settle_at" : null,
      "fee" : 23204,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:48.28Z",
      "updated_at" : "2017-03-27T18:01:48.55Z",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRhLhkuqc1aPpLZGV77KQHAc"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRhLhkuqc1aPpLZGV77KQHAc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "parent" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
        }
      }
    }, {
      "id" : "TRsDhGYyT2iCZsrpY5eMJftY",
      "amount" : 232035,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "8be5cb2e-216f-4c5d-b8ab-f85a19b2327f",
      "currency" : "USD",
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "source" : "PI8jksL2cPtP2RLn1udjWzw9",
      "destination" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "ready_to_settle_at" : null,
      "fee" : 23204,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:47.15Z",
      "updated_at" : "2017-03-27T18:01:48.39Z",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsDhGYyT2iCZsrpY5eMJftY/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
        }
      }
    }, {
      "id" : "TRsKHiCYDcbUjoptSdXNfT1g",
      "amount" : 641277,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "d9149afc-86a1-486a-998b-10de3c6b39df",
      "currency" : "USD",
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "source" : "PIiTtAugaYJ72vwGgBCZXPFJ",
      "destination" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "ready_to_settle_at" : null,
      "fee" : 64128,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:44.67Z",
      "updated_at" : "2017-03-27T18:01:44.82Z",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsKHiCYDcbUjoptSdXNfT1g"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsKHiCYDcbUjoptSdXNfT1g/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsKHiCYDcbUjoptSdXNfT1g/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsKHiCYDcbUjoptSdXNfT1g/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TRsKHiCYDcbUjoptSdXNfT1g/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PIiTtAugaYJ72vwGgBCZXPFJ"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
        }
      }
    }, {
      "id" : "TR6wQHhXzrNANbQx5ENpdUci",
      "amount" : 501062,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "51327cd3-0a70-4f88-b82a-a37b7ae2b297",
      "currency" : "USD",
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "source" : "PI8jksL2cPtP2RLn1udjWzw9",
      "destination" : "PI7aNojAFGd8Vi9yvU3B4mod",
      "ready_to_settle_at" : null,
      "fee" : 50106,
      "statement_descriptor" : "SPN*ACME ANCHORS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T18:01:44.06Z",
      "updated_at" : "2017-03-27T18:01:44.24Z",
      "merchant_identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        },
        "self" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF"
        },
        "reversals" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.simonpayments.com/transfers/TR6wQHhXzrNANbQx5ENpdUci/disputes"
        },
        "source" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI8jksL2cPtP2RLn1udjWzw9"
        },
        "destination" : {
          "href" : "https://api-staging.simonpayments.com/payment_instruments/PI7aNojAFGd8Vi9yvU3B4mod"
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


## Create ROLE_PLATFORM User
```shell
curl https://api-staging.simonpayments.com/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40 \
    -d '
	{
	    "role": "ROLE_PLATFORM"
	}'

```
> Example Response:

```json
{
  "id" : "US2ZtHZG25bkUnsKWJc25dKk",
  "password" : "31524d85-cfba-4bf9-8dd0-688059716d9a",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PLATFORM",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:35.30Z",
  "updated_at" : "2017-03-27T18:01:35.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/US2ZtHZG25bkUnsKWJc25dKk"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    }
  }
}
```


This is the equivalent of provisioning API keys (i.e. credentials) for a Platform.

<aside class="notice">
A credential with a level of ROLE_PLATFORM has access to all Application and Merchant data.
</aside>


#### HTTP Request

`POST https://api-staging.simonpayments.com/users`

#### URL Parameters
Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user


## Create ROLE_MERCHANT User
```shell
curl https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "USkt2SSmL9hUmzz4ETgTvATE",
  "password" : "64ead5ec-8e2d-4048-a9ab-b0da17c201bb",
  "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:34.92Z",
  "updated_at" : "2017-03-27T18:01:34.92Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USkt2SSmL9hUmzz4ETgTvATE"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/identities/IDisW8wNJg3RvTDW3ieUGfJF/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '{}'

```
> Example Response:

```json
{
  "id" : "US9YGjjDeS6pzD1tnEpc33Hk",
  "password" : "f603b4c7-971d-440b-9e8f-f45e3ebb0c20",
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:45.23Z",
  "updated_at" : "2017-03-27T18:01:45.23Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/US9YGjjDeS6pzD1tnEpc33Hk"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/users/TR6wQHhXzrNANbQx5ENpdUci \
    -H "Content-Type: application/vnd.json+api" \
    -u  USuLfsumBoZixiKvmovnUZps:e722eafe-0bc5-450d-a41a-c9c48c3c5a40

```
> Example Response:

```json
{
  "id" : "USdfmiYeT2zJARHvt91o98kN",
  "password" : null,
  "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:33.53Z",
  "updated_at" : "2017-03-27T18:01:33.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/USdfmiYeT2zJARHvt91o98kN"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
curl https://api-staging.simonpayments.com/users/US9YGjjDeS6pzD1tnEpc33Hk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -X PUT \
    -d '
	{
	    "enabled": false
	}'

```
> Example Response:

```json
{
  "id" : "US9YGjjDeS6pzD1tnEpc33Hk",
  "password" : null,
  "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-03-27T18:01:45.19Z",
  "updated_at" : "2017-03-27T18:01:45.58Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/users/US9YGjjDeS6pzD1tnEpc33Hk"
    },
    "applications" : {
      "href" : "https://api-staging.simonpayments.com/applications"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "US9YGjjDeS6pzD1tnEpc33Hk",
      "password" : null,
      "identity" : "IDisW8wNJg3RvTDW3ieUGfJF",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-03-27T18:01:45.19Z",
      "updated_at" : "2017-03-27T18:01:45.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/US9YGjjDeS6pzD1tnEpc33Hk"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "USkt2SSmL9hUmzz4ETgTvATE",
      "password" : null,
      "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-03-27T18:01:34.90Z",
      "updated_at" : "2017-03-27T18:01:34.90Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/USkt2SSmL9hUmzz4ETgTvATE"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
        }
      }
    }, {
      "id" : "USdfmiYeT2zJARHvt91o98kN",
      "password" : null,
      "identity" : "ID3EeRyDn2cibtmhGBMZQAy6",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-03-27T18:01:33.53Z",
      "updated_at" : "2017-03-27T18:01:33.87Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/users/USdfmiYeT2zJARHvt91o98kN"
        },
        "applications" : {
          "href" : "https://api-staging.simonpayments.com/applications"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
> Example Response:

```json
{
  "id" : "WH2oiugBggdsZabDP49qmEwJ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "created_at" : "2017-03-27T18:01:36.35Z",
  "updated_at" : "2017-03-27T18:01:36.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WH2oiugBggdsZabDP49qmEwJ"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.simonpayments.com/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request

## Retrieve a Webhook

```shell



curl https://api-staging.simonpayments.com/webhooks/WH2oiugBggdsZabDP49qmEwJ \
    -H "Content-Type: application/vnd.json+api" \
    -u USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0


```
> Example Response:

```json
{
  "id" : "WH2oiugBggdsZabDP49qmEwJ",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APpQYhFe2yxLyWvGb9cYprtY",
  "created_at" : "2017-03-27T18:01:36.35Z",
  "updated_at" : "2017-03-27T18:01:36.35Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.simonpayments.com/webhooks/WH2oiugBggdsZabDP49qmEwJ"
    },
    "application" : {
      "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
    -u  USdfmiYeT2zJARHvt91o98kN:aedaece9-f759-40dc-96f6-b641850f67f0

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WH2oiugBggdsZabDP49qmEwJ",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APpQYhFe2yxLyWvGb9cYprtY",
      "created_at" : "2017-03-27T18:01:36.35Z",
      "updated_at" : "2017-03-27T18:01:36.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.simonpayments.com/webhooks/WH2oiugBggdsZabDP49qmEwJ"
        },
        "application" : {
          "href" : "https://api-staging.simonpayments.com/applications/APpQYhFe2yxLyWvGb9cYprtY"
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
