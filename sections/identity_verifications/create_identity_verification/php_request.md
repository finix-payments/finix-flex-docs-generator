use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_merchant_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{provision_merchant_scenario_php_request}});