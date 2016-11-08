from {{python_client_resource_name}}.resources import Authorization
authorization = Authorization(**{{create_authorization_scenario_python_request}}).save()


from finix.resources import Authorization
 +
 +authorization = Authorization.get(id="{{fetch_authorization_scenario_id}}")