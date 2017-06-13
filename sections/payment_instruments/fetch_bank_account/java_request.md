import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.views.Instrument;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;

Maybe<Instrument> response = api.paymentInstruments
    .id("{{fetch_bank_account_scenario_id}}")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Bank Account");
}

Instrument bankAccountView = response.view();
