curl {{staging_base_url}}/applications/{{create_app_scenario_id}}/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{associate_dummyV1_payment_processor_scenario_curl_request}}
