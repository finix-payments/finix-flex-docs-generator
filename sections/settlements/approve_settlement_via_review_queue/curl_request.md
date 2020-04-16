curl {{staging_base_url}/review_queue/{{approve_settlement_via_review_queue_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d {{approve_settlement_via_review_queue_scenario_curl_request}}
