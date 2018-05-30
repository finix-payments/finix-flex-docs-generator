// Download the PHP Client here: {{php_client_repo}}

require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{php_client_resource_name}}/Settings.php');

{{api_name}}\Settings::configure([
	"root_url" => '{{staging_base_url}}',
	"username" => '{{basic_auth_username_payouts}}',
	"password" => '{{basic_auth_password_payouts}}']
	);

require(__DIR__ . '/src/{{php_client_resource_name}}/Bootstrap.php');
{{php_client_resource_name}}\Bootstrap::init();
