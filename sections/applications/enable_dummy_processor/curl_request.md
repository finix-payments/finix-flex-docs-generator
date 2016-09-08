curl {{base_url}}/applications/{{create_app_scenario_id}}/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -d '{{associate_dummyV1_payment_processor_scenario_curl_request}}
