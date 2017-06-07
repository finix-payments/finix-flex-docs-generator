import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.forms.SettlementForm;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.;
import java.util.Currency;


Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .currency("USD")
    .build()
);

SettlementForm formSettlement = SettlementForm.builder()
        .currency(Currency.getInstance("USD"))
        .build();

Transfer transfer = api.transfers.id("{{capture_authorization_scenario_id}}").get().view();

Maybe<Settlement> request = api.identities.id("{{create_merchant_identity_scenario_id}}").settlements.post(formSettlement);

if (! request.succeeded()) {
    throw new RuntimeException("API error attempting to create batch settlement");
}

Settlement settlementBatch = request.view();
