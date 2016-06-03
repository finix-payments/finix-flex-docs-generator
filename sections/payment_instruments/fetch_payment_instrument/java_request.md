`BankAccount`

```
import io.finix.payments.processing.client.model.BankAccount;

BankAccount bankAccount = client.bankAccountsClient().fetch("PIi98CoYWpQZi8w7ZimJxuJ")
```

`PaymentCard`

```
import io.finix.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("PIi98CoYWpQZi8w7ZimJxuJ");
```