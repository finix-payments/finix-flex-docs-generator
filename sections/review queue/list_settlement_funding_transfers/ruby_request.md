settlement = {{ruby_client_resource_name}}::Settlement.retrieve(:id=>"{{fetch_settlement_scenario_id}}")
transfers = settlement.funding_transfers