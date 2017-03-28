use {{php_client_resource_name}}\Resources\Merchant;
use {{php_client_resource_name}}\Resources\Verification;

$merchant = Merchant::retrieve('{{fetch_merchant_scenario_id}}');
$verifications = Verification::getPagination($merchant->getHref("verifications"));

