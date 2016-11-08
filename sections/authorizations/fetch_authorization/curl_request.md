
curl {{staging_base_url}}/authorizations/{{fetch_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}
