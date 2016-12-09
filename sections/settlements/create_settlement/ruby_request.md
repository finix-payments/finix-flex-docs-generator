identity = {{ruby_client_resource_name}}::Identity.find(:id=>"{{create_merchant_identity_scenario_id}}")
settlement = identity.create_settlement({{create_settlement_scenario_ruby_request}})