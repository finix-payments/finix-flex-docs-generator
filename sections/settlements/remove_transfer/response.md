Do you have a transfer in a batch settlement that you think may be a fraudulent transaction? You can remove the `Transfer` or an array of `Transfers` from a batch settlement.

Per the JSON API for deleting a resource, our API doesn't have a response body when removing a transfer from a settlement.


#### HTTP Request

`POST {{staging_base_url}}/settlements/:SETTLEMENT_ID/transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement
