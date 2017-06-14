import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Transfer;

Maybe<Transfer> response = api.transfers
    .id("{{fetch_transfer_scenario_id}}")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Transfer");
}

Transfer transferView = response.view();
