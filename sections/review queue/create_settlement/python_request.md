from {{python_client_resource_name}}.resources import Identity
from {{python_client_resource_name}}.resources import Settlement

identity = Identity.get(id="{{fetch_identity_scenario_id}}")
settlement = Settlement(**{{create_settlement_scenario_python_request}})
identity.create_settlement(settlement)