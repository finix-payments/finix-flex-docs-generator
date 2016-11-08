curl {{staging_base_url}}/applications/{{create_app_scenario_id}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{}'
