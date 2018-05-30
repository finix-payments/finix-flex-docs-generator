curl {{staging_base_url}}/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username_payouts}}:{{platform_basic_auth_password_payouts}} \
    -d '{{create_app_scenario_curl_request}}'
