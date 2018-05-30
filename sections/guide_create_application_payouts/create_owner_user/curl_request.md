curl {{staging_base_url}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username_payouts}}:{{platform_basic_auth_password_payouts}} \
    -d '{{create_owner_user_scenario_curl_request}}'
