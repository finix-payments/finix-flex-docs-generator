> Example Response:

```json
{{create_buyer_identity_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities`

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
