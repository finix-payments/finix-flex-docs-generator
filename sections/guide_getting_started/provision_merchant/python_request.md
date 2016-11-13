from {{python_client_resource_name}}.resources import Identity
from {{python_client_resource_name}}.resources import Merchant

identity = Identity.get(id="{{fetch_identity_scenario_id}}")
merchant = identity.provision_merchant_on(Merchant())