
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("{{create_token_scenario}}")
    .identity("{{fetch_identity_scenario_id}}")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);
