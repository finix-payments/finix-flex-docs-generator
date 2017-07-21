from {{python_client_resource_name}}.resources import Transfer
transfer = Transfer.get(id="{{fetch_transfer_scenario_id}}")

refund = transfer.reverse(**{{create_refund_scenario_python_request}})
refund.tags["order_number"] = "12121212"
refund.save()
