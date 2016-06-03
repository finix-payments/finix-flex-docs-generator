> Example Response:

```json
{{create_identity_scenario_response}}
```

### HTTP Request

`POST {{base_url}}/identities`

### Request Arguments

Field | Type | Description | Example
----- | ---- | ----------- | -------
tags | *object*, **optional** | Key value pair for annotating custom meta data | {'order_number': '123123123'}
first_name | *string*, **optional** | First name of the customer or representative of the business | Dwayne
last_name | *string*, **optional** | Last name of the customer or representative of the business | Johnson
tax_id | *string*, **optional** | Nine digit Social Security Number for the representative of the business | 123456789
day | *integer*, **optional** | Day field of date of birth | 1
month | *integer*, **optional** | Month field of date of birth | 2
year | *string*, **optional** | Year field of date of birth | 1988
phone | *string*, **optional** | Phone integer of the person. Note: There's a separate field for the business phone integer | 1408756449
email | *string*, **optional** | Email address of the customer or representative of the business. | someone@example.com
business_name | *string*, **optional** | Full legal business name if the Identity is a business | Business, Inc
doing_business_as | *string*, **optional** | Business name used with customers if different from its legal name (Between 0 and 16 characters long) | Bob's Burgers
business_type | *string*, **optional** | The type of business | INDIVIDUAL_SOLE_PROPRIETORSHIP, CORPORATION, LIMITED_LIABILITY_COMPANY, PARTNERSHIP, LIMITED_PARTNERSHIP, GENERAL_PARTNERSHIP, ASSOCIATION_ESTATE_TRUST, TAX_EXEMPT_ORGANIZATION, INTERNATIONAL_ORGANIZATION, GOVERNMENT_AGENCY, JOINT_VENTURE
business_tax_id | *string*, **optional** | Nine digit SSN if business_type is INDIVIDUAL_SOLE_PROPRIETORSHIP or EIN for all other business types | 123456789
business_phone | *string*, **optional** | Phone integer of the business | 0123456789
line1 | *string*, **optional** | Street address of the associated card. | 1423 S Joane Way
line2 | *string*, **optional** | Second line of the address of the associated card. |  Apt. 3
city | *string*, **optional** | City of the associated card. | San Mateo
region | *string*, **optional** | State of the associated card. | CA
postal_code | *string*, **optional** | Postal of the associated card. | 92704
country | *string*, **optional** | Country of the associated card. | USA
annual_card_volume | *integer*, **optional** |  Approximate annual credit card sales in cents expected to be processed under this Identity
max_transaction_amount | *integer*, **optional** |  Maximum amount in cents that can be transacted on behalf of this Identity's when serving as a merchant
mcc | *string*, **optional** |  MCC code that this merchant will be classified under
url | *string*, **optional** |  Website for the merchant
