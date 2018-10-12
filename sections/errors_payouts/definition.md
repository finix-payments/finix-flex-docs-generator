## Errors

HTTP Code | Meaning
---------- | -------
400 | Bad Request -- You've attemped an invalid request
401 | Unauthorized -- You have used the incorrect API key
402 | Upstream Processor Error -- Errors caused by 3rd party service
404 | Not Found -- The specified resource could not be found
422 | Unprocessable Entity -- The parameters were valid but the request failed. The error is usually some misunderstanding of various steps that have to be executed in order (e.g. attempting to initiate a transfer on behalf of a merchant that has not yet been approved)
500 | Internal Server Error -- We had a problem with our server. Try again later.

Below are the different error values that the `messages` attribute will return for Push to Card.

Error Code | Messages
---------- | -------
REFER_TO_CARD_ISSUER | Please contact card issuer for more information.
INVALID_MERCHANT | Merchant not permitted for this transaction type
PICK_UP_CARD_NO_FRAUD | Please contact card issuer for more information.
DO_NOT_HONOR | Please contact card issuer for more information.
ERROR |Please attempt transaction again but if it still cannot be processed try again at a later time
PICK_UP_CARD_FRAUD_ACCOUNT | Please contact card issuer for more information.
INVALID_TRANSACTION | Issuing bank does not support this transaction type on this card. Please contact card issuer for more information.
INVALID_AMOUNT_OR_CURRENCY | Transaction violates network amount limit.
INVALID_ACCOUNT_NUMBER | The account number does not exist. Please make sure the account number is correct or contact your issuer.
NO_SUCH_ISSUER | The issuer can not be found. Please check card number to ensure it is valid.
RE_ENTER_TRANSACTION | Please attempt transaction again and contact card issuer if it still cannot be processed.
NO_ACTION_TAKEN | Please contact card issuer for more information.
UNABLE_TO_LOCATE_RECORD | The account number does not exist. Please make sure the account number is correct or contact your issuer.
FILE_TEMPORARILY_NOT_AVAILABLE | Please contact card issuer for more information.
NO_CREDIT_ACCOUNT | Issuer has declined the transaction because the card is not a credit account. Please try another card.
LOST_CARD_PICK_UP_FRAUD_ACCOUNT | Please contact card issuer for more information.
STOLEN_CARD_PICK_UP_FRAUD_ACCOUNT | Please contact card issuer for more information.
NOT_SUFFICIENT_FUNDS | Card issuer has declined the transaction as it does not have sufficient funds.
NO_CHECKING_ACCOUNT | The card is not tied to a checking account and thus cannot be processed. Please try another card.
NO_SAVINGS_ACCOUNT | The card is not tied to a savings account and thus cannot be processed. Please try another card.
EXPIRED_CARD | The expiration date is expired or missing. Please correct and try again.
INCORRECT_PIN | The PIN is invalid or missing. Please try again with the correct PIN.
TRANSACTION_NOT_PERMITTED | Transaction not permitted to cardholder. Please contact card issuer for more information.
SUSPECTED_FRAUD | Please contact card issuer for more information.
EXCEEDS_APPROVAL_AMOUNT_LIMIT | Transaction violates issuer amount limit. Please contact card issuer for more information or try with another card.
RESTRICTED_CARD | Card not supported in this region or country. Please contact card issuer for more information.
TRANSACTION_DOES_NOT_FULFILL_AML_REQUIREMENT | This transaction does not fulfill compliance requirements and cannot be processed.
EXCEEDS_WITHDRAWAL_FREQUENCY_LIMIT | Please attempt with another card or contact card issuer for more information.
ALLOWABLE_NUMBER_OF_PIN_ENTRY_TRIES_EXCEEDED | The maximum permitted number of PIN entry attempts has been exceeded. Please use another payment method.
CRYPTOGRAPHIC_ERROR_FOUND_IN_PIN | The supplied PIN is invalid.
NEGATIVE_RESULTS | Invalid security code.
CANNOT_VERIFY_PIN | The PIN is invalid or missing. Please try again with the correct PIN.
ISSUER_INOPERATIVE | Please attempt transaction again and contact card issuer if it still cannot be processed.
FINANCIAL_INSTITUTION_NOT_FOUND | The issuer can not be found. Please check card number to ensure it is valid.
TRANSACTION_NOT_COMPLETED_LAW_VIOLATION | The transaction cannot be completed because it violates a law.
SURCHARGE_AMOUNT_NOT_SUPPORTED | The supplied surcharge amount is not supported by the issuer.
TRANSACTION_AMOUNT_EXCEEDS_PREAUTHORIZED_APPROVAL_AMOUNT | Transaction violates amount limit.
CARD_AUTHENTICATION_FAILED | Please contact card issuer for more information.
STOP_PAYMENT_ORDER | Please contact card issuer for more information.
