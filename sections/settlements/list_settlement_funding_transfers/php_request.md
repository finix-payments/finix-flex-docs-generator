use {{api_name}}\Resources\Settlement;

$settlement = Settlement::retrieve('{{fetch_settlement_scenario_id}}');
$settlements = Settlement::getPagination($settlement->getHref("funding_transfers"));
