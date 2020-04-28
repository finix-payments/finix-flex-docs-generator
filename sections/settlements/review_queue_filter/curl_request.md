curl {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&entity_id={{review_queue_filter_entity_id}}  \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
