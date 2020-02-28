> Example Response:

```json
{{create_settlement_split_payout_explicit_scenario_response}}
```

<aside class="notice">
Only a User with ROLE_PLATFORM level credentials can use the Split Payout feature.
</aside>

Gives the user the ability to update what the funding instruction amounts will be. If funding instructions have been manually overridden we will not rerun our calculations.

#### HTTP Request

`POST {{staging_base_url}}//settlement/settlements/:SETTLEMENT_ID/funding_instructions`

#### User-specific Request Arguments

Field | Type | Description
----- | ---- | -----------
type | *string*, **required** | The type of how the new funding instructions will be recalculated (EXPLICIT_AMOUNTS, NEW_EQUATIONS)
name | *string*, **required** | Name that will be given to the funding instruction (i.e. MERCHANT_FUNDING_INSTRUCTION_SPLIT_1)
level                     | *string*, **required** | Level describing who will be paid (PLATFORM, APPLICATION, MERCHANT)
amount                    | *string*, **required** | Amount of the funding instruction. Required when type = EXPLICIT_AMOUNTS
currency                  | *string*, **required** | 3-letter ISO code designating the currency of the Transfers (e.g. USD)
source_instrument_id      | *string*, **required** | Will likely remove the ID from the payload
destination_instrument_id | *string*, **required** | ID of the Payment Instrument where funds will be sent
rail                      | *string*, **required** | The rail that will be used for the funding instruction (PAYFAC_CREDIT, SAME_DAY_ACH, NOOP)
