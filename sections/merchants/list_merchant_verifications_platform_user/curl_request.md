curl {{staging_base_url}}/merchants/{{fetch_merchant_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}}
