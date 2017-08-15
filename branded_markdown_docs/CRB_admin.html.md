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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410

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
                  .user("USiFamqVgvMwqN2yS1Ky8GEA")
                  .password("d699b9a5-40f9-492d-ae93-f96c3c306410")
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
	"username" => 'USiFamqVgvMwqN2yS1Ky8GEA',
	"password" => 'd699b9a5-40f9-492d-ae93-f96c3c306410']
	);

require(__DIR__ . '/src/CRB/Bootstrap.php');
CRB\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crb.config import configure
configure(root_url="https://api-staging.crbpay.io", auth=("USiFamqVgvMwqN2yS1Ky8GEA", "d699b9a5-40f9-492d-ae93-f96c3c306410"))

```
To communicate with the CRB API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USiFamqVgvMwqN2yS1Ky8GEA`

- Password: `d699b9a5-40f9-492d-ae93-f96c3c306410`

- Application ID: `APfz6mtTf41HacNCNiixy57c`

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
    -u USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Marshall", 
	        "last_name": "Curry", 
	        "email": "Marshall@gmail.com", 
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

$identity = new Identity(ID31nVq9QQ2HZTUvMsjQQHe);
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
	        "first_name": "Marshall", 
	        "last_name": "Curry", 
	        "email": "Marshall@gmail.com", 
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
  "id" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "entity" : {
    "title" : null,
    "first_name" : "Marshall",
    "last_name" : "Curry",
    "email" : "Marshall@gmail.com",
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
  "created_at" : "2017-07-06T05:32:39.95Z",
  "updated_at" : "2017-07-06T05:32:39.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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
    -u USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "name": "Marcie Henderson", 
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
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
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
        .identity("ID31nVq9QQ2HZTUvMsjQQHe")
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

$identity = Identity::retrieve('ID31nVq9QQ2HZTUvMsjQQHe');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Henderson", 
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
	    "identity"=> "ID31nVq9QQ2HZTUvMsjQQHe"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Henderson", 
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
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "fingerprint" : "FPR764826810",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Henderson",
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
  "created_at" : "2017-07-06T05:32:41.84Z",
  "updated_at" : "2017-07-06T05:32:41.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/updates"
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

### Step 3: Verify card is eligible to receive push-to-card disbursements

Now that we've associated a payment instrument to a recipient, we'll need to verify whether or not the card is eligible to receive push-to-card disbursements. How? By making a request to the `Verifications` endpoint. The returned `Verification` resource returns a set of general attributes and details about the card in question (e.g. card type, issuer information). For example, the `inquiry_details` object will contain a `push_funds_block_indicator` attribute that indicates if it is eligible for push-to-card disbursements. Below you'll see a number of fields and the potential responses.

```shell
curl https://api-staging.crbpay.io/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
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

Maybe<Verification> verificationResponse = api.instruments.id("PIpEUWYVBT1F3uDAKNh7MbZ5").verifications.post(verificationForm);
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


from crossriver.resources import PaymentInstrument
from crossriver.resources import Verification


payment_card = PaymentInstrument.get(id="PIpEUWYVBT1F3uDAKNh7MbZ5")

verify = payment_card.verify_on(Verification(**
	{
	    "processor": "VISA_V1"
	}))

```
> Example Response:

```json
{
  "id" : "VIqegfG9kHrrzLGNHGgbsvmS",
  "tags" : { },
  "messages" : [ ],
  "raw" : {
    "validation_details" : {
      "systems_trace_audit_number" : "448",
      "transaction_identifier" : "1234",
      "approval_code" : "003403",
      "action_code" : "85",
      "response_code" : "5",
      "address_verification_results" : "N"
    },
    "inquiry_details" : {
      "systems_trace_audit_number" : "448",
      "card_type_code" : "C",
      "billing_currency_code" : 986,
      "billing_currency_minor_digits" : 2,
      "issuer_name" : "Visa Test Bank",
      "card_issuer_country_code" : 76,
      "fast_funds_indicator" : "N",
      "push_funds_block_indicator" : "N",
      "online_gambing_block_indicator" : "Y"
    },
    "general_inquiry_details" : {
      "systems_trace_audit_number" : "448",
      "status" : {
        "status_code" : "CDI000",
        "status_description" : "Success"
      }
    }
  },
  "processor" : "VISA_V1",
  "state" : "SUCCEEDED",
  "created_at" : "2017-07-06T05:33:30.55Z",
  "updated_at" : "2017-07-06T05:33:33.59Z",
  "trace_id" : "448",
  "payment_instrument" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "merchant" : null,
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/verifications/VIqegfG9kHrrzLGNHGgbsvmS"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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

#### Card Verification 2 Results (cvv2_result_code)
Letter | Description
------ | -------------------------------------------------------------------
M | CVV  verified
N, P, S | CVV not verified
U | Issuer does not participate in CVV2 service

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
N | Does not accept push-to-card payments

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

### Step 4: Provision Recipient Account

```shell
curl https://api-staging.crbpay.io/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
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

Maybe<Identity> response = api.identities.id("ID31nVq9QQ2HZTUvMsjQQHe").get();
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

$identity = Identity::retrieve('ID31nVq9QQ2HZTUvMsjQQHe');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from crossriver.resources import Identity
from crossriver.resources import Merchant

identity = Identity.get(id="PIpEUWYVBT1F3uDAKNh7MbZ5")
merchant = identity.provision_merchant_on(Merchant())

```
> Example Response:

```json
{
  "id" : "MUhWT3d1nRKAPRVZMskJoUKB",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "verification" : "VItm7vkFDKwCYnGLDKPvweon",
  "merchant_profile" : "MPwBstNj76sdssKTcJr7GQZK",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-07-06T05:32:43.44Z",
  "updated_at" : "2017-07-06T05:32:43.44Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/merchants/MUhWT3d1nRKAPRVZMskJoUKB"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/merchants/MUhWT3d1nRKAPRVZMskJoUKB/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.crbpay.io:443/merchant_profiles/MPwBstNj76sdssKTcJr7GQZK"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "verification" : {
      "href" : "https://api-staging.crbpay.io:443/verifications/VItm7vkFDKwCYnGLDKPvweon"
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


### Step 5: Send Payout

```shell
curl https://api-staging.crbpay.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIpEUWYVBT1F3uDAKNh7MbZ5", 
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
        .destination("PIpEUWYVBT1F3uDAKNh7MbZ5")
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
	    "destination"=> "PIpEUWYVBT1F3uDAKNh7MbZ5", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$transfer = $transfer->save();
```
```python


from crossriver.resources import Transfer

payout = Transfer(**
	{
	    "name": "Marcie Henderson", 
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
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()

```
> Example Response:

```json
{
  "id" : "TRbBHbTQoC2uPxLUDYFA2x1c",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "447",
  "currency" : "USD",
  "application" : "APfz6mtTf41HacNCNiixy57c",
  "source" : "PImfHE94yj98755zDc86WGbG",
  "destination" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:32:45.28Z",
  "updated_at" : "2017-07-06T05:32:47.48Z",
  "idempotency_id" : null,
  "merchant_identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PImfHE94yj98755zDc86WGbG"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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
          applicationId: 'APfz6mtTf41HacNCNiixy57c',
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
  "id" : "TKoWRX22WA5YEfzmUfFejhwB",
  "fingerprint" : "FPR1202406258",
  "created_at" : "2017-07-06T05:32:59.43Z",
  "updated_at" : "2017-07-06T05:32:59.43Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-07-07T05:32:59.43Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.crbpay.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}'


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKoWRX22WA5YEfzmUfFejhwB")
    .identity("ID31nVq9QQ2HZTUvMsjQQHe")
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
	    "token"=> "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID31nVq9QQ2HZTUvMsjQQHe"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIoWRX22WA5YEfzmUfFejhwB",
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
  "created_at" : "2017-07-06T05:33:00.89Z",
  "updated_at" : "2017-07-06T05:33:00.89Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/updates"
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
    secureForm.submit('/applications/APfz6mtTf41HacNCNiixy57c/tokens', {
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
  "id" : "TKoWRX22WA5YEfzmUfFejhwB",
  "fingerprint" : "FPR1202406258",
  "created_at" : "2017-07-06T05:32:59.43Z",
  "updated_at" : "2017-07-06T05:32:59.43Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-07-07T05:32:59.43Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKoWRX22WA5YEfzmUfFejhwB")
    .identity("ID31nVq9QQ2HZTUvMsjQQHe")
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
	    "token"=> "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID31nVq9QQ2HZTUvMsjQQHe"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIoWRX22WA5YEfzmUfFejhwB",
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
  "created_at" : "2017-07-06T05:33:00.89Z",
  "updated_at" : "2017-07-06T05:33:00.89Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/updates"
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

# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-staging.crbpay.io/applications/APfz6mtTf41HacNCNiixy57c \
    -H "Content-Type: application/vnd.json+api" \
    -u UScDQHHFKkfFk5pLEGdn6zoK:4c81c4dc-8f56-448a-9f6d-731a35e39e8f 

```
```java

```
```php
<?php
use CRB\Resources\Application;

$application = Application::retrieve('APfz6mtTf41HacNCNiixy57c');

```
```python


from crossriver.resources import Application

application = Application.get(id="APfz6mtTf41HacNCNiixy57c")
```
> Example Response:

```json
{
  "id" : "APfz6mtTf41HacNCNiixy57c",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-07-06T05:32:34.98Z",
  "updated_at" : "2017-07-06T05:32:38.57Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "processors" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/processors"
    },
    "users" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/application_profile"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.crbpay.io/applications/:APPLICATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application`

## Create an Application
```shell
curl https://api-staging.crbpay.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScDQHHFKkfFk5pLEGdn6zoK:4c81c4dc-8f56-448a-9f6d-731a35e39e8f \
    -d '
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "USiFamqVgvMwqN2yS1Ky8GEA", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}'

```
```java

```
```php
<?php
use CRB\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Paypal"
	    ), 
	    "user"=> "USiFamqVgvMwqN2yS1Ky8GEA", 
	    "entity"=> array(
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 5
	        ), 
	        "settlement_bank_account"=> "CORPORATE", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 1200000, 
	        "phone"=> "1234567890", 
	        "doing_business_as"=> "Paypal", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Paypal", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();

```
```python


from crossriver.resources import Application

application = Application(**
	{
	    "tags": {
	        "application_name": "Paypal"
	    }, 
	    "user": "USiFamqVgvMwqN2yS1Ky8GEA", 
	    "entity": {
	        "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
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
	        "doing_business_as": "Paypal", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Paypal", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "APfz6mtTf41HacNCNiixy57c",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-07-06T05:32:34.99Z",
  "updated_at" : "2017-07-06T05:32:34.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "processors" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/processors"
    },
    "users" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/application_profile"
    }
  }
}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can create a new Application.
</aside>

#### HTTP Request

`POST https://api-staging.crbpay.io/applications`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
user | *string*, **required** | User ID for the owner of the `Application`


#### Business-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
business_name | *string*, **required** | Merchant's full legal business name (If INDIVIDUAL_SOLE_PROPRIETORSHIP, please input first name, Full legal last name and middle initial; max 120 characters)
doing_business_as | *string*, **required** | Alternate name of the business. If no other name is used please use the same value for business_name (max 60 characters)
business_type | *string*, **required** | Please select one of the following values: INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY
business_tax_id | *string*, **required** | Nine digit Tax Identification Number (TIN), Employer Identification Number (EIN) or if the business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP and a Tax ID is not available, the principal's Social Security Number (SSN)
url | *string*, **required** | Merchant's publicly available website (max 100 characters)
business_phone | *string*, **required** | Customer service phone number where the merchant can be reached (max 10 characters)
incorporation_date  | *object*, **required** | Date company was founded (See below for a full list of the child attributes)
business_address | *object*, **required** | Primary address for the legal entity (Full description of child attributes below)

#### Principal-specific Request Arguments
(i.e. authorized representative or primary contact responsible for the account)

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **required** | Full legal first name of the merchant's principal representative (max 20 characters)
last_name | *string*, **required** | Full legal last name of the merchant's principal representative (max 20 characters)
title | *string*, **required** | Principal's corporate title or role (i.e. Chief Executive Officer, CFO, etc.; max 60 characters)
principal_percentage_ownership | *integer*, **required** | Percentage of company owned by the principal (min 0; max 100)
tax_id | *string*, **required** | Nine digit Social Security Number (SSN) for the principal
dob | *object*, **required** | Principal's date of birth (Full description of child attributes below)
phone | *string*, **required** | Principal's phone number (max 10 characters)
email | *string*, **required** | Principal's email address where they can be reached (max 100 characters)
personal_address | *object*, **required** | Principal's personal home address. This field is used for identity verification purposes (Full description of child attributes below)

#### Processing-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
default_statement_descriptor | *string*, **required** | Billing descriptor displayed on the buyer's bank or card statement (Length must be between 1 and 20 characters)
annual_card_volume | *integer*, **required** |  Approximate annual credit card sales expected to be processed in cents by this merchant (max 23 characters)
max_transaction_amount | *integer*, **required** |  Maximum amount that can be transacted for a single transaction in cents (max 12 characters)
mcc | *string*, **required** |  Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under
has_accepted_credit_cards_previously | *boolean*, **optional** | Defaults to false if not passed

#### Address-object Request Arguments

Field | Type | Description
----- | ---- | -----------
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
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
curl https://api-staging.crbpay.io/applications/APfz6mtTf41HacNCNiixy57c/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScDQHHFKkfFk5pLEGdn6zoK:4c81c4dc-8f56-448a-9f6d-731a35e39e8f \
    -X PUT \
    -d '
	{
	    "processing_enabled": false
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
  "id" : "APfz6mtTf41HacNCNiixy57c",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-07-06T05:32:34.98Z",
  "updated_at" : "2017-07-06T05:33:22.61Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "processors" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/processors"
    },
    "users" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/application_profile"
    }
  }
}
```

Disable an `Applications's` ability to create new `Transfers` and `Authorizations`

#### HTTP Request

`PUT https://api-staging.crbpay.io/applications/:APPLICATION_ID`

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
curl https://api-staging.crbpay.io/applications/APfz6mtTf41HacNCNiixy57c/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScDQHHFKkfFk5pLEGdn6zoK:4c81c4dc-8f56-448a-9f6d-731a35e39e8f \
    -X PUT \
    -d '
	{
	    "settlement_enabled": false
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
  "id" : "APfz6mtTf41HacNCNiixy57c",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-07-06T05:32:34.98Z",
  "updated_at" : "2017-07-06T05:33:23.87Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "processors" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/processors"
    },
    "users" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/application_profile"
    }
  }
}
```

Disable an `Applications's` ability to create new `Settlements`

#### HTTP Request

`PUT https://api-staging.crbpay.io/applications/:APPLICATION_ID`

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
curl https://api-staging.crbpay.io/applications/APfz6mtTf41HacNCNiixy57c/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '{}'

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
  "id" : "USf45bEsYfXFWUs6gb59hece",
  "password" : "4617348d-b224-4914-84d4-283141ef55c3",
  "identity" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-07-06T05:32:51.68Z",
  "updated_at" : "2017-07-06T05:32:51.68Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/users/USf45bEsYfXFWUs6gb59hece"
    },
    "applications" : {
      "href" : "https://api-staging.crbpay.io:443/applications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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

`POST https://api-staging.crbpay.io/applications/:APPLICATION_ID/users`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:APPLICATION_ID | ID of the `Application` you would like to create keys for

## [ADMIN] List all Applications
```shell
curl https://api-staging.crbpay.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410

```
```java

```
```php
<?php

```
```python


from crossriver.resources import Application

application = Application.get()
```
> Example Response:

```json
{
  "_embedded" : {
    "applications" : [ {
      "id" : "APfz6mtTf41HacNCNiixy57c",
      "enabled" : true,
      "tags" : {
        "application_name" : "Paypal"
      },
      "owner" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
      "processing_enabled" : true,
      "settlement_enabled" : false,
      "created_at" : "2017-07-06T05:32:34.98Z",
      "updated_at" : "2017-07-06T05:32:38.57Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
        },
        "processors" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/processors"
        },
        "users" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
        },
        "transfers" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c/application_profile"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io/applications/?offset=0&limit=20&sort=created_at,desc"
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

`GET https://api-staging.crbpay.io/applications/`


# Identities

An `Identity` resource represents either a person or business and is in many ways the centerpiece of the payment API's 
architecture. Transfers and Payment `Instruments` must be associated with an `Identity`. This structure makes it easy 
to manage and reconcile their associated payment history, transaction history, and payouts.

This field is optionally used to collect KYC information for the recipient.
## Create an Identity for a Recipient


```shell
curl https://api-staging.crbpay.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Marshall", 
	        "last_name": "Curry", 
	        "email": "Marshall@gmail.com", 
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
	        "first_name"=> "Marshall", 
	        "last_name"=> "Curry", 
	        "email"=> "Marshall@gmail.com", 
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
	        "first_name": "Marshall", 
	        "last_name": "Curry", 
	        "email": "Marshall@gmail.com", 
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
  "id" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "entity" : {
    "title" : null,
    "first_name" : "Marshall",
    "last_name" : "Curry",
    "email" : "Marshall@gmail.com",
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
  "created_at" : "2017-07-06T05:32:39.95Z",
  "updated_at" : "2017-07-06T05:32:39.95Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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

## Fetch a Identity

```shell

curl https://api-staging.crbpay.io/identities/ID31nVq9QQ2HZTUvMsjQQHe \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("ID31nVq9QQ2HZTUvMsjQQHe").get();
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

$identity = Identity::retrieve('ID31nVq9QQ2HZTUvMsjQQHe');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="ID31nVq9QQ2HZTUvMsjQQHe")

```
> Example Response:

```json
{
  "id" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "entity" : {
    "title" : null,
    "first_name" : "Fran",
    "last_name" : "Diaz",
    "email" : "Step@gmail.com",
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
  "created_at" : "2017-07-06T05:32:39.93Z",
  "updated_at" : "2017-07-06T05:32:48.89Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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

## Update an Identity
```shell
curl https://api-staging.crbpay.io/identities/ID31nVq9QQ2HZTUvMsjQQHe \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Fran", 
	        "last_name": "Diaz", 
	        "email": "Step@gmail.com", 
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
  "id" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "entity" : {
    "title" : null,
    "first_name" : "Fran",
    "last_name" : "Diaz",
    "email" : "Step@gmail.com",
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
  "created_at" : "2017-07-06T05:32:39.93Z",
  "updated_at" : "2017-07-06T05:32:48.89Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/disputes"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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

## List all Identities
```shell
curl https://api-staging.crbpay.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410


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
      "id" : "ID31nVq9QQ2HZTUvMsjQQHe",
      "entity" : {
        "title" : null,
        "first_name" : "Fran",
        "last_name" : "Diaz",
        "email" : "Step@gmail.com",
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
      "created_at" : "2017-07-06T05:32:39.93Z",
      "updated_at" : "2017-07-06T05:32:48.89Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
        },
        "verifications" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe/disputes"
        },
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
        }
      }
    }, {
      "id" : "IDkS4LuSJkoKTEJZ6pV1PeDg",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Paypal",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
        "doing_business_as" : "Paypal",
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
        "application_name" : "Paypal"
      },
      "created_at" : "2017-07-06T05:32:34.98Z",
      "updated_at" : "2017-07-06T05:32:35.00Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg"
        },
        "verifications" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/identities/IDkS4LuSJkoKTEJZ6pV1PeDg/disputes"
        },
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}'

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKoWRX22WA5YEfzmUfFejhwB")
    .identity("ID31nVq9QQ2HZTUvMsjQQHe")
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
	    "token"=> "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID31nVq9QQ2HZTUvMsjQQHe"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKoWRX22WA5YEfzmUfFejhwB", 
	    "type": "TOKEN", 
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIoWRX22WA5YEfzmUfFejhwB",
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
  "created_at" : "2017-07-06T05:33:00.89Z",
  "updated_at" : "2017-07-06T05:33:00.89Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIoWRX22WA5YEfzmUfFejhwB/updates"
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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "name": "Marcie Henderson", 
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
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
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
        .identity("ID31nVq9QQ2HZTUvMsjQQHe")
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

$identity = Identity::retrieve('ID31nVq9QQ2HZTUvMsjQQHe');
$card = new PaymentCard(
	array(
	    "name"=> "Marcie Henderson", 
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
	    "identity"=> "ID31nVq9QQ2HZTUvMsjQQHe"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Marcie Henderson", 
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
	    "identity": "ID31nVq9QQ2HZTUvMsjQQHe"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "fingerprint" : "FPR764826810",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Henderson",
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
  "created_at" : "2017-07-06T05:32:41.84Z",
  "updated_at" : "2017-07-06T05:32:41.84Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/updates"
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
curl https://api-staging.crbpay.io/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \

```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;
;

Maybe<PaymentCard> response = api.instruments
  .id("PIpEUWYVBT1F3uDAKNh7MbZ5")
  .get();

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

$card = PaymentInstrument::retrieve('PIpEUWYVBT1F3uDAKNh7MbZ5');

```
```python



```
> Example Response:

```json
{
  "id" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "fingerprint" : "FPR764826810",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Marcie Henderson",
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
  "created_at" : "2017-07-06T05:32:41.80Z",
  "updated_at" : "2017-07-06T05:32:41.80Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
    },
    "authorizations" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "transfers" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/verifications"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "updates" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/updates"
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
curl https://api-staging.crbpay.io/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
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

Maybe<Verification> verificationResponse = api.instruments.id("PIpEUWYVBT1F3uDAKNh7MbZ5").verifications.post(verificationForm);
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


from crossriver.resources import PaymentInstrument
from crossriver.resources import Verification


payment_card = PaymentInstrument.get(id="PIpEUWYVBT1F3uDAKNh7MbZ5")

verify = payment_card.verify_on(Verification(**
	{
	    "processor": "VISA_V1"
	}))

```
> Example Response:

```json
{
  "id" : "VIqegfG9kHrrzLGNHGgbsvmS",
  "tags" : { },
  "messages" : [ ],
  "raw" : {
    "validation_details" : {
      "systems_trace_audit_number" : "448",
      "transaction_identifier" : "1234",
      "approval_code" : "003403",
      "action_code" : "85",
      "response_code" : "5",
      "address_verification_results" : "N"
    },
    "inquiry_details" : {
      "systems_trace_audit_number" : "448",
      "card_type_code" : "C",
      "billing_currency_code" : 986,
      "billing_currency_minor_digits" : 2,
      "issuer_name" : "Visa Test Bank",
      "card_issuer_country_code" : 76,
      "fast_funds_indicator" : "N",
      "push_funds_block_indicator" : "N",
      "online_gambing_block_indicator" : "Y"
    },
    "general_inquiry_details" : {
      "systems_trace_audit_number" : "448",
      "status" : {
        "status_code" : "CDI000",
        "status_description" : "Success"
      }
    }
  },
  "processor" : "VISA_V1",
  "state" : "SUCCEEDED",
  "created_at" : "2017-07-06T05:33:30.55Z",
  "updated_at" : "2017-07-06T05:33:33.59Z",
  "trace_id" : "448",
  "payment_instrument" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "merchant" : null,
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/verifications/VIqegfG9kHrrzLGNHGgbsvmS"
    },
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "payment_instrument" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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

#### Card Verification 2 Results (cvv2_result_code)
Letter | Description
------ | -------------------------------------------------------------------
M | CVV  verified
N, P, S | CVV not verified
U | Issuer does not participate in CVV2 service

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
N | Does not accept push-to-card payments

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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIpEUWYVBT1F3uDAKNh7MbZ5", 
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
        .destination("PIpEUWYVBT1F3uDAKNh7MbZ5")
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
	    "destination"=> "PIpEUWYVBT1F3uDAKNh7MbZ5", 
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
  "id" : "TRbBHbTQoC2uPxLUDYFA2x1c",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "447",
  "currency" : "USD",
  "application" : "APfz6mtTf41HacNCNiixy57c",
  "source" : "PImfHE94yj98755zDc86WGbG",
  "destination" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:32:45.28Z",
  "updated_at" : "2017-07-06T05:32:47.48Z",
  "idempotency_id" : null,
  "merchant_identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PImfHE94yj98755zDc86WGbG"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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


## Fetch a Payout

```shell

curl https://api-staging.crbpay.io/transfers/TRbBHbTQoC2uPxLUDYFA2x1c \
    -H "Content-Type: application/vnd.json+api" \
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410


```
```java
import io.crb.payments.forms.*;
import io.crb.payments.views.*;
import io.crb.payments.interfaces.ApiError;
import io.crb.payments.interfaces.Maybe;

Maybe<Transfer> response = api.transfers.id("TRbBHbTQoC2uPxLUDYFA2x1c").get();
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

$transfer = Transfer::retrieve('TRbBHbTQoC2uPxLUDYFA2x1c');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRbBHbTQoC2uPxLUDYFA2x1c")

```
> Example Response:

```json
{
  "id" : "TRbBHbTQoC2uPxLUDYFA2x1c",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "447",
  "currency" : "USD",
  "application" : "APfz6mtTf41HacNCNiixy57c",
  "source" : "PImfHE94yj98755zDc86WGbG",
  "destination" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "CRB*CRB PAY",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-07-06T05:32:45.22Z",
  "updated_at" : "2017-07-06T05:32:47.48Z",
  "idempotency_id" : null,
  "merchant_identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
    },
    "self" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
    },
    "reversals" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/disputes"
    },
    "source" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PImfHE94yj98755zDc86WGbG"
    },
    "destination" : {
      "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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
    -u  USiFamqVgvMwqN2yS1Ky8GEA:d699b9a5-40f9-492d-ae93-f96c3c306410

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
      "id" : "TRbBHbTQoC2uPxLUDYFA2x1c",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "447",
      "currency" : "USD",
      "application" : "APfz6mtTf41HacNCNiixy57c",
      "source" : "PImfHE94yj98755zDc86WGbG",
      "destination" : "PIpEUWYVBT1F3uDAKNh7MbZ5",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "CRB*CRB PAY",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-07-06T05:32:45.22Z",
      "updated_at" : "2017-07-06T05:32:47.48Z",
      "idempotency_id" : null,
      "merchant_identity" : "ID31nVq9QQ2HZTUvMsjQQHe",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.crbpay.io:443/applications/APfz6mtTf41HacNCNiixy57c"
        },
        "self" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.crbpay.io:443/identities/ID31nVq9QQ2HZTUvMsjQQHe"
        },
        "reversals" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.crbpay.io:443/transfers/TRbBHbTQoC2uPxLUDYFA2x1c/disputes"
        },
        "source" : {
          "href" : "https://api-staging.crbpay.io:443/payment_instruments/PImfHE94yj98755zDc86WGbG"
        },
        "destination" : {
          "href" : "https://api-staging.crbpay.io:443/payment_instruments/PIpEUWYVBT1F3uDAKNh7MbZ5"
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
