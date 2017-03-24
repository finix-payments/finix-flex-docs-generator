use {{php_client_resource_name}}\Resources\Settlement;

$settlement = Settlement::retrieve('{{fetch_settlement_scenario_id}}');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));
