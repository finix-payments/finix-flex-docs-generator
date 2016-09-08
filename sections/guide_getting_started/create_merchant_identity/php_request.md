use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_merchant_identity_scenario_php_request}}
);
$identity = $identity->save();
