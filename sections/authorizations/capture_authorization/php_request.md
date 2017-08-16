use {{php_client_resource_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');
$authorization = $authorization->capture([
                    "capture_amount"=> 50,
                    "fee"=> 10
                ]);
