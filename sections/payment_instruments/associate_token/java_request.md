import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCardToken;

PaymentCard paymentCard = client.paymentCardsClient().save(
  PaymentCardToken.builder()
    .type("TOKEN")
    .token("{{create_token_scenario_id}}")
    .identity("{{fetch_identity_scenario_id}}")
    .build()
);
