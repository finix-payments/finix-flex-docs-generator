use {{php_client_resource_name}}\Resources\Transfer;

$debit = new Transfer({{create_sale_scenario_php_request}});
$debit = $debit->save();
