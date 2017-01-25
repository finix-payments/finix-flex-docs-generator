import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("{{provision_merchant_scenario_id}}")
    .source("{{create_card_scenario_id}}")
    .build()
);
