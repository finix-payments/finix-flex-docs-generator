from {{python_client_resource_name}}.resources import Transfer

payout = Transfer(**{{create_bank_debit_idempotency_scenario_python_request}}).save()
