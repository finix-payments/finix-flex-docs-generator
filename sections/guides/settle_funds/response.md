> Example Response:

```json
{{create_settlement_scenario_response}}
```

Awesome! Now you know how to charge a card and reverse the debit.

Now you need to settle out the funds to your merchant. To do so you will create a Settlement resource. Each settlement is comprised of all the Transfers that have a SUCCEEDED state and that have not been previously settled out.