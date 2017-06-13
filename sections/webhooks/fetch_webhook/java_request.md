import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Webhook;

Maybe<Webhook> response = api.webhooks
        .id({{fetch_webhook_scenario_id}})
        .get();

if(! response.succeeded()){
    System.out.println(response.error());
    System.out.println(response.error().getDetails());
    throw new RuntimeException("API error attempting to fetch Webhook");
}
Webhook webhookView = response.view();
