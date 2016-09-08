curl {{base_url}}/applications/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -d '{{create_app_scenario_curl_request}}'
