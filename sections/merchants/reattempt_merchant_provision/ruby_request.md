identity = {{ruby_client_resource_name}}::Identity('{{create_merchant_identity_scenario_id}}');

merchant = identity.veryify_on(:processor => 'DUMMY_V1')