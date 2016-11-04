curl {{staging_base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_recipient_push_to_card_transfer_curl_request}}'
