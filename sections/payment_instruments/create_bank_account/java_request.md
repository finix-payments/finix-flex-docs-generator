
import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

BankAccount bankAccount = client.bankAccountsClient().save(
  BankAccount.builder()
    .name(Name.parse("Billy Bob Thorton III"))
    .identity("IDaAUrraYjDT4i2w1C2VGBpY")
    .accountNumber("84012312415")
    .bankCode("840123124")
    .accountType(BankAccountType.SAVINGS)
    .companyName("company name")
    .country("USA")
    .currency("USD")
    .build()
);
