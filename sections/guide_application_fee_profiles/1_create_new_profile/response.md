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
application | *string*, **required** | ID of `Application`
basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each card-based `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual card-based `Transfer`
ach_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of an eCheck (ACH Debit). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
ach_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual `Transfer`
charge_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based `Transfers`
dispute_inquiry_fixed_fee | *integer*, **optional** | Applied when a dispute is created in state INQUIRY
dispute_fixed_fee | *integer*, **optional** | Applied when a dispute is created or moved to state PENDING
american_express_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each American Express `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
american_express_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual American Express `Transfer`
american_express_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for American Express `Transfers`
american_express_assessment_basis_points | *integer*, **optional** | Applies to gross American Express card volume
diners_club_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each Diners `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
diners_club_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual Diners `Transfer`
diners_club_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for Diners `Transfers`
discover_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each Discover `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
discover_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual Discover `Transfer`
discover_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for Discover `Transfers`
discover_assessments_basis_points | *integer*, **optional** | Assessment applies to gross Discover card transaction volume
discover_data_usage_fixed_fee | *integer*, **optional** | Applies to all U.S.-based authorization transactions
discover_network_authorization_fixed_fee | *integer*, **optional** | This fee will applies to all Discover network authorizations and will replace the previously assessed Data Transmission
jcb_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each JCB `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
jcb_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual JCB `Transfer`
jcb_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for JCB `Transfers`
mastercard_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each MasterCard `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
mastercard_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual MasterCard `Transfer`
mastercard_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for MasterCard `Transfers`
mastercard_assessments_under1k_basis_points | *integer*, **optional** | Assessment applies to Mastercard transactions less than or equal to $1,000
mastercard_assessments_over1k_basis_points | *integer*, **optional** | Assessment applies to Mastercard credit sale transactions greater than $1,000
mastercard_acquirer_fees_basis_points | *integer*, **optional** |  Fee is assessed on a business's gross MasterCard processing volume. This fee varies per acquirer based on MasterCard's assessed charge as it's distributed across the acquirer's portfolio of merchants. Generally, the ALF fee is a fraction of a basis point. For example, 0.0045%, 0.0075%, etc. are examples of a likely ALF fee
visa_basis_points | *integer*, **optional** | Percentage-based fee incurred against the full amount of each Visa `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%)
visa_fixed_fee | *integer*, **optional** | Fee in cents incurred for each individual Visa `Transfer`
visa_charge_interchange | *integer*, **optional** | Set to True to incur interchange fees for Visa `Transfers`
visa_assessments_basis_points | *integer*, **optional** |Applies to all Visa credit transactions
visa_acquirer_processing_fixed_fee | *integer*, **optional** | All U.S.-based credit card authorizations acquired in the U.S. regardless of where the issuer/cardholder is located. If your business is based in the U.S., the acquirer processing fee will apply to all Visa credit card authorizations
visa_credit_voucher_fixed_fee | *integer*, **optional** | Applies to refunds
visa_kilobyte_access_fixed_fee | *integer*, **optional** | Charged on each authorization transaction submitted to Visa's network for settlement
visa_base_II_system_file_transmission_fixed_fee | *integer*, **optional** | Applies to all Visa transactions and is charged in addition to other transaction-based assessments
visa_base_II_credit_voucher_fixed_fee | *integer*, **optional** | Applies to all U.S.-based refund
rounding_mode | *integer*, **optional** | Pass in AGGREGATE if you want to round after the settlement calculation. Default is rounding before the sum of the settlement calculation (i.e. round each fee transfer).
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
