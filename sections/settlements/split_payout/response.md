> Example Response:



Allows a user to split a settlement into separate funding instructions. For example, a payment facilitator can split the settlement into multiple parts- a portion of the settlement can go to the merchant, another part can be allocated to the operating account, and another part can go towards paying back the loan the merchant took out. This feature is not available by default and cannot be called on the `DUMMY_V1` processor, please email support@finixpayments.com to learn more.


<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can make this API call.
</aside>

#### HTTP Request

`POST {{staging_base_url}}/settlements/:SETTLEMENT_ID`

#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the `Settlement`


#### Request Arguments

Field | Type | Description
----- | ---- | -----------
destination | *string*, **required** | ID of the `Payment Instrument` where the funds should be deposited
amount | *integer*, **required** | The amount of the authorization in cents
currency | *integer*, **required** | 3-letter currency code that the funds should be deposited (e.g. USD)
tags | *object*, **optional** | Key value pair for annotating custom meta data (e.g. order numbers)
