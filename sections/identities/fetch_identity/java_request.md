import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

Maybe<Identity> response = api.identities.id("{{create_recipient_identity_payouts_scenario_id}}").get();
if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to fetch Identity");
}
Identity identity = response.view();