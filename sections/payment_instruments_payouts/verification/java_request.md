import io.{{api_name_downcase}}.payments.processing.client.model.VerificationForm;

VerificationForm form = VerificationForm.builder().processor("VISA_V1").build();
    Maybe<Verification> request = app.instruments.id("{{fetch_credit_card_scenario_id}}").verifications.post(form);
