from finix.resources import PaymentCard

payment_card = PaymentCard(
    name="Joe-Doe",
    expiration_month=12,
    expiration_year=2030,
    number="4111 1111 1111 1111",
    security_code=231
).save()