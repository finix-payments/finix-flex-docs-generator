curl {{staging_base_url}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -d '{{create_owner_user_scenario_curl_request}}'
