use {{php_client_resource_name}}\Resources\Application;

$application = new Application({{create_app_scenario_php_request}});
$application = $application->save();