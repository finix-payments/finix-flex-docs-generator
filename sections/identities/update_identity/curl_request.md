curl {{base_url}}/identities/{{update_identity_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{update_identity_scenario_curl_request}}'
