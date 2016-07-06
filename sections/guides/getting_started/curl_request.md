

# With cURL, just supply your username as basic auth (-u) in the header of each request as follows:

curl "api_endpoint_here" \
    -H "Content-Type: application/vnd.json+api" \
    -u  {{basic_auth_username}}:{{basic_auth_password}}
