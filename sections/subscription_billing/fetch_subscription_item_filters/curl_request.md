curl {{staging_base_url}}/subscription/subscription_items?subscription_group_id={{fetch_subscription_group_scenario_response_id}}&merchant_id={{provision_merchant_scenario_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
