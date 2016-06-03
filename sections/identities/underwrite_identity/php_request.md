use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{underwrite_identity_scenario_php_request}});