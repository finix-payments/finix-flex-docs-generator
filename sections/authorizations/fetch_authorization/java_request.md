import io.{{api_name_downcase}}.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Authorization;

Maybe <Authorization> response =  api.authorizations
    .id("{{fetch_authorization_scenario_id}}")
    .get();

if(! response.succeeded()){
    System.out.println(response.error());
    throw new RuntimeException("API error in attempting to fetch Authorization");
}

Authorization authorization = response.view();
