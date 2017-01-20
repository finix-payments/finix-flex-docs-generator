Merchant merchant = client.merchantsClient().fetch("{{fetch_merchant_scenario_id}}");
Verification verification = merchant.verifyOn(
  Verification.builder().build()
);