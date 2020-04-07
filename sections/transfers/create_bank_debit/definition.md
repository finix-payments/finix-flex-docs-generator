## Debit a Bank Account (ie eCheck)

Returns: Note eCheck transactions can be rejected for up to sixty days for a variety of reasons including insufficient funds, closed accounts, or a revoked authorization (i.e. dispute). Because of the 60 day threshold, {{api_name}} can configure a delay in the settling of an eCheck. For example, your application can implement a six day delay in order to feel more confident that the eCheck will not be rejected.

<aside class="notice">
By default, {{api_name}} implements a {{ACH_business_day_delay}} day business day delay on eCheck.
</aside>

<aside class="warning">
 Ensure that you create an additional buyer `Identity` separate from the Merchant `Identity`. Associate the buyer `Identity` with the bank account you tokenize.  
</aside>



 When a return occurs a Transfer of type `REVERSAL` with a subtype `SYSTEM` is automatically created and will negatively impact the future settlement.
