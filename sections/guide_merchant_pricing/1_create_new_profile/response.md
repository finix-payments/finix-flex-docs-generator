> Example Response:

```json
{{create_merchant_fee_profile_scenario_response}}
```

Setting new pricing for a `Merchant` will only impact the pricing for this merchant. It will not impact other merchants or the Application as a whole. Merchants with custom pricing will not inherit changes to the Application's default pricing.

#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of `Merchant`
basis_points | *number*, **optional** | One hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *number*, **optional** | A set amount paid that doesn't change
ach_basis_points | *number*, **optional** | Cost for ACH
charged_interchange | *boolean*, **optional** | Set to True to charge for interchange
tags | *object*, **optional** | Key value pair for annotating custom meta data
(e.g. order numbers)
