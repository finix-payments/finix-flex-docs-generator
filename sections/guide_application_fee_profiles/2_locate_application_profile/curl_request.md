curl {{staging_base_url}}/applications/{{fetch_application_scenario_id}}/application_profile \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
