import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.lib.Page;
import io.{{api_name_downcase}}.payments.views.Instrument;

Maybe<Page<Instrument>> response = api.instruments.get();

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    System.out.println(error.getMessage());
    System.out.println(error.getDetails());
    throw new RuntimeException("API error attempting to list all Payment Instruments");
}

Page<Instrument> page = response.view();
