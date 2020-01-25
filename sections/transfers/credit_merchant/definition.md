## Credit Merchant

As a Payment Facilitator, there are many instances where you may want to create a Debit or Credit adjustment on your merchants.

Examples:

1. You may want to charge your merchants a fee for a special scenario (chargebacks, minimum transaction limit not met, etc.)
You may want to try and collect money from your merchants if you suspect their activity is fraudulent.
A merchant may accidentally type in a wrong bank account number and their funding instructions were sent to another account.
You may want to Credit a merchant for a technical issue they may have experienced.

In the scenarios above, there are two APIs at your disposal to Debit and Credit your sub-merchants via ACH. Each API call will debit or credit a merchant through our settlements infrastructure. The money will either be credited or debited from the FBO account.  At the moment, there isn't an API to Credit or Debit your PayFac Operating Account. It is in our roadmap.



This API call will create a Transfer that will Credit a merchant for the amount specified in cents. The Transfer will be added to the merchant's next settlement. The settlement must be approved with the Transfer created by this API call in order to successfully Credit the merchant.
