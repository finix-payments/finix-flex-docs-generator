transfer = {{ruby_client_resource_name}}::Transfer.retrieve(:id=>"{{update_identity_scenario_id}}")

refund = transfer.reverse("{create_refund_scenario_ruby_request}}")
refund.tags = {"order_number"=> "12121212"}
refund.save
