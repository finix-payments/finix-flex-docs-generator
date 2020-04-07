> Example Response:

```json
{{create_application_fee_profile_qualified_tiers_scenario_response}}
```

Qualified Tiered Fees gives the customer the ability to create fees based off a simple calculation.
Interchange Percentage = Approximate Interchange Fee Amount / Purchase Amount

The user will create tiered buckets for each card brand and card type. When an interchange percent lands in a tier, a fixed fee and basis point fee will be created for the sale.

#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of `Application`
basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each card-based `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual card-based `Transfer`
ach_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of an eCheck (ACH Debit). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
ach_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual `Transfer`
charge_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based `Transfers`
