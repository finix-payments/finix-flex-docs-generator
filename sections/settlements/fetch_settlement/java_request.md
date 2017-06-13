import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Settlement;

Maybe<Settlement> response = api.settlements
  .id("{{fetch_settlement_scenario_id}}")
  .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch settlement");
}

Settlement settlementView = response.view();
