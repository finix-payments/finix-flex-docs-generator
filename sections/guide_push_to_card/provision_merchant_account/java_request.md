Identity identity = client.identitiesClient().fetchResource("{{create_recipient_card_scenario_id}}");
identity.provisionMerchantOn(Merchant.builder().build());