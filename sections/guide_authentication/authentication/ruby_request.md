# To download the Ruby gem:
# gem install {{ruby_gem}}

require '{{ruby_require_statement}}'

{{ruby_client_resource_name}}.configure(
    :root_url => '{{staging_base_url}}',
    :user=>'{{basic_auth_username}}',
    :password => '{{basic_auth_password}}'
)