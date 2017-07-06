merchant = {{ruby_client_resource_name}}::Merchant.retrieve(:id => "{{fetch_merchant_scenario_id}}")

verification = merchant.entity["default_statement_descriptor"] = "Prestige World Wide"
