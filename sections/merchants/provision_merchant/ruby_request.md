identity = {{ruby_client_resource_name}}::Identity.find(:id => "{{fetch_merchant_scenario_id}}")

merchant = identity.provision_merchant_on()