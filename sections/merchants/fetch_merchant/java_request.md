import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.views.Merchant;

Merchant merchant = api.merchants
    .id("{{fetch_merchant_scenario_id}}")
    .get()
    .view();
