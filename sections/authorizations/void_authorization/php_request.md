use {{php_client_resource_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{create_authorization_scenario_id}}');
$authorization->void(true);
$authorization = $authorization->save();

