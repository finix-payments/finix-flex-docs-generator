curl {{staging_base_url}}/merchants/{{fetch_merchant_settle_upon_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -X PUT \
    -d '{{merchant_settle_upon_scenario_curl_request}}'
