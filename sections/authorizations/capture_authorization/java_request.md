import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;

AuthorizationUpdateForm form = AuthorizationUpdateForm.builder()
        .captureAmount(100L)
        .fee(10L)
        .statementDescriptor("Order 123")
        .build();

Maybe<Authorization> responseAuthorization = api.authorizations.id("{{create_authorization_scenario_id}}").put(form);

if (! responseAuthorization.succeeded()) {
    ApiError error = responseAuthorization.error();
    System.out.println(error.getMessage());
    throw new RuntimeException("API error attempting to capture authorization");
}
Authorization capturedAuth = responseAuthorization.view();
