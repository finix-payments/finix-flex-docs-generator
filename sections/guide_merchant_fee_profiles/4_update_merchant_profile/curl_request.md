curl {{staging_base_url}}/merchant_profiles/{{update_merchant_profile_scenario_response_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{update_merchant_profile_scenario_curl_request}}'
