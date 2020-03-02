curl {{staging_base_url}}/subscription/subscription_schedules?name=test_subscription_schedule&subscription_type=PERIODIC  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
