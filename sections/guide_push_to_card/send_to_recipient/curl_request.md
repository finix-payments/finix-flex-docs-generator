curl {{staging_base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d '{{create_recipient_push_to_card_transfer_curl_request}}'
