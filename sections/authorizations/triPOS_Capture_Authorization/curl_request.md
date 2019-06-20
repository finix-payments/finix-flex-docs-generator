curl https://finix.sandbox-payments-api.com/authorizations/AUuCfRve8QG6G1wnPCReiLma \
   -H "Content-Type: application/vnd.json+api" \
   -u  USjHFGYvecE4LBitYG8KDE2g:b698f403-d9b7-4157-82d8-162cea8c8cc3 \
   -X PUT \
   -d '
     {
         "capture_amount": 150
     }'
