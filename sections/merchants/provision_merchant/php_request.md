use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Merchant;

$identity = Identity::retrieve('{{create_merchant_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{provision_merchant_scenario_php_request}});






