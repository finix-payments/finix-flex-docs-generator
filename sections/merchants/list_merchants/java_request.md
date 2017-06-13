import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.lib.Page;
import io.{{api_name_downcase}}.payments.views.Merchant;

Maybe<Page<Merchant>> request = api.merchants.get();

if (! request.succeeded()) {
  ApiError error = request.error();
  System.out.println(error.getCode());
  System.out.println(error.getMessage());
  System.out.println(error.getDetails());
  throw new RuntimeException("API error attempting to list all Merchants");
}

Page<Merchant> page = request.view();
