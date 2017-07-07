from {{python_client_resource_name}}.resources import PaymentCard

card = PaymentCard(**{{create_card_scenario_python_request}}).save()
check_for_updates = card.update("{{fetch_merchant_scenario_id}}")
