
curl {{base_url}}/settlements/{{fetch_settlement_scenario_id}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}
