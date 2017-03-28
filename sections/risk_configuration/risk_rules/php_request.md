use {{api_name}}\Resources\Identity;
use {{api_name}}\Resources\Settlement;

$identity = Identity::retrieve('{{fetch_identity_scenario_id}}');
$settlement = new Settlement({{create_settlement_scenario_php_request}});
$settlement = $identity->createSettlement($settlement);
