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
## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	        "default_statement_descriptor"=> "Lees Sandwiches", 
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
	        "doing_business_as"=> "Lees Sandwiches", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Lees Sandwiches", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.LeesSandwiches.com", 
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
  "id" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T18:45:29.00Z",
  "updated_at" : "2016-09-09T18:45:29.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	    "identity"=> "IDd5PnWSt5y8tvBqu719VHYZ"
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
  "id" : "PIcbZthtnNww2dipdgpcs5nf",
  "fingerprint" : "FPR966610431",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T18:45:40.37Z",
  "updated_at" : "2016-09-09T18:45:40.37Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDd5PnWSt5y8tvBqu719VHYZ');

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
  "id" : "MU9iTMjWWyim756AgDXFt2Um",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "verification" : "VIk9qKq4XJQVfQ4S1aGJ7mJi",
  "merchant_profile" : "MP45GorF66TgYmo3zMypEgYB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-09-09T18:45:42.84Z",
  "updated_at" : "2016-09-09T18:45:42.84Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU9iTMjWWyim756AgDXFt2Um"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU9iTMjWWyim756AgDXFt2Um/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP45GorF66TgYmo3zMypEgYB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIk9qKq4XJQVfQ4S1aGJ7mJi"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	        "first_name"=> "Jessie", 
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
  "id" : "IDhErR8YpyVQRUvGZxt7Wmft",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-09-09T18:45:45.06Z",
  "updated_at" : "2016-09-09T18:45:45.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "name": "Maggie Chang", 
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
	    "identity": "IDhErR8YpyVQRUvGZxt7Wmft"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Maggie Chang", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
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
	    "identity"=> "IDhErR8YpyVQRUvGZxt7Wmft"
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
  "id" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "fingerprint" : "FPR-1299301881",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Chang",
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
  "created_at" : "2016-09-09T18:45:46.12Z",
  "updated_at" : "2016-09-09T18:45:46.12Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDhErR8YpyVQRUvGZxt7Wmft",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/updates"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "merchant_identity": "IDd5PnWSt5y8tvBqu719VHYZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIm5XghDC7k81Jr3C1GNRqAS", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDd5PnWSt5y8tvBqu719VHYZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIm5XghDC7k81Jr3C1GNRqAS", 
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
  "id" : "AUrtDS7exVgd6YEHysCAXTgj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:56.98Z",
  "updated_at" : "2016-09-09T18:45:57.05Z",
  "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : false,
  "expires_at" : "2016-09-16T18:45:56.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

### Step 6: Create an Authorization
```shell
curl https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUrtDS7exVgd6YEHysCAXTgj');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();

```
```java
import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUrtDS7exVgd6YEHysCAXTgj");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUrtDS7exVgd6YEHysCAXTgj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRu5iEGHBmqwuw4C51gpjstt",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:56.82Z",
  "updated_at" : "2016-09-09T18:45:58.85Z",
  "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : false,
  "expires_at" : "2016-09-16T18:45:56.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

### Step 7: Create a Batch Settlment
```shell
curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDd5PnWSt5y8tvBqu719VHYZ');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
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
  "id" : "STqDkJBWWbnBJwvAns1UXQFM",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "currency" : "USD",
  "created_at" : "2016-09-09T18:57:15.69Z",
  "updated_at" : "2016-09-09T18:57:15.80Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2047681,
  "total_fee" : 204769,
  "net_amount" : 1842912,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

`POST https://api-test.payline.io/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Embedded Tokenization Using Iframe

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to Payline. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

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
          applicationId: 'APdNpPsNNG1L3Ayp5ZBDV1FD',
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
  "id" : "TKqiqq2WMdrcwzP3VYSaXgED",
  "fingerprint" : "FPR222704565",
  "created_at" : "2016-09-09T18:46:01.06Z",
  "updated_at" : "2016-09-09T18:46:01.06Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-09-10T18:46:01.04Z",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    }
  }
}
```


```shell

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```

# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "merchant_identity": "IDd5PnWSt5y8tvBqu719VHYZ", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIm5XghDC7k81Jr3C1GNRqAS", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDd5PnWSt5y8tvBqu719VHYZ", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIm5XghDC7k81Jr3C1GNRqAS", 
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
  "id" : "AUrtDS7exVgd6YEHysCAXTgj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:56.98Z",
  "updated_at" : "2016-09-09T18:45:57.05Z",
  "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : false,
  "expires_at" : "2016-09-16T18:45:56.98Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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
curl https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUrtDS7exVgd6YEHysCAXTgj');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUrtDS7exVgd6YEHysCAXTgj");
authorization = authorization.capture(50L);

```
> Example Response:

```json
{
  "id" : "AUrtDS7exVgd6YEHysCAXTgj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRu5iEGHBmqwuw4C51gpjstt",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:56.82Z",
  "updated_at" : "2016-09-09T18:45:58.85Z",
  "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : false,
  "expires_at" : "2016-09-16T18:45:56.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

curl https://api-test.payline.io/authorizations/AUqP9bUxpPVq5N8brsELLUNp \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "AUqP9bUxpPVq5N8brsELLUNp",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:46:03.60Z",
  "updated_at" : "2016-09-09T18:46:05.06Z",
  "trace_id" : "3dd4e266-0092-4783-8584-5c2b3f842580",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : true,
  "expires_at" : "2016-09-16T18:46:03.60Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUqP9bUxpPVq5N8brsELLUNp"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

curl https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUrtDS7exVgd6YEHysCAXTgj');

```
```java

import io.payline.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUrtDS7exVgd6YEHysCAXTgj");

```
> Example Response:

```json
{
  "id" : "AUrtDS7exVgd6YEHysCAXTgj",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRu5iEGHBmqwuw4C51gpjstt",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:56.82Z",
  "updated_at" : "2016-09-09T18:45:58.85Z",
  "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "is_void" : false,
  "expires_at" : "2016-09-16T18:45:56.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
```
import io.payline.payments.processing.client.model.Authorization;

client.authorizationsClient().<Resources<Authorization>>resourcesIterator()
  .forEachRemaining(page-> {
    Collection<Authorization> authorizations = page.getContent();
    //do something
  });
```
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AUqP9bUxpPVq5N8brsELLUNp",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:46:03.60Z",
      "updated_at" : "2016-09-09T18:46:05.06Z",
      "trace_id" : "3dd4e266-0092-4783-8584-5c2b3f842580",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "is_void" : true,
      "expires_at" : "2016-09-16T18:46:03.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUqP9bUxpPVq5N8brsELLUNp"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        }
      }
    }, {
      "id" : "AUrtDS7exVgd6YEHysCAXTgj",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRu5iEGHBmqwuw4C51gpjstt",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:56.82Z",
      "updated_at" : "2016-09-09T18:45:58.85Z",
      "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "is_void" : false,
      "expires_at" : "2016-09-16T18:45:56.82Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/authorizations/AUrtDS7exVgd6YEHysCAXTgj"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "transfer" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

# Disputes

Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl https://api-test.payline.io/disputes/DIsex4QT7rncGZKVpYGJZGB1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DIsex4QT7rncGZKVpYGJZGB1');

```
```java

import io.payline.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("DIsex4QT7rncGZKVpYGJZGB1");

```
> Example Response:

```json
{
  "id" : "DIsex4QT7rncGZKVpYGJZGB1",
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "amount" : 0,
  "state" : "PENDING",
  "transfer" : "TRbo1SJa6R42Xuj3dm39buEg",
  "reason" : "FRAUD",
  "identity" : "IDhErR8YpyVQRUvGZxt7Wmft",
  "created_at" : "2016-09-09T18:47:01.35Z",
  "updated_at" : "2016-09-09T18:47:01.35Z",
  "occurred_at" : "2016-09-09T18:46:29.85Z",
  "respond_by" : "2016-09-16T18:47:01.65Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/disputes/DIsex4QT7rncGZKVpYGJZGB1"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfer" : {
      "href" : "https://api-test.payline.io/transfers/TRbo1SJa6R42Xuj3dm39buEg"
    },
    "evidence" : {
      "href" : "https://api-test.payline.io/disputes/DIsex4QT7rncGZKVpYGJZGB1/evidence"
    }
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/disputes/:DISPUTE_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:DISPUTE_ID | ID of the Dispute


## List all Disputes
```shell
curl https://api-test.payline.io/disputes/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
import io.payline.payments.processing.client.model.Dispute;

transfer.disputeClient().<Resources<Dispute>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Dispute> disputes = page.getContent();
  })
```
> Example Response:

```json
{
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/disputes?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 0
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/disputes/`


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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jessie", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	        "first_name"=> "Jessie", 
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
  "id" : "IDhErR8YpyVQRUvGZxt7Wmft",
  "entity" : {
    "title" : null,
    "first_name" : "Jessie",
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
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2016-09-09T18:45:45.06Z",
  "updated_at" : "2016-09-09T18:45:45.06Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
	        "default_statement_descriptor": "Lees Sandwiches", 
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
	        "doing_business_as": "Lees Sandwiches", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Lees Sandwiches", 
	        "tax_id": "123456789", 
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "url": "www.LeesSandwiches.com", 
	        "annual_card_volume": 12000000
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	        "default_statement_descriptor"=> "Lees Sandwiches", 
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
	        "doing_business_as"=> "Lees Sandwiches", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Lees Sandwiches", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.LeesSandwiches.com", 
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
  "id" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T18:45:29.00Z",
  "updated_at" : "2016-09-09T18:45:29.00Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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

curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDd5PnWSt5y8tvBqu719VHYZ');
```
```java

import io.payline.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDd5PnWSt5y8tvBqu719VHYZ");

```
> Example Response:

```json
{
  "id" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Lees Sandwiches",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2016-09-09T18:45:28.95Z",
  "updated_at" : "2016-09-09T18:45:28.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
      "id" : "IDhErR8YpyVQRUvGZxt7Wmft",
      "entity" : {
        "title" : null,
        "first_name" : "Jessie",
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
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2016-09-09T18:45:45.00Z",
      "updated_at" : "2016-09-09T18:45:45.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDdUZpVCw8FBFNKic2USUMq1",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Dunder Mifflin",
        "business_type" : "GOVERNMENT_AGENCY",
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
      "created_at" : "2016-09-09T18:45:39.14Z",
      "updated_at" : "2016-09-09T18:45:39.14Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDdUZpVCw8FBFNKic2USUMq1/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDewS2MY4siVocWGXLpYC3pi",
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
      "created_at" : "2016-09-09T18:45:38.04Z",
      "updated_at" : "2016-09-09T18:45:38.04Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDewS2MY4siVocWGXLpYC3pi/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDanmF8nUZcJ69FjeEKjXRD",
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
      "created_at" : "2016-09-09T18:45:36.96Z",
      "updated_at" : "2016-09-09T18:45:36.96Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDanmF8nUZcJ69FjeEKjXRD/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDuGAZWpbRry4BBPH976G8YM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
      "created_at" : "2016-09-09T18:45:35.85Z",
      "updated_at" : "2016-09-09T18:45:35.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDuGAZWpbRry4BBPH976G8YM/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDqYtAcSBhTMajyLgJioVFKz",
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
      "created_at" : "2016-09-09T18:45:34.78Z",
      "updated_at" : "2016-09-09T18:45:34.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDqYtAcSBhTMajyLgJioVFKz/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDBKziFmuYtj9qDJDEiEm9G",
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
      "created_at" : "2016-09-09T18:45:33.73Z",
      "updated_at" : "2016-09-09T18:45:33.73Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDBKziFmuYtj9qDJDEiEm9G/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDx4bftrYvHVHVEfdgpK7MS",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2016-09-09T18:45:32.52Z",
      "updated_at" : "2016-09-09T18:45:32.52Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDx4bftrYvHVHVEfdgpK7MS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDnPoV65aRUyMvUNrdnf4kH",
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
      "created_at" : "2016-09-09T18:45:31.33Z",
      "updated_at" : "2016-09-09T18:45:31.33Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDnPoV65aRUyMvUNrdnf4kH/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDmwV5UZDnm7PyiGNbFoe1hS",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "CORPORATION",
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
      "created_at" : "2016-09-09T18:45:30.06Z",
      "updated_at" : "2016-09-09T18:45:30.06Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDmwV5UZDnm7PyiGNbFoe1hS/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2016-09-09T18:45:28.95Z",
      "updated_at" : "2016-09-09T18:45:28.95Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "IDfUZyah9skwSWz1AWFh5LmX",
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
      "created_at" : "2016-09-09T18:45:19.87Z",
      "updated_at" : "2016-09-09T18:45:20.66Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/verifications"
        },
        "merchants" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/merchants"
        },
        "settlements" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX/disputes"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Walter", 
	        "last_name": "Lopez", 
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Walter",
    "last_name" : "Lopez",
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
  "created_at" : "2016-09-09T18:45:28.95Z",
  "updated_at" : "2016-09-09T18:46:26.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/verifications"
    },
    "merchants" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants"
    },
    "settlements" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/authorizations"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/disputes"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
 processor.](#update-merchant-information-on-processor)


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

curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDd5PnWSt5y8tvBqu719VHYZ');

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
  "id" : "MU9iTMjWWyim756AgDXFt2Um",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "verification" : "VIk9qKq4XJQVfQ4S1aGJ7mJi",
  "merchant_profile" : "MP45GorF66TgYmo3zMypEgYB",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2016-09-09T18:45:42.84Z",
  "updated_at" : "2016-09-09T18:45:42.84Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/merchants/MU9iTMjWWyim756AgDXFt2Um"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/merchants/MU9iTMjWWyim756AgDXFt2Um/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-test.payline.io/merchant_profiles/MP45GorF66TgYmo3zMypEgYB"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "verification" : {
      "href" : "https://api-test.payline.io/verifications/VIk9qKq4XJQVfQ4S1aGJ7mJi"
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


# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Settlement
```shell

curl https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDd5PnWSt5y8tvBqu719VHYZ');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
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
  "id" : "STqDkJBWWbnBJwvAns1UXQFM",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "currency" : "USD",
  "created_at" : "2016-09-09T18:57:15.69Z",
  "updated_at" : "2016-09-09T18:57:15.80Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2047681,
  "total_fee" : 204769,
  "net_amount" : 1842912,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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
request to the transfers link (i.e. POST https://api-test.payline.io/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://api-test.payline.io/identities/:IDENTITY_ID/settlements`

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


curl https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STqDkJBWWbnBJwvAns1UXQFM');

```
```java

import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STqDkJBWWbnBJwvAns1UXQFM");

```
> Example Response:

```json
{
  "id" : "STqDkJBWWbnBJwvAns1UXQFM",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "currency" : "USD",
  "created_at" : "2016-09-09T18:57:15.53Z",
  "updated_at" : "2016-09-09T18:57:17.47Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2047681,
  "total_fee" : 204769,
  "net_amount" : 1842912,
  "destination" : "PIcbZthtnNww2dipdgpcs5nf",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://api-test.payline.io/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Fund a Settlement
```shell
curl https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM \
    -H "Content-Type: application/vnd.json+api" \
    -u  USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110 \
    -X PUT \
    -d '
	{
	    "destination": "PIcbZthtnNww2dipdgpcs5nf"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "STqDkJBWWbnBJwvAns1UXQFM",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "currency" : "USD",
  "created_at" : "2016-09-09T18:57:15.53Z",
  "updated_at" : "2016-09-09T18:57:17.47Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 2047681,
  "total_fee" : 204769,
  "net_amount" : 1842912,
  "destination" : "PIcbZthtnNww2dipdgpcs5nf",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers"
    },
    "funding_transfers" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
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

`POST https://api-test.payline.io/settlements/:SETTLEMENT_ID`

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
curl https://api-test.payline.io/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STqDkJBWWbnBJwvAns1UXQFM",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "currency" : "USD",
      "created_at" : "2016-09-09T18:57:15.53Z",
      "updated_at" : "2016-09-09T18:57:17.47Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 2047681,
      "total_fee" : 204769,
      "net_amount" : 1842912,
      "destination" : "PIcbZthtnNww2dipdgpcs5nf",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers"
        },
        "funding_transfers" : {
          "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers
```shell
curl https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java
client.settlementsClient().<Resources<Settlement>>resourcesIterator()
  .forEachRemaining(settlementPage -> {
    Collection<Settlement> settlements = settlementPage.getContent();
    //do something
  });
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR8SuknR1geUBYK3QCmsKuMY",
      "amount" : 90,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "77934d31-4dec-4bd2-b5b8-4f4a31f147bf",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "destination" : "PIcbZthtnNww2dipdgpcs5nf",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:57:17.07Z",
      "updated_at" : "2016-09-09T18:57:17.64Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR8SuknR1geUBYK3QCmsKuMY"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR8SuknR1geUBYK3QCmsKuMY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR8SuknR1geUBYK3QCmsKuMY/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR8SuknR1geUBYK3QCmsKuMY/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
        }
      }
    }, {
      "id" : "TR9Tdc1H4oyRJiaJJqNkZMw5",
      "amount" : 756858,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "cd8f9d43-ae2b-4110-9ed9-55bc9ead5178",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "destination" : "PIcbZthtnNww2dipdgpcs5nf",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:57:17.07Z",
      "updated_at" : "2016-09-09T18:57:17.77Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR9Tdc1H4oyRJiaJJqNkZMw5"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR9Tdc1H4oyRJiaJJqNkZMw5/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR9Tdc1H4oyRJiaJJqNkZMw5/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR9Tdc1H4oyRJiaJJqNkZMw5/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
        }
      }
    }, {
      "id" : "TRsiARA4kjG1xVKM5Yj2ytQ8",
      "amount" : 285966,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "54e5d96c-af7a-411c-a974-d3554313d7b1",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "destination" : "PIcbZthtnNww2dipdgpcs5nf",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:57:17.07Z",
      "updated_at" : "2016-09-09T18:57:17.88Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRsiARA4kjG1xVKM5Yj2ytQ8"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRsiARA4kjG1xVKM5Yj2ytQ8/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRsiARA4kjG1xVKM5Yj2ytQ8/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRsiARA4kjG1xVKM5Yj2ytQ8/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
        }
      }
    }, {
      "id" : "TRfBpRpSsFTe66r6ozdnjKjL",
      "amount" : 799999,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "534cac22-5a2d-4603-b274-a28eff6bad76",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "destination" : "PIcbZthtnNww2dipdgpcs5nf",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:57:17.07Z",
      "updated_at" : "2016-09-09T18:57:17.99Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRfBpRpSsFTe66r6ozdnjKjL"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRfBpRpSsFTe66r6ozdnjKjL/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRfBpRpSsFTe66r6ozdnjKjL/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRfBpRpSsFTe66r6ozdnjKjL/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/funding_transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 4
  }
}
```

List the `Transfers` of type `CREDIT` that result from issuing funding instructions
for the `Settlement`.

#### HTTP Request

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Transfers in a Settlement
```shell

curl https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRbo1SJa6R42Xuj3dm39buEg",
      "amount" : 888888,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "b37863bb-3ab1-4452-b901-7e2b1ce271a3",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : "2016-09-09T18:47:08.91Z",
      "fee" : 88889,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:46:29.85Z",
      "updated_at" : "2016-09-09T18:47:01.68Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRbo1SJa6R42Xuj3dm39buEg"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRbo1SJa6R42Xuj3dm39buEg/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRbo1SJa6R42Xuj3dm39buEg/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRbo1SJa6R42Xuj3dm39buEg/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    }, {
      "id" : "TRu5iEGHBmqwuw4C51gpjstt",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : "2016-09-09T18:47:08.91Z",
      "fee" : 10,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:58.48Z",
      "updated_at" : "2016-09-09T18:46:02.77Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    }, {
      "id" : "TRa892wVpRdHFR2ka1kEyssJ",
      "amount" : 840953,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "12ca968c-0bf8-4e37-a344-86471a7a7f55",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : "2016-09-09T18:47:08.91Z",
      "fee" : 84095,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:50.87Z",
      "updated_at" : "2016-09-09T18:46:04.94Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    }, {
      "id" : "TR2mLJRJi7H92VVZMGDDnqXS",
      "amount" : 317740,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "9e07f5e3-4d81-438d-a323-58116a9239cf",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : "2016-09-09T18:47:08.91Z",
      "fee" : 31774,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:47.97Z",
      "updated_at" : "2016-09-09T18:46:05.29Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/settlements/STqDkJBWWbnBJwvAns1UXQFM/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-test.payline.io/settlements/:SETTLEMENT_ID/transfers`


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
## Retrieve a Transfer
```shell

curl https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRa892wVpRdHFR2ka1kEyssJ');



```
```java

import io.payline.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRa892wVpRdHFR2ka1kEyssJ");

```
> Example Response:

```json
{
  "id" : "TRa892wVpRdHFR2ka1kEyssJ",
  "amount" : 840953,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "12ca968c-0bf8-4e37-a344-86471a7a7f55",
  "currency" : "USD",
  "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
  "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
  "ready_to_settle_at" : null,
  "fee" : 84095,
  "statement_descriptor" : "PLD*LEES SANDWICHES",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:50.87Z",
  "updated_at" : "2016-09-09T18:46:04.94Z",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "reversals" : {
      "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/reversals"
    },
    "disputes" : {
      "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/disputes"
    },
    "source" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
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

curl https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRa892wVpRdHFR2ka1kEyssJ');
$refund = $debit->reverse(50);
```
```java

import io.payline.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
> Example Response:

```json
{
  "id" : "TRkAq84TEWTyQsARKfTbkqhy",
  "amount" : 100,
  "tags" : { },
  "state" : "PENDING",
  "trace_id" : "0c461364-9e9b-4b45-a9d0-e01233528100",
  "currency" : "USD",
  "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
  "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
  "destination" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "PLD*LEES SANDWICHES",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2016-09-09T18:45:55.00Z",
  "updated_at" : "2016-09-09T18:45:55.19Z",
  "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "self" : {
      "href" : "https://api-test.payline.io/transfers/TRkAq84TEWTyQsARKfTbkqhy"
    },
    "parent" : {
      "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ"
    },
    "destination" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
    },
    "merchant_identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "payment_instruments" : {
      "href" : "https://api-test.payline.io/transfers/TRkAq84TEWTyQsARKfTbkqhy/payment_instruments"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
      "id" : "TRu5iEGHBmqwuw4C51gpjstt",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "75dd0a60-45c0-4bd2-8086-a97546ab9f8a",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:58.48Z",
      "updated_at" : "2016-09-09T18:46:02.77Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRu5iEGHBmqwuw4C51gpjstt/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    }, {
      "id" : "TRkAq84TEWTyQsARKfTbkqhy",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "0c461364-9e9b-4b45-a9d0-e01233528100",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "destination" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:54.72Z",
      "updated_at" : "2016-09-09T18:46:04.57Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRkAq84TEWTyQsARKfTbkqhy"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRkAq84TEWTyQsARKfTbkqhy/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "parent" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        }
      }
    }, {
      "id" : "TRa892wVpRdHFR2ka1kEyssJ",
      "amount" : 840953,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "12ca968c-0bf8-4e37-a344-86471a7a7f55",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : null,
      "fee" : 84095,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:50.87Z",
      "updated_at" : "2016-09-09T18:46:04.94Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TRa892wVpRdHFR2ka1kEyssJ/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        }
      }
    }, {
      "id" : "TR2mLJRJi7H92VVZMGDDnqXS",
      "amount" : 317740,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "9e07f5e3-4d81-438d-a323-58116a9239cf",
      "currency" : "USD",
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "source" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "destination" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "ready_to_settle_at" : null,
      "fee" : 31774,
      "statement_descriptor" : "PLD*LEES SANDWICHES",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2016-09-09T18:45:47.97Z",
      "updated_at" : "2016-09-09T18:46:05.29Z",
      "merchant_identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "self" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS"
        },
        "payment_instruments" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "reversals" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/reversals"
        },
        "disputes" : {
          "href" : "https://api-test.payline.io/transfers/TR2mLJRJi7H92VVZMGDDnqXS/disputes"
        },
        "source" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "destination" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
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
    "count" : 4
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
    -u USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
  "id" : "WHpEesh5NqiC67Fn7E1NSPgS",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
  "created_at" : "2016-09-09T18:45:27.79Z",
  "updated_at" : "2016-09-09T18:45:27.79Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHpEesh5NqiC67Fn7E1NSPgS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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



curl https://api-test.payline.io/webhooks/WHpEesh5NqiC67Fn7E1NSPgS \
    -H "Content-Type: application/vnd.json+api" \
    -u USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHpEesh5NqiC67Fn7E1NSPgS');



```
```java

import io.payline.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHpEesh5NqiC67Fn7E1NSPgS");

```
> Example Response:

```json
{
  "id" : "WHpEesh5NqiC67Fn7E1NSPgS",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
  "created_at" : "2016-09-09T18:45:27.82Z",
  "updated_at" : "2016-09-09T18:45:27.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/webhooks/WHpEesh5NqiC67Fn7E1NSPgS"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
      "id" : "WHpEesh5NqiC67Fn7E1NSPgS",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APdNpPsNNG1L3Ayp5ZBDV1FD",
      "created_at" : "2016-09-09T18:45:27.82Z",
      "updated_at" : "2016-09-09T18:45:27.82Z",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/webhooks/WHpEesh5NqiC67Fn7E1NSPgS"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "name": "Maggie Chang", 
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
	    "identity": "IDhErR8YpyVQRUvGZxt7Wmft"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Maggie Chang", 
	    "expiration_year"=> 2020, 
	    "tags"=> array(
	        "card name"=> "Business Card"
	    ), 
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
	    "identity"=> "IDhErR8YpyVQRUvGZxt7Wmft"
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
  "id" : "PIm5XghDC7k81Jr3C1GNRqAS",
  "fingerprint" : "FPR-1299301881",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "4242",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Maggie Chang",
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
  "created_at" : "2016-09-09T18:45:46.12Z",
  "updated_at" : "2016-09-09T18:45:46.12Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDhErR8YpyVQRUvGZxt7Wmft",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/updates"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
	    "identity"=> "IDd5PnWSt5y8tvBqu719VHYZ"
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
  "id" : "PIcbZthtnNww2dipdgpcs5nf",
  "fingerprint" : "FPR966610431",
  "tags" : { },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T18:45:40.37Z",
  "updated_at" : "2016-09-09T18:45:40.37Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

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
          applicationId: 'APdNpPsNNG1L3Ayp5ZBDV1FD',
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
  "id" : "TKqiqq2WMdrcwzP3VYSaXgED",
  "fingerprint" : "FPR222704565",
  "created_at" : "2016-09-09T18:46:01.06Z",
  "updated_at" : "2016-09-09T18:46:01.06Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2016-09-10T18:46:01.04Z",
  "_links" : {
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    }
  }
}
```

```shell
curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "token": "TKqiqq2WMdrcwzP3VYSaXgED", 
	    "type": "TOKEN", 
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqiqq2WMdrcwzP3VYSaXgED", 
	    "type": "TOKEN", 
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
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
  "id" : "PIqiqq2WMdrcwzP3VYSaXgED",
  "fingerprint" : "FPR-752937284",
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
  "created_at" : "2016-09-09T18:46:02.15Z",
  "updated_at" : "2016-09-09T18:46:02.15Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/updates"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
    -d '
	{
	    "token": "TKqiqq2WMdrcwzP3VYSaXgED", 
	    "type": "TOKEN", 
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	{
	    "token": "TKqiqq2WMdrcwzP3VYSaXgED", 
	    "type": "TOKEN", 
	    "identity": "IDd5PnWSt5y8tvBqu719VHYZ"
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
  "id" : "PIqiqq2WMdrcwzP3VYSaXgED",
  "fingerprint" : "FPR-752937284",
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
  "created_at" : "2016-09-09T18:46:02.15Z",
  "updated_at" : "2016-09-09T18:46:02.15Z",
  "instrument_type" : "PAYMENT_CARD",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
    },
    "updates" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/updates"
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


curl https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIcbZthtnNww2dipdgpcs5nf');

```
```java

import io.payline.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIcbZthtnNww2dipdgpcs5nf")

```
> Example Response:

```json
{
  "id" : "PIcbZthtnNww2dipdgpcs5nf",
  "fingerprint" : "FPR966610431",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T18:45:40.24Z",
  "updated_at" : "2016-09-09T18:45:41.51Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
curl https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf \
    -H "Content-Type: application/vnd.json+api" \
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a \
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
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
```java

```
> Example Response:

```json
{
  "id" : "PIcbZthtnNww2dipdgpcs5nf",
  "fingerprint" : "FPR966610431",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "created_at" : "2016-09-09T18:45:40.24Z",
  "updated_at" : "2016-09-09T18:45:41.51Z",
  "instrument_type" : "BANK_ACCOUNT",
  "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
  "_links" : {
    "self" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
    },
    "authorizations" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/authorizations"
    },
    "identity" : {
      "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
    },
    "transfers" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/transfers"
    },
    "verifications" : {
      "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/verifications"
    },
    "application" : {
      "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    -u  USwVP7ZZJJ1CLgMoHFvdQx4t:479f2ce6-4e31-4f75-9071-6b84826fd55a
```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'USwVP7ZZJJ1CLgMoHFvdQx4t', '479f2ce6-4e31-4f75-9071-6b84826fd55a');
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
      "id" : "PIqiqq2WMdrcwzP3VYSaXgED",
      "fingerprint" : "FPR-752937284",
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
      "created_at" : "2016-09-09T18:46:02.00Z",
      "updated_at" : "2016-09-09T18:46:02.00Z",
      "instrument_type" : "PAYMENT_CARD",
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIqiqq2WMdrcwzP3VYSaXgED/updates"
        }
      }
    }, {
      "id" : "PIm5XghDC7k81Jr3C1GNRqAS",
      "fingerprint" : "FPR-1299301881",
      "tags" : { },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "4242",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Maggie Chang",
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
      "created_at" : "2016-09-09T18:45:46.02Z",
      "updated_at" : "2016-09-09T18:45:57.05Z",
      "instrument_type" : "PAYMENT_CARD",
      "identity" : "IDhErR8YpyVQRUvGZxt7Wmft",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDhErR8YpyVQRUvGZxt7Wmft"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        },
        "updates" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm5XghDC7k81Jr3C1GNRqAS/updates"
        }
      }
    }, {
      "id" : "PI5By6mv1LqofTeJ6tXMfPE7",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:42.68Z",
      "updated_at" : "2016-09-09T18:45:42.68Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PI5By6mv1LqofTeJ6tXMfPE7/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIm1orzwaNNiY4stueeBmrzE",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:42.68Z",
      "updated_at" : "2016-09-09T18:45:42.68Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm1orzwaNNiY4stueeBmrzE"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm1orzwaNNiY4stueeBmrzE/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm1orzwaNNiY4stueeBmrzE/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIm1orzwaNNiY4stueeBmrzE/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIn7YSuWXC6X9RqBCsGpsRQ7",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:42.68Z",
      "updated_at" : "2016-09-09T18:45:42.68Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIn7YSuWXC6X9RqBCsGpsRQ7"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIn7YSuWXC6X9RqBCsGpsRQ7/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIn7YSuWXC6X9RqBCsGpsRQ7/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIn7YSuWXC6X9RqBCsGpsRQ7/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIcbZthtnNww2dipdgpcs5nf",
      "fingerprint" : "FPR966610431",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "created_at" : "2016-09-09T18:45:40.24Z",
      "updated_at" : "2016-09-09T18:45:41.51Z",
      "instrument_type" : "BANK_ACCOUNT",
      "identity" : "IDd5PnWSt5y8tvBqu719VHYZ",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDd5PnWSt5y8tvBqu719VHYZ"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIcbZthtnNww2dipdgpcs5nf/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PImiuiBHYPzEXsGJCe9vFh3M",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:22.84Z",
      "updated_at" : "2016-09-09T18:45:22.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfUZyah9skwSWz1AWFh5LmX",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiuiBHYPzEXsGJCe9vFh3M"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiuiBHYPzEXsGJCe9vFh3M/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiuiBHYPzEXsGJCe9vFh3M/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PImiuiBHYPzEXsGJCe9vFh3M/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIgFthnvZioZM43JKADRyVLp",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:22.84Z",
      "updated_at" : "2016-09-09T18:45:22.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfUZyah9skwSWz1AWFh5LmX",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgFthnvZioZM43JKADRyVLp"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgFthnvZioZM43JKADRyVLp/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgFthnvZioZM43JKADRyVLp/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIgFthnvZioZM43JKADRyVLp/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIiNCyLBRgWZti3Q6tGZw8xX",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:22.84Z",
      "updated_at" : "2016-09-09T18:45:22.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDfUZyah9skwSWz1AWFh5LmX",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNCyLBRgWZti3Q6tGZw8xX"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNCyLBRgWZti3Q6tGZw8xX/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDfUZyah9skwSWz1AWFh5LmX"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNCyLBRgWZti3Q6tGZw8xX/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIiNCyLBRgWZti3Q6tGZw8xX/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
        }
      }
    }, {
      "id" : "PIsboMj74gvDZxPVgdMm1Gnz",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2016-09-09T18:45:22.84Z",
      "updated_at" : "2016-09-09T18:45:22.84Z",
      "instrument_type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDjFtXt19dt59nd6jyyF7VuF",
      "_links" : {
        "self" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsboMj74gvDZxPVgdMm1Gnz"
        },
        "authorizations" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsboMj74gvDZxPVgdMm1Gnz/authorizations"
        },
        "identity" : {
          "href" : "https://api-test.payline.io/identities/IDjFtXt19dt59nd6jyyF7VuF"
        },
        "transfers" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsboMj74gvDZxPVgdMm1Gnz/transfers"
        },
        "verifications" : {
          "href" : "https://api-test.payline.io/payment_instruments/PIsboMj74gvDZxPVgdMm1Gnz/verifications"
        },
        "application" : {
          "href" : "https://api-test.payline.io/applications/APdNpPsNNG1L3Ayp5ZBDV1FD"
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
    "count" : 10
  }
}
```

#### HTTP Request

`GET https://api-test.payline.io/payment_instruments`

