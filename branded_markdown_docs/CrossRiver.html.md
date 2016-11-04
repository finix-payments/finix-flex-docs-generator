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
    -u  None:None

```
```python


from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("None", "None"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `None`

- Password: `None`

- Application ID: `APkXv4H4EFsN2XDqHHgDHvCH`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
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
```python



```
> Example Response:

```json
{
  "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
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
  "created_at" : "2016-11-04T18:12:02.55Z",
  "updated_at" : "2016-11-04T18:12:02.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u  None:None \
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
	    "identity": "ID2vAEnEE63Sw6DP1Vhz4xou"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PI6ouGNg3Hef35xLxKiN6CRh",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-04T18:12:10.54Z",
  "updated_at" : "2016-11-04T18:12:10.54Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```python



```
> Example Response:

```json
{
  "id" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "verification" : "VIrBzvaxNJK7kBVsmjCURtcf",
  "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-04T18:12:12.07Z",
  "updated_at" : "2016-11-04T18:12:12.07Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIrBzvaxNJK7kBVsmjCURtcf"
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
    -u  None:None \
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
```python



```
> Example Response:

```json
{
  "id" : "IDJv8M3WiRoNJLdwMQERseZ",
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
  "created_at" : "2016-11-04T18:12:13.41Z",
  "updated_at" : "2016-11-04T18:12:13.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u  None:None \
    -d '
	{
	    "name": "Sean Chang", 
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
	    "identity": "IDJv8M3WiRoNJLdwMQERseZ"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PIgD8LQDKYZoWifmwnySHeSz",
  "fingerprint" : "FPR-1725276824",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Chang",
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
  "created_at" : "2016-11-04T18:12:13.97Z",
  "updated_at" : "2016-11-04T18:12:13.97Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDJv8M3WiRoNJLdwMQERseZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/updates"
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
    -u  None:None \
    -d '
	{
	    "merchant_identity": "ID2vAEnEE63Sw6DP1Vhz4xou", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIgD8LQDKYZoWifmwnySHeSz", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```python



```
> Example Response:

```json
{
  "id" : "AUhJm5rigLU95uuydwz8qVTv",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:20.44Z",
  "updated_at" : "2016-11-04T18:12:20.46Z",
  "trace_id" : "82429ec7-8778-46b5-9602-8c47d2e7efda",
  "source" : "PIgD8LQDKYZoWifmwnySHeSz",
  "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "is_void" : false,
  "expires_at" : "2016-11-11T18:12:20.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUhJm5rigLU95uuydwz8qVTv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
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
curl https://api-staging.finix.io/authorizations/AUhJm5rigLU95uuydwz8qVTv \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```python



```
> Example Response:

```json
{
  "id" : "AUhJm5rigLU95uuydwz8qVTv",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRcreu9x8o4FUHoDcEZD941V",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:20.30Z",
  "updated_at" : "2016-11-04T18:12:21.36Z",
  "trace_id" : "82429ec7-8778-46b5-9602-8c47d2e7efda",
  "source" : "PIgD8LQDKYZoWifmwnySHeSz",
  "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "is_void" : false,
  "expires_at" : "2016-11-11T18:12:20.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/authorizations/AUhJm5rigLU95uuydwz8qVTv"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "transfer" : {
      "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
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

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** https://api-staging.finix.io

- **Production API:** https://api.finix.io

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
          applicationId: 'APkXv4H4EFsN2XDqHHgDHvCH',
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
  "id" : "TKgNK8H5Qr49xNFmxm9X1eY7",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-04T18:12:23.00Z",
  "updated_at" : "2016-11-04T18:12:23.00Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-05T18:12:23.00Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
	{
	    "token": "TKgNK8H5Qr49xNFmxm9X1eY7", 
	    "type": "TOKEN", 
	    "identity": "ID2vAEnEE63Sw6DP1Vhz4xou"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PIgNK8H5Qr49xNFmxm9X1eY7",
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
  "created_at" : "2016-11-04T18:12:23.90Z",
  "updated_at" : "2016-11-04T18:12:23.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/updates"
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
    -u None:None \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jim", 
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
```python



```
> Example Response:

```json
{
  "id" : "ID66ohrB618eUqA58MdPVr6G",
  "entity" : {
    "title" : null,
    "first_name" : "Jim",
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
  "created_at" : "2016-11-04T18:12:37.37Z",
  "updated_at" : "2016-11-04T18:12:37.37Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u None:None \
    -d '
	{
	    "name": "Sean Lopez", 
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
	    "identity": "ID66ohrB618eUqA58MdPVr6G"
	}'
```
```python



```
> Example Response:

```json
{
  "id" : "PItpSEeugC18nehxMcCFYcLF",
  "fingerprint" : "FPR-1565164664",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Lopez",
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
  "created_at" : "2016-11-04T18:12:39.22Z",
  "updated_at" : "2016-11-04T18:12:39.22Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID66ohrB618eUqA58MdPVr6G",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/updates"
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
curl https://api-staging.finix.io/identities/'MUqAQxW4GN3ZburE8pWoNZJr'/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '
```
```python



```
> Example Response:

```json
{
  "id" : "TR9mjKgPzWMtkSp8STrshL6Q",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "83803",
  "currency" : "USD",
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "source" : "PIwsxMD9BuvQqJ7T1FF88DQN",
  "destination" : "PItpSEeugC18nehxMcCFYcLF",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:41.36Z",
  "updated_at" : "2016-11-04T18:12:42.42Z",
  "merchant_identity" : "ID8hBB363XVWxeF6akLei282",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF"
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
    -u None:None \
    -d '
	{
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "merchant_identity": "ID66ohrB618eUqA58MdPVr6G", 
	    "destination": "PItpSEeugC18nehxMcCFYcLF", 
	    "currency": "USD", 
	    "amount": 10000, 
	    "processor": "VISA_V1"
	}'

```
```python



```
> Example Response:

```json
{
  "id" : "TR9mjKgPzWMtkSp8STrshL6Q",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "83803",
  "currency" : "USD",
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "source" : "PIwsxMD9BuvQqJ7T1FF88DQN",
  "destination" : "PItpSEeugC18nehxMcCFYcLF",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:41.36Z",
  "updated_at" : "2016-11-04T18:12:42.42Z",
  "merchant_identity" : "ID8hBB363XVWxeF6akLei282",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF"
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
    -u  None:None \
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
```python



```
> Example Response:

```json
{
  "id" : "IDJv8M3WiRoNJLdwMQERseZ",
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
  "created_at" : "2016-11-04T18:12:13.41Z",
  "updated_at" : "2016-11-04T18:12:13.41Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u  None:None \
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
```python



```
> Example Response:

```json
{
  "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
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
  "created_at" : "2016-11-04T18:12:02.55Z",
  "updated_at" : "2016-11-04T18:12:02.55Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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

curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
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
  "created_at" : "2016-11-04T18:12:02.48Z",
  "updated_at" : "2016-11-04T18:12:02.48Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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

## List all Identities
```shell
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID66ohrB618eUqA58MdPVr6G",
      "entity" : {
        "title" : null,
        "first_name" : "Jim",
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
      "created_at" : "2016-11-04T18:12:37.31Z",
      "updated_at" : "2016-11-04T18:12:37.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDJv8M3WiRoNJLdwMQERseZ",
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
      "created_at" : "2016-11-04T18:12:13.35Z",
      "updated_at" : "2016-11-04T18:12:13.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8Pb91vGyRp8TasukyLf5S9",
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
      "created_at" : "2016-11-04T18:12:09.77Z",
      "updated_at" : "2016-11-04T18:12:09.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDwcHArpBCbsp3QsaRVwvbPL",
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
      "created_at" : "2016-11-04T18:12:09.25Z",
      "updated_at" : "2016-11-04T18:12:09.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8udqn7gW5k3GBbRdMfYACD",
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
      "created_at" : "2016-11-04T18:12:08.74Z",
      "updated_at" : "2016-11-04T18:12:08.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDp285FcRy4gXL1taVUkM6HN",
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
      "created_at" : "2016-11-04T18:12:07.60Z",
      "updated_at" : "2016-11-04T18:12:07.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID6r9xYbSAVMGyjU21BgTWih",
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
      "created_at" : "2016-11-04T18:12:07.09Z",
      "updated_at" : "2016-11-04T18:12:07.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDowuiL7p5zrYtgpp5u2qhfB",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-04T18:12:06.28Z",
      "updated_at" : "2016-11-04T18:12:06.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDk27K97wyqVD4ADDMEPfz8V",
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
      "created_at" : "2016-11-04T18:12:05.59Z",
      "updated_at" : "2016-11-04T18:12:05.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDsAS8wMnrJ6Yr2ouE3Xx6z6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-11-04T18:12:04.42Z",
      "updated_at" : "2016-11-04T18:12:04.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDoKc3qAdYbN54kH1dFXmSqG",
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
      "created_at" : "2016-11-04T18:12:03.37Z",
      "updated_at" : "2016-11-04T18:12:03.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
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
      "created_at" : "2016-11-04T18:12:02.48Z",
      "updated_at" : "2016-11-04T18:12:02.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8hBB363XVWxeF6akLei282",
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
      "created_at" : "2016-11-04T18:11:58.00Z",
      "updated_at" : "2016-11-04T18:11:58.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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


## Update an Identity
```shell
curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Fran", 
	        "last_name": "Wade", 
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
```python



```
> Example Response:

```json
{
  "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Fran",
    "last_name" : "Wade",
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
  "created_at" : "2016-11-04T18:12:02.48Z",
  "updated_at" : "2016-11-04T18:13:07.52Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
## Provision a Merchant

```shell

curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '


```
```python



```

> Example Response:

```json
{
  "id" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "verification" : "VIrBzvaxNJK7kBVsmjCURtcf",
  "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-04T18:12:12.07Z",
  "updated_at" : "2016-11-04T18:12:12.07Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIrBzvaxNJK7kBVsmjCURtcf"
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

`POST https://api-staging.finix.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
          {
            "tags": {
              "key_2": "value_2"
            }
          }
        '

```
```python



```
> Example Response:

```json
{
  "id" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "verification" : "VIrBzvaxNJK7kBVsmjCURtcf",
  "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-11-04T18:12:12.07Z",
  "updated_at" : "2016-11-04T18:12:12.07Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIrBzvaxNJK7kBVsmjCURtcf"
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
curl https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "id" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "verification" : null,
  "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2016-11-04T18:12:11.92Z",
  "updated_at" : "2016-11-04T18:12:12.24Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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

## Create a Merchant User
```shell
curl https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '{}'

```
```python



```
> Example Response:

```json
{
  "id" : "USjCpf8q8USL2PUbTXoi9UNP",
  "password" : "6ef24915-ac61-4949-8f9a-65548b495b63",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2016-11-04T18:12:17.64Z",
  "updated_at" : "2016-11-04T18:12:17.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USjCpf8q8USL2PUbTXoi9UNP"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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


## Reattempt Merchant Provisioning
```shell
curl https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '{}'
```
```python



```
> Example Response:

```json
{
  "id" : "VImnAxWubwLSQ1wDeP2yDbjw",
  "external_trace_id" : "3927026a-d53c-488c-aad0-21fbbce764de",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-04T18:13:09.59Z",
  "updated_at" : "2016-11-04T18:13:09.61Z",
  "payment_instrument" : null,
  "merchant" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImnAxWubwLSQ1wDeP2yDbjw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
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

## Update Info on Processor
```shell
curl https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '{}'

```
```python



```
> Example Response:

```json
{
  "id" : "VImnAxWubwLSQ1wDeP2yDbjw",
  "external_trace_id" : "3927026a-d53c-488c-aad0-21fbbce764de",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2016-11-04T18:13:09.59Z",
  "updated_at" : "2016-11-04T18:13:09.61Z",
  "payment_instrument" : null,
  "merchant" : "MUtdYw4NvM2Z1EGMv72FkCkG",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/verifications/VImnAxWubwLSQ1wDeP2yDbjw"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "merchant" : {
      "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
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

## List all Merchants
```shell
curl https://api-staging.finix.io/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUqAQxW4GN3ZburE8pWoNZJr",
      "identity" : "ID66ohrB618eUqA58MdPVr6G",
      "verification" : null,
      "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
      "processor" : "DUMMY_V1",
      "processing_enabled" : false,
      "settlement_enabled" : false,
      "tags" : { },
      "created_at" : "2016-11-04T18:12:43.14Z",
      "updated_at" : "2016-11-04T18:12:43.14Z",
      "onboarding_state" : "PROVISIONING",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUqAQxW4GN3ZburE8pWoNZJr"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUqAQxW4GN3ZburE8pWoNZJr/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "MUtdYw4NvM2Z1EGMv72FkCkG",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "verification" : null,
      "merchant_profile" : "MPrx8QsoVALmDvUbGomnHwCp",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2016-11-04T18:12:11.92Z",
      "updated_at" : "2016-11-04T18:12:12.24Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications"
        },
        "merchant_profile" : {
          "href" : "https://api-staging.finix.io/merchant_profiles/MPrx8QsoVALmDvUbGomnHwCp"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
curl https://api-staging.finix.io/merchants/MUtdYw4NvM2Z1EGMv72FkCkG/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "ID66ohrB618eUqA58MdPVr6G",
      "entity" : {
        "title" : null,
        "first_name" : "Jim",
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
      "created_at" : "2016-11-04T18:12:37.31Z",
      "updated_at" : "2016-11-04T18:12:37.31Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDJv8M3WiRoNJLdwMQERseZ",
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
      "created_at" : "2016-11-04T18:12:13.35Z",
      "updated_at" : "2016-11-04T18:12:13.35Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8Pb91vGyRp8TasukyLf5S9",
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
      "created_at" : "2016-11-04T18:12:09.77Z",
      "updated_at" : "2016-11-04T18:12:09.77Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8Pb91vGyRp8TasukyLf5S9/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDwcHArpBCbsp3QsaRVwvbPL",
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
      "created_at" : "2016-11-04T18:12:09.25Z",
      "updated_at" : "2016-11-04T18:12:09.25Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDwcHArpBCbsp3QsaRVwvbPL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8udqn7gW5k3GBbRdMfYACD",
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
      "created_at" : "2016-11-04T18:12:08.74Z",
      "updated_at" : "2016-11-04T18:12:08.74Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8udqn7gW5k3GBbRdMfYACD/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDp285FcRy4gXL1taVUkM6HN",
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
      "created_at" : "2016-11-04T18:12:07.60Z",
      "updated_at" : "2016-11-04T18:12:07.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDp285FcRy4gXL1taVUkM6HN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID6r9xYbSAVMGyjU21BgTWih",
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
      "created_at" : "2016-11-04T18:12:07.09Z",
      "updated_at" : "2016-11-04T18:12:07.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID6r9xYbSAVMGyjU21BgTWih/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDowuiL7p5zrYtgpp5u2qhfB",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2016-11-04T18:12:06.28Z",
      "updated_at" : "2016-11-04T18:12:06.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDowuiL7p5zrYtgpp5u2qhfB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDk27K97wyqVD4ADDMEPfz8V",
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
      "created_at" : "2016-11-04T18:12:05.59Z",
      "updated_at" : "2016-11-04T18:12:05.59Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDk27K97wyqVD4ADDMEPfz8V/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDsAS8wMnrJ6Yr2ouE3Xx6z6",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2016-11-04T18:12:04.42Z",
      "updated_at" : "2016-11-04T18:12:04.42Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDsAS8wMnrJ6Yr2ouE3Xx6z6/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "IDoKc3qAdYbN54kH1dFXmSqG",
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
      "created_at" : "2016-11-04T18:12:03.37Z",
      "updated_at" : "2016-11-04T18:12:03.37Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoKc3qAdYbN54kH1dFXmSqG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID2vAEnEE63Sw6DP1Vhz4xou",
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
      "created_at" : "2016-11-04T18:12:02.48Z",
      "updated_at" : "2016-11-04T18:12:02.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "ID8hBB363XVWxeF6akLei282",
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
      "created_at" : "2016-11-04T18:11:58.00Z",
      "updated_at" : "2016-11-04T18:11:58.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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




# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Create a Card
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
	{
	    "name": "Sean Chang", 
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
	    "identity": "IDJv8M3WiRoNJLdwMQERseZ"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PIgD8LQDKYZoWifmwnySHeSz",
  "fingerprint" : "FPR-1725276824",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Sean Chang",
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
  "created_at" : "2016-11-04T18:12:13.97Z",
  "updated_at" : "2016-11-04T18:12:13.97Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDJv8M3WiRoNJLdwMQERseZ",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/updates"
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
    -u  None:None \
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
	    "identity": "ID2vAEnEE63Sw6DP1Vhz4xou"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PI6ouGNg3Hef35xLxKiN6CRh",
  "fingerprint" : "FPR-1215770130",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-04T18:12:10.54Z",
  "updated_at" : "2016-11-04T18:12:10.54Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
          applicationId: 'APkXv4H4EFsN2XDqHHgDHvCH',
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
  "id" : "TKgNK8H5Qr49xNFmxm9X1eY7",
  "fingerprint" : "FPR284253560",
  "created_at" : "2016-11-04T18:12:23.00Z",
  "updated_at" : "2016-11-04T18:12:23.00Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-11-05T18:12:23.00Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    }
  }
}
```

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d '
	{
	    "token": "TKgNK8H5Qr49xNFmxm9X1eY7", 
	    "type": "TOKEN", 
	    "identity": "ID2vAEnEE63Sw6DP1Vhz4xou"
	}'

```
```python



```
### Step 4: Associate to an Identity

> Example Response:

```json
{
  "id" : "PIgNK8H5Qr49xNFmxm9X1eY7",
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
  "created_at" : "2016-11-04T18:12:23.90Z",
  "updated_at" : "2016-11-04T18:12:23.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/updates"
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
    -u  None:None \
    -d '
	{
	    "token": "TKgNK8H5Qr49xNFmxm9X1eY7", 
	    "type": "TOKEN", 
	    "identity": "ID2vAEnEE63Sw6DP1Vhz4xou"
	}'


```
```python



```
> Example Response:

```json
{
  "id" : "PIgNK8H5Qr49xNFmxm9X1eY7",
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
  "created_at" : "2016-11-04T18:12:23.90Z",
  "updated_at" : "2016-11-04T18:12:23.90Z",
  "instrument_type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/updates"
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


## Fetch a Payment Instrument

```shell


curl https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \

```
```python



```
> Example Response:

```json
{
  "id" : "PI6ouGNg3Hef35xLxKiN6CRh",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-04T18:12:10.44Z",
  "updated_at" : "2016-11-04T18:12:11.32Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
curl https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
	    }
	}'

```
```python



```
> Example Response:

```json
{
  "id" : "PI6ouGNg3Hef35xLxKiN6CRh",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-11-04T18:12:10.44Z",
  "updated_at" : "2016-11-04T18:12:11.32Z",
  "instrument_type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u  None:None
```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PItpSEeugC18nehxMcCFYcLF",
      "fingerprint" : "FPR-1565164664",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Sean Lopez",
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
      "created_at" : "2016-11-04T18:12:39.14Z",
      "updated_at" : "2016-11-04T18:12:39.14Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID66ohrB618eUqA58MdPVr6G",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID66ohrB618eUqA58MdPVr6G"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF/updates"
        }
      }
    }, {
      "id" : "PIcXXs677mCoEGHtijejEheT",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:34.89Z",
      "updated_at" : "2016-11-04T18:12:34.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcXXs677mCoEGHtijejEheT"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcXXs677mCoEGHtijejEheT/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcXXs677mCoEGHtijejEheT/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIcXXs677mCoEGHtijejEheT/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PInEkTMRE34graD9ms9rhG1Z",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:34.89Z",
      "updated_at" : "2016-11-04T18:12:34.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInEkTMRE34graD9ms9rhG1Z"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInEkTMRE34graD9ms9rhG1Z/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInEkTMRE34graD9ms9rhG1Z/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PInEkTMRE34graD9ms9rhG1Z/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIwsxMD9BuvQqJ7T1FF88DQN",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:34.89Z",
      "updated_at" : "2016-11-04T18:12:34.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIjUYynSXuJw5uYghJL4e1Si",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:34.89Z",
      "updated_at" : "2016-11-04T18:12:34.89Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjUYynSXuJw5uYghJL4e1Si"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjUYynSXuJw5uYghJL4e1Si/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjUYynSXuJw5uYghJL4e1Si/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIjUYynSXuJw5uYghJL4e1Si/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIgNK8H5Qr49xNFmxm9X1eY7",
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
      "created_at" : "2016-11-04T18:12:23.77Z",
      "updated_at" : "2016-11-04T18:12:23.77Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgNK8H5Qr49xNFmxm9X1eY7/updates"
        }
      }
    }, {
      "id" : "PIrkmpUrawSm356DLY5g4kuo",
      "fingerprint" : "FPR-1215770130",
      "tags" : { },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-04T18:12:14.68Z",
      "updated_at" : "2016-11-04T18:12:14.68Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDJv8M3WiRoNJLdwMQERseZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrkmpUrawSm356DLY5g4kuo"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrkmpUrawSm356DLY5g4kuo/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrkmpUrawSm356DLY5g4kuo/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrkmpUrawSm356DLY5g4kuo/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIgD8LQDKYZoWifmwnySHeSz",
      "fingerprint" : "FPR-1725276824",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Sean Chang",
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
      "created_at" : "2016-11-04T18:12:13.89Z",
      "updated_at" : "2016-11-04T18:12:20.46Z",
      "instrument_type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDJv8M3WiRoNJLdwMQERseZ",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDJv8M3WiRoNJLdwMQERseZ"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz/updates"
        }
      }
    }, {
      "id" : "PI4UzjFS9tMN5gXS9oEn99Rb",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:11.92Z",
      "updated_at" : "2016-11-04T18:12:11.92Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4UzjFS9tMN5gXS9oEn99Rb"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4UzjFS9tMN5gXS9oEn99Rb/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4UzjFS9tMN5gXS9oEn99Rb/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI4UzjFS9tMN5gXS9oEn99Rb/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIiJj9MbmJ39HrkqegnrNqos",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:11.92Z",
      "updated_at" : "2016-11-04T18:12:11.92Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIchzapAepf945YNxXkj9sch",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:12:11.92Z",
      "updated_at" : "2016-11-04T18:12:11.92Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIchzapAepf945YNxXkj9sch"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIchzapAepf945YNxXkj9sch/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIchzapAepf945YNxXkj9sch/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIchzapAepf945YNxXkj9sch/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PI6ouGNg3Hef35xLxKiN6CRh",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-11-04T18:12:10.44Z",
      "updated_at" : "2016-11-04T18:12:11.32Z",
      "instrument_type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6ouGNg3Hef35xLxKiN6CRh/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIagLck1w6iTqPy3wF2gtRiA",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:11:58.84Z",
      "updated_at" : "2016-11-04T18:11:58.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIagLck1w6iTqPy3wF2gtRiA"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIagLck1w6iTqPy3wF2gtRiA/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIagLck1w6iTqPy3wF2gtRiA/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIagLck1w6iTqPy3wF2gtRiA/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PI9BojPUZW21DwHSkgUqi2eF",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:11:58.84Z",
      "updated_at" : "2016-11-04T18:11:58.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9BojPUZW21DwHSkgUqi2eF"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9BojPUZW21DwHSkgUqi2eF/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9BojPUZW21DwHSkgUqi2eF/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9BojPUZW21DwHSkgUqi2eF/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PI3mTXsME91v6WA7W9GgJskY",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:11:58.84Z",
      "updated_at" : "2016-11-04T18:11:58.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3mTXsME91v6WA7W9GgJskY"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3mTXsME91v6WA7W9GgJskY/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3mTXsME91v6WA7W9GgJskY/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI3mTXsME91v6WA7W9GgJskY/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        }
      }
    }, {
      "id" : "PIdJngk1trVwyVZzHALdMiBX",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-11-04T18:11:58.84Z",
      "updated_at" : "2016-11-04T18:11:58.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdJngk1trVwyVZzHALdMiBX"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdJngk1trVwyVZzHALdMiBX/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdJngk1trVwyVZzHALdMiBX/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIdJngk1trVwyVZzHALdMiBX/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
```shell

curl https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None


```
```python



```
> Example Response:

```json
{
  "id" : "TRvrjUj9GNaAqPHEknwoCMoe",
  "amount" : 182533,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "CANCELED",
  "trace_id" : "74f745f9-2b95-4efa-9599-7cd8a383fdc4",
  "currency" : "USD",
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "source" : "PIgD8LQDKYZoWifmwnySHeSz",
  "destination" : "PIiJj9MbmJ39HrkqegnrNqos",
  "ready_to_settle_at" : null,
  "fee" : 18253,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:15.89Z",
  "updated_at" : "2016-11-04T18:12:19.23Z",
  "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos"
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

curl https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  None:None \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```python



```
> Example Response:

```json
{
  "id" : "TRdvdVk3dY5C6ECgjgAaqia8",
  "amount" : 100,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "654231f5-0c3e-4f2e-8c1f-4c2a12af3bc5",
  "currency" : "USD",
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "source" : "PIiJj9MbmJ39HrkqegnrNqos",
  "destination" : "PIgD8LQDKYZoWifmwnySHeSz",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FNX*GOLDS GYM",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-11-04T18:12:19.25Z",
  "updated_at" : "2016-11-04T18:12:19.35Z",
  "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRdvdVk3dY5C6ECgjgAaqia8"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRdvdVk3dY5C6ECgjgAaqia8/payment_instruments"
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
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR9mjKgPzWMtkSp8STrshL6Q",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "83803",
      "currency" : "USD",
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "source" : "PIwsxMD9BuvQqJ7T1FF88DQN",
      "destination" : "PItpSEeugC18nehxMcCFYcLF",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-04T18:12:41.16Z",
      "updated_at" : "2016-11-04T18:12:42.42Z",
      "merchant_identity" : "ID8hBB363XVWxeF6akLei282",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8hBB363XVWxeF6akLei282"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR9mjKgPzWMtkSp8STrshL6Q/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwsxMD9BuvQqJ7T1FF88DQN"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PItpSEeugC18nehxMcCFYcLF"
        }
      }
    }, {
      "id" : "TRcreu9x8o4FUHoDcEZD941V",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "82429ec7-8778-46b5-9602-8c47d2e7efda",
      "currency" : "USD",
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "source" : "PIgD8LQDKYZoWifmwnySHeSz",
      "destination" : "PIiJj9MbmJ39HrkqegnrNqos",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-04T18:12:21.15Z",
      "updated_at" : "2016-11-04T18:12:21.36Z",
      "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcreu9x8o4FUHoDcEZD941V/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos"
        }
      }
    }, {
      "id" : "TRdvdVk3dY5C6ECgjgAaqia8",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "9bb29306-fc70-4a3e-9193-ab53030db4a4",
      "currency" : "USD",
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "source" : "PIiJj9MbmJ39HrkqegnrNqos",
      "destination" : "PIgD8LQDKYZoWifmwnySHeSz",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-04T18:12:19.06Z",
      "updated_at" : "2016-11-04T18:12:19.35Z",
      "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRdvdVk3dY5C6ECgjgAaqia8"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRdvdVk3dY5C6ECgjgAaqia8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
        }
      }
    }, {
      "id" : "TRx856DemNLnXsKcPtqBVsH8",
      "amount" : 463709,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "e5f73866-f21a-4bd8-bac1-cef5da5056ea",
      "currency" : "USD",
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "source" : "PIrkmpUrawSm356DLY5g4kuo",
      "destination" : "PIiJj9MbmJ39HrkqegnrNqos",
      "ready_to_settle_at" : null,
      "fee" : 46371,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-04T18:12:16.72Z",
      "updated_at" : "2016-11-04T18:12:16.92Z",
      "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRx856DemNLnXsKcPtqBVsH8"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRx856DemNLnXsKcPtqBVsH8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRx856DemNLnXsKcPtqBVsH8/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRx856DemNLnXsKcPtqBVsH8/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRx856DemNLnXsKcPtqBVsH8/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrkmpUrawSm356DLY5g4kuo"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos"
        }
      }
    }, {
      "id" : "TRvrjUj9GNaAqPHEknwoCMoe",
      "amount" : 182533,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "74f745f9-2b95-4efa-9599-7cd8a383fdc4",
      "currency" : "USD",
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "source" : "PIgD8LQDKYZoWifmwnySHeSz",
      "destination" : "PIiJj9MbmJ39HrkqegnrNqos",
      "ready_to_settle_at" : null,
      "fee" : 18253,
      "statement_descriptor" : "FNX*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-11-04T18:12:15.89Z",
      "updated_at" : "2016-11-04T18:12:19.23Z",
      "merchant_identity" : "ID2vAEnEE63Sw6DP1Vhz4xou",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID2vAEnEE63Sw6DP1Vhz4xou"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRvrjUj9GNaAqPHEknwoCMoe/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIgD8LQDKYZoWifmwnySHeSz"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIiJj9MbmJ39HrkqegnrNqos"
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
    -u None:None \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

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
  "id" : "WHjum91z2Ag7kGC9uM6bQPbe",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "created_at" : "2016-11-04T18:12:01.86Z",
  "updated_at" : "2016-11-04T18:12:01.86Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHjum91z2Ag7kGC9uM6bQPbe"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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



curl https://api-staging.finix.io/webhooks/WHjum91z2Ag7kGC9uM6bQPbe \
    -H "Content-Type: application/vnd.json+api" \
    -u None:None


```
```python



```
> Example Response:

```json
{
  "id" : "WHjum91z2Ag7kGC9uM6bQPbe",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
  "created_at" : "2016-11-04T18:12:01.86Z",
  "updated_at" : "2016-11-04T18:12:01.86Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHjum91z2Ag7kGC9uM6bQPbe"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
    -u  None:None

```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHjum91z2Ag7kGC9uM6bQPbe",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APkXv4H4EFsN2XDqHHgDHvCH",
      "created_at" : "2016-11-04T18:12:01.86Z",
      "updated_at" : "2016-11-04T18:12:01.86Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHjum91z2Ag7kGC9uM6bQPbe"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APkXv4H4EFsN2XDqHHgDHvCH"
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
