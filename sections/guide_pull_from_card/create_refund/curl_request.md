
curl {{staging_base_url}}/transfers/{{create_sender_push_to_card_transfer_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username_payouts}}:{{basic_auth_password_payouts}} \
    -d  '{{create_refund_aft_scenario_curl_request}}'
