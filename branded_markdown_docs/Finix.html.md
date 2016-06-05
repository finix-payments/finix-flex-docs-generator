---
title: Finix API Reference

language_tabs:
  - shell: cURL
  - php: PHP
  - java: Java

includes:
  - errors

search: true
---

# Guides


## Getting Started
```shell


# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

```
This guide will demonstrate the main workflows for utilizing the Finix Payments API for platforms and marketplaces. We have language bindings in cURL, PHP, Ruby, Python, C#, Java and Perl! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

To communicate with the Finix API you'll need to authenticate your requests with a username and password. For the sandbox environment you may use the credentials listed below or you can supply your own.

- Username: `USqyhyT9n9QeeLbh63kYTWBN`

- Password: `7e5c303e-c9c4-4899-9274-3962786d084a`

You should also know your Application ID. An Application, also referred as an "App", is a resource that represents your web App or any service that connects customers (i.e. buyers) and merchants (i.e. sellers). For the sandbox environment you may use the following ID:

- App ID: `AP7v8pfY36AzsGMdWB2wB37j`


## Create an Identity for a Merchant

```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "phone": "1234567890", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "mcc": "0742", 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "max_transaction_amount": 120000, 
	        "principal_percentage_ownership": 100, 
	        "doing_business_as": "Pollos Hermanos", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Pollos Hermanos", 
	        "url": "www.PollosHermanos.com", 
	        "business_name": "Pollos Hermanos", 
	        "incorporation_date": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "business_tax_id": "123456789", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
	        "url"=> "www.PollosHermanos.com", 
	        "business_name"=> "Pollos Hermanos", 
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
```java

import io.finix.payments.processing.client.model.Identity;

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
	    "created_at": "2016-06-05T22:57:03.47Z", 
	    "updated_at": "2016-06-05T22:57:03.47Z", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "title": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Pollos Hermanos", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Pollos Hermanos", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.PollosHermanos.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Pollos Hermanos", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/merchants"
	        }
	    }, 
	    "id": "IDgjCAM3iEYELUG4rTwM6Bof"
	}
```

Before we can charge a card we need to create an Identity resource. An Identity represents a person or business. In this case, the Identity will represent the merchant (i.e. seller). Let's create one now.You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Create a New Bank Account
```shell

curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d "
	{
	    "account_type": "SAVINGS", 
	    "name": "Fran Lemke", 
	    "bank_code": "123123123", 
	    "country": "USA", 
	    "currency": "USD", 
	    "account_number": "123123123", 
	    "type": "BANK_ACCOUNT", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
	}"


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	    "identity"=> "IDeVSYLXEjpQu3i61phpmAcg"
	));
$bank_account = $bank_account->save();


```
```java

import io.finix.payments.processing.client.model.BankAccount;

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
	    "created_at": "2016-06-05T22:57:13.24Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-05T22:57:13.24Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI7qk1L9ArF6mGJX7vkL5gAz", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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
identity | *string*, **required**| Identity resource which the bank account is associated. | IDeVSYLXEjpQu3i61phpmAcg
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


curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "merchant": null, 
	    "instrument": null, 
	    "processor": "DUMMY_V1", 
	    "identity": null
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
```java

import io.finix.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);

```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-05T22:57:16.63Z", 
	    "messages": [], 
	    "updated_at": "2016-06-05T22:57:16.66Z", 
	    "id": "VItwb6F6coPggxCHuuf9avP8", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "external_trace_id": "2512e759-d604-49b0-a9d8-4dc352dad5c3", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
	}
```

Before, being able to process funds to this seller we will need to perform an identity verification to underwrite them as a Merchant. Only underwritten Identities can be paid out per KYC regulations.


## Provision Merchant Account
```shell

curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "processor": "DUMMY_V1"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
```java

import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());

```
> Example Response:

```json

	{
	    "created_at": "2016-06-05T22:57:14.97Z", 
	    "updated_at": "2016-06-05T22:57:14.97Z", 
	    "id": "MUeAWuBZa8vUtQUCpBXpZDcd", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/merchants/MUeAWuBZa8vUtQUCpBXpZDcd"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-staging.finix.io/merchant_profiles/MPid2GHckexaQotpgUSzNwwp"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/merchants/MUeAWuBZa8vUtQUCpBXpZDcd/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "verification": {
	            "href": "https://api-staging.finix.io/verifications/VI6rgh8i7gTpq1AxrNRQ3x7t"
	        }
	    }, 
	    "verification": "VI6rgh8i7gTpq1AxrNRQ3x7t", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPid2GHckexaQotpgUSzNwwp", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
	}
```

Once the Identity has been verified, Finix will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.

## Create an Identity for a Buyer (i.e. buyer)
```shell


curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "first_name": "Dwayne", 
	        "last_name": "Johnson"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
```java

import io.finix.payments.processing.client.model.Identity;

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
	    "created_at": "2016-06-05T22:57:17.50Z", 
	    "updated_at": "2016-06-05T22:57:17.50Z", 
	    "entity": {
	        "business_type": null, 
	        "business_phone": null, 
	        "first_name": "Dwayne", 
	        "last_name": "Johnson", 
	        "amex_mid": null, 
	        "title": null, 
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
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/merchants"
	        }
	    }, 
	    "id": "IDmFNoDYZeioNCgEyk3kFPV2"
	}
```
This next step should sound familiar. Let's create an Identity to represent the buyer. You'll want to store the ID of the newly created Identity resource as you'll reference it later.


## Create a Payment Instrument (i.e. card)
```shell


curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
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
	    "identity": "IDmFNoDYZeioNCgEyk3kFPV2"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	    "identity"=> "IDmFNoDYZeioNCgEyk3kFPV2"
	));
$card = $card->save();


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
	    "updated_at": "2016-06-05T22:57:18.28Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2"
	        }, 
	        "updates": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/updates"
	        }
	    }, 
	    "created_at": "2016-06-05T22:57:18.28Z", 
	    "id": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "identity": "IDmFNoDYZeioNCgEyk3kFPV2"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "fee": 10, 
	    "currency": "USD", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "amount": 100, 
	    "processor": "DUMMY_V1"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDeVSYLXEjpQu3i61phpmAcg", 
	    "source"=> "PIntahNnMqaxdDnwkC5oYrb6", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```
```java

import io.finix.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);

```

> Example Response:

```json

	{
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "destination": "PIaZMcu221Whh9tBgEtjZ7Ld", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-05T22:57:19.71Z", 
	    "created_at": "2016-06-05T22:57:19.55Z", 
	    "tags": {}, 
	    "trace_id": "c76addd8-95e1-40d6-87a4-f9629ae4c084", 
	    "statement_descriptor": "FNX*GOLDS GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIaZMcu221Whh9tBgEtjZ7Ld"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/disputes"
	        }
	    }, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "type": "DEBIT", 
	    "id": "TR6it2JUNoFd8faSkqYzyEGt"
	}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.


## Reverse the Transfer (i.e. issue a refund)
```shell

curl https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

import io.finix.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```

> Example Response:

```json

	{
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "destination": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-05T22:58:53.27Z", 
	    "created_at": "2016-06-05T22:58:53.13Z", 
	    "tags": {}, 
	    "trace_id": "bd0de806-cacc-466c-9ef0-a4df3e0ec05a", 
	    "statement_descriptor": "FNX*GOLDS GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRat3P2xTvZA56LjLMhXakhU"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRat3P2xTvZA56LjLMhXakhU/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt"
	        }
	    }, 
	    "source": "PIaZMcu221Whh9tBgEtjZ7Ld", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "type": "REVERSAL", 
	    "id": "TRat3P2xTvZA56LjLMhXakhU"
	}
```

What if we need to issue a refund to the buyer? First, you'll need to take the previously stored Transfer ID and interpolate it into the following url path. The amount can be equal to or less than the original debit.

## Settle out funds to a Merchant
```shell

curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)

```
> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-05T22:59:58.64Z", 
	    "updated_at": "2016-06-05T22:59:58.65Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STw6kgajsRAqjmhNVUPdmpN3", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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
    applicationId: "AP7v8pfY36AzsGMdWB2wB37j",
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
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | AP7v8pfY36AzsGMdWB2wB37j
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
    "id": "TK78eYSSyqqxzjqefZt5PhoQ",
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d "
	{
	    "token": "TK78eYSSyqqxzjqefZt5PhoQ", 
	    "type": "TOKEN", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
	}"


> Example Response:

json

	{
	    "instrument_type": "TOKEN", 
	    "tags": {}, 
	    "created_at": "2016-06-05T23:00:00.78Z", 
	    "updated_at": "2016-06-05T23:00:00.78Z", 
	    "token": "TK78eYSSyqqxzjqefZt5PhoQ", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIkj6pWmmsoSZJyLKLhXUZPV/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIkj6pWmmsoSZJyLKLhXUZPV"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIkj6pWmmsoSZJyLKLhXUZPV/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIkj6pWmmsoSZJyLKLhXUZPV/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "fingerprint": "FPR-2015343239", 
	    "id": "PIkj6pWmmsoSZJyLKLhXUZPV", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "currency": "USD", 
	    "amount": 100, 
	    "processor": "DUMMY_V1", 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6"
	}'



```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDeVSYLXEjpQu3i61phpmAcg", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PIntahNnMqaxdDnwkC5oYrb6"
	));
$authorization = $authorization->save();

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .processor("DUMMY_V1")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "transfer": null, 
	    "created_at": "2016-06-05T22:58:54.65Z", 
	    "trace_id": "82e84887-9b9e-4879-88a0-0de1ab8f76cd", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-12T22:58:54.65Z", 
	    "updated_at": "2016-06-05T22:58:54.67Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUwX5rkz4dKAHR2oxXuPqs1f"
	        }
	    }, 
	    "id": "AUwX5rkz4dKAHR2oxXuPqs1f"
	}
```

### HTTP Request

`POST https://api-staging.finix.io/authorizations`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PIntahNnMqaxdDnwkC5oYrb6
merchant_identity | *string*, **required** | UID. | IDeVSYLXEjpQu3i61phpmAcg
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Capture an Authorization

```shell

curl https://api-staging.finix.io/authorizations/AUwX5rkz4dKAHR2oxXuPqs1f \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
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
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUwX5rkz4dKAHR2oxXuPqs1f');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUwX5rkz4dKAHR2oxXuPqs1f");
authorization = authorization.capture(50L);

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "transfer": "TR5rwD6zDxajnoPEbvf59ybQ", 
	    "created_at": "2016-06-05T22:58:54.50Z", 
	    "trace_id": "82e84887-9b9e-4879-88a0-0de1ab8f76cd", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-12T22:58:54.50Z", 
	    "updated_at": "2016-06-05T22:58:54.50Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TR5rwD6zDxajnoPEbvf59ybQ"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUwX5rkz4dKAHR2oxXuPqs1f"
	        }
	    }, 
	    "id": "AUwX5rkz4dKAHR2oxXuPqs1f"
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

curl https://api-staging.finix.io/authorizations/AUwX5rkz4dKAHR2oxXuPqs1f \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Authorization;

$authorization = Authorization::retrieve('AUwX5rkz4dKAHR2oxXuPqs1f');

```
```java

import io.finix.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("AUwX5rkz4dKAHR2oxXuPqs1f");

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "transfer": "TR5rwD6zDxajnoPEbvf59ybQ", 
	    "created_at": "2016-06-05T22:58:54.50Z", 
	    "trace_id": "82e84887-9b9e-4879-88a0-0de1ab8f76cd", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-06-12T22:58:54.50Z", 
	    "updated_at": "2016-06-05T22:58:54.50Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TR5rwD6zDxajnoPEbvf59ybQ"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/authorizations/AUwX5rkz4dKAHR2oxXuPqs1f"
	        }
	    }, 
	    "id": "AUwX5rkz4dKAHR2oxXuPqs1f"
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

curl https://api-staging.finix.io/disputes/DIvd18AYSNA3EzyyMbGb5gpg \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Dispute;

$dispute = Dispute::retrieve('DIvd18AYSNA3EzyyMbGb5gpg');

```
```java

import io.finix.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("DIvd18AYSNA3EzyyMbGb5gpg");

```
> Example Response:

```json

	{
	    "state": "PENDING", 
	    "transfer": "TR5bfADYSh231e98us57ymnE", 
	    "created_at": "2016-06-05T22:58:09.10Z", 
	    "tags": {}, 
	    "occurred_at": "2016-06-05T22:57:20.90Z", 
	    "amount": 0, 
	    "updated_at": "2016-06-05T22:58:09.10Z", 
	    "reason": "FRAUD", 
	    "_links": {
	        "transfer": {
	            "href": "https://api-staging.finix.io/transfers/TR5bfADYSh231e98us57ymnE"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/disputes/DIvd18AYSNA3EzyyMbGb5gpg"
	        }, 
	        "evidence": {
	            "href": "https://api-staging.finix.io/disputes/DIvd18AYSNA3EzyyMbGb5gpg/evidence"
	        }
	    }, 
	    "respond_by": "2016-06-12T22:58:09.27Z", 
	    "id": "DIvd18AYSNA3EzyyMbGb5gpg", 
	    "identity": "IDmFNoDYZeioNCgEyk3kFPV2"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "first_name": "Dwayne", 
	        "last_name": "Johnson"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
```java

import io.finix.payments.processing.client.model.Identity;

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
	    "created_at": "2016-06-05T22:57:17.50Z", 
	    "updated_at": "2016-06-05T22:57:17.50Z", 
	    "entity": {
	        "business_type": null, 
	        "business_phone": null, 
	        "first_name": "Dwayne", 
	        "last_name": "Johnson", 
	        "amex_mid": null, 
	        "title": null, 
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
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2/merchants"
	        }
	    }, 
	    "id": "IDmFNoDYZeioNCgEyk3kFPV2"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "phone": "1234567890", 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "mcc": "0742", 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "max_transaction_amount": 120000, 
	        "principal_percentage_ownership": 100, 
	        "doing_business_as": "Pollos Hermanos", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Pollos Hermanos", 
	        "url": "www.PollosHermanos.com", 
	        "business_name": "Pollos Hermanos", 
	        "incorporation_date": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "business_tax_id": "123456789", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	        "doing_business_as"=> "Pollos Hermanos", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Pollos Hermanos", 
	        "url"=> "www.PollosHermanos.com", 
	        "business_name"=> "Pollos Hermanos", 
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
```java

import io.finix.payments.processing.client.model.Identity;

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
	    "created_at": "2016-06-05T22:57:03.47Z", 
	    "updated_at": "2016-06-05T22:57:03.47Z", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "title": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Pollos Hermanos", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Pollos Hermanos", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.PollosHermanos.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Pollos Hermanos", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDgjCAM3iEYELUG4rTwM6Bof/merchants"
	        }
	    }, 
	    "id": "IDgjCAM3iEYELUG4rTwM6Bof"
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

curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');
```
```java

import io.finix.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDeVSYLXEjpQu3i61phpmAcg");

```
> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-06-05T22:57:01.92Z", 
	    "updated_at": "2016-06-05T22:57:01.92Z", 
	    "entity": {
	        "business_type": "LIMITED_LIABILITY_COMPANY", 
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "dwayne", 
	        "last_name": "Sunkhronos", 
	        "amex_mid": null, 
	        "title": null, 
	        "dob": {
	            "year": 1978, 
	            "day": 27, 
	            "month": 6
	        }, 
	        "default_statement_descriptor": "Golds Gym", 
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "Golds Gym", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "url": "www.GoldsGym.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Golds Gym", 
	        "tax_id_provided": true, 
	        "email": "user@example.org", 
	        "short_business_name": null
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "settlements": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/disputes"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/merchants"
	        }
	    }, 
	    "id": "IDeVSYLXEjpQu3i61phpmAcg"
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

curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "processor": "DUMMY_V1"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
```java

import io.finix.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());

```

> Example Response:

```json

	{
	    "created_at": "2016-06-05T22:57:14.97Z", 
	    "updated_at": "2016-06-05T22:57:14.97Z", 
	    "id": "MUeAWuBZa8vUtQUCpBXpZDcd", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/merchants/MUeAWuBZa8vUtQUCpBXpZDcd"
	        }, 
	        "merchant_profile": {
	            "href": "https://api-staging.finix.io/merchant_profiles/MPid2GHckexaQotpgUSzNwwp"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/merchants/MUeAWuBZa8vUtQUCpBXpZDcd/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "verification": {
	            "href": "https://api-staging.finix.io/verifications/VI6rgh8i7gTpq1AxrNRQ3x7t"
	        }
	    }, 
	    "verification": "VI6rgh8i7gTpq1AxrNRQ3x7t", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPid2GHckexaQotpgUSzNwwp", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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


curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "merchant": null, 
	    "instrument": null, 
	    "processor": "DUMMY_V1", 
	    "identity": null
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
```
```java

import io.finix.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-05T22:57:16.63Z", 
	    "messages": [], 
	    "updated_at": "2016-06-05T22:57:16.66Z", 
	    "id": "VItwb6F6coPggxCHuuf9avP8", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "external_trace_id": "2512e759-d604-49b0-a9d8-4dc352dad5c3", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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

curl https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Verification;

$verification = Verification::retrieve('VItwb6F6coPggxCHuuf9avP8');

```
```java

import io.finix.payments.processing.client.model.Verification;

Verification verification = client.verificationsClient().fetch("VItwb6F6coPggxCHuuf9avP8");

```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-05T22:57:16.51Z", 
	    "messages": [], 
	    "updated_at": "2016-06-05T22:57:16.51Z", 
	    "id": "VItwb6F6coPggxCHuuf9avP8", 
	    "instrument": null, 
	    "state": "SUCCEEDED", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "external_trace_id": "2512e759-d604-49b0-a9d8-4dc352dad5c3", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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

curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "currency": "USD", 
	    "processor": "DUMMY_V1"
	}'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Identity;
use Finix\Resources\Settlement;

$identity = Identity::retrieve('IDeVSYLXEjpQu3i61phpmAcg');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)

```


> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-05T22:59:58.64Z", 
	    "updated_at": "2016-06-05T22:59:58.65Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STw6kgajsRAqjmhNVUPdmpN3", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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


curl https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Settlement;

$settlement = Settlement::retrieve('STw6kgajsRAqjmhNVUPdmpN3');

```
```java

import io.finix.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("STw6kgajsRAqjmhNVUPdmpN3");

```
> Example Response:

```json

	{
	    "total_amount": 888988, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-06-05T22:59:58.52Z", 
	    "updated_at": "2016-06-05T22:59:58.52Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/settlements/STw6kgajsRAqjmhNVUPdmpN3"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "total_fee": 0, 
	    "id": "STw6kgajsRAqjmhNVUPdmpN3", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "fee": 10, 
	    "currency": "USD", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "amount": 100, 
	    "processor": "DUMMY_V1"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDeVSYLXEjpQu3i61phpmAcg", 
	    "source"=> "PIntahNnMqaxdDnwkC5oYrb6", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
```
```java

import io.finix.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);

```


> Example Response:

```json

	{
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "destination": "PIaZMcu221Whh9tBgEtjZ7Ld", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-05T22:57:19.71Z", 
	    "created_at": "2016-06-05T22:57:19.55Z", 
	    "tags": {}, 
	    "trace_id": "c76addd8-95e1-40d6-87a4-f9629ae4c084", 
	    "statement_descriptor": "FNX*GOLDS GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIaZMcu221Whh9tBgEtjZ7Ld"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/disputes"
	        }
	    }, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "type": "DEBIT", 
	    "id": "TR6it2JUNoFd8faSkqYzyEGt"
	}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

### HTTP Request

`POST https://api-staging.finix.io/transfers`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PIntahNnMqaxdDnwkC5oYrb6
merchant_identity | *string*, **required** | UID. | IDeVSYLXEjpQu3i61phpmAcg
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Refund a Debit
```shell

curl https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d  '
	  {
	  "refund_amount" : 100
  	}
	'

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$debit = Transfer::retrieve('TR6it2JUNoFd8faSkqYzyEGt');
$refund = $debit->reverse(50);
```
```java

import io.finix.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```


> Example Response:

```json

	{
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "destination": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "state": "PENDING", 
	    "updated_at": "2016-06-05T22:58:53.27Z", 
	    "created_at": "2016-06-05T22:58:53.13Z", 
	    "tags": {}, 
	    "trace_id": "bd0de806-cacc-466c-9ef0-a4df3e0ec05a", 
	    "statement_descriptor": "FNX*GOLDS GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TRat3P2xTvZA56LjLMhXakhU"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TRat3P2xTvZA56LjLMhXakhU/payment_instruments"
	        }, 
	        "parent": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt"
	        }
	    }, 
	    "source": "PIaZMcu221Whh9tBgEtjZ7Ld", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "type": "REVERSAL", 
	    "id": "TRat3P2xTvZA56LjLMhXakhU"
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

curl https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Transfer;

$transfer = Transfer::retrieve('TR6it2JUNoFd8faSkqYzyEGt');



```
```java

import io.finix.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TR6it2JUNoFd8faSkqYzyEGt");

```
> Example Response:

```json

	{
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "destination": "PIaZMcu221Whh9tBgEtjZ7Ld", 
	    "state": "SUCCEEDED", 
	    "updated_at": "2016-06-05T22:57:19.39Z", 
	    "created_at": "2016-06-05T22:57:19.39Z", 
	    "tags": {}, 
	    "trace_id": "c76addd8-95e1-40d6-87a4-f9629ae4c084", 
	    "statement_descriptor": "FNX*GOLDS GYM", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt"
	        }, 
	        "destination": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIaZMcu221Whh9tBgEtjZ7Ld"
	        }, 
	        "payment_instruments": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/payment_instruments"
	        }, 
	        "source": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "disputes": {
	            "href": "https://api-staging.finix.io/transfers/TR6it2JUNoFd8faSkqYzyEGt/disputes"
	        }
	    }, 
	    "source": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "merchant_identity": "IDeVSYLXEjpQu3i61phpmAcg", 
	    "type": "DEBIT", 
	    "id": "TR6it2JUNoFd8faSkqYzyEGt"
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
    -u USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	            {
	            "url" : "http://requestb.in/vts8mpvt"
	            }
	        '

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



```
```java

import io.finix.payments.processing.client.model.Webhook;

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
	    "created_at": "2016-06-05T22:57:01.26Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-05T22:57:01.26Z", 
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/webhooks/WHjkgdTWURxQ3pjojr9nES9x"
	        }
	    }, 
	    "id": "WHjkgdTWURxQ3pjojr9nES9x"
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



curl https://api-staging.finix.io/webhooks/WHjkgdTWURxQ3pjojr9nES9x \
    -H "Content-Type: application/vnd.json+api" \
    -u USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\Webhook;

$webhook = Webhook::retrieve('WHjkgdTWURxQ3pjojr9nES9x');



```
```java

import io.finix.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHjkgdTWURxQ3pjojr9nES9x");

```

> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-06-05T22:57:01.26Z", 
	    "enabled": true, 
	    "updated_at": "2016-06-05T22:57:01.26Z", 
	    "application": "AP7v8pfY36AzsGMdWB2wB37j", 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/webhooks/WHjkgdTWURxQ3pjojr9nES9x"
	        }
	    }, 
	    "id": "WHjkgdTWURxQ3pjojr9nES9x"
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
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
	    "identity": "IDmFNoDYZeioNCgEyk3kFPV2"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	    "identity"=> "IDmFNoDYZeioNCgEyk3kFPV2"
	));
$card = $card->save();


```
```java

import io.finix.payments.processing.client.model.PaymentCard;

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
	    "updated_at": "2016-06-05T22:57:18.28Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR1034748039", 
	    "_links": {
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/authorizations"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/verifications"
	        }, 
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/transfers"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDmFNoDYZeioNCgEyk3kFPV2"
	        }, 
	        "updates": {
	            "href": "https://api-staging.finix.io/payment_instruments/PIntahNnMqaxdDnwkC5oYrb6/updates"
	        }
	    }, 
	    "created_at": "2016-06-05T22:57:18.28Z", 
	    "id": "PIntahNnMqaxdDnwkC5oYrb6", 
	    "identity": "IDmFNoDYZeioNCgEyk3kFPV2"
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
identity | *string*, **required** | Identity resource which the card is associated. | IDmFNoDYZeioNCgEyk3kFPV2
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
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d '
	{
	    "account_type": "SAVINGS", 
	    "name": "Fran Lemke", 
	    "bank_code": "123123123", 
	    "country": "USA", 
	    "currency": "USD", 
	    "account_number": "123123123", 
	    "type": "BANK_ACCOUNT", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
	}'


```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
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
	    "identity"=> "IDeVSYLXEjpQu3i61phpmAcg"
	));
$bank_account = $bank_account->save();


```
```java

import io.finix.payments.processing.client.model.BankAccount;

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
	    "created_at": "2016-06-05T22:57:13.24Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-06-05T22:57:13.24Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/transfers"
	        }, 
	        "self": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz"
	        }, 
	        "authorizations": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://api-staging.finix.io/payment_instruments/PI7qk1L9ArF6mGJX7vkL5gAz/verifications"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI7qk1L9ArF6mGJX7vkL5gAz", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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
identity | *string*, **required**| Identity resource which the bank account is associated. | IDeVSYLXEjpQu3i61phpmAcg
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


curl https://api-staging.finix.io/payment_instruments/IDeVSYLXEjpQu3i61phpmAcg/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();

use Finix\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('DIvd18AYSNA3EzyyMbGb5gpg');

```
```java

import io.finix.payments.processing.client.model.BankAccount;

BankAccount bankAccount = client.bankAccountsClient().fetch("DIvd18AYSNA3EzyyMbGb5gpg")

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-05T22:57:16.63Z", 
	    "messages": [], 
	    "updated_at": "2016-06-05T22:57:16.66Z", 
	    "id": "VItwb6F6coPggxCHuuf9avP8", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "external_trace_id": "2512e759-d604-49b0-a9d8-4dc352dad5c3", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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


curl https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USqyhyT9n9QeeLbh63kYTWBN:7e5c303e-c9c4-4899-9274-3962786d084a \
    -d "
	{
	    "merchant": null, 
	    "instrument": null, 
	    "processor": "DUMMY_V1", 
	    "identity": null
	}"

```
```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Finix/Settings.php');
Finix\Settings::configure('https://api-staging.finix.io', 'USqyhyT9n9QeeLbh63kYTWBN', '7e5c303e-c9c4-4899-9274-3962786d084a');
require(__DIR__ . '/src/Finix/Bootstrap.php');
Finix\Bootstrap::init();


```
```java

import io.finix.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-06-05T22:57:16.63Z", 
	    "messages": [], 
	    "updated_at": "2016-06-05T22:57:16.66Z", 
	    "id": "VItwb6F6coPggxCHuuf9avP8", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://api-staging.finix.io/verifications/VItwb6F6coPggxCHuuf9avP8"
	        }, 
	        "identity": {
	            "href": "https://api-staging.finix.io/identities/IDeVSYLXEjpQu3i61phpmAcg"
	        }
	    }, 
	    "external_trace_id": "2512e759-d604-49b0-a9d8-4dc352dad5c3", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDeVSYLXEjpQu3i61phpmAcg"
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


