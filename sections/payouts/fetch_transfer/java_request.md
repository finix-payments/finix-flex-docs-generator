import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;

Maybe<Transfer> response = api.transfers.id("{{fetch_transfer_scenario_id}}").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Transfer");
}
Transfer card = response.view();