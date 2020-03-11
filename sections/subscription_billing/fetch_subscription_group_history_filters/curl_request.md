curl {{staging_base_url}}/subscription/subscription_groups/{{fetch_subscription_group_scenario_response_id}}/subscription_group_histories?subscription_schedule_id={{create_subscription_schedule_scenario_id}}&subscription_plan_id={{create_subscription_plan_scenario_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
