from {{python_client_resource_name}}.resources import Identity

identity = Identity.get(id="{{fetch_identity_scenario_id}}")
identity.entity["first_name"] = "Bernard"
identity.save()
