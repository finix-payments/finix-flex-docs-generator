curl {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&outcome=PENDING  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} 
