import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .type("TOKEN")
    .token("{{associate_token_scenario_id}}")
    .identity("{{fetch_identity_scenario_id}}")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);

