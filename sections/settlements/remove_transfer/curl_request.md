
curl {{staging_base_url}}/settlements/{{fetch_transfer_scenario_id}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{remove_transfer_scenario_curl_request}}'
