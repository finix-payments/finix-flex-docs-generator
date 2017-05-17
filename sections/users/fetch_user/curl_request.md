curl {{staging_base_url}}/users/{{fetch_user_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
