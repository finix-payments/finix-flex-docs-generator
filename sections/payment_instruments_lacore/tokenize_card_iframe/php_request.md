use {{php_client_resource_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_curl_request}});
$card = $card->save();
