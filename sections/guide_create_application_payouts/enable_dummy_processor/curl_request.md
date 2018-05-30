curl {{staging_base_url}}/applications/{{create_app_scenario_id}}/processors \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username_payouts}}:{{platform_basic_auth_password_payouts}} \
    -d '{{associate_visaV1_payment_processor_scenario_curl_request}}'
