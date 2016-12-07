use {{api_name}}\Resources\PaymentCard;
use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_recipient_identity_scenario_id}}');
$card = new PaymentCard({{create_recipient_card_scenario_php_request}});
$card = $identity->createPaymentCard($card);
