transfer = {{ruby_client_resource_name}}::Transfer.retrieve(:id=>"{{fetch_transfer_scenario_id}}")

transfer.tags = {"order_number"=> "12121212"}
