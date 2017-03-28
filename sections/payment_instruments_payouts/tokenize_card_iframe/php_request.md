use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{associate_token_scenario_curl_request}});
$card = $card->save();
