curl {{staging_base_url}}/settlement/settlements/{{fetch_settlement_split_payout_id}}/funding_instructions \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{platform_basic_auth_username}}:{{platform_basic_auth_password}} \
    -d '{{create_settlement_split_payout_equation_scenario}}'
