import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.forms.WebhookForm;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Webhook;

WebhookForm form = WebhookForm.builder()
    .url("http://requestb.in/1jb5zu11")
    .build();

Maybe<Webhook> request = api.webhooks.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create Webhook");
}
Webhook webhookView = request.view();
