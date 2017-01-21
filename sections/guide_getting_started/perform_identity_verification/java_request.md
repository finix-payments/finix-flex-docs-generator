
import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = identity.verify(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);
