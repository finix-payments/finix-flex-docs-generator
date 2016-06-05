
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "phone"=> "1234567890", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "mcc"=> "0742", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 120000, 
	        "principal_percentage_ownership"=> 100, 
	        "doing_business_as"=> "Dunder Mifflin", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Dunder Mifflin", 
	        "url"=> "www.DunderMifflin.com", 
	        "business_name"=> "Dunder Mifflin", 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_tax_id"=> "123456789", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "bank_code"=> "123123123", 
	    "country"=> "USA", 
	    "currency"=> "USD", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDxhFxphTTEPPevsfWcScpC3"
	));
$bank_account = $bank_account->save();


use Payline\Resources\Identity;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "first_name"=> "Dwayne", 
	        "last_name"=> "Johnson"
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "expiration_year"=> 2020, 
	    "number"=> "4242424242424242", 
	    "expiration_month"=> 12, 
	    "address"=> array(
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    ), 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDjuRFj8TBroYGA6uRZT4aCU"
	));
$card = $card->save();


use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDxhFxphTTEPPevsfWcScpC3", 
	    "source"=> "PIm8J4roNG5TE2FtswJFGY9g", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDxhFxphTTEPPevsfWcScpC3", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PIm8J4roNG5TE2FtswJFGY9g"
	));
$authorization = $authorization->save();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsdEUSP86DiChQzFKVEXWMP');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AUsdEUSP86DiChQzFKVEXWMP');

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DI9b1dqFV3RmwaAa1k6cxAWz');

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "first_name"=> "Dwayne", 
	        "last_name"=> "Johnson"
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "first_name"=> "dwayne", 
	        "last_name"=> "Sunkhronos", 
	        "phone"=> "1234567890", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "mcc"=> "0742", 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "max_transaction_amount"=> 120000, 
	        "principal_percentage_ownership"=> 100, 
	        "doing_business_as"=> "Dunder Mifflin", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Dunder Mifflin", 
	        "url"=> "www.DunderMifflin.com", 
	        "business_name"=> "Dunder Mifflin", 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_tax_id"=> "123456789", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "email"=> "user@example.org", 
	        "tax_id"=> "5779"
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Verification;

$verification = Verification::retrieve('VIpiZvsLaX39YfgD9JD1TEkr');

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDxhFxphTTEPPevsfWcScpC3');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STaL11bfgDpzJmRMA3uLb6nk');

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDxhFxphTTEPPevsfWcScpC3", 
	    "source"=> "PIm8J4roNG5TE2FtswJFGY9g", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRtXHpcZ8w3YY9MdpySH39PA');
$refund = $debit->reverse(50);
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRtXHpcZ8w3YY9MdpySH39PA');



use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WH8T8Uz3qht5YyMJjsMxWYL8');



use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "expiration_year"=> 2020, 
	    "number"=> "4242424242424242", 
	    "expiration_month"=> 12, 
	    "address"=> array(
	        "city"=> "San Mateo", 
	        "country"=> "USA", 
	        "region"=> "CA", 
	        "line2"=> "Apartment 7", 
	        "line1"=> "741 Douglass St", 
	        "postal_code"=> "94114"
	    ), 
	    "security_code"=> "112", 
	    "type"=> "PAYMENT_CARD", 
	    "identity"=> "IDjuRFj8TBroYGA6uRZT4aCU"
	));
$card = $card->save();


use Payline\Resources\PaymentInstrument;

$bank_account = new PaymentInstrument(
	array(
	    "account_type"=> "SAVINGS", 
	    "name"=> "Fran Lemke", 
	    "bank_code"=> "123123123", 
	    "country"=> "USA", 
	    "currency"=> "USD", 
	    "account_number"=> "123123123", 
	    "type"=> "BANK_ACCOUNT", 
	    "identity"=> "IDxhFxphTTEPPevsfWcScpC3"
	));
$bank_account = $bank_account->save();


use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('DI9b1dqFV3RmwaAa1k6cxAWz');


