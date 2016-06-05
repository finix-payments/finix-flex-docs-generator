
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
	        "doing_business_as"=> "Prestige World Wide", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Prestige World Wide", 
	        "url"=> "www.PrestigeWorldWide.com", 
	        "business_name"=> "Prestige World Wide", 
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
	    "identity"=> "IDviGtLw6GkqoPDtAkJ6KmNd"
	));
$bank_account = $bank_account->save();


use Payline\Resources\Identity;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');

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
	    "identity"=> "IDbq6maJgrm2xriCyRU4TFbh"
	));
$card = $card->save();


use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDviGtLw6GkqoPDtAkJ6KmNd", 
	    "source"=> "PIcW3ufSNpKKg3N81Kuz14ae", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDviGtLw6GkqoPDtAkJ6KmNd", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PIcW3ufSNpKKg3N81Kuz14ae"
	));
$authorization = $authorization->save();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU3SshCjfVV2hR1QABcUJACy');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU3SshCjfVV2hR1QABcUJACy');

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DIgZqdyHDiMWZo8DPckyKTkw');

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
	        "doing_business_as"=> "Prestige World Wide", 
	        "annual_card_volume"=> 12000000, 
	        "default_statement_descriptor"=> "Prestige World Wide", 
	        "url"=> "www.PrestigeWorldWide.com", 
	        "business_name"=> "Prestige World Wide", 
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

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');

$merchant = $identity->provisionMerchantOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');
$identity_verification = $identity->verifyOn(
	array(
	    "processor"=> "DUMMY_V1"
	));
use Payline\Resources\Verification;

$verification = Verification::retrieve('VI2AhmYSt8FG5b5bDEroNzyb');

use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDviGtLw6GkqoPDtAkJ6KmNd');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STuek2CGQjGr4yM7vfoyYjm9');

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "fee"=> 10, 
	    "currency"=> "USD", 
	    "merchant_identity"=> "IDviGtLw6GkqoPDtAkJ6KmNd", 
	    "source"=> "PIcW3ufSNpKKg3N81Kuz14ae", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1"
	));
$debit = $debit->save();
use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRayKyreDFn7epnPcGFPQvKr');
$refund = $debit->reverse(50);
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRayKyreDFn7epnPcGFPQvKr');



use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHa7hLWdQ44kDjbiwVtXpBWt');



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
	    "identity"=> "IDbq6maJgrm2xriCyRU4TFbh"
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
	    "identity"=> "IDviGtLw6GkqoPDtAkJ6KmNd"
	));
$bank_account = $bank_account->save();


use Payline\Resources\PaymentInstrument;

$card = PaymentInstrument::retrieve('DIgZqdyHDiMWZo8DPckyKTkw');


