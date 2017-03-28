use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Merchant;

$identity = Identity::retrieve('{{create_recipient_identity_payouts_scenario_id}}');

$merchant = $identity->provisionMerchantOn(new Merchant());
