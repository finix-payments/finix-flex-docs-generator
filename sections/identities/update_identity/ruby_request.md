identity = {{ruby_client_resource_name}}::Identity.retrieve(:id=>"{{fetch_identity_scenario_id}}")

identity.entity["first_name"] = "Bernard"
identity.save