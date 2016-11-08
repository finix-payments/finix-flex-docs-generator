from {{python_client_resource_name}}.resources import Authorization

authorization = Authorization.get(id="{{fetch_authorization_scenario_id}}")
authorization.capture(**{{capture_authorization_scenario_python_request}})
