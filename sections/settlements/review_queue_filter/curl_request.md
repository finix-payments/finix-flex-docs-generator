<<<<<<< HEAD
curl {{staging_base_url}}//review_queue?entity_type=SETTLEMENT&entity_id={{review_queue_filter_entity_id}}  \
=======
curl {{staging_base_url}}/review_queue?entity_type=SETTLEMENT&entity_id={{review_queue_filter_entity_id}}  \
>>>>>>> c76305dcb707c22a18d0678af1eabb4f77792ca5
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}}
