from finix.resources import BankAccount

bank_account = BankAccount(
   name=sample_name(),
   account_number="84012312415",
   bank_code="840123124",
   account_type="SAVINGS",
   company_name="sample company",
   country="USA",
   currency="USD"
).save()