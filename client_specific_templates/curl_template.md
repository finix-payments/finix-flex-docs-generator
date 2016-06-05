

# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:
curl "api_endpoint_here"
-u {{basic_auth_username}}:{{basic_auth_password}}



curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_merchant_identity_scenario_curl_request}}'


curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{create_bank_account_scenario_curl_request}}"




curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_identity_verification_scenario_curl_request}}'


curl {{base_url}}/identities/{{create_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{underwrite_identity_scenario_curl_request}}'




curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_buyer_identity_scenario_curl_request}}'



curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_card_scenario_curl_request}}'




curl {{base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_debit_scenario_curl_request}}'



curl {{base_url}}/transfers/{{create_debit_scenario_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d  '{{create_refund_scenario_curl_request}}'


curl {{base_url}}/identities/{{create_identity_scenario_id}}/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_settlement_scenario_curl_request}}'


curl {{base_url}}/authorizations \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_authorization_scenario_curl_request}}'




curl {{base_url}}/authorizations/{{fetch_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -X PUT \
    -d '{{capture_authorization_scenario_curl_request}}'


curl {{base_url}}/authorizations/{{fetch_authorization_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}


curl {{base_url}}/disputes/{{fetch_dispute_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}




curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_buyer_identity_scenario_curl_request}}'



curl {{base_url}}/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_merchant_identity_scenario_curl_request}}'


curl {{base_url}}/identities/{{fetch_identity_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}


curl {{base_url}}/identities/{{create_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{underwrite_identity_scenario_curl_request}}'




curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_identity_verification_scenario_curl_request}}'


curl {{base_url}}/verifications/{{fetch_identity_verification_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}


curl {{base_url}}/identities/{{create_identity_scenario_id}}/settlements \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_settlement_scenario_curl_request}}'



curl {{base_url}}/settlements/{{fetch_settlement_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \



curl {{base_url}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_debit_scenario_curl_request}}'



curl {{base_url}}/transfers/{{create_debit_scenario_id}}/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d  '{{create_refund_scenario_curl_request}}'


curl {{base_url}}/transfers/{{fetch_transfer_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}



curl {{base_url}}/webhooks \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_webhook_scenario_curl_request}}'




curl {{base_url}}/webhooks/{{fetch_webhook_scenario_id}} \
    -H "Content-Type: application/vnd.json+api" \
    -u {{basic_auth_username}}:{{basic_auth_password}}




curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_card_scenario_curl_request}}'



curl {{base_url}}/payment_instruments \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_bank_account_scenario_curl_request}}'




curl {{base_url}}/payment_instruments/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \



curl {{base_url}}/identities/{{create_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d "{{create_identity_verification_scenario_curl_request}}"

