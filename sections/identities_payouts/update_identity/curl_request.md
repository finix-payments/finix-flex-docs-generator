curl {{staging_base_url}}/identities/{{update_identity_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -X PUT \
    -d '{{update_identity_scenario_curl_request}}'
