```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();


use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_merchant_identity_scenario_php_request}}
);
$identity = $identity->save();

use {{api_name}}\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument({{create_bank_account_scenario_php_request}});
$bank_account = $bank_account->save();


use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{underwrite_identity_scenario_php_request}});
use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{underwrite_identity_scenario_php_request}});
use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_buyer_identity_scenario_php_request}}
);
$identity = $identity->save();

use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{create_card_scenario_php_request}});
$card = $card->save();


use {{api_name}}\Resources\Transfer;

$debit = new Transfer({{create_debit_scenario_php_request}});
$debit = $debit->save();

use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = $identity->createSettlement({{create_settlement_scenario_php_request}});

use {{api_name}}\Resources\Authorization;

$authorization = new Authorization({{create_authorization_scenario_php_request}});
$authorization = $authorization->save();

use {{api_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
use {{api_name}}\Resources\Authorization;

$authorization = Authorization::retrieve('{{fetch_authorization_scenario_id}}');

use {{api_name}}\Resources\Dispute;

$dispute = Dispute::retrieve('{{fetch_dispute_scenario_id}}');

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_buyer_identity_scenario_php_request}}
);
$identity = $identity->save();

use {{api_name}}\Resources\Identity;

$identity = new Identity({{create_merchant_identity_scenario_php_request}}
);
$identity = $identity->save();

use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');

$merchant = $identity->provisionMerchantOn({{underwrite_identity_scenario_php_request}});
use {{api_name}}\Resources\Identity;

$identity = Identity::retrieve('{{create_identity_scenario_id}}');
$identity_verification = $identity->verifyOn({{underwrite_identity_scenario_php_request}});
use {{api_name}}\Resources\Verification;

$verification = Verification::retrieve('{{fetch_identity_verification_scenario_id}}');

use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = $identity->createSettlement({{create_settlement_scenario_php_request}});

use {{api_name}}\Resources\Settlement;

$settlement = Settlement::retrieve('{{fetch_settlement_scenario_id}}');

use {{api_name}}\Resources\Transfer;

$debit = new Transfer({{create_debit_scenario_php_request}});
$debit = $debit->save();
use {{api_name}}\Resources\Transfer;

$debit = Transfer::retrieve('{{create_debit_scenario_id}}');
$refund = $debit->reverse(50);
use {{api_name}}\Resources\Transfer;

$transfer = Transfer::retrieve('{{fetch_transfer_scenario_id}}');



use {{api_name}}\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



use {{api_name}}\Resources\Webhook;

$webhook = Webhook::retrieve('{{fetch_webhook_scenario_id}}');



use {{api_name}}\Resources\PaymentInstrument;

$card = new PaymentInstrument({{create_card_scenario_php_request}});
$card = $card->save();


use {{api_name}}\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument({{create_bank_account_scenario_php_request}});
$bank_account = $bank_account->save();


use {{api_name}}\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('{{fetch_dispute_scenario_id}}');


