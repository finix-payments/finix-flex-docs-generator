curl {{staging_base_url}}/users/{{disable_user_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{disable_user_scenario_curl_request}}'
