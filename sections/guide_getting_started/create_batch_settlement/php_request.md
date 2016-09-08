use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = $identity->createSettlement({{create_settlement_scenario_php_request}});
