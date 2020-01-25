use {{php_client_resource_name}}\Resources\Transfer;

$debit = Transfer::retrieve('{{create_sender_push_to_card_transfer_id}}');
$refund = $debit->reverse(11);
