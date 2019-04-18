### Step 3: Verify Address Verification System (AVS)  and CVV

Now that we've associated a payment instrument to a sender, we have the ability to verify whether or not the card has passed AVS and CVV checks. How? By making a request to the `Verifications` endpoint. The returned `Verification` resource returns a set of general attributes and details about the card in question (e.g. card type, issuer information). Below you'll see a number of fields and the potential responses.
