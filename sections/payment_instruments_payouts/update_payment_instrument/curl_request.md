curl {{staging_base_url}}/payment_instruments/{{update_payment_instrument_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{update_payment_instrument_scenario_curl_request}}'
