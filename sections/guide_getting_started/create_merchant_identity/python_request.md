from finix.resources import Identity

identity = Identity(entity={
    "first_name": "xdwayne",
    "last_name": SYNC_UNDERWRITING_LAST_NAME,
    "email": "xuser@example.org",
}).save()