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