curl {{staging_base_url}}/merchants/{{fetch_merchant_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}
