from {{python_client_resource_name}}.resources import Settlements
settlement = Settlement.get(id="{{fetch_settlement_scenario_id}}")
transfers = settlement.funding_transfers
