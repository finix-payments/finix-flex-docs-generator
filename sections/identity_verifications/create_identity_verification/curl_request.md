

curl {{staging_base_url}}/identities/{{create_merchant_identity_scenario_id}}/verifications \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{create_identity_verification_scenario_curl_request}}'
