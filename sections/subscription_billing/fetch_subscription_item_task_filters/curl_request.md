curl {{staging_base_url}}/subscription/subscription_items/{{create_subsciption_item_scenario_response_id}}/subscription_item_tasks?state=CANCELLED&merchant_id={{fetch_merchant_scenario_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
