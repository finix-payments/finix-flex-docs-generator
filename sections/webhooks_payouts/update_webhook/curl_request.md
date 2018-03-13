curl {{staging_base_url}}/webhooks/{{fetch_webhook_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{update_webhook_scenario_curl_request}}'
