use {{php_client_resource_name}}\Resources\Identity;
use {{php_client_resource_name}}\Resources\Merchant;

$identity = Identity::retrieve('{{create_sender_identity_payouts_scenario_id}}');

$merchant = $identity->provisionMerchantOn(new Merchant());
