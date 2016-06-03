
> Example Response:

```json
{{create_debit_scenario_response}}
```

At this point we've created resources representing the merchant, the buyer, and the buyer's card.

To debit a card, you'll need to create a Transfer. What's a Transfer? Glad you asked! A Transfer is basically any omnidirectional flow of funds. In other words, a Transfer can be a debit to a card, a credit to a bank account, or even a refund. For now let's focus on charging a card.

To do this we'll supply the buyer's Payment Instrument ID as the source and the seller's Identity ID as the merchant_identity. Note that the 'amount' field is amount in cents of the debit that will be charged on the card. The fee field is the amount in cents you would like to collect out of the debit amount before settling out to the merchant. Therefore, the fee must be equal or less than the amount field.

Simple enough, right? You'll also want to store the ID from that Transfer for your records. For the last section of this guide where we'll be showing you how to issue a refund.

