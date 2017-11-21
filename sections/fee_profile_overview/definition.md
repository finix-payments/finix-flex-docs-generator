# Fee Profiles

With {{api_name_downcase}}, you have the power to configure an entire `Application's` `fee_profile` or a specific `Merchant's` `fee_profile`. A `fee_profile` consists of percentage and fixed based fees that are subtracted from the total `amount` for each `Transfer`.

Both an `Application` and a `Merchant` can have a `fee_profile`; however if an `Application` and it's `Merchant` have a `fee_profile`, the `Merchant's` `fee_profile` will take precedence. By default, both an `Application's` and a `Merchant's` `fee_profile` will be null.
