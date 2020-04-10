curl {{staging_base_url}}/subscription/subscription_group/{{fetch_subscription_group_scenario_response_id}}/subscription_items \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{create_subsciption_item_scenario_curl_request}}'
