
import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("{{create_merchant_identity_scenario_id}}")
      .source("{{create_card_scenario_id}}")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .build()
);
