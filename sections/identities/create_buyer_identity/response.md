> Example Response:

```json
{{create_buyer_identity_scenario_response}}
```
All fields for a buyer's Identity are optional. However, a `business_type` field should not be passed. Passing a `business_type` indicates that the Identity should be treated as a merchant.

#### HTTP Request

`POST {{staging_base_url}}/identities`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
first_name | *string*, **optional** | First name
last_name | *string*, **optional** | Last name
phone | *string*, **optional** | Phone number
email | *string*, **optional** | Email address
line1 | *string*, **optional** | First line of the address (max 35 characters)
line2 | *string*, **optional** | Second line of the address (max 35 characters)
city | *string*, **optional** | City (max 20 characters)
region | *string*, **optional** | 2-letter State code
postal_code | *string*, **optional** | Zip or Postal code (max 7 characters)
country | *string*, **optional** | 3-Letter Country code
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
