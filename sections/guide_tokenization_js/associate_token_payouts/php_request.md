use {{php_client_resource_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_php_request}});
$card = $card->save();
