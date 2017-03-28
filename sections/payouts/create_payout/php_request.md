use {{php_client_resource_name}}\Resources\Transfer;

$debit = new Transfer({{create_recipient_push_to_card_transfer_php_request}});
$debit = $debit->save();