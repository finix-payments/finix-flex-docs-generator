> Example Response:

```json
{{create_merchant_fee_profile_scenario_response}}
```

Tiered Billing is a fee structure that determines how much merchants pay per transaction based on the  inputs below. Tiered billing charges do not supercede other fee profile elements. In other words, other fee profile elements can still be enabled and charged for a transaction, such as pass-through Dues & Assessments.

* Card Brand (i.e. Visa, Mastercard, etc.)
* Card Type (i.e. Debit vs Credit)
* Interchange Rate (i.e. 1.25%)
The combination of each of these inputs results in a transaction fee plan categorized into 1 of 3 buckets:

* Qualified
* Mid-qualified
* Non-qualified

*Card brand and transaction type*
* Repeat the following for each variation of card brand and card type as shown in the sample payload, such as for VISA and DEBIT.
* Ranges must validate correctly; i.e., when buckets meet at a boundary, one bucket's boundary should be INCLUSIVE and the other EXCLUSIVE. The 0 and 10000 items must be INCLUSIVE to ensure all values are covered.
* The lowest range in a rate tier must have a 0 as its range_low and low_type as INCLUSIVE.
* The highest range in a rate tier must have a 10000 as its range_high and high_type as INCLUSIVE.

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
charged_interchange | *boolean*, **optional** | Set to True to incur interchange fees for card-based Transfers.
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)

card_brand |	*string*, **required** |	A value from this list: VISA, MASTERCARD, DISCOVER, AMERICAN\_EXPRESS
card_type	| *string*, **required** |	A value from this list: DEBIT, CREDIT
display_name |*string*, **optional** | Merchant-facing string describing the billing bucket
range_low	| *integer*, **required**	| basis points for interchange rate, for the low-side of the range.
low_type	| *integer*, **required** | A value from this list: INCLUSIVE, EXCLUSIVE, describes if the bottom of the range includes that number or only values above that number.
range_high |*integer*, **required**	| basis points for interchange rate, for the high-side of the range.
high_type	| *string*, **optional** | A value from this list: INCLUSIVE, EXCLUSIVE, describes if the top of the range includes that number or only values below that number.

## Schematic of Tiered Billing
https://gist.github.com/ambarp513/b5b2436cbcb6053db52f862b56222d26

## Example of Tiered Billing
https://user-images.githubusercontent.com/54867959/72749069-e6c25600-3bb0-11ea-932a-e54cabf96d9b.png
