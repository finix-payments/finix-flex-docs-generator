#### HTTP Request

`POST {{staging_base_url}}/transfers/:TRANSFER_ID/reversals`


#### URL Parameters

Field | Type | Description
----- | ---- | -----------
:TRANSFER_ID | *string*, **required** | ID of the original Transfer

#### Request Arguments

Field | Type | Description
----- | ---- | -----------
refund_amount | *integer*, **required** | The amount of the refund in cents (Must be equal to or less than the amount of the original `Transfer`)
:DEVICE_ID | *string*, **required** | The ID of the activated device

```
{
    "id": "TRkWoMAdBwfVgYQpL8csYbtH",
    "amount": 150,
    "tags": {},
    "state": "SUCCEEDED",
    "trace_id": "FNXhYDzG8GLyL2gmE77Ygnjai",
    "currency": "USD",
    "application": "APuZMfMerci2JuLUs7xWpf5G",
    "source": null,
    "destination": "PIp89SyE68fV5rxRCZUJz39c",
    "ready_to_settle_at": null,
    "fee": 0,
    "statement_descriptor": "FNXQA*POLLOS HERMANOS",
    "type": "REVERSAL",
    "messages": [],
    "raw": null,
    "created_at": "2019-04-02T11:11:03.42Z",
    "updated_at": "2019-04-02T11:11:17.34Z",
    "idempotency_id": null,
    "merchant_identity": "ID8W4rxaFN8HsxqugmesLMVo",
    "device": "DVkBqa68V1ZQusodU8o6mB62",
    "subtype": "API",
    "_links": {
        "application": {
            "href": "https://finix.sandbox-payments-api.com/applications/APuZMfMerci2JuLUs7xWpf5G"
        },
        "self": {
            "href": "https://finix.sandbox-payments-api.com/transfers/TRkWoMAdBwfVgYQpL8csYbtH"
        },
        "parent": {
            "href": "https://finix.sandbox-payments-api.com/transfers/TRu7UQdLY3GG2EnPbKNazQYv"
        },
        "destination": {
            "href": "https://finix.sandbox-payments-api.com/payment_instruments/PIp89SyE68fV5rxRCZUJz39c"
        },
        "merchant_identity": {
            "href": "https://finix.sandbox-payments-api.com/identities/ID8W4rxaFN8HsxqugmesLMVo"
        },
        "payment_instruments": {
            "href": "https://finix.sandbox-payments-api.com/transfers/TRkWoMAdBwfVgYQpL8csYbtH/payment_instruments"
        }
    }
}
```
