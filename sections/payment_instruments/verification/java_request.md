import io.{{api_name_downcase}}.payments.processing.client.model.VerificationForm;

VerificationForm form = VerificationForm.builder().processor("VISA_V1").build();
    Maybe<Verification> request = app.instruments.id("PIdqX9PzXRB3BAzRs3CpoAF4").verifications.post(form);
