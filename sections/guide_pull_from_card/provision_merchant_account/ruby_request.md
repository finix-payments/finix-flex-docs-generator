identity = {{ruby_client_resource_name}}::Identity.retrieve(:id=>"{{create_sender_identity_payouts_scenario_id}}")

merchant = identity.provision_merchant
