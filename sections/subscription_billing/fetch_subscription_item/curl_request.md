
curl {{staging_base_url}}/subscription/subscription_schedules/{{create_subsciption_item_scenario_response_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
