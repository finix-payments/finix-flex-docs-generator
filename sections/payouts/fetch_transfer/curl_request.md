curl {{staging_base_url}}/transfers/{{fetch_transfer_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}}
