---
title: CrossRiver API Reference

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

3. [Push-to-Card](#push-to-card): This guide walks
through using the Visa Direct API to push payments to debit cards. With push-to-card
funds are disbursed to a debit card within 30 minutes or less. 

4. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.crossriver.payments.processing.client</groupId>
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

import io.crossriver.payments.processing.client.ProcessingClient;
import io.crossriver.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("https://api-staging.finix.io");
  client.setupUserIdAndPassword("UScmCeWVYZdFSFzAThVurdq2", "e72014c4-bbd8-4418-9973-399cbeaf4dc2");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CrossRiver/Settings.php');

CrossRiver\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'UScmCeWVYZdFSFzAThVurdq2',
	"password" => 'e72014c4-bbd8-4418-9973-399cbeaf4dc2']
	);

require(__DIR__ . '/src/CrossRiver/Bootstrap.php');
CrossRiver\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("UScmCeWVYZdFSFzAThVurdq2", "e72014c4-bbd8-4418-9973-399cbeaf4dc2"))

```
To communicate with the CrossRiver API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `UScmCeWVYZdFSFzAThVurdq2`

- Password: `e72014c4-bbd8-4418-9973-399cbeaf4dc2`

- Application ID: `APdotQeZPi5LhR2cLvVJ4TfN`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely seperate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://api-staging.finix.io`

- **Production API:** `https://api.finix.io`

## Push-to-Card
### Step 1: Create a Recipient Identity
```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Amy", 
	        "last_name": "Green", 
	        "email": "Amy@gmail.com", 
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

import io.crossriver.payments.processing.client.model.Address;
import io.crossriver.payments.processing.client.model.BankAccountType;
import io.crossriver.payments.processing.client.model.BusinessType;
import io.crossriver.payments.processing.client.model.Date;
import io.crossriver.payments.processing.client.model.Entity;
import io.crossriver.payments.processing.client.model.Identity;;

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
        .dob(Date.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1000l)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .defaultStatementDescriptor("Business Inc")
        .incorporationDate(Date.builder()
          .day(1)
          .month(12)
          .year(2012)
          .build()
        )
        .principalPercentageOwnership(51)
        .build()
    )
    .build()
);

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = new Identity(IDnTDxow7BMHoyEt4jmxUWaT);
$identity = $identity->save();



```
```python



```
> Example Response:

```json
{
  "id" : "IDnTDxow7BMHoyEt4jmxUWaT",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
    "last_name" : "Green",
    "email" : "Amy@gmail.com",
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
  "created_at" : "2017-03-27T17:56:01.99Z",
  "updated_at" : "2017-03-27T17:56:01.99Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP3V4Max5GyNR9rS2DuViufX"
    }
  }
}
```

Use the resulting ID of the newly created Recipient Identity to associate any payouts or payment instruments that are used. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds.

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

### Step 2:  Add a Payment Instrument for the Recipient 

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "name": "Alex Henderson", 
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
	    "identity": "IDnTDxow7BMHoyEt4jmxUWaT"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDptkXTi55kx3iPeZNCQ7ooC")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDnTDxow7BMHoyEt4jmxUWaT');
$card = new PaymentCard(
	array(
	    "name"=> "Alex Henderson", 
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
	    "identity"=> "IDnTDxow7BMHoyEt4jmxUWaT"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PI6XNN1UVJDQJkJH1yNcDx2H",
  "fingerprint" : "FPR316679720",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Alex Henderson",
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
  "created_at" : "2017-03-27T17:56:02.39Z",
  "updated_at" : "2017-03-27T17:56:02.39Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnTDxow7BMHoyEt4jmxUWaT",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP3V4Max5GyNR9rS2DuViufX"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H/updates"
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

### Step 3: Provision Sender Account
```shell
curl https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
Identity identity = client.identitiesClient().fetchResource("IDnTDxow7BMHoyEt4jmxUWaT");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use CrossRiver\Resources\Identity;
use CrossRiver\Resources\Merchant;

$identity = Identity::retrieve('IDnTDxow7BMHoyEt4jmxUWaT');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MUkpJorYSP6Lpy98htN25GB5",
  "identity" : "IDnTDxow7BMHoyEt4jmxUWaT",
  "verification" : "VImG9iFfKEqk2iHEsGokPi7w",
  "merchant_profile" : "MP2oiKJvX4pfvyWuEpa448Qm",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-27T17:56:02.78Z",
  "updated_at" : "2017-03-27T17:56:02.78Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUkpJorYSP6Lpy98htN25GB5"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUkpJorYSP6Lpy98htN25GB5/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MP2oiKJvX4pfvyWuEpa448Qm"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP3V4Max5GyNR9rS2DuViufX"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VImG9iFfKEqk2iHEsGokPi7w"
    }
  }
}
```

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor


### Step 4: Send Payout

Once you have tokenized the payment card as above you can send funds to it at any time by simply calling the API


```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PI6XNN1UVJDQJkJH1yNcDx2H", 
	    "processor": "VISA_V1", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
Map<String,String> tags = new HashMap<String,String>();
tags.put("order_number", "21DFASJSAKAS");

Transfer cardPayout = client.transfersClient().save(
  Transfer.builder()
    .tags(tags)
    .merchantIdentity(identity.getId())
    .destination(paymentCard.getId())
    .currency("USD")
    .amount(10000l)
    .processor("VISA_V1")
    .build()
);

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PI6XNN1UVJDQJkJH1yNcDx2H", 
	    "processor"=> "VISA_V1", 
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
  "id" : "TR6qsqqnWaK4YCP3v49AECb5",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190756",
  "currency" : "USD",
  "application" : "AP3V4Max5GyNR9rS2DuViufX",
  "source" : "PIe9eS3z9abL9f8DVxDTr3Fo",
  "destination" : "PI6XNN1UVJDQJkJH1yNcDx2H",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T17:56:03.74Z",
  "updated_at" : "2017-03-27T17:56:05.22Z",
  "merchant_identity" : "IDnTDxow7BMHoyEt4jmxUWaT",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP3V4Max5GyNR9rS2DuViufX"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qsqqnWaK4YCP3v49AECb5"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qsqqnWaK4YCP3v49AECb5/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDnTDxow7BMHoyEt4jmxUWaT"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qsqqnWaK4YCP3v49AECb5/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qsqqnWaK4YCP3v49AECb5/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TR6qsqqnWaK4YCP3v49AECb5/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIe9eS3z9abL9f8DVxDTr3Fo"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6XNN1UVJDQJkJH1yNcDx2H"
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
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
statement_descriptor | *string*, **required** | Description that will show up on card statement 
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)


## Embedded Tokenization

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
          applicationId: 'APdotQeZPi5LhR2cLvVJ4TfN',
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
  "id" : "TKwmZpfw8HatEbbXLXMGzbo3",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-27T17:55:55.27Z",
  "updated_at" : "2017-03-27T17:55:55.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-28T17:55:55.27Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKwmZpfw8HatEbbXLXMGzbo3")
    .identity("IDptkXTi55kx3iPeZNCQ7ooC")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDptkXTi55kx3iPeZNCQ7ooC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIwmZpfw8HatEbbXLXMGzbo3",
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
  "created_at" : "2017-03-27T17:55:55.66Z",
  "updated_at" : "2017-03-27T17:55:55.66Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/updates"
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
    server: "https://api-staging.finix.io",
    applicationId: "APdotQeZPi5LhR2cLvVJ4TfN",
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
  "id" : "TKwmZpfw8HatEbbXLXMGzbo3",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-27T17:55:55.27Z",
  "updated_at" : "2017-03-27T17:55:55.27Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-28T17:55:55.27Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}'

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKwmZpfw8HatEbbXLXMGzbo3")
    .identity("IDptkXTi55kx3iPeZNCQ7ooC")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDptkXTi55kx3iPeZNCQ7ooC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIwmZpfw8HatEbbXLXMGzbo3",
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
  "created_at" : "2017-03-27T17:55:55.66Z",
  "updated_at" : "2017-03-27T17:55:55.66Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/updates"
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
  "id" : "USn41KywSS1sZapjwjDAvWax",
  "password" : "7aec6331-7e19-4d1f-931a-6f59c35eaeca",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:40.01Z",
  "updated_at" : "2017-03-27T17:55:40.01Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USn41KywSS1sZapjwjDAvWax"
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
	        "application_name": "Facebook"
	    }, 
	    "user": "USn41KywSS1sZapjwjDAvWax", 
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
	        "doing_business_as": "Facebook", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Facebook", 
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
use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USn41KywSS1sZapjwjDAvWax", 
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
	        "doing_business_as"=> "Facebook", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Facebook", 
	        "business_tax_id"=> "123456789", 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	));
$application = $application->save();
```
```python



```
> Example Response:

```json
{
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T17:55:40.40Z",
  "updated_at" : "2017-03-27T17:55:40.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
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
  "id" : "PRo8AtG7WWPKb9wo7c59udk8",
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "default_merchant_profile" : "MP95wtKfbhdbPA6unHrBtyXD",
  "created_at" : "2017-03-27T17:55:40.97Z",
  "updated_at" : "2017-03-27T17:55:40.97Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors/PRo8AtG7WWPKb9wo7c59udk8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "processing_enabled": true
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
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : true,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T17:55:40.39Z",
  "updated_at" : "2017-03-27T17:56:13.27Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
### Step 5: Enable Settlement Functionality
```shell
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -X PUT \
    -d '
	{
	    "settlement_enabled": true
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
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T17:55:40.39Z",
  "updated_at" : "2017-03-27T17:56:13.62Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use CrossRiver\Resources\Application;

$application = Application::retrieve('APdotQeZPi5LhR2cLvVJ4TfN');

```
```python


from crossriver.resources import Application

application = Application.get(id="APdotQeZPi5LhR2cLvVJ4TfN")
```
> Example Response:

```json
{
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T17:55:40.39Z",
  "updated_at" : "2017-03-27T17:55:42.64Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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

## Create an Application
```shell
curl https://api-staging.finix.io/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
    -d '
	{
	    "tags": {
	        "application_name": "Facebook"
	    }, 
	    "user": "USn41KywSS1sZapjwjDAvWax", 
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
	        "doing_business_as": "Facebook", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Facebook", 
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
use CrossRiver\Resources\Application;

$application = new Application(
	array(
	    "tags"=> array(
	        "application_name"=> "Facebook"
	    ), 
	    "user"=> "USn41KywSS1sZapjwjDAvWax", 
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
	        "doing_business_as"=> "Facebook", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "business_name"=> "Facebook", 
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
	        "application_name": "Facebook"
	    }, 
	    "user": "USn41KywSS1sZapjwjDAvWax", 
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
	        "doing_business_as": "Facebook", 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "Facebook", 
	        "business_tax_id": "123456789", 
	        "email": "user@example.org", 
	        "tax_id": "5779"
	    }
	}).save()
```
> Example Response:

```json
{
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T17:55:40.40Z",
  "updated_at" : "2017-03-27T17:55:40.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
## [ADMIN] Disable Processing Functionality
```shell
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
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
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-03-27T17:55:40.39Z",
  "updated_at" : "2017-03-27T17:56:11.81Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
## [ADMIN] Disable Settlement Functionality
```shell
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
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
  "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "enabled" : true,
  "tags" : {
    "application_name" : "Facebook"
  },
  "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-27T17:55:40.39Z",
  "updated_at" : "2017-03-27T17:56:12.16Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
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
  "id" : "USsXvzMt65HUJXNthWuEZDXc",
  "password" : "cc2d3c88-6c10-424e-aee3-3e96a27189e6",
  "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:41.49Z",
  "updated_at" : "2017-03-27T17:55:41.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USsXvzMt65HUJXNthWuEZDXc"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
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
  "id" : "PRo8AtG7WWPKb9wo7c59udk8",
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "default_merchant_profile" : "MP95wtKfbhdbPA6unHrBtyXD",
  "created_at" : "2017-03-27T17:55:40.97Z",
  "updated_at" : "2017-03-27T17:55:40.97Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors/PRo8AtG7WWPKb9wo7c59udk8"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

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
      "id" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "enabled" : true,
      "tags" : {
        "application_name" : "Facebook"
      },
      "owner" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-03-27T17:55:40.39Z",
      "updated_at" : "2017-03-27T17:55:42.64Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/application_profile"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Marcie", 
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
```java

import io.crossriver.payments.processing.client.model.Identity;

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
```php
<?php
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Marcie", 
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
	        "phone": "7145677613", 
	        "first_name": "Marcie", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "IDv287X9zMoAwDKuXwKYSGUV",
  "entity" : {
    "title" : null,
    "first_name" : "Marcie",
    "last_name" : "Kline",
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
  "created_at" : "2017-03-27T17:55:48.86Z",
  "updated_at" : "2017-03-27T17:55:48.86Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
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
	        "ownership_type": "PRIVATE", 
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
```java

import io.crossriver.payments.processing.client.model.Address;
import io.crossriver.payments.processing.client.model.BankAccountType;
import io.crossriver.payments.processing.client.model.BusinessType;
import io.crossriver.payments.processing.client.model.Date;
import io.crossriver.payments.processing.client.model.Entity;
import io.crossriver.payments.processing.client.model.Identity;

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
        .dob(Date.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1000l)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .defaultStatementDescriptor("Business Inc")
        .incorporationDate(Date.builder()
          .day(1)
          .month(12)
          .year(2012)
          .build()
        )
        .principalPercentageOwnership(51)
        .build()
    )
    .build()
);

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Golds Gym", 
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
	        "ownership_type"=> "PRIVATE", 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Golds Gym", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Golds Gym", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.GoldsGym.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

```
```python


from crossriver.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": True, 
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
	        "ownership_type": "PRIVATE", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "IDptkXTi55kx3iPeZNCQ7ooC",
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
  "created_at" : "2017-03-27T17:55:43.30Z",
  "updated_at" : "2017-03-27T17:55:43.30Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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

curl https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDptkXTi55kx3iPeZNCQ7ooC");

```
```php
<?php
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDptkXTi55kx3iPeZNCQ7ooC');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDptkXTi55kx3iPeZNCQ7ooC")

```
> Example Response:

```json
{
  "id" : "IDptkXTi55kx3iPeZNCQ7ooC",
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
  "created_at" : "2017-03-27T17:55:43.28Z",
  "updated_at" : "2017-03-27T17:55:43.28Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "Henderson", 
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
  "id" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "Henderson",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
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
    "key" : "value_2"
  },
  "created_at" : "2017-03-27T17:55:43.28Z",
  "updated_at" : "2017-03-27T17:56:10.29Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2


```
```java
import io.crossriver.payments.processing.client.model.Identity;

client.identitiesClient().<Resources<Identity>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Identity> identities = page.getContent();
    //do something
  });

```
```php
<?php
use CrossRiver\Resources\Identity;

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
      "id" : "IDv287X9zMoAwDKuXwKYSGUV",
      "entity" : {
        "title" : null,
        "first_name" : "Marcie",
        "last_name" : "Kline",
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
      "created_at" : "2017-03-27T17:55:48.85Z",
      "updated_at" : "2017-03-27T17:55:48.85Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDmbHALLpPqn3JfMnDoWeEtf",
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
      "created_at" : "2017-03-27T17:55:46.98Z",
      "updated_at" : "2017-03-27T17:55:46.98Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDmbHALLpPqn3JfMnDoWeEtf/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDfzT87JJc4UYTLs2XVyNRkL",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Golds Gym",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
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
      "created_at" : "2017-03-27T17:55:46.62Z",
      "updated_at" : "2017-03-27T17:55:46.62Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDfzT87JJc4UYTLs2XVyNRkL/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "ID7LCfY2f93TWWsfSiPu9iGn",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Lees Sandwiches"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T17:55:46.19Z",
      "updated_at" : "2017-03-27T17:55:46.19Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7LCfY2f93TWWsfSiPu9iGn/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDc1xcV4fiirnz4zyTyVs8Vu",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "ASSOCIATION_ESTATE_TRUST",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T17:55:45.84Z",
      "updated_at" : "2017-03-27T17:55:45.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDc1xcV4fiirnz4zyTyVs8Vu/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDeM1GqmNcWZYRtkt4gvVVVH",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "GENERAL_PARTNERSHIP",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T17:55:45.48Z",
      "updated_at" : "2017-03-27T17:55:45.48Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDeM1GqmNcWZYRtkt4gvVVVH/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDreEZo39eRx3uESu12Yuscq",
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
      "created_at" : "2017-03-27T17:55:45.09Z",
      "updated_at" : "2017-03-27T17:55:45.09Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDreEZo39eRx3uESu12Yuscq/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDpWViy5N3PZr9EaaKFkwQC3",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Prestige World Wide",
        "business_type" : "PARTNERSHIP",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Prestige World Wide"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T17:55:44.60Z",
      "updated_at" : "2017-03-27T17:55:44.60Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpWViy5N3PZr9EaaKFkwQC3/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDvtaURhUMo1LD6xyQRpKUtM",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "ACME Anchors",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
      "created_at" : "2017-03-27T17:55:44.20Z",
      "updated_at" : "2017-03-27T17:55:44.20Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDvtaURhUMo1LD6xyQRpKUtM/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "ID8iQocBEdrgYVhpYYrbsw68",
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-27T17:55:43.84Z",
      "updated_at" : "2017-03-27T17:55:43.84Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID8iQocBEdrgYVhpYYrbsw68/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDptkXTi55kx3iPeZNCQ7ooC",
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
      "created_at" : "2017-03-27T17:55:43.28Z",
      "updated_at" : "2017-03-27T17:55:43.28Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Facebook",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "application_name" : "Facebook"
      },
      "created_at" : "2017-03-27T17:55:40.39Z",
      "updated_at" : "2017-03-27T17:55:40.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    "count" : 12
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/identities/`


# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;
import io.crossriver.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TKwmZpfw8HatEbbXLXMGzbo3")
    .identity("IDptkXTi55kx3iPeZNCQ7ooC")
    .build()
);

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDptkXTi55kx3iPeZNCQ7ooC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKwmZpfw8HatEbbXLXMGzbo3", 
	    "type": "TOKEN", 
	    "identity": "IDptkXTi55kx3iPeZNCQ7ooC"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIwmZpfw8HatEbbXLXMGzbo3",
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
  "created_at" : "2017-03-27T17:55:55.66Z",
  "updated_at" : "2017-03-27T17:55:55.66Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/updates"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "name": "Laura White", 
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
	    "identity": "IDv287X9zMoAwDKuXwKYSGUV"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDptkXTi55kx3iPeZNCQ7ooC")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CrossRiver\Resources\PaymentCard;
use CrossRiver\Resources\Identity;

$identity = Identity::retrieve('IDptkXTi55kx3iPeZNCQ7ooC');
$card = new PaymentCard(
	array(
	    "name"=> "Laura White", 
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
	    "identity"=> "IDv287X9zMoAwDKuXwKYSGUV"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Laura White", 
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
	    "identity": "IDv287X9zMoAwDKuXwKYSGUV"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIt4Y7QuT5efbXKhSt4ch8ss",
  "fingerprint" : "FPR1214397770",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura White",
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
  "created_at" : "2017-03-27T17:55:49.63Z",
  "updated_at" : "2017-03-27T17:55:49.63Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDv287X9zMoAwDKuXwKYSGUV",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/updates"
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

## Fetch a Credit Card
```shell
curl https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIt4Y7QuT5efbXKhSt4ch8ss")

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIt4Y7QuT5efbXKhSt4ch8ss');

```
```python



```
> Example Response:

```json
{
  "id" : "PIt4Y7QuT5efbXKhSt4ch8ss",
  "fingerprint" : "FPR1214397770",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura White",
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
  "created_at" : "2017-03-27T17:55:49.60Z",
  "updated_at" : "2017-03-27T17:55:53.72Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDv287X9zMoAwDKuXwKYSGUV",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Update a Payment Instrument
```shell
curl https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "Display Name": "Updated Field"
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
  "id" : "PI5bsRcn2pn7VbSd8bEiHQ5S",
  "fingerprint" : "FPR-1215770130",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXX3123",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-03-27T17:55:47.36Z",
  "updated_at" : "2017-03-27T17:55:47.76Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2
```
```java
import io.crossriver.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

```
```php
<?php
use CrossRiver\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
```python



```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIwmZpfw8HatEbbXLXMGzbo3",
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
      "created_at" : "2017-03-27T17:55:55.61Z",
      "updated_at" : "2017-03-27T17:55:55.61Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIwmZpfw8HatEbbXLXMGzbo3/updates"
        }
      }
    }, {
      "id" : "PI7DByuBFyWWPmzwAudVqCeQ",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-27T17:55:49.97Z",
      "updated_at" : "2017-03-27T17:55:49.97Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDv287X9zMoAwDKuXwKYSGUV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7DByuBFyWWPmzwAudVqCeQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7DByuBFyWWPmzwAudVqCeQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7DByuBFyWWPmzwAudVqCeQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7DByuBFyWWPmzwAudVqCeQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIt4Y7QuT5efbXKhSt4ch8ss",
      "fingerprint" : "FPR1214397770",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Laura White",
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
      "created_at" : "2017-03-27T17:55:49.60Z",
      "updated_at" : "2017-03-27T17:55:53.72Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDv287X9zMoAwDKuXwKYSGUV",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDv287X9zMoAwDKuXwKYSGUV"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "updates" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss/updates"
        }
      }
    }, {
      "id" : "PIfkhVCRegK7gMsUwfGxuG7f",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:48.15Z",
      "updated_at" : "2017-03-27T17:55:48.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfkhVCRegK7gMsUwfGxuG7f"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfkhVCRegK7gMsUwfGxuG7f/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfkhVCRegK7gMsUwfGxuG7f/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIfkhVCRegK7gMsUwfGxuG7f/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIofjgEgchy8Aops61VQMFLQ",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:48.15Z",
      "updated_at" : "2017-03-27T17:55:48.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIofjgEgchy8Aops61VQMFLQ"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIofjgEgchy8Aops61VQMFLQ/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIofjgEgchy8Aops61VQMFLQ/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIofjgEgchy8Aops61VQMFLQ/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:48.15Z",
      "updated_at" : "2017-03-27T17:55:48.15Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PI5bsRcn2pn7VbSd8bEiHQ5S",
      "fingerprint" : "FPR-1215770130",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXX3123",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-03-27T17:55:47.36Z",
      "updated_at" : "2017-03-27T17:55:47.76Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI5bsRcn2pn7VbSd8bEiHQ5S/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIhNtmwJnz6NWfXZexJRYVF6",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:40.95Z",
      "updated_at" : "2017-03-27T17:55:40.95Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "ID8bW3W9DmKEgFYF4GfDJ8or",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhNtmwJnz6NWfXZexJRYVF6"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhNtmwJnz6NWfXZexJRYVF6/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/ID8bW3W9DmKEgFYF4GfDJ8or"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhNtmwJnz6NWfXZexJRYVF6/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIhNtmwJnz6NWfXZexJRYVF6/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIrJheaR7opmA68vJMmsoBtx",
      "fingerprint" : "FPR-2042121662",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:40.95Z",
      "updated_at" : "2017-03-27T17:55:40.95Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrJheaR7opmA68vJMmsoBtx"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrJheaR7opmA68vJMmsoBtx/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrJheaR7opmA68vJMmsoBtx/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIrJheaR7opmA68vJMmsoBtx/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PIqPfu4N26xnZzurZfhnmEMg",
      "fingerprint" : "FPR-1383578548",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:40.95Z",
      "updated_at" : "2017-03-27T17:55:40.95Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPfu4N26xnZzurZfhnmEMg"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPfu4N26xnZzurZfhnmEMg/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPfu4N26xnZzurZfhnmEMg/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIqPfu4N26xnZzurZfhnmEMg/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "PI9QA8qCE2mD1F6CXPNV2Qbn",
      "fingerprint" : "FPR-1645745263",
      "tags" : { },
      "name" : null,
      "created_at" : "2017-03-27T17:55:40.95Z",
      "updated_at" : "2017-03-27T17:55:40.95Z",
      "instrument_type" : "VIRTUAL",
      "type" : "VIRTUAL",
      "currency" : "USD",
      "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9QA8qCE2mD1F6CXPNV2Qbn"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9QA8qCE2mD1F6CXPNV2Qbn/authorizations"
        },
        "identity" : {
          "href" : "https://api-staging.finix.io/identities/IDuwB4ZnZxZF8DgbP49LY7fX"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9QA8qCE2mD1F6CXPNV2Qbn/transfers"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI9QA8qCE2mD1F6CXPNV2Qbn/verifications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    "count" : 11
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/payment_instruments`

# Payouts

A `Payout` represents any flow of funds either to or from a `Payment Instrument`.
For example, a `Payout` can be either a [debit to a card](#debit-a-card), a
credit to a bank account, or a [refund to a card](#refund-a-debit) depending on
the request.

`Payouts` can have three possible states values: PENDING, SUCCEEDED, or FAILED.

- **SUCCEEDED:** Funds captured and available for settlement (i.e. disbursement
via ACH Credit)
        
- **FAILED:** Authorization attempt failed

By default, `Payouts` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

## Debit a Card

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
	{
	    "fee": 86212, 
	    "source": "PI7DByuBFyWWPmzwAudVqCeQ", 
	    "merchant_identity": "IDptkXTi55kx3iPeZNCQ7ooC", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 862124
	}'


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDptkXTi55kx3iPeZNCQ7ooC")
      .source("PIt4Y7QuT5efbXKhSt4ch8ss")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```
```php
<?php
use CrossRiver\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 78020, 
	    "source"=> "PIt4Y7QuT5efbXKhSt4ch8ss", 
	    "merchant_identity"=> "IDptkXTi55kx3iPeZNCQ7ooC", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 780202
	));
$debit = $debit->save();
```
```python



```


> Example Response:

```json
{
  "id" : "TRoPjWASFFrftXHxAHAiSnX3",
  "amount" : 780202,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "03d78679-7bd5-4470-af18-3d342e58ca64",
  "currency" : "USD",
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "source" : "PIt4Y7QuT5efbXKhSt4ch8ss",
  "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
  "ready_to_settle_at" : null,
  "fee" : 78020,
  "statement_descriptor" : "FIN*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T17:55:50.46Z",
  "updated_at" : "2017-03-27T17:55:50.53Z",
  "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
    }
  }
}
```

A `Payout` representing a customer payment where funds are obtained from a
card (i.e. debit). These specific `Payouts` are distinguished by their type
which return DEBIT.

#### HTTP Request

`POST https://api-staging.finix.io/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be charged
amount | *integer*, **required** | The total amount that will be charged in cents (e.g. 100 cents to charge $1.00)
fee | *integer*, **optional** | The amount of the `Payout` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Payouts` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
## Retrieve a Payout
```shell

curl https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRoPjWASFFrftXHxAHAiSnX3");

```
```php
<?php
use CrossRiver\Resources\Transfer;

$transfer = Transfer::retrieve('TRoPjWASFFrftXHxAHAiSnX3');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRoPjWASFFrftXHxAHAiSnX3")

```
> Example Response:

```json
{
  "id" : "TRoPjWASFFrftXHxAHAiSnX3",
  "amount" : 780202,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "03d78679-7bd5-4470-af18-3d342e58ca64",
  "currency" : "USD",
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "source" : "PIt4Y7QuT5efbXKhSt4ch8ss",
  "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
  "ready_to_settle_at" : null,
  "fee" : 78020,
  "statement_descriptor" : "FIN*GOLDS GYM",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T17:55:50.41Z",
  "updated_at" : "2017-03-27T17:55:50.53Z",
  "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
    }
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers/:PAYOUT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYOUT_ID | ID of the `Payout`

## Refund a Debit
```shell

curl https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d  '
          {
          "refund_amount" : 100
        }
        '

```
```java

import io.crossriver.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
```php
<?php
use CrossRiver\Resources\Transfer;

$debit = Transfer::retrieve('TRoPjWASFFrftXHxAHAiSnX3');
$refund = $debit->reverse(11);
```
```python


from crossriver.resources import Transfer

transfer = Transfer.get(id="TRoPjWASFFrftXHxAHAiSnX3")
transfer.reverse(**
          {
          "refund_amount" : 100
        }
        )
```
> Example Response:

```json
{
  "id" : "TRKo4cqPambA9BV3oN3E1dY",
  "amount" : 226252,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "060e92f5-afc5-4607-8ca5-3a4938d61340",
  "currency" : "USD",
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "source" : "PIff4xSaYNCdiJqxcg2CSKaF",
  "destination" : "PIt4Y7QuT5efbXKhSt4ch8ss",
  "ready_to_settle_at" : null,
  "fee" : 22625,
  "statement_descriptor" : "FIN*GOLDS GYM",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-27T17:55:53.07Z",
  "updated_at" : "2017-03-27T17:55:53.13Z",
  "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRKo4cqPambA9BV3oN3E1dY"
    },
    "parent" : {
      "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRKo4cqPambA9BV3oN3E1dY/payment_instruments"
    }
  }
}
```

A `Payout` representing the refund (i.e. reversal) of a previously created
`Payout` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Payout`. These specific `Payouts` are distinguished by
their type which return REVERSAL.


#### HTTP Request

`POST https://api-staging.finix.io/transfers/:PAYOUT_ID/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYOUT_ID | ID of the original `Payout`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | The amount of the refund in cents (Must be equal to or less than the amount of the original `Payout`)

## List all Payouts
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

```
```java
import io.crossriver.payments.processing.client.model.Transfer;

client.transfersClient().<Resources<Transfer>>resourcesIterator()
  .forEachRemaining(transfersPage -> {
    Collection<Transfer> transfers = transfersPage.getContent();
    //do something with `transfers`
  });

```
```php
<?php
use CrossRiver\Resources\Transfer;

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
      "id" : "TRoSNYnBkGWoxULTcxjhjTqx",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "76150d5e-dbdd-4359-9616-f55a65d4b4cb",
      "currency" : "USD",
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "source" : "PIt4Y7QuT5efbXKhSt4ch8ss",
      "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FIN*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T17:55:54.14Z",
      "updated_at" : "2017-03-27T17:56:06.89Z",
      "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRoSNYnBkGWoxULTcxjhjTqx"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRoSNYnBkGWoxULTcxjhjTqx/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRoSNYnBkGWoxULTcxjhjTqx/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRoSNYnBkGWoxULTcxjhjTqx/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRoSNYnBkGWoxULTcxjhjTqx/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
        }
      }
    }, {
      "id" : "TRKo4cqPambA9BV3oN3E1dY",
      "amount" : 226252,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "21a4b79b-d6f7-4e51-80f2-75bc634940d7",
      "currency" : "USD",
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "source" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "destination" : "PIt4Y7QuT5efbXKhSt4ch8ss",
      "ready_to_settle_at" : null,
      "fee" : 22625,
      "statement_descriptor" : "FIN*GOLDS GYM",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T17:55:52.96Z",
      "updated_at" : "2017-03-27T17:55:53.13Z",
      "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRKo4cqPambA9BV3oN3E1dY"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRKo4cqPambA9BV3oN3E1dY/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
        }
      }
    }, {
      "id" : "TR8ZH288DvVPdTo4B6XaKjdc",
      "amount" : 226252,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "50557feb-022c-4786-a220-ce2d054b0928",
      "currency" : "USD",
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "source" : "PIt4Y7QuT5efbXKhSt4ch8ss",
      "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "ready_to_settle_at" : null,
      "fee" : 22625,
      "statement_descriptor" : "FIN*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T17:55:52.53Z",
      "updated_at" : "2017-03-27T17:55:53.04Z",
      "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR8ZH288DvVPdTo4B6XaKjdc/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
        }
      }
    }, {
      "id" : "TRqjF9HyhYABzTw6xGKNeZKu",
      "amount" : 862124,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "5b69b473-1755-4408-ad90-9c0dcf525dd6",
      "currency" : "USD",
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "source" : "PI7DByuBFyWWPmzwAudVqCeQ",
      "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "ready_to_settle_at" : null,
      "fee" : 86212,
      "statement_descriptor" : "FIN*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T17:55:50.93Z",
      "updated_at" : "2017-03-27T17:55:51.03Z",
      "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRqjF9HyhYABzTw6xGKNeZKu"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRqjF9HyhYABzTw6xGKNeZKu/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRqjF9HyhYABzTw6xGKNeZKu/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRqjF9HyhYABzTw6xGKNeZKu/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRqjF9HyhYABzTw6xGKNeZKu/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI7DByuBFyWWPmzwAudVqCeQ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
        }
      }
    }, {
      "id" : "TRoPjWASFFrftXHxAHAiSnX3",
      "amount" : 780202,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "03d78679-7bd5-4470-af18-3d342e58ca64",
      "currency" : "USD",
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "source" : "PIt4Y7QuT5efbXKhSt4ch8ss",
      "destination" : "PIff4xSaYNCdiJqxcg2CSKaF",
      "ready_to_settle_at" : null,
      "fee" : 78020,
      "statement_descriptor" : "FIN*GOLDS GYM",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-27T17:55:50.41Z",
      "updated_at" : "2017-03-27T17:56:03.07Z",
      "merchant_identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRoPjWASFFrftXHxAHAiSnX3/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIt4Y7QuT5efbXKhSt4ch8ss"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIff4xSaYNCdiJqxcg2CSKaF"
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


## Create ROLE_PLATFORM User
```shell
curl https://api-staging.finix.io/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8 \
    -d '
	{
	    "role": "ROLE_PLATFORM"
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
  "id" : "US3zSQCcXoY7wxuSPUmp6CFg",
  "password" : "e5acb6f0-2744-4569-a117-1661a80ecb5a",
  "identity" : null,
  "enabled" : true,
  "role" : "ROLE_PLATFORM",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:41.90Z",
  "updated_at" : "2017-03-27T17:55:41.90Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US3zSQCcXoY7wxuSPUmp6CFg"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    }
  }
}
```


This is the equivalent of provisioning API keys (i.e. credentials) for a Platform.

<aside class="notice">
A credential with a level of ROLE_PLATFORM has access to all Application and Merchant data.
</aside>


#### HTTP Request

`POST https://api-staging.finix.io/users`

#### URL Parameters
Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user


## Create ROLE_MERCHANT User
```shell
curl https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
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
  "id" : "USsXvzMt65HUJXNthWuEZDXc",
  "password" : "cc2d3c88-6c10-424e-aee3-3e96a27189e6",
  "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:41.49Z",
  "updated_at" : "2017-03-27T17:55:41.49Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USsXvzMt65HUJXNthWuEZDXc"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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

## Create ROLE_MERCHANT User
```shell
curl https://api-staging.finix.io/identities/IDptkXTi55kx3iPeZNCQ7ooC/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
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
  "id" : "US67fWxbMLsp9TSkTrrJifJz",
  "password" : "23518e63-f5ac-464a-b53c-111d6704a811",
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "enabled" : true,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:51.44Z",
  "updated_at" : "2017-03-27T17:55:51.44Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US67fWxbMLsp9TSkTrrJifJz"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/users/TRoPjWASFFrftXHxAHAiSnX3 \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php

```
```python


from crossriver.resources import User
user = User.get(id="USn41KywSS1sZapjwjDAvWax")

```
> Example Response:

```json
{
  "id" : "USn41KywSS1sZapjwjDAvWax",
  "password" : null,
  "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:40.01Z",
  "updated_at" : "2017-03-27T17:55:40.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USn41KywSS1sZapjwjDAvWax"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
curl https://api-staging.finix.io/users/US67fWxbMLsp9TSkTrrJifJz \
    -H "Content-Type: application/vnd.json+api" \
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -X PUT \
    -d '
	{
	    "enabled": false
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
  "id" : "US67fWxbMLsp9TSkTrrJifJz",
  "password" : null,
  "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
  "enabled" : false,
  "role" : "ROLE_MERCHANT",
  "tags" : { },
  "created_at" : "2017-03-27T17:55:51.41Z",
  "updated_at" : "2017-03-27T17:55:51.84Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/US67fWxbMLsp9TSkTrrJifJz"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

```
```java

```
```php
<?php

```
```python


from crossriver.resources import User
users = User.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "users" : [ {
      "id" : "US67fWxbMLsp9TSkTrrJifJz",
      "password" : null,
      "identity" : "IDptkXTi55kx3iPeZNCQ7ooC",
      "enabled" : true,
      "role" : "ROLE_MERCHANT",
      "tags" : { },
      "created_at" : "2017-03-27T17:55:51.41Z",
      "updated_at" : "2017-03-27T17:55:52.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/US67fWxbMLsp9TSkTrrJifJz"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "USsXvzMt65HUJXNthWuEZDXc",
      "password" : null,
      "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-03-27T17:55:41.47Z",
      "updated_at" : "2017-03-27T17:55:41.47Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USsXvzMt65HUJXNthWuEZDXc"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
        }
      }
    }, {
      "id" : "USn41KywSS1sZapjwjDAvWax",
      "password" : null,
      "identity" : "IDuwB4ZnZxZF8DgbP49LY7fX",
      "enabled" : true,
      "role" : "ROLE_PARTNER",
      "tags" : { },
      "created_at" : "2017-03-27T17:55:40.01Z",
      "updated_at" : "2017-03-27T17:55:40.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/users/USn41KywSS1sZapjwjDAvWax"
        },
        "applications" : {
          "href" : "https://api-staging.finix.io/applications"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);


```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
$webhook = $webhook->save();

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
  "id" : "WHfxre4aRNXZssiC8W43QQBS",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "created_at" : "2017-03-27T17:55:42.97Z",
  "updated_at" : "2017-03-27T17:55:42.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHfxre4aRNXZssiC8W43QQBS"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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



curl https://api-staging.finix.io/webhooks/WHfxre4aRNXZssiC8W43QQBS \
    -H "Content-Type: application/vnd.json+api" \
    -u UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2


```
```java

import io.crossriver.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("WHfxre4aRNXZssiC8W43QQBS");

```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhook = Webhook::retrieve('WHfxre4aRNXZssiC8W43QQBS');



```
```python


from crossriver.resources import Webhook
webhook = Webhook.get(id="WHfxre4aRNXZssiC8W43QQBS")

```
> Example Response:

```json
{
  "id" : "WHfxre4aRNXZssiC8W43QQBS",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
  "created_at" : "2017-03-27T17:55:42.97Z",
  "updated_at" : "2017-03-27T17:55:42.97Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/webhooks/WHfxre4aRNXZssiC8W43QQBS"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
    -u  UScmCeWVYZdFSFzAThVurdq2:e72014c4-bbd8-4418-9973-399cbeaf4dc2

```
```java
import io.crossriver.payments.processing.client.model.Webhook;

client.webhookClient().<Resources<Webhook>>resourcesIterator()
  .forEachRemaining(webhookPage -> {
    Collection<Webhook> webhooks = webhookPage.getContent();
    //do something with `webhooks`
  });
```
```php
<?php
use CrossRiver\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


```
```python


from crossriver.resources import Webhook
webhooks = Webhook.get()

```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHfxre4aRNXZssiC8W43QQBS",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "APdotQeZPi5LhR2cLvVJ4TfN",
      "created_at" : "2017-03-27T17:55:42.97Z",
      "updated_at" : "2017-03-27T17:55:42.97Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/webhooks/WHfxre4aRNXZssiC8W43QQBS"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APdotQeZPi5LhR2cLvVJ4TfN"
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
```java
```
```php
<?php
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
