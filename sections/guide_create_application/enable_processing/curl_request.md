curl {{staging_base_url}}/applications/{{fetch_application_scenario_id}}/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -X PUT \
    -d '{{toggle_on_application_processing_scenario_curl_request}}'
