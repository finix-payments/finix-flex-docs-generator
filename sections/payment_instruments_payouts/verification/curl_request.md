curl {{staging_base_url}}/payment_instruments/{{fetch_credit_card_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{payment_instrument_verification_scenario_curl_request}}'
