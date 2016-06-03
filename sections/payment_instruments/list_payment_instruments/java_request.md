`BankAccount`

```
import io.payline.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });
```

`PaymentCard`

```
import io.payline.payments.processing.client.model.PaymentCard;

client.paymentCardsClient().<Resources<PaymentCard>>resourcesIterator()
  .forEachRemaining(paPage -> {
    Collection<PaymentCard> paymentCards = paPage.getContent();
    //do something
  });
```