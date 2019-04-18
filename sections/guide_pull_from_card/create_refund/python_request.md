from {{python_client_resource_name}}.resources import Transfer

transfer = Transfer.get(id="{{create_sender_push_to_card_transfer_id}}")
transfer.reverse(**{{create_refund_scenario_python_request}})
