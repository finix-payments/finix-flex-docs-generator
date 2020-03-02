
curl {{staging_base_url}}/subscription/subscription_items/{{create_subsciption_item_scenario_response_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -X DELETE\
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
