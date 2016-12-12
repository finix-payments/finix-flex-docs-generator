identity = {{ruby_client_resource_name}}::Identity.retrieve(:id=>"{{create_merchant_identity_scenario_id}}")

merchant = identity.provision_merchant