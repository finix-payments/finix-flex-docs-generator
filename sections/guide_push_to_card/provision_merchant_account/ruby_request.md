identity = {{ruby_client_resource_name}}::Identity.find(:id=>"{{create_recipient_card_scenario_id}}")

merchant = identity.provision_merchant_on()