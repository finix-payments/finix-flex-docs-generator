
import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .destination("{{create_recipient_card_scenario_id}}")
      .amount(8888)
      .currency("USD")
      .tags(tags)
      .build()
);
