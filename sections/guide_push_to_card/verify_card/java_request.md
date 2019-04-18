import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;


 VerificationForm verificationForm = VerificationForm.builder()
    .processor("VISA_V1")
    .build();

Maybe<Verification> verificationResponse = api.instruments.id("{{create_card_verification_scenario_id}}").verifications.post(verificationForm);
if (! verificationResponse.succeeded()) {
    ApiError error = verificationResponse.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create a Verification");
}
Verification verification = verificationResponse.view();
