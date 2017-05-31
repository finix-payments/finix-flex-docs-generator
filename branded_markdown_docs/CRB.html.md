---
title: CRB API Reference

language_tabs:
- shell: cURL
- java: Java
- php: PHP
- python: Python



includes:
  - errors

search: true
---

# Guides

## Overview

These guides provide a collection of resources for utilizing the CRB
API and its client libraries. We offer a number of client libraries for
interfacing with the API, and you can view example code snippets for each in
the dark area to the right.

1. [Authentication](#authentication): A quick guide on how to properly
authenticate and interface with the API.

2. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 

3. [Tokenization with Hosted Fields](#tokenization-with-hosted-fields): This guide
explains how to properly tokenize cards in production via hosted fields.

## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.crbpay.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.crb.payments.processing.client</groupId>
  <artifactId>finix</artifactId>
  <version>${version}</version>
</dependency>

...

<repositories>
  <repository>
    <id>oss-snapshots</id>
    <url>https://oss.sonatype.org/content/repositories/snapshots</url>
    <snapshots>
      <enabled>true</enabled>
    </snapshots>
  </repository>
</repositories>

*/

import io.crb.payments.ApiClient;
import io.crb.payments.views.*;
import io.crb.payments.forms.*;

//...

public static void main(String[] args) {

  ApiClient api = ApiClient.builder()
                  .url("https://api-staging.crbpay.io")
                  .user("US3YmXJXbcxe1oBXsX9vNQGQ")
                  .password("eabd2675-e4db-4b36-b6b5-a7dee2c3542b")
                  .build();
//...



```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CRB/Settings.php');

CRB\Settings::configure([
	"root_url" => 'https://api-staging.crbpay.io',
	"username" => 'US3YmXJXbcxe1oBXsX9vNQGQ',
	"password" => 'eabd2675-e4db-4b36-b6b5-a7dee2c3542b']
	);

require(__DIR__ . '/src/CRB/Bootstrap.php');
CRB\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crb.config import configure
configure(root_url="https://api-staging.crbpay.io", auth=("US3YmXJXbcxe1oBXsX9vNQGQ", "eabd2675-e4db-4b36-b6b5-a7dee2c3542b"))

```
To communicate with the CRB API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US3YmXJXbcxe1oBXsX9vNQGQ`

- Password: `eabd2675-e4db-4b36-b6b5-a7dee2c3542b`

- Application ID: `APsKuVbSYCPqbXYhhQWQJQnq`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://api-staging.crbpay.io`

- **Production API:** `https://api.finix.io`

## Push-to-Card
### Step 1: Create a Recipient Identity
```shell
curl https://api-staging.crbpay.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
	        "email": "Laura@gmail.com", 
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
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.forms.Address;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import io.crb.payments.forms.Date;


IdentityForm form = IdentityForm.builder()
    .entity(
    IdentityEntityForm.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
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
        .build())
    .build();

Maybe<Identity> response = api.identities.post(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}

Identity identity = response.view();
```
```php
<?php
use CRB\Resources\Identity;

$identity = new Identity(IDeoUBEa2qmSZXSgWzBSPgc8);
$identity = $identity->save();



```
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
	        "email": "Laura@gmail.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Kline",
    "email" : "Laura@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677612",
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
  "created_at" : "2017-05-22T19:18:17.30Z",
  "updated_at" : "2017-05-22T19:18:17.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    }
  }
}
```

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

#### HTTP Request

`POST https://api-staging.crbpay.io/identities`

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

### Step 2:  Add a Payment Instrument for the Recipient 

```shell
curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "name": "Bob Le", 
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
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.forms.Address;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("IDeoUBEa2qmSZXSgWzBSPgc8")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
if (! response.succeeded()) {
    ApiError error = response .error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard card = response.view();

```
```php
<?php
use CRB\Resources\PaymentCard;
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDeoUBEa2qmSZXSgWzBSPgc8');
$card = new PaymentCard(
	array(
	    "name"=> "Bob Le", 
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
	    "identity"=> "IDeoUBEa2qmSZXSgWzBSPgc8"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "fingerprint" : "FPR-548299190",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Le",
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
  "created_at" : "2017-05-22T19:18:18.47Z",
  "updated_at" : "2017-05-22T19:18:18.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/updates"
    }
  }
}
```

<aside class="warning">
Please note that creating cards directly via the API should only be done for
testing purposes. You must use the Tokenization iframe or javascript client
to remain out of PCI scope.
</aside>

Now that we've created an `Identity` for our recipient, we'll need to tokenize a credit card where funds will be disbursed.

In the API, credit cards are represented by the `Payment Instrument` resource.

To classify the `Payment Instrument` as a credit card you'll need to pass `PAYMENT_CARD` in the type field of your request, and you'll also want to pass the ID of the `Identity` that you created in the last step via the identity field to properly associate it with your recipient.

#### HTTP Request

`POST https://api-staging.crbpay.io/payment_instruments`

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

### Step 3: Provision Recipient Account
```shell
curl https://api-staging.crbpay.io/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDeoUBEa2qmSZXSgWzBSPgc8").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> merchantResponse = api.identities.id(identity.id).merchants.post(form);

if (! merchantResponse.succeeded()) {
            ApiError error = merchantResponse.error();
            System.out.println(error.getCode());
            throw new RuntimeException("API error attempting to provision Merchant");
        }
Merchant merchant = merchantResponse.view();
```
```php
<?php
use CRB\Resources\Identity;
use CRB\Resources\Merchant;

$identity = Identity::retrieve('IDeoUBEa2qmSZXSgWzBSPgc8');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MU9z7DrRP7LBuhHVS3vLFvtb",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "verification" : "VIre7jjrTr896eExNB4Q3oj2",
  "merchant_profile" : "MP9LQ3P5qj8ERuw4zQyPR6xw",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-05-22T19:18:19.15Z",
  "updated_at" : "2017-05-22T19:18:19.15Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/merchants/MU9z7DrRP7LBuhHVS3vLFvtb"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/merchants/MU9z7DrRP7LBuhHVS3vLFvtb/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.crbpay.io:443/merchant_profiles/MP9LQ3P5qj8ERuw4zQyPR6xw"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "verification" : {
      "href" : "https://api-staging.crbpay.io:443/verifications/VIre7jjrTr896eExNB4Q3oj2"
    }
  }
}
```

Now that we've associated a Payment Instrument with our recipient's `Identity` we're ready to provision a Recipient account. This is the last step before you can begin paying out an Identity. Luckily you've already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource.

#### HTTP Request

`POST https://api-staging.crbpay.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor


### Step 4: Send Payout




```shell
curl https://api-staging.crbpay.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PI8D8zDPcbTq6dAZbbyW83Ed", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .amount(100L)
        .currency(Currency.getInstance("USD"))
        .idempotencyId("Idsfk23jnasdfkjf")
        .destination("PI8D8zDPcbTq6dAZbbyW83Ed")
        .tags(ImmutableMap.of("order_number", "21DFASJSAKAS"))
.build();

Maybe<Transfer> response = api.transfers.post(form);
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Transfer");
}
Transfer transfer = response.view();
```
```php
<?php
use CRB\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI8D8zDPcbTq6dAZbbyW83Ed", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$transfer = $transfer->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRpjDv1xQLns23rurNPSQdCA",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "310",
  "currency" : "USD",
  "application" : "APsKuVbSYCPqbXYhhQWQJQnq",
  "source" : "PIf5UozeAUfzEg8ZemQechjs",
  "destination" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-05-22T19:18:20.12Z",
  "updated_at" : "2017-05-22T19:18:22.49Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIf5UozeAUfzEg8ZemQechjs"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    }
  }
}
```


Now the final step - time to payout the recipient!

Next you'll need to create a `Transfer`.  What's a `Transfer`? Glad you asked! A `Transfer` represents any flow of funds either to or from a Payment Instrument. In this case a Payout to a card.

To create a `Transfer` we'll simply supply the Payment Instrument ID of the previously tokenized card as the destination field. Also, be sure to note that the amount field is in cents.

Simple enough, right? You'll also want to store the ID from that `Transfer` for your records. `Transfers` can have two possible states SUCCEEDED and FAILED.


#### HTTP Request

`POST https://api-staging.crbpay.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where funds will be sent
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Embedded Tokenization

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to CRB. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial
transactions via the CRB API.
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
<script type="text/javascript" src="https://vgs-assets.s3.amazonaws.com/payline-1.latest.js"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        Payline.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: 'APsKuVbSYCPqbXYhhQWQJQnq',
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
  "id" : "TK7RoadsioNcGGNFFSorw3n6",
  "fingerprint" : "FPR1202406258",
  "created_at" : "2017-05-22T19:18:28.00Z",
  "updated_at" : "2017-05-22T19:18:28.00Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-05-23T19:18:28.00Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TK7RoadsioNcGGNFFSorw3n6")
    .identity("IDeoUBEa2qmSZXSgWzBSPgc8")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7RoadsioNcGGNFFSorw3n6", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDeoUBEa2qmSZXSgWzBSPgc8"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI7RoadsioNcGGNFFSorw3n6",
  "fingerprint" : "FPR1202406258",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-05-22T19:18:28.64Z",
  "updated_at" : "2017-05-22T19:18:28.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/updates"
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

`POST https://api-staging.crbpay.io/payment_instruments`


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
[jsFiddle example](https://jsfiddle.net/rserna2010/Ls101sou/).

### Step 1: Include library

```html
 <script type="text/javascript" src="https://js.verygoodvault.com/js-vgfield-2/crb.js"></script>
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
    secureForm.submit('/applications/APsKuVbSYCPqbXYhhQWQJQnq/tokens', {
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
  "id" : "TK7RoadsioNcGGNFFSorw3n6",
  "fingerprint" : "FPR1202406258",
  "created_at" : "2017-05-22T19:18:28.00Z",
  "updated_at" : "2017-05-22T19:18:28.00Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-05-23T19:18:28.00Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
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
curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TK7RoadsioNcGGNFFSorw3n6")
    .identity("IDeoUBEa2qmSZXSgWzBSPgc8")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7RoadsioNcGGNFFSorw3n6", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDeoUBEa2qmSZXSgWzBSPgc8"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}).save()

```
> Example Response:

```json
{
  "id" : "PI7RoadsioNcGGNFFSorw3n6",
  "fingerprint" : "FPR1202406258",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-05-22T19:18:28.64Z",
  "updated_at" : "2017-05-22T19:18:28.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/updates"
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

`POST https://api-staging.crbpay.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


# Identities

An `Identity` resource represents either a person or business and is in many ways the centerpiece of the payment API's 
architecture. Transfers and Payment `Instruments` must be associated with an `Identity`. This structure makes it easy 
to manage and reconcile their associated payment history, transaction history, and payouts.

This field is optionally used to collect KYC information for the recipient.
## Create an Identity for a Recipient


```shell
curl https://api-staging.crbpay.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
	        "email": "Laura@gmail.com", 
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
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.forms.Address;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import io.crb.payments.forms.Date;


IdentityForm form = IdentityForm.builder()
    .entity(
    IdentityEntityForm.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
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
        .build())
    .build();

Maybe<Identity> response = api.identities.post(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}

Identity identity = response.view();
```
```php
<?php
use CRB\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677612", 
	        "first_name"=> "Laura", 
	        "last_name"=> "Kline", 
	        "email"=> "Laura@gmail.com", 
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
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Laura", 
	        "last_name": "Kline", 
	        "email": "Laura@gmail.com", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Kline",
    "email" : "Laura@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677612",
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
  "created_at" : "2017-05-22T19:18:17.30Z",
  "updated_at" : "2017-05-22T19:18:17.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.crbpay.io/identities`

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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code

## Retrieve a Identity
```shell

curl https://api-staging.crbpay.io/identities/IDeoUBEa2qmSZXSgWzBSPgc8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDeoUBEa2qmSZXSgWzBSPgc8").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

```
```php
<?php
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDeoUBEa2qmSZXSgWzBSPgc8');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDeoUBEa2qmSZXSgWzBSPgc8")

```
> Example Response:

```json
{
  "id" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Henderson",
    "email" : "Jessie@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677612",
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
  "created_at" : "2017-05-22T19:18:17.29Z",
  "updated_at" : "2017-05-22T19:18:23.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.crbpay.io/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl https://api-staging.crbpay.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

Page<Identity> page = api.identities.get().view();
while (page.hasNext()) {
    page = page.getNext();
}
```
```php
<?php
use CRB\Resources\Identity;

$identities= Identity::getPagination("/identities");


```
```python


from crossriver.resources import Identity
identity = Identity.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDeoUBEa2qmSZXSgWzBSPgc8",
      "entity" : {
        "title" : null,
        "first_name" : "Laura",
        "last_name" : "Henderson",
        "email" : "Jessie@gmail.com",
        "business_name" : null,
        "business_type" : null,
        "doing_business_as" : null,
        "phone" : "7145677612",
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
      "created_at" : "2017-05-22T19:18:17.29Z",
      "updated_at" : "2017-05-22T19:18:23.12Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
        },
        "verifications" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
        }
      }
    }, {
      "id" : "IDwcpKQn1aq7bCUnz21XhLqB",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "WePay",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "application_name" : "WePay"
      },
      "created_at" : "2017-05-22T19:18:14.35Z",
      "updated_at" : "2017-05-22T19:18:14.36Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB"
        },
        "verifications" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDwcpKQn1aq7bCUnz21XhLqB/disputes"
        },
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.crbpay.io/identities/`


## Update an Identity
```shell
curl https://api-staging.crbpay.io/identities/IDeoUBEa2qmSZXSgWzBSPgc8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Laura", 
	        "last_name": "Henderson", 
	        "email": "Jessie@gmail.com", 
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
```java

```
```php
<?php

```
```python



```
> Example Response:

```json
{
  "id" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "entity" : {
    "title" : null,
    "first_name" : "Laura",
    "last_name" : "Henderson",
    "email" : "Jessie@gmail.com",
    "business_name" : null,
    "business_type" : null,
    "doing_business_as" : null,
    "phone" : "7145677612",
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
  "created_at" : "2017-05-22T19:18:17.29Z",
  "updated_at" : "2017-05-22T19:18:23.12Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    }
  }
}
```
<aside class="notice">
tax_id and business_tax_id are not updatable. If either field was input incorrectly,
please create a new Identity resource.
</aside>



#### HTTP Request

`POST https://api-staging.crbpay.io/identities`

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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code

# Payment Instruments

A `Payment Instrument` resource represents either a credit card.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Associate a Token
```shell
curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TK7RoadsioNcGGNFFSorw3n6")
    .identity("IDeoUBEa2qmSZXSgWzBSPgc8")
.build();

Maybe<PaymentCard> cardResponse = api.instruments.post(tokenForm);
if (! cardResponse.succeeded()) {
    ApiError error = cardResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard paymentCard = cardResponse.view();

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TK7RoadsioNcGGNFFSorw3n6", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDeoUBEa2qmSZXSgWzBSPgc8"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TK7RoadsioNcGGNFFSorw3n6", 
	    "type": "TOKEN", 
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI7RoadsioNcGGNFFSorw3n6",
  "fingerprint" : "FPR1202406258",
  "tags" : { },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
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
  "created_at" : "2017-05-22T19:18:28.64Z",
  "updated_at" : "2017-05-22T19:18:28.64Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI7RoadsioNcGGNFFSorw3n6/updates"
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

`POST https://api-staging.crbpay.io/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Create a Card
```shell


curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "name": "Bob Le", 
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
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.forms.Address;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("IDeoUBEa2qmSZXSgWzBSPgc8")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
if (! response.succeeded()) {
    ApiError error = response .error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard card = response.view();

```
```php
<?php
use CRB\Resources\PaymentCard;
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDeoUBEa2qmSZXSgWzBSPgc8');
$card = new PaymentCard(
	array(
	    "name"=> "Bob Le", 
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
	    "identity"=> "IDeoUBEa2qmSZXSgWzBSPgc8"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Le", 
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
	    "identity": "IDeoUBEa2qmSZXSgWzBSPgc8"
	}).save()
```
> Example Response:

```json
{
  "id" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "fingerprint" : "FPR-548299190",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Le",
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
  "created_at" : "2017-05-22T19:18:18.47Z",
  "updated_at" : "2017-05-22T19:18:18.47Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/updates"
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

`POST https://api-staging.crbpay.io/payment_instruments`

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
## Fetch a Credit Card
```shell
curl https://api-staging.crbpay.io/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<PaymentCard> response = api.instruments.id("PI8D8zDPcbTq6dAZbbyW83Ed").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Payment Card");
}
PaymentCard card = response.view();
```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PI8D8zDPcbTq6dAZbbyW83Ed');

```
```python



```
> Example Response:

```json
{
  "id" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "fingerprint" : "FPR-548299190",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Le",
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
  "created_at" : "2017-05-22T19:18:18.44Z",
  "updated_at" : "2017-05-22T19:18:18.44Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://api-staging.crbpay.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Payment Instrument Verification

```shell
curl https://api-staging.crbpay.io/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "processor": "VISA_V1"
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;


 VerificationForm verificationForm = VerificationForm.builder()
    .processor("VISA_V1")
    .build();

Maybe<Verification> verificationResponse = api.instruments.id("PI8D8zDPcbTq6dAZbbyW83Ed").verifications.post(verificationForm);
if (! verificationResponse.succeeded()) {
    ApiError error = verificationResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create a Verification");
}
Verification verification = verificationResponse.view();

```
```php
<?php

```
```python



```
> Example Response:

```json
{
  "id" : "VIhjPnMQYN7Bp5VmiMYLiVTR",
  "tags" : { },
  "messages" : [ ],
  "raw" : {
    "validation_details" : {
      "systems_trace_audit_number" : "311",
      "transaction_identifier" : "1234",
      "approval_code" : "003403",
      "action_code" : "85",
      "response_code" : "5",
      "address_verification_results" : "N"
    },
    "inquiry_details" : {
      "systems_trace_audit_number" : "311",
      "card_type_code" : "C",
      "billing_currency_code" : 986,
      "billing_currency_minor_digits" : 2,
      "issuer_name" : "Visa Test Bank",
      "card_issuer_country_code" : 76,
      "fast_funds_indicator" : "N",
      "push_funds_block_indicator" : "N",
      "online_gambing_block_indicator" : "Y"
    }
  },
  "processor" : "VISA_V1",
  "state" : "SUCCEEDED",
  "created_at" : "2017-05-22T19:18:44.02Z",
  "updated_at" : "2017-05-22T19:18:46.12Z",
  "trace_id" : "311",
  "payment_instrument" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "merchant" : null,
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/verifications/VIhjPnMQYN7Bp5VmiMYLiVTR"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.crbpay.io/payment_instruments/:PAYMENT_INSTRUMENT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor | *string*, **required** | The name of the processor, which needs to be: `VISA_V1`

#### Address Verification Results (address_verification_results)
Letter | Description
------ | -------------------------------------------------------------------
D, F, M | Address verified
A, B, C, G, I, N, P, R, S, U, W | Address not verified

#### Card Type (card_type_code)

This one-character code indicates whether the account is credit, debit, prepaid, deferred debit, or charge.

Letter | Description
------ | -------------------------------------------------------------------
C | Credit  
D | Debit  
H | Charge Card    
P | Prepaid  
R | Deferred Debit  

#### Fasts Funds Indicator (fast_funds_indicator)

Indicates whether or not the card is Fast Funds eligible (i.e. if the funds will settle in 30 mins or less). If not eligible, typically funds will settle within 2 days.

Letter | Description
------ | -------------------------------------------------------------------
B, D | Fast Funds eligible
N | Not eligible for Fast Funds

#### Push Funds Indicator (push_funds_block_indicator)

This code indicates if the associated card can receive push-to-card disbursements.

Letter | Description
------ | -------------------------------------------------------------------
A, B, C | Accepts push-to-card payments
C | Does not accept push-to-card payments

#### Online Gambling Block Indicator (online_gambing_block_indicator)

Indicates if the card can receive push-payments for online gambling payouts.

Letter | Description
------ | -------------------------------------------------------------------
Y | Blocked for online gambling payouts
N | Not blocked for online gambling payouts

#### Card Product ID (card_product_id)

A combination of card brand, platform, class and scheme.

Letter | Description
------ | -------------------------------------------------------------------
A | Visa Traditional
AX | American Express
B | Visa Traditional Rewards
C | Visa Signature
D | Visa Signature Preferred
DI | Discover
DN | Diners
E | Proprietary ATM
F | Visa Classic
G | Visa Business
G1 | Visa Signature Business
G2 | Visa Business Check Card
G3 | Visa Business Enhanced
G4 | Visa Infinite Business
G5 | Visa Business Rewards
I | Visa Infinite
I1 | Visa Infinite Privilege
I2 | Visa UHNW
J3 | Visa Healthcare
JC | JCB
K | Visa Corporate T&E
K1 | Visa Government Corporate T&E
L | Visa Electron
M | MasterCard
N | Visa Platinum
N1 | Visa Rewards
N2 | Visa Select
P | Visa Gold
Q | Private Label
Q1 | Private Label Prepaid
Q2 | Private Label Basic
Q3 | Private Label Standard
Q4 | Private Label Enhanced
Q5 | Private Label Specialized
Q6 | Private Label Premium
R | Proprietary
S | Visa Purchasing
S1 | Visa Purchasing with Fleet
S2 | Visa Government Purchasing
S3 | Visa Government Purchasing with Fleet
S4 | Visa Commercial Agriculture
S5 | Visa Commercial Transport
S6 | Visa Commercial Marketplace
U | Visa Travel Money
V | Visa V PAY

#### Product Sub-Type (card_product_subtype)

Description of product subtype.

Letter | Description
------ | -------------------------------------------------------------------
AC | Agriculture Maintenance Account
AE | Agriculture Debit Account/Electron
AG | Agriculture
AI | Agriculture Investment Loan
CG | Brazil Cargo
CS | Construction
DS | Distribution
HC | Healthcare
LP | Visa Large Purchase Advantage
MA | Visa Mobile Agent
MB | Interoperable Mobile Branchless Banking
MG | Visa Mobile General
VA | Visa Vale - Supermarket
VF | Visa Vale - Fuel
VR | Visa Vale - Restaurant

#### Card Sub-Type (card_subtype_code)

The code for account funding source subtype, such as reloadable and non-reloadable.

Letter | Description
------ | -------------------------------------------------------------------
N | Non-Reloadable
R | Reloadable

# Transfer

A `Transfer` represents any payout to a card

Payouts can have two possible states values: SUCCEEDED or FAILED.

- **SUCCEEDED:**  Funds have been disbursed.
        
- **FAILED:** Attempt to disburse has failed



## Create Payout

```shell
curl https://api-staging.crbpay.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PI8D8zDPcbTq6dAZbbyW83Ed", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .amount(100L)
        .currency(Currency.getInstance("USD"))
        .idempotencyId("Idsfk23jnasdfkjf")
        .destination("PI8D8zDPcbTq6dAZbbyW83Ed")
        .tags(ImmutableMap.of("order_number", "21DFASJSAKAS"))
.build();

Maybe<Transfer> response = api.transfers.post(form);
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Transfer");
}
Transfer transfer = response.view();
```
```php
<?php
use CRB\Resources\Transfer;

$debit = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI8D8zDPcbTq6dAZbbyW83Ed", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$debit = $debit->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRpjDv1xQLns23rurNPSQdCA",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "310",
  "currency" : "USD",
  "application" : "APsKuVbSYCPqbXYhhQWQJQnq",
  "source" : "PIf5UozeAUfzEg8ZemQechjs",
  "destination" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-05-22T19:18:20.12Z",
  "updated_at" : "2017-05-22T19:18:22.49Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIf5UozeAUfzEg8ZemQechjs"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.crbpay.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where funds will be sent
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Retrieve a Payout
```shell

curl https://api-staging.crbpay.io/transfers/TRpjDv1xQLns23rurNPSQdCA \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

Maybe<Transfer> response = api.transfers.id("TRpjDv1xQLns23rurNPSQdCA").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Transfer");
}
Transfer card = response.view();
```
```php
<?php
use CRB\Resources\Transfer;

$transfer = Transfer::retrieve('TRpjDv1xQLns23rurNPSQdCA');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRpjDv1xQLns23rurNPSQdCA")

```
> Example Response:

```json
{
  "id" : "TRpjDv1xQLns23rurNPSQdCA",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "310",
  "currency" : "USD",
  "application" : "APsKuVbSYCPqbXYhhQWQJQnq",
  "source" : "PIf5UozeAUfzEg8ZemQechjs",
  "destination" : "PI8D8zDPcbTq6dAZbbyW83Ed",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-05-22T19:18:20.07Z",
  "updated_at" : "2017-05-22T19:18:22.49Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIf5UozeAUfzEg8ZemQechjs"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.crbpay.io/transfers/:PAYOUT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYOUT_ID | ID of the `Payout`

## List all Payouts
```shell
curl https://api-staging.crbpay.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US3YmXJXbcxe1oBXsX9vNQGQ:eabd2675-e4db-4b36-b6b5-a7dee2c3542b

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;


Page<Transfer> page = api.transfers.get().view();
while (page.hasNext()) {
    page = page.getNext();

}
```
```php
<?php
use CRB\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


```
```python


from crossriver.resources import Transfer
transfer = Transfer.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRpjDv1xQLns23rurNPSQdCA",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "310",
      "currency" : "USD",
      "application" : "APsKuVbSYCPqbXYhhQWQJQnq",
      "source" : "PIf5UozeAUfzEg8ZemQechjs",
      "destination" : "PI8D8zDPcbTq6dAZbbyW83Ed",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "CRB*CRB PAY",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-05-22T19:18:20.07Z",
      "updated_at" : "2017-05-22T19:18:22.49Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDeoUBEa2qmSZXSgWzBSPgc8",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APsKuVbSYCPqbXYhhQWQJQnq"
        },
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDeoUBEa2qmSZXSgWzBSPgc8"
        },
        "reversals" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRpjDv1xQLns23rurNPSQdCA/disputes"
        },
        "source" : {
          "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIf5UozeAUfzEg8ZemQechjs"
        },
        "destination" : {
          "href" : "https://api-staging.crbpay.io:443/payment_instruments/PI8D8zDPcbTq6dAZbbyW83Ed"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.crbpay.io/transfers`
