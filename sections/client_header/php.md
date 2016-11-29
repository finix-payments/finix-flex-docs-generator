```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');

{{api_name}}\Settings::configure([
	"root_url" => '{{staging_base_url}}',
	"username" => '{{basic_auth_username}}',
	"password" => '{{basic_auth_password}}']
	);


require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();
