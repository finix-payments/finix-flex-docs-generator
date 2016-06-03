---
title: Finix API Reference

language_tabs:
  - shell: cURL
  - php: PHP

includes:
  - errors

search: true
---

# Guides


## Getting Started
```shell


# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
This guide will demonstrate the main workflows for utilizing the Finix Payments API for platforms and marketplaces. We have language bindings in cURL, PHP, Ruby, Python, C#, Java and Perl! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

To communicate with the Finix API you'll need to authenticate your requests with a username and password. For the sandbox environment you may use the credentials listed below or you can supply your own.

- Username: `USoBmxXjyNWJzEufDtXdbuV8`

- Password: `fe398ca8-bf15-4aa1-bc36-0ff448c77bab`

You should also know your Application ID. An Application, also referred as an "App", is a resource that represents your web App or any service that connects customers (i.e. buyers) and merchants (i.e. sellers). For the sandbox environment you may use the following ID:

- App ID: `APrRQxKrRfkC4MkL3Qa3qEW1`


## Create an Identity for a Merchant

```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"tags\": {
	        \"key\": \"value\"
	    }, 
	    \"entity\": {
	        \"business_type\": \"INDIVIDUAL_SOLE_PROPRIETORSHIP\", 
	        \"business_phone\": \"+1 (408) 756-4497\", 
	        \"first_name\": \"dwayne\", 
	        \"last_name\": \"Sunkhronos\", 
	        \"phone\": \"1234567890\", 
	        \"dob\": {
	            \"year\": 1978, 
	            \"day\": 27, 
	            \"month\": 6
	        }, 
	        \"mcc\": \"0742\", 
	        \"business_address\": {
	            \"city\": \"San Mateo\", 
	            \"country\": \"USA\", 
	            \"region\": \"CA\", 
	            \"line2\": \"Apartment 8\", 
	            \"line1\": \"741 Douglass St\", 
	            \"postal_code\": \"94114\"
	        }, 
	        \"max_transaction_amount\": 120000, 
	        \"principal_percentage_ownership\": 100, 
	        \"doing_business_as\": \"Gold's Gym\", 
	        \"annual_card_volume\": 12000000, 
	        \"default_statement_descriptor\": \"Gold's Gym\", 
	        \"url\": \"www.Gold'sGym.com\", 
	        \"business_name\": \"Gold's Gym\", 
	        \"incorporation_date\": {
	            \"year\": 1978, 
	            \"day\": 27, 
	            \"month\": 6
	        }, 
	        \"business_tax_id\": \"123456789\", 
	        \"personal_address\": {
	            \"city\": \"San Mateo\", 
	            \"country\": \"USA\", 
	            \"region\": \"CA\", 
	            \"line2\": \"Apartment 7\", 
	            \"line1\": \"741 Douglass St\", 
	            \"postal_code\": \"94114\"
	        }, 
	        \"email\": \"user@example.org\", 
	        \"tax_id\": \"5779\"
	    }
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "phone"=> "1234567890", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "mcc"=> "0742", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 120000, 
	        "principal_percentage_ownership"=> 100, 
	        "doing_business_as"=> "Gold's Gym", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Gold's Gym", 
	        "url"=> "www.Gold'sGym.com", 
	        "business_name"=> "Gold's Gym", 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_tax_id"=> "123456789", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	)
);
$identity = $identity->save();

```

> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:43:25.52Z", 
	    "updated_at": "2016-06-02T22:43:25.52Z", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Gold's Gym", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Gold's Gym", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.Gold'sGym.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Gold's Gym", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/merchants"
	        }
	    }, 
	    "id": "IDmDq5VJgDhSurQxrM2sJoqD"
	}
```

Before we can charge a card we need to create an Identity resource. An Identity represents a person or business. In this case, the Identity will represent the merchant (i.e. seller). Let's create one now.You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Create a New Bank Account
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"account_type\": \"SAVINGS\", 
	    \"name\": \"Fran Lemke\", 
	    \"bank_code\": \"123123123\", 
	    \"country\": \"USA\", 
	    \"currency\": \"USD\", 
	    \"account_number\": \"123123123\", 
	    \"type\": \"BANK_ACCOUNT\", 
	    \"identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "bank_code"=> "123123123", 
	    "country"=> "USA", 
	    "currency"=> "USD", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDAyTLs4vrJDCMNp6BFHAGF"
	));
$bank_account = $bank_account->save();


```
> Example Response:

```json

	{
	    "instrument_type": "BANK_ACCOUNT", 
	    "masked_account_number": "XXXXX3123", 
	    "name": "Fran Lemke", 
	    "tags": {}, 
	    "country": "USA", 
	    "created_at": "2016-06-02T22:43:34.48Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-02T22:43:34.48Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI2XUFqgEDxT9Q3aUYRcQZTA", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```
<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | IDAyTLs4vrJDCMNp6BFHAGF
account_type | *string*, **required** | Checking or Savings | SAVINGS
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | BANK_ACCOUNT
currency | *string*, **optional** | Default currency used when settling funds. | USD
first_name | *string*, **optional** | Customer's first name on bank account. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
country | *string*, **optional** | Country of the associated bank account. | USA
bic | *string*, **optional** | TBD. | foo
iban | *string*, **optional** | International Bank Account integer | foo
company_name | *string*, **optional** | Name of company if the bank account is a company account. |  Bob's Burgers


## Perform an Identity Verification
```shell


curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"merchant\": null, 
	    \"instrument\": null, 
	    \"processor\": \"DUMMY_V1\", 
	    \"identity\": null
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:43:37.64Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:43:37.67Z", 
	    "id": "VI3vea6eKdRhoaeXAAmf86Q1", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "external_trace_id": "28b097f1-1ac4-469a-8edb-7fd6f949de99", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Before, being able to process funds to this seller we will need to perform an identity verification to underwrite them as a Merchant. Only underwritten Identities can be paid out per KYC regulations.


## Provision Merchant Account
```shell

curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
> Example Response:

```json

	{
	    "created_at": "2016-06-02T22:43:36.10Z", 
	    "updated_at": "2016-06-02T22:43:36.10Z", 
	    "id": "MUnsRFnkNjTzDrYZ9GsFu8nk", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/merchants/MUnsRFnkNjTzDrYZ9GsFu8nk"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-staging.finix.io/merchant_profiles/MPgXyBjtqhZXPUtbX4vpqiNG"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/merchants/MUnsRFnkNjTzDrYZ9GsFu8nk/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "verification": {
	            "href": "https://api-staging.finix.io/verifications/VIwZBfx4tRWXwkV2asE6n7Fz"
	        }
	    }, 
	    "verification": "VIwZBfx4tRWXwkV2asE6n7Fz", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPgXyBjtqhZXPUtbX4vpqiNG", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Once the Identity has been verified, Finix will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.

## Create an Identity for a Buyer (i.e. buyer)
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"tags\": {
	        \"key\": \"value\"
	    }, 
	    \"entity\": {
	        \"first_name\": \"Dwayne\", 
	        \"last_name\": \"Johnson\"
	    }
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "first_name"=> "Dwayne", 
	        "last_name"=> "Johnson"
	    )
	)
);
$identity = $identity->save();

```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:43:38.49Z", 
	    "updated_at": "2016-06-02T22:43:38.49Z", 
	    "entity": {
	        "business_type": null, 
	        "business_phone": null, 
	        "first_name": "Dwayne", 
	        "last_name": "Johnson", 
	        "amex_mid": null, 
	        "dob": null, 
	        "default_statement_descriptor": null, 
	        "business_tax_id_provided": false, 
	        "business_address": null, 
	        "doing_business_as": null, 
	        "phone": null, 
	        "discover_mid": null, 
	        "url": null, 
	        "personal_address": null, 
	        "business_name": null, 
	        "tax_id_provided": false, 
	        "email": null, 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/merchants"
	        }
	    }, 
	    "id": "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	}
```
This next step should sound familiar. Let's create an Identity to represent the buyer. You'll want to store the ID of the newly created Identity resource as you'll reference it later.


## Create a Payment Instrument (i.e. card)
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"expiration_year\": 2020, 
	    \"number\": \"4242424242424242\", 
	    \"expiration_month\": 12, 
	    \"address\": {
	        \"city\": \"San Mateo\", 
	        \"country\": \"USA\", 
	        \"region\": \"CA\", 
	        \"line2\": \"Apartment 7\", 
	        \"line1\": \"741 Douglass St\", 
	        \"postal_code\": \"94114\"
	    }, 
	    \"security_code\": \"112\", 
	    \"type\": \"PAYMENT_CARD\", 
	    \"identity\": \"IDcq7bJ4vTXn1RxY5v4UMQ3T\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
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
	    "identity"=> "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	));
$card = $card->save();


```
> Example Response:

```json

	{
	    "instrument_type": "PAYMENT_CARD", 
	    "card_type": "UNKNOWN", 
	    "name": "Dwayne Johnson", 
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
	    "updated_at": "2016-06-02T22:43:39.27Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T"
	        }, 
	        "updates": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/updates"
	        }
	    }, 
	    "created_at": "2016-06-02T22:43:39.27Z", 
	    "id": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "identity": "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	}
```

Now that we have an Identity resource representing our buyer, we'll need to create a Payment Instrument which can represent either a card or bank account. In this instance we'll create a card with the request to the right (note you'll need to interpolate your own buyer's Identity from the previous request).

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

Be sure to store the ID of your newly tokenized Payment Instrument.


## Create a Transfer (i.e. debit the card)
```shell


curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"fee\": 10, 
	    \"currency\": \"USD\", 
	    \"merchant_identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\", 
	    \"source\": \"PI5zCmfsnrvhVvPX9h14r3GJ\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "source"=> "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```

> Example Response:

```json

	{
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "destination": "PIrpGUd5TDf8dKDPFr9bfgMH", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:43:40.59Z", 
	    "created_at": "2016-06-02T22:43:40.46Z", 
	    "tags": {}, 
	    "trace_id": "f75403f8-7174-4dd4-87b1-ed2e5400ace4", 
	    "statement_descriptor": "FNX*GOLD'S GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIrpGUd5TDf8dKDPFr9bfgMH"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/disputes"
	        }
	    }, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "type": "DEBIT", 
	    "id": "TRbfrkiuuCEd71qFuMMkBbvu"
	}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.


## Reverse the Transfer (i.e. issue a refund)
```shell

curl https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d  "
	  {
	  \"refund_amount\" : 100
  	}		
	"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```

> Example Response:

```json

	{
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "destination": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:45:13.76Z", 
	    "created_at": "2016-06-02T22:45:13.64Z", 
	    "tags": {}, 
	    "trace_id": "98028e8a-2da8-4627-adf3-1bc328174698", 
	    "statement_descriptor": "FNX*GOLD'S GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRuSFU37qwp3YD4aYKA9V9X8"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRuSFU37qwp3YD4aYKA9V9X8/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu"
	        }
	    }, 
	    "source": "PIrpGUd5TDf8dKDPFr9bfgMH", 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "type": "REVERSAL", 
	    "id": "TRuSFU37qwp3YD4aYKA9V9X8"
	}
```

What if we need to issue a refund to the buyer? First, you'll need to take the previously stored Transfer ID and interpolate it into the following url path. The amount can be equal to or less than the original debit.

## Settle out funds to a Merchant
```shell

curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"currency\": \"USD\", 
	    \"processor\": \"DUMMY_V1\"
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

```
> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:46:18.05Z", 
	    "updated_at": "2016-06-02T22:46:18.06Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "ST6em979P6RerKZAqxNMJTcb", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Awesome! Now you know how to charge a card and reverse the debit.

Now you need to settle out the funds to your merchant. To do so you will create a Settlement resource. Each settlement is comprised of all the Transfers that have a SUCCEEDED state and that have not been previously settled out.
# Tokenization.js
To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js, keeps you out of the PCI scope by sending sensitive payment information over SSL directly to the Finix servers.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/2hxnjL0q/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Finix API.
</aside>


## Step 1: Include library
To use tokenization.js you will first need to include the library. Please include the script tag as demonstrated to the right.

html
<script type="text/javascript" src="https://js.verygoodproxy.com/tokenization.1-latest.js"></script>


<aside class="notice">
Note that we do not recommend hosting the tokenization.js library locally as doing so prevents important updates.
</aside>

## Step 2: Create a form
html
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

Before collecting the sensitive payment information, we will need to construct an HTML form for users to input the data.

We have provided a simple example to the right for capturing Payment Instrument data.

## Step 3: Configure and initialize

javascript
var initTokenization = function() {
  Tokenization.init({
    server: "https://api-staging.finix.io",
    applicationId: "APrRQxKrRfkC4MkL3Qa3qEW1",
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

We will need to configure the client so that it POSTs to the correct endpoint and associates the Payment Instrument to your application. During the initialization we will also use the JQuery selector method to capture the form data.

### Initialization Fields
Field | Type | Description | Example
----- | ---- | ----------- | -------
server | *string*, **required** |  The base url for the Finix API| https://api-staging.finix.io
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | APrRQxKrRfkC4MkL3Qa3qEW1
hosted_fields | *object*, **required** |  An object containing the payment instrument information collected from your form.  | Johnson

### hosted_fields object for card
Field | Type | Description | Example
----- | ---- | ----------- | -------
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020

### hosted_fields object for bankAccount
Field | Type | Description | Example
----- | ---- | ----------- | -------
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124


## Step 4: Submit payload and handle response

javascript
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


> Example Tokenization Response:
javascript
{
    "id": "TKmMEyy7CQmfeFrJq1JfnigP",
    "fingerprint": "FPR-1392097976",
    "created_at": "2016-03-07T22:27:01.611",
    "updated_at": "2016-03-07T22:27:01.611",
    "instrument_type": "PAYMENT_CARD"
}


Finally we will need to register a click event that fires when our users submit the form and define a callback for handling the tokenization.js response. We have included an example to the right.

## Step 5: Send token to your back-end server for storing

javascript
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


Great now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server. You can expand on the callback that you previously created like so:

## Step 6: Associate to an Identity



curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"token\": \"TKmMEyy7CQmfeFrJq1JfnigP\", 
	    \"type\": \"TOKEN\", 
	    \"identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\"
	}"


> Example Response:

json

	{
	    "instrument_type": "TOKEN", 
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:19.55Z", 
	    "updated_at": "2016-06-02T22:46:19.55Z", 
	    "token": "TKmMEyy7CQmfeFrJq1JfnigP", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIidozqLLaLceXuigdHMdAD2/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIidozqLLaLceXuigdHMdAD2"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIidozqLLaLceXuigdHMdAD2/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIidozqLLaLceXuigdHMdAD2/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "fingerprint": "FPR-403206930", 
	    "id": "PIidozqLLaLceXuigdHMdAD2", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}

Before you can use the newly tokenized card or bank account you will need to associate it with an Identity. To do this you must make an authenticated POST request to `https://api-staging.finix.io/payment_instruments` like demonstrated to the right.

### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`
# Authorizations
An Authorization resource (also known as a card hold) reserves a specific amount on a card to be captured (debited) at a later date, usually within 7 days. When an Authorization is captured it produces a Transfer resource.


## Create a New Authorization
```shell

curl https://api-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"merchant_identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\", 
	    \"currency\": \"USD\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\", 
	    \"source\": \"PI5zCmfsnrvhVvPX9h14r3GJ\"
	}"



```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PI5zCmfsnrvhVvPX9h14r3GJ"
	));
$authorization = $authorization->save();

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:45:14.81Z", 
	    "trace_id": "47bc9c38-d601-4617-9867-3a87fcbd8b80", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:45:14.81Z", 
	    "updated_at": "2016-06-02T22:45:14.82Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUeVX2Rkz9k3j8aS8vUsYQf9"
	        }
	    }, 
	    "id": "AUeVX2Rkz9k3j8aS8vUsYQf9"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/authorizations`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PI5zCmfsnrvhVvPX9h14r3GJ
merchant_identity | *string*, **required** | UID. | IDAyTLs4vrJDCMNp6BFHAGF
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Capture an Authorization

```shell

curl https://api-staging.finix.io/authorizations/AUeVX2Rkz9k3j8aS8vUsYQf9 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -X PUT \
    -d "
	{
	    \"fee\": \"10\", 
	    \"void_me\": null, 
	    \"statement_descriptor\": \"Bob's Burgers\", 
	    \"capture_amount\": 100
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUeVX2Rkz9k3j8aS8vUsYQf9');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "transfer": "TR75UyzaqSzypJ5q4b95ZEfo", 
	    "created_at": "2016-06-02T22:45:14.67Z", 
	    "trace_id": "47bc9c38-d601-4617-9867-3a87fcbd8b80", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:45:14.67Z", 
	    "updated_at": "2016-06-02T22:45:14.67Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TR75UyzaqSzypJ5q4b95ZEfo"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUeVX2Rkz9k3j8aS8vUsYQf9"
	        }
	    }, 
	    "id": "AUeVX2Rkz9k3j8aS8vUsYQf9"
	}
```

### HTTP Request

`PUT https://api-staging.finix.io/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
capture_amount | *integer*, **required** | The amount of the authorization you would like to capture in cents. Must be less than or equal to the amount of the authorization | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100

## Retrieve an Authorization
```shell

curl https://api-staging.finix.io/authorizations/AUeVX2Rkz9k3j8aS8vUsYQf9 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUeVX2Rkz9k3j8aS8vUsYQf9');

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "transfer": "TR75UyzaqSzypJ5q4b95ZEfo", 
	    "created_at": "2016-06-02T22:45:14.67Z", 
	    "trace_id": "47bc9c38-d601-4617-9867-3a87fcbd8b80", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:45:14.67Z", 
	    "updated_at": "2016-06-02T22:45:14.67Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TR75UyzaqSzypJ5q4b95ZEfo"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUeVX2Rkz9k3j8aS8vUsYQf9"
	        }
	    }, 
	    "id": "AUeVX2Rkz9k3j8aS8vUsYQf9"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


# Disputes
Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl https://api-staging.finix.io/disputes/DItY913WtRH1hU2oakgf6QRw \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Dispute;

$dispute = Dispute::retrieve('DItY913WtRH1hU2oakgf6QRw');

```
> Example Response:

```json

	{
	    "state": "PENDING", 
	    "transfer": "TRwqG8suJyuU6keYEbnkMrFx", 
	    "created_at": "2016-06-02T22:44:08.83Z", 
	    "tags": {}, 
	    "occurred_at": "2016-06-02T22:43:41.68Z", 
	    "amount": 0, 
	    "updated_at": "2016-06-02T22:44:08.83Z", 
	    "reason": "FRAUD", 
	    "_links": {
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TRwqG8suJyuU6keYEbnkMrFx"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/disputes/DItY913WtRH1hU2oakgf6QRw"
	        }, 
	        "evidence": {
	            "href": "https://api-staging.finix.io/disputes/DItY913WtRH1hU2oakgf6QRw/evidence"
	        }
	    }, 
	    "respond_by": "2016-06-09T22:44:09.00Z", 
	    "id": "DItY913WtRH1hU2oakgf6QRw", 
	    "identity": "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/disputes/dispute_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
dispute_id | ID of the Dispute

# Identities
An Identity resource represents a business or person. Payment Instrument resources may be associated to an Identity.

## Create an Identity for a Buyer
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"tags\": {
	        \"key\": \"value\"
	    }, 
	    \"entity\": {
	        \"first_name\": \"Dwayne\", 
	        \"last_name\": \"Johnson\"
	    }
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "first_name"=> "Dwayne", 
	        "last_name"=> "Johnson"
	    )
	)
);
$identity = $identity->save();

```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:43:38.49Z", 
	    "updated_at": "2016-06-02T22:43:38.49Z", 
	    "entity": {
	        "business_type": null, 
	        "business_phone": null, 
	        "first_name": "Dwayne", 
	        "last_name": "Johnson", 
	        "amex_mid": null, 
	        "dob": null, 
	        "default_statement_descriptor": null, 
	        "business_tax_id_provided": false, 
	        "business_address": null, 
	        "doing_business_as": null, 
	        "phone": null, 
	        "discover_mid": null, 
	        "url": null, 
	        "personal_address": null, 
	        "business_name": null, 
	        "tax_id_provided": false, 
	        "email": null, 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T/merchants"
	        }
	    }, 
	    "id": "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/identities`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
first_name | *string*, **optional** | First name  | Dwayne
last_name | *string*, **optional** | Last name  | Johnson
phone | *string*, **optional** | Phone number | 1408756449
email | *string*, **optional** | Email address | someone@example.com
line1 | *string*, **optional** | Street address | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address |  Apt. 3
city | *string*, **optional** | City | San Mateo
region | *string*, **optional** | State | CA
postal_code | *string*, **optional** | Postal code | 92704
country | *string*, **optional** | Country  | USA
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}

## Create an Identity for a Merchant
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"tags\": {
	        \"key\": \"value\"
	    }, 
	    \"entity\": {
	        \"business_type\": \"INDIVIDUAL_SOLE_PROPRIETORSHIP\", 
	        \"business_phone\": \"+1 (408) 756-4497\", 
	        \"first_name\": \"dwayne\", 
	        \"last_name\": \"Sunkhronos\", 
	        \"phone\": \"1234567890\", 
	        \"dob\": {
	            \"year\": 1978, 
	            \"day\": 27, 
	            \"month\": 6
	        }, 
	        \"mcc\": \"0742\", 
	        \"business_address\": {
	            \"city\": \"San Mateo\", 
	            \"country\": \"USA\", 
	            \"region\": \"CA\", 
	            \"line2\": \"Apartment 8\", 
	            \"line1\": \"741 Douglass St\", 
	            \"postal_code\": \"94114\"
	        }, 
	        \"max_transaction_amount\": 120000, 
	        \"principal_percentage_ownership\": 100, 
	        \"doing_business_as\": \"Gold's Gym\", 
	        \"annual_card_volume\": 12000000, 
	        \"default_statement_descriptor\": \"Gold's Gym\", 
	        \"url\": \"www.Gold'sGym.com\", 
	        \"business_name\": \"Gold's Gym\", 
	        \"incorporation_date\": {
	            \"year\": 1978, 
	            \"day\": 27, 
	            \"month\": 6
	        }, 
	        \"business_tax_id\": \"123456789\", 
	        \"personal_address\": {
	            \"city\": \"San Mateo\", 
	            \"country\": \"USA\", 
	            \"region\": \"CA\", 
	            \"line2\": \"Apartment 7\", 
	            \"line1\": \"741 Douglass St\", 
	            \"postal_code\": \"94114\"
	        }, 
	        \"email\": \"user@example.org\", 
	        \"tax_id\": \"5779\"
	    }
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "phone"=> "1234567890", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "mcc"=> "0742", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 120000, 
	        "principal_percentage_ownership"=> 100, 
	        "doing_business_as"=> "Gold's Gym", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Gold's Gym", 
	        "url"=> "www.Gold'sGym.com", 
	        "business_name"=> "Gold's Gym", 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_tax_id"=> "123456789", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	)
);
$identity = $identity->save();

```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:43:25.52Z", 
	    "updated_at": "2016-06-02T22:43:25.52Z", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Gold's Gym", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Gold's Gym", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.Gold'sGym.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Gold's Gym", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDmDq5VJgDhSurQxrM2sJoqD/merchants"
	        }
	    }, 
	    "id": "IDmDq5VJgDhSurQxrM2sJoqD"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/identities`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
business_name | *string*, **required** | Full legal business name | Business, Inc
doing_business_as | *string*, **required** | Business name used if different from its legal name | Bob's Burgers
business_type | *string*, **required** | Type of business | INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, LIMITED_PARTNERSHIP, GENERAL_PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit SSN if business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP or EIN for all other business types | 123456789
business_phone | *string*, **required** | Phone number of the business | 0123456789
first_name | *string*, **required** | First name of the representative of the business | Dwayne
last_name | *string*, **required** | Last name of the representative of the business | Johnson
tax_id | *string*, **required** | Nine digit Social Security Number for the company representative | 123456789
phone | *string*, **required** | Company representative's phone number (Note: There's a separate field for the business phone integer) | 1408756449
email | *string*, **required** | Email address where support requests will be sent | someone@example.com
line1 | *string*, **required** | Street address | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address |  Apt. 3
city | *string*, **required** | City | San Mateo
region | *string*, **required** | State | CA
postal_code | *string*, **required** | Postal code | 92704
country | *string*, **required** | Country  | USA
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales in cents expected to be processed under this Merchant | 10000
max_transaction_amount | *integer*, **required** |  Maximum amount in cents that can be transacted on a single transaction | 10000
mcc | *string*, **required** |  MCC code that this merchant will be classified under | 5422
url | *string*, **required** |  Company website | www.mybusiness.com
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}
default_statement_descriptor | *string*, *required** | String displayed on the buyer's bank or card statement. Length must be between 1 and 20 charactesrs. | {'order_number': '123123123'}
principal_percentage_ownership | *integer*, *required** | Percentage of company owned by the principal | 51
incorporation_date  | *object*, **required** | Date company was incorporated. Comprised of day, month, and year. | see below
day | *integer*, **required** | Day field of the incorporation date| 1
month | *integer*, **required** | Month field of the incorporation date | 2
year | *string*, **required** | Year field of the incorporation date | 1988
dob | *object*, **required** | Date of birth of the company reprentative's date of birth. Comprised of day, month, and year. | see below
day | *integer*, **required** | Day field of the company reprentative's date of birth | 1
month | *integer*, **required** | Month field of the company reprentative's date of birth | 2
year | *string*, **required** | Year field of the company reprentative's date of birth | 1988
## Retrieve a Identity
```shell

curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');
```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:43:24.56Z", 
	    "updated_at": "2016-06-02T22:43:24.56Z", 
	    "entity": {
	        "business_type": "LIMITED_LIABILITY_COMPANY", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Gold's Gym", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Gold's Gym", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.Gold'sGym.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Gold's Gym", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/merchants"
	        }
	    }, 
	    "id": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/identities/identity_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

## Underwrite an Identity

```shell

curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```

> Example Response:

```json

	{
	    "created_at": "2016-06-02T22:43:36.10Z", 
	    "updated_at": "2016-06-02T22:43:36.10Z", 
	    "id": "MUnsRFnkNjTzDrYZ9GsFu8nk", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/merchants/MUnsRFnkNjTzDrYZ9GsFu8nk"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-staging.finix.io/merchant_profiles/MPgXyBjtqhZXPUtbX4vpqiNG"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/merchants/MUnsRFnkNjTzDrYZ9GsFu8nk/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "verification": {
	            "href": "https://api-staging.finix.io/verifications/VIwZBfx4tRWXwkV2asE6n7Fz"
	        }
	    }, 
	    "verification": "VIwZBfx4tRWXwkV2asE6n7Fz", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPgXyBjtqhZXPUtbX4vpqiNG", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Underwrite a previously created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


### HTTP Request

`POST https://api-staging.finix.io/identities/identity_id/merchants`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

# Identity Verifications
Identities (merchants) to whom you wish to pay out must be underwritten as per KYC regulations. Each attempt at verifying an Identity creates a Verification resource.

## Create an Identity Verification

```shell


curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"merchant\": null, 
	    \"instrument\": null, 
	    \"processor\": \"DUMMY_V1\", 
	    \"identity\": null
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:43:37.64Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:43:37.67Z", 
	    "id": "VI3vea6eKdRhoaeXAAmf86Q1", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "external_trace_id": "28b097f1-1ac4-469a-8edb-7fd6f949de99", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-staging.finix.io/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1


## Retrieve an Identity Verification
```shell

curl https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Verification;

$verification = Verification::retrieve('VI3vea6eKdRhoaeXAAmf86Q1');

```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:43:37.53Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:43:37.53Z", 
	    "id": "VI3vea6eKdRhoaeXAAmf86Q1", 
	    "instrument": null, 
	    "state": "SUCCEEDED", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "external_trace_id": "28b097f1-1ac4-469a-8edb-7fd6f949de99", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/verifications/verification_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
verification_id | ID of the Identity Verification

# Settlements
A Settlement resource represents a collection of Transfers that are to be paid out to a specific Merchant.


## Create a New Settlement
```shell

curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"currency\": \"USD\", 
	    \"processor\": \"DUMMY_V1\"
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDAyTLs4vrJDCMNp6BFHAGF');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

```


> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:46:18.05Z", 
	    "updated_at": "2016-06-02T22:46:18.06Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "ST6em979P6RerKZAqxNMJTcb", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/identities/:identity_id/settlements`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1
currency | *integer*, **required** | The currency for the settlement. | USD


## Fetch a Settlement

```shell


curl https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('ST6em979P6RerKZAqxNMJTcb');

```
> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:46:17.94Z", 
	    "updated_at": "2016-06-02T22:46:17.94Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/ST6em979P6RerKZAqxNMJTcb"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "ST6em979P6RerKZAqxNMJTcb", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Fetch a previously created Settlement.

### HTTP Request

`POST https://api-staging.finix.io/settlements/settlement_id/`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
settlement_id | ID of the Settlment

# Transfers
A Transfer resource represents any omnidirectional flow of funds. Transfers can represent either a debit to a card, a credit to a bank account, or a refund to a card depending on the request. Transfers have a state attribute representing the current state of the transaction. There are three possible status values: PENDING, SUCCEEDED, or FAILED.

## Debit a Card

```shell


curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"fee\": 10, 
	    \"currency\": \"USD\", 
	    \"merchant_identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\", 
	    \"source\": \"PI5zCmfsnrvhVvPX9h14r3GJ\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "source"=> "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```


> Example Response:

```json

	{
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "destination": "PIrpGUd5TDf8dKDPFr9bfgMH", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:43:40.59Z", 
	    "created_at": "2016-06-02T22:43:40.46Z", 
	    "tags": {}, 
	    "trace_id": "f75403f8-7174-4dd4-87b1-ed2e5400ace4", 
	    "statement_descriptor": "FNX*GOLD'S GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIrpGUd5TDf8dKDPFr9bfgMH"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/disputes"
	        }
	    }, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "type": "DEBIT", 
	    "id": "TRbfrkiuuCEd71qFuMMkBbvu"
	}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST https://api-staging.finix.io/transfers`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PI5zCmfsnrvhVvPX9h14r3GJ
merchant_identity | *string*, **required** | UID. | IDAyTLs4vrJDCMNp6BFHAGF
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Refund a Debit
```shell

curl https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d  "
	  {
	  \"refund_amount\" : 100
  	}		
	"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TRbfrkiuuCEd71qFuMMkBbvu');
$refund = $debit->reverse(50);
```


> Example Response:

```json

	{
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "destination": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:45:13.76Z", 
	    "created_at": "2016-06-02T22:45:13.64Z", 
	    "tags": {}, 
	    "trace_id": "98028e8a-2da8-4627-adf3-1bc328174698", 
	    "statement_descriptor": "FNX*GOLD'S GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRuSFU37qwp3YD4aYKA9V9X8"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRuSFU37qwp3YD4aYKA9V9X8/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu"
	        }
	    }, 
	    "source": "PIrpGUd5TDf8dKDPFr9bfgMH", 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "type": "REVERSAL", 
	    "id": "TRuSFU37qwp3YD4aYKA9V9X8"
	}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

### HTTP Request

`POST https://api-staging.finix.io/transfers/transfer_id/reversals`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
refund_amount | *integer*, **required** | The amount of the refund in cents. Must be equal to or less than the amount of the original debit. | 100

## Retrieve a Transfer
```shell

curl https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TRbfrkiuuCEd71qFuMMkBbvu');



```
> Example Response:

```json

	{
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "destination": "PIrpGUd5TDf8dKDPFr9bfgMH", 
	    "state": "SUCCEEDED", 
	    "updated_at": "2016-06-02T22:43:40.32Z", 
	    "created_at": "2016-06-02T22:43:40.32Z", 
	    "tags": {}, 
	    "trace_id": "f75403f8-7174-4dd4-87b1-ed2e5400ace4", 
	    "statement_descriptor": "FNX*GOLD'S GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIrpGUd5TDf8dKDPFr9bfgMH"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TRbfrkiuuCEd71qFuMMkBbvu/disputes"
	        }
	    }, 
	    "source": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "merchant_identity": "IDAyTLs4vrJDCMNp6BFHAGF", 
	    "type": "DEBIT", 
	    "id": "TRbfrkiuuCEd71qFuMMkBbvu"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/transfers/transfer_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the Transfer


# Webhooks
Webhooks allow you to build or set up integrations which subscribe to certain events on the Finix API. When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL. Webhooks are particularly useful for updating asynchronous state changes in Transfers or notifications of newly created Disputes.

## Create a New Webhook
```shell

curl https://api-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	            {
	            \"url\" : \"http://requestb.in/vts8mpvt\"
	            }
	        "

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-06-02T22:43:23.84Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-02T22:43:23.84Z", 
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/webhooks/WHi69PP2ak8gV2g3AAp1n5dL"
	        }
	    }, 
	    "id": "WHi69PP2ak8gV2g3AAp1n5dL"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/webhooks`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
url | *string*, **required** | The HTTP or HTTPS url the callbacks will be made to | https://examplesite.com


## Retrieve a Webhook

```shell



curl https://api-staging.finix.io/webhooks/WHi69PP2ak8gV2g3AAp1n5dL \
    -H "Content-Type: application/vnd.json+api" \
    -u USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHi69PP2ak8gV2g3AAp1n5dL');



```

> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-06-02T22:43:23.84Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-02T22:43:23.84Z", 
	    "application": "APrRQxKrRfkC4MkL3Qa3qEW1", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/webhooks/WHi69PP2ak8gV2g3AAp1n5dL"
	        }
	    }, 
	    "id": "WHi69PP2ak8gV2g3AAp1n5dL"
	}
```

### HTTP Request

`GET https://api-staging.finix.io/webhooks/webhook_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
webhook_id | ID of the Webhook

# Payment Instruments
A Payment Instrument resource represents either a credit card or bank account. All information is securely vaulted and referenced by an ID. A Payment Instrument may be created multiple times, and each tokenization produces a unique ID. Each ID may only be associated one time and to only one Identity. Once associated, a Payment Instrument may not be disassociated from an Identity.


## Create a New Card
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"expiration_year\": 2020, 
	    \"number\": \"4242424242424242\", 
	    \"expiration_month\": 12, 
	    \"address\": {
	        \"city\": \"San Mateo\", 
	        \"country\": \"USA\", 
	        \"region\": \"CA\", 
	        \"line2\": \"Apartment 7\", 
	        \"line1\": \"741 Douglass St\", 
	        \"postal_code\": \"94114\"
	    }, 
	    \"security_code\": \"112\", 
	    \"type\": \"PAYMENT_CARD\", 
	    \"identity\": \"IDcq7bJ4vTXn1RxY5v4UMQ3T\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
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
	    "identity"=> "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	));
$card = $card->save();


```
> Example Response:

```json

	{
	    "instrument_type": "PAYMENT_CARD", 
	    "card_type": "UNKNOWN", 
	    "name": "Dwayne Johnson", 
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
	    "updated_at": "2016-06-02T22:43:39.27Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDcq7bJ4vTXn1RxY5v4UMQ3T"
	        }, 
	        "updates": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI5zCmfsnrvhVvPX9h14r3GJ/updates"
	        }
	    }, 
	    "created_at": "2016-06-02T22:43:39.27Z", 
	    "id": "PI5zCmfsnrvhVvPX9h14r3GJ", 
	    "identity": "IDcq7bJ4vTXn1RxY5v4UMQ3T"
	}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
identity | *string*, **required** | Identity resource which the card is associated. | IDcq7bJ4vTXn1RxY5v4UMQ3T
first_name | *string*, **optional** | Customer's first name on card. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | PAYMENT_CARD
number | *string*, **required** | The digits of the credit card integer. | 1111 111 1111 1111
security_code | *string*, **optional** | The 3-4 digit security code for the card. | 123
expiration_month | *integer*, **required** | Expiration month (e.g. 12 for December). | 11
expiration_year | *integer*, **required** | Expiration year. | 2020
line1 | *string*, **optional** | Street address of the associated card. | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address of the associated card. |  Apt. 3
city | *string*, **optional** | City of the associated card. | San Mateo
region | *string*, **optional** | State of the associated card. | CA
postal_code | *string*, **optional** | Postal of the associated card. | 92704
country | *string*, **optional** | Country of the associated card. | USA
## Create a New Bank Account
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"account_type\": \"SAVINGS\", 
	    \"name\": \"Fran Lemke\", 
	    \"bank_code\": \"123123123\", 
	    \"country\": \"USA\", 
	    \"currency\": \"USD\", 
	    \"account_number\": \"123123123\", 
	    \"type\": \"BANK_ACCOUNT\", 
	    \"identity\": \"IDAyTLs4vrJDCMNp6BFHAGF\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "bank_code"=> "123123123", 
	    "country"=> "USA", 
	    "currency"=> "USD", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDAyTLs4vrJDCMNp6BFHAGF"
	));
$bank_account = $bank_account->save();


```
> Example Response:

```json

	{
	    "instrument_type": "BANK_ACCOUNT", 
	    "masked_account_number": "XXXXX3123", 
	    "name": "Fran Lemke", 
	    "tags": {}, 
	    "country": "USA", 
	    "created_at": "2016-06-02T22:43:34.48Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-02T22:43:34.48Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI2XUFqgEDxT9Q3aUYRcQZTA/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI2XUFqgEDxT9Q3aUYRcQZTA", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-staging.finix.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | IDAyTLs4vrJDCMNp6BFHAGF
account_type | *string*, **required** | Checking or Savings | SAVINGS
type | *string*, **required** | Type of Payment Instrument. For cards input PAYMENT_CARD. | BANK_ACCOUNT
currency | *string*, **optional** | Default currency used when settling funds. | USD
first_name | *string*, **optional** | Customer's first name on bank account. | Dwayne
last_name | *string*, **optional** | Customer's last name on card. | Johnson
full_name | *string*, **optional** | Customer's full name on card. | Dwayne Johnson
country | *string*, **optional** | Country of the associated bank account. | USA
bic | *string*, **optional** | TBD. | foo
iban | *string*, **optional** | International Bank Account integer | foo
company_name | *string*, **optional** | Name of company if the bank account is a company account. |  Bob's Burgers


## Create an Identity Verification

```shell


curl https://api-staging.finix.io/payment_instruments/IDAyTLs4vrJDCMNp6BFHAGF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('DItY913WtRH1hU2oakgf6QRw');

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:43:37.64Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:43:37.67Z", 
	    "id": "VI3vea6eKdRhoaeXAAmf86Q1", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "external_trace_id": "28b097f1-1ac4-469a-8edb-7fd6f949de99", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-staging.finix.io/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1


## Create an Identity Verification

```shell


curl https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USoBmxXjyNWJzEufDtXdbuV8:fe398ca8-bf15-4aa1-bc36-0ff448c77bab \
    -d "
	{
	    \"merchant\": null, 
	    \"instrument\": null, 
	    \"processor\": \"DUMMY_V1\", 
	    \"identity\": null
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USoBmxXjyNWJzEufDtXdbuV8', 'fe398ca8-bf15-4aa1-bc36-0ff448c77bab');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:43:37.64Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:43:37.67Z", 
	    "id": "VI3vea6eKdRhoaeXAAmf86Q1", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VI3vea6eKdRhoaeXAAmf86Q1"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDAyTLs4vrJDCMNp6BFHAGF"
	        }
	    }, 
	    "external_trace_id": "28b097f1-1ac4-469a-8edb-7fd6f949de99", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDAyTLs4vrJDCMNp6BFHAGF"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-staging.finix.io/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1


