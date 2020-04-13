> Example Response:

```json
{{create_application_fee_profile_qualified_tiers_scenario_response}}
```

Qualified tiers allow Payment Facilitators to create various fee tiers based on the interchange percentage. The interchange percentage is the approximate interchange fee amount divided by the purchase amount. When an interchange percent falls within a certain tier, a fixed fee and basis point fee is created for that sale.

Each Card Network within the `Fee Profile` must have at least one tier associated to it. The Payment Facilitator can create an unlimited amount of tiers; however, at least one tier required.


#### HTTP Request

`POST {{staging_base_url}}/fee_profiles`

#### General Fee Profile Request Arguments

Field | Type | Description
----- | ---- | -----------
:APPLICATION_ID | *string*, **required** | ID of `Application`
basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each card-based `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual card-based `Transfer`
ach_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of an eCheck (ACH Debit). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
ach_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual `Transfer`
charge_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based `Transfers`

#### First level of the structure:
Field | Type | Description
----- | ---- | -----------
qualified_tiers | *object*, **optional** | The top of the qualified tier tree


#### Second level of the structure:
Field | Type | Description
----- | ---- | -----------
american_express | *object*, **required** | American Express qualified tiers
discover | *object*, **required** | Discover qualified tiers
mastercard | *object*, **required** | Mastercard qualified tiers
visa | *object*, **required** | Visa qualified tiers
unknown_card_type | *object*, **required** | Default qualified tiers if card brand could not be determined

#### Third level of the structure:
Field | Type | Description
----- | ---- | -----------
credit | *array*, **required** | Fee buckets for credit card purchases
debit | *array*, **required** | Fee buckets for debit card purchases


<aside class="notice">
IMPORTANT: The last bucket in each tier must have the max_interchange completely omitted. Or max_interchange = null. This is because the last interchange bound goes to infinity.
</aside>


#### Fourth level of the structure:
Field | Type | Description
----- | ---- | -----------
display_name | *string*, **required** | Custom name given to this type of fee tier
basis_points | *integer*, **required** | Measure of interest rates or percentage used to calculate fees
fixed | *integer*, **required** | A fixed fee that will be charged if this bucket is used
max_interchange | *string*, **required** | The bounds of the qualified tier bucket



#### Response
Field | Type | Description
----- | ---- | -----------
min_interchange | *string* | 0: Represents the lower bound of the first tier. Integers that are greater than 0: Represents the middle bounds of the fee bucket.
