use {{php_client_resource_name}}\Resources\Identity;

$identity = new Identity({{create_buyer_identity_scenario_php_request}});
$identity = $identity->save();
