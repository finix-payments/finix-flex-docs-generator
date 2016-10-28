from finix.resources import Settlement

settlement = Settlement(
    processor="DUMMY_V1",
    currency="USD"
).save()