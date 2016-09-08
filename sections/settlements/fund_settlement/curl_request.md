curl {{base_url}}/settlements/{{create_settlement_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -X PUT \
    -d '{{fund_settlement_scenario_curl_request}}'
