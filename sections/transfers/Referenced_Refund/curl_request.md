curl https://finix.sandbox-payments-api.com/transfers/TRkWoMAdBwfVgYQpL8csYbtH/reversals \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHFGYvecE4LBitYG8KDE2g:b698f403-d9b7-4157-82d8-162cea8c8cc3 \
    -d  '
        {
          "refund_amount" : 150,
          "device": "DVkBqa68V1ZQusodU8o6mB62"
        }'
