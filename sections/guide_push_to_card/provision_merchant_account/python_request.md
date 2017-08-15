from {{python_client_resource_name}}.resources import Identity
from {{python_client_resource_name}}.resources import Merchant

identity = Identity.get(id="{{create_recipient_card_scenario_id}}")
merchant = identity.provision_merchant_on(Merchant())
