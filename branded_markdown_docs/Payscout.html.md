---
title: Payscout API Reference

language_tabs:
  - shell: cURL
  - php: PHP
  - ruby: Ruby
  - python: Python
  - csharp: C#
  - java: Java
  - perl: Perl

includes:
  - errors

search: true
---

# Guides

## Getting Started

```shell
# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```

```php
// To get started follow these steps:
// Download the Payscout PHP Client
// Download composer (https://getcomposer.org/download)
// Install the dependencies in the composer.json file or download locally with: composer install --prefer-source --no-interaction
// Configure the API as shown below
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();
```

```ruby

```

```python

```

```csharp

```

```java

```


```perl

```

This guide will demonstrate the main workflows for utilizing the Payscout Payments API for platforms and marketplaces. We have language bindings in cURL, PHP, Ruby, Python, C#, Java and Perl! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

To communicate with the Payscout API you'll need to authenticate your requests with a username and password. For the sandbox environment you may use the credentials listed below or you can supply your own.

- Username: `USbfbQ3A7GvXpjSpc9stwhPq`

- Password: `affbfbad-0cab-4033-9509-d584834a4bc0`

We have also included a seperate set of credentials associated with the same application.
- Username: `USh83p26KBJS9wMZCKa7vygi`

- Password: `c16f70d1-c957-48a5-beec-ea83d829a915`

To access the the Merchant dashboards:
- Username: `USqrw55NccLqoV6W9q3wpwsW`
- Password: `39221b3b-0f82-443f-acb0-6ef4aa24eeba`


You should also know your Application ID. An Application, also referred as an "App", is a resource that represents your web App or any service that connects customers (i.e. buyers) and merchants (i.e. sellers). For the sandbox environment you may use the following ID:

- App ID: `APsZ4K3jRswSZ7JpRChLf6dq`


## Create an Identity for a Merchant
```shell
curl https://payscout-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
        \"tags\": {
            \"key\": \"value\"
        },
        \"entity\": {
            \"first_name\": \"dwayne\",
            \"last_name\": \"Sunkhronos\",
            \"phone\": \"1234567890\",
            \"personal_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 7\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"business_name\": \"business inc\",
            \"business_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 8\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"tax_id\": \"5779\",
            \"business_type\": \"LIMITED_LIABILITY_COMPANY\",
            \"business_phone\": \"+1 (408) 756-4497\",
            \"dob\": {
                \"year\": 1978,
                \"day\": 27,
                \"month\": 6
            },
            \"business_tax_id\": \"123456789\",
            \"doing_business_as\": \"doingBusinessAs\",
            \"email\": \"user@example.org\"
        }
}"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = new Identity(array(
    "entity"=> array(
        "business_type"=> "LIMITED_LIABILITY_COMPANY",
        "business_phone"=> "+1 (408) 756-4497",
        "first_name"=> "dwayne",
        "last_name"=> "Sunkhronos",
        "dob"=> array(
            "month"=> 5,
            "day"=> 27,
            "year"=> 1978
        ),
        "business_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 8",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "doing_business_as"=> "doingBusinessAs",
        "phone"=> "1234567890",
        "personal_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 7",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "business_name"=> "business inc",
        "business_tax_id"=> "123456789",
        "email"=> "user@example.org",
        "tax_id"=> "5779"
    )
));
$identity = $identity->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "tags": {
    "key": "value"
  },
  "entity": {
    "last_name": "Sunkhronos",
    "phone": "1234567890",
    "personal_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 7",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "business_name": "business inc",
    "business_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 8",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "tax_id": "5779",
    "business_type": "LIMITED_LIABILITY_COMPANY",
    "business_phone": "+1 (408) 756-4497",
    "first_name": "dwayne",
    "dob": {
      "year": 1978,
      "day": 27,
      "month": 5
    },
    "business_tax_id": "123456789",
    "doing_business_as": "doingBusinessAs",
    "email": "user@example.org"
  }
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities', values, headers
puts response

```

```python
from urllib2 import Request, urlopen

values = """
  {
    "tags": {
      "key": "value"
    },
    "entity": {
      "last_name": "Sunkhronos",
      "phone": "1234567890",
      "personal_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 7",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "business_name": "business inc",
      "business_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 8",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "tax_id": "5779",
      "business_type": "LIMITED_LIABILITY_COMPANY",
      "business_phone": "+1 (408) 756-4497",
      "first_name": "dwayne",
      "dob": {
        "year": 1978,
        "day": 27,
        "month": 5
      },
      "business_tax_id": "123456789",
      "doing_business_as": "doingBusinessAs",
      "email": "user@example.org"
    }
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }}");
Response response = client.target("https://payscout-staging.finix.io/identities")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));

```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities", Content => $data);

print $response->as_string;

```

```c#
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"tags\": {    \"key\": \"value\"  },  \"entity\": {    \"last_name\": \"Sunkhronos\",    \"phone\": \"1234567890\",    \"personal_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 7\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"business_name\": \"business inc\",    \"business_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 8\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"tax_id\": \"5779\",    \"business_type\": \"LIMITED_LIABILITY_COMPANY\",    \"business_phone\": \"+1 (408) 756-4497\",    \"first_name\": \"dwayne\",    \"dob\": {      \"year\": 1978,      \"day\": 27,      \"month\": 5    },    \"business_tax_id\": \"123456789\",    \"doing_business_as\": \"doingBusinessAs\",    \"email\": \"user@example.org\"  }}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }

```

> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-04-29T16:39:35.28Z", 
	    "updated_at": "2016-04-29T16:39:35.28Z", 
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
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "doingBusinessAs", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "business inc", 
	        "tax_id_provided": true, 
	        "email": "user@example.org"
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/authorizations"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "settlements": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/disputes"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications"
	        }, 
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants"
	        }
	    }, 
	    "default_statement_descriptor": null, 
	    "id": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Before we can charge a card we need to create an Identity resource. An Identity represents a person or business. In this case, the Identity will represent the merchant (i.e. seller). Let's create one now.You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Perform an Identity Verification

```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
         \"tags\": {
           \"name\": \"test-verification\"
         },
         \"processor\": \"DUMMY_V1\",
         \"identity\": null,
         \"instrument\": null,
         \"merchant\": null
       }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;
use Payscout\Resources\Verification;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1");
$verification = $identity->verifyOn($payload);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "tags": {
    "name": "test-verification"
  },
  "processor": "DUMMY_V1",
  "identity": null,
  "instrument": null,
  "merchant": null
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications', values, headers
puts response

```

```python
from urllib2 import Request, urlopen

values = """
  {
    "tags": {
      "name": "test-verification"
    },
    "processor": "DUMMY_V1",
    "identity": null,
    "instrument": null,
    "merchant": null
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"tags\": {    \"name\": \"test-verification\"  },  \"processor\": \"DUMMY_V1\",  \"identity\": null,  \"instrument\": null,  \"merchant\": null}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities/{identity_id}/verifications", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'tags': {    'name': 'test-verification'  },  'processor': 'DUMMY_V1',  'identity': null,  'instrument': null,  'merchant': null}");
Response response = client.target("https://payscout-staging.finix.io/identities/{identity_id}/verifications")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'tags': {    'name': 'test-verification'  },  'processor': 'DUMMY_V1',  'identity': null,  'instrument': null,  'merchant': null};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications", Content => $data);

print $response->as_string;
```

> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-04-29T16:39:40.71Z", 
	    "messages": [], 
	    "updated_at": "2016-04-29T16:39:40.74Z", 
	    "id": "VIt9Y4eZdHbpundYsogcT2kN", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "external_trace_id": "b49296f9-af98-4b75-a335-0bd29547296d", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Before, being able to process funds to this seller we will need to perform an identity verification to underwrite them as a Merchant. Only underwritten Identities can be paid out per KYC regulations.

## Simulate Underwriting the Merchant

```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
     \"processor\": \"DUMMY_V1\"
     }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1");
$merchant = $identity->provisionMerchantOn($payload);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "processor": "DUMMY_V1"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "processor": "DUMMY_V1"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"processor\": \"DUMMY_V1\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities/{identity_id}/merchants", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'processor': 'DUMMY_V1'}");
Response response = client.target("https://payscout-staging.finix.io/identities/{identity_id}/merchants")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'processor': 'DUMMY_V1'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants", Content => $data);

print $response->as_string;
```

> Example Response:

```json

	{
	    "created_at": "2016-04-29T16:39:38.29Z", 
	    "updated_at": "2016-04-29T16:39:38.29Z", 
	    "id": "MU3CvPexfzmnKt9GDh4jtYCx", 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/merchants/MU3CvPexfzmnKt9GDh4jtYCx"
	        }, 
	        "merchant_profile": {
	            "href": "https://payscout-staging.finix.io/merchant_profiles/MPwYe3fNHZ5XP17nTGZwP7Bh"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/merchants/MU3CvPexfzmnKt9GDh4jtYCx/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "verification": {
	            "href": "https://payscout-staging.finix.io/verifications/VI9bpbAsAHoVNzWm5GkC2TAw"
	        }
	    }, 
	    "verification": "VI9bpbAsAHoVNzWm5GkC2TAw", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPwYe3fNHZ5XP17nTGZwP7Bh", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Once the Identity has been verified, Payscout will need to review the submitted information and finally underwrite the Identity. You will receive an event fired off to your webhook notifying you when the Merchant has been approved. To simulate this step run this request so that they can begin processing funds.

## Create an Identity for a Buyer (i.e. buyer)

```shell
curl https://payscout-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
        \"tags\": {
            \"key\": \"value\"
        },
        \"entity\": {
            \"first_name\": \"dwayne\",
            \"last_name\": \"Sunkhronos\",
            \"phone\": \"1234567890\",
            \"personal_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 7\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"business_name\": \"business inc\",
            \"business_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 8\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"tax_id\": \"5779\",
            \"business_type\": \"LIMITED_LIABILITY_COMPANY\",
            \"business_phone\": \"+1 (408) 756-4497\",
            \"dob\": {
                \"year\": 1978,
                \"day\": 27,
                \"month\": 6
            },
            \"business_tax_id\": \"123456789\",
            \"doing_business_as\": \"doingBusinessAs\",
            \"email\": \"user@example.org\"
        }
}"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = new Identity(array(
    "entity"=> array(
        "business_type"=> "LIMITED_LIABILITY_COMPANY",
        "business_phone"=> "+1 (408) 756-4497",
        "first_name"=> "dwayne",
        "last_name"=> "Sunkhronos",
        "dob"=> array(
            "month"=> 5,
            "day"=> 27,
            "year"=> 1978
        ),
        "business_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 8",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "doing_business_as"=> "doingBusinessAs",
        "phone"=> "1234567890",
        "personal_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 7",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "business_name"=> "business inc",
        "business_tax_id"=> "123456789",
        "email"=> "user@example.org",
        "tax_id"=> "5779"
    )
));
$identity = $identity->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "tags": {
    "key": "value"
  },
  "entity": {
    "last_name": "Sunkhronos",
    "phone": "1234567890",
    "personal_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 7",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "business_name": "business inc",
    "business_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 8",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "tax_id": "5779",
    "business_type": "LIMITED_LIABILITY_COMPANY",
    "business_phone": "+1 (408) 756-4497",
    "first_name": "dwayne",
    "dob": {
      "year": 1978,
      "day": 27,
      "month": 5
    },
    "business_tax_id": "123456789",
    "doing_business_as": "doingBusinessAs",
    "email": "user@example.org"
  }
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities', values, headers
puts response

```

```python
from urllib2 import Request, urlopen

values = """
  {
    "tags": {
      "key": "value"
    },
    "entity": {
      "last_name": "Sunkhronos",
      "phone": "1234567890",
      "personal_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 7",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "business_name": "business inc",
      "business_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 8",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "tax_id": "5779",
      "business_type": "LIMITED_LIABILITY_COMPANY",
      "business_phone": "+1 (408) 756-4497",
      "first_name": "dwayne",
      "dob": {
        "year": 1978,
        "day": 27,
        "month": 5
      },
      "business_tax_id": "123456789",
      "doing_business_as": "doingBusinessAs",
      "email": "user@example.org"
    }
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }}");
Response response = client.target("https://payscout-staging.finix.io/identities")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));

```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities", Content => $data);

print $response->as_string;

```

```c#
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"tags\": {    \"key\": \"value\"  },  \"entity\": {    \"last_name\": \"Sunkhronos\",    \"phone\": \"1234567890\",    \"personal_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 7\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"business_name\": \"business inc\",    \"business_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 8\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"tax_id\": \"5779\",    \"business_type\": \"LIMITED_LIABILITY_COMPANY\",    \"business_phone\": \"+1 (408) 756-4497\",    \"first_name\": \"dwayne\",    \"dob\": {      \"year\": 1978,      \"day\": 27,      \"month\": 5    },    \"business_tax_id\": \"123456789\",    \"doing_business_as\": \"doingBusinessAs\",    \"email\": \"user@example.org\"  }}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }

```

> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-04-29T16:39:35.28Z", 
	    "updated_at": "2016-04-29T16:39:35.28Z", 
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
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "doingBusinessAs", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "business inc", 
	        "tax_id_provided": true, 
	        "email": "user@example.org"
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/authorizations"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "settlements": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/disputes"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications"
	        }, 
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants"
	        }
	    }, 
	    "default_statement_descriptor": null, 
	    "id": "IDwW594hgk6No6rThnhCVeCq"
	}
```
This next step should sound familiar. Let's create an Identity to represent the buyer. You'll want to store the ID of the newly created Identity resource as you'll reference it later.

## Create a Payment Instrument (i.e. card)

```shell
curl https://payscout-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
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
       \"identity\": \"IDwW594hgk6No6rThnhCVeCq\"
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\PaymentInstrument;

$card = new PaymentInstrument(array(
    "name"=> array(
        "first_name"=> "Joe",
        "last_name"=> "Doe",
        "full_name"=> "Joe Doe"
    ),
    "type"=> "PAYMENT_CARD",
    "tags"=> null,
    "expiration_month"=> 12,
    "expiration_year"=> 2017,
    "number"=> "4111 1111 1111 1111",
    "security_code"=> "231",
    "address"=> null,
    "identity" => IDwW594hgk6No6rThnhCVeCq,
    ));
$card = $card->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "identity": "IDwW594hgk6No6rThnhCVeCq",
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
  "type": "PAYMENT_CARD"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/payment_instruments', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "identity": "IDwW594hgk6No6rThnhCVeCq",
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
    "type": "PAYMENT_CARD"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/payment_instruments', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"expiration_year\": 2020,  \"number\": \"4242424242424242\",  \"expiration_month\": 12,  \"address\": {    \"city\": \"San Mateo\",    \"country\": \"USA\",    \"region\": \"CA\",    \"line2\": \"Apartment 7\",    \"line1\": \"741 Douglass St\",    \"postal_code\": \"94114\"  },  \"security_code\": \"112\",  \"type\": \"PAYMENT_CARD\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("payment_instruments", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'expiration_year': 2020,  'number': '4242424242424242',  'expiration_month': 12,  'address': {    'city': 'San Mateo',    'country': 'USA',    'region': 'CA',    'line2': 'Apartment 7',    'line1': '741 Douglass St',    'postal_code': '94114'  },  'security_code': '112',  'type': 'PAYMENT_CARD'}");
Response response = client.target("https://payscout-staging.finix.io/payment_instruments")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'expiration_year': 2020,  'number': '4242424242424242',  'expiration_month': 12,  'address': {    'city': 'San Mateo',    'country': 'USA',    'region': 'CA',    'line2': 'Apartment 7',    'line1': '741 Douglass St',    'postal_code': '94114'  },  'security_code': '112',  'type': 'PAYMENT_CARD'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/payment_instruments", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "instrument_type": "PAYMENT_CARD", 
	    "card_type": "UNKNOWN", 
	    "name": "dwayne Sunkhronos", 
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
	    "updated_at": "2016-04-29T16:39:42.51Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR967679505", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDgKiqrJNBaLRWSjs6sWrKwu"
	        }
	    }, 
	    "created_at": "2016-04-29T16:39:42.51Z", 
	    "id": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "identity": "IDgKiqrJNBaLRWSjs6sWrKwu"
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
curl https://payscout-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
       \"currency\": \"USD\",
       \"amount\": 100,
       \"fee\": 10,
       \"processor\": \"DUMMY_V1\",
       \"statement_descriptor\": \"Bob's Burgers Order 123\",
       \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",
       \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\"
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Transfer;
$payload = array(
    "processor" => "DUMMY_V1",
    "amount" => 100,
    "fee" => 10,
    "currency" => "USD",
    "merchant_identity" => "IDwW594hgk6No6rThnhCVeCq",
    "source" => "PItBoYHhbKNroSRmUgB5MXjc");
$debit = new Transfer($payload);
$debit = $debit->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

 values = '{
   "currency": "USD",
   "source": "PItBoYHhbKNroSRmUgB5MXjc",
   "processor": "DUMMY_V1",
   "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
   "amount": 100,
   "fee" => 100
 }'

 headers = {
   :content_type => 'application/vnd.json+api',
   :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
 }

 response = RestClient.post 'https://payscout-staging.finix.io/transfers', values, headers
 puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "currency": "USD",
    "amount": 100,
    "fee": 10,
    "processor": "DUMMY_V1",
    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
    "source": "PItBoYHhbKNroSRmUgB5MXjc"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/transfers', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"currency\": \"USD\",  \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\",  \"processor\": \"DUMMY_V1\",  \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"amount\": 100}",  \"fee\": 10}",System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("transfers", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'currency': 'USD',  'source': 'PItBoYHhbKNroSRmUgB5MXjc',  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'amount': 100, 'fee': 10}");
Response response = client.target("https://payscout-staging.finix.io/transfers")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'currency': 'USD',  'source': 'PItBoYHhbKNroSRmUgB5MXjc',  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'amount': 100, 'fee': 10};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/transfers", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "destination": "PIht64noXsMri4GNoQETnhce", 
	    "state": "PENDING", 
	    "updated_at": "2016-04-29T16:39:44.82Z", 
	    "created_at": "2016-04-29T16:39:44.31Z", 
	    "tags": {}, 
	    "trace_id": "3ee62990-6d2f-45da-9250-06abe4e5c56f", 
	    "statement_descriptor": "PSC*PAYSCOUT", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG"
	        }, 
	        "destination": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PIht64noXsMri4GNoQETnhce"
	        }, 
	        "source": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/disputes"
	        }
	    }, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "type": "DEBIT", 
	    "id": "TR9T6bjbVvvRo1JNkmPQPqiG"
	}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.



## Reverse the Transfer (i.e. issue a refund)


```shell
curl https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d  "{
       \"refund_amount\": 100
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Transfer;

$debit = Transfer::retrieve("TR9T6bjbVvvRo1JNkmPQPqiG");
$refund = $debit->reverse(100);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "refund_amount": 100
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "refund_amount": 100
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"refund_amount\": 100}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("transfers/{transfer_id}/reversals", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'refund_amount': 100}");
Response response = client.target("https://payscout-staging.finix.io/transfers/{transfer_id}/reversals")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'refund_amount': 100};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals", Content => $data);

print $response->as_string;

```


> Example Response:

```json

	{
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "destination": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "state": "PENDING", 
	    "updated_at": "2016-04-29T16:40:49.46Z", 
	    "created_at": "2016-04-29T16:40:49.33Z", 
	    "tags": {}, 
	    "trace_id": "6da001f4-281b-44d7-aa12-ab9640630e34", 
	    "statement_descriptor": "PSC*PAYSCOUT", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/transfers/TR21gB2Yxgov4cLoG4ukESYg"
	        }, 
	        "destination": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "parent": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG"
	        }
	    }, 
	    "source": "PIht64noXsMri4GNoQETnhce", 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "type": "REVERSAL", 
	    "id": "TR21gB2Yxgov4cLoG4ukESYg"
	}
```

What if we need to issue a refund to the buyer? First, you'll need to take the previously stored Transfer ID and interpolate it into the following url path. The amount can be equal to or less than the original debit.

## Settle out funds to a Merchant

```shell
curl https://payscout-staging.finix.io/identities/identity_id/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
        \"identity\": \"IDwW594hgk6No6rThnhCVeCq\",
        \"processor\": \"DUMMY_V1\",
        \"currency\": \"USD\"
        }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Settlement;
use Payscout\Resources\Identity;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1",
    "currency"=>"USD");
$settlement = $identity->createSettlement($payload);
```

```ruby

```

```python

```

```csharp

```


```perl

```

> Example Response:

```json

	{
	    "total_amount": 888958, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-04-29T16:41:55.35Z", 
	    "updated_at": "2016-04-29T16:41:55.43Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "total_fee": 30, 
	    "id": "STpspeSDXZDuVStLupbiT4Hy", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Awesome! Now you know how to charge a card and reverse the debit.

Now you need to settle out the funds to your merchant. To do so you will create a Settlement resource. Each settlement is comprised of all the Transfers that have a SUCCEEDED state and that have not been previously settled out.

# Tokenization.js
To ensure that you remain PCI compliant, please use tokenization.js to tokenize cards and bank accounts. Tokenization.js, keeps you out of the PCI scope by sending sensitive payment information over SSL directly to the Payscout servers.

For a complete example of how to use tokenization.js please refer to this [jsFiddle example](http://jsfiddle.net/rserna2010/9hbny54d/).

<aside class="warning">
Creating payment instruments directly via the API should only be done for testing purposes.
</aside>

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the Payscout API.
</aside>


## Step 1: Include library
To use tokenization.js you will first need to include the library. Please include the script tag as demonstrated to the right.

```html
<script type="text/javascript" src="https://js.verygoodproxy.com/tokenization.1-latest.js"></script>
```

<aside class="notice">
Note that we do not recommend hosting the tokenization.js library locally as doing so prevents important updates.
</aside>

## Step 2: Create a form
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
Before collecting the sensitive payment information, we will need to construct an HTML form for users to input the data.

We have provided a simple example to the right for capturing Payment Instrument data.

## Step 3: Configure and initialize

```javascript
var initTokenization = function() {
  Tokenization.init({
    server: "https://payscout-staging.finix.io",
    applicationId: "APsZ4K3jRswSZ7JpRChLf6dq",
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
We will need to configure the client so that it POSTs to the correct endpoint and associates the Payment Instrument to your application. During the initialization we will also use the JQuery selector method to capture the form data.

### Initialization Fields
Field | Type | Description | Example
----- | ---- | ----------- | -------
server | *string*, **required** |  The base url for the Payscout API| https://payscout-staging.finix.io
applicationId | *string*, **required** | The ID for your Application, also referred to as your App | APsZ4K3jRswSZ7JpRChLf6dq
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

> Example Tokenization Response:
```javascript
{
    "id": "TKmgcL9uhv11re4wk1X9NYYf",
    "fingerprint": "FPR-1392097976",
    "created_at": "2016-03-07T22:27:01.611",
    "updated_at": "2016-03-07T22:27:01.611",
    "instrument_type": "PAYMENT_CARD"
}
```

Finally we will need to register a click event that fires when our users submit the form and define a callback for handling the tokenization.js response. We have included an example to the right.

## Step 5: Send token to your back-end server for storing

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

Great now that you have created a token you will want to store that ID to utilize the token in the future. To do this you will need to send the ID from your front-end client to your back-end server. You can expand on the callback that you previously created like so:

## Step 6: Associate to an Identity


```shell
curl https://payscout-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
       \"token\": \"TKmgcL9uhv11re4wk1X9NYYf\",
       \"type\": \"token\",
       \"identity\": \"IDwW594hgk6No6rThnhCVeCq\"
       }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\PaymentInstrument;

$card = new PaymentInstrument(array(
    "type"=> "token",
    "token"=> "TKmgcL9uhv11re4wk1X9NYYf",
    "identity" => IDwW594hgk6No6rThnhCVeCq
    ));
$card = $card->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "identity": "IDwW594hgk6No6rThnhCVeCq",
  "token": "TKmgcL9uhv11re4wk1X9NYYf",
  "type": "token"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/payment_instruments', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "identity": "IDwW594hgk6No6rThnhCVeCq",
    "token": "TKmgcL9uhv11re4wk1X9NYYf",
    "type": "token"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/payment_instruments', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"token\": \"TKmgcL9uhv11re4wk1X9NYYf\", \"type\": \"token\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("payment_instruments", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'token': "TKmgcL9uhv11re4wk1X9NYYf",  'type': 'token'}");
Response response = client.target("https://payscout-staging.finix.io/payment_instruments")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'type': "token",  'token': 'TKmgcL9uhv11re4wk1X9NYYf'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/payment_instruments", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "instrument_type": "TOKEN", 
	    "tags": {}, 
	    "created_at": "2016-04-29T16:41:57.97Z", 
	    "updated_at": "2016-04-29T16:41:57.97Z", 
	    "token": "TKmgcL9uhv11re4wk1X9NYYf", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI8TM9KdKq3x6kgj9GQ4iiP7/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI8TM9KdKq3x6kgj9GQ4iiP7"
	        }, 
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI8TM9KdKq3x6kgj9GQ4iiP7/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI8TM9KdKq3x6kgj9GQ4iiP7/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "fingerprint": "FPR863770462", 
	    "id": "PI8TM9KdKq3x6kgj9GQ4iiP7", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```
Before you can use the newly tokenized card or bank account you will need to associate it with an Identity. To do this you must make an authenticated POST request to `https://payscout-staging.finix.io/payment_instruments` like demonstrated to the right.

#### HTTP Request

`POST https://payscout-staging.finix.io/payment_instruments`

# Identities
An Identity resource represents a business or person. Payment Instrument resources may be associated to an Identity.

## Create a New Identity

```shell
curl https://payscout-staging.finix.io/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
        \"tags\": {
            \"key\": \"value\"
        },
        \"entity\": {
            \"first_name\": \"dwayne\",
            \"last_name\": \"Sunkhronos\",
            \"phone\": \"1234567890\",
            \"personal_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 7\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"business_name\": \"business inc\",
            \"business_address\": {
                \"city\": \"San Mateo\",
                \"country\": \"USA\",
                \"region\": \"CA\",
                \"line2\": \"Apartment 8\",
                \"line1\": \"741 Douglass St\",
                \"postal_code\": \"94114\"
            },
            \"tax_id\": \"5779\",
            \"business_type\": \"LIMITED_LIABILITY_COMPANY\",
            \"business_phone\": \"+1 (408) 756-4497\",
            \"dob\": {
                \"year\": 1978,
                \"day\": 27,
                \"month\": 6
            },
            \"business_tax_id\": \"123456789\",
            \"doing_business_as\": \"doingBusinessAs\",
            \"email\": \"user@example.org\"
        }
}"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = new Identity(array(
    "entity"=> array(
        "business_type"=> "LIMITED_LIABILITY_COMPANY",
        "business_phone"=> "+1 (408) 756-4497",
        "first_name"=> "dwayne",
        "last_name"=> "Sunkhronos",
        "dob"=> array(
            "month"=> 5,
            "day"=> 27,
            "year"=> 1978
        ),
        "business_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 8",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "doing_business_as"=> "doingBusinessAs",
        "phone"=> "1234567890",
        "personal_address"=> array(
            "city"=> "San Mateo",
            "country"=> "USA",
            "region"=> "CA",
            "line2"=> "Apartment 7",
            "line1"=> "741 Douglass St",
            "postal_code"=> "94114"
        ),
        "business_name"=> "business inc",
        "business_tax_id"=> "123456789",
        "email"=> "user@example.org",
        "tax_id"=> "5779"
    )
));
$identity = $identity->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "tags": {
    "key": "value"
  },
  "entity": {
    "last_name": "Sunkhronos",
    "phone": "1234567890",
    "personal_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 7",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "business_name": "business inc",
    "business_address": {
      "city": "San Mateo",
      "country": "USA",
      "region": "CA",
      "line2": "Apartment 8",
      "line1": "741 Douglass St",
      "postal_code": "94114"
    },
    "tax_id": "5779",
    "business_type": "LIMITED_LIABILITY_COMPANY",
    "business_phone": "+1 (408) 756-4497",
    "first_name": "dwayne",
    "dob": {
      "year": 1978,
      "day": 27,
      "month": 5
    },
    "business_tax_id": "123456789",
    "doing_business_as": "doingBusinessAs",
    "email": "user@example.org"
  }
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities', values, headers
puts response

```

```python
from urllib2 import Request, urlopen

values = """
  {
    "tags": {
      "key": "value"
    },
    "entity": {
      "last_name": "Sunkhronos",
      "phone": "1234567890",
      "personal_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 7",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "business_name": "business inc",
      "business_address": {
        "city": "San Mateo",
        "country": "USA",
        "region": "CA",
        "line2": "Apartment 8",
        "line1": "741 Douglass St",
        "postal_code": "94114"
      },
      "tax_id": "5779",
      "business_type": "LIMITED_LIABILITY_COMPANY",
      "business_phone": "+1 (408) 756-4497",
      "first_name": "dwayne",
      "dob": {
        "year": 1978,
        "day": 27,
        "month": 5
      },
      "business_tax_id": "123456789",
      "doing_business_as": "doingBusinessAs",
      "email": "user@example.org"
    }
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }}");
Response response = client.target("https://payscout-staging.finix.io/identities")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));

```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'tags': {    'key': 'value'  },  'entity': {    'last_name': 'Sunkhronos',    'phone': '1234567890',    'personal_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 7',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'business_name': 'business inc',    'business_address': {      'city': 'San Mateo',      'country': 'USA',      'region': 'CA',      'line2': 'Apartment 8',      'line1': '741 Douglass St',      'postal_code': '94114'    },    'tax_id': '5779',    'business_type': 'LIMITED_LIABILITY_COMPANY',    'business_phone': '+1 (408) 756-4497',    'first_name': 'dwayne',    'dob': {      'year': 1978,      'day': 27,      'month': 5    },    'business_tax_id': '123456789',    'doing_business_as': 'doingBusinessAs',    'email': 'user@example.org'  }};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities", Content => $data);

print $response->as_string;

```

```c#
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"tags\": {    \"key\": \"value\"  },  \"entity\": {    \"last_name\": \"Sunkhronos\",    \"phone\": \"1234567890\",    \"personal_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 7\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"business_name\": \"business inc\",    \"business_address\": {      \"city\": \"San Mateo\",      \"country\": \"USA\",      \"region\": \"CA\",      \"line2\": \"Apartment 8\",      \"line1\": \"741 Douglass St\",      \"postal_code\": \"94114\"    },    \"tax_id\": \"5779\",    \"business_type\": \"LIMITED_LIABILITY_COMPANY\",    \"business_phone\": \"+1 (408) 756-4497\",    \"first_name\": \"dwayne\",    \"dob\": {      \"year\": 1978,      \"day\": 27,      \"month\": 5    },    \"business_tax_id\": \"123456789\",    \"doing_business_as\": \"doingBusinessAs\",    \"email\": \"user@example.org\"  }}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }

```

> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-04-29T16:39:35.28Z", 
	    "updated_at": "2016-04-29T16:39:35.28Z", 
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
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "doingBusinessAs", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "business inc", 
	        "tax_id_provided": true, 
	        "email": "user@example.org"
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/authorizations"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "settlements": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/disputes"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications"
	        }, 
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants"
	        }
	    }, 
	    "default_statement_descriptor": null, 
	    "id": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`POST https://payscout-staging.finix.io/identities`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}
first_name | *string*, **optional** | First name of the customer or representative of the business | Dwayne
last_name | *string*, **optional** | Last name of the customer or representative of the business | Johnson
tax_id | *string*, **optional** | Last four digits of the Social Security integer of the customer or representative of the business | 5779
day | *integer*, **optional** | Day field of date of birth | 1
month | *integer*, **optional** | Month field of date of birth | 2
year | *string*, **optional** | Year field of date of birth | 1988
phone | *string*, **optional** | Phone integer of the person. Note: There's a separate field for the business phone integer | 1408756449
email | *string*, **optional** | Email address of the customer or representative of the business. | someone@example.com
business_name | *string*, **optional** | Full legal business name if the Identity is a business | Business, Inc
doing_business_as | *string*, **optional** | Name business is using with customers if different from its legal name | Bob's Burgers
business_type | *string*, **optional** | The type of business | INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, LIMITED_PARTNERSHIP, GENERAL_PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY, JOINT_VENTURE
business_tax_id | *string*, **optional** | Employee Identification integer of the business if the customer is a business | 123456789
business_phone | *string*, **optional** | Phone integer of the business | 0123456789
line1 | *string*, **optional** | Street address of the associated card. | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address of the associated card. |  Apt. 3
city | *string*, **optional** | City of the associated card. | San Mateo
region | *string*, **optional** | State of the associated card. | CA
postal_code | *string*, **optional** | Postal of the associated card. | 92704
country | *string*, **optional** | Country of the associated card. | USA


## Retrieve a Identity

```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq', headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("identities/{identity_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/identities/{identity_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq");

print $response->as_string;

```


> Example Response:

```json

	{
	    "tags": {
	        "key": "value"
	    }, 
	    "created_at": "2016-04-29T16:39:35.21Z", 
	    "updated_at": "2016-04-29T16:39:35.21Z", 
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
	        "business_tax_id_provided": true, 
	        "business_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 8", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "doing_business_as": "doingBusinessAs", 
	        "phone": "1234567890", 
	        "discover_mid": null, 
	        "personal_address": {
	            "city": "San Mateo", 
	            "country": "USA", 
	            "region": "CA", 
	            "line2": "Apartment 7", 
	            "line1": "741 Douglass St", 
	            "postal_code": "94114"
	        }, 
	        "business_name": "business inc", 
	        "tax_id_provided": true, 
	        "email": "user@example.org"
	    }, 
	    "_links": {
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/authorizations"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "settlements": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/settlements"
	        }, 
	        "payment_instruments": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/payment_instruments"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/disputes"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications"
	        }, 
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/transfers"
	        }, 
	        "underwriting": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants"
	        }
	    }, 
	    "default_statement_descriptor": null, 
	    "id": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/identities/identity_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


## Underwrite an Identity


```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
     \"processor\": \"DUMMY_V1\"
     }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1");
$merchant = $identity->provisionMerchantOn($payload);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "processor": "DUMMY_V1"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "processor": "DUMMY_V1"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"processor\": \"DUMMY_V1\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities/{identity_id}/merchants", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'processor': 'DUMMY_V1'}");
Response response = client.target("https://payscout-staging.finix.io/identities/{identity_id}/merchants")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'processor': 'DUMMY_V1'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/merchants", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "created_at": "2016-04-29T16:39:38.29Z", 
	    "updated_at": "2016-04-29T16:39:38.29Z", 
	    "id": "MU3CvPexfzmnKt9GDh4jtYCx", 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/merchants/MU3CvPexfzmnKt9GDh4jtYCx"
	        }, 
	        "merchant_profile": {
	            "href": "https://payscout-staging.finix.io/merchant_profiles/MPwYe3fNHZ5XP17nTGZwP7Bh"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/merchants/MU3CvPexfzmnKt9GDh4jtYCx/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "verification": {
	            "href": "https://payscout-staging.finix.io/verifications/VI9bpbAsAHoVNzWm5GkC2TAw"
	        }
	    }, 
	    "verification": "VI9bpbAsAHoVNzWm5GkC2TAw", 
	    "underwriting_state": "PROVISIONING", 
	    "merchant_profile": "MPwYe3fNHZ5XP17nTGZwP7Bh", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Underwrite a previously created Identity resource so that they can act as a seller and have funds disbursed to their bank account.


#### HTTP Request

`POST https://payscout-staging.finix.io/identities/identity_id/merchants`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

# Identity Verifications
Identities (merchants) to whom you wish to pay out must be underwritten as per KYC regulations. Each attempt at verifying an Identity creates a Verification resource.

## Create an Identity Verification


```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
         \"tags\": {
           \"name\": \"test-verification\"
         },
         \"processor\": \"DUMMY_V1\",
         \"identity\": null,
         \"instrument\": null,
         \"merchant\": null
       }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Identity;
use Payscout\Resources\Verification;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1");
$verification = $identity->verifyOn($payload);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "tags": {
    "name": "test-verification"
  },
  "processor": "DUMMY_V1",
  "identity": null,
  "instrument": null,
  "merchant": null
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications', values, headers
puts response

```

```python
from urllib2 import Request, urlopen

values = """
  {
    "tags": {
      "name": "test-verification"
    },
    "processor": "DUMMY_V1",
    "identity": null,
    "instrument": null,
    "merchant": null
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"tags\": {    \"name\": \"test-verification\"  },  \"processor\": \"DUMMY_V1\",  \"identity\": null,  \"instrument\": null,  \"merchant\": null}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("identities/{identity_id}/verifications", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'tags': {    'name': 'test-verification'  },  'processor': 'DUMMY_V1',  'identity': null,  'instrument': null,  'merchant': null}");
Response response = client.target("https://payscout-staging.finix.io/identities/{identity_id}/verifications")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'tags': {    'name': 'test-verification'  },  'processor': 'DUMMY_V1',  'identity': null,  'instrument': null,  'merchant': null};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/verifications", Content => $data);

print $response->as_string;
```




> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-04-29T16:39:40.71Z", 
	    "messages": [], 
	    "updated_at": "2016-04-29T16:39:40.74Z", 
	    "id": "VIt9Y4eZdHbpundYsogcT2kN", 
	    "instrument": null, 
	    "state": "PENDING", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "external_trace_id": "b49296f9-af98-4b75-a335-0bd29547296d", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

Perform an identity verification check against a previously created Identity.

#### HTTP Request

`POST https://payscout-staging.finix.io/identities/identity_id/verifications`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
identity_id | ID of the Identity


#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Service used for verifying the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1


## Retrieve an Identity Verification

```shell
curl https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Verification;

$verification = Verification::retrieve("VIt9Y4eZdHbpundYsogcT2kN");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN', headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("verifications/{verification_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/verifications/{verification_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN");

print $response->as_string;
```


> Example Response:

```json

	{
	    "tags": {}, 
	    "created_at": "2016-04-29T16:39:40.56Z", 
	    "messages": [], 
	    "updated_at": "2016-04-29T16:39:40.56Z", 
	    "id": "VIt9Y4eZdHbpundYsogcT2kN", 
	    "instrument": null, 
	    "state": "SUCCEEDED", 
	    "underwritten_merchant": null, 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/verifications/VIt9Y4eZdHbpundYsogcT2kN"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "external_trace_id": "b49296f9-af98-4b75-a335-0bd29547296d", 
	    "processor": "DUMMY_V1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/verifications/verification_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
verification_id | ID of the Identity Verification


# Payment Instruments
A Payment Instrument resource represents either a credit card or bank account. All information is securely vaulted and referenced by an ID. A Payment Instrument may be created multiple times, and each tokenization produces a unique ID. Each ID may only be associated one time and to only one Identity. Once associated, a Payment Instrument may not be disassociated from an Identity.

## Create a New Card

```shell
curl https://payscout-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
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
       \"identity\": \"IDwW594hgk6No6rThnhCVeCq\"
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\PaymentInstrument;

$card = new PaymentInstrument(array(
    "name"=> array(
        "first_name"=> "Joe",
        "last_name"=> "Doe",
        "full_name"=> "Joe Doe"
    ),
    "type"=> "PAYMENT_CARD",
    "tags"=> null,
    "expiration_month"=> 12,
    "expiration_year"=> 2017,
    "number"=> "4111 1111 1111 1111",
    "security_code"=> "231",
    "address"=> null,
    "identity" => IDwW594hgk6No6rThnhCVeCq,
    ));
$card = $card->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "identity": "IDwW594hgk6No6rThnhCVeCq",
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
  "type": "PAYMENT_CARD"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/payment_instruments', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "identity": "IDwW594hgk6No6rThnhCVeCq",
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
    "type": "PAYMENT_CARD"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/payment_instruments', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"expiration_year\": 2020,  \"number\": \"4242424242424242\",  \"expiration_month\": 12,  \"address\": {    \"city\": \"San Mateo\",    \"country\": \"USA\",    \"region\": \"CA\",    \"line2\": \"Apartment 7\",    \"line1\": \"741 Douglass St\",    \"postal_code\": \"94114\"  },  \"security_code\": \"112\",  \"type\": \"PAYMENT_CARD\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("payment_instruments", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'expiration_year': 2020,  'number': '4242424242424242',  'expiration_month': 12,  'address': {    'city': 'San Mateo',    'country': 'USA',    'region': 'CA',    'line2': 'Apartment 7',    'line1': '741 Douglass St',    'postal_code': '94114'  },  'security_code': '112',  'type': 'PAYMENT_CARD'}");
Response response = client.target("https://payscout-staging.finix.io/payment_instruments")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'expiration_year': 2020,  'number': '4242424242424242',  'expiration_month': 12,  'address': {    'city': 'San Mateo',    'country': 'USA',    'region': 'CA',    'line2': 'Apartment 7',    'line1': '741 Douglass St',    'postal_code': '94114'  },  'security_code': '112',  'type': 'PAYMENT_CARD'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/payment_instruments", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "instrument_type": "PAYMENT_CARD", 
	    "card_type": "UNKNOWN", 
	    "name": "dwayne Sunkhronos", 
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
	    "updated_at": "2016-04-29T16:39:42.51Z", 
	    "expiration_month": 12, 
	    "security_code_verification": "UNKNOWN", 
	    "address_verification": "UNKNOWN", 
	    "last_four": "4242", 
	    "fingerprint": "FPR967679505", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDgKiqrJNBaLRWSjs6sWrKwu"
	        }
	    }, 
	    "created_at": "2016-04-29T16:39:42.51Z", 
	    "id": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "identity": "IDgKiqrJNBaLRWSjs6sWrKwu"
	}
```

<aside class="warning">
Creating cards directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

#### HTTP Request

`POST https://payscout-staging.finix.io/payment_instruments`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
identity | *string*, **required** | Identity resource which the card is associated. | IDgKiqrJNBaLRWSjs6sWrKwu
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
curl https://payscout-staging.finix.io/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
       \"account_type\": \"SAVINGS\",
       \"name\": \"Fran Lemke\",
       \"bank_code\": \"123123123\",
       \"country\": \"USA\",
       \"currency\": \"USD\",
       \"account_number\": \"123123123\",
       \"type\": \"BANK_ACCOUNT\",
       \"identity\": \"IDwW594hgk6No6rThnhCVeCq\"
       }"
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\PaymentInstrument;

$bank = new PaymentInstrument(array(
    "name"=> array(
        "first_name"=> "Joe",
        "last_name"=> "Doe",
        "full_name"=> "Joe Doe"
    ),
    "type"=> "BANK_ACCOUNT",
    "tags"=> null,
    "account_number"=> "84012312415",
    "bank_code"=> "840123124",
    "account_type"=> "SAVINGS",
    "iban"=> null,
    "bic"=> null,
    "company_name"=> "company name",
    "country"=> "USA",
    "currency"=> "USD",
    "identity" => "IDwW594hgk6No6rThnhCVeCq"
    ));
$bank = $bank->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "currency": "USD",
  "account_type": "SAVINGS",
  "name": "Fran Lemke",
  "bank_code": "123123123",
  "country": "USA",
  "type": "BANK_ACCOUNT",
  "identity": "IDwW594hgk6No6rThnhCVeCq",
  "account_number": "123123123"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/payment_instruments', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "currency": "USD",
    "account_type": "SAVINGS",
    "name": "Fran Lemke",
    "bank_code": "123123123",
    "country": "USA",
    "type": "BANK_ACCOUNT",
    "identity": "IDwW594hgk6No6rThnhCVeCq",
    "account_number": "123123123"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/payment_instruments', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"currency\": \"USD\",  \"account_type\": \"SAVINGS\",  \"name\": \"Fran Lemke\",  \"bank_code\": \"123123123\",  \"country\": \"USA\",  \"type\": \"BANK_ACCOUNT\",  \"identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"account_number\": \"123123123\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("payment_instruments", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'currency': 'USD',  'account_type': 'SAVINGS',  'name': 'Fran Lemke',  'bank_code': '123123123',  'country': 'USA',  'type': 'BANK_ACCOUNT',  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'account_number': '123123123'}");
Response response = client.target("https://payscout-staging.finix.io/payment_instruments")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'currency': 'USD',  'account_type': 'SAVINGS',  'name': 'Fran Lemke',  'bank_code': '123123123',  'country': 'USA',  'type': 'BANK_ACCOUNT',  'identity': 'IDwW594hgk6No6rThnhCVeCq',  'account_number': '123123123'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/payment_instruments", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "instrument_type": "BANK_ACCOUNT", 
	    "masked_account_number": "XXXXX3123", 
	    "name": "Fran Lemke", 
	    "tags": {}, 
	    "country": "USA", 
	    "created_at": "2016-04-29T16:39:37.24Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-04-29T16:39:37.24Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1"
	        }, 
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI3M33D11n22J7xU4bAbwbe1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```
<aside class="warning">
Creating bank accounts directly via the API should only be done for testing purposes.
</aside>
Please review our guide on how to tokenize cards via the [tokenization.js library](#tokenization-js)

#### HTTP Request

`POST https://payscout-staging.finix.io/payment_instruments`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
account_number | *string*, **required** | Bank account number. | 84012312415
bank_code | *string*, **required** | Routing number. Specified in FedACH database defined by the US Federal Reserve. | 840123124
identity | *string*, **required**| Identity resource which the bank account is associated. | IDwW594hgk6No6rThnhCVeCq
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



## Retrieve a Payment Instrument

```shell
curl https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve("PI3M33D11n22J7xU4bAbwbe1");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1', headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("payment_instruments/{payment_instrument_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/payment_instruments/{payment_instrument_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1");

print $response->as_string;

```


> Example Response:

```json

	{
	    "instrument_type": "BANK_ACCOUNT", 
	    "masked_account_number": "XXXXX3123", 
	    "name": "Fran Lemke", 
	    "tags": {}, 
	    "country": "USA", 
	    "created_at": "2016-04-29T16:39:37.10Z", 
	    "bank_code": "123123123", 
	    "updated_at": "2016-04-29T16:39:37.10Z", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1"
	        }, 
	        "authorizations": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/authorizations"
	        }, 
	        "verifications": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PI3M33D11n22J7xU4bAbwbe1/verifications"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "fingerprint": "FPR-1215770130", 
	    "id": "PI3M33D11n22J7xU4bAbwbe1", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/payment_instruments/payment_instrument_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
payment_instrument_id | ID of the Payment Instrument



# Card Authorizations
An Authorization resource (also known as a card hold) reserves a specific amount on a card to be captured (debited) at a later date, usually within 7 days. When an Authorization is captured it produces a Transfer resource.

## Create a New Authorization

```shell
curl https://payscout-staging.finix.io/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
       \"currency\": \"USD\",
       \"amount\": 100,
       \"processor\": \"DUMMY_V1\",
       \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",
       \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\"
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Authorization;

$payload = array(
    "processor" => "DUMMY_V1",
    "amount" => 100,
    "merchant_identity" => "IDwW594hgk6No6rThnhCVeCq",
    "source" => "PItBoYHhbKNroSRmUgB5MXjc",
    "tags" => array("Key" => "Value"));
$auth = new Authorization($payload);
$auth = $auth->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "currency": "USD",
  "amount": 100,
  "processor": "DUMMY_V1",
  "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
  "source": "PItBoYHhbKNroSRmUgB5MXjc"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/authorizations', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "currency": "USD",
    "amount": 100,
    "processor": "DUMMY_V1",
    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
    "source": "PItBoYHhbKNroSRmUgB5MXjc"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/authorizations', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"currency\": \"USD\",  \"amount\": 100,  \"processor\": \"DUMMY_V1\",  \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("authorizations", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'currency': 'USD',  'amount': 100,  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'source': 'PItBoYHhbKNroSRmUgB5MXjc'}");
Response response = client.target("https://payscout-staging.finix.io/authorizations")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'currency': 'USD',  'amount': 100,  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'source': 'PItBoYHhbKNroSRmUgB5MXjc'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/authorizations", Content => $data);

print $response->as_string;

```

> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "transfer": null, 
	    "created_at": "2016-04-29T16:40:50.91Z", 
	    "trace_id": "e1ad00b2-df07-4b46-b1d3-85ed50f78fbf", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-05-06T16:40:50.91Z", 
	    "updated_at": "2016-04-29T16:40:50.97Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA"
	        }
	    }, 
	    "id": "AUaaxqwWDXf4memwXMCVcTBA"
	}
```

#### HTTP Request

`POST https://payscout-staging.finix.io/authorizations`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PItBoYHhbKNroSRmUgB5MXjc
merchant_identity | *string*, **required** | UID. | IDwW594hgk6No6rThnhCVeCq
amount | *integer*, **required** | The amount of the debit in cents. | 100
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Retrieve an Authorization

```shell
curl https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Authorization;

$auth = Authorization::retrieve("AUaaxqwWDXf4memwXMCVcTBA");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA', headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("authorizations/{authorization_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/authorizations/{authorization_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA");

print $response->as_string;

```


> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "transfer": "TRvitQhjjJ3d4tV3Td5x8q6X", 
	    "created_at": "2016-04-29T16:40:50.69Z", 
	    "trace_id": "e1ad00b2-df07-4b46-b1d3-85ed50f78fbf", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-05-06T16:40:50.69Z", 
	    "updated_at": "2016-04-29T16:40:50.69Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "transfer": {
	            "href": "https://payscout-staging.finix.io/transfers/TRvitQhjjJ3d4tV3Td5x8q6X"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA"
	        }
	    }, 
	    "id": "AUaaxqwWDXf4memwXMCVcTBA"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/authorizations/authorization_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization



## Capture an Authorization

```shell
curl https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -X PUT \
    -d "{
       \"capture_amount\": 100,
       \"statement_descriptor\": \"Bobs Burgers\",
       \"fee\": 10
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Authorization;

$auth = Authorization::retrieve("AUaaxqwWDXf4memwXMCVcTBA")
$auth->capture_amount = 100;
$captured_auth = $auth->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "capture_amount": 100
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.put 'https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "capture_amount": 100
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA', data=values, headers=headers)
request.get_method = lambda: 'PUT'

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"capture_amount\": 100}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PutAsync("authorizations/{authorization_id}", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'capture_amount': 100}");
Response response = client.target("https://payscout-staging.finix.io/authorizations/{authorization_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .put(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'capture_amount': 100};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->put("https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA", Content => $data);

print $response->as_string;
```


> Example Response:

```json

	{
	    "tags": {}, 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "transfer": "TRvitQhjjJ3d4tV3Td5x8q6X", 
	    "created_at": "2016-04-29T16:40:50.69Z", 
	    "trace_id": "e1ad00b2-df07-4b46-b1d3-85ed50f78fbf", 
	    "state": "SUCCEEDED", 
	    "expires_at": "2016-05-06T16:40:50.69Z", 
	    "updated_at": "2016-04-29T16:40:50.69Z", 
	    "currency": "USD", 
	    "amount": 100, 
	    "is_void": false, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "transfer": {
	            "href": "https://payscout-staging.finix.io/transfers/TRvitQhjjJ3d4tV3Td5x8q6X"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/authorizations/AUaaxqwWDXf4memwXMCVcTBA"
	        }
	    }, 
	    "id": "AUaaxqwWDXf4memwXMCVcTBA"
	}
```

#### HTTP Request

`PUT https://payscout-staging.finix.io/authorizations/authorization_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
authorization_id | ID of the Authorization


#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
capture_amount | *integer*, **required** | The amount of the authorization you would like to capture in cents. Must be less than or equal to the amount of the authorization | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100


# Transfers
A Transfer resource represents any omnidirectional flow of funds. Transfers can represent either a debit to a card, a credit to a bank account, or a refund to a card depending on the request. Transfers have a state attribute representing the current state of the transaction. There are three possible status values: PENDING, SUCCEEDED, or FAILED.

## Debit a Card

```shell
curl https://payscout-staging.finix.io/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
       \"currency\": \"USD\",
       \"amount\": 100,
       \"fee\": 10,
       \"processor\": \"DUMMY_V1\",
       \"statement_descriptor\": \"Bob's Burgers\",
       \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",
       \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\"
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Transfer;
$payload = array(
    "processor" => "DUMMY_V1",
    "amount" => 100,
    "fee" => 10,
    "currency" => "USD",
    "merchant_identity" => "IDwW594hgk6No6rThnhCVeCq",
    "source" => "PItBoYHhbKNroSRmUgB5MXjc");
$debit = new Transfer($payload);
$debit = $debit->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

 values = '{
   "currency": "USD",
   "source": "PItBoYHhbKNroSRmUgB5MXjc",
   "processor": "DUMMY_V1",
   "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
   "amount": 100,
   "fee" => 100
 }'

 headers = {
   :content_type => 'application/vnd.json+api',
   :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
 }

 response = RestClient.post 'https://payscout-staging.finix.io/transfers', values, headers
 puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "currency": "USD",
    "amount": 100,
    "fee": 10,
    "processor": "DUMMY_V1",
    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq",
    "source": "PItBoYHhbKNroSRmUgB5MXjc"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/transfers', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"currency\": \"USD\",  \"source\": \"PItBoYHhbKNroSRmUgB5MXjc\",  \"processor\": \"DUMMY_V1\",  \"merchant_identity\": \"IDwW594hgk6No6rThnhCVeCq\",  \"amount\": 100}",  \"fee\": 10}",System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("transfers", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'currency': 'USD',  'source': 'PItBoYHhbKNroSRmUgB5MXjc',  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'amount': 100, 'fee': 10}");
Response response = client.target("https://payscout-staging.finix.io/transfers")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'currency': 'USD',  'source': 'PItBoYHhbKNroSRmUgB5MXjc',  'processor': 'DUMMY_V1',  'merchant_identity': 'IDwW594hgk6No6rThnhCVeCq',  'amount': 100, 'fee': 10};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/transfers", Content => $data);

print $response->as_string;
```



> Example Response:

```json

	{
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "destination": "PIht64noXsMri4GNoQETnhce", 
	    "state": "PENDING", 
	    "updated_at": "2016-04-29T16:39:44.82Z", 
	    "created_at": "2016-04-29T16:39:44.31Z", 
	    "tags": {}, 
	    "trace_id": "3ee62990-6d2f-45da-9250-06abe4e5c56f", 
	    "statement_descriptor": "PSC*PAYSCOUT", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG"
	        }, 
	        "destination": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PIht64noXsMri4GNoQETnhce"
	        }, 
	        "source": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/disputes"
	        }
	    }, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "type": "DEBIT", 
	    "id": "TR9T6bjbVvvRo1JNkmPQPqiG"
	}
```

A Transfer consisting of obtaining (charging) money from a card (i.e. debit).

#### HTTP Request

`POST https://payscout-staging.finix.io/transfers`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
source | *string*, **required** | The Payment Instrument to debited. | PItBoYHhbKNroSRmUgB5MXjc
merchant_identity | *string*, **required** | UID. | IDwW594hgk6No6rThnhCVeCq
amount | *integer*, **required** | The amount of the debit in cents. | 100
fee | *integer*, **optional** | The amount of the transaction you would like to collect as your fee. Must be less than or equal to the amount | 100
statement_descriptor | *string*, **required** | Text that will appear on the buyer's statement. Must be 18 characters or less. | Bob's Burgers
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1

## Refund a Debit


```shell
curl https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d  "{
       \"refund_amount\": 100
       }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Transfer;

$debit = Transfer::retrieve("TR9T6bjbVvvRo1JNkmPQPqiG");
$refund = $debit->reverse(100);
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "refund_amount": 100
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "refund_amount": 100
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"refund_amount\": 100}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("transfers/{transfer_id}/reversals", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'refund_amount': 100}");
Response response = client.target("https://payscout-staging.finix.io/transfers/{transfer_id}/reversals")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'refund_amount': 100};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals", Content => $data);

print $response->as_string;

```


> Example Response:

```json

	{
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "destination": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "state": "PENDING", 
	    "updated_at": "2016-04-29T16:40:49.46Z", 
	    "created_at": "2016-04-29T16:40:49.33Z", 
	    "tags": {}, 
	    "trace_id": "6da001f4-281b-44d7-aa12-ab9640630e34", 
	    "statement_descriptor": "PSC*PAYSCOUT", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 0, 
	    "_links": {
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/transfers/TR21gB2Yxgov4cLoG4ukESYg"
	        }, 
	        "destination": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "parent": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG"
	        }
	    }, 
	    "source": "PIht64noXsMri4GNoQETnhce", 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "type": "REVERSAL", 
	    "id": "TR21gB2Yxgov4cLoG4ukESYg"
	}
```

A Transfer representing a refund of a debit transaction. The amount of the refund may be any value up to the amount of the original debit.

#### HTTP Request

`POST https://payscout-staging.finix.io/transfers/transfer_id/reversals`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the original Transfer


#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
refund_amount | *integer*, **required** | The amount of the refund in cents. Must be equal to or less than the amount of the original debit. | 100

## Retrieve a Transfer

```shell
curl https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Transfer;

$debit = Transfer::retrieve("TR9T6bjbVvvRo1JNkmPQPqiG");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG', headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("transfers/{transfer_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/transfers/{transfer_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG");

print $response->as_string;

```


> Example Response:

```json

	{
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "destination": "PIht64noXsMri4GNoQETnhce", 
	    "state": "SUCCEEDED", 
	    "updated_at": "2016-04-29T16:39:44.03Z", 
	    "created_at": "2016-04-29T16:39:44.03Z", 
	    "tags": {}, 
	    "trace_id": "3ee62990-6d2f-45da-9250-06abe4e5c56f", 
	    "statement_descriptor": "PSC*PAYSCOUT", 
	    "currency": "USD", 
	    "amount": 100, 
	    "fee": 10, 
	    "_links": {
	        "reversals": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/reversals"
	        }, 
	        "merchant_identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG"
	        }, 
	        "destination": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PIht64noXsMri4GNoQETnhce"
	        }, 
	        "source": {
	            "href": "https://payscout-staging.finix.io/payment_instruments/PItBoYHhbKNroSRmUgB5MXjc"
	        }, 
	        "disputes": {
	            "href": "https://payscout-staging.finix.io/transfers/TR9T6bjbVvvRo1JNkmPQPqiG/disputes"
	        }
	    }, 
	    "source": "PItBoYHhbKNroSRmUgB5MXjc", 
	    "merchant_identity": "IDwW594hgk6No6rThnhCVeCq", 
	    "type": "DEBIT", 
	    "id": "TR9T6bjbVvvRo1JNkmPQPqiG"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/transfers/transfer_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
transfer_id | ID of the Transfer


# Disputes
Disputes, also known as chargebacks, represent any customer-disputed charge.

## Retrieve a Dispute

```shell
curl https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Dispute;

$dispute = Dispute::retrieve("DI6cBJg71oSzmQUzuj2PYo4T");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T', headers=headers)

response_body = urlopen(request).read()
print response_body
```


```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("disputes/{dispute_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/disputes/{dispute_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "Basic VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T");

print $response->as_string;

```


> Example Response:

```json

	{
	    "state": "PENDING", 
	    "transfer": "TRpdmLDYp2iw7oNmMcKM3kEw", 
	    "created_at": "2016-04-29T16:40:04.67Z", 
	    "tags": {}, 
	    "occurred_at": "2016-04-29T16:39:46.09Z", 
	    "amount": 0, 
	    "updated_at": "2016-04-29T16:40:04.67Z", 
	    "reason": "FRAUD", 
	    "_links": {
	        "transfer": {
	            "href": "https://payscout-staging.finix.io/transfers/TRpdmLDYp2iw7oNmMcKM3kEw"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T"
	        }, 
	        "evidence": {
	            "href": "https://payscout-staging.finix.io/disputes/DI6cBJg71oSzmQUzuj2PYo4T/evidence"
	        }
	    }, 
	    "respond_by": "2016-05-06T16:40:04.89Z", 
	    "id": "DI6cBJg71oSzmQUzuj2PYo4T"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/disputes/dispute_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
dispute_id | ID of the Dispute



# Webhooks
Webhooks allow you to build or set up integrations which subscribe to certain events on the Payscout API. When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL. Webhooks are particularly useful for updating asynchronous state changes in Transfers or notifications of newly created Disputes.

## Create a New Webhook

```shell
curl https://payscout-staging.finix.io/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d '{"url": "https://examplesite.com"}'
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Webhook;

$payload = array("url" => "https://examplesite.com");

$webhook = new Webhook($payload);
$webhook = $webhook->save();
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

values = '{
  "url": "https://examplesite.com"
}'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.post 'https://payscout-staging.finix.io/webhooks', values, headers
puts response
```

```python
from urllib2 import Request, urlopen

values = """
  {
    "url": "https://examplesite.com"
  }
"""

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/webhooks', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

    using (var content = new StringContent("{  \"url\": \"https://examplesite.com\"}", System.Text.Encoding.Default, "application/vnd.json+api"))
    {
      using (var response = await httpClient.PostAsync("webhooks", content))
      {
        string responseData = await response.Content.ReadAsStringAsync();
      }
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Entity<String> payload = Entity.text("{  'url': 'https://examplesite.com'}");
Response response = client.target("https://payscout-staging.finix.io/webhooks")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .post(payload);

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;
my $data = {  'url': 'https://examplesite.com'};

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->post("https://payscout-staging.finix.io/webhooks", Content => $data);

print $response->as_string;
```


> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-04-29T16:40:48.47Z", 
	    "enabled": true, 
	    "updated_at": "2016-04-29T16:40:48.47Z", 
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY"
	        }
	    }, 
	    "id": "WHoCWzhn2uPD81tJfyKxR6MY"
	}
```

#### HTTP Request

`POST https://payscout-staging.finix.io/webhooks`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
url | *string*, **required** | The HTTP or HTTPS url the callbacks will be made to | https://examplesite.com


## Retrieve a Webhook

```shell
curl https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY \
    -H "Content-Type: application/vnd.json+api" \
    -u USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```

```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Webhook;

$webhook = Webhook::retrieve("WHoCWzhn2uPD81tJfyKxR6MY");
```

```ruby
require 'rubygems' if RUBY_VERSION < '1.9'
require 'rest_client'

headers = {
  :content_type => 'application/vnd.json+api',
  :authorization => 'VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}

response = RestClient.get 'https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY', headers
puts response
```

```python
from urllib2 import Request, urlopen

headers = {
  'Content-Type': 'application/vnd.json+api',
  'Authorization': 'VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA=='
}
request = Request('https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY', headers=headers)

response_body = urlopen(request).read()
print response_body
```

```csharp
//Common testing requirement. If you are consuming an API in a sandbox/test region, uncomment this line of code ONLY for non production uses.
//System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

//Be sure to run "Install-Package Microsoft.Net.Http" from your nuget command line.
using System;
using System.Net.Http;

var baseAddress = new Uri("https://payscout-staging.finix.io/");

using (var httpClient = new HttpClient{ BaseAddress = baseAddress })
{


  httpClient.DefaultRequestHeaders.TryAddWithoutValidation("authorization", "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

  using(var response = await httpClient.GetAsync("webhooks/{webhooks_id}"))
  {

        string responseData = await response.Content.ReadAsStringAsync();
  }
}
```

```java
// Maven : Add these dependecies to your pom.xml (java6+)
// <dependency>
//     <groupId>org.glassfish.jersey.core</groupId>
//     <artifactId>jersey-client</artifactId>
//     <version>2.8</version>
// </dependency>
// <dependency>
//     <groupId>org.glassfish.jersey.media</groupId>
//     <artifactId>jersey-media-json-jackson</artifactId>
//     <version>2.8</version>
// </dependency>

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.MediaType;

Client client = ClientBuilder.newClient();
Response response = client.target("https://payscout-staging.finix.io/webhooks/{webhooks_id}")
  .request(MediaType.TEXT_PLAIN_TYPE)
  .header("Authorization", "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==")
  .get();

System.out.println("status: " + response.getStatus());
System.out.println("headers: " + response.getHeaders());
System.out.println("body:" + response.readEntity(String.class));
```


```perl
require LWP::UserAgent;

my $ua   = LWP::UserAgent->new;

$ua->default_header("Content-Type" => "application/vnd.json+api");
$ua->default_header("Authorization" => "VVNiZmJRM0E3R3ZYcGpTcGM5c3R3aFBxOmFmZmJmYmFkLTBjYWItNDAzMy05NTA5LWQ1ODQ4MzRhNGJjMA==");

my $response = $ua->get("https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY");

print $response->as_string;
```


> Example Response:

```json

	{
	    "url": "http://requestb.in/vts8mpvt", 
	    "created_at": "2016-04-29T16:40:48.49Z", 
	    "enabled": true, 
	    "updated_at": "2016-04-29T16:40:48.49Z", 
	    "application": "APsZ4K3jRswSZ7JpRChLf6dq", 
	    "_links": {
	        "self": {
	            "href": "https://payscout-staging.finix.io/webhooks/WHoCWzhn2uPD81tJfyKxR6MY"
	        }
	    }, 
	    "id": "WHoCWzhn2uPD81tJfyKxR6MY"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/webhooks/webhook_id`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
webhook_id | ID of the Webhook


# Settlements
A Settlement resource represents a collection of Transfers that are to be paid out to a specific Merchant.

## Create a New Settlement

```shell
curl https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0 \
    -d "{
        \"processor\": \"DUMMY_V1\",
        \"currency\": \"USD\"
        }"
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Settlement;
use Payscout\Resources\Identity;

$identity = Identity::retrieve("IDwW594hgk6No6rThnhCVeCq");
$payload = array(
    "processor" => "DUMMY_V1",
    "currency"=>"USD");
$settlement = $identity->createSettlement($payload);
```

```ruby

```

```python

```

```csharp

```


```perl

```

> Example Response:

```json

	{
	    "total_amount": 888958, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-04-29T16:41:55.35Z", 
	    "updated_at": "2016-04-29T16:41:55.43Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "total_fee": 30, 
	    "id": "STpspeSDXZDuVStLupbiT4Hy", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`POST https://payscout-staging.finix.io/identities/:identity_id/settlements`

#### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
processor | *string*, **required** | Processor used for underwriting the Identity, please use "DUMMY_V1" for now to test the API. | DUMMY_V1
currency | *integer*, **required** | The currency for the settlement. | USD


## Retrieve a Settlement

```shell
curl https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy \
    -H "Content-Type: application/vnd.json+api" \
    -u  USbfbQ3A7GvXpjSpc9stwhPq:affbfbad-0cab-4033-9509-d584834a4bc0
```


```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/Payscout/Settings.php');
Payscout\Settings::configure('https://payscout-staging.finix.io', 'USbfbQ3A7GvXpjSpc9stwhPq', 'affbfbad-0cab-4033-9509-d584834a4bc0');
require(__DIR__ . '/src/Payscout/Bootstrap.php');
\Payscout\Bootstrap::init();

use Payscout\Resources\Settlement;
use Payscout\Resources\Identity;

$settlement = Settlement::retrieve("STpspeSDXZDuVStLupbiT4Hy");
```

```ruby

```

```python

```

```csharp

```


```perl

```

> Example Response:

```json

	{
	    "total_amount": 888958, 
	    "tags": {}, 
	    "transfer": null, 
	    "created_at": "2016-04-29T16:41:55.17Z", 
	    "updated_at": "2016-04-29T16:41:55.17Z", 
	    "processor": "DUMMY_V1", 
	    "currency": "USD", 
	    "_links": {
	        "transfers": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy/transfers"
	        }, 
	        "self": {
	            "href": "https://payscout-staging.finix.io/settlements/STpspeSDXZDuVStLupbiT4Hy"
	        }, 
	        "identity": {
	            "href": "https://payscout-staging.finix.io/identities/IDwW594hgk6No6rThnhCVeCq"
	        }
	    }, 
	    "total_fee": 30, 
	    "id": "STpspeSDXZDuVStLupbiT4Hy", 
	    "identity": "IDwW594hgk6No6rThnhCVeCq"
	}
```

#### HTTP Request

`GET https://payscout-staging.finix.io/settlements/:settlement_id`

