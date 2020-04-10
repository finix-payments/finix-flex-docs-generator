> Example Response:

```json
{{create_merchant_fee_profile_scenario_response}}
```

Setting new pricing for a `Merchant` will only impact the pricing for this merchant. It will not impact other `Merchants` or the `Application` as a whole. `Merchants` with custom pricing will not inherit changes to the `Application's` default pricing.

#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:MERCHANT_ID | *string*, **required** | ID of `Merchant`
basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each card-based Transfer. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual card-based `Transfer`
ach_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of an eCheck (ACH Debit). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
ach_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual `Transfer`
charge_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based Transfers.
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
