from {{python_client_resource_name}}.resources import Merchant
merchant = Merchant.get(id="{{fetch_merchant_scenario_id}}")

merchant.entity["first_name"] = "Michael"
merchant.save()
