curl https://finix.sandbox-payments-api.com/transfers \
    -H "Content-Type: application/vnd.json+api" \
    -u  USjHFGYvecE4LBitYG8KDE2g:b698f403-d9b7-4157-82d8-162cea8c8cc3 \
    -d  '
    {
      "device": "DVf2H8sh4LZZC52GTUrwCPPf",
      "tags": {
        "order_number": "chris123transfer"
      },
      "currency": "USD",
      "amount": 150,
      "operation_key": "CARD_PRESENT_UNREFERENCED_REFUND"
    }'
