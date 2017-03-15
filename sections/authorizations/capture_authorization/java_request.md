
import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("{{fetch_authorization_scenario_id}}");
Long captureAmount = 50L;
Long feeAmount = 10L
authorization = authorization.capture(captureAmount, feeAmount);
