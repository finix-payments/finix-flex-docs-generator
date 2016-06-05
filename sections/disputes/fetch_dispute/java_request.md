
import io.{{api_name_downcase}}.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("{{fetch_dispute_scenario_id}}");
