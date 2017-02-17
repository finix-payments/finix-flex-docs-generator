transfer = {{ruby_client_resource_name}}::Transfer.retrieve(:id=> "{{fetch_transfer_scenario_id}}")

refund = transfer.reverse(100)
