use {{php_client_resource_name}}\Resources\Transfer;

$debit = Transfer::retrieve('{{create_bank_debit_scenario_id}}');
$refund = $debit->reverse(11);
