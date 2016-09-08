use {{api_name}}\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument({{create_bank_account_scenario_php_request}});
$bank_account = $bank_account->save();
