import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;

AuthorizationCreateForm formCreateAuthorization = AuthorizationCreateForm.builder()
                .idempotencyId("{{create_authorization_idempotency_scenario_idempotency_id}}")
                .amount(10000L)
                .merchantIdentity("{{create_merchant_identity_scenario_id}}")
                .source("{{create_card_scenario_id}}")
                .build();

Maybe<Authorization> response = api.authorizations.post(formCreateAuthorization);

if (! response.succeeded()) {
  ApiError error = response.error();
  System.out.println(error.getMessage());
  throw new RuntimeException("API error attempting to creating Authorization");
}

Authorization authorization = response.view();
