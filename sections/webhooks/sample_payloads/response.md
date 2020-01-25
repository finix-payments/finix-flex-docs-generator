### Created Authorization

```javascript

{
  "type" : "created",
  "entity" : "authorization",
  "occurred_at" : "2016-07-06T08:15:21.734",
  "_embedded" : {
    "authorizations" : [ {
      "amount" : 100,
      "trace_id" : "5e157d2f-1362-4ab2-86af-3f97a8f28f0d",
      "created_at" : "2016-07-06T08:15:21.63Z",
      "source" : "PIeAkgVK9TPBnmyf6CSskv5i",
      "merchant_identity" : "IDradKrsCKMYJyj3VFKimKuy",
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      },
      "transfer" : null,
      "expires_at" : "2016-07-13T08:15:21.63Z",
      "updated_at" : "2016-07-06T08:15:21.65Z",
      "is_void" : false,
      "currency" : "USD",
      "id" : "AUfU8FU7RfgTmhfRagrF1RpS",
      "state" : "SUCCEEDED"
    } ]
  }
}
```

### Created New Transfer

```javascript
{
 "type" : "created",
  "entity" : "transfer",
  "occurred_at" : "2016-07-06T07:41:38.466",
  "_embedded" : {
    "transfers" : [ {
      "amount" : 100,
      "trace_id" : "e87b8ebc-177e-4e11-9cc3-6cfcfae7adc8",
      "fee" : 0,
      "destination" : "PIg3pCsoqrygp1gCvBNvfT3x",
      "created_at" : "2016-07-06T07:41:38.24Z",
      "source" : "PI2f1E5JVeQriDMeDpULnae3",
      "merchant_identity" : "IDoXe9ce6ztf6Pbpoq2WbeMt",
      "type" : "REVERSAL",
      "tags" : { },
      "statement_descriptor" : "PLD*POLLOS HERMANOS",
      "application" : "APdHz4LE8cNmJbbK7WW2egcg",
      "updated_at" : "2016-07-06T07:41:38.37Z",
      "currency" : "USD",
      "id" : "TRjgpj7b7xZXN18XyD7G3JER",
      "state" : "PENDING"
    } ]
  }
}
```

### Updated Transfer

```javascript
{
  "type" : "updated",
  "entity" : "transfer",
  "occurred_at" : "2016-07-06T07:08:02.342",
  "_embedded" : {
    "transfers" : [ {
      "amount" : 100,
      "trace_id" : "55ab6c90-2cfd-47ea-8f9b-c7385880617d",
      "fee" : 0,
      "destination" : "PIx7rQE9dzEGoccQ76D22xuZ",
      "created_at" : "2016-07-06T07:07:39.51Z",
      "source" : "PIoHzz6XzUzCqi5YqL9TVGN6",
      "merchant_identity" : "IDhxk2ESd2eFF38ewG7Eth93",
      "type" : "REVERSAL",
      "tags" : { },
      "statement_descriptor" : "PLD*PRESTIGE WORLD WI",
      "application" : "APwD1R6mEokpr84pypG4TBZv",
      "updated_at" : "2016-07-06T07:08:02.19Z",
      "currency" : "USD",
      "id" : "TR4CUpq9T8E6tBDmWMxQQ2P1",
      "state" : "SUCCEEDED"
    } ]
  }
}

```



### Created Payment Instrument

```javascript
{
    "type": "created",
    "entity": "instrument",
    "occurred_at": "2019-10-16T23:13:12.133",
    "_embedded": {
        "instruments": [
            {
                "address": {
                    "line1": "900 Metro Center Blv",
                    "line2": null,
                    "city": "San Francisco",
                    "region": "CA",
                    "postal_code": "94404",
                    "country": "USA"
                },
                "address_verification": "UNKNOWN",
                "bin": "489514",
                "security_code_verification": "UNKNOWN",
                "created_at": "2019-10-16T23:13:11.90Z",
                "instrument_type": "PAYMENT_CARD",
                "card_type": "UNKNOWN",
                "type": "PAYMENT_CARD",
                "tags": {
                    "card_name": "Business Card"
                },
                "expiration_year": 2020,
                "application": "APf7avmNAHZ9Qtm2mENaGQT",
                "updated_at": "2019-10-16T23:13:11.91Z",
                "last_four": "0006",
                "identity": "IDxmDPpYkpQCaFj4LAnwXyJW",
                "fingerprint": "FPRogKWsRQks2HGaau5eGR9AF",
                "expiration_month": 3,
                "name": "Ayisha Curry",
                "currency": "USD",
                "id": "PIgSQx5XHNiwef1Bh87tzqNB",
                "brand": "VISA"
            }
        ]
    }
}
```

### Created Identity

```javascript
{
  "type" : "created",
  "entity" : "identity",
  "occurred_at" : "2016-07-06T07:05:57.659",
  "_embedded" : {
    "identitys" : [ {
      "updated_at" : "2016-07-06T07:05:57.55Z",
      "created_at" : "2016-07-06T07:05:57.55Z",
      "id" : "IDt9PQrHhTmmwxHrmcxt46Eq",
      "entity" : {
        "title" : "CEO",
        "first_name" : "dwayne",
        "last_name" : "Sunkhronos",
        "email" : "user@example.org",
        "business_name" : "Bobs Burgers",
        "business_type" : "INTERNATIONAL_ORGANIZATION",
        "doing_business_as" : "Bobs Burgers",
        "phone" : "1234567890",
        "business_phone" : "+1 (408) 756-4497",
        "personal_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 7",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "business_address" : {
          "line1" : "741 Douglass St",
          "line2" : "Apartment 8",
          "city" : "San Mateo",
          "region" : "CA",
          "postal_code" : "94114",
          "country" : "USA"
        },
        "dob" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "discover_mid" : null,
        "url" : "www.BobsBurgers.com",
        "annual_card_volume" : 12000000,
        "has_accepted_credit_cards_previously" : true,
        "incorporation_date" : {
          "day" : 27,
          "month" : 6,
          "year" : 1978
        },
        "principal_percentage_ownership" : 50,
        "short_business_name" : null,
        "tax_id_provided" : true,
        "business_tax_id_provided" : true,
        "default_statement_descriptor" : "Bobs Burgers"
      },
      "tags" : {
        "key" : "value"
      }
    } ]
  }
}
```

### Provisioned Merchant

```javascript
{
  "type" : "created",
  "entity" : "merchant",
  "occurred_at" : "2017-11-30T23:29:22.877",
  "_embedded" : {
    "merchants" : [ {
      "updated_at" : "2017-11-30T23:29:22.25Z",
      "identity" : "IDbNi5P4w9QdMd6xdJq39V3s",
      "settlement_enabled" : true,
      "created_at" : "2017-11-30T23:29:22.12Z",
      "id" : "MUkAgao5qJNtpSdNJx5MXMgx",
      "processing_enabled" : true,
      "onboarding_state" : "APPROVED",
      "processor" : "DUMMY_V1",
      "verification" : null,
      "merchant_profile" : "MPvTW1DZihdgLS8yzAtdbjPf",
      "tags" : { }
    } ]
  }
}
```

### Successfully Underwritten Merchant

```javascript
{
  "type" : "created",
  "entity" : "verification",
  "occurred_at" : "2017-11-30T23:29:22.538",
  "_embedded" : {
    "verifications" : [ {
      "trace_id" : "d46e18d0-d171-4c4d-b0ff-3bac81a5324c",
      "updated_at" : "2017-11-30T23:29:22.33Z",
      "payment_instrument" : null,
      "identity" : null,
      "messages" : [ ],
      "raw" : "RawDummyMerchantUnderwriteResult",
      "created_at" : "2017-11-30T23:29:22.15Z",
      "merchant" : "MUkAgao5qJNtpSdNJx5MXMgx",
      "id" : "VI3o8e4ebrfo6NR7LuCNmmoz",
      "state" : "SUCCEEDED",
      "processor" : "DUMMY_V1",
      "tags" : {
        "key_2" : "value_2"
      }
    } ]
  }
}
```

### Created Dispute

```javascript
{
  "type" : "created",
  "entity" : "dispute",
  "occurred_at" : "2016-07-06T08:14:01.288",
  "_embedded" : {
    "disputes" : [ {
      "occurred_at" : "2016-07-06T08:13:47.56Z",
      "reason" : "FRAUD",
      "amount" : 0,
      "transfer" : "TRnEarDDVuVkBJLBL6PhZTLT",
      "updated_at" : "2016-07-06T08:14:01.18Z",
      "identity" : "ID4DFq8Q2V1zHoaU8WCTzpge",
      "created_at" : "2016-07-06T08:14:01.18Z",
      "id" : "DIvHQsw2tcwUhkMtzXVbksxo",
      "state" : "PENDING",
      "respond_by" : "2016-07-13T08:14:01.18Z",
      "tags" : {
        "order_number" : "21DFASJSAKAS"
      }
    } ]
  }
}
```

### Created Instrument Update

```javascript
{
  "type": "updated",
  "entity": "instrument_update",
  "occurred_at": "2017-08-14T14:17:43.004",
  "_embedded": {
    "instrument_updates": [{
      "trace_id": "FNXa2UvnrWMA6h4uER2F3wcg",
      "application": "APuEebjbpT8Baz8VqERaEx3z",
      "updated_at": "2017-08-14T14:17:42.97Z",
      "payment_instrument": "PIrgiJ1KtZVaT4dqDeDkveYh",
      "merchant": "MUxtD9KaVh1Ax5WRKBQZntPX",
      "messages": [
        "No match found"
      ],
      "created_at": "2017-08-09T23:58:05.74Z",
      "id": "IUkE7oida5Jupzd471HPkjqu",
      "state": "FAILED"
    }]
  }
}
```

### Update Payment Instrument

```javascript
{
    "type": "updated",
    "entity": "instrument",
    "occurred_at": "2019-10-16T23:13:12.133",
    "_embedded": {
        "instruments": [
            {
                "address": {
                    "line1": "900 Metro Center Blv",
                    "line2": null,
                    "city": "San Francisco",
                    "region": "CA",
                    "postal_code": "94404",
                    "country": "USA"
                },
                "address_verification": "UNKNOWN",
                "bin": "489514",
                "security_code_verification": "UNKNOWN",
                "created_at": "2019-10-16T23:13:11.90Z",
                "instrument_type": "PAYMENT_CARD",
                "card_type": "UNKNOWN",
                "type": "PAYMENT_CARD",
                "tags": {
                    "card_name": "Business Card"
                },
                "expiration_year": 2020,
                "application": "APf7avmNAHZ9Qtm2mENaGQT",
                "updated_at": "2019-10-16T23:13:11.91Z",
                "last_four": "0006",
                "identity": "IDxmDPpYkpQCaFj4LAnwXyJW",
                "fingerprint": "FPRogKWsRQks2HGaau5eGR9AF",
                "expiration_month": 3,
                "name": "Ayisha Curry",
                "currency": "USD",
                "id": "PIgSQx5XHNiwef1Bh87tzqNB",
                "brand": "VISA"
            }
        ]
    }
}
```


### Create Settlement  

```javascript
{
  "type": "created",
  "entity": "settlement",
  "occurred_at": "2018-03-06T20:41:34.277",
  "_embedded": {
    "settlements": [
      {
        "updated_at": "2018-03-06T20:41:34.00Z",
        "total_amount": 557710,
        "identity": "IDj4Y23Xd5Xn5vvtBR7gfxLM",
        "total_fees": 25402,
        "total_fee": 25402,
        "destination": null,
        "created_at": "2018-03-06T20:41:33.73Z",
        "currency": "USD",
        "id": "STqdtjFPKbcFZJ7VFpoQ4niu",
        "net_amount": 532308,
        "processor": "LITLE_V1",
        "tags": {}
      }
    ]
  }
}
```

### Fund Settlement  

```javascript
{
  "type": "updated",
  "entity": "settlement",
  "occurred_at": "2018-03-06T20:42:25.439",
  "_embedded": {
    "settlements": [
      {
        "updated_at": "2018-03-06T20:42:19.29Z",
        "total_amount": 557710,
        "identity": "IDj4Y23Xd5Xn5vvtBR7gfxLM",
        "total_fees": 25402,
        "total_fee": 25402,
        "destination": "PIreVTtPDXoRhww3VZiLZR3L",
        "created_at": "2018-03-06T20:41:33.73Z",
        "currency": "USD",
        "id": "STqdtjFPKbcFZJ7VFpoQ4niu",
        "net_amount": 532308,
        "processor": "LITLE_V1",
        "tags": {}
      }
    ]
  }
}
```

### Awaiting for Approval Settlement  (v2 Settlement Engine)

```javascript
{
  "type": "updated",
  "entity": "settlement_v2",
  "occurred_at": "2020-01-16T20:17:35.817",
  "_embedded": {
    "settlements_v2": [
      {
        "exception": false,
        "fee_count": 6,
        "processor_type": "DUMMY_V1",
        "created_at": "2020-01-15T01:27:04.36Z",
        "merchant_id": "MU87xmmN4pZZgm97Cok3oAp",
        "adjustment_credit_count": 0,
        "settlement_group_id": "SG5jV9hZJkp6a9i3WfJUja9q",
        "transfer_credit_count": 0,
        "adjustment_debit_count": 0,
        "transfer_debit_count": 2,
        "updated_at": "2020-01-16T20:17:08.85Z",
        "total_amount": 4000,
        "total_fee_amount": 338,
        "currency": "USD",
        "id": "ST5jVXU8pAv4CM23W1Y5bp85",
        "net_amount": 3662,
        "dispute_debit_count": 0,
        "reverse_count": 0,
        "status": "AWAITING_APPROVAL",
        "dispute_credit_count": 0
      }
    ]
  }
}
```

### Approved Settlement  (v2 Settlement Engine)

```javascript
{
  "type": "updated",
  "entity": "settlement_v2",
  "occurred_at": "2020-01-16T20:17:35.817",
  "_embedded": {
    "settlements_v2": [
      {
        "exception": false,
        "fee_count": 6,
        "processor_type": "DUMMY_V1",
        "created_at": "2020-01-15T01:27:04.36Z",
        "merchant_id": "MU87xmmN4pZZgm97Cok3oAp",
        "adjustment_credit_count": 0,
        "settlement_group_id": "SG5jV9hZJkp6a9i3WfJUja9q",
        "transfer_credit_count": 0,
        "adjustment_debit_count": 0,
        "transfer_debit_count": 2,
        "updated_at": "2020-01-16T20:17:08.85Z",
        "total_amount": 4000,
        "total_fee_amount": 338,
        "currency": "USD",
        "id": "ST5jVXU8pAv4CM23W1Y5bp85",
        "net_amount": 3662,
        "dispute_debit_count": 0,
        "reverse_count": 0,
        "status": "APPROVED",
        "dispute_credit_count": 0
      }
    ]
  }
}
```
