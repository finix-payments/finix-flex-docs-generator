Do you have a transfer in a batch settlement that you think may be a fraudulent transaction? So as long as the `Settlement` hasn't been funded, you can remove the `Transfer` or an array of `Transfers`, along with its corresponding fee from a batch settlement.

<aside class="notice">
Per the JSON API for deleting a resource, our API doesn't have a response body when removing a transfer from a settlement.
</aside>

#### HTTP Request

`DELETE {{staging_base_url}}/settlements/:SETTLEMENT_ID/transfers`


#### URL Parameters

Parameter | Description
--------- | -------------------------------------------------------------------
:SETTLEMENT_ID | ID of the Settlement
