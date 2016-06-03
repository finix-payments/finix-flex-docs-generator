From your `identity`

```
import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)
```

or from your `client`

```
import io.payline.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().save(
    Settlement.builder()
        .processor("DUMMY_V1")
        .currency("USD")
        .build()
);
```