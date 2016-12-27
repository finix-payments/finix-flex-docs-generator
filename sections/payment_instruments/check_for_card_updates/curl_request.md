curl {{staging_base_url}}/payment_instruments/'{{fetch_payment_instrument_scenario_id}}'/updates \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{check_for_card_updates_scenario_curl_request}}'
