curl {{staging_base_url}}/merchant_profiles/{{fetch_merchant_profile_id}}/ \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{admin_basic_auth_username}}:{{admin_basic_auth_password}} \
    