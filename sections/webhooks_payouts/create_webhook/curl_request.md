curl {{staging_base_url}}/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{create_webhook_scenario_curl_request}}'
