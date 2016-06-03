use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{create_card_scenario_php_request}});
$card = $card->save();

