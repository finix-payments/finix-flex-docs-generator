curl {{staging_base_url}}/disputes/{{fetch_dispute_scenario_id}}/evidence \
    -H "Content-Type: application/pdf/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}} \
    -F 'data=@path/to/local/file' testfile.pdf
