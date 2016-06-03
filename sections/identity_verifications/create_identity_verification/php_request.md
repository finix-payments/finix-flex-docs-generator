use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{underwrite_identity_scenario_php_request}});