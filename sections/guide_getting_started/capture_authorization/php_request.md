use {{api_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
