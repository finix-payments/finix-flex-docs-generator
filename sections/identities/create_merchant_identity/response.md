> Example Response:

```json
{{create_merchant_identity_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities`

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