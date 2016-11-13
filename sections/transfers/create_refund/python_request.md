from {{python_client_resource_name}}.resources import Transfer

transfer = Transfer.get(id="{{fetch_transfer_scenario_id}}")
transfer.reverse(**{{create_refund_scenario_python_request}})