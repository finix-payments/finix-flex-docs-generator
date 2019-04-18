import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.forms.Address;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;

PaymentCardForm form = PaymentCardForm.builder()
        .name("Joe Doe")
        .number("4957030420210454")
        .securityCode("112")
        .expirationYear(2020)
        .identity("{{fetch_identity_scenario_id}}")
        .expirationMonth(12)
        .address(
                Address.builder()
                        .city("San Mateo")
                        .country("USA")
                        .region("CA")
                        .line1("123 Fake St")
                        .line2("#7")
                        .postalCode("90210")
                        .build()
        )
        .tags(ImmutableMap.of("card_name", "Business Card"))
        .build();

Maybe<PaymentCard> response = api.instruments.post(form);
if (! response.succeeded()) {
    ApiError error = response .error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Payment Card");
}
PaymentCard card = response.view();
