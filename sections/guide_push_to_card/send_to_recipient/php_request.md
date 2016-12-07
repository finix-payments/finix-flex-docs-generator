use {{api_name}}\Resources\Transfer;

$transfer = new Transfer({{create_recipient_push_to_card_transfer_php_request}});
$transfer = $transfer->save();