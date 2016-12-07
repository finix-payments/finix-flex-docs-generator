use {{api_name}}\Resources\Merchant;
use {{api_name}}\Resources\Verification;

$merchant = Merchant::retrieve('{{fetch_merchant_scenario_id}}');
$verifications = Verification::getPagination($merchant->getHref("verifications"));

