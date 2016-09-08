
curl {{base_url}}/authorizations/{{void_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{void_authorization_scenario_curl_request}}'
