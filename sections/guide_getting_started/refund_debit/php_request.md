use {{php_client_resource_name}}\Resources\Transfer;

$debit = Transfer::retrieve('{{create_debit_scenario_id}}');
$refund = $debit->reverse(50);