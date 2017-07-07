from {{python_client_resource_name}}.resources import Merchant
from {{python_client_resource_name}}.resources import Verification

merchant = Merchant.get(id="{{fetch_merchant_scenario_id}}")

reattempt_merchant_provision = merchant.verify_on(Verification())
