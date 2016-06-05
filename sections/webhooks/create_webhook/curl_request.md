
curl {{base_url}}/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_webhook_scenario_curl_request}}'
