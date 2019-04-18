use {{php_client_resource_name}}\Resources\PaymentCard;
use {{php_client_resource_name}}\Resources\Identity;

$card = new PaymentCard({{create_recipient_card_scenario_php_request}});
$card = $identity->createPaymentCard($card);
