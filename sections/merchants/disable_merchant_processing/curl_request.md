curl {{staging_base_url}}/merchants/{{fetch_merchant_scenario_id}}/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -X PUT \
    -d '{{toggle_merchant_processing_scenario_curl_request}}'