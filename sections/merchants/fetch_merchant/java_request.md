import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Merchant;

Maybe<Merchant> response = api.merchants
    .id(merchant.id)
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Merchant");
}

Merchant merchantView = response.view();
