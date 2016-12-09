transfer = {{ruby_client_resource_name}}::Transfer.find(:id=> "{{fetch_transfer_scenario_id}}")

refund = {{ruby_client_resource_name}}::Transfer.reverse({{create_refund_scenario_ruby_request}}).save