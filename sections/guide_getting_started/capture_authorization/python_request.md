from finix.resources import Authorization

authorization = Authorization(
    amount=100,
    processor="DUMMY_V1",
    source="PIeffbMtvz2Hiy6dwBbaHhKq",
    merchant_identity="IDrktKp2HNpogF3BWMmiSGrz"
).save()