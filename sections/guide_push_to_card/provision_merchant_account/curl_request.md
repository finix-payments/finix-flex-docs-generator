curl {{staging_base_url}}/identities/{{create_recipient_identity_payouts_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{provision_push_merchant_scenario_curl_request}}'
