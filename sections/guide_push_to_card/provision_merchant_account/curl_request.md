curl https://api-staging.finix.io/identities/'{{provision_merchant_account_scenario_id}}'/merchants \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -d '{{provision_merchant_account_scenario_curl_request}}'