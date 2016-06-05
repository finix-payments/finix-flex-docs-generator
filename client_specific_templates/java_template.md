

import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .businessName("business inc")
        .businessType(BusinessType.LIMITED_LIABILITY_COMPANY)
        .doingBusinessAs("doingBusinessAs")
        .phone("1234567890")
        .businessPhone("+1 (408) 756-4497")
        .taxId("123456789")
        .businessTaxId("123456789")
        .personalAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .businessAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .dob(DateOfBirth.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .build()
    )
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name("Joe-Doe")
      .identity("IDaAUrraYjDT4i2w1C2VGBpY")
      .accountNumber("84012312415")
      .bankCode("840123124")
      .accountType(BankAccountType.SAVINGS)
      .companyName("company name")
      .country("USA")
      .currency("USD")
      .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());


import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .build()
    )
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe-Doe")
    .identity("ID572pSyFj71oVExp6XWiGRP")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build();
paymentCard = client.paymentCardsClient().save(paymentCard);


import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);


import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)


import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().save(
  Authorization.builder()
    .amount(100L)
    .merchantIdentity("IDrktKp2HNpogF3BWMmiSGrz")
    .processor("DUMMY_V1")
    .source("PIeffbMtvz2Hiy6dwBbaHhKq")
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("{{fetch_authorization_scenario_id}}");
authorization = authorization.capture(50L);


import io.{{api_name_downcase}}.payments.processing.client.model.Authorization;

Authorization authorization = client.authorizationsClient().fetch("{{fetch_authorization_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Dispute;

Dispute dispute = transfer.disputeClient().fetch("{{fetch_dispute_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .build()
    )
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().save(
  Identity.builder()
    .entity(
      Entity.builder()
        .firstName("dwayne")
        .lastName("Sunkhronos")
        .email("user@example.org")
        .businessName("business inc")
        .businessType(BusinessType.LIMITED_LIABILITY_COMPANY)
        .doingBusinessAs("doingBusinessAs")
        .phone("1234567890")
        .businessPhone("+1 (408) 756-4497")
        .taxId("123456789")
        .businessTaxId("123456789")
        .personalAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .businessAddress(
          Address.builder()
            .line1("741 Douglass St")
            .line2("Apartment 7")
            .city("San Mateo")
            .region("CA")
            .postalCode("94114")
            .country("USA")
            .build()
        )
        .dob(DateOfBirth.builder()
          .day(27)
          .month(5)
          .year(1978)
          .build()
        )
        .settlementCurrency("USD")
        .settlementBankAccount(BankAccountType.CORPORATE)
        .maxTransactionAmount(1)
        .mcc(7399)
        .url("http://sample-entity.com")
        .annualCardVolume(100)
        .build()
    )
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Identity;

Identity identity = client.identitiesClient().fetch("{{fetch_identity_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Merchant;

Merchant merchant = identity.provisionMerchantOn(Merchant.builder().processor("DUMMY_V1").build());


import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = identity.verifyOn(
  Verification.builder()
    .processor("DUMMY_V1")
    .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Verification;

Verification verification = client.verificationsClient().fetch("{{fetch_identity_verification_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = identity.createSettlement(
  Settlement.builder()
    .processor("DUMMY_V1")
    .currency("USD")
    .build()
)


import io.{{api_name_downcase}}.payments.processing.client.model.Settlement;

Settlement settlement = client.settlementsClient().fetch("{{fetch_settlement_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Map<String, String> tags = new HashMap<>();
tags.put("name", "sample-tag");

Transfer transfer = client.transfersClient().save(
    Transfer.builder()
      .merchantIdentity("IDaAUrraYjDT4i2w1C2VGBpY")
      .source("PIi98CoYWpQZi8w7ZimJxuJ")
      .amount(888888)
      .currency("USD")
      .tags(tags)
      .processor("DUMMY_V1")
      .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.Refund;

Refund refund = transfer.reverse(100L);


import io.{{api_name_downcase}}.payments.processing.client.model.Transfer;

Transfer transfer = client.transfersClient().fetch("{{fetch_transfer_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().save(
    Webhook.builder()
      .url("https://tools.ietf.org/html/rfc2606#section-3")
      .build()
);



import io.{{api_name_downcase}}.payments.processing.client.model.Webhook;

Webhook webhook = client.webhookClient().fetch("{{fetch_webhook_scenario_id}}");


import io.{{api_name_downcase}}.payments.processing.client.model.PaymentCard;

PaymentCard paymentCard = PaymentCard.builder()
    .name("Joe-Doe")
    .identity("ID572pSyFj71oVExp6XWiGRP")
    .expirationMonth(12)
    .expirationYear(2030)
    .number("4111 1111 1111 1111")
    .securityCode("231")
    .build(); 
paymentCard = client.paymentCardsClient().save(paymentCard);


import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

bankAccount = client.bankAccountsClient().save(
    BankAccount.builder()
      .name("Joe-Doe")
      .identity("IDaAUrraYjDT4i2w1C2VGBpY")
      .accountNumber("84012312415")
      .bankCode("840123124")
      .accountType(BankAccountType.SAVINGS)
      .companyName("company name")
      .country("USA")
      .currency("USD")
      .build()
);


import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

BankAccount bankAccount = client.bankAccountsClient().fetch("{{fetch_dispute_scenario_id}}")


import io.{{api_name_downcase}}.payments.processing.client.model.BankAccount;

client.bankAccountsClient().<Resources<BankAccount>>resourcesIterator()
  .forEachRemaining(baPage -> {
    Collection<BankAccount> bankAccounts = baPage.getContent();
    //do something
  });

