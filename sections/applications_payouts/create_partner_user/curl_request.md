curl {{staging_base_url}}/applications/{{create_app_scenario_id}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{}'
