
curl {{staging_base_url}}/identities/{{create_merchant_identity_scenario_id}}/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{provision_merchant_scenario_curl_request}}'

