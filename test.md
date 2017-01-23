---
title: Payline API Reference

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
```shell


# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c

```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
These guides provide a collection of resources for utilizing the Payline API and its client libraries.

1. [Quickstart](#quickstart): This guide explains the basic workflow of charging a card via the API.

2. [Tokenization.js](#tokenization-js): This guide explains how to properly tokenize cards in production via our javascript client to remain out of PCI scope

We offer a number of client libraries for interfacing with the API, and you view example code snippets for each in the dark area to the right.

## Authentication

To communicate with the Payline API you'll need to authenticate your requests with a `username` and `password`. To test the API against the sandbox environment feel free to use the credentials below:

- Username: `UStd1ZKrErMGNZLTHVPsRGa6`

- Password: `c6acbab3-b269-4a84-862a-4e03762d084c`

You should also know your `Application` ID. An `Application`, also referred as an "App", is a resource that represents your web app. In other words, any web service that connects buyers (i.e. customers) and sellers (i.e. merchants). This guide uses the following sandbox `Application` ID:

- App ID: `APbGTAgkdigUhi9P3UW8fSXW`

These next few sections will show you step-by-step how to provision merchant accounts, tokenize cards, charge those cards, and finally settle (i.e. payout) those funds out to your merchants.

## Quickstart

### Step 1: Create an Identity for a Merchant

```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    },
	    "entity": {
	        "last_name": "Sunkhronos",
	        "amex_mid": "12345678910",
	        "max_transaction_amount": 120000,
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
	        "tax_id": "5779",
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
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
	        "tax_id"=> "5779",
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
	    "tags": {
	        "key": "value"
	    },
	    "created_at": "2016-06-24T20:51:13.23Z",
	    "updated_at": "2016-06-24T20:51:13.23Z",
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        "business_phone": "+1 (408) 756-4497",
	        "first_name": "dwayne",
	        "last_name": "Sunkhronos",
	        "amex_mid": "12345678910",
	        "title": "CEO",
	        "dob": {
	            "year": 1978,
	            "day": 27,
	            "month": 6
	        },
	        "default_statement_descriptor": "Petes Coffee",
	        "business_tax_id_provided": true,
	        "business_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 8",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "doing_business_as": "Petes Coffee",
	        "phone": "1234567890",
	        "discover_mid": null,
	        "url": "www.PetesCoffee.com",
	        "personal_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 7",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "business_name": "Petes Coffee",
	        "tax_id_provided": true,
	        "email": "user@example.org",
	        "short_business_name": null
	    },
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/settlements"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/payment_instruments"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/disputes"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/transfers"
	        },
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/merchants"
	        }
	    },
	    "id": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go in greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information
`POST https://https://api-test.payline.io/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)
`POST https://https://api-test.payline.io/payment_instruments/`

3. Finally, provision the `Merchant` account
`POST https://https://api-test.payline.io/identities/IDENTITY_ID/merchants`


Let's start with the first step by creating an `Identity` resource, which in many ways is the centerpiece for the payment API's architecture. Each `Identity` represents either a buyer or a merchant. We use this resource to associate cards, bank accounts, and transactions. This structure makes it simple to manage and reconcile a merchant's associated bank accounts, transaction history, and payouts. More importantly, the `Identity` resource is used to collect underwriting information for the business and its principal.

Let's create one now (look to the right for an example request). You'll want to store the ID of the newly created `Identity` resource as you'll reference it later.

### HTTP Request

`POST https://api-test.payline.io/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please inout first name, last name and middle initial)
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
first_name | *string*, **required** | First name of the merchant's principal representative
last_name | *string*, **required** | Last name of the merchant's principal representative
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
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf/)) that this merchant will be classified under
amex_mid | *string*, **required** |  American Express Merchant ID for enabling Amex's OptBlue processing (Length must be between 10 and 11 characters)
discover_mid | *string*, **optional** |  Discover Merchant ID
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
day | *integer*, **required** | Day business was incorporated
month | *integer*, **required** | Month business was incorporated
year | *string*, **required** | Year business was incorporated


#### DOB-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day of birth (between 1 and 31)
month | *integer*, **required** | Month of birth (between 1 and 12)
year | *string*, **required** | Year of birth (4-digit)

### Step 2: Tokenize a Bank Account for Settling (i.e. funding) your Merchant

```shell

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "account_type": "SAVINGS",
	    "name": "Fran Lemke",
	    "bank_code": "123123123",
	    "country": "USA",
	    "currency": "USD",
	    "account_number": "123123123",
	    "type": "BANK_ACCOUNT",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS",
	    "name"=> "Fran Lemke",
	    "bank_code"=> "123123123",
	    "country"=> "USA",
	    "currency"=> "USD",
	    "account_number"=> "123123123",
	    "type"=> "BANK_ACCOUNT",
	    "identity"=> "IDfdJzXCNJN3yRRHTszAXCyn"
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
	    "instrument_type": "BANK_ACCOUNT",
	    "masked_account_number": "XXXXX3123",
	    "name": "Fran Lemke",
	    "tags": {},
	    "country": "USA",
	    "created_at": "2016-06-24T20:51:26.35Z",
	    "bank_code": "123123123",
	    "updated_at": "2016-06-24T20:51:26.35Z",
	    "currency": "USD",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w"
	        },
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/authorizations"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/verifications"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "fingerprint": "FPR-1215770130",
	    "id": "PIw8g34pvjGMoedpPrUeGZ1w",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Now that we've created an `Identity` for our merchant, we'll need to add a bank account where we can settle out the funds that are processed on behalf of your merchant (i.e. their funding account).

In the API, bank accounts -- as well as credit cards -- are represented by the `Payment Instrument` resource. There are two means of creating a `Payment Instrument`: 1) directly via the API and 2) via our Tokenization.js library. For testing purposes, we'll create one directly via the API; however, please review our guide on how to tokenize payment instruments via the [tokenization.js library](#tokenization-js) when in production.

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>

To classify the `Payment Instrument` as a bank account you'll need to pass BANK_ACCOUNT in the `type` field of your request, and you'll also want to pass the ID of the `Identity` that you created in the last step via the `identity` field to properly associate it with your merchant.


### HTTP Request

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
company_name | *string*, **optional** | Name of the business if the account is a corporate account
country | *string*, **optional** | Country the account is registered (defaults to USA)
currency | *string*, **optional** | Currency the account is in (defaults to USD)

### Step 3: Provision Merchant Accountsadfadsfd

```shell

curl https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
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
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfdJzXCNJN3yRRHTszAXCyn');

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

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());
```

> Example Response:

```json

	{
	    "created_at": "2016-06-24T20:51:30.36Z",
	    "updated_at": "2016-06-24T20:51:30.36Z",
	    "id": "MUppksuMV6juqs3Rk8owdQPf",
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/merchants/MUppksuMV6juqs3Rk8owdQPf"
	        },
	        "merchant_profile": {
	            "href": "https://api-test.payline.io/merchant_profiles/MPvCs96xJLR92JFRqeEP1Bxo"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/merchants/MUppksuMV6juqs3Rk8owdQPf/verifications"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "verification": {
	            "href": "https://api-test.payline.io/verifications/VIcDL5vKm6s4LKhQ7KNocfZ7"
	        }
	    },
	    "verification": "VIcDL5vKm6s4LKhQ7KNocfZ7",
	    "underwriting_state": "PROVISIONING",
	    "merchant_profile": "MPvCs96xJLR92JFRqeEP1Bxo",
	    "processor": "DUMMY_V1",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Now that we've associated a `Payment Instrument` with our seller's `Identity` we're ready to provision a `Merchant` account. This is the last step before you can begin processing on their behalf. Luckily you've already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource. Take a second to inspect this newly created resource, particularly the `underwriting_state`, which can have 3 potential states:

1. `PROVISIONING`: Request is pending (state will typically change after two minutes)

2. `APPROVED`: Merchant has been approved and can begin processing

3. `REJECTED`: Merchant was rejected by the processor either because the collected underwriting information was invalid or it failed one a number of regulatory and compliance checks (e.g. KYC, OFAC or MATCH)

<aside class="notice">
Provisioning a `Merchant` account is an asynchronous request. We recommend creating a [Webhook](#webhooks) to listen for the state change.
</aside>


#### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/merchants`

##### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

### Step 4: Create an Identity for a Buyer

```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    },
	    "entity": {
	        "phone": "7145677613",
	        "first_name": "Fran",
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

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
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
	        "first_name"=> "Fran",
	        "last_name"=> "Kline",
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
	    "tags": {
	        "key": "value"
	    },
	    "created_at": "2016-06-24T20:51:32.21Z",
	    "updated_at": "2016-06-24T20:51:32.21Z",
	    "entity": {
	        "business_type": null,
	        "business_phone": null,
	        "first_name": "Fran",
	        "last_name": "Kline",
	        "amex_mid": null,
	        "title": null,
	        "dob": null,
	        "default_statement_descriptor": null,
	        "business_tax_id_provided": false,
	        "business_address": null,
	        "doing_business_as": null,
	        "phone": "7145677613",
	        "discover_mid": null,
	        "url": null,
	        "personal_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 7",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "business_name": null,
	        "tax_id_provided": false,
	        "email": "therock@gmail.com",
	        "short_business_name": null
	    },
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh"
	        },
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/settlements"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/payment_instruments"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/disputes"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/transfers"
	        },
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/merchants"
	        }
	    },
	    "id": "IDnhejvgoCNPX6HbD9fJBNzh"
	}
```

Now that we have successfully provisioned a `Merchant` we'll need to create an
`Identity` that represents your buyer. Don't worry tho you won't need to capture
the same amount of underwriting information from your buyer. **All the
fields are optional, so long as you don't pass a business_type field**. Passing
a business_type will introduce the underwriting form validators. Typically, we
suggest at least collecting the buyer's name and email to help with accounting,
reconciliation, and chargebacks.

### HTTP Request

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
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "name": "Jessie Chang",
	    "expiration_year": 2020,
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
	    "identity": "IDnhejvgoCNPX6HbD9fJBNzh"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Jessie Chang",
	    "expiration_year"=> 2020,
	    "number"=> "4242424242424242",
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
	    "identity"=> "IDnhejvgoCNPX6HbD9fJBNzh"
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
	    "instrument_type": "PAYMENT_CARD",
	    "card_type": "UNKNOWN",
	    "name": "Jessie Chang",
	    "expiration_year": 2020,
	    "tags": {},
	    "brand": "VISA",
	    "address": {
	        "city": "San Mateo",
	        "country": "USA",
	        "region": "CA",
	        "line2": "Apartment 7",
	        "line1": "741 Douglass St",
	        "postal_code": "94114"
	    },
	    "updated_at": "2016-06-24T20:51:33.68Z",
	    "expiration_month": 12,
	    "security_code_verification": "UNKNOWN",
	    "address_verification": "UNKNOWN",
	    "last_four": "4242",
	    "fingerprint": "FPR-797428441",
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/transfers"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh"
	        },
	        "updates": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/updates"
	        }
	    },
	    "created_at": "2016-06-24T20:51:33.68Z",
	    "id": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "identity": "IDnhejvgoCNPX6HbD9fJBNzh"
	}
```

Now that we have an `Identity` resource representing our buyer, we'll need to
create a `Payment Instrument` which represents the credit card you'll be debiting.
Note you'll need to interpolate your own buyer's `Identity` ID from the
previous request to properly associate it.

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
You must use the Tokenization.js library to remain out of PCI scope.
</aside>

Please review our guide on how to tokenize cards via the [tokenization.js library.](#tokenization-js)

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
identity | *string*, **required** | ID of the `Identity` that the card should be associated
type | *string*, **required** | Type of Payment Instrument (for cards input PAYMENT_CARD)
number | *string*, **required** | The digits of the credit card integer
security_code | *string*, **optional** | The 3-4 digit security code for the card
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | 4-digit expiration year
name | *string*, **optional** | Full name of the registered card holder
address | *string*, **optional** | Billing address (Full description of child attributes below)


#### Address-object Request Arguments

line1 | *string*, **optional** | First line of the address
line2 | *string*, **optional** | Second line of the address
city | *string*, **optional** | City
region | *string*, **optional** | State
postal_code | *string*, **optional** | Zip or Postal code
country | *string*, **optional** | 3-Letter Country code


### Step 6: Create a Transfer (i.e. debit the card)
```shell


curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency": "USD",
	    "amount": 811607,
	    "fee": 81161,
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "merchant_identity"=> "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency"=> "USD",
	    "amount"=> 811607,
	    "fee"=> 81161,
	    "source"=> "PI99jSCNqdqK7RQPaf9Css4Y"
	));
$debit = $debit->save();
```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```

> Example Response:

```json

	{
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "destination": "PIvVQiEDnHqU5vAsZ3rbWxDR",
	    "state": "PENDING",
	    "updated_at": "2016-06-24T20:51:35.60Z",
	    "created_at": "2016-06-24T20:51:35.43Z",
	    "tags": {},
	    "trace_id": "61be2142-3045-488a-b9b8-c43ebfc61087",
	    "statement_descriptor": "PLD*PETES COFFEE",
	    "currency": "USD",
	    "amount": 811607,
	    "fee": 81161,
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/reversals"
	        },
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe"
	        },
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvVQiEDnHqU5vAsZ3rbWxDR"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/payment_instruments"
	        },
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/disputes"
	        }
	    },
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "type": "DEBIT",
	    "id": "TR9ZWBgVr4xFTvBURqesRADe"
	}
```

At this point we've created resources representing the merchant, the buyer, and
the buyer's card.

To debit a card, you'll need to create a `Transfer`. What's a `Transfer`? Glad
you asked! A `Transfer` is basically any flow of funds from one
`Payment Instrument`. In other words, a `Transfer` can be charging a card,
issuing a credit to a bank account or a refund. For now let's focus on charging
a card.

To do this we'll supply the buyer's `Payment Instrument` ID as the source and
the seller's `Identity` ID as the merchant_identity. Note that the 'amount'
field is in cents. The `fee` field is the amount in cents you would like to
keep before settling out to the merchant. For example, if you're charging your
 buyer $100 on behalf of your merchant, and you're charging a %10 service fee
for using your marketplace you'll want to pass $100 as the `amount` and $10 as
the `fee`. This way when the funds are eventually settled out only $90 will be
disbursed to your merchant.

Simple enough, right? You'll also want to store the ID from that `Transfer` for
your records. Next we're going to show you how to settle out the funds to your
merchant.


### HTTP Request

`POST https://api-test.payline.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be charged in cents (e.g., 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the transfer you would like to collect as your fee (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the transfer (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Settle out funds to a Merchant
```shell

curl https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "currency": "USD",
	    "processor": "DUMMY_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDfdJzXCNJN3yRRHTszAXCyn');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD",
	    "processor"=> "DUMMY_V1"
	));

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```
> Example Response:

```json

	{
	    "total_amount": 1700495,
	    "tags": {},
	    "transfer": null,
	    "created_at": "2016-06-24T20:54:18.30Z",
	    "updated_at": "2016-06-24T20:54:18.32Z",
	    "processor": "DUMMY_V1",
	    "currency": "USD",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "total_fee": 0,
	    "id": "STmXHfHYiD7i2tT7tdNcuhDC",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Awesome! Now you know how to charge a card. Next you need to settle out the
funds to your merchant. To do so you will create a `Settlement` resource. Each
settlement is comprised of all the `Transfers` that have a SUCCEEDED state and
that have not been previously settled out. In addition, `Settlements` will deduct
 any refunded amounts. In other words, if a merchant has a `Transfer` in the
 PENDING state it will not be included in the batch settlement. The
 `total_amount` is the net settled out amount in cents (i.e. the amount in cents
 that will be deposited into your merchant's bank account after your fees have
 been deducted).

<aside class="notice">
To view all the `Transfers` that were included in a `Settlement` you can make a
request to the 'transfers' link (i.e. `POST https://api-test.payline.io/settlements/:settlement_id/transfers`
</aside>

 ### HTTP Request

 `POST https://api-test.payline.io/identities/:identity_id/settlements`

 #### Request Arguments

 Field | Type | Description
 ----- | ---- | -----------
 currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
 tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Tokenization.js
To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js, keeps you out of the PCI scope by sending sensitive payment information over SSL directly to the Payline servers.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/sab76Lne/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Payline API.
</aside>


### Step 1: Include library

To use tokenization.js you will first need to include the library. Please include the script tag as demonstrated to the right.

```html
<script type="text/javascript" src="https://js.verygoodproxy.com/tokenization.1-latest.js"></script>


<aside class="notice">
Note that we do not recommend hosting the tokenization.js library locally as doing so prevents important updates.
</aside>
```

### Step 2: Create a form

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


Before collecting the sensitive payment information, we will need to construct an HTML form for users to input the data.

We have provided a simple example to the right for capturing Payment Instrument data.

### Step 3: Configure and initialize

```javascript
var initTokenization = function() {
  Tokenization.init({
    server: "https://api-test.payline.io",
    applicationId: "APbGTAgkdigUhi9P3UW8fSXW",
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



We will need to configure the client so that it POSTs to the correct endpoint and associates the Payment Instrument to your application. During the initialization we will also use the JQuery selector method to capture the form data.

#### Initialization Fields
Field | Type | Description | Example
----- | ---- | ----------- | -------
server | *string*, **required** |  The base url for the Payline API| https://api-test.payline.io
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | APbGTAgkdigUhi9P3UW8fSXW
hosted_fields | *object*, **required** |  An object containing the payment instrument information collected from your form.  | Johnson

#### hosted_fields object for card
Field | Type | Description | Example
----- | ---- | ----------- | -------
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020

#### hosted_fields object for bankAccount
Field | Type | Description | Example
----- | ---- | ----------- | -------
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124


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

> Example Tokenization Response:
```json
{
    "id": "TKniysXmtYV1astMC1jyZN8E",
    "fingerprint": "FPR-1392097976",
    "created_at": "2016-03-07T22:27:01.611",
    "updated_at": "2016-03-07T22:27:01.611",
    "instrument_type": "PAYMENT_CARD"
}
```

Finally we will need to register a click event that fires when our users submit the form and define a callback for handling the tokenization.js response. We have included an example to the right.

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

Great now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server. You can expand on the callback that you previously created like so:

### Step 6: Associate to an Identity


```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d "
	{
	    "token": "TKniysXmtYV1astMC1jyZN8E",
	    "type": "TOKEN",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}"
```

> Example Response:

```json

	{
	    "instrument_type": "TOKEN",
	    "tags": {},
	    "created_at": "2016-06-24T20:54:24.47Z",
	    "updated_at": "2016-06-24T20:54:24.47Z",
	    "token": "TKniysXmtYV1astMC1jyZN8E",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PI72BFgTKD1rrWCWwkxojWo8/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PI72BFgTKD1rrWCWwkxojWo8"
	        },
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PI72BFgTKD1rrWCWwkxojWo8/authorizations"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PI72BFgTKD1rrWCWwkxojWo8/verifications"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "fingerprint": "FPR536576269",
	    "id": "PI72BFgTKD1rrWCWwkxojWo8",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Before you can use the newly tokenized card or bank account you will need to associate it with an Identity. To do this you must make an authenticated POST request to `https://api-test.payline.io/payment_instruments` like demonstrated to the right.

#### HTTP Request

`POST https://api-test.payline.io/payment_instruments`
# Authorizations
An Authorization resource (also known as a card hold) reserves a specific amount on a card to be captured (debited) at a later date, usually within 7 days. When an Authorization is captured it produces a Transfer resource.


## Create an Authorization
```shell

curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency": "USD",
	    "amount": 100,
	    "processor": "DUMMY_V1",
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y"
	}'



```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency"=> "USD",
	    "amount"=> 100,
	    "processor"=> "DUMMY_V1",
	    "source"=> "PI99jSCNqdqK7RQPaf9Css4Y"
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
	    "tags": {},
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "transfer": null,
	    "created_at": "2016-06-24T20:53:12.48Z",
	    "trace_id": "ee9b261a-f137-485a-bb92-1138109cdde1",
	    "state": "SUCCEEDED",
	    "expires_at": "2016-07-01T20:53:12.48Z",
	    "updated_at": "2016-06-24T20:53:12.51Z",
	    "currency": "USD",
	    "amount": 100,
	    "is_void": false,
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU3qQRkPu58BGBboK6HR9cP5"
	        }
	    },
	    "id": "AU3qQRkPu58BGBboK6HR9cP5"
	}
```

### HTTP Request

`POST https://api-test.payline.io/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The Payment Instrument to debited.
merchant_identity | *string*, **required** | UID.
amount | *integer*, **required** | The amount of the debit in cents.

## Capture an Authorization

```shell

curl https://api-test.payline.io/authorizations/AU3qQRkPu58BGBboK6HR9cP5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -X PUT \
    -d '
	{
	    "fee": "10",
	    "void_me": null,
	    "statement_descriptor": "Bob's Burgers",
	    "capture_amount": 100
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU3qQRkPu58BGBboK6HR9cP5');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU3qQRkPu58BGBboK6HR9cP5");
authorization = authorization.capture(50L);

```
> Example Response:

```json

	{
	    "tags": {},
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "transfer": "TRhwDeD3mdDkwjjJAdx9gVgW",
	    "created_at": "2016-06-24T20:53:12.31Z",
	    "trace_id": "ee9b261a-f137-485a-bb92-1138109cdde1",
	    "state": "SUCCEEDED",
	    "expires_at": "2016-07-01T20:53:12.31Z",
	    "updated_at": "2016-06-24T20:53:12.31Z",
	    "currency": "USD",
	    "amount": 100,
	    "is_void": false,
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRhwDeD3mdDkwjjJAdx9gVgW"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU3qQRkPu58BGBboK6HR9cP5"
	        }
	    },
	    "id": "AU3qQRkPu58BGBboK6HR9cP5"
	}
```

### HTTP Request

`PUT https://api-test.payline.io/authorizations/authorization_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the authorization you would like to capture in cents. Must be less than or equal to the amount of the authorization
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less.
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount

## Retrieve an Authorization
```shell

curl https://api-test.payline.io/authorizations/AU3qQRkPu58BGBboK6HR9cP5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU3qQRkPu58BGBboK6HR9cP5');

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AU3qQRkPu58BGBboK6HR9cP5");

```
> Example Response:

```json

	{
	    "tags": {},
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "transfer": "TRhwDeD3mdDkwjjJAdx9gVgW",
	    "created_at": "2016-06-24T20:53:12.31Z",
	    "trace_id": "ee9b261a-f137-485a-bb92-1138109cdde1",
	    "state": "SUCCEEDED",
	    "expires_at": "2016-07-01T20:53:12.31Z",
	    "updated_at": "2016-06-24T20:53:12.31Z",
	    "currency": "USD",
	    "amount": 100,
	    "is_void": false,
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRhwDeD3mdDkwjjJAdx9gVgW"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU3qQRkPu58BGBboK6HR9cP5"
	        }
	    },
	    "id": "AU3qQRkPu58BGBboK6HR9cP5"
	}
```

### HTTP Request

`GET https://api-test.payline.io/authorizations/authorization_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


# Disputes
Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl https://api-test.payline.io/disputes/DIv8G3e2vkuiYUhRFUfLeL4C \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DIv8G3e2vkuiYUhRFUfLeL4C');

```
```java

import io.payline.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("DIv8G3e2vkuiYUhRFUfLeL4C");

```
> Example Response:

```json

	{
	    "state": "PENDING",
	    "transfer": "TRmvDpQ4oFRMmZaJHARX1ecG",
	    "created_at": "2016-06-24T20:52:01.23Z",
	    "tags": {},
	    "occurred_at": "2016-06-24T20:51:37.53Z",
	    "amount": 0,
	    "updated_at": "2016-06-24T20:52:01.23Z",
	    "reason": "FRAUD",
	    "_links": {
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRmvDpQ4oFRMmZaJHARX1ecG"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/disputes/DIv8G3e2vkuiYUhRFUfLeL4C"
	        },
	        "evidence": {
	            "href": "https://api-test.payline.io/disputes/DIv8G3e2vkuiYUhRFUfLeL4C/evidence"
	        }
	    },
	    "respond_by": "2016-07-01T20:52:01.41Z",
	    "id": "DIv8G3e2vkuiYUhRFUfLeL4C",
	    "identity": "IDnhejvgoCNPX6HbD9fJBNzh"
	}
```

### HTTP Request

`GET https://api-test.payline.io/disputes/dispute_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
dispute_id | ID of the Dispute

# Identities
An `Identity` resource represents either a buyer or a merchant, and is in many ways the centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must be associated with an `Identity`. For both buyers and merchants, this structure makes it easy to manage and reconcile their associated bank accounts, transaction history, and payouts.

For merchants, the `Identity` resource is used to collect underwriting information for the business and its principal.

## Create an Identity for a Buyer
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    },
	    "entity": {
	        "phone": "7145677613",
	        "first_name": "Fran",
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
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
	        "first_name"=> "Fran",
	        "last_name"=> "Kline",
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
	    "tags": {
	        "key": "value"
	    },
	    "created_at": "2016-06-24T20:51:32.21Z",
	    "updated_at": "2016-06-24T20:51:32.21Z",
	    "entity": {
	        "business_type": null,
	        "business_phone": null,
	        "first_name": "Fran",
	        "last_name": "Kline",
	        "amex_mid": null,
	        "title": null,
	        "dob": null,
	        "default_statement_descriptor": null,
	        "business_tax_id_provided": false,
	        "business_address": null,
	        "doing_business_as": null,
	        "phone": "7145677613",
	        "discover_mid": null,
	        "url": null,
	        "personal_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 7",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "business_name": null,
	        "tax_id_provided": false,
	        "email": "therock@gmail.com",
	        "short_business_name": null
	    },
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh"
	        },
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/settlements"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/payment_instruments"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/disputes"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/transfers"
	        },
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh/merchants"
	        }
	    },
	    "id": "IDnhejvgoCNPX6HbD9fJBNzh"
	}
```

### HTTP Request

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
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "tags": {
	        "key": "value"
	    },
	    "entity": {
	        "last_name": "Sunkhronos",
	        "amex_mid": "12345678910",
	        "max_transaction_amount": 120000,
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
	        "tax_id": "5779",
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
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
	        "tax_id"=> "5779",
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
	    "tags": {
	        "key": "value"
	    },
	    "created_at": "2016-06-24T20:51:13.23Z",
	    "updated_at": "2016-06-24T20:51:13.23Z",
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        "business_phone": "+1 (408) 756-4497",
	        "first_name": "dwayne",
	        "last_name": "Sunkhronos",
	        "amex_mid": "12345678910",
	        "title": "CEO",
	        "dob": {
	            "year": 1978,
	            "day": 27,
	            "month": 6
	        },
	        "default_statement_descriptor": "Petes Coffee",
	        "business_tax_id_provided": true,
	        "business_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 8",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "doing_business_as": "Petes Coffee",
	        "phone": "1234567890",
	        "discover_mid": null,
	        "url": "www.PetesCoffee.com",
	        "personal_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 7",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "business_name": "Petes Coffee",
	        "tax_id_provided": true,
	        "email": "user@example.org",
	        "short_business_name": null
	    },
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/settlements"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/payment_instruments"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/disputes"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/transfers"
	        },
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/merchants"
	        }
	    },
	    "id": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

### HTTP Request

`POST https://api-test.payline.io/identities`

#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please inout first name, last name and middle initial)
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
first_name | *string*, **required** | First name of the merchant's principal representative
last_name | *string*, **required** | Last name of the merchant's principal representative
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
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf/)) that this merchant will be classified under
amex_mid | *string*, **required** |  American Express Merchant ID for enabling Amex's OptBlue processing (Length must be between 10 and 11 characters)
discover_mid | *string*, **optional** |  Discover Merchant ID
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
day | *integer*, **required** | Day business was incorporated
month | *integer*, **required** | Month business was incorporated
year | *string*, **required** | Year business was incorporated


#### DOB-object Request Arguments

Field | Type | Description
----- | ---- | -----------
day | *integer*, **required** | Day of birth (between 1 and 31)
month | *integer*, **required** | Month of birth (between 1 and 12)
year | *string*, **required** | Year of birth (4-digit)
## Retrieve a Identity
```shell

curl https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfdJzXCNJN3yRRHTszAXCyn');
```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDfdJzXCNJN3yRRHTszAXCyn");

```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    },
	    "created_at": "2016-06-24T20:51:13.16Z",
	    "updated_at": "2016-06-24T20:51:13.16Z",
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        "business_phone": "+1 (408) 756-4497",
	        "first_name": "dwayne",
	        "last_name": "Sunkhronos",
	        "amex_mid": "12345678910",
	        "title": "CEO",
	        "dob": {
	            "year": 1978,
	            "day": 27,
	            "month": 6
	        },
	        "default_statement_descriptor": "Petes Coffee",
	        "business_tax_id_provided": true,
	        "business_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 8",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "doing_business_as": "Petes Coffee",
	        "phone": "1234567890",
	        "discover_mid": null,
	        "url": "www.PetesCoffee.com",
	        "personal_address": {
	            "city": "San Mateo",
	            "country": "USA",
	            "region": "CA",
	            "line2": "Apartment 7",
	            "line1": "741 Douglass St",
	            "postal_code": "94114"
	        },
	        "business_name": "Petes Coffee",
	        "tax_id_provided": true,
	        "email": "user@example.org",
	        "short_business_name": null
	    },
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/settlements"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/payment_instruments"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/disputes"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/transfers"
	        },
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/merchants"
	        }
	    },
	    "id": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

### HTTP Request

`GET https://api-test.payline.io/identities/identity_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

## Provision a Merchant

```shell

curl https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
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
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDfdJzXCNJN3yRRHTszAXCyn');

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
	    "created_at": "2016-06-24T20:51:30.36Z",
	    "updated_at": "2016-06-24T20:51:30.36Z",
	    "id": "MUppksuMV6juqs3Rk8owdQPf",
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/merchants/MUppksuMV6juqs3Rk8owdQPf"
	        },
	        "merchant_profile": {
	            "href": "https://api-test.payline.io/merchant_profiles/MPvCs96xJLR92JFRqeEP1Bxo"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/merchants/MUppksuMV6juqs3Rk8owdQPf/verifications"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "verification": {
	            "href": "https://api-test.payline.io/verifications/VIcDL5vKm6s4LKhQ7KNocfZ7"
	        }
	    },
	    "verification": "VIcDL5vKm6s4LKhQ7KNocfZ7",
	    "underwriting_state": "PROVISIONING",
	    "merchant_profile": "MPvCs96xJLR92JFRqeEP1Bxo",
	    "processor": "DUMMY_V1",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Provision a Merchant created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


# Settlements
A Settlement resource represents a collection of Transfers that are to be paid out to a specific Merchant.


## Create a Settlement
```shell

curl https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "currency": "USD",
	    "processor": "DUMMY_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDfdJzXCNJN3yRRHTszAXCyn');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD",
	    "processor"=> "DUMMY_V1"
	));

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
)

```


> Example Response:

```json

	{
	    "total_amount": 1700495,
	    "tags": {},
	    "transfer": null,
	    "created_at": "2016-06-24T20:54:18.30Z",
	    "updated_at": "2016-06-24T20:54:18.32Z",
	    "processor": "DUMMY_V1",
	    "currency": "USD",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "total_fee": 0,
	    "id": "STmXHfHYiD7i2tT7tdNcuhDC",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```


 ### HTTP Request

 `POST https://api-test.payline.io/identities/:identity_id/settlements`

 #### Request Arguments

 Field | Type | Description
 ----- | ---- | -----------
 currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
 tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Fetch a Settlement

```shell


curl https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STmXHfHYiD7i2tT7tdNcuhDC');

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STmXHfHYiD7i2tT7tdNcuhDC");

```
> Example Response:

```json

	{
	    "total_amount": 1700495,
	    "tags": {},
	    "transfer": null,
	    "created_at": "2016-06-24T20:54:18.17Z",
	    "updated_at": "2016-06-24T20:54:18.17Z",
	    "processor": "DUMMY_V1",
	    "currency": "USD",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STmXHfHYiD7i2tT7tdNcuhDC"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "total_fee": 0,
	    "id": "STmXHfHYiD7i2tT7tdNcuhDC",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```

Fetch a previously created Settlement.

### HTTP Request

`POST https://api-test.payline.io/settlements/settlement_id/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
settlement_id | ID of the Settlment

# Transfers
A Transfer resource represents any omnidirectional flow of funds. Transfers can represent either a debit to a card, a credit to a bank account, or a refund to a card depending on the request. Transfers have a state attribute representing the current state of the transaction. There are three possible status values: PENDING, SUCCEEDED, or FAILED.

## Debit a Card

```shell


curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency": "USD",
	    "amount": 811607,
	    "fee": 81161,
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "merchant_identity"=> "IDfdJzXCNJN3yRRHTszAXCyn",
	    "currency"=> "USD",
	    "amount"=> 811607,
	    "fee"=> 81161,
	    "source"=> "PI99jSCNqdqK7RQPaf9Css4Y"
	));
$debit = $debit->save();
```
```java

import io.payline.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```


> Example Response:

```json

	{
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "destination": "PIvVQiEDnHqU5vAsZ3rbWxDR",
	    "state": "PENDING",
	    "updated_at": "2016-06-24T20:51:35.60Z",
	    "created_at": "2016-06-24T20:51:35.43Z",
	    "tags": {},
	    "trace_id": "61be2142-3045-488a-b9b8-c43ebfc61087",
	    "statement_descriptor": "PLD*PETES COFFEE",
	    "currency": "USD",
	    "amount": 811607,
	    "fee": 81161,
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/reversals"
	        },
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe"
	        },
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvVQiEDnHqU5vAsZ3rbWxDR"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/payment_instruments"
	        },
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/disputes"
	        }
	    },
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "type": "DEBIT",
	    "id": "TR9ZWBgVr4xFTvBURqesRADe"
	}
```

A `Transfer` consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST https://api-test.payline.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be charged in cents (e.g., 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the transfer you would like to collect as your fee (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the transfer (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Refund a Debit
```shell

curl https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
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
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TR9ZWBgVr4xFTvBURqesRADe');
$refund = $debit->reverse(50);
```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```


> Example Response:

```json

	{
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "destination": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "state": "PENDING",
	    "updated_at": "2016-06-24T20:53:10.79Z",
	    "created_at": "2016-06-24T20:53:10.63Z",
	    "tags": {},
	    "trace_id": "041a1bed-d7e5-4443-b87b-479bcf293ee3",
	    "statement_descriptor": "PLD*PETES COFFEE",
	    "currency": "USD",
	    "amount": 100,
	    "fee": 0,
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TRs8YcNwmPrV3AL4YbKKFYcy"
	        },
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TRs8YcNwmPrV3AL4YbKKFYcy/payment_instruments"
	        },
	        "parent": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe"
	        }
	    },
	    "source": "PIvVQiEDnHqU5vAsZ3rbWxDR",
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "type": "REVERSAL",
	    "id": "TRs8YcNwmPrV3AL4YbKKFYcy"
	}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

### HTTP Request

`POST https://api-test.payline.io/transfers/transfer_id/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | The amount of the refund in cents. Must be equal to or less than the amount of the original debit

## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TR9ZWBgVr4xFTvBURqesRADe');



```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR9ZWBgVr4xFTvBURqesRADe");

```
> Example Response:

```json

	{
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "destination": "PIvVQiEDnHqU5vAsZ3rbWxDR",
	    "state": "SUCCEEDED",
	    "updated_at": "2016-06-24T20:51:35.25Z",
	    "created_at": "2016-06-24T20:51:35.25Z",
	    "tags": {},
	    "trace_id": "61be2142-3045-488a-b9b8-c43ebfc61087",
	    "statement_descriptor": "PLD*PETES COFFEE",
	    "currency": "USD",
	    "amount": 811607,
	    "fee": 81161,
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/reversals"
	        },
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe"
	        },
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvVQiEDnHqU5vAsZ3rbWxDR"
	        },
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/payment_instruments"
	        },
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR9ZWBgVr4xFTvBURqesRADe/disputes"
	        }
	    },
	    "source": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "merchant_identity": "IDfdJzXCNJN3yRRHTszAXCyn",
	    "type": "DEBIT",
	    "id": "TR9ZWBgVr4xFTvBURqesRADe"
	}
```

### HTTP Request

`GET https://api-test.payline.io/transfers/transfer_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the Transfer


# Webhooks
Webhooks allow you to build or set up integrations which subscribe to certain events on the Payline API. When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL. Webhooks are particularly useful for updating asynchronous state changes in Transfers or notifications of newly created Disputes.

## Create a Webhook
```shell

curl https://api-test.payline.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	            {
	            "url" : "http://requestb.in/vts8mpvt"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
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
	    "url": "http://requestb.in/vts8mpvt",
	    "created_at": "2016-06-24T20:51:12.10Z",
	    "enabled": true,
	    "updated_at": "2016-06-24T20:51:12.10Z",
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/webhooks/WHcWu8MmnyrppBarsdtfLKWB"
	        }
	    },
	    "id": "WHcWu8MmnyrppBarsdtfLKWB"
	}
```

### HTTP Request

`POST https://api-test.payline.io/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request


## Retrieve a Webhook

```shell



curl https://api-test.payline.io/webhooks/WHcWu8MmnyrppBarsdtfLKWB \
    -H "Content-Type: application/vnd.json+api" \
    -u UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHcWu8MmnyrppBarsdtfLKWB');



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHcWu8MmnyrppBarsdtfLKWB");

```

> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt",
	    "created_at": "2016-06-24T20:51:12.09Z",
	    "enabled": true,
	    "updated_at": "2016-06-24T20:51:12.09Z",
	    "application": "APbGTAgkdigUhi9P3UW8fSXW",
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/webhooks/WHcWu8MmnyrppBarsdtfLKWB"
	        }
	    },
	    "id": "WHcWu8MmnyrppBarsdtfLKWB"
	}
```

### HTTP Request

`GET https://api-test.payline.io/webhooks/webhook_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
webhook_id | ID of the Webhook

# Payment Instruments
A Payment Instrument resource represents either a credit card or bank account. All information is securely vaulted and referenced by an ID. A Payment Instrument may be created multiple times, and each tokenization produces a unique ID. Each ID may only be associated one time and to only one Identity. Once associated, a Payment Instrument may not be disassociated from an Identity.


## Create a Card
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "name": "Jessie Chang",
	    "expiration_year": 2020,
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
	    "identity": "IDnhejvgoCNPX6HbD9fJBNzh"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Jessie Chang",
	    "expiration_year"=> 2020,
	    "number"=> "4242424242424242",
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
	    "identity"=> "IDnhejvgoCNPX6HbD9fJBNzh"
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
	    "instrument_type": "PAYMENT_CARD",
	    "card_type": "UNKNOWN",
	    "name": "Jessie Chang",
	    "expiration_year": 2020,
	    "tags": {},
	    "brand": "VISA",
	    "address": {
	        "city": "San Mateo",
	        "country": "USA",
	        "region": "CA",
	        "line2": "Apartment 7",
	        "line1": "741 Douglass St",
	        "postal_code": "94114"
	    },
	    "updated_at": "2016-06-24T20:51:33.68Z",
	    "expiration_month": 12,
	    "security_code_verification": "UNKNOWN",
	    "address_verification": "UNKNOWN",
	    "last_four": "4242",
	    "fingerprint": "FPR-797428441",
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/authorizations"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/verifications"
	        },
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/transfers"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDnhejvgoCNPX6HbD9fJBNzh"
	        },
	        "updates": {
	            "href": "https://api-test.payline.io/payment_instruments/PI99jSCNqdqK7RQPaf9Css4Y/updates"
	        }
	    },
	    "created_at": "2016-06-24T20:51:33.68Z",
	    "id": "PI99jSCNqdqK7RQPaf9Css4Y",
	    "identity": "IDnhejvgoCNPX6HbD9fJBNzh"
	}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
identity | *string*, **required** | ID of the `Identity` that the card should be associated
type | *string*, **required** | Type of Payment Instrument (for cards input PAYMENT_CARD)
number | *string*, **required** | The digits of the credit card integer
security_code | *string*, **optional** | The 3-4 digit security code for the card
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December)
expiration_year | *integer*, **required** | 4-digit expiration year
name | *string*, **optional** | Full name of the registered card holder
address | *string*, **optional** | Billing address (Full description of child attributes below)


#### Address-object Request Arguments

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
    -u  UStd1ZKrErMGNZLTHVPsRGa6:c6acbab3-b269-4a84-862a-4e03762d084c \
    -d '
	{
	    "account_type": "SAVINGS",
	    "name": "Fran Lemke",
	    "bank_code": "123123123",
	    "country": "USA",
	    "currency": "USD",
	    "account_number": "123123123",
	    "type": "BANK_ACCOUNT",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'UStd1ZKrErMGNZLTHVPsRGa6', 'c6acbab3-b269-4a84-862a-4e03762d084c');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS",
	    "name"=> "Fran Lemke",
	    "bank_code"=> "123123123",
	    "country"=> "USA",
	    "currency"=> "USD",
	    "account_number"=> "123123123",
	    "type"=> "BANK_ACCOUNT",
	    "identity"=> "IDfdJzXCNJN3yRRHTszAXCyn"
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
	    "instrument_type": "BANK_ACCOUNT",
	    "masked_account_number": "XXXXX3123",
	    "name": "Fran Lemke",
	    "tags": {},
	    "country": "USA",
	    "created_at": "2016-06-24T20:51:26.35Z",
	    "bank_code": "123123123",
	    "updated_at": "2016-06-24T20:51:26.35Z",
	    "currency": "USD",
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/transfers"
	        },
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w"
	        },
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/authorizations"
	        },
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PIw8g34pvjGMoedpPrUeGZ1w/verifications"
	        },
	        "identity": {
	            "href": "https://api-test.payline.io/identities/IDfdJzXCNJN3yRRHTszAXCyn"
	        }
	    },
	    "fingerprint": "FPR-1215770130",
	    "id": "PIw8g34pvjGMoedpPrUeGZ1w",
	    "identity": "IDfdJzXCNJN3yRRHTszAXCyn"
	}
```
<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize payment instruments via the [tokenization.js library](#tokenization-js)

### HTTP Request

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
company_name | *string*, **optional** | Name of the business if the account is a corporate account
country | *string*, **optional** | Country the account is registered (defaults to USA)
currency | *string*, **optional** | Currency the account is in (defaults to USD)

