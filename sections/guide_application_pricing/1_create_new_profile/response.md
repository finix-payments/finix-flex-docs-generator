> Example Response:

```json
{{create_application_fee_profile_scenario_response}}
```

Setting new pricing for an `Application` will only impact the pricing for this application and any of it's submerchants that do not have custom pricing. If a submerchant's `fee_profile` is not null, it will not inherit the new Application pricing by default.

#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of `Application`
basis_points | *number*, **optional** | One hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *number*, **optional** | A set amount paid that doesn't change  
ach_basis_points | *number*, **optional** | Cost for ACH
charged_interchange | *boolean*, **optional** | Set to True to charge for interchange
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
