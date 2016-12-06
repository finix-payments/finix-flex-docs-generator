use {{api_name}}\Resources\Authorization;

$authorization = new Authorization({{create_authorization_scenario_php_request}});
$authorization = $authorization->save();

$authorization = Authorization::retrieve('{{create_authorization_scenario_id}}');
$authorization->void(true);
$authorization = $authorization->save();

