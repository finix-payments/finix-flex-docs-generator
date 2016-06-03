
curl {{base_url}}/identities/{{create_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{underwrite_identity_scenario_curl_request}}"

