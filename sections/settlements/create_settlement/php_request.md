use {{php_client_resource_name}}\Resources\Identity;
use {{php_client_resource_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = new Settlement({{create_settlement_scenario_php_request}});
$settlement = $identity->createSettlement($settlement);
