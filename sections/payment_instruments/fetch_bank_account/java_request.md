
import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = client.paymentCardsClient().fetch("{{fetch_bank_account_scenario_id}}")
