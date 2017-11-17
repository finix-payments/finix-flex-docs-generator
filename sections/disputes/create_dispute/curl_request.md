curl {{staging_base_url}}/disputes \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    <!-- -d '{{create_dispute_scenario_request}}' -->
    -d '{{create_dispute_scenario_curl_request}}'
