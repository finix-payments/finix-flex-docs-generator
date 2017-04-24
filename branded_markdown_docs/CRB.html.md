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

curl https://api-staging.finix.io/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8

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

import io.crb.payments.processing.client.ProcessingClient;
import io.crb.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("https://api-staging.finix.io");
  client.setupUserIdAndPassword("UShEGgXixGZuuhnESgF69Prc", "4924749b-4b9f-4a74-af70-396cb2018bc8");

//...

```
```php
<?php
// Download the PHP Client here: https://github.com/finix-payments/processing-php-client

require_once('vendor/autoload.php');
require(__DIR__ . '/src/CRB/Settings.php');

CRB\Settings::configure([
	"root_url" => 'https://api-staging.finix.io',
	"username" => 'UShEGgXixGZuuhnESgF69Prc',
	"password" => '4924749b-4b9f-4a74-af70-396cb2018bc8']
	);

require(__DIR__ . '/src/CRB/Bootstrap.php');
CRB\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install crossriver

import crossriver

from crb.config import configure
configure(root_url="https://api-staging.finix.io", auth=("UShEGgXixGZuuhnESgF69Prc", "4924749b-4b9f-4a74-af70-396cb2018bc8"))

```
To communicate with the CRB API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `UShEGgXixGZuuhnESgF69Prc`

- Password: `4924749b-4b9f-4a74-af70-396cb2018bc8`

- Application ID: `APbVjnZrqJiP9FhG1fEdnGYK`

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
    -u UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Walter", 
	        "last_name": "Le", 
	        "email": "Walter@gmail.com", 
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

import io.crb.payments.processing.client.model.Address;
import io.crb.payments.processing.client.model.BankAccountType;
import io.crb.payments.processing.client.model.BusinessType;
import io.crb.payments.processing.client.model.Date;
import io.crb.payments.processing.client.model.Entity;
import io.crb.payments.processing.client.model.Identity;;

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

$identity = new Identity(ID7ke4ccaeYEsCmoueTSV6WC);
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
	        "first_name": "Walter", 
	        "last_name": "Le", 
	        "email": "Walter@gmail.com", 
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
  "id" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "entity" : {
    "title" : null,
    "first_name" : "Walter",
    "last_name" : "Le",
    "email" : "Walter@gmail.com",
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
  "created_at" : "2017-04-17T23:48:17.75Z",
  "updated_at" : "2017-04-17T23:48:17.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 2:  Add a Payment Instrument for the Recipient 

```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "name": "Bob Chang", 
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
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}'


```
```java
import io.crb.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe Doe")
    .identity("ID7ke4ccaeYEsCmoueTSV6WC")
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

$identity = Identity::retrieve('ID7ke4ccaeYEsCmoueTSV6WC');
$card = new PaymentCard(
	array(
	    "name"=> "Bob Chang", 
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
	    "identity"=> "ID7ke4ccaeYEsCmoueTSV6WC"
	));
$card = $identity->createPaymentCard($card);

```
```python



```
> Example Response:

```json
{
  "id" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "fingerprint" : "FPR-1624323282",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Chang",
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
  "created_at" : "2017-04-17T23:48:18.14Z",
  "updated_at" : "2017-04-17T23:48:18.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/updates"
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
line1 | *string*, **required** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **required** | 2-letter State code
postal_code | *string*, **required** | Zip or Postal code (max 7 characters)
country | *string*, **required** | 3-Letter Country code

### Step 3: Provision Recipient Account
```shell
curl https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "processor": "VISA_V1", 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
Identity identity = client.identitiesClient().fetchResource("ID7ke4ccaeYEsCmoueTSV6WC");
identity.provisionMerchantOn(Merchant.builder().build());
```
```php
<?php
use CRB\Resources\Identity;
use CRB\Resources\Merchant;

$identity = Identity::retrieve('ID7ke4ccaeYEsCmoueTSV6WC');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python



```
> Example Response:

```json
{
  "id" : "MUeNgHqRUNGmPyUCMGnHkXHW",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "verification" : "VI6x3oxpbeXFvtKhYzG2bd8k",
  "merchant_profile" : "MPxkxEPeDY2Zwtz19ZC7SEPt",
  "processor" : "VISA_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-04-17T23:48:18.62Z",
  "updated_at" : "2017-04-17T23:48:18.62Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/merchants/MUeNgHqRUNGmPyUCMGnHkXHW"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/merchants/MUeNgHqRUNGmPyUCMGnHkXHW/verifications"
    },
    "merchant_profile" : {
      "href" : "https://api-staging.finix.io/merchant_profiles/MPxkxEPeDY2Zwtz19ZC7SEPt"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "verification" : {
      "href" : "https://api-staging.finix.io/verifications/VI6x3oxpbeXFvtKhYzG2bd8k"
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
    -u UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIvHJJwiPQcreT4koHD8jTDJ", 
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
	    "destination"=> "PIvHJJwiPQcreT4koHD8jTDJ", 
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
  "id" : "TRtcHptHMfgR4dh8mWAugsw2",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190853",
  "currency" : "USD",
  "application" : "APbVjnZrqJiP9FhG1fEdnGYK",
  "source" : "PIkQYy8Zsh6RkYqUmm8hjDnL",
  "destination" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:19.74Z",
  "updated_at" : "2017-04-17T23:48:22.24Z",
  "merchant_identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkQYy8Zsh6RkYqUmm8hjDnL"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
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
          applicationId: 'APbVjnZrqJiP9FhG1fEdnGYK',
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
  "id" : "TKx7ehuUBht5jokV7j1S2goY",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:48:25.56Z",
  "updated_at" : "2017-04-17T23:48:25.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:48:25.56Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}'


```
```java
import io.crb.payments.processing.client.model.PaymentCard;
import io.crb.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKx7ehuUBht5jokV7j1S2goY")
            .identity("ID7ke4ccaeYEsCmoueTSV6WC")
    .build()
);
```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKx7ehuUBht5jokV7j1S2goY", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID7ke4ccaeYEsCmoueTSV6WC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIx7ehuUBht5jokV7j1S2goY",
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
  "created_at" : "2017-04-17T23:48:25.98Z",
  "updated_at" : "2017-04-17T23:48:25.98Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/updates"
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
    secureForm.submit('/applications/APbVjnZrqJiP9FhG1fEdnGYK/tokens', {
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
  "id" : "TKx7ehuUBht5jokV7j1S2goY",
  "fingerprint" : "FPR-1132692079",
  "created_at" : "2017-04-17T23:48:25.56Z",
  "updated_at" : "2017-04-17T23:48:25.56Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-04-18T23:48:25.56Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}'

```
```java
import io.crb.payments.processing.client.model.PaymentCard;
import io.crb.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKx7ehuUBht5jokV7j1S2goY")
            .identity("ID7ke4ccaeYEsCmoueTSV6WC")
    .build()
);
```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKx7ehuUBht5jokV7j1S2goY", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID7ke4ccaeYEsCmoueTSV6WC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}).save()

```
> Example Response:

```json
{
  "id" : "PIx7ehuUBht5jokV7j1S2goY",
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
  "created_at" : "2017-04-17T23:48:25.98Z",
  "updated_at" : "2017-04-17T23:48:25.98Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/updates"
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


# Identities

An `Identity` resource represents either a person or business and is in many ways the centerpiece of the payment API's 
architecture. Transfers and Payment `Instruments` must be associated with an `Identity`. This structure makes it easy 
to manage and reconcile their associated payment history, transaction history, and payouts.

This field is optionally used to collect KYC information for the recipient.
## Create an Identity for a Recipient


```shell
curl https://api-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Walter", 
	        "last_name": "Le", 
	        "email": "Walter@gmail.com", 
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

import io.crb.payments.processing.client.model.Identity;

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
	        "phone"=> "7145677612", 
	        "first_name"=> "Walter", 
	        "last_name"=> "Le", 
	        "email"=> "Walter@gmail.com", 
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
	        "first_name": "Walter", 
	        "last_name": "Le", 
	        "email": "Walter@gmail.com", 
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
  "id" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "entity" : {
    "title" : null,
    "first_name" : "Walter",
    "last_name" : "Le",
    "email" : "Walter@gmail.com",
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
  "created_at" : "2017-04-17T23:48:17.75Z",
  "updated_at" : "2017-04-17T23:48:17.75Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
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

curl https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8

```
```java

import io.crb.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("ID7ke4ccaeYEsCmoueTSV6WC");

```
```php
<?php
use CRB\Resources\Identity;

$identity = Identity::retrieve('ID7ke4ccaeYEsCmoueTSV6WC');
```
```python


from crossriver.resources import Identity
identity = Identity.get(id="ID7ke4ccaeYEsCmoueTSV6WC")

```
> Example Response:

```json
{
  "id" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "entity" : {
    "title" : null,
    "first_name" : "Jim",
    "last_name" : "Wade",
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
  "created_at" : "2017-04-17T23:48:17.74Z",
  "updated_at" : "2017-04-17T23:48:22.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
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
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8


```
```java
import io.crb.payments.processing.client.model.Identity;

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
      "id" : "ID7ke4ccaeYEsCmoueTSV6WC",
      "entity" : {
        "title" : null,
        "first_name" : "Jim",
        "last_name" : "Wade",
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
      "created_at" : "2017-04-17T23:48:17.74Z",
      "updated_at" : "2017-04-17T23:48:22.78Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
        }
      }
    }, {
      "id" : "ID2EnmpibyFciQjwsVpcedZN",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "BrainTree",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
        "doing_business_as" : "BrainTree",
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
        "application_name" : "BrainTree"
      },
      "created_at" : "2017-04-17T23:48:16.15Z",
      "updated_at" : "2017-04-17T23:48:16.16Z",
      "_links" : {
        "self" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN"
        },
        "verifications" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/verifications"
        },
        "merchants" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/merchants"
        },
        "settlements" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/settlements"
        },
        "authorizations" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/authorizations"
        },
        "transfers" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/transfers"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/payment_instruments"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/identities/ID2EnmpibyFciQjwsVpcedZN/disputes"
        },
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
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
    "count" : 2
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/identities/`


## Update an Identity
```shell
curl https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677612", 
	        "first_name": "Jim", 
	        "last_name": "Wade", 
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

```
```php
<?php

```
```python



```
> Example Response:

```json
{
  "id" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "entity" : {
    "title" : null,
    "first_name" : "Jim",
    "last_name" : "Wade",
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
  "created_at" : "2017-04-17T23:48:17.74Z",
  "updated_at" : "2017-04-17T23:48:22.78Z",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/verifications"
    },
    "merchants" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/merchants"
    },
    "settlements" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/settlements"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/authorizations"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/transfers"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/payment_instruments"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC/disputes"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    }
  }
}
```
<aside class="notice">
tax_id and business_tax_id are not updatable. If either field was input incorrectly,
please create a new Identity resource.
</aside>



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
curl https://api-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}'


```
```java
import io.crb.payments.processing.client.model.PaymentCard;
import io.crb.payments.processing.client.model.PaymentCardToken;

PaymentCard card = client.paymentCardsClient().associateToken(
    PaymentCardToken.builder()
            .token("TKx7ehuUBht5jokV7j1S2goY")
            .identity("ID7ke4ccaeYEsCmoueTSV6WC")
    .build()
);
```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKx7ehuUBht5jokV7j1S2goY", 
	    "type"=> "TOKEN", 
	    "identity"=> "ID7ke4ccaeYEsCmoueTSV6WC"
	));
$card = $card->save();

```
```python


from crossriver.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKx7ehuUBht5jokV7j1S2goY", 
	    "type": "TOKEN", 
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIx7ehuUBht5jokV7j1S2goY",
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
  "created_at" : "2017-04-17T23:48:25.98Z",
  "updated_at" : "2017-04-17T23:48:25.98Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIx7ehuUBht5jokV7j1S2goY/updates"
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
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "name": "Bob Chang", 
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
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}'


```
```java

import io.crb.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name(Name.parse("Joe Doe"))
    .identity("ID7ke4ccaeYEsCmoueTSV6WC")
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

$identity = Identity::retrieve('ID7ke4ccaeYEsCmoueTSV6WC');
$card = new PaymentCard(
	array(
	    "name"=> "Bob Chang", 
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
	    "identity"=> "ID7ke4ccaeYEsCmoueTSV6WC"
	));
$card = $identity->createPaymentCard($card);

```
```python


from crossriver.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Bob Chang", 
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
	    "identity": "ID7ke4ccaeYEsCmoueTSV6WC"
	}).save()
```
> Example Response:

```json
{
  "id" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "fingerprint" : "FPR-1624323282",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Chang",
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
  "created_at" : "2017-04-17T23:48:18.14Z",
  "updated_at" : "2017-04-17T23:48:18.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/updates"
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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
## Fetch a Credit Card
```shell
curl https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \

```
```java

import io.crb.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIvHJJwiPQcreT4koHD8jTDJ")

```
```php
<?php
use CRB\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIvHJJwiPQcreT4koHD8jTDJ');

```
```python



```
> Example Response:

```json
{
  "id" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "fingerprint" : "FPR-1624323282",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Bob Chang",
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
  "created_at" : "2017-04-17T23:48:18.09Z",
  "updated_at" : "2017-04-17T23:48:18.09Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "self" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
    },
    "authorizations" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/authorizations"
    },
    "identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "transfers" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/transfers"
    },
    "verifications" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/verifications"
    },
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "updates" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ/updates"
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



## Create Payout

```shell
curl https://api-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8 \
    -d '
	{
	    "currency": "USD", 
	    "amount": 10000, 
	    "destination": "PIvHJJwiPQcreT4koHD8jTDJ", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'


```
```java

import io.crb.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .destination("PIvHJJwiPQcreT4koHD8jTDJ")
      .amount(8888)
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
	    "currency"=> "USD", 
	    "amount"=> 10000, 
	    "destination"=> "PIvHJJwiPQcreT4koHD8jTDJ", 
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
  "id" : "TRtcHptHMfgR4dh8mWAugsw2",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190853",
  "currency" : "USD",
  "application" : "APbVjnZrqJiP9FhG1fEdnGYK",
  "source" : "PIkQYy8Zsh6RkYqUmm8hjDnL",
  "destination" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:19.74Z",
  "updated_at" : "2017-04-17T23:48:22.24Z",
  "merchant_identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkQYy8Zsh6RkYqUmm8hjDnL"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
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

curl https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2 \
    -H "Content-Type: application/vnd.json+api" \
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8


```
```java

import io.crb.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("TRtcHptHMfgR4dh8mWAugsw2");

```
```php
<?php
use CRB\Resources\Transfer;

$transfer = Transfer::retrieve('TRtcHptHMfgR4dh8mWAugsw2');



```
```python


from crossriver.resources import Transfer
transfer = Transfer.get(id="TRtcHptHMfgR4dh8mWAugsw2")

```
> Example Response:

```json
{
  "id" : "TRtcHptHMfgR4dh8mWAugsw2",
  "amount" : 10000,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "trace_id" : "190853",
  "currency" : "USD",
  "application" : "APbVjnZrqJiP9FhG1fEdnGYK",
  "source" : "PIkQYy8Zsh6RkYqUmm8hjDnL",
  "destination" : "PIvHJJwiPQcreT4koHD8jTDJ",
  "ready_to_settle_at" : null,
  "fee" : 0,
  "statement_descriptor" : "FIN*FINIXPAYMENTS",
  "type" : "CREDIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-04-17T23:48:19.64Z",
  "updated_at" : "2017-04-17T23:48:22.24Z",
  "merchant_identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
  "_links" : {
    "application" : {
      "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
    },
    "self" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2"
    },
    "payment_instruments" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
    },
    "reversals" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/reversals"
    },
    "fees" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/fees"
    },
    "disputes" : {
      "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/disputes"
    },
    "source" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIkQYy8Zsh6RkYqUmm8hjDnL"
    },
    "destination" : {
      "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
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
    -u  UShEGgXixGZuuhnESgF69Prc:4924749b-4b9f-4a74-af70-396cb2018bc8

```
```java
import io.crb.payments.processing.client.model.Transfer;

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
      "id" : "TRtcHptHMfgR4dh8mWAugsw2",
      "amount" : 10000,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "190853",
      "currency" : "USD",
      "application" : "APbVjnZrqJiP9FhG1fEdnGYK",
      "source" : "PIkQYy8Zsh6RkYqUmm8hjDnL",
      "destination" : "PIvHJJwiPQcreT4koHD8jTDJ",
      "ready_to_settle_at" : null,
      "fee" : 0,
      "statement_descriptor" : "FIN*FINIXPAYMENTS",
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-04-17T23:48:19.64Z",
      "updated_at" : "2017-04-17T23:48:22.24Z",
      "merchant_identity" : "ID7ke4ccaeYEsCmoueTSV6WC",
      "_links" : {
        "application" : {
          "href" : "https://api-staging.finix.io/applications/APbVjnZrqJiP9FhG1fEdnGYK"
        },
        "self" : {
          "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2"
        },
        "payment_instruments" : {
          "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://api-staging.finix.io/identities/ID7ke4ccaeYEsCmoueTSV6WC"
        },
        "reversals" : {
          "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/reversals"
        },
        "fees" : {
          "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/fees"
        },
        "disputes" : {
          "href" : "https://api-staging.finix.io/transfers/TRtcHptHMfgR4dh8mWAugsw2/disputes"
        },
        "source" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIkQYy8Zsh6RkYqUmm8hjDnL"
        },
        "destination" : {
          "href" : "https://api-staging.finix.io/payment_instruments/PIvHJJwiPQcreT4koHD8jTDJ"
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
    "count" : 1
  }
}
```

#### HTTP Request

`GET https://api-staging.finix.io/transfers`
