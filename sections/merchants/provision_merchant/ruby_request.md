identity = {{ruby_client_resource_name}}::Identity.retrieve(:id => "{{fetch_merchant_scenario_id}}")

merchant = identity.provision_merchant