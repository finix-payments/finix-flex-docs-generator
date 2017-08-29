## Tags

All {{api_name}} objects (i.e. `Authorization`, `Application`, `Identity`, `Merchant`, `Payment Instrument`, `Settlement`, `Transfer`) include a tags attribute that allows the user to include key-value metadata to their object. For example, when creating a `Payment Instrument`, you may want to include more data about the card. Simply pass a custom key and value, such as "card-type": "business card". Or when creating an `Authorization`, you may want to include specific information about the transaction, such as a unique ID or additional information about the transaction.
