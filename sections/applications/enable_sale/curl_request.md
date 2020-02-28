curl {{staging_base_url}}/applications/{{create_app_scenario_id}}/processors/DUMMY_V1 \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{enable_sale_scenario_curl_request}}'
