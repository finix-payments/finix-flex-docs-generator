curl {{staging_base_url}}/settlements/{{create_settlement_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -X PUT \
    -d '{{fund_settlement_scenario_curl_request}}'
