curl {{staging_base_url}}/payment_instruments/{{create_card_verification_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{payment_instrument_verification_payouts_scenario_curl_request}}'
