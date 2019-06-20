curl https://finix.sandbox-payments-api.com/merchants/MUu56ZGx3Xb6U9gAqKfgNisd/devices \
        -H "Content-Type: application/vnd.json+api" \
        -u  USjHFGYvecE4LBitYG8KDE2g:b698f403-d9b7-4157-82d8-162cea8c8cc3 \
        -d '
      {
        "name": "Finix  triPOS #1",
        "model": "MX915",
        "description": "Mike Jones",
        "configuration": {
          "allow_debit": true,
          "prompt_signature": "NEVER"
        }
      }'
