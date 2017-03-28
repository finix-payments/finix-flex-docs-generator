use {{php_client_resource_name}}\Resources\Identity;

$identity = new Identity({{create_recipient_identity_payouts_scenario_php_request}});
$identity = $identity->save();
