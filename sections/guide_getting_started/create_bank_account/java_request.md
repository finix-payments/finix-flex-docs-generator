import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.enums.BankAccountType;
import io.{{api_name_downcase}}.payments.forms.BankAccountForm;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.BankAccount;
import io.{{api_name_downcase}}.payments.views.Identity;
import java.util.Currency;

BankAccountForm form = BankAccountForm.builder()
        .name("Joe Doe")
        .identity("{{fetch_identity_scenario_id}}")
        .accountNumber("84012312415")
        .bankCode("840123124")
        .accountType(BankAccountType.SAVINGS)
        .companyName("company name")
        .country("USA")
        .currency(Currency.getInstance("USD"))
        .build();

Maybe<BankAccount> request = api.instruments.post(form);

if (! request.succeeded()) {
    ApiError error = request.error();
    System.out.println(error);
    throw new RuntimeException("API error attempting to create bank account");
}
BankAccount bankAccount = request.view();
