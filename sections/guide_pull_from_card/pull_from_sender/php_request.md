use {{php_client_resource_name}}\Resources\Transfer;

$transfer = new Transfer({{create_sender_push_to_card_transfer_php_request}});
$transfer = $transfer->save();
