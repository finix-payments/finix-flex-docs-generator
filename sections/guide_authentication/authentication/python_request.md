from {{api_name_downcase}}.config import configure
configure(root_url="{{staging_base_url}}", auth=("{{basic_auth_username}}", "{{basic_auth_password}}"))
