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

3. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.


## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1

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
  client.setupUserIdAndPassword("US2wvHrSzBTFs7wNcQkGceB5", "572ccbe7-e255-4e98-9ab1-a060ef1c83c1");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CRB/Settings.php');

CRB\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'US2wvHrSzBTFs7wNcQkGceB5',
	"password" => '572ccbe7-e255-4e98-9ab1-a060ef1c83c1']
	);

require(__DIR__ . '/src/CRB/Bootstrap.php');
CRB\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crossriver.config import configure
configure(root_url="https://api-staging.finix.io", auth=("US2wvHrSzBTFs7wNcQkGceB5", "572ccbe7-e255-4e98-9ab1-a060ef1c83c1"))

```
To communicate with the CRB API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `US2wvHrSzBTFs7wNcQkGceB5`

- Password: `572ccbe7-e255-4e98-9ab1-a060ef1c83c1`

- Application ID: `AP2zYUCqfabUSSHKBX3BCcbL`

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
    -u US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Sean", 
	        "last_name": "Serna", 
	        "email": "Sean@gmail.com", 
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
use CRB\Resources\Identity;

$identity = new Identity(IDwan49kxDFsi2NUYJzxgcyM);
$identity = $identity->save();



```
```python



```
> Example Response:

```json
{
  "id" : "IDwan49kxDFsi2NUYJzxgcyM",
  "entity" : {
    "title" : null,
    "first_name" : "Sean",
    "last_name" : "Serna",
    "email" : "Sean@gmail.com",
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
  "created_at" : "2017-03-23T20:09:32.14Z",
  "updated_at" : "2017-03-23T20:09:32.14Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APk2bCVX1BPQDbX3YYrzb57U"
    }
  }
}
```

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

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
    -u US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "name": "Laura Jones", 
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
	    "identity": "IDwan49kxDFsi2NUYJzxgcyM"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("IDpuGPQr1V4sVJL6FvofVKtd")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CRB\Resources\PaymentCard;
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDwan49kxDFsi2NUYJzxgcyM');
$card = new PaymentCard(
	array(
	    "name"=> "Laura Jones", 
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
	    "identity"=> "IDwan49kxDFsi2NUYJzxgcyM"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PIn54LgMRTkHfA2X2rsrmYzc",
  "fingerprint" : "FPR738669030",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Laura Jones",
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
  "created_at" : "2017-03-23T20:09:32.51Z",
  "updated_at" : "2017-03-23T20:09:32.51Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwan49kxDFsi2NUYJzxgcyM",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APk2bCVX1BPQDbX3YYrzb57U"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc/updates"
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

### Step 3: Provision Recipient Account
```shell
curl https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
Identity identity = client.identitiesClient().fetchResource("IDwan49kxDFsi2NUYJzxgcyM");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use CRB\Resources\Identity;
use CRB\Resources\Merchant;

$identity = Identity::retrieve('IDwan49kxDFsi2NUYJzxgcyM');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MU34vS6hJs7YKFLKMhAuAnbG",
  "identity" : "IDwan49kxDFsi2NUYJzxgcyM",
  "verification" : "VIjQm6jBJsyZhZ3Kns966pMZ",
  "merchant_profile" : "MPwePbrBNuRSwvYyuqUka6G1",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-03-23T20:09:32.88Z",
  "updated_at" : "2017-03-23T20:09:32.88Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MU34vS6hJs7YKFLKMhAuAnbG"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MU34vS6hJs7YKFLKMhAuAnbG/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPwePbrBNuRSwvYyuqUka6G1"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APk2bCVX1BPQDbX3YYrzb57U"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VIjQm6jBJsyZhZ3Kns966pMZ"
    }
  }
}
```

Now that we've associated a Payment Instrument with our recipient's `Identity` we're ready to provision a Recipient account. This is the last step before you can begin paying out an Identity. Luckily you've already done most of the heavy lifting. Just make one final POST request, and you'll be returned a `Merchant` resource.

#### HTTP Request

`POST https://api-staging.finix.io/identities/identityID/merchants`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
processor| *string*, **optional** | Name of Processor


### Step 4: Send Payout




```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIn54LgMRTkHfA2X2rsrmYzc", 
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
use CRB\Resources\Transfer;

$transfer = new Transfer(
	array(
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PIn54LgMRTkHfA2X2rsrmYzc", 
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
  "id" : "TRfiiWFJ7FHGtNL7rphvoZVv",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190730",
  "currency" : "USD",
  "application" : "APk2bCVX1BPQDbX3YYrzb57U",
  "source" : "PIqqUMaW1QGQ5WJAs7BjCwwA",
  "destination" : "PIn54LgMRTkHfA2X2rsrmYzc",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-23T20:09:33.96Z",
  "updated_at" : "2017-03-23T20:09:35.08Z",
  "merchant_identity" : "IDwan49kxDFsi2NUYJzxgcyM",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APk2bCVX1BPQDbX3YYrzb57U"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIqqUMaW1QGQ5WJAs7BjCwwA"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc"
    }
  }
}
```


Now the final step - time to payout the recipient!

Next you'll need to create a `Transfer`.  What's a `Transfer`? Glad you asked! A `Transfer` represents any flow of funds either to or from a Payment Instrument. In this case a Payout to a card.

To create a `Transfer` we'll simply supply the Payment Instrument ID of the previously tokenized card as the destination field. Also, be sure to note that the amount field is in cents.

Simple enough, right? You'll also want to store the ID from that `Transfer` for your records. `Transfers` can have two possible states SUCCEEDED and FAILED.


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
          applicationId: 'AP2zYUCqfabUSSHKBX3BCcbL',
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
  "id" : "TKib7F3aXEv2R84MBjZCPBac",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-23T20:09:25.33Z",
  "updated_at" : "2017-03-23T20:09:25.33Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-24T20:09:25.33Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKib7F3aXEv2R84MBjZCPBac")
    .identity("IDpuGPQr1V4sVJL6FvofVKtd")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKib7F3aXEv2R84MBjZCPBac", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDpuGPQr1V4sVJL6FvofVKtd"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIib7F3aXEv2R84MBjZCPBac",
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
  "created_at" : "2017-03-23T20:09:25.69Z",
  "updated_at" : "2017-03-23T20:09:25.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/updates"
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

To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js ensures sensitive card data never touches your servers and keeps you out of PCI scope by sending this info over SSL directly to CRB.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/2hxnjL0q/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the CRB API.
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
    applicationId: "AP2zYUCqfabUSSHKBX3BCcbL",
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
server | *string*, **required** |  The base url for the CRB API
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
  "id" : "TKib7F3aXEv2R84MBjZCPBac",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-03-23T20:09:25.33Z",
  "updated_at" : "2017-03-23T20:09:25.33Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-03-24T20:09:25.33Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}'

```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("TKib7F3aXEv2R84MBjZCPBac")
    .identity("IDpuGPQr1V4sVJL6FvofVKtd")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKib7F3aXEv2R84MBjZCPBac", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDpuGPQr1V4sVJL6FvofVKtd"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIib7F3aXEv2R84MBjZCPBac",
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
  "created_at" : "2017-03-23T20:09:25.69Z",
  "updated_at" : "2017-03-23T20:09:25.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/updates"
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

# Applications

An `Application` resource represents a web application (e.g. marketplace, ISV,
SaaS platform). In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Fetch an Application
```shell
curl https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL \
    -H "Content-Type: application/vnd.json+api" \
    -u  US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8

```
```java

```
```php
<?php
use CRB\Resources\Application;

$application = Application::retrieve('AP2zYUCqfabUSSHKBX3BCcbL');

```
```python


from crossriver.resources import Application

application = Application.get(id="AP2zYUCqfabUSSHKBX3BCcbL")
```
> Example Response:

```json
{
  "id" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDs9dfDoD82W3B5m78QJn1Tj",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "created_at" : "2017-03-23T20:09:09.39Z",
  "updated_at" : "2017-03-23T20:09:11.82Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/application_profile"
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
	        "application_name": "Paypal"
	    }, 
	    "user": "USuG1xL5MP6JNj3YFJmfYoQf", 
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
	    "user"=> "USuG1xL5MP6JNj3YFJmfYoQf", 
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
	    "user": "USuG1xL5MP6JNj3YFJmfYoQf", 
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
  "id" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDs9dfDoD82W3B5m78QJn1Tj",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-23T20:09:09.40Z",
  "updated_at" : "2017-03-23T20:09:09.40Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/application_profile"
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
curl https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/ \
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
  "id" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDs9dfDoD82W3B5m78QJn1Tj",
  "processing_enabled" : false,
  "settlement_enabled" : true,
  "created_at" : "2017-03-23T20:09:09.39Z",
  "updated_at" : "2017-03-23T20:09:41.43Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/application_profile"
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
curl https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/ \
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
  "id" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "enabled" : true,
  "tags" : {
    "application_name" : "Paypal"
  },
  "owner" : "IDs9dfDoD82W3B5m78QJn1Tj",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "created_at" : "2017-03-23T20:09:09.39Z",
  "updated_at" : "2017-03-23T20:09:41.80Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "processors" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors"
    },
    "users" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users"
    },
    "owner_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/transfers"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/disputes"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/authorizations"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/settlements"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/merchants"
    },
    "identities" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/identities"
    },
    "webhooks" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/webhooks"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/reversals"
    },
    "tokens" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/tokens"
    },
    "application_profile" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/application_profile"
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
curl https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
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
  "id" : "USkVS1UR99PLWeNJBBcd6pxv",
  "password" : "d5e419da-eecb-4cec-8f5e-e95f18df17da",
  "identity" : "IDs9dfDoD82W3B5m78QJn1Tj",
  "enabled" : true,
  "role" : "ROLE_PARTNER",
  "tags" : { },
  "created_at" : "2017-03-23T20:09:10.71Z",
  "updated_at" : "2017-03-23T20:09:10.71Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/users/USkVS1UR99PLWeNJBBcd6pxv"
    },
    "applications" : {
      "href" : "https://api-staging.finix.io/applications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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
curl https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors \
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
  "id" : "PR6ZfbnEEDXofdzHWJbfn9cK",
  "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "default_merchant_profile" : "MP5Rf5tF5WvtRV8DCiokZzs9",
  "created_at" : "2017-03-23T20:09:10.12Z",
  "updated_at" : "2017-03-23T20:09:10.12Z",
  "processor" : "DUMMY_V1",
  "config" : {
    "canDebitBankAccount" : true,
    "key2" : "value-2",
    "key1" : "value-1"
  },
  "enabled" : true,
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors/PR6ZfbnEEDXofdzHWJbfn9cK"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1

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
      "id" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "enabled" : true,
      "tags" : {
        "application_name" : "Paypal"
      },
      "owner" : "IDs9dfDoD82W3B5m78QJn1Tj",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "created_at" : "2017-03-23T20:09:09.39Z",
      "updated_at" : "2017-03-23T20:09:11.82Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "processors" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/processors"
        },
        "users" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/users"
        },
        "owner_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/transfers"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/disputes"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/authorizations"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/settlements"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/merchants"
        },
        "identities" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/identities"
        },
        "webhooks" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/webhooks"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/reversals"
        },
        "tokens" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/tokens"
        },
        "application_profile" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL/application_profile"
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

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.

This field is optionally used to collect KYC information for the recipient.
## Create an Identity for a Recipient


```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Amy", 
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
use CRB\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Amy", 
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
	        "first_name": "Amy", 
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
	}).save()
```
> Example Response:

```json
{
  "id" : "ID3VddmXEwkRwiZWWrKAEz3n",
  "entity" : {
    "title" : null,
    "first_name" : "Amy",
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
    "ownership_type" : null,
    "tax_id_provided" : false,
    "business_tax_id_provided" : false,
    "default_statement_descriptor" : null
  },
  "tags" : {
    "key" : "value"
  },
  "created_at" : "2017-03-23T20:09:18.19Z",
  "updated_at" : "2017-03-23T20:09:18.19Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    }
  }
}
```

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

## Retrieve a Identity
```shell

curl https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1

```
```java

import io.crossriver.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("IDpuGPQr1V4sVJL6FvofVKtd");

```
```php
<?php
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDpuGPQr1V4sVJL6FvofVKtd');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="IDpuGPQr1V4sVJL6FvofVKtd")

```
> Example Response:

```json
{
  "id" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Pollos Hermanos",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 27,
      "month" : 6,
      "year" : 1978
    },
    "max_transaction_amount" : 12000000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Pollos Hermanos"
  },
  "tags" : {
    "Studio Rating" : "4.7"
  },
  "created_at" : "2017-03-23T20:09:12.54Z",
  "updated_at" : "2017-03-23T20:09:12.54Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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
curl https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "White", 
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
  "id" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "White",
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
    "mcc" : "0742",
    "dob" : {
      "day" : 2,
      "month" : 5,
      "year" : 1988
    },
    "max_transaction_amount" : 1200000,
    "amex_mid" : null,
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
    "ownership_type" : "PRIVATE",
    "tax_id_provided" : true,
    "business_tax_id_provided" : true,
    "default_statement_descriptor" : "Petes Coffee"
  },
  "tags" : {
    "key" : "value_2"
  },
  "created_at" : "2017-03-23T20:09:12.54Z",
  "updated_at" : "2017-03-23T20:09:39.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1


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
      "id" : "ID3VddmXEwkRwiZWWrKAEz3n",
      "entity" : {
        "title" : null,
        "first_name" : "Amy",
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
        "ownership_type" : null,
        "tax_id_provided" : false,
        "business_tax_id_provided" : false,
        "default_statement_descriptor" : null
      },
      "tags" : {
        "key" : "value"
      },
      "created_at" : "2017-03-23T20:09:18.17Z",
      "updated_at" : "2017-03-23T20:09:18.17Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDrGxhMtxzQnFiJxeF9sh2ip",
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
      "created_at" : "2017-03-23T20:09:16.23Z",
      "updated_at" : "2017-03-23T20:09:16.23Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrGxhMtxzQnFiJxeF9sh2ip/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDoAHbCT8hLtCeg6uyUUPj3m",
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
      "created_at" : "2017-03-23T20:09:15.75Z",
      "updated_at" : "2017-03-23T20:09:15.75Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDoAHbCT8hLtCeg6uyUUPj3m/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDZNKLBNB8qRPcUQ7uMvvHi",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pawny City Hall"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-23T20:09:15.34Z",
      "updated_at" : "2017-03-23T20:09:15.34Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDZNKLBNB8qRPcUQ7uMvvHi/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDbD8ucMhsPJcSQgop5npWPy",
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
      "created_at" : "2017-03-23T20:09:14.97Z",
      "updated_at" : "2017-03-23T20:09:14.97Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDbD8ucMhsPJcSQgop5npWPy/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDapPFJFy13sscDcc9dF4JU8",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "GENERAL_PARTNERSHIP",
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
      "created_at" : "2017-03-23T20:09:14.44Z",
      "updated_at" : "2017-03-23T20:09:14.44Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDapPFJFy13sscDcc9dF4JU8/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDrkSUWXLgc16JQAs4WVs6tG",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pawny City Hall",
        "business_type" : "LIMITED_PARTNERSHIP",
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
      "created_at" : "2017-03-23T20:09:14.05Z",
      "updated_at" : "2017-03-23T20:09:14.05Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDrkSUWXLgc16JQAs4WVs6tG/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "ID5dpFTj5yLnoygAEq6W6xXT",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "PARTNERSHIP",
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
      "created_at" : "2017-03-23T20:09:13.68Z",
      "updated_at" : "2017-03-23T20:09:13.68Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID5dpFTj5yLnoygAEq6W6xXT/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDhEQZhP1pMybJPCzyW1cR2R",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-23T20:09:13.30Z",
      "updated_at" : "2017-03-23T20:09:13.30Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDhEQZhP1pMybJPCzyW1cR2R/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "ID3yqSK5ykovLqaUWZUcvpQ",
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
      "created_at" : "2017-03-23T20:09:12.94Z",
      "updated_at" : "2017-03-23T20:09:12.94Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID3yqSK5ykovLqaUWZUcvpQ/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Pollos Hermanos",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
        "mcc" : "0742",
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "max_transaction_amount" : 12000000,
        "amex_mid" : null,
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
        "ownership_type" : "PRIVATE",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Pollos Hermanos"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-03-23T20:09:12.54Z",
      "updated_at" : "2017-03-23T20:09:12.54Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        }
      }
    }, {
      "id" : "IDs9dfDoD82W3B5m78QJn1Tj",
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
      "created_at" : "2017-03-23T20:09:09.39Z",
      "updated_at" : "2017-03-23T20:09:09.40Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/IDs9dfDoD82W3B5m78QJn1Tj/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
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

A `Payment Instrument` resource represents either a credit card.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Associate a Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}'


```
```java
import io.crossriver.payments.processing.client.model.PaymentCard;
import io.crossriver.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("TKib7F3aXEv2R84MBjZCPBac")
    .identity("IDpuGPQr1V4sVJL6FvofVKtd")
    .build()
);

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKib7F3aXEv2R84MBjZCPBac", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDpuGPQr1V4sVJL6FvofVKtd"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKib7F3aXEv2R84MBjZCPBac", 
	    "type": "TOKEN", 
	    "identity": "IDpuGPQr1V4sVJL6FvofVKtd"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIib7F3aXEv2R84MBjZCPBac",
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
  "created_at" : "2017-03-23T20:09:25.69Z",
  "updated_at" : "2017-03-23T20:09:25.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIib7F3aXEv2R84MBjZCPBac/updates"
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
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "name": "Bob Green", 
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
	    "identity": "ID3VddmXEwkRwiZWWrKAEz3n"
	}'


```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("IDpuGPQr1V4sVJL6FvofVKtd")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);

```
```php
<?php
use CRB\Resources\PaymentCard;
use CRB\Resources\Identity;

$identity = Identity::retrieve('IDpuGPQr1V4sVJL6FvofVKtd');
$card = new PaymentCard(
	array(
	    "name"=> "Bob Green", 
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
	    "identity"=> "ID3VddmXEwkRwiZWWrKAEz3n"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Green", 
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
	    "identity": "ID3VddmXEwkRwiZWWrKAEz3n"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIusm3xzZGofMxf5beGpBSrD",
  "fingerprint" : "FPR432782986",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Green",
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
  "created_at" : "2017-03-23T20:09:18.55Z",
  "updated_at" : "2017-03-23T20:09:18.55Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3VddmXEwkRwiZWWrKAEz3n",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/updates"
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
curl https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \

```
```java

import io.crossriver.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIusm3xzZGofMxf5beGpBSrD")

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIusm3xzZGofMxf5beGpBSrD');

```
```python



```
> Example Response:

```json
{
  "id" : "PIusm3xzZGofMxf5beGpBSrD",
  "fingerprint" : "FPR432782986",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Green",
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
  "created_at" : "2017-03-23T20:09:18.52Z",
  "updated_at" : "2017-03-23T20:09:23.41Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID3VddmXEwkRwiZWWrKAEz3n",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID3VddmXEwkRwiZWWrKAEz3n"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD/updates"
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

# Transfer

A `Transfer` represents any payout to a card

Payouts can have two possible states values: SUCCEEDED or FAILED.

- **SUCCEEDED:**  Funds have been disbursed.
        
- **FAILED:** Attempt to disburse has failed



## Payout to a Card

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1 \
    -d '
	{
	    "fee": 26826, 
	    "source": "PIsevrSV9YApKESzYAF3WtnZ", 
	    "merchant_identity": "IDpuGPQr1V4sVJL6FvofVKtd", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 268261
	}'


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDpuGPQr1V4sVJL6FvofVKtd")
      .source("PIusm3xzZGofMxf5beGpBSrD")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);

```
```php
<?php
use CRB\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 45672, 
	    "source"=> "PIusm3xzZGofMxf5beGpBSrD", 
	    "merchant_identity"=> "IDpuGPQr1V4sVJL6FvofVKtd", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 456719
	));
$debit = $debit->save();
```
```python



```
> Example Response:

```json
{
  "id" : "TRfiiWFJ7FHGtNL7rphvoZVv",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190730",
  "currency" : "USD",
  "application" : "APk2bCVX1BPQDbX3YYrzb57U",
  "source" : "PIqqUMaW1QGQ5WJAs7BjCwwA",
  "destination" : "PIn54LgMRTkHfA2X2rsrmYzc",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-23T20:09:33.96Z",
  "updated_at" : "2017-03-23T20:09:35.08Z",
  "merchant_identity" : "IDwan49kxDFsi2NUYJzxgcyM",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APk2bCVX1BPQDbX3YYrzb57U"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDwan49kxDFsi2NUYJzxgcyM"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRfiiWFJ7FHGtNL7rphvoZVv/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIqqUMaW1QGQ5WJAs7BjCwwA"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIn54LgMRTkHfA2X2rsrmYzc"
    }
  }
}
```

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


## Retrieve a Payout
```shell

curl https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1


```
```java

import io.crossriver.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRv8wdT89Q8mPRSc5cwnZn9X");

```
```php
<?php
use CRB\Resources\Transfer;

$transfer = Transfer::retrieve('TRv8wdT89Q8mPRSc5cwnZn9X');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRv8wdT89Q8mPRSc5cwnZn9X")

```
> Example Response:

```json
{
  "id" : "TRv8wdT89Q8mPRSc5cwnZn9X",
  "amount" : 456719,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "424d5354-0791-4f56-9181-b5568da4d29c",
  "currency" : "USD",
  "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
  "source" : "PIusm3xzZGofMxf5beGpBSrD",
  "destination" : "PI6pBnXyS5xYQTGTMNwpQbCs",
  "ready_to_settle_at" : null,
  "fee" : 45672,
  "statement_descriptor" : "FIN*POLLOS HERMANOS",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-03-23T20:09:19.34Z",
  "updated_at" : "2017-03-23T20:09:19.46Z",
  "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PI6pBnXyS5xYQTGTMNwpQbCs"
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

## List all Payouts
```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  US2wvHrSzBTFs7wNcQkGceB5:572ccbe7-e255-4e98-9ab1-a060ef1c83c1

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
      "id" : "TRcGfU3twfEKmtKAtKuVncW5",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "729f34c5-0ac8-44d3-b3b3-60d1e4d51f08",
      "currency" : "USD",
      "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "source" : "PIusm3xzZGofMxf5beGpBSrD",
      "destination" : "PI6pBnXyS5xYQTGTMNwpQbCs",
      "ready_to_settle_at" : null,
      "fee" : 10,
      "statement_descriptor" : "FIN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-23T20:09:24.20Z",
      "updated_at" : "2017-03-23T20:09:24.30Z",
      "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGfU3twfEKmtKAtKuVncW5"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGfU3twfEKmtKAtKuVncW5/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGfU3twfEKmtKAtKuVncW5/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGfU3twfEKmtKAtKuVncW5/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRcGfU3twfEKmtKAtKuVncW5/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6pBnXyS5xYQTGTMNwpQbCs"
        }
      }
    }, {
      "id" : "TRpgmxGfQ2SYcesHwqFffypZ",
      "amount" : 1734,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "56edc17e-ff8a-4c13-ace0-b72a859f722a",
      "currency" : "USD",
      "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "source" : "PI6pBnXyS5xYQTGTMNwpQbCs",
      "destination" : "PIusm3xzZGofMxf5beGpBSrD",
      "ready_to_settle_at" : null,
      "fee" : 173,
      "statement_descriptor" : "FIN*POLLOS HERMANOS",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-23T20:09:22.56Z",
      "updated_at" : "2017-03-23T20:09:22.72Z",
      "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRpgmxGfQ2SYcesHwqFffypZ"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRpgmxGfQ2SYcesHwqFffypZ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "parent" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
        }
      }
    }, {
      "id" : "TR6ZCR7V8BNYHEApNrGaiids",
      "amount" : 1734,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "6ea4d622-29aa-478e-a26e-344395ead43d",
      "currency" : "USD",
      "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "source" : "PIusm3xzZGofMxf5beGpBSrD",
      "destination" : "PI6pBnXyS5xYQTGTMNwpQbCs",
      "ready_to_settle_at" : null,
      "fee" : 173,
      "statement_descriptor" : "FIN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-23T20:09:22.04Z",
      "updated_at" : "2017-03-23T20:09:22.63Z",
      "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR6ZCR7V8BNYHEApNrGaiids/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6pBnXyS5xYQTGTMNwpQbCs"
        }
      }
    }, {
      "id" : "TR6y22dxR3HBqLo2zbrNd2N",
      "amount" : 268261,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "630c7164-c365-437a-9e2a-0566b18be377",
      "currency" : "USD",
      "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "source" : "PIsevrSV9YApKESzYAF3WtnZ",
      "destination" : "PI6pBnXyS5xYQTGTMNwpQbCs",
      "ready_to_settle_at" : null,
      "fee" : 26826,
      "statement_descriptor" : "FIN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-23T20:09:19.94Z",
      "updated_at" : "2017-03-23T20:09:20.05Z",
      "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TR6y22dxR3HBqLo2zbrNd2N"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TR6y22dxR3HBqLo2zbrNd2N/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TR6y22dxR3HBqLo2zbrNd2N/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TR6y22dxR3HBqLo2zbrNd2N/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TR6y22dxR3HBqLo2zbrNd2N/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIsevrSV9YApKESzYAF3WtnZ"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6pBnXyS5xYQTGTMNwpQbCs"
        }
      }
    }, {
      "id" : "TRv8wdT89Q8mPRSc5cwnZn9X",
      "amount" : 456719,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "424d5354-0791-4f56-9181-b5568da4d29c",
      "currency" : "USD",
      "application" : "AP2zYUCqfabUSSHKBX3BCcbL",
      "source" : "PIusm3xzZGofMxf5beGpBSrD",
      "destination" : "PI6pBnXyS5xYQTGTMNwpQbCs",
      "ready_to_settle_at" : null,
      "fee" : 45672,
      "statement_descriptor" : "FIN*POLLOS HERMANOS",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-03-23T20:09:19.34Z",
      "updated_at" : "2017-03-23T20:09:19.46Z",
      "merchant_identity" : "IDpuGPQr1V4sVJL6FvofVKtd",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/AP2zYUCqfabUSSHKBX3BCcbL"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/IDpuGPQr1V4sVJL6FvofVKtd"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRv8wdT89Q8mPRSc5cwnZn9X/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIusm3xzZGofMxf5beGpBSrD"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PI6pBnXyS5xYQTGTMNwpQbCs"
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
