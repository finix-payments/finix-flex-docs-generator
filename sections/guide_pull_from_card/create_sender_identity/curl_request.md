curl {{staging_base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{create_sender_identity_payouts_scenario_curl_request}}'
