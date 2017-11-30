---
title: Lacore API Reference

language_tabs:
- shell: cURL
- java: Java
- php: PHP
- python: Python
- ruby: Ruby



search: true
---

# Topics 

## API Endpoints

We provide two distinct base urls for making API requests depending on
whether you would like to utilize the sandbox or production environments. These
two environments are completely separate and share no information, including
API credentials. For testing please use the Staging API and when you are ready to
 process live transactions use the Production endpoint.

- **Staging API:** `https://lacore-sandbox.finixpayments.com`

- **Production API:** `https://api.live.lacore.finixpymnts.com`

## Authentication



```shell
# With CURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl https://lacore-sandbox.finixpayments.com/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.lacore.payments.processing.client</groupId>
  <artifactId>payline-data</artifactId>
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

import io.lacore.payments.ApiClient;
import io.lacore.payments.views.*;
import io.lacore.payments.forms.*;

//...

public static void main(String[] args) {

  ApiClient api = ApiClient.builder()
                  .url("https://lacore-sandbox.finixpayments.com")
                  .user("USed8KcvU1NcqCjL2gecsdE7")
                  .password("6bb7691d-eb11-4fba-a65e-c8f352dca244")
                  .build();
//...



```
```php
<?php
// Download the PHP Client here: https://github.com/Payline/payline-php

require_once('vendor/autoload.php');
require(__DIR__ . '/src/Lacore/Settings.php');

Lacore\Settings::configure([
	"root_url" => 'https://lacore-sandbox.finixpayments.com',
	"username" => 'USed8KcvU1NcqCjL2gecsdE7',
	"password" => '6bb7691d-eb11-4fba-a65e-c8f352dca244']
	);

require(__DIR__ . '/src/Lacore/Bootstrap.php');
Lacore\Bootstrap::init();

```
```python


# To install the python client run the command below from your terminal:
# pip install lacore

import lacore

from lacore.config import configure
configure(root_url="https://lacore-sandbox.finixpayments.com", auth=("USed8KcvU1NcqCjL2gecsdE7", "6bb7691d-eb11-4fba-a65e-c8f352dca244"))

```
```ruby
# To download the Ruby gem:
# gem install payline-data

require 'payline'

Lacore.configure(
    :root_url => 'https://lacore-sandbox.finixpayments.com',
    :user=>'USed8KcvU1NcqCjL2gecsdE7',
    :password => '6bb7691d-eb11-4fba-a65e-c8f352dca244'
)
```
To communicate with the Lacore API you'll need to authenticate your requests
via http basic access authentication with a `username` and `password`, which you
can locate in your dashboard. If you do not have a dashboard feel free to test
the API with the credentials below:

- Username: `USed8KcvU1NcqCjL2gecsdE7`

- Password: `6bb7691d-eb11-4fba-a65e-c8f352dca244`

- Application ID: `AP3VrWhf2cFx5QakKk5UrT3f`

Your `Application` is a resource that represents your web app. In other words,
any web service that connects buyers (i.e. customers) and sellers
(i.e. merchants).

## Idempotency Requests

You'll notice the authorization and transfer object have a field named `idempotency_id` which ensures the API request is only performed once. Why is this important? We've all experienced a hanging request while on a checkout page and feared that if we refresh or submit the payment again we'll be charged twice. With Lacore, we remove the ambiguity by having the user generate a unique `idempotency_id` and sending it with the normal payload. If the user attempts a request with the same `idempotency_id`, the response will raise an exception. Now you can rest assured that when you create an authorization or debit a bank account that the user will be protected from potential network issues by simply passing `idempotency_id` in body of the request.

## Tags

All Lacore objects (i.e. `Authorization`, `Application`, `Identity`, `Merchant`, `Payment Instrument`, `Settlement`, `Transfer`) include a tags attribute that allows the user to include key-value metadata to their object. For example, when creating a `Payment Instrument`, you may want to include more data about the card. Simply pass a custom key and value, such as "card-type": "business card". Or when creating an `Authorization`, you may want to include specific information about the transaction, such as a unique ID or additional information about the transaction.

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
 `4957030420210454` | Payment card positive result  
 `4000000000000036` | Payment card AVS total failure
 `4000000000000127` | Payment card CVC failure

## Errors

Error Code | Meaning
---------- | -------
400 | Bad Request -- You've attemped an invalid request
401 | Unauthorized -- You have used the incorrect API key
402 | Upstream Processor Error -- Errors caused by 3rd party service
404 | Not Found -- The specified resource could not be found
422 | Unprocessable Entity -- The parameters were valid but the request failed. The error is usually some misunderstanding of various steps that have to be executed in order (e.g. attempting to initiate a transfer on behalf of a merchant that has not yet been approved)
500 | Internal Server Error -- We had a problem with our server. Try again later.

# Guides

## Overview

These guides provide a collection of resources for utilizing the Lacore
API and its client libraries. We offer a number of client libraries for
interfacing with the API, and you can view example code snippets for each in
the dark area to the right.

1. [Authentication](#authentication): Learn how to properly
authenticate and interface with the API.

2. [Getting Started](#getting-started): A step-by-step guide demonstrating the basic workflow
of charging a card. This guide will walk you through provisioning merchant
accounts, tokenizing cards, charging those cards, and finally settling (i.e.
payout) those funds out to your merchants.

3. [Embedded Tokenization](#embedded-tokenization): This guide
explains how to properly tokenize cards in production via our embedded iframe.

## Getting Started
### Step 1: Create an Identity for a Merchant

```shell
curl https://lacore-sandbox.finixpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": true, 
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
	        "ownership_type": "PRIVATE", 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
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
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.enums.BusinessType;
import io.lacore.payments.forms.Address;
import io.lacore.payments.forms.Date;
import io.lacore.payments.forms.IdentityEntityForm;
import io.lacore.payments.forms.IdentityForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Identity;


IdentityForm form = IdentityForm.builder()
  .entity(IdentityEntityForm.builder()
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
  .personalAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .businessAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .dob(Date.builder().day(Integer.valueOf(27)).month(Integer.valueOf(5)).year(Integer.valueOf(1978)).build())
  .maxTransactionAmount(Long.valueOf(1000L))
  .mcc("7399").url("http://sample-entity.com")
  .annualCardVolume(Long.valueOf(100L))
  .defaultStatementDescriptor("Business Inc")
  .incorporationDate(Date.builder().day(Integer.valueOf(1)).month(Integer.valueOf(12)).year(Integer.valueOf(2012)).build())
  .principalPercentageOwnership(Integer.valueOf(51)).build()).build();

Maybe<Identity> response = api.identities.post(form);
if(! response.succeeded().booleanValue()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}
    Identity identity = (Identity)response.view();
    identity.getId();

```
```php
<?php
use Lacore\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
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
	        "ownership_type"=> "PRIVATE", 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
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
```python


from lacore.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": True, 
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
	        "ownership_type": "PRIVATE", 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
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
	}).save()

```
```ruby
identity = Lacore::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Petes Coffee", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "incorporation_date"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "business_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "ownership_type"=> "PRIVATE", 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PetesCoffee.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-11-28T02:57:06.39Z",
  "updated_at" : "2017-11-28T02:57:06.39Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

Before we can begin charging cards we'll need to provision a `Merchant` account for your seller. This requires 3-steps, which we'll go into greater detail in the next few sections:

1. First, create an `Identity` resource with the merchant's underwriting and identity verification information

    `POST https://lacore-sandbox.finixpayments.com/identities/`

2. Second, create a `Payment Instrument` representing the merchant's bank account where processed funds will be settled (i.e. deposited)

    `POST https://lacore-sandbox.finixpayments.com/payment_instruments/`

3. Finally, provision the `Merchant` account

    `POST https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID/merchants`

Let's start with the first step by creating an `Identity` resource. Each `Identity` represents either a person or a business. We use this resource to associate cards and payouts. This structure makes it simple to manage and reconcile payment instruments and payout history. Accounting of funds is done using the Identity so it's recommended to have an Identity per recipient of funds. Additionally, the Identity resource is optionally used to collect KYC information.

You'll want to store the ID of the newly created `Identity` resource for
reference later.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities`

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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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

### Step 2: Tokenize a Bank Account for Funding your Merchant
```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
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
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}'


```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.enums.BankAccountType;
import io.lacore.payments.forms.BankAccountForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.BankAccount;
import io.lacore.payments.views.Identity;
import java.util.Currency;

BankAccountForm form = BankAccountForm.builder()
        .name("Joe Doe")
        .identity("IDwdNkeVs6byLWrz3Fe44kDv")
        .accountNumber("84012312415")
        .bankCode("840123124")
        .accountType(BankAccountType.SAVINGS)
        .companyName("company name")
        .country("USA")
        .currency(Currency.getInstance("USD"))
        .build();

Maybe<BankAccount> request = api.instruments.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create bank account");
}
BankAccount bankAccount = request.view();

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\BankAccount;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$bank_account = new BankAccount(
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
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
```python


from lacore.resources import BankAccount

bank_account = BankAccount(**
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
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save()

```
```ruby
bank_account = Lacore::BankAccount.new(
	{
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> {
	        "Bank Account"=> "Company Account"
	    }, 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save
```
> Example Response:

```json
{
  "id" : "PI3gsjWarFX8GzVvkChU7V6U",
  "fingerprint" : "FPR1890442507",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs8yR",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-11-28T02:57:16.23Z",
  "updated_at" : "2017-11-28T02:57:16.23Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **required** | Account owner's full name (max 40 characters)
### Step 3: Provision Merchant Account

```shell
curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'
```
```java
import io.lacore.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().build());

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\Merchant;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$merchant = $identity->provisionMerchantOn(new Merchant());
```
```python


from lacore.resources import Identity
from lacore.resources import Merchant

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
merchant = identity.provision_merchant_on(Merchant())
```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "verification" : "VIwUZauXhoKuGSAxEkdSWpj1",
  "merchant_profile" : "MPibQCVXSe3fWtmJ6BEPqKS8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-11-28T02:57:17.94Z",
  "updated_at" : "2017-11-28T02:57:17.94Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications"
    },
    "merchant_profile" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchant_profiles/MPibQCVXSe3fWtmJ6BEPqKS8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "verification" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIwUZauXhoKuGSAxEkdSWpj1"
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

3. `REJECTED`: Merchant was rejected by the processor either because the information collected was invalid or it failed one of a number of regulatory and/or
compliance checks (e.g. KYC, OFAC or MATCH)
  * processing_enabled: False
  * settlement_enabled: False

<aside class="notice">
Provisioning a Merchant account is an asynchronous request. We recommend creating
a Webhook to listen for the state change.
</aside>


#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

### Step 4: Create an Identity for a Buyer
```shell

curl https://lacore-sandbox.finixpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jim", 
	        "last_name": "Green", 
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
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.forms.Address;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.forms.Date;


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
use Lacore\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Green", 
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


from lacore.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jim", 
	        "last_name": "Green", 
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
```ruby
identity = Lacore::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Green", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }
	    }
	}).save

```
> Example Response:

```json
{
  "id" : "IDnGxd37hZkrFRuF9dyzieYK",
  "entity" : {
    "title" : null,
    "first_name" : "Jim",
    "last_name" : "Green",
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
  "created_at" : "2017-11-28T02:57:19.14Z",
  "updated_at" : "2017-11-28T02:57:19.14Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

Now that we have successfully provisioned a `Merchant` we'll need to create an
`Identity` that represents your buyer. Don't worry though you won't need to capture
the same amount of information from your buyer. **So long as you
don't pass a business_type field all the fields are optional.**

<aside class="warning">
Passing a business_type will introduce the underwriting form validators.
</aside>

Typically, we suggest at least collecting the buyer's name and email to help
with accounting, reconciliation, and chargebacks.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities`

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

### Step 5: Tokenize a Card
```shell


curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "name": "Walter Jones", 
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
	    "identity": "IDnGxd37hZkrFRuF9dyzieYK"
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.forms.Address;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("IDwdNkeVs6byLWrz3Fe44kDv")
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
use Lacore\Resources\PaymentCard;
use Lacore\Resources\Identity;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Jones", 
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
	    "identity"=> "IDnGxd37hZkrFRuF9dyzieYK"
	));
$card = $identity->createPaymentCard($card);

```
```python


from lacore.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Jones", 
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
	    "identity": "IDnGxd37hZkrFRuF9dyzieYK"
	}).save()
```
```ruby
card = Lacore::PaymentCard.new(
	{
	    "name"=> "Walter Jones", 
	    "expiration_year"=> 2020, 
	    "tags"=> {
	        "card_name"=> "Business Card"
	    }, 
	    "number"=> "4957030420210454", 
	    "expiration_month"=> 12, 
	    "address"=> {
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    }, 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDnGxd37hZkrFRuF9dyzieYK"
	}).save
```
> Example Response:

```json
{
  "id" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "fingerprint" : "FPR-819304959",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Jones",
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
  "created_at" : "2017-11-28T02:57:20.19Z",
  "updated_at" : "2017-11-28T02:57:20.19Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnGxd37hZkrFRuF9dyzieYK",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/updates"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`

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

### Step 6: Create an Authorization
```shell
curl https://lacore-sandbox.finixpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

AuthorizationCreateForm formCreateAuthorization = AuthorizationCreateForm.builder()
    .amount(10000L)
    .merchantIdentity("IDwdNkeVs6byLWrz3Fe44kDv")
    .source("PIbw5neVqmvTe2ZHWbjEoKdj")
    .build();

Maybe<Authorization> response = api.authorizations.post(formCreateAuthorization);

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getMessage());
  throw new RuntimeException("API error attempting to creating Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();

```
```python


from lacore.resources import Authorization
authorization = Authorization(**
	{
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()

```
```ruby
authorization = Lacore::Authorization.new(
	{
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU2nHicAxHDtZ46rkeY5snPk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:29.11Z",
  "updated_at" : "2017-11-28T02:57:29.16Z",
  "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : false,
  "expires_at" : "2017-12-05T02:57:29.11Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
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
for your records so that we can capture those funds in the next step.


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

`POST https://lacore-sandbox.finixpayments.com/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The buyer's `Payment Instrument` ID that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

### Step 7: Capture the Authorization
```shell
curl https://lacore-sandbox.finixpayments.com/authorizations/AU2nHicAxHDtZ46rkeY5snPk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'
```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

AuthorizationUpdateForm form = AuthorizationUpdateForm.builder()
    .captureAmount(100L)
    .fee(10L)
    .statementDescriptor("Order 123")
    .build();

Maybe<Authorization> response = api.authorizations.id("AU2nHicAxHDtZ46rkeY5snPk").put(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getMessage());
    throw new RuntimeException("API error attempting to capture authorization");
}
Authorization capturedAuthorization = response.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = Authorization::retrieve('AU2nHicAxHDtZ46rkeY5snPk');
$authorization = $authorization->capture(50, 10);

```
```python


from lacore.resources import Authorization

authorization = Authorization.get(id="AU2nHicAxHDtZ46rkeY5snPk")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Lacore::Authorization.retrieve(:id=>"AU2nHicAxHDtZ46rkeY5snPk")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU2nHicAxHDtZ46rkeY5snPk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRurPqe5d7k51egCdKAM5uRV",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:29.07Z",
  "updated_at" : "2017-11-28T02:57:31.56Z",
  "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : false,
  "expires_at" : "2017-12-05T02:57:29.07Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "transfer" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
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
 a 10% service fee you'll want to pass 1000 as the fee. This way when the
 funds are eventually settled out only $90 will be disbursed to your merchant.

Once successfully captured the `transfer` field of the `Authorization` will
contain the ID for the corresponding `Transfer` resource. By default, `Transfers`
will be in a PENDING state. PENDING means that the system hasn't submitted the
capture request as they are submitted via batch request. Once submited
the state of the `Transfer` will update to SUCCEEDED.

Next we're going to show you how to settle out the funds to your merchant.

#### HTTP Request

`PUT https://lacore-sandbox.finixpayments.com/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
capture_amount | *integer*, **required** | The amount of the  `Authorization`  you would like to capture in cents. Must be less than or equal to the amount of the `Authorization`
fee | *integer*, **optional** | Amount of the captured `Authorization` you would like to collect as your fee. Must be less than or equal to the amount

### Step 8: Create a Batch Settlement
```shell
curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.SettlementForm;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.*;
import java.util.Currency;


Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

SettlementForm formSettlement = SettlementForm.builder()
    .currency(Currency.getInstance("USD"))
    .build();

Transfer transfer = api.transfers.id("AU2nHicAxHDtZ46rkeY5snPk").get().view();

Maybe<Settlement> response = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").settlements.post(formSettlement);

if (! response.succeeded()) {
    throw new RuntimeException("API error attempting to create batch settlement");
}

Settlement settlementBatch = response.view();

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\Settlement;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$settlement = new Settlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));
$settlement = $identity->createSettlement($settlement);

```
```python


from lacore.resources import Identity
from lacore.resources import Settlement

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")
settlement = identity.create_settlement(
	{
	    "currency"=> "USD", 
	    "tags"=> {
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    }
	})
```
> Example Response:

```json
{
  "id" : "STuhMoB2msMu31GtmVqVW6Z8",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "currency" : "USD",
  "created_at" : "2017-11-28T03:00:40.66Z",
  "updated_at" : "2017-11-28T03:00:40.68Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 762224,
  "total_fees" : 76225,
  "total_fee" : 76225,
  "net_amount" : 685999,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "funding_transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=debit"
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
The `total_amount` minus the `total_fee` equals the `net_amount` (the amount in cents
that will be deposited into your merchant's bank account).

<aside class="notice">
Once a batch Settlement has been created it will undergo review and typically be
paid out within 24 hours.
</aside>

Note that for reconciliation purposes each `Settlement` contains a [transfers
link](#list-transfers-in-a-settlement) which returns a list of all the
`Transfers` that comprise the batch.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID/settlements`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Embedded Tokenization

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to Lacore. For your
convenience we've provided a [jsfiddle](https://jsfiddle.net/ne96gvxs/) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Lacore API.
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
where you're hosting the aforementioned button. Please include the script as demonstrated to the right. Please refrain from hosting the iframe library locally as doing so prevents important updates.


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
          applicationId: 'AP3VrWhf2cFx5QakKk5UrT3f',
          environment: 'sandbox',
        }, function (tokenizedResponse) {
          // Define a callback to send your token to your back-end server
        });
      });
    });
 </script>
```


Next we need to configure the client so that it associates the card with your `Application`. We will also need to register a click event that fires when our users click on the button, thereby rendering the iframe on the page. Then when the form is submitted you'll be returned a unique `Token` resource representing the submitted card details. We will also need to define a callback for handling that response.

<aside class="notice">
 When you're ready to tokenize in production, pass `live` for the `environment` attribute.
</aside>


In the next step we'll show you how to claim the instrument via an authenticated HTTPS request on your back-end for future use.

> Example Response:

```json
{
  "id" : "TKsUM93k8ohxsKC33BkBXxeq",
  "fingerprint" : "FPR-1937246613",
  "created_at" : "2017-11-28T02:57:33.69Z",
  "updated_at" : "2017-11-28T02:57:33.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-11-29T02:57:33.69Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

### Step 4: Associate the Token
```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKsUM93k8ohxsKC33BkBXxeq")
    .identity("IDwdNkeVs6byLWrz3Fe44kDv")
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
use Lacore\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	));
$card = $card->save();

```
```python


from lacore.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save()

```
```ruby
card = Lacore::PaymentInstrument.new(
	{
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIsUM93k8ohxsKC33BkBXxeq",
  "fingerprint" : "FPR-1937246613",
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
  "created_at" : "2017-11-28T02:57:34.45Z",
  "updated_at" : "2017-11-28T02:57:34.45Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/updates"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`


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
[jsFiddle example](https://jsfiddle.net/rserna2010/vap35hru/).

### Step 1: Include library

```html
 <script type="text/javascript" src="https://js.verygoodvault.com/js-vgfield-2/payline.js"></script>
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
    secureForm.submit('/applications/AP3VrWhf2cFx5QakKk5UrT3f/tokens', {
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
  "id" : "TKsUM93k8ohxsKC33BkBXxeq",
  "fingerprint" : "FPR-1937246613",
  "created_at" : "2017-11-28T02:57:33.69Z",
  "updated_at" : "2017-11-28T02:57:33.69Z",
  "instrument_type" : "PAYMENT_CARD",
  "expires_at" : "2017-11-29T02:57:33.69Z",
  "currency" : "USD",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
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
curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}'

```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKsUM93k8ohxsKC33BkBXxeq")
    .identity("IDwdNkeVs6byLWrz3Fe44kDv")
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
use Lacore\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	));
$card = $card->save();

```
```python


from lacore.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save()

```
```ruby
card = Lacore::PaymentInstrument.new(
	{
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIsUM93k8ohxsKC33BkBXxeq",
  "fingerprint" : "FPR-1937246613",
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
  "created_at" : "2017-11-28T02:57:34.45Z",
  "updated_at" : "2017-11-28T02:57:34.45Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/updates"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Idempotency Requests

You'll notice the authorization and transfer object have a field named `idempotency_id` which ensures the API request is only performed once. Why is this important? We've all experienced a hanging request while on a checkout page and feared that if we refresh or submit the payment again we'll be charged twice. With Lacore, we remove the ambiguity by having the user generate a unique `idempotency_id` and sending it with the normal payload. If the user attempts a request with the same `idempotency_id`, the response will raise an exception. Now you can rest assured that when you create an authorization or debit a bank account that the user will be protected from potential network issues by simply passing `idempotency_id` in body of the request.

# Authorizations

An `Authorization` (also known as a card hold) reserves a specific amount on a
card to be captured (i.e. debited) at a later date, usually within 7 days.
When an `Authorization` is captured it produces a `Transfer` resource.

## Create an Authorization


```shell
curl https://lacore-sandbox.finixpayments.com/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

AuthorizationCreateForm formCreateAuthorization = AuthorizationCreateForm.builder()
                .amount(10000L)
                .merchantIdentity("IDwdNkeVs6byLWrz3Fe44kDv")
                .source("PIbw5neVqmvTe2ZHWbjEoKdj")
                .build();

Maybe<Authorization> response = api.authorizations.post(formCreateAuthorization);

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getMessage());
  throw new RuntimeException("API error attempting to creating Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    )
	));
$authorization = $authorization->save();


```
```python


from lacore.resources import Authorization

authorization = Authorization(**
	{
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency": "USD", 
	    "amount": 100, 
	    "source": "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }
	}).save()
```
```ruby
authorization = Lacore::Authorization.new(
	{
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "source"=> "PIbw5neVqmvTe2ZHWbjEoKdj", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "AU2nHicAxHDtZ46rkeY5snPk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:29.11Z",
  "updated_at" : "2017-11-28T02:57:29.16Z",
  "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : false,
  "expires_at" : "2017-12-05T02:57:29.11Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    }
  }
}
```

`Authorizations` have two possible states SUCCEEDED and FAILED. If the `Authorization`
 has succeeded, it must be captured before the `expires_at` or the funds will
 be released.

Learn how to prevent duplicate authorizations by passing an [idempotency ID](#idempotency-requests) in the payload.

<aside class="warning">
Authorizations on debit cards actually place a hold on funds in the cardholder's
bank account and may lead to lower than expected balances and/or insufficient
funds issues.
</aside>


<aside class="notice">
If the transfer field of an Authorization is null it has not yet been captured.
</aside>


#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/authorizations`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | The `Payment Instrument` that you will be performing the authorization
merchant_identity | *string*, **required** | The ID of the `Identity` for the merchant that you are transacting on behalf of
amount | *integer*, **required** | The amount of the authorization in cents
currency | *string*, **required** | [3-letter ISO code](https://en.wikipedia.org/wiki/ISO_4217) designating the currency (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
idempotency_id | *string*, **optional** | A randomly generated value that you want associated with the request

## Capture an Authorization
```shell
curl https://lacore-sandbox.finixpayments.com/authorizations/AU2nHicAxHDtZ46rkeY5snPk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -X PUT \
    -d '
	{
	    "fee": "10", 
	    "capture_amount": 100
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

AuthorizationUpdateForm form = AuthorizationUpdateForm.builder()
        .captureAmount(100L)
        .fee(10L)
        .statementDescriptor("Order 123")
        .build();

Maybe<Authorization> responseAuthorization = api.authorizations.id("AU2nHicAxHDtZ46rkeY5snPk").put(form);

if (! responseAuthorization.succeeded()) {
    ApiError error = responseAuthorization.error();
    System.out.println(error.getMessage());
    throw new RuntimeException("API error attempting to capture authorization");
}
Authorization capturedAuth = responseAuthorization.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = Authorization::retrieve('AU2nHicAxHDtZ46rkeY5snPk');
$authorization = $authorization->capture([
                    "capture_amount"=> 50,
                    "fee"=> 10
                ]);

```
```python


from lacore.resources import Authorization

authorization = Authorization.get(id="AU2nHicAxHDtZ46rkeY5snPk")
authorization.capture(**
	{
	    "fee": "10", 
	    "capture_amount": 100
	})

```
```ruby
authorization = Lacore::Authorization.retrieve(:id=>"AU2nHicAxHDtZ46rkeY5snPk")
authorization = authorization.capture(
	{
	    "fee"=> "10", 
	    "capture_amount"=> 100
	})



```
> Example Response:

```json
{
  "id" : "AU2nHicAxHDtZ46rkeY5snPk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRurPqe5d7k51egCdKAM5uRV",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:29.07Z",
  "updated_at" : "2017-11-28T02:57:31.56Z",
  "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : false,
  "expires_at" : "2017-12-05T02:57:29.07Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "transfer" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
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

`PUT https://lacore-sandbox.finixpayments.com/authorizations/:AUTHORIZATION_ID`

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

curl https://lacore-sandbox.finixpayments.com/authorizations/AU2UEo8u2Vpm9QSVoxTenKCo \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -X PUT \
    -d '
	{
	    "void_me": true
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.AuthorizationUpdateForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.*;

AuthorizationUpdateForm formVoid = AuthorizationUpdateForm.builder()
        .voidMe(true)
        .build();

Maybe<Authorization> response = api.authorizations.id("AU2nHicAxHDtZ46rkeY5snPk").put(formVoid);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to void authorization");
}
Authorization voidAuthorization = response.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = Authorization::retrieve('AU2nHicAxHDtZ46rkeY5snPk');
$authorization->void(true);
$authorization = $authorization->save();


```
```python


from lacore.resources import Authorization

authorization = Authorization.get(id="AU2nHicAxHDtZ46rkeY5snPk")
authorization.void()

```
```ruby
authorization = Lacore::Authorization.retrieve(:id=>"AU2nHicAxHDtZ46rkeY5snPk")
authorization = authorization.void
```
> Example Response:

```json
{
  "id" : "AU2UEo8u2Vpm9QSVoxTenKCo",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : null,
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:35.41Z",
  "updated_at" : "2017-11-28T02:57:36.54Z",
  "trace_id" : "aad31848-214f-431c-81a2-b810893cd33f",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : true,
  "expires_at" : "2017-12-05T02:57:35.41Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2UEo8u2Vpm9QSVoxTenKCo"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    }
  }
}
```

Cancels the `Authorization` thereby releasing the funds. After voiding an
`Authorization` it can no longer be captured.

#### HTTP Request

`PUT https://lacore-sandbox.finixpayments.com/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
void_me | *boolean*, **required** | Set to True to void the `Authorization`

## Fetch an Authorization

```shell

curl https://lacore-sandbox.finixpayments.com/authorizations/AU2nHicAxHDtZ46rkeY5snPk \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.ApiClient;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Authorization;

Maybe <Authorization> response =  api.authorizations
    .id("AU2nHicAxHDtZ46rkeY5snPk")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    throw new RuntimeException("API error in attempting to fetch Authorization");
}

Authorization authorization = response.view();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorization = Authorization::retrieve('AU2nHicAxHDtZ46rkeY5snPk');

```
```python


from lacore.resources import Authorization

authorization = Authorization.get(id="AU2nHicAxHDtZ46rkeY5snPk")
```
```ruby
authorization = Lacore::Authorization.retrieve(:id=>"AU2nHicAxHDtZ46rkeY5snPk")


```
> Example Response:

```json
{
  "id" : "AU2nHicAxHDtZ46rkeY5snPk",
  "amount" : 100,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "SUCCEEDED",
  "currency" : "USD",
  "transfer" : "TRurPqe5d7k51egCdKAM5uRV",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:29.07Z",
  "updated_at" : "2017-11-28T02:57:31.56Z",
  "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
  "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "is_void" : false,
  "expires_at" : "2017-12-05T02:57:29.07Z",
  "idempotency_id" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "transfer" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    }
  }
}
```

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/authorizations/:AUTHORIZATION_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:AUTHORIZATION_ID | ID of the Authorization


## List all Authorizations
```shell
curl https://lacore-sandbox.finixpayments.com/authorizations/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.*;

Maybe<Page<Authorization>> response = api.authorizations.get();

if (! response.succeeded()) {
   ApiError error = response.error();
   System.out.println(error.getCode());
   System.out.println(error.getMessage());
   System.out.println(error.getDetails());
   throw new RuntimeException("API error attempting to list all Authorizations");
}

 Page<Authorization> page = response.view();
 Page<Authorization> page2 = page.getNext();

```
```php
<?php
use Lacore\Resources\Authorization;

$authorizations = Authorization::getPagination("/authorizations");


```
```python


from lacore.resources import Authorization

authorization = Authorization.get()
```
```ruby
authorizations = Lacore::Authorization.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "authorizations" : [ {
      "id" : "AU2UEo8u2Vpm9QSVoxTenKCo",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:35.41Z",
      "updated_at" : "2017-11-28T02:57:36.54Z",
      "trace_id" : "aad31848-214f-431c-81a2-b810893cd33f",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "is_void" : true,
      "expires_at" : "2017-12-05T02:57:35.41Z",
      "idempotency_id" : null,
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2UEo8u2Vpm9QSVoxTenKCo"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        }
      }
    }, {
      "id" : "AUvEYTPVbKjsFcz7FC2bLBzW",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : null,
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:30.15Z",
      "updated_at" : "2017-11-28T02:57:30.22Z",
      "trace_id" : "0c38a5b8-fde3-4615-be4c-ffb0de7c4492",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "is_void" : false,
      "expires_at" : "2017-12-05T02:57:30.15Z",
      "idempotency_id" : "01a016eaa60a46eaab381855f5d431ab",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AUvEYTPVbKjsFcz7FC2bLBzW"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        }
      }
    }, {
      "id" : "AU2nHicAxHDtZ46rkeY5snPk",
      "amount" : 100,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "currency" : "USD",
      "transfer" : "TRurPqe5d7k51egCdKAM5uRV",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:29.07Z",
      "updated_at" : "2017-11-28T02:57:31.56Z",
      "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "is_void" : false,
      "expires_at" : "2017-12-05T02:57:29.07Z",
      "idempotency_id" : null,
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/authorizations/AU2nHicAxHDtZ46rkeY5snPk"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "transfer" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/authorizations?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/authorizations/`

# Identities

An `Identity` resource represents either a buyer or a merchant and is in a many ways the 
centerpiece of the payment API's architecture. `Transfers` and `Payment Instruments` must 
be associated with an `Identity`. For both buyers ans merchants this structure makes it easy 
to manage and reconcile their associated banks accounts, transaction history, and payouts.

## Create an Identity for a Buyer


```shell


curl https://lacore-sandbox.finixpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jim", 
	        "last_name": "Green", 
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
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.forms.Address;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.forms.Date;


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
use Lacore\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Green", 
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


from lacore.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "key": "value"
	    }, 
	    "entity": {
	        "phone": "7145677613", 
	        "first_name": "Jim", 
	        "last_name": "Green", 
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
```ruby
identity = Lacore::Identity.new(
	{
	    "tags"=> {
	        "key"=> "value"
	    }, 
	    "entity"=> {
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Green", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDnGxd37hZkrFRuF9dyzieYK",
  "entity" : {
    "title" : null,
    "first_name" : "Jim",
    "last_name" : "Green",
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
  "created_at" : "2017-11-28T02:57:19.14Z",
  "updated_at" : "2017-11-28T02:57:19.14Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```
All fields for a buyer's Identity are optional. However, a `business_type` field should not be passed. Passing a `business_type` indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **optional** | First name
last_name | *string*, **optional** | Last name
phone | *string*, **optional** | Phone number
email | *string*, **optional** | Email address
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Create an Identity for a Merchant
```shell


curl https://lacore-sandbox.finixpayments.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": true, 
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
	        "ownership_type": "PRIVATE", 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
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
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.enums.BusinessType;
import io.lacore.payments.forms.Address;
import io.lacore.payments.forms.Date;
import io.lacore.payments.forms.IdentityEntityForm;
import io.lacore.payments.forms.IdentityForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Identity;


IdentityForm form = IdentityForm.builder()
  .entity(IdentityEntityForm.builder()
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
  .personalAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .businessAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .dob(Date.builder().day(Integer.valueOf(27)).month(Integer.valueOf(5)).year(Integer.valueOf(1978)).build())
  .maxTransactionAmount(Long.valueOf(1000L))
  .mcc("7399").url("http://sample-entity.com")
  .annualCardVolume(Long.valueOf(100L))
  .defaultStatementDescriptor("Business Inc")
  .incorporationDate(Date.builder().day(Integer.valueOf(1)).month(Integer.valueOf(12)).year(Integer.valueOf(2012)).build())
  .principalPercentageOwnership(Integer.valueOf(51)).build()).build();

Maybe<Identity> response = api.identities.post(form);
if(! response.succeeded().booleanValue()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}
    Identity identity = (Identity)response.view();
    

```
```php
<?php
use Lacore\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "Studio Rating"=> "4.7"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
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
	        "ownership_type"=> "PRIVATE", 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
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
```python


from lacore.resources import Identity

identity = Identity(**
	{
	    "tags": {
	        "Studio Rating": "4.7"
	    }, 
	    "entity": {
	        "last_name": "Sunkhronos", 
	        "max_transaction_amount": 12000000, 
	        "has_accepted_credit_cards_previously": True, 
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
	        "ownership_type": "PRIVATE", 
	        "first_name": "dwayne", 
	        "title": "CEO", 
	        "business_tax_id": "123456789", 
	        "doing_business_as": "Petes Coffee", 
	        "principal_percentage_ownership": 50, 
	        "email": "user@example.org", 
	        "mcc": "0742", 
	        "phone": "1234567890", 
	        "business_name": "Petes Coffee", 
	        "tax_id": "123456789", 
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
	}).save()
```
```ruby
identity = Lacore::Identity.new(
	{
	    "tags"=> {
	        "Studio Rating"=> "4.7"
	    }, 
	    "entity"=> {
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 12000000, 
	        "has_accepted_credit_cards_previously"=> true, 
	        "default_statement_descriptor"=> "Petes Coffee", 
	        "personal_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "incorporation_date"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "business_address"=> {
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        }, 
	        "ownership_type"=> "PRIVATE", 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Petes Coffee", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Petes Coffee", 
	        "tax_id"=> "123456789", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> {
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        }, 
	        "url"=> "www.PetesCoffee.com", 
	        "annual_card_volume"=> 12000000
	    }
	}).save
```
> Example Response:

```json
{
  "id" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-11-28T02:57:06.39Z",
  "updated_at" : "2017-11-28T02:57:06.39Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```
Create an `Identity` resource with the merchant's underwriting information.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities`

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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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

## Fetch a Identity

```shell

curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();

```
```php
<?php
use Lacore\Resources\Identity;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
```
```python


from lacore.resources import Identity
identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")

```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")


```
> Example Response:

```json
{
  "id" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "entity" : {
    "title" : "CEO",
    "first_name" : "dwayne",
    "last_name" : "Sunkhronos",
    "email" : "user@example.org",
    "business_name" : "Petes Coffee",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
  "created_at" : "2017-11-28T02:57:06.38Z",
  "updated_at" : "2017-11-28T02:57:06.38Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## List all Identities
```shell
curl https://lacore-sandbox.finixpayments.com/identities/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244


```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;

Maybe<Page<Identity>> response = api.identities.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Identities");
}

Page<Identity> page = response.view();

```
```php
<?php
use Lacore\Resources\Identity;

$identities= Identity::getPagination("/identities");


```
```python


from lacore.resources import Identity
identity = Identity.get()

```
```ruby
identities = Lacore::Identity.retrieve


```
> Example Response:

```json
{
  "_embedded" : {
    "identities" : [ {
      "id" : "IDnGxd37hZkrFRuF9dyzieYK",
      "entity" : {
        "title" : null,
        "first_name" : "Jim",
        "last_name" : "Green",
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
      "created_at" : "2017-11-28T02:57:19.13Z",
      "updated_at" : "2017-11-28T02:57:19.13Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDqsr431S8Ya6sFfnCcxLHAV",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "GOVERNMENT_AGENCY",
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
        "ownership_type" : "PUBLIC",
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Petes Coffee"
      },
      "tags" : {
        "Studio Rating" : "4.7"
      },
      "created_at" : "2017-11-28T02:57:15.04Z",
      "updated_at" : "2017-11-28T02:57:15.04Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqsr431S8Ya6sFfnCcxLHAV/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDsJ3rLUMjR8zyFcKQiApRAK",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "TAX_EXEMPT_ORGANIZATION",
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
      "created_at" : "2017-11-28T02:57:14.03Z",
      "updated_at" : "2017-11-28T02:57:14.03Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDsJ3rLUMjR8zyFcKQiApRAK/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDrj5YKKwyGb6gyFeMPqQhxf",
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
      "created_at" : "2017-11-28T02:57:12.90Z",
      "updated_at" : "2017-11-28T02:57:12.90Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDrj5YKKwyGb6gyFeMPqQhxf/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDvLY4WcigLHU3PX3voKfJYh",
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
      "created_at" : "2017-11-28T02:57:11.44Z",
      "updated_at" : "2017-11-28T02:57:11.44Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDvLY4WcigLHU3PX3voKfJYh/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDaN82RYizLYujUfVyQuqZXA",
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
      "created_at" : "2017-11-28T02:57:09.76Z",
      "updated_at" : "2017-11-28T02:57:09.76Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDaN82RYizLYujUfVyQuqZXA/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDe41MCockCKnsPXd2X4yi3g",
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
      "created_at" : "2017-11-28T02:57:08.69Z",
      "updated_at" : "2017-11-28T02:57:08.69Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDe41MCockCKnsPXd2X4yi3g/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDqDZ15AuEJxfxrz9YWzgu5B",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Lees Sandwiches",
        "business_type" : "CORPORATION",
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
      "created_at" : "2017-11-28T02:57:07.42Z",
      "updated_at" : "2017-11-28T02:57:07.42Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDqDZ15AuEJxfxrz9YWzgu5B/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Petes Coffee",
        "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
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
      "created_at" : "2017-11-28T02:57:06.38Z",
      "updated_at" : "2017-11-28T02:57:06.38Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "IDmuTMfuKfvVVQiaEWXLHZNK",
      "entity" : {
        "title" : null,
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "HyperWallet",
        "business_type" : "LIMITED_LIABILITY_COMPANY",
        "doing_business_as" : "HyperWallet",
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
        "application_name" : "HyperWallet"
      },
      "created_at" : "2017-11-28T02:57:00.35Z",
      "updated_at" : "2017-11-28T02:57:00.36Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/verifications"
        },
        "merchants" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/merchants"
        },
        "settlements" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/settlements"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/authorizations"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/transfers"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/payment_instruments"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK/disputes"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/identities?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/identities/`


## Update an Identity
```shell
curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "key": "value_2"
	    }, 
	    "entity": {
	        "business_phone": "+1 (408) 756-4497", 
	        "first_name": "Bernard", 
	        "last_name": "James", 
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
	        "doing_business_as": "Dunder Mifflin", 
	        "annual_card_volume": 12000000, 
	        "default_statement_descriptor": "Dunder Mifflin", 
	        "url": "www.DunderMifflin.com", 
	        "business_name": "Dunder Mifflin", 
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
import io.lacore.payments.ApiClient;
import io.lacore.payments.enums.BusinessType;
import io.lacore.payments.forms.*;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Identity;

IdentityForm form = IdentityForm.builder()
                .entity(
                  IdentityEntityForm.builder()
                      .firstName("dwayne")
                      .email("self@newdomain.com")
                      .businessPhone("+1 (408) 756-4497")
                      .build())
                .build();

Maybe<Identity> response = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").put(form);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to update identity");
}

Identity updatedIdentity = response.view();

```
```php
<?php

```
```python


from lacore.resources import Identity

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
identity.entity["first_name"] = "Bernard"
identity.save()

```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")

identity.entity["first_name"] = "Bernard"
identity.save
```
> Example Response:

```json
{
  "id" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "entity" : {
    "title" : "CTO",
    "first_name" : "Bernard",
    "last_name" : "James",
    "email" : "user@example.org",
    "business_name" : "Dunder Mifflin",
    "business_type" : "INDIVIDUAL_SOLE_PROPRIETORSHIP",
    "doing_business_as" : "Dunder Mifflin",
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
    "key" : "value_2"
  },
  "created_at" : "2017-11-28T02:57:06.38Z",
  "updated_at" : "2017-11-28T02:57:58.08Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/verifications"
    },
    "merchants" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants"
    },
    "settlements" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/authorizations"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/transfers"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/payment_instruments"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv/disputes"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
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

`POST https://lacore-sandbox.finixpayments.com/identities`

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
ownership_type | *string*, **required** | Values can be either PUBLIC to indicate a publicly traded company or PRIVATE for privately held businesses

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
line1 | *string*, **optional** | First line of the address (max 60 characters)
line2 | *string*, **optional** | Second line of the address (max 60 characters)
city | *string*, **required** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code


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

curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").get();
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
use Lacore\Resources\Identity;
use Lacore\Resources\Merchant;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from lacore.resources import Identity
from lacore.resources import Merchant

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")

merchant = identity.provision_merchant
```

> Example Response:

```json
{
  "id" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "verification" : "VIwUZauXhoKuGSAxEkdSWpj1",
  "merchant_profile" : "MPibQCVXSe3fWtmJ6BEPqKS8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-11-28T02:57:17.94Z",
  "updated_at" : "2017-11-28T02:57:17.94Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications"
    },
    "merchant_profile" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchant_profiles/MPibQCVXSe3fWtmJ6BEPqKS8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "verification" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIwUZauXhoKuGSAxEkdSWpj1"
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

3. `REJECTED`: Merchant was rejected by the processor either because the underwriting information collected was invalid or it failed one a number of regulatory and compliance checks (e.g. KYC, OFAC or MATCH)

<aside class="notice">
Provisioning a `Merchant` account is an asynchronous request. We recommend creating a Webhook to listen for the state change.
</aside>



#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

# Merchants

A `Merchant` resource represents a business's merchant account on a processor. In other words, any web service that connects buyers (i.e.
customers) and sellers (i.e. merchants).

## Provision a Merchant
```shell
curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "processor": null, 
	    "tags": {
	        "key_2": "value_2"
	    }
	}'

```
```java
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.*;
import io.finix.payments.forms.*;

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .processor(null)
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> underwriteMerchant = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").merchants.post(form);

if(! underwriteMerchant.succeeded()){
   System.out.println(underwriteMerchant.error());
}

Merchant provisionMerchant = underwriteMerchant.view();

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\Merchant;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');

$merchant = $identity->provisionMerchantOn(new Merchant());

```
```python


from lacore.resources import Identity
from lacore.resources import Merchant

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
merchant = identity.provision_merchant_on(Merchant())

```
```ruby
identity = Lacore::Identity.retrieve(:id => "MUc9AnmXPDqA3V332VcpxaWM")

merchant = identity.provision_merchant
```
> Example Response:

```json
{
  "id" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "verification" : "VIwUZauXhoKuGSAxEkdSWpj1",
  "merchant_profile" : "MPibQCVXSe3fWtmJ6BEPqKS8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : false,
  "settlement_enabled" : false,
  "tags" : { },
  "created_at" : "2017-11-28T02:57:17.94Z",
  "updated_at" : "2017-11-28T02:57:17.94Z",
  "onboarding_state" : "PROVISIONING",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications"
    },
    "merchant_profile" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchant_profiles/MPibQCVXSe3fWtmJ6BEPqKS8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "verification" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIwUZauXhoKuGSAxEkdSWpj1"
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


`Merchant` resources can have 3 potential `onboarding_states`:

1. `PROVISIONING`: Request is pending (state will typically change after two minutes)
  * processing_enabled: False
  * settlement_enabled: False

2. `APPROVED`: Merchant has been approved and can begin processing
  * processing_enabled: True
  * settlement_enabled: True

3. `REJECTED`: Merchant was rejected by the processor either because the
information collected was invalid or it failed one of a number of regulatory and/or
compliance checks (e.g. KYC, OFAC or MATCH)
  * processing_enabled: False
  * settlement_enabled: False

<aside class="notice">
Provisioning a `Merchant` account is an asynchronous request. We recommend creating a Webhook to listen for the state change.
</aside>



#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the Identity

## Fetch a Merchant

```shell
curl https://lacore-sandbox.finixpayments.com/merchants/MUc9AnmXPDqA3V332VcpxaWM \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Merchant;

Maybe<Merchant> response = api.merchants
    .id(merchant.id)
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Merchant");
}

Merchant merchantView = response.view();

```
```php
<?php
use Lacore\Resources\Merchant;

$merchant = Merchant::retrieve('MUc9AnmXPDqA3V332VcpxaWM');

```
```python


from lacore.resources import Merchant
merchant = Merchant.get(id="MUc9AnmXPDqA3V332VcpxaWM")

```
```ruby
merchant = Lacore::Merchant.retrieve(:id => "MUc9AnmXPDqA3V332VcpxaWM")

```
> Example Response:

```json
{
  "id" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "verification" : null,
  "merchant_profile" : "MPibQCVXSe3fWtmJ6BEPqKS8",
  "processor" : "DUMMY_V1",
  "processing_enabled" : true,
  "settlement_enabled" : true,
  "tags" : { },
  "created_at" : "2017-11-28T02:57:17.91Z",
  "updated_at" : "2017-11-28T02:57:18.04Z",
  "onboarding_state" : "APPROVED",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications"
    },
    "merchant_profile" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchant_profiles/MPibQCVXSe3fWtmJ6BEPqKS8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/merchants/:MERCHANT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Reattempt Merchant Provisioning
```shell
curl https://lacore-sandbox.finixpayments.com/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '{}'
```
```java
Merchant merchant = client.merchantsClient().fetch("MUc9AnmXPDqA3V332VcpxaWM");
Verification verification = merchant.verify(
  Verification.builder().build()
);
```
```php
<?php
use Lacore\Resources\Merchant;
use Lacore\Resources\Verification;

$merchant = Merchant::retrieve('MUc9AnmXPDqA3V332VcpxaWM');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python


from lacore.resources import Merchant
from lacore.resources import Verification

merchant = Merchant.get(id="MUc9AnmXPDqA3V332VcpxaWM")

verification = merchant.verify_on(Verification())

```
```ruby
merchant = Lacore::Merchant.retrieve(:id => "MUc9AnmXPDqA3V332VcpxaWM")

verification = merchant.verify
```
> Example Response:

```json
{
  "id" : "VIorYuZQnE5dVQP8mYu9E8RS",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-11-28T02:58:00.40Z",
  "updated_at" : "2017-11-28T02:58:00.46Z",
  "trace_id" : "41fb7c07-572f-40f2-a9b7-bbd49276a774",
  "payment_instrument" : null,
  "merchant" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIorYuZQnE5dVQP8mYu9E8RS"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "merchant" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    }
  }
}
```

Re-attempt provisioning a `Merchant` account on a processor if the previous attempt
returned a FAILED `onboarding_state`.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## Update Info on Processor
```shell
curl https://lacore-sandbox.finixpayments.com/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '{}'

```
```java

```
```php
<?php
use Lacore\Resources\Merchant;
use Lacore\Resources\Verification;

$merchant = Merchant::retrieve('MUc9AnmXPDqA3V332VcpxaWM');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);
```
```python


from lacore.resources import Merchant
merchant = Merchant.get(id="MUc9AnmXPDqA3V332VcpxaWM")

merchant.entity["first_name"] = "Michael"
merchant.save()

```
```ruby
merchant = Lacore::Merchant.retrieve(:id => "MUc9AnmXPDqA3V332VcpxaWM")

verification = merchant.entity["default_statement_descriptor"] = "Prestige World Wide"

```
> Example Response:

```json
{
  "id" : "VIorYuZQnE5dVQP8mYu9E8RS",
  "tags" : { },
  "messages" : [ ],
  "raw" : null,
  "processor" : "DUMMY_V1",
  "state" : "PENDING",
  "created_at" : "2017-11-28T02:58:00.40Z",
  "updated_at" : "2017-11-28T02:58:00.46Z",
  "trace_id" : "41fb7c07-572f-40f2-a9b7-bbd49276a774",
  "payment_instrument" : null,
  "merchant" : "MUc9AnmXPDqA3V332VcpxaWM",
  "identity" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIorYuZQnE5dVQP8mYu9E8RS"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "merchant" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
    }
  }
}
```

Update `Identity` information (e.g. default_statement_descriptor, KYC info, etc.)
on the underlying processor.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

## List all Merchants
```shell
curl https://lacore-sandbox.finixpayments.com/merchants/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;
import io.lacore.payments.views.Merchant;

Maybe<Page<Merchant>> response = api.merchants.get();

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getCode());
  System.out.println(error.getMessage());
  System.out.println(error.getDetails());
  throw new RuntimeException("API error attempting to list all Merchants");
}

Page<Merchant> page = response.view();

```
```php
<?php
use Lacore\Resources\Merchant;

$merchants = Merchant::getPagination("/merchants");


```
```python


from lacore.resources import Merchant
merchant = Merchant.get()

```
```ruby
merchants = Lacore::Merchant.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "merchants" : [ {
      "id" : "MUc9AnmXPDqA3V332VcpxaWM",
      "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "verification" : null,
      "merchant_profile" : "MPibQCVXSe3fWtmJ6BEPqKS8",
      "processor" : "DUMMY_V1",
      "processing_enabled" : true,
      "settlement_enabled" : true,
      "tags" : { },
      "created_at" : "2017-11-28T02:57:17.91Z",
      "updated_at" : "2017-11-28T02:57:18.04Z",
      "onboarding_state" : "APPROVED",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications"
        },
        "merchant_profile" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/merchant_profiles/MPibQCVXSe3fWtmJ6BEPqKS8"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/merchants?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/merchants/`

## List Merchant Verifications
```shell
curl https://lacore-sandbox.finixpayments.com/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java

```
```php
<?php
use Lacore\Resources\Merchant;
use Lacore\Resources\Verification;

$merchant = Merchant::retrieve('MUc9AnmXPDqA3V332VcpxaWM');
$verifications = Verification::getPagination($merchant->getHref("verifications"));


```
```python


from lacore.resources import Merchant
merchant = Merchant.get(id="MUc9AnmXPDqA3V332VcpxaWM")
verifications = merchant.verifications

```
```ruby
merchant = Lacore::Merchant.retrieve(:id => "MUc9AnmXPDqA3V332VcpxaWM")
verifications = merchant.verifications
```
> Example Response:

```json
{
  "_embedded" : {
    "verifications" : [ {
      "id" : "VIwUZauXhoKuGSAxEkdSWpj1",
      "tags" : {
        "key_2" : "value_2"
      },
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "processor" : "DUMMY_V1",
      "state" : "SUCCEEDED",
      "created_at" : "2017-11-28T02:57:17.91Z",
      "updated_at" : "2017-11-28T02:57:18.08Z",
      "trace_id" : "b26d997d-477d-4523-bb0e-ec22eb79a2cc",
      "payment_instrument" : null,
      "merchant" : "MUc9AnmXPDqA3V332VcpxaWM",
      "identity" : null,
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/verifications/VIwUZauXhoKuGSAxEkdSWpj1"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "merchant" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/merchants/MUc9AnmXPDqA3V332VcpxaWM"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/merchants/MUc9AnmXPDqA3V332VcpxaWM/verifications?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
  }
}
```

Retrieve all attempts to onboard (i.e. provision) a merchant onto a processor.

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/merchants/:MERCHANT_ID/verifications`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:MERCHANT_ID | ID of the `Merchant`

# Payment Instruments

A `Payment Instrument` resource represents either a credit card or bank account.
A `Payment Instrument` may be tokenized multiple times and each tokenization produces
a unique ID. Each ID may only be associated one time and to only one `Identity`.
Once associated, a `Payment Instrument` may not be disassociated from an
`Identity`.


## Create a Card
```shell


curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "name": "Walter Jones", 
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
	    "identity": "IDnGxd37hZkrFRuF9dyzieYK"
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.forms.Address;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("IDwdNkeVs6byLWrz3Fe44kDv")
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
use Lacore\Resources\PaymentCard;
use Lacore\Resources\Identity;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$card = new PaymentCard(
	array(
	    "name"=> "Walter Jones", 
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
	    "identity"=> "IDnGxd37hZkrFRuF9dyzieYK"
	));
$card = $identity->createPaymentCard($card);

```
```python


from lacore.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Jones", 
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
	    "identity": "IDnGxd37hZkrFRuF9dyzieYK"
	}).save()
```
```ruby
card = Lacore::PaymentCard.new(
	{
	    "name"=> "Walter Jones", 
	    "expiration_year"=> 2020, 
	    "tags"=> {
	        "card_name"=> "Business Card"
	    }, 
	    "number"=> "4957030420210454", 
	    "expiration_month"=> 12, 
	    "address"=> {
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    }, 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDnGxd37hZkrFRuF9dyzieYK"
	}).save
```
> Example Response:

```json
{
  "id" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "fingerprint" : "FPR-819304959",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Jones",
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
  "created_at" : "2017-11-28T02:57:20.19Z",
  "updated_at" : "2017-11-28T02:57:20.19Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnGxd37hZkrFRuF9dyzieYK",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/updates"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`

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
## Create a Bank Account
```shell

curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
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
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}'


```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.enums.BankAccountType;
import io.lacore.payments.forms.BankAccountForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.BankAccount;
import io.lacore.payments.views.Identity;
import java.util.Currency;

BankAccountForm form = BankAccountForm.builder()
        .name("Joe Doe")
        .identity("IDwdNkeVs6byLWrz3Fe44kDv")
        .accountNumber("84012312415")
        .bankCode("840123124")
        .accountType(BankAccountType.SAVINGS)
        .companyName("company name")
        .country("USA")
        .currency(Currency.getInstance("USD"))
        .build();

Maybe<BankAccount> request = api.instruments.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create bank account");
}
BankAccount bankAccount = request.view();

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\BankAccount;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$bank_account = new BankAccount(
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
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	));
$bank_account = $identity->createBankAccount($bank_account);
```
```python


from lacore.resources import BankAccount

bank_account = BankAccount(**
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
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save()
```
```ruby
bank_account = Lacore::BankAccount.new(
	{
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "tags"=> {
	        "Bank Account"=> "Company Account"
	    }, 
	    "country"=> "USA", 
	    "bank_code"=> "123123123", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save
```
> Example Response:

```json
{
  "id" : "PI3gsjWarFX8GzVvkChU7V6U",
  "fingerprint" : "FPR1890442507",
  "tags" : {
    "Bank Account" : "Company Account"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs8yR",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-11-28T02:57:16.23Z",
  "updated_at" : "2017-11-28T02:57:16.23Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
account_number | *string*, **required** | Bank account number
bank_code | *string*, **required** | Bank routing number
type | *string*, **required** | Type of `Payment Instrument` (for bank accounts use BANK_ACCOUNT)
identity | *string*, **required**| ID for the `Identity` resource which the account is associated
account_type | *string*, **required** | Either CHECKING or SAVINGS
name | *string*, **required** | Account owner's full name (max 40 characters)
## Associate a Token
```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

TokenAssociationForm tokenForm =  TokenAssociationForm.builder()
    .token("TKsUM93k8ohxsKC33BkBXxeq")
    .identity("IDwdNkeVs6byLWrz3Fe44kDv")
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
use Lacore\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	));
$card = $card->save();

```
```python


from lacore.resources import PaymentInstrument

payment_instrument = PaymentInstrument(**
	{
	    "token": "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type": "TOKEN", 
	    "identity": "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save()
```
```ruby
card = Lacore::PaymentInstrument.new(
	{
	    "token"=> "TKsUM93k8ohxsKC33BkBXxeq", 
	    "type"=> "TOKEN", 
	    "identity"=> "IDwdNkeVs6byLWrz3Fe44kDv"
	}).save
```
> Example Response:

```json
{
  "id" : "PIsUM93k8ohxsKC33BkBXxeq",
  "fingerprint" : "FPR-1937246613",
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
  "created_at" : "2017-11-28T02:57:34.45Z",
  "updated_at" : "2017-11-28T02:57:34.45Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/updates"
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

`POST https://lacore-sandbox.finixpayments.com/payment_instruments`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
token | *string*, **required** | ID for the `Token` that was returned via the tokenization client or hosted iframe
type | *string*, **required** | Must pass TOKEN as the value
identity | *string*, **required**| ID for the `Identity` resource which the account is to be associated


## Fetch a Bank Account

```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.views.Instrument;
import io.lacore.payments.interfaces.Maybe;

Maybe<Instrument> response = api.paymentInstruments
    .id("PI3gsjWarFX8GzVvkChU7V6U")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Bank Account");
}

Instrument bankAccountView = response.view();

```
```php
<?php
use Lacore\Resources\PaymentInstrument;

$bank_account = PaymentInstrument::retrieve('PI3gsjWarFX8GzVvkChU7V6U');

```
```python


from lacore.resources import PaymentInstrument
bank_account = PaymentInstrument.get(id="PI3gsjWarFX8GzVvkChU7V6U")

```
```ruby
bank_account = Lacore::BankAccount.retrieve(:id=> "PI3gsjWarFX8GzVvkChU7V6U")

```
> Example Response:

```json
{
  "id" : "PI3gsjWarFX8GzVvkChU7V6U",
  "fingerprint" : "FPR1890442507",
  "tags" : {
    "Display Name" : "Updated Field"
  },
  "bank_code" : "123123123",
  "country" : "USA",
  "masked_account_number" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs8yR",
  "name" : "Fran Lemke",
  "account_type" : "SAVINGS",
  "created_at" : "2017-11-28T02:57:16.21Z",
  "updated_at" : "2017-11-28T02:57:17.04Z",
  "instrument_type" : "BANK_ACCOUNT",
  "type" : "BANK_ACCOUNT",
  "currency" : "USD",
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `BANK_ACCOUNT`

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Fetch a Credit Card
```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \

```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;

Maybe<PaymentCard> response = api.instruments
  .id("PIbw5neVqmvTe2ZHWbjEoKdj")
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
use Lacore\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('PIbw5neVqmvTe2ZHWbjEoKdj');

```
```python


from lacore.resources import PaymentInstrument
credit_card = PaymentInstrument.get(id="PIbw5neVqmvTe2ZHWbjEoKdj")

```
```ruby
card = Lacore::PaymentCard.retrieve(:id=> "PIbw5neVqmvTe2ZHWbjEoKdj")


```
> Example Response:

```json
{
  "id" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "fingerprint" : "FPR-819304959",
  "tags" : {
    "card_name" : "Business Card"
  },
  "expiration_month" : 12,
  "expiration_year" : 2020,
  "last_four" : "0454",
  "brand" : "VISA",
  "card_type" : "UNKNOWN",
  "name" : "Walter Jones",
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
  "created_at" : "2017-11-28T02:57:20.16Z",
  "updated_at" : "2017-11-28T02:57:29.14Z",
  "instrument_type" : "PAYMENT_CARD",
  "type" : "PAYMENT_CARD",
  "currency" : "USD",
  "identity" : "IDnGxd37hZkrFRuF9dyzieYK",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
    },
    "authorizations" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/authorizations"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/transfers"
    },
    "verifications" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/verifications"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "updates" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/updates"
    }
  }
}
```

Fetch a previously created `Payment Instrument` that is of type `PAYMENT_CARD`

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:PAYMENT_INSTRUMENT_ID | ID of the `Payment Instrument`

## Check for Card Updates (Account Updater)

Lacore works with card networks so that your costumers can continue, without interruption, using your service even if their card has changed due to it being closed, lost, or stolen. When a successful account update record is located, the `Payment Instrument` will be automatically updated with the new primary account number or new expiration date.

<aside class="warning">
Please note that only Visa, MasterCard, and Discover cards are compatible with this feature. Also, this feature does not support changes to a card's address.
</aside>

```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "merchant": "MUc9AnmXPDqA3V332VcpxaWM"
	}'

```
```java

```
```php
<?php

```
```python


from lacore.resources import PaymentCard

card = PaymentCard(**
	{
	    "name": "Walter Jones", 
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
	    "identity": "IDnGxd37hZkrFRuF9dyzieYK"
	}).save()
update = card.update("MUc9AnmXPDqA3V332VcpxaWM")

```
```ruby

```
> Example Response:

```json
{
  "id" : "IU2pq92HhJM4Eo3UNEMPji4L",
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "merchant" : "MUc9AnmXPDqA3V332VcpxaWM",
  "state" : "PENDING",
  "messages" : [ ],
  "created_at" : "2017-11-28T02:57:37.65Z",
  "updated_at" : "2017-11-28T02:57:37.67Z",
  "payment_instrument" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "trace_id" : "a7f1b4d6-6035-4d44-bad3-897c87568ef2",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/updates/IU2pq92HhJM4Eo3UNEMPji4L"
    },
    "payment_instrument" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### Immediate Response

When first making a Post request to the `updates` endpoint, the state field will either be pending or failed.

1. `PENDING`: The initial Account Update request has been approved by the card networks and is awaiting review.

2. `FAILED`: Request rejected due to one of the following reasons:
  * Invalid credit card number
  * Invalid expiration date


#### Subsequent Response


Once Lacore receives a response from the card network, the state of the `Update` resource will return either `SUCCEEDED` or `FAILED`. Each `Update` will also provide a message that details the reason for the outcome. If either an account number or expiration date was found, Lacore will automatically update the
associated `Payment Instrument` resource with the new details and the card will be
ready for use.


<aside class="warning">
This process can take up to five days. Lacore suggests utilizing webhooks
to listen for the response.
</aside>

1. `SUCCEEDED` Messages:
  * No changes found
  * The account number was changed
  * The expiration date was changed

2. `FAILED` Messages:
  * No match found
  * Invalid payment type (often due to unsupported card brands, e.g. Amex)
  * The issuing bank does not participate in the update program
  * The account was closed

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/payment_instruments/:PAYMENT_INSTRUMENT_ID/updates/`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of the `Merchant`
:PAYMENT_INSTRUMENT_ID | *string*, **required** | ID of the `Payment Instrument`

## List all Payment Instruments

```shell
curl https://lacore-sandbox.finixpayments.com/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244
```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;
import io.lacore.payments.views.Instrument;

Maybe<Page<Instrument>> response = api.instruments.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Payment Instruments");
}

Page<Instrument> page = response.view();

```
```php
<?php
use Lacore\Resources\PaymentInstrument;

$paymentinstruments = PaymentInstrument::getPagination("/payment_instruments");


```
```python


from lacore.resources import PaymentInstrument
payment_instruments = PaymentInstrument.get()

```
```ruby
payment_instruments = Lacore::PaymentInstruments.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "payment_instruments" : [ {
      "id" : "PIsUM93k8ohxsKC33BkBXxeq",
      "fingerprint" : "FPR-1937246613",
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
      "created_at" : "2017-11-28T02:57:34.42Z",
      "updated_at" : "2017-11-28T02:57:34.42Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/authorizations"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/transfers"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/verifications"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "updates" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIsUM93k8ohxsKC33BkBXxeq/updates"
        }
      }
    }, {
      "id" : "PIqmjxTeuN8udXNdFTqkx1zf",
      "fingerprint" : "FPR1890442507",
      "tags" : {
        "Bank Account" : "Company Account"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs8yR",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-11-28T02:57:21.29Z",
      "updated_at" : "2017-11-28T02:57:21.29Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDnGxd37hZkrFRuF9dyzieYK",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf/authorizations"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf/transfers"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf/verifications"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    }, {
      "id" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "fingerprint" : "FPR-819304959",
      "tags" : {
        "card_name" : "Business Card"
      },
      "expiration_month" : 12,
      "expiration_year" : 2020,
      "last_four" : "0454",
      "brand" : "VISA",
      "card_type" : "UNKNOWN",
      "name" : "Walter Jones",
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
      "created_at" : "2017-11-28T02:57:20.16Z",
      "updated_at" : "2017-11-28T02:57:29.14Z",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "currency" : "USD",
      "identity" : "IDnGxd37hZkrFRuF9dyzieYK",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/authorizations"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDnGxd37hZkrFRuF9dyzieYK"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/transfers"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/verifications"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "updates" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj/updates"
        }
      }
    }, {
      "id" : "PI3gsjWarFX8GzVvkChU7V6U",
      "fingerprint" : "FPR1890442507",
      "tags" : {
        "Display Name" : "Updated Field"
      },
      "bank_code" : "123123123",
      "country" : "USA",
      "masked_account_number" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs8yR",
      "name" : "Fran Lemke",
      "account_type" : "SAVINGS",
      "created_at" : "2017-11-28T02:57:16.21Z",
      "updated_at" : "2017-11-28T02:57:17.04Z",
      "instrument_type" : "BANK_ACCOUNT",
      "type" : "BANK_ACCOUNT",
      "currency" : "USD",
      "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U"
        },
        "authorizations" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/authorizations"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/transfers"
        },
        "verifications" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U/verifications"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/payment_instruments?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/payment_instruments`

# Settlements

A `Settlement` is a logical construct representing a collection (i.e. batch) of
`Transfers` that are intended to be paid out to a specific `Merchant`.

## Create a Batch Settlement

```shell

curl https://lacore-sandbox.finixpayments.com/identities/IDwdNkeVs6byLWrz3Fe44kDv/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	}'

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.SettlementForm;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.*;
import java.util.Currency;


Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

SettlementForm formSettlement = SettlementForm.builder()
        .currency(Currency.getInstance("USD"))
        .build();

Transfer transfer = api.transfers.id("AU2nHicAxHDtZ46rkeY5snPk").get().view();

Maybe<Settlement> response = api.identities.id("IDwdNkeVs6byLWrz3Fe44kDv").settlements.post(formSettlement);

if (! response.succeeded()) {
    throw new RuntimeException("API error attempting to create batch settlement");
}

Settlement settlementBatch = response.view();

```
```php
<?php
use Lacore\Resources\Identity;
use Lacore\Resources\Settlement;

$identity = Identity::retrieve('IDwdNkeVs6byLWrz3Fe44kDv');
$settlement = new Settlement(
	array(
	    "currency"=> "USD", 
	    "tags"=> array(
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    )
	));
$settlement = $identity->createSettlement($settlement);

```
```python


from lacore.resources import Identity
from lacore.resources import Settlement

identity = Identity.get(id="IDwdNkeVs6byLWrz3Fe44kDv")
settlement = Settlement(**
	{
	    "currency": "USD", 
	    "tags": {
	        "Internal Daily Settlement ID": "21DFASJSAKAS"
	    }
	})
identity.create_settlement(settlement)
```
```ruby
identity = Lacore::Identity.retrieve(:id=>"IDwdNkeVs6byLWrz3Fe44kDv")
settlement = identity.create_settlement(
	{
	    "currency"=> "USD", 
	    "tags"=> {
	        "Internal Daily Settlement ID"=> "21DFASJSAKAS"
	    }
	})
```
> Example Response:

```json
{
  "id" : "STuhMoB2msMu31GtmVqVW6Z8",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "currency" : "USD",
  "created_at" : "2017-11-28T03:00:40.66Z",
  "updated_at" : "2017-11-28T03:00:40.68Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 762224,
  "total_fees" : 76225,
  "total_fee" : 76225,
  "net_amount" : 685999,
  "destination" : null,
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "funding_transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=debit"
    }
  }
}
```
Each settlement is comprised of all the `Transfers` that have a SUCCEEDED state and
that have not been previously settled out. In other words, if a merchant has a
`Transfer` in the PENDING state it will not be included in the batch settlement.
In addition, `Settlements` will include any refunded Transfers as a deduction.
The `total_amount` minus the `total_fee` equals the `net_amount` (the amount in cents
that will be deposited into your merchant's bank account).

<aside class="notice">
To view all the Transfers that were included in a Settlement you can make a
request to the transfers link (i.e. POST https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/transfers
</aside>


#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/identities/:IDENTITY_ID/settlements`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:IDENTITY_ID | ID of the `Identity` for the merchant you wish to settle out


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

## Fetch a Batch Settlement

```shell


curl https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Settlement;

Maybe<Settlement> response = api.settlements
  .id("STuhMoB2msMu31GtmVqVW6Z8")
  .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch settlement");
}

Settlement settlementView = response.view();

```
```php
<?php
use Lacore\Resources\Settlement;

$settlement = Settlement::retrieve('STuhMoB2msMu31GtmVqVW6Z8');

```
```python


from lacore.resources import Settlements
settlement = Settlements.get(id="STuhMoB2msMu31GtmVqVW6Z8")

```
```ruby
settlement = Lacore::Settlement.retrieve(:id=>"STuhMoB2msMu31GtmVqVW6Z8")

```
> Example Response:

```json
{
  "id" : "STuhMoB2msMu31GtmVqVW6Z8",
  "tags" : {
    "Internal Daily Settlement ID" : "21DFASJSAKAS"
  },
  "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "currency" : "USD",
  "created_at" : "2017-11-28T03:00:40.63Z",
  "updated_at" : "2017-11-28T03:00:41.97Z",
  "processor" : "DUMMY_V1",
  "total_amount" : 762224,
  "total_fees" : 76225,
  "total_fee" : 76225,
  "net_amount" : 685999,
  "destination" : "PI3gsjWarFX8GzVvkChU7V6U",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "funding_transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers"
    },
    "transfers" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=fee"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=reverse"
    },
    "credits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=credit"
    },
    "debits" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=debit"
    }
  }
}
```

Fetch a previously created `Settlement`.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


## Remove Transfer(s) from a Batch Settlements

```shell

curl https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "transfers": [
	        "TRowh7R9qyzTEezyCrwkWmoV"
	    ]
	}'

```
```java

```
```php
<?php

```
```python



```
```ruby

```
Do you have a transfer in a batch settlement that you think may be a fraudulent transaction? So as long as the `Settlement` hasn't been funded, you can remove the `Transfer` or an array of `Transfers`, along with its corresponding fee from a batch settlement.

<aside class="notice">
Per the JSON API for deleting a resource, our API doesn't have a response body when removing a transfer from a settlement.
</aside>

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement

## List all Batch Settlements

```shell
curl https://lacore-sandbox.finixpayments.com/settlements/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;
import io.lacore.payments.views.Settlement;

Maybe<Page<Settlement>> request = api.settlements.get();

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Settlements");
}

Page<Settlement> page = request.view();

```
```php
<?php
use Lacore\Resources\Settlement;

$settlements = Settlement::getPagination("/settlements");


```
```python


from lacore.resources import Settlement
settlements = Settlement.get()

```
```ruby
settlements = Lacore::Settlement.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "settlements" : [ {
      "id" : "STuhMoB2msMu31GtmVqVW6Z8",
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "currency" : "USD",
      "created_at" : "2017-11-28T03:00:40.63Z",
      "updated_at" : "2017-11-28T03:00:41.97Z",
      "processor" : "DUMMY_V1",
      "total_amount" : 762224,
      "total_fees" : 76225,
      "total_fee" : 76225,
      "net_amount" : 685999,
      "destination" : "PI3gsjWarFX8GzVvkChU7V6U",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "funding_transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers"
        },
        "transfers" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=fee"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=reverse"
        },
        "credits" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=credit"
        },
        "debits" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?type=debit"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/settlements?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


## List Funding Transfers in a Batch Settlement

```shell
curl https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
Settlement settlement = client.settlementsClient().fetch("STuhMoB2msMu31GtmVqVW6Z8");
  settlement.fundingTransfersClient().<Resources<Transfer>>resourcesIterator()
    .forEachRemaining(page -> {
      Collection<Transfer> transfers = page.getContent();
      transfers.forEach(transfer ->
     // do something
      );
    });
}
```
```php
<?php
use Lacore\Resources\Settlement;

$settlement = Settlement::retrieve('STuhMoB2msMu31GtmVqVW6Z8');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));

```
```python


from lacore.resources import Settlements
settlement = Settlement.get(id="STuhMoB2msMu31GtmVqVW6Z8")
transfers = settlement.funding_transfers

```
```ruby
settlement = Lacore::Settlement.retrieve(:id=>"STuhMoB2msMu31GtmVqVW6Z8")
transfers = settlement.funding_transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRfVkTP3u4yrkYB8KmpFXnCN",
      "amount" : 685999,
      "tags" : {
        "Internal Daily Settlement ID" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "904bbb9b-9cea-4fff-85c3-ae1af3547883",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "destination" : "PI3gsjWarFX8GzVvkChU7V6U",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "CREDIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T03:00:41.68Z",
      "updated_at" : "2017-11-28T03:00:41.92Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRfVkTP3u4yrkYB8KmpFXnCN"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRfVkTP3u4yrkYB8KmpFXnCN/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRfVkTP3u4yrkYB8KmpFXnCN/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRfVkTP3u4yrkYB8KmpFXnCN/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRfVkTP3u4yrkYB8KmpFXnCN/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI3gsjWarFX8GzVvkChU7V6U"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8/funding_transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 1
  }
}
```

List the `Transfers` of type `CREDIT` that result from issuing a `Settlement`.

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/funding_transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement

## List Transfers in a Batch Settlement

```shell

curl https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
Settlement settlement = client.settlementsClient().fetch("STuhMoB2msMu31GtmVqVW6Z8");
    settlement.transfersClient().<Resources<Transfer>>resourcesIterator()
      .forEachRemaining(page -> {
        Collection<Transfer> transfers = page.getContent();
        transfers.forEach(transfer ->
       // do something
        );
      });
  }



```
```php
<?php
use Lacore\Resources\Settlement;

$settlement = Settlement::retrieve('STuhMoB2msMu31GtmVqVW6Z8');
$settlements = Settlement::getPagination($settlement->getHref("transfers"));

```
```python



```
```ruby
settlement = Lacore::Settlement.retrieve(:id=>"STuhMoB2msMu31GtmVqVW6Z8")
transfers = settlement.transfers
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TR8KC6PW4pwrJERyyKMb9DFZ",
      "amount" : 37623,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "8090697d-c3f9-45db-82b8-d45c2120e806",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "destination" : "PItwi5ge8SrUdjfrrDEUcD97",
      "ready_to_settle_at" : "2017-11-28T03:00:38.79Z",
      "fee_profile" : "FPwXTEhS5yCJwoHHtfYcVEHQ",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T03:00:38.53Z",
      "updated_at" : "2017-11-28T03:00:38.79Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDmuTMfuKfvVVQiaEWXLHZNK",
      "subtype" : "APPLICATION_FEE",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR8KC6PW4pwrJERyyKMb9DFZ"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR8KC6PW4pwrJERyyKMb9DFZ/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR8KC6PW4pwrJERyyKMb9DFZ/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR8KC6PW4pwrJERyyKMb9DFZ/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR8KC6PW4pwrJERyyKMb9DFZ/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PItwi5ge8SrUdjfrrDEUcD97"
        },
        "fee_profile" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/fee_profiles/FPwXTEhS5yCJwoHHtfYcVEHQ"
        }
      }
    }, {
      "id" : "TRd1jPYK4hwrzeMFnWMFH5De",
      "amount" : 38589,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "1bb290cd-4089-457a-8d85-97138cef44eb",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "destination" : "PItwi5ge8SrUdjfrrDEUcD97",
      "ready_to_settle_at" : "2017-11-28T03:00:38.48Z",
      "fee_profile" : "FPwXTEhS5yCJwoHHtfYcVEHQ",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T03:00:38.20Z",
      "updated_at" : "2017-11-28T03:00:38.47Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDmuTMfuKfvVVQiaEWXLHZNK",
      "subtype" : "APPLICATION_FEE",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRd1jPYK4hwrzeMFnWMFH5De"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRd1jPYK4hwrzeMFnWMFH5De/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDmuTMfuKfvVVQiaEWXLHZNK"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRd1jPYK4hwrzeMFnWMFH5De/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRd1jPYK4hwrzeMFnWMFH5De/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRd1jPYK4hwrzeMFnWMFH5De/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PItwi5ge8SrUdjfrrDEUcD97"
        },
        "fee_profile" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/fee_profiles/FPwXTEhS5yCJwoHHtfYcVEHQ"
        }
      }
    }, {
      "id" : "TRgxiRbyNUr5A5TA5KroaM6F",
      "amount" : 13,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "37a426dd-2ba3-4211-b252-92d58765e758",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "destination" : "PI61FW1hmjZtbvfqS4NKXxfV",
      "ready_to_settle_at" : "2017-11-28T03:00:38.14Z",
      "fee_profile" : "FPwXTEhS5yCJwoHHtfYcVEHQ",
      "fee" : 0,
      "statement_descriptor" : null,
      "type" : "FEE",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T03:00:37.81Z",
      "updated_at" : "2017-11-28T03:00:38.13Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDxoyrdEFwnP85cHzBfecs2D",
      "subtype" : "PLATFORM_FEE",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRgxiRbyNUr5A5TA5KroaM6F"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRgxiRbyNUr5A5TA5KroaM6F/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDxoyrdEFwnP85cHzBfecs2D"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRgxiRbyNUr5A5TA5KroaM6F/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRgxiRbyNUr5A5TA5KroaM6F/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRgxiRbyNUr5A5TA5KroaM6F/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PI61FW1hmjZtbvfqS4NKXxfV"
        },
        "fee_profile" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/fee_profiles/FPwXTEhS5yCJwoHHtfYcVEHQ"
        }
      }
    }, {
      "id" : "TRurPqe5d7k51egCdKAM5uRV",
      "amount" : 100,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : "2017-11-28T03:00:37.79Z",
      "fee_profile" : null,
      "fee" : 10,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:31.42Z",
      "updated_at" : "2017-11-28T02:58:00.57Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    }, {
      "id" : "TR3BQY5tKaRwvi6M5yjEP1m2",
      "amount" : 385892,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "53d4391a-24de-4916-beff-b77d15f348df",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : "2017-11-28T03:00:38.18Z",
      "fee_profile" : null,
      "fee" : 38589,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:23.15Z",
      "updated_at" : "2017-11-28T02:58:01.57Z",
      "idempotency_id" : "8a927c4aea884485802a65644d5d899f",
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    }, {
      "id" : "TRowh7R9qyzTEezyCrwkWmoV",
      "amount" : 376232,
      "tags" : {
        "order_number" : "12121212"
      },
      "state" : "SUCCEEDED",
      "trace_id" : "a821a477-c002-4c15-b15f-40b4e22ce733",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : "2017-11-28T03:00:38.51Z",
      "fee_profile" : null,
      "fee" : 37623,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:22.22Z",
      "updated_at" : "2017-11-28T02:58:01.71Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/settlements/STuhMoB2msMu31GtmVqVW6Z8/transfers?offset=0&limit=20&sort=created_at,desc"
    }
  },
  "page" : {
    "offset" : 0,
    "limit" : 20,
    "count" : 6
  }
}
```

List the batch of `Transfers` of type `DEBIT` and `REFUND` that comprise the net
 settled amount of a `Settlement`.

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/settlements/:SETTLEMENT_ID/transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement


# Transfers

A `Transfer` represents any flow of funds either to or from a `Payment Instrument`.
For example, a `Transfer` is a credit to a bank account [refund to a card](#refund-a-debit).

A `Transfer` can have one of three types: `Debit`, `Credit`, or `Reversal`. Each type indicates a different funds flow. For example:

* A **Debit** is created after capturing an Authorization or creating eCheck where funds are pulled from the issuer into the settlement account

* A **Reversal** represents a refund or chargeback where funds are returned to a customer

* A **Credit** is produced when funds are transferred to a merchant's bank account when funding (i.e. paying out) a batch settlement

`Transfers` can have four possible states values: PENDING, SUCCEEDED, FAILED, or CANCELED.

- **PENDING:** Authorization on `Payment Instrument` successfully created (i.e.
funds are being held), but awaiting system to batch submit the capture request
to complete the transaction

- **SUCCEEDED:** Funds captured and available for settlement (i.e. disbursement
via ACH Credit)

- **FAILED:** Authorization attempt failed

- **CANCELED:** Created, and then reversed before transfer has transitioned to succeeded

By default, `Transfers` will be in a PENDING state and will eventually (typically
within an hour) update to SUCCEEDED.

`ready_to_settle_at` field can have 2 possible values:

1. `null`: Funds have been captured, but are not yet ready to be paid out
2. `TIMESTAMP`: A UTC timestamp that specifies when the funds will be available to be payout out. Once in the past, the Transfer will be eligible for inclusion in a batch Settlement.

<aside class="notice">
When an Authorization is captured a corresponding Transfer will also be created.
</aside>

## Debit a Bank Account (ie eCheck)

Returns: Note eCheck transactions can be rejected for up to 60 days for a variety of reasons including insufficient funds, closed accounts, or a revoked authorization (i.e. dispute). When a return occurs a Transfer of type `REVERSAL` with a subtype `SYSTEM` is automatically created and will negatively impact the future settlement. 

```shell
curl https://lacore-sandbox.finixpayments.com/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
	{
	    "fee": 37623, 
	    "source": "PIqmjxTeuN8udXNdFTqkx1zf", 
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 376232
	}'


```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .amount(100L)
        .currency(Currency.getInstance("USD"))
        .source("PIbw5neVqmvTe2ZHWbjEoKdj}")
        .merchantIdentity("IDwdNkeVs6byLWrz3Fe44kDv")
        .tags(ImmutableMap.of("order_number", "21DFASJSAKAS"))
        .build();

Maybe<Transfer> response = api.transfers.post(form);
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to debit Bank Account");
}
Transfer transfer = response.view();

```
```php
<?php
use Lacore\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 37623, 
	    "source"=> "PIqmjxTeuN8udXNdFTqkx1zf", 
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "tags"=> array(
	        "order_number"=> "21DFASJSAKAS"
	    ), 
	    "currency"=> "USD", 
	    "amount"=> 376232
	));
$debit = $debit->save();

```
```python


from lacore.resources import Transfer

payout = Transfer(**
	{
	    "fee": 37623, 
	    "source": "PIqmjxTeuN8udXNdFTqkx1zf", 
	    "merchant_identity": "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "tags": {
	        "order_number": "21DFASJSAKAS"
	    }, 
	    "currency": "USD", 
	    "amount": 376232
	}).save()

```
```ruby
Lacore::Transfer.new(
	{
	    "fee"=> 37623, 
	    "source"=> "PIqmjxTeuN8udXNdFTqkx1zf", 
	    "merchant_identity"=> "IDwdNkeVs6byLWrz3Fe44kDv", 
	    "tags"=> {
	        "order_number"=> "21DFASJSAKAS"
	    }, 
	    "currency"=> "USD", 
	    "amount"=> 376232
	}).save

```


> Example Response:

```json
{
  "id" : "TRowh7R9qyzTEezyCrwkWmoV",
  "amount" : 376232,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "a821a477-c002-4c15-b15f-40b4e22ce733",
  "currency" : "USD",
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
  "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
  "ready_to_settle_at" : null,
  "fee_profile" : null,
  "fee" : 37623,
  "statement_descriptor" : "LAC*PETES COFFEE",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:22.27Z",
  "updated_at" : "2017-11-28T02:57:22.32Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/fees"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/disputes"
    },
    "source" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
    },
    "destination" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
    }
  }
}
```

A `Transfer` representing a customer payment where funds are obtained from a
bank account (i.e. ACH Debit, eCheck). These specific `Transfers` are
distinguished by their type which return DEBIT.

Learn how to prevent duplicate transfers by passing an [idempotency ID](#idempotency-requests) in the payload.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/transfers`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
source | *string*, **required** | ID of the `Payment Instrument` that will be debited
merchant_identity | *string*, **required** | `Identity` ID of the merchant whom you're charging on behalf of
amount | *integer*, **required** | The total amount that will be debited in cents (e.g. 100 cents to debit $1.00)
fee | *integer*, **optional** | The amount of the `Transfer` you would like to collect as your fee in cents. Defaults to zero (Must be less than or equal to the amount)
currency | *string*, **required** | 3-letter ISO code designating the currency of the `Transfers` (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
idempotency_id | *string*, **optional** | A randomly generated value that you want associated with the request

## Fetch a Transfer

```shell

curl https://lacore-sandbox.finixpayments.com/transfers/TRowh7R9qyzTEezyCrwkWmoV \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244


```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Transfer;

Maybe<Transfer> response = api.transfers
    .id("TRowh7R9qyzTEezyCrwkWmoV")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Transfer");
}

Transfer transferView = response.view();

```
```php
<?php
use Lacore\Resources\Transfer;

$transfer = Transfer::retrieve('TRowh7R9qyzTEezyCrwkWmoV');



```
```python


from lacore.resources import Transfer
transfer = Transfer.get(id="TRowh7R9qyzTEezyCrwkWmoV")

```
```ruby
transfer = Lacore::Transfer.retrieve(:id=> "TRowh7R9qyzTEezyCrwkWmoV")

```
> Example Response:

```json
{
  "id" : "TRowh7R9qyzTEezyCrwkWmoV",
  "amount" : 376232,
  "tags" : {
    "order_number" : "21DFASJSAKAS"
  },
  "state" : "PENDING",
  "trace_id" : "a821a477-c002-4c15-b15f-40b4e22ce733",
  "currency" : "USD",
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
  "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
  "ready_to_settle_at" : null,
  "fee_profile" : null,
  "fee" : 37623,
  "statement_descriptor" : "LAC*PETES COFFEE",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:22.22Z",
  "updated_at" : "2017-11-28T02:57:22.32Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/fees"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/disputes"
    },
    "source" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
    },
    "destination" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
    }
  }
}
```

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`

## Refund a Debit
```shell

curl https://lacore-sandbox.finixpayments.com/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d  '
                  {
                  "refund_amount" : 100
                  }
                '

```
```java

import io.lacore.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);

```
```php
<?php
use Lacore\Resources\Transfer;

$debit = Transfer::retrieve('TRowh7R9qyzTEezyCrwkWmoV');
$refund = $debit->reverse(11);

```
```python


from lacore.resources import Transfer

transfer = Transfer.get(id="TRowh7R9qyzTEezyCrwkWmoV")
transfer.reverse(**
                  {
                  "refund_amount" : 100
                  }
                )
```
```ruby
transfer = Lacore::Transfer.retrieve(:id=> "TRowh7R9qyzTEezyCrwkWmoV")

refund = transfer.reverse(100)

```
> Example Response:

```json
{
  "id" : "TRcvLf8civTVGyj4Fxypy6vi",
  "amount" : 620259,
  "tags" : { },
  "state" : "SUCCEEDED",
  "trace_id" : "5d3c5c52-07b7-4058-9972-2c34c1bb9007",
  "currency" : "USD",
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
  "destination" : "PIbw5neVqmvTe2ZHWbjEoKdj",
  "ready_to_settle_at" : null,
  "fee_profile" : null,
  "fee" : 62026,
  "statement_descriptor" : "LAC*PETES COFFEE",
  "type" : "REVERSAL",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:27.90Z",
  "updated_at" : "2017-11-28T02:57:27.97Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRcvLf8civTVGyj4Fxypy6vi"
    },
    "parent" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX"
    },
    "destination" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRcvLf8civTVGyj4Fxypy6vi/payment_instruments"
    }
  }
}
```

A `Transfer` representing the refund (i.e. reversal) of a previously created
`Transfer` (type DEBIT). The refunded amount may be any value up to the amount
of the original `Transfer`. These specific `Transfers` are distinguished by
their type which return REVERSAL.

A Reversal can have two `subtypes` indicating how they were created:

* **API**: Transfer created via an end-user API request (e.g. POST)
* **SYSTEM**: Transfer created via the upstream processor (e.g. resulting from
  an eCheck return); Note that SYSTEM created Transfers are rare occurrences.

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/transfers/:TRANSFER_ID/reversals`

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
curl https://lacore-sandbox.finixpayments.com/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;
import io.lacore.payments.views.Transfer;

Maybe<Page<Transfer>> request = api.transfers.get();

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Transfers");
}

Page<Transfer> page = request.view();

```
```php
<?php
use Lacore\Resources\Transfer;

$transfers = Transfer::getPagination("/transfers");


```
```python


from lacore.resources import Transfer
transfer = Transfer.get()

```
```ruby
transfers = Lacore::Transfer.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "transfers" : [ {
      "id" : "TRurPqe5d7k51egCdKAM5uRV",
      "amount" : 100,
      "tags" : { },
      "state" : "PENDING",
      "trace_id" : "6d38ef94-5ab3-4922-a495-070d8e5a1735",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 10,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:31.42Z",
      "updated_at" : "2017-11-28T02:57:31.56Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRurPqe5d7k51egCdKAM5uRV/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    }, {
      "id" : "TRcvLf8civTVGyj4Fxypy6vi",
      "amount" : 620259,
      "tags" : { },
      "state" : "SUCCEEDED",
      "trace_id" : "23e7d284-f6a2-4528-b66f-154f8269902b",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "destination" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 62026,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "REVERSAL",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:27.80Z",
      "updated_at" : "2017-11-28T02:57:27.97Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRcvLf8civTVGyj4Fxypy6vi"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRcvLf8civTVGyj4Fxypy6vi/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "parent" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
        }
      }
    }, {
      "id" : "TRtUrGL784WTKpR8yFTFSheX",
      "amount" : 620259,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "CANCELED",
      "trace_id" : "a6392d3c-6a9a-4268-8407-53bae0230af9",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIbw5neVqmvTe2ZHWbjEoKdj",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 62026,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:26.94Z",
      "updated_at" : "2017-11-28T02:57:27.87Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRtUrGL784WTKpR8yFTFSheX/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIbw5neVqmvTe2ZHWbjEoKdj"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    }, {
      "id" : "TR3BQY5tKaRwvi6M5yjEP1m2",
      "amount" : 385892,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "53d4391a-24de-4916-beff-b77d15f348df",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 38589,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:23.15Z",
      "updated_at" : "2017-11-28T02:57:23.24Z",
      "idempotency_id" : "8a927c4aea884485802a65644d5d899f",
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TR3BQY5tKaRwvi6M5yjEP1m2/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    }, {
      "id" : "TRowh7R9qyzTEezyCrwkWmoV",
      "amount" : 376232,
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "state" : "PENDING",
      "trace_id" : "a821a477-c002-4c15-b15f-40b4e22ce733",
      "currency" : "USD",
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
      "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
      "ready_to_settle_at" : null,
      "fee_profile" : null,
      "fee" : 37623,
      "statement_descriptor" : "LAC*PETES COFFEE",
      "type" : "DEBIT",
      "messages" : [ ],
      "raw" : null,
      "created_at" : "2017-11-28T02:57:22.22Z",
      "updated_at" : "2017-11-28T02:57:22.32Z",
      "idempotency_id" : null,
      "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
      "subtype" : "API",
      "_links" : {
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        },
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV"
        },
        "payment_instruments" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/payment_instruments"
        },
        "merchant_identity" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
        },
        "reversals" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals"
        },
        "fees" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/fees"
        },
        "disputes" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/disputes"
        },
        "source" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
        },
        "destination" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/transfers?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/transfers`
## Update a Transfer

```shell
curl https://lacore-sandbox.finixpayments.com/transfers/TRowh7R9qyzTEezyCrwkWmoV/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -X PUT \
    -d '
	{
	    "tags": {
	        "order_number": "12121212"
	    }
	}'

```
```java
import io.lacore.payments.forms.*;
import io.lacore.payments.views.*;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .tags(ImmutableMap.of("order_number", "12121212"))
        .build();

Maybe<Transfer> response = api.transfers.post(form);

Maybe<Transfer> response = api.transfers.id("TRowh7R9qyzTEezyCrwkWmoV").put(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to update transfer");
}
Transfer transfer = response.view();

```
```php
<?php

```
```python


from lacore.resources import Transfer
transfer = Transfer.get(id="TRowh7R9qyzTEezyCrwkWmoV")

refund = transfer.reverse(**
                  {
                  "refund_amount" : 100
                  }
                )
refund.tags["order_number"] = "12121212"
refund.save()

```
```ruby
transfer = Lacore::Transfer.retrieve(:id=>"TRowh7R9qyzTEezyCrwkWmoV")

refund = transfer.reverse(100)
refund.tags = {"order_number"=> "12121212"}
refund.save

```
> Example Response:

```json
{
  "id" : "TRowh7R9qyzTEezyCrwkWmoV",
  "amount" : 376232,
  "tags" : {
    "order_number" : "12121212"
  },
  "state" : "PENDING",
  "trace_id" : "a821a477-c002-4c15-b15f-40b4e22ce733",
  "currency" : "USD",
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "source" : "PIqmjxTeuN8udXNdFTqkx1zf",
  "destination" : "PIkNQbiLoyhnEE6Wt9euHugq",
  "ready_to_settle_at" : null,
  "fee_profile" : null,
  "fee" : 37623,
  "statement_descriptor" : "LAC*PETES COFFEE",
  "type" : "DEBIT",
  "messages" : [ ],
  "raw" : null,
  "created_at" : "2017-11-28T02:57:22.22Z",
  "updated_at" : "2017-11-28T02:57:59.18Z",
  "idempotency_id" : null,
  "merchant_identity" : "IDwdNkeVs6byLWrz3Fe44kDv",
  "subtype" : "API",
  "_links" : {
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    },
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV"
    },
    "payment_instruments" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/payment_instruments"
    },
    "merchant_identity" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/identities/IDwdNkeVs6byLWrz3Fe44kDv"
    },
    "reversals" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/reversals"
    },
    "fees" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/fees"
    },
    "disputes" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/transfers/TRowh7R9qyzTEezyCrwkWmoV/disputes"
    },
    "source" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIqmjxTeuN8udXNdFTqkx1zf"
    },
    "destination" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/payment_instruments/PIkNQbiLoyhnEE6Wt9euHugq"
    }
  }
}
```

#### HTTP Request

`PUT https://lacore-sandbox.finixpayments.com/transfers/:TRANSFER_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:TRANSFER_ID | ID of the `Transfer`


#### Request Parameters
Field | Type | Description
----- | ---- | -----------
tags | *object*, **required** | Key value pair for annotating custom meta data (e.g. order numbers)

# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the Lacore API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.


## Create a Webhook
```shell

curl https://lacore-sandbox.finixpayments.com/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244 \
    -d '
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                '

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.forms.WebhookForm;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Webhook;

WebhookForm form = WebhookForm.builder()
    .url("http://requestb.in/1jb5zu11")
    .build();

Maybe<Webhook> request = api.webhooks.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create Webhook");
}
Webhook webhookView = request.view();

```
```php
<?php
use Lacore\Resources\Webhook;

$webhook = new Webhook(
                    array(
                    "url" => "http=>//requestb.in/1jb5zu11"
                    )
                );
$webhook = $webhook->save();

```
```python


from lacore.resources import Webhook
webhook = Webhook(**
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                ).save()

```
```ruby
webhook = Lacore::Webhook.new(
                    {
                    "url" => "http=>//requestb.in/1jb5zu11"
                    }
                ).save
```
> Example Response:

```json
{
  "id" : "WHaAAQbfvPeo5iVN36H26rQK",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "created_at" : "2017-11-28T02:57:05.18Z",
  "updated_at" : "2017-11-28T02:57:05.18Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/webhooks/WHaAAQbfvPeo5iVN36H26rQK"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### HTTP Request

`POST https://lacore-sandbox.finixpayments.com/webhooks`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
url | *string*, **required** | The HTTP or HTTPS url where the callbacks will be sent via POST request (max 120 characters)


## Fetch a Webhook

```shell



curl https://lacore-sandbox.finixpayments.com/webhooks/WHaAAQbfvPeo5iVN36H26rQK \
    -H "Content-Type: application/vnd.json+api" \
    -u USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244


```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.views.Webhook;

Maybe<Webhook> response = api.webhooks
        .id("WHaAAQbfvPeo5iVN36H26rQK")
        .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Webhook");
}
Webhook webhookView = response.view();

```
```php
<?php
use Lacore\Resources\Webhook;

$webhook = Webhook::retrieve('WHaAAQbfvPeo5iVN36H26rQK');



```
```python


from lacore.resources import Webhook
webhook = Webhook.get(id="WHaAAQbfvPeo5iVN36H26rQK")

```
```ruby
webhook = Lacore::Webhook.retrieve(:id=> "WHaAAQbfvPeo5iVN36H26rQK")


```
> Example Response:

```json
{
  "id" : "WHaAAQbfvPeo5iVN36H26rQK",
  "url" : "http://requestb.in/1jb5zu11",
  "enabled" : true,
  "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
  "created_at" : "2017-11-28T02:57:05.19Z",
  "updated_at" : "2017-11-28T02:57:05.19Z",
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/webhooks/WHaAAQbfvPeo5iVN36H26rQK"
    },
    "application" : {
      "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
    }
  }
}
```

#### HTTP Request

`GET https://lacore-sandbox.finixpayments.com/webhooks/:WEBHOOK_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:WEBHOOK_ID | ID of the `Webhook`
## List all Webhooks

```shell
curl https://lacore-sandbox.finixpayments.com/webhooks/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  USed8KcvU1NcqCjL2gecsdE7:6bb7691d-eb11-4fba-a65e-c8f352dca244

```
```java
import io.lacore.payments.ApiClient;
import io.lacore.payments.interfaces.ApiError;
import io.lacore.payments.interfaces.Maybe;
import io.lacore.payments.lib.Page;
import io.lacore.payments.views.Webhook;

Maybe<Page<Webhook>> response = api.webhooks.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Webhooks");
}

Page<Webhook> page = response.view();

```
```php
<?php
use Lacore\Resources\Webhook;

$webhooks = Webhook::getPagination("/webhooks");


```
```python


from lacore.resources import Webhook
webhooks = Webhook.get()

```
```ruby
webhooks = Lacore::Webhook.retrieve
```
> Example Response:

```json
{
  "_embedded" : {
    "webhooks" : [ {
      "id" : "WHaAAQbfvPeo5iVN36H26rQK",
      "url" : "http://requestb.in/1jb5zu11",
      "enabled" : true,
      "application" : "AP3VrWhf2cFx5QakKk5UrT3f",
      "created_at" : "2017-11-28T02:57:05.19Z",
      "updated_at" : "2017-11-28T02:57:05.19Z",
      "_links" : {
        "self" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/webhooks/WHaAAQbfvPeo5iVN36H26rQK"
        },
        "application" : {
          "href" : "https://lacore-sandbox.finixpayments.com:443/applications/AP3VrWhf2cFx5QakKk5UrT3f"
        }
      }
    } ]
  },
  "_links" : {
    "self" : {
      "href" : "https://lacore-sandbox.finixpayments.com/webhooks?offset=0&limit=20&sort=created_at,desc"
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

`GET https://lacore-sandbox.finixpayments.com/webhooks`
    

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
```ruby
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

### Created Instrument Update

```javascript
{
  "type": "updated",
  "entity": "instrument_update",
  "occurred_at": "2017-08-14T14:17:43.004",
  "_embedded": {
    "instrument_updates": [{
      "trace_id": "FNXa2UvnrWMA6h4uER2F3wcg",
      "application": "APuEebjbpT8Baz8VqERaEx3z",
      "updated_at": "2017-08-14T14:17:42.97Z",
      "payment_instrument": "PIrgiJ1KtZVaT4dqDeDkveYh",
      "merchant": "MUxtD9KaVh1Ax5WRKBQZntPX",
      "messages": [
        "No match found"
      ],
      "created_at": "2017-08-09T23:58:05.74Z",
      "id": "IUkE7oida5Jupzd471HPkjqu",
      "state": "FAILED"
    }]
  }
}
```

### Update Payment Instrument

```javascript
{
  "type" : "updated",
  "entity" : "instrument",
  "occurred_at" : "2017-08-04T23:52:49.759",
  "_embedded" : {
    "instruments" : [ {
      "updated_at" : "2017-08-04T23:52:49.70Z",
      "identity" : "IDcVVAdGYhiaq4Xka6PVHYVD",
      "fingerprint" : "FPR316679720",
      "created_at" : "2017-05-23T18:52:54.64Z",
      "currency" : "USD",
      "id" : "PIc2DqWRD8wiNYLqQBMAYjku",
      "instrument_type" : "PAYMENT_CARD",
      "type" : "PAYMENT_CARD",
      "tags" : {
        "driver" : "123"
      }
    } ]
  }
}
```

