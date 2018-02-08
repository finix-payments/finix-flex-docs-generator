use {{php_client_resource_name}}\Resources\PaymentCard;
use {{php_client_resource_name}}\Resources\Identity;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$card = new PaymentCard({{create_card_scenario_php_request}});
$card = $identity->createPaymentCard($card);
