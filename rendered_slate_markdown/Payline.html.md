---
title: Payline API Reference

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
-u US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
This guide will demonstrate the main workflows for utilizing the Payline Payments API for platforms and marketplaces. We have language bindings in cURL, PHP, Ruby, Python, C#, Java and Perl! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

To communicate with the Payline API you'll need to authenticate your requests with a username and password. For the sandbox environment you may use the credentials listed below or you can supply your own.

- Username: `US63fB1dhBkr9Ji7J7CKHGJS`

- Password: `a20ee653-8d5b-46cd-823f-2e1623424ed2`

You should also know your Application ID. An Application, also referred as an "App", is a resource that represents your web App or any service that connects customers (i.e. buyers) and merchants (i.e. sellers). For the sandbox environment you may use the following ID:

- App ID: `AP43Ds6QHdgLmEyBYV8LKC9n`


## Create an Identity for a Merchant

```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
	        \"doing_business_as\": \"ACME Anchors\", 
	        \"annual_card_volume\": 12000000, 
	        \"default_statement_descriptor\": \"ACME Anchors\", 
	        \"url\": \"www.ACMEAnchors.com\", 
	        \"business_name\": \"ACME Anchors\", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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
	        "doing_business_as"=> "ACME Anchors", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "ACME Anchors", 
	        "url"=> "www.ACMEAnchors.com", 
	        "business_name"=> "ACME Anchors", 
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
	    "created_at": "2016-06-02T22:46:33.37Z", 
	    "updated_at": "2016-06-02T22:46:33.37Z", 
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
	        "default_statement_descriptor": "ACME Anchors", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "ACME Anchors", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.ACMEAnchors.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "ACME Anchors", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx"
	        }, 
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/merchants"
	        }
	    }, 
	    "id": "ID2bMtfRQKSw53Dnpf9P9Vtx"
	}
```

Before we can charge a card we need to create an Identity resource. An Identity represents a person or business. In this case, the Identity will represent the merchant (i.e. seller). Let's create one now.You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Create a New Bank Account
```shell

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"account_type\": \"SAVINGS\", 
	    \"name\": \"Fran Lemke\", 
	    \"bank_code\": \"123123123\", 
	    \"country\": \"USA\", 
	    \"currency\": \"USD\", 
	    \"account_number\": \"123123123\", 
	    \"type\": \"BANK_ACCOUNT\", 
	    \"identity\": \"ID67gisxSME8z41TMT6cWWxE\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
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
	    "identity"=> "ID67gisxSME8z41TMT6cWWxE"
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
	    "created_at": "2016-06-02T22:46:41.35Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-02T22:46:41.35Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK"
	        }, 
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI5Ky7h3oXxyzfJaDkBkotLK", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```
<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | ID67gisxSME8z41TMT6cWWxE
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


curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:45.00Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:46:45.02Z", 
	    "id": "VIrdCttxzXJY1fwPqYmC6A1M", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "external_trace_id": "6a524f4f-dca3-4583-8085-771b5dd42635", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Before, being able to process funds to this seller we will need to perform an identity verification to underwrite them as a Merchant. Only underwritten Identities can be paid out per KYC regulations.


## Provision Merchant Account
```shell

curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
> Example Response:

```json

	{
	    "created_at": "2016-06-02T22:46:43.58Z", 
	    "updated_at": "2016-06-02T22:46:43.58Z", 
	    "id": "MU6nckETwS86JUaSC3mVJ7Zd", 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/merchants/MU6nckETwS86JUaSC3mVJ7Zd"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-test.payline.io/merchant_profiles/MPxfA4dJhiJvYuPhuGXhYA6J"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/merchants/MU6nckETwS86JUaSC3mVJ7Zd/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "verification": {
	            "href": "https://api-test.payline.io/verifications/VIdWeeRKuzXdd2V4rDz4uzzp"
	        }
	    }, 
	    "verification": "VIdWeeRKuzXdd2V4rDz4uzzp", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPxfA4dJhiJvYuPhuGXhYA6J", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Once the Identity has been verified, Payline will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.

## Create an Identity for a Buyer (i.e. buyer)
```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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
	    "created_at": "2016-06-02T22:46:45.87Z", 
	    "updated_at": "2016-06-02T22:46:45.87Z", 
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
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs"
	        }, 
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/merchants"
	        }
	    }, 
	    "id": "ID86ZjMvTqhCJftxQ5SwRCzs"
	}
```
This next step should sound familiar. Let's create an Identity to represent the buyer. You'll want to store the ID of the newly created Identity resource as you'll reference it later.


## Create a Payment Instrument (i.e. card)
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
	    \"identity\": \"ID86ZjMvTqhCJftxQ5SwRCzs\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "ID86ZjMvTqhCJftxQ5SwRCzs"
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
	    "updated_at": "2016-06-02T22:46:46.68Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs"
	        }, 
	        "updates": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/updates"
	        }
	    }, 
	    "created_at": "2016-06-02T22:46:46.68Z", 
	    "id": "PIsbuEdmifSPuucPYasovecf", 
	    "identity": "ID86ZjMvTqhCJftxQ5SwRCzs"
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


curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"fee\": 10, 
	    \"currency\": \"USD\", 
	    \"merchant_identity\": \"ID67gisxSME8z41TMT6cWWxE\", 
	    \"source\": \"PIsbuEdmifSPuucPYasovecf\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "ID67gisxSME8z41TMT6cWWxE", 
	    "source"=> "PIsbuEdmifSPuucPYasovecf", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```

> Example Response:

```json

	{
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "destination": "PIvo5YHR2n4YUdjVxZMjLrHa", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:46:48.06Z", 
	    "created_at": "2016-06-02T22:46:47.96Z", 
	    "tags": {}, 
	    "trace_id": "c57e0ec1-1655-4d3f-b8be-70f6d7067e14", 
	    "statement_descriptor": "PLD*LEE SANDWHICHES", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW"
	        }, 
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvo5YHR2n4YUdjVxZMjLrHa"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/disputes"
	        }
	    }, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "type": "DEBIT", 
	    "id": "TR7GEU5xuY6g6Ygz1xZJb2PW"
	}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.


## Reverse the Transfer (i.e. issue a refund)
```shell

curl https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d  "
	  {
	  \"refund_amount\" : 100
  	}		
	"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```

> Example Response:

```json

	{
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "destination": "PIsbuEdmifSPuucPYasovecf", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:48:21.15Z", 
	    "created_at": "2016-06-02T22:48:21.03Z", 
	    "tags": {}, 
	    "trace_id": "9d9c7a0b-69d0-452c-bec0-68837e4905e0", 
	    "statement_descriptor": "PLD*LEE SANDWHICHES", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR9YVHLnhjHdLY9koxnspsw3"
	        }, 
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR9YVHLnhjHdLY9koxnspsw3/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW"
	        }
	    }, 
	    "source": "PIvo5YHR2n4YUdjVxZMjLrHa", 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "type": "REVERSAL", 
	    "id": "TR9YVHLnhjHdLY9koxnspsw3"
	}
```

What if we need to issue a refund to the buyer? First, you'll need to take the previously stored Transfer ID and interpolate it into the following url path. The amount can be equal to or less than the original debit.

## Settle out funds to a Merchant
```shell

curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"currency\": \"USD\", 
	    \"processor\": \"DUMMY_V1\"
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');
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
	    "created_at": "2016-06-02T22:49:25.27Z", 
	    "updated_at": "2016-06-02T22:49:25.27Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STbULpWdK7mgK9yvGjnXDYbd", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Awesome! Now you know how to charge a card and reverse the debit.

Now you need to settle out the funds to your merchant. To do so you will create a Settlement resource. Each settlement is comprised of all the Transfers that have a SUCCEEDED state and that have not been previously settled out.
# Tokenization.js
To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js, keeps you out of the PCI scope by sending sensitive payment information over SSL directly to the Payline servers.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/sab76Lne/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Payline API.
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
    server: "https://api-test.payline.io",
    applicationId: "AP43Ds6QHdgLmEyBYV8LKC9n",
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
server | *string*, **required** |  The base url for the Payline API| https://api-test.payline.io
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | AP43Ds6QHdgLmEyBYV8LKC9n
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
    "id": "TKaQfUQhFUeyJPzTkdQM7sCc",
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



curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"token\": \"TKaQfUQhFUeyJPzTkdQM7sCc\", 
	    \"type\": \"TOKEN\", 
	    \"identity\": \"ID67gisxSME8z41TMT6cWWxE\"
	}"


> Example Response:

json

	{
	    "instrument_type": "TOKEN", 
	    "tags": {}, 
	    "created_at": "2016-06-02T22:49:26.92Z", 
	    "updated_at": "2016-06-02T22:49:26.92Z", 
	    "token": "TKaQfUQhFUeyJPzTkdQM7sCc", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PIbE4DXw4CLN1Dm8Au7QpW1h/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PIbE4DXw4CLN1Dm8Au7QpW1h"
	        }, 
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PIbE4DXw4CLN1Dm8Au7QpW1h/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PIbE4DXw4CLN1Dm8Au7QpW1h/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "fingerprint": "FPR2017699798", 
	    "id": "PIbE4DXw4CLN1Dm8Au7QpW1h", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}

Before you can use the newly tokenized card or bank account you will need to associate it with an Identity. To do this you must make an authenticated POST request to `https://api-test.payline.io/payment_instruments` like demonstrated to the right.

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`
# Authorizations
An Authorization resource (also known as a card hold) reserves a specific amount on a card to be captured (debited) at a later date, usually within 7 days. When an Authorization is captured it produces a Transfer resource.


## Create a New Authorization
```shell

curl https://api-test.payline.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"merchant_identity\": \"ID67gisxSME8z41TMT6cWWxE\", 
	    \"currency\": \"USD\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\", 
	    \"source\": \"PIsbuEdmifSPuucPYasovecf\"
	}"



```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "ID67gisxSME8z41TMT6cWWxE", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PIsbuEdmifSPuucPYasovecf"
	));
$authorization = $authorization->save();

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:48:22.24Z", 
	    "trace_id": "e3301221-eddb-4c02-ad52-09e1dde2cafe", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:48:22.24Z", 
	    "updated_at": "2016-06-02T22:48:22.25Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU5yExS7eGwGxhywcUEd6nkT"
	        }
	    }, 
	    "id": "AU5yExS7eGwGxhywcUEd6nkT"
	}
```

### HTTP Request

`POST https://api-test.payline.io/authorizations`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PIsbuEdmifSPuucPYasovecf
merchant_identity | *string*, **required** | UID. | ID67gisxSME8z41TMT6cWWxE
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Capture an Authorization

```shell

curl https://api-test.payline.io/authorizations/AU5yExS7eGwGxhywcUEd6nkT \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU5yExS7eGwGxhywcUEd6nkT');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "transfer": "TRvaYidxM487KZYLJ262JnS2", 
	    "created_at": "2016-06-02T22:48:22.10Z", 
	    "trace_id": "e3301221-eddb-4c02-ad52-09e1dde2cafe", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:48:22.10Z", 
	    "updated_at": "2016-06-02T22:48:22.10Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRvaYidxM487KZYLJ262JnS2"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU5yExS7eGwGxhywcUEd6nkT"
	        }
	    }, 
	    "id": "AU5yExS7eGwGxhywcUEd6nkT"
	}
```

### HTTP Request

`PUT https://api-test.payline.io/authorizations/authorization_id`

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

curl https://api-test.payline.io/authorizations/AU5yExS7eGwGxhywcUEd6nkT \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU5yExS7eGwGxhywcUEd6nkT');

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "transfer": "TRvaYidxM487KZYLJ262JnS2", 
	    "created_at": "2016-06-02T22:48:22.10Z", 
	    "trace_id": "e3301221-eddb-4c02-ad52-09e1dde2cafe", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-09T22:48:22.10Z", 
	    "updated_at": "2016-06-02T22:48:22.10Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRvaYidxM487KZYLJ262JnS2"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/authorizations/AU5yExS7eGwGxhywcUEd6nkT"
	        }
	    }, 
	    "id": "AU5yExS7eGwGxhywcUEd6nkT"
	}
```

### HTTP Request

`GET https://api-test.payline.io/authorizations/authorization_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


# Disputes
Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute
```shell

curl https://api-test.payline.io/disputes/DI6FGa3YkpkANkpxj1XX9QQy \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DI6FGa3YkpkANkpxj1XX9QQy');

```
> Example Response:

```json

	{
	    "state": "PENDING", 
	    "transfer": "TRb38YFXh2Hk1XemMELKRJRM", 
	    "created_at": "2016-06-02T22:47:01.21Z", 
	    "tags": {}, 
	    "occurred_at": "2016-06-02T22:46:49.09Z", 
	    "amount": 0, 
	    "updated_at": "2016-06-02T22:47:01.21Z", 
	    "reason": "FRAUD", 
	    "_links": {
	        "transfer": {
	            "href": "https://api-test.payline.io/transfers/TRb38YFXh2Hk1XemMELKRJRM"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/disputes/DI6FGa3YkpkANkpxj1XX9QQy"
	        }, 
	        "evidence": {
	            "href": "https://api-test.payline.io/disputes/DI6FGa3YkpkANkpxj1XX9QQy/evidence"
	        }
	    }, 
	    "respond_by": "2016-06-09T22:47:01.39Z", 
	    "id": "DI6FGa3YkpkANkpxj1XX9QQy", 
	    "identity": "ID86ZjMvTqhCJftxQ5SwRCzs"
	}
```

### HTTP Request

`GET https://api-test.payline.io/disputes/dispute_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
dispute_id | ID of the Dispute

# Identities
An Identity resource represents a business or person. Payment Instrument resources may be associated to an Identity.

## Create an Identity for a Buyer
All fields for a buyer's Identity are optional. However, a business_type field should not be passed. Passing a business_type indicates that the Identity should be treated as a merchant.

```shell


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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
	    "created_at": "2016-06-02T22:46:45.87Z", 
	    "updated_at": "2016-06-02T22:46:45.87Z", 
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
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs"
	        }, 
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs/merchants"
	        }
	    }, 
	    "id": "ID86ZjMvTqhCJftxQ5SwRCzs"
	}
```

### HTTP Request

`POST https://api-test.payline.io/identities`

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


curl https://api-test.payline.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
	        \"doing_business_as\": \"ACME Anchors\", 
	        \"annual_card_volume\": 12000000, 
	        \"default_statement_descriptor\": \"ACME Anchors\", 
	        \"url\": \"www.ACMEAnchors.com\", 
	        \"business_name\": \"ACME Anchors\", 
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

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
	        "doing_business_as"=> "ACME Anchors", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "ACME Anchors", 
	        "url"=> "www.ACMEAnchors.com", 
	        "business_name"=> "ACME Anchors", 
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
	    "created_at": "2016-06-02T22:46:33.37Z", 
	    "updated_at": "2016-06-02T22:46:33.37Z", 
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
	        "default_statement_descriptor": "ACME Anchors", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "ACME Anchors", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.ACMEAnchors.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "ACME Anchors", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx"
	        }, 
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/ID2bMtfRQKSw53Dnpf9P9Vtx/merchants"
	        }
	    }, 
	    "id": "ID2bMtfRQKSw53Dnpf9P9Vtx"
	}
```

### HTTP Request

`POST https://api-test.payline.io/identities`

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

curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');
```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-02T22:46:32.44Z", 
	    "updated_at": "2016-06-02T22:46:32.44Z", 
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
	        "default_statement_descriptor": "Lee Sandwhiches", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Lee Sandwhiches", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.LeeSandwhiches.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Lee Sandwhiches", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "settlements": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/merchants"
	        }
	    }, 
	    "id": "ID67gisxSME8z41TMT6cWWxE"
	}
```

### HTTP Request

`GET https://api-test.payline.io/identities/identity_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

## Underwrite an Identity

```shell

curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```

> Example Response:

```json

	{
	    "created_at": "2016-06-02T22:46:43.58Z", 
	    "updated_at": "2016-06-02T22:46:43.58Z", 
	    "id": "MU6nckETwS86JUaSC3mVJ7Zd", 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/merchants/MU6nckETwS86JUaSC3mVJ7Zd"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-test.payline.io/merchant_profiles/MPxfA4dJhiJvYuPhuGXhYA6J"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/merchants/MU6nckETwS86JUaSC3mVJ7Zd/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "verification": {
	            "href": "https://api-test.payline.io/verifications/VIdWeeRKuzXdd2V4rDz4uzzp"
	        }
	    }, 
	    "verification": "VIdWeeRKuzXdd2V4rDz4uzzp", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPxfA4dJhiJvYuPhuGXhYA6J", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Underwrite a previously created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/merchants`

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


curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:45.00Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:46:45.02Z", 
	    "id": "VIrdCttxzXJY1fwPqYmC6A1M", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "external_trace_id": "6a524f4f-dca3-4583-8085-771b5dd42635", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/verifications`


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

curl https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Verification;

$verification = Verification::retrieve('VIrdCttxzXJY1fwPqYmC6A1M');

```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:44.89Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:46:44.89Z", 
	    "id": "VIrdCttxzXJY1fwPqYmC6A1M", 
	    "instrument": null, 
	    "state": "SUCCEEDED", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "external_trace_id": "6a524f4f-dca3-4583-8085-771b5dd42635", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

### HTTP Request

`GET https://api-test.payline.io/verifications/verification_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
verification_id | ID of the Identity Verification

# Settlements
A Settlement resource represents a collection of Transfers that are to be paid out to a specific Merchant.


## Create a New Settlement
```shell

curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"currency\": \"USD\", 
	    \"processor\": \"DUMMY_V1\"
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('ID67gisxSME8z41TMT6cWWxE');
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
	    "created_at": "2016-06-02T22:49:25.27Z", 
	    "updated_at": "2016-06-02T22:49:25.27Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STbULpWdK7mgK9yvGjnXDYbd", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

### HTTP Request

`POST https://api-test.payline.io/identities/:identity_id/settlements`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1
currency | *integer*, **required** | The currency for the settlement. | USD


## Fetch a Settlement

```shell


curl https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STbULpWdK7mgK9yvGjnXDYbd');

```
> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-02T22:49:25.16Z", 
	    "updated_at": "2016-06-02T22:49:25.16Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/settlements/STbULpWdK7mgK9yvGjnXDYbd"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STbULpWdK7mgK9yvGjnXDYbd", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Fetch a previously created Settlement.

### HTTP Request

`POST https://api-test.payline.io/settlements/settlement_id/`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
settlement_id | ID of the Settlment

# Transfers
A Transfer resource represents any omnidirectional flow of funds. Transfers can represent either a debit to a card, a credit to a bank account, or a refund to a card depending on the request. Transfers have a state attribute representing the current state of the transaction. There are three possible status values: PENDING, SUCCEEDED, or FAILED.

## Debit a Card

```shell


curl https://api-test.payline.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"fee\": 10, 
	    \"currency\": \"USD\", 
	    \"merchant_identity\": \"ID67gisxSME8z41TMT6cWWxE\", 
	    \"source\": \"PIsbuEdmifSPuucPYasovecf\", 
	    \"amount\": 100, 
	    \"processor\": \"DUMMY_V1\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "ID67gisxSME8z41TMT6cWWxE", 
	    "source"=> "PIsbuEdmifSPuucPYasovecf", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```


> Example Response:

```json

	{
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "destination": "PIvo5YHR2n4YUdjVxZMjLrHa", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:46:48.06Z", 
	    "created_at": "2016-06-02T22:46:47.96Z", 
	    "tags": {}, 
	    "trace_id": "c57e0ec1-1655-4d3f-b8be-70f6d7067e14", 
	    "statement_descriptor": "PLD*LEE SANDWHICHES", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW"
	        }, 
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvo5YHR2n4YUdjVxZMjLrHa"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/disputes"
	        }
	    }, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "type": "DEBIT", 
	    "id": "TR7GEU5xuY6g6Ygz1xZJb2PW"
	}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST https://api-test.payline.io/transfers`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PIsbuEdmifSPuucPYasovecf
merchant_identity | *string*, **required** | UID. | ID67gisxSME8z41TMT6cWWxE
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Refund a Debit
```shell

curl https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d  "
	  {
	  \"refund_amount\" : 100
  	}		
	"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TR7GEU5xuY6g6Ygz1xZJb2PW');
$refund = $debit->reverse(50);
```


> Example Response:

```json

	{
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "destination": "PIsbuEdmifSPuucPYasovecf", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-02T22:48:21.15Z", 
	    "created_at": "2016-06-02T22:48:21.03Z", 
	    "tags": {}, 
	    "trace_id": "9d9c7a0b-69d0-452c-bec0-68837e4905e0", 
	    "statement_descriptor": "PLD*LEE SANDWHICHES", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR9YVHLnhjHdLY9koxnspsw3"
	        }, 
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR9YVHLnhjHdLY9koxnspsw3/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW"
	        }
	    }, 
	    "source": "PIvo5YHR2n4YUdjVxZMjLrHa", 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "type": "REVERSAL", 
	    "id": "TR9YVHLnhjHdLY9koxnspsw3"
	}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

### HTTP Request

`POST https://api-test.payline.io/transfers/transfer_id/reversals`

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

curl https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TR7GEU5xuY6g6Ygz1xZJb2PW');



```
> Example Response:

```json

	{
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "destination": "PIvo5YHR2n4YUdjVxZMjLrHa", 
	    "state": "SUCCEEDED", 
	    "updated_at": "2016-06-02T22:46:47.81Z", 
	    "created_at": "2016-06-02T22:46:47.81Z", 
	    "tags": {}, 
	    "trace_id": "c57e0ec1-1655-4d3f-b8be-70f6d7067e14", 
	    "statement_descriptor": "PLD*LEE SANDWHICHES", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW"
	        }, 
	        "destination": {
	            "href": "https://api-test.payline.io/payment_instruments/PIvo5YHR2n4YUdjVxZMjLrHa"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "disputes": {
	            "href": "https://api-test.payline.io/transfers/TR7GEU5xuY6g6Ygz1xZJb2PW/disputes"
	        }
	    }, 
	    "source": "PIsbuEdmifSPuucPYasovecf", 
	    "merchant_identity": "ID67gisxSME8z41TMT6cWWxE", 
	    "type": "DEBIT", 
	    "id": "TR7GEU5xuY6g6Ygz1xZJb2PW"
	}
```

### HTTP Request

`GET https://api-test.payline.io/transfers/transfer_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the Transfer


# Webhooks
Webhooks allow you to build or set up integrations which subscribe to certain events on the Payline API. When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL. Webhooks are particularly useful for updating asynchronous state changes in Transfers or notifications of newly created Disputes.

## Create a New Webhook
```shell

curl https://api-test.payline.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	            {
	            \"url\" : \"http://requestb.in/vts8mpvt\"
	            }
	        "

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-06-02T22:46:31.82Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-02T22:46:31.82Z", 
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/webhooks/WHoLHVB5Kk5dmYE1rWsx7urw"
	        }
	    }, 
	    "id": "WHoLHVB5Kk5dmYE1rWsx7urw"
	}
```

### HTTP Request

`POST https://api-test.payline.io/webhooks`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
url | *string*, **required** | The HTTP or HTTPS url the callbacks will be made to | https://examplesite.com


## Retrieve a Webhook

```shell



curl https://api-test.payline.io/webhooks/WHoLHVB5Kk5dmYE1rWsx7urw \
    -H "Content-Type: application/vnd.json+api" \
    -u US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHoLHVB5Kk5dmYE1rWsx7urw');



```

> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-06-02T22:46:31.82Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-02T22:46:31.82Z", 
	    "application": "AP43Ds6QHdgLmEyBYV8LKC9n", 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/webhooks/WHoLHVB5Kk5dmYE1rWsx7urw"
	        }
	    }, 
	    "id": "WHoLHVB5Kk5dmYE1rWsx7urw"
	}
```

### HTTP Request

`GET https://api-test.payline.io/webhooks/webhook_id`

### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
webhook_id | ID of the Webhook

# Payment Instruments
A Payment Instrument resource represents either a credit card or bank account. All information is securely vaulted and referenced by an ID. A Payment Instrument may be created multiple times, and each tokenization produces a unique ID. Each ID may only be associated one time and to only one Identity. Once associated, a Payment Instrument may not be disassociated from an Identity.


## Create a New Card
```shell


curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
	    \"identity\": \"ID86ZjMvTqhCJftxQ5SwRCzs\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

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
	    "identity"=> "ID86ZjMvTqhCJftxQ5SwRCzs"
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
	    "updated_at": "2016-06-02T22:46:46.68Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID86ZjMvTqhCJftxQ5SwRCzs"
	        }, 
	        "updates": {
	            "href": "https://api-test.payline.io/payment_instruments/PIsbuEdmifSPuucPYasovecf/updates"
	        }
	    }, 
	    "created_at": "2016-06-02T22:46:46.68Z", 
	    "id": "PIsbuEdmifSPuucPYasovecf", 
	    "identity": "ID86ZjMvTqhCJftxQ5SwRCzs"
	}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
identity | *string*, **required** | Identity resource which the card is associated. | ID86ZjMvTqhCJftxQ5SwRCzs
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

curl https://api-test.payline.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
    -d "
	{
	    \"account_type\": \"SAVINGS\", 
	    \"name\": \"Fran Lemke\", 
	    \"bank_code\": \"123123123\", 
	    \"country\": \"USA\", 
	    \"currency\": \"USD\", 
	    \"account_number\": \"123123123\", 
	    \"type\": \"BANK_ACCOUNT\", 
	    \"identity\": \"ID67gisxSME8z41TMT6cWWxE\"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
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
	    "identity"=> "ID67gisxSME8z41TMT6cWWxE"
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
	    "created_at": "2016-06-02T22:46:41.35Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-02T22:46:41.35Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/transfers"
	        }, 
	        "self": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK"
	        }, 
	        "authorizations": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-test.payline.io/payment_instruments/PI5Ky7h3oXxyzfJaDkBkotLK/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI5Ky7h3oXxyzfJaDkBkotLK", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

### HTTP Request

`POST https://api-test.payline.io/payment_instruments`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | ID67gisxSME8z41TMT6cWWxE
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


curl https://api-test.payline.io/payment_instruments/ID67gisxSME8z41TMT6cWWxE/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();

use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('DI6FGa3YkpkANkpxj1XX9QQy');

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:45.00Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:46:45.02Z", 
	    "id": "VIrdCttxzXJY1fwPqYmC6A1M", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "external_trace_id": "6a524f4f-dca3-4583-8085-771b5dd42635", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/verifications`


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


curl https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US63fB1dhBkr9Ji7J7CKHGJS:a20ee653-8d5b-46cd-823f-2e1623424ed2 \
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
require(__DIR__ . '/src/Payline/Settings.php');
Payline\Settings::configure('https://api-test.payline.io', 'US63fB1dhBkr9Ji7J7CKHGJS', 'a20ee653-8d5b-46cd-823f-2e1623424ed2');
require(__DIR__ . '/src/Payline/Bootstrap.php');
Payline\Bootstrap::init();


```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-02T22:46:45.00Z", 
	    "messages": [], 
	    "updated_at": "2016-06-02T22:46:45.02Z", 
	    "id": "VIrdCttxzXJY1fwPqYmC6A1M", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-test.payline.io/verifications/VIrdCttxzXJY1fwPqYmC6A1M"
	        }, 
	        "identity": {
	            "href": "https://api-test.payline.io/identities/ID67gisxSME8z41TMT6cWWxE"
	        }
	    }, 
	    "external_trace_id": "6a524f4f-dca3-4583-8085-771b5dd42635", 
	    "processor": "DUMMY_V1", 
	    "identity": "ID67gisxSME8z41TMT6cWWxE"
	}
```

Perform an identity verification check against a previously created Identity.

### HTTP Request

`POST https://api-test.payline.io/identities/identity_id/verifications`


### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1


