curl {{staging_base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{create_recipient_card_scenario_curl_request}}'
