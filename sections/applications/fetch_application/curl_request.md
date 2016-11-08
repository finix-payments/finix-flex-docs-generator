curl {{staging_base_url}}/applications/{{fetch_application_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}}
