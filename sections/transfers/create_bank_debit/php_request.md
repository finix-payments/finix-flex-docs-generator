use {{api_name}}\Resources\Transfer;

$debit = new Transfer({{create_debit_scenario_php_request}});
$debit = $debit->save();