```php
<?php
require_once('vendor/autoload.php');
require(__DIR__ . '/src/{{api_name}}/Settings.php');
{{api_name}}\Settings::configure('{{base_url}}', '{{basic_auth_username}}', '{{basic_auth_password}}');
require(__DIR__ . '/src/{{api_name}}/Bootstrap.php');
{{api_name}}\Bootstrap::init();
