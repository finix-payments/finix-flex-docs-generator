use {{api_name}}\Resources\PaymentCard;
use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$card = new PaymentCard({{create_card_scenario_php_request}});
$card = $identity->createPaymentCard($card);
