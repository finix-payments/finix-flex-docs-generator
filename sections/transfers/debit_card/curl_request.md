curl {{staging_base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_card_debit_scenario_curl_request}}'
