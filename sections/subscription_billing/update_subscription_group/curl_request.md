curl {{staging_base_url}}/subscription/subscription_groups/{{create_subscription_group_scenario_response_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -X PATCH \
    -d '{{update_subsciption_group_scenario_curl_request}}'
