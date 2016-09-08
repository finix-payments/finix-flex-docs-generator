curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_merchant_identity_scenario_curl_request}}'
