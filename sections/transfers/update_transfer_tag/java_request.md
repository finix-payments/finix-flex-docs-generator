import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import com.google.common.collect.ImmutableMap;
import java.util.Currency;

TransferForm form = TransferForm.builder()
        .tags(ImmutableMap.of("order_number", "12121212"))
        .build();

Maybe<Transfer> response = api.transfers.post(form);

Maybe<Transfer> response = api.transfers.id("{{fetch_transfer_scenario_id}}").put(form);

if (! response.succeeded()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to update transfer");
}
Transfer transfer = response.view();
