Identity identity = client.identitiesClient().fetchResource("{{create_recipient_identity_payouts_scenario_id}}");
identity.provisionMerchantOn(Merchant.builder().build());