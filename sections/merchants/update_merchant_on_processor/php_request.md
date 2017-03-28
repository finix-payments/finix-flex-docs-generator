use {{php_client_resource_name}}\Resources\Merchant;
use {{php_client_resource_name}}\Resources\Verification;

$merchant = Merchant::retrieve('{{fetch_merchant_scenario_id}}');
$verification = new Verification();
$verification = $merchant->verifyOn($verification);