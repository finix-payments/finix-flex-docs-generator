curl {{staging_base_url}}/settlement_engine/settlements/{{list_settlement_transfers_v2_scenario_id}}/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}