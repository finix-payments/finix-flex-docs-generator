import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.forms.AuthorizationUpdateForm;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.*;

AuthorizationUpdateForm formVoid = AuthorizationUpdateForm.builder()
        .voidMe(true)
        .build();

Maybe<Authorization> response = api.authorizations.id("{{fetch_authorization_scenario_id}}").put(formVoid);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to void authorization");
}
Authorization voidAuthorization = response.view();
