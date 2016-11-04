curl {{staging_base_url}}/identities/{{create_merchant_identity_scenario_id}}/users \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{}'
