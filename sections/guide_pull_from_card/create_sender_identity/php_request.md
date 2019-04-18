use {{php_client_resource_name}}\Resources\Identity;

$identity = new Identity({{create_sender_identity_payouts_scenario_id}});
$identity = $identity->save();
