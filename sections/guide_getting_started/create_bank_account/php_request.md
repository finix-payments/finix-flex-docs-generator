use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\BankAccount;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$bank_account = new BankAccount({{create_bank_account_scenario_php_request}});
$bank_account = $identity->createBankAccount($bank_account);