
import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;
import io.{{api_name_downcase}}.payments.processing.client.model.Name;

BankAccount bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name(Name.parse("Joe Doe"))
      .identity(identity.getId())  //  or use "{{fetch_identity_scenario_id}}"
      .accountNumber("84012312415")
      .bankCode("840123124")
      .accountType(BankAccountType.SAVINGS)
      .companyName("company name")
      .country("USA")
      .currency("USD")
      .build()
);

