import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.*;
import io.finix.payments.forms.*;

MerchantUnderwritingForm form = MerchantUnderwritingForm.builder()
    .processor(null)
    .tags(ImmutableMap.of("key", "value"))
    .build();

Maybe<Merchant> underwriteMerchant = api.identities.id("{{fetch_identity_scenario_id}}").merchants.post(form);

if(! underwriteMerchant.succeeded()){
   System.out.println(underwriteMerchant.error());
}

Merchant provisionMerchant = underwriteMerchant.view();
