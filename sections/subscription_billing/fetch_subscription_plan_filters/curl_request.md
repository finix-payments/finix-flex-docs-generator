curl {{staging_base_url}}/subscription/subscription_plans?name=plan_name&subscription_plan_type=FEE  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
