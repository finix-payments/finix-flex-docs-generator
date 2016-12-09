identity = {{ruby_client_resource_name}}::Identity.find(:id=>"{{fetch_identity_scenario_id}}")

identity.entity["first_name"] = "Bernard"
identity.save