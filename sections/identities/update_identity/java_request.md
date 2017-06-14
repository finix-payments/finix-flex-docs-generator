import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.enums.BusinessType;
import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Identity;

IdentityForm form = IdentityForm.builder()
                .entity(
                  IdentityEntityForm.builder()
                      .firstName("dwayne")
                      .email("self@newdomain.com")
                      .businessPhone("+1 (408) 756-4497")
                      .build())
                .build();

Maybe<Identity> response = api.identities.id("{{fetch_identity_scenario_id}}").put(form);

if (! response.succeeded()) {
    System.out.println(response.error());
    throw new RuntimeException("API error attempting to update identity");
}

Identity updatedIdentity = response.view();
