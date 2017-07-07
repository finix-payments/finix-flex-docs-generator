from {{python_client_resource_name}}.resources import Merchant

merchant_identity = Merchant.get(id="{{fetch_merchant_scenario_id}}")

provision_merchant = merchant_identity.provision_merchant_on(Merchant())

list_all_merchant_verifications = provision_merchant.verifications
