curl {{staging_base_url}}/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_authorization_idempotency_scenario_curl_request}}'
