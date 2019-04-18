from {{python_client_resource_name}}.resources import Transfer
transfer = Transfer.get(id="{{fetch_transfer_scenario_id}}")

transfer.tags["order_number"] = "12121212"
transfer.save()
