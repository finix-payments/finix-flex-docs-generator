authorization = {{ruby_client_resource_name}}::Authorization.find(:id=>{{fetch_authorization_scenario_id}})
authorization = authorization.capture(:capture_amount => 50, :fee => 10)