> Example Response:

```json
{{create_application_fee_profile_scenario_response}}
```

Setting new pricing for an `Application` will only impact the pricing for this `Application` and any of it's submerchants that do not have custom pricing. If a submerchant's `fee_profile` is not null, it will not inherit the new `Application` pricing by default.

#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of `Application`
basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each card-based Transfer. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual card-based `Transfer`
ach_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of an eCheck (ACH Debit). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
ach_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual `Transfer`
charged_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based Transfers.
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
