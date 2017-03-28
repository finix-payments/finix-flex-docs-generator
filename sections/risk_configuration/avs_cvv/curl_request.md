curl {{staging_base_url}}/risk_profiles/{{fetch_risk_profile_scenario_id}}/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    -X PUT \
    -d '{{avs_scenario_curl_request}}'
