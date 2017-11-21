curl {{staging_base_url}}/fee_profiles \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{create_application_fee_profile_scenario_curl_request}}'
