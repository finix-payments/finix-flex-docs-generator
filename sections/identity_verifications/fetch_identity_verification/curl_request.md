
curl {{base_url}}/verifications/{{fetch_identity_verification_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}
