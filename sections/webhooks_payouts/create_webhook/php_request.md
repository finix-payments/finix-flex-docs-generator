use {{php_client_resource_name}}\Resources\Webhook;

$webhook = new Webhook({{create_webhook_scenario_php_request}});
$webhook = $webhook->save();
