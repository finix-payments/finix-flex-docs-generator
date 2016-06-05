```
import io.finix.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);
```