curl https://finix.sandbox-payments-api.com/settlements/STxxxxxxxxx/funding_transfers \
 -H "Content-Type: application/vnd.json+api" \
 -u US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834 \
 -X POST \
 -d '
   {
   "destination": "PIxxxxx",
   "currency": "USD",
   "amount": 200
   }'
