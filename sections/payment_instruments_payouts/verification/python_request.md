from {{python_client_resource_name}}.resources import PaymentInstrument
from {{python_client_resource_name}}.resources import Verification


payment_card = PaymentInstrument.get(id="{{create_card_verification_scenario_id}}")

verify = payment_card.verify_on(Verification(**{{payment_instrument_verification_payouts_scenario_python_request}}))
