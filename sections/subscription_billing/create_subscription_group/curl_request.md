curl {{staging_base_url}}/subscription/subscription_schedules \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{create_subscription_plan_scenario_curl_request}}'
