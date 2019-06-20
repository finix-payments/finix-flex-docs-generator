curl {{staging_base_url}}/transfers/{{fetch_transfer_scenario_id}}/
-H "Content-Type: application/vnd.json+api"
-u {{basic_auth_username}}:{{basic_auth_password}}
-X PUT
-d '{{update_transfer_scenario_curl_request}}'
