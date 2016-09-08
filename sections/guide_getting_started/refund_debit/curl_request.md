
curl {{base_url}}/transfers/{{create_debit_scenario_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d  '{{create_refund_scenario_curl_request}}'
