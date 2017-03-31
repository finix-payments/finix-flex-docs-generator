PaymentCardToken paymentCard = PaymentCardToken.builder()
    .type(TOKEN)
    .token("{{create_token_scenario_id}}")
    .identity("{{fetch_identity_scenario_id}}")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);
