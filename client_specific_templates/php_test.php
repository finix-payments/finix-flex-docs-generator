
use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 120000,
	        "default_statement_descriptor"=> "Pawny City Hall", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "5779", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
	        "annual_card_volume"=> 12000000
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
	    "identity"=> "IDmAU6skpdxVpkVxDazo6vt6"
	));
$bank_account = $bank_account->save();



use Payline\Resources\Identity;

$identity = Identity::retrieve('IDmAU6skpdxVpkVxDazo6vt6');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);


use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Henderson", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        )
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Fran Sterling", 
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
	    "identity"=> "IDtvFQuCqcSbFAxuXdCnBxHo"
	));
$card = $card->save();


use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "merchant_identity"=> "IDmAU6skpdxVpkVxDazo6vt6", 
	    "currency"=> "USD", 
	    "amount"=> 192863, 
	    "fee"=> 19286, 
	    "source"=> "PIacGx85omA5mQZHUw4A8Etz"
	));
$debit = $debit->save();
use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDmAU6skpdxVpkVxDazo6vt6');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Authorization;

$authorization = new Authorization(
	array(
	    "merchant_identity"=> "IDmAU6skpdxVpkVxDazo6vt6", 
	    "currency"=> "USD", 
	    "amount"=> 100, 
	    "processor"=> "DUMMY_V1", 
	    "source"=> "PIacGx85omA5mQZHUw4A8Etz"
	));
$authorization = $authorization->save();

use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU9WhCbNyF1twgGSSGjduXh2');
$authorization->capture_amount = 50;
$authorization = $authorization->capture();
use Payline\Resources\Authorization;

$authorization = Authorization::retrieve('AU9WhCbNyF1twgGSSGjduXh2');

use Payline\Resources\Dispute;

$dispute = Dispute::retrieve('DIqTYMUMHvcjkrYPmU9DggRv');

use Payline\Resources\Identity;

$identity = new Identity(
	array(
	    "tags"=> array(
	        "key"=> "value"
	    ), 
	    "entity"=> array(
	        "phone"=> "7145677613", 
	        "first_name"=> "Jim", 
	        "last_name"=> "Henderson", 
	        "email"=> "therock@gmail.com", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        )
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
	        "last_name"=> "Sunkhronos", 
	        "max_transaction_amount"=> 120000,
	        "default_statement_descriptor"=> "Pawny City Hall", 
	        "personal_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 7", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "incorporation_date"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "business_address"=> array(
	            "city"=> "San Mateo", 
	            "country"=> "USA", 
	            "region"=> "CA", 
	            "line2"=> "Apartment 8", 
	            "line1"=> "741 Douglass St", 
	            "postal_code"=> "94114"
	        ), 
	        "first_name"=> "dwayne", 
	        "title"=> "CEO", 
	        "business_tax_id"=> "123456789", 
	        "doing_business_as"=> "Pawny City Hall", 
	        "principal_percentage_ownership"=> 50, 
	        "email"=> "user@example.org", 
	        "mcc"=> "0742", 
	        "phone"=> "1234567890", 
	        "business_name"=> "Pawny City Hall", 
	        "tax_id"=> "5779", 
	        "business_type"=> "INDIVIDUAL_SOLE_PROPRIETORSHIP", 
	        "business_phone"=> "+1 (408) 756-4497", 
	        "dob"=> array(
	            "year"=> 1978, 
	            "day"=> 27, 
	            "month"=> 6
	        ), 
	        "url"=> "www.PawnyCityHall.com", 
	        "annual_card_volume"=> 12000000
	    )
	)
);
$identity = $identity->save();

use Payline\Resources\Identity;

$identity = Identity::retrieve('IDmAU6skpdxVpkVxDazo6vt6');
use Payline\Resources\Identity;

$identity = Identity::retrieve('IDmAU6skpdxVpkVxDazo6vt6');

$merchant = $identity->provisionMerchantOn(
	  array(
	    "tags"=> array(
	      "key_2"=> "value_2"
	    )
	  )
	);
use Payline\Resources\Identity;
use Payline\Resources\Settlement;

$identity = Identity::retrieve('IDmAU6skpdxVpkVxDazo6vt6');
$settlement = $identity->createSettlement(
	array(
	    "currency"=> "USD", 
	    "processor"=> "DUMMY_V1"
	));

use Payline\Resources\Settlement;

$settlement = Settlement::retrieve('STv7ccEXEPybpzKgET44Dt96');

use Payline\Resources\Transfer;

$debit = new Transfer(
	array(
	    "merchant_identity"=> "IDmAU6skpdxVpkVxDazo6vt6", 
	    "currency"=> "USD", 
	    "amount"=> 192863, 
	    "fee"=> 19286, 
	    "source"=> "PIacGx85omA5mQZHUw4A8Etz"
	));
$debit = $debit->save();
use Payline\Resources\Transfer;

$debit = Transfer::retrieve('TRtT8ELXTQCuSv87RcQJ13Uo');
$refund = $debit->reverse(50);
use Payline\Resources\Transfer;

$transfer = Transfer::retrieve('TRtT8ELXTQCuSv87RcQJ13Uo');



use Payline\Resources\Webhook;

$webhook = new Webhook('create_webhook_scenario_php_request');
$webhook = $webhook->save();



use Payline\Resources\Webhook;

$webhook = Webhook::retrieve('WHhdj5DrgwNwidLTTD3poXai');



use Payline\Resources\PaymentInstrument;

$card = new PaymentInstrument(
	array(
	    "name"=> "Fran Sterling", 
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
	    "identity"=> "IDtvFQuCqcSbFAxuXdCnBxHo"
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
	    "identity"=> "IDmAU6skpdxVpkVxDazo6vt6"
	));
$bank_account = $bank_account->save();


