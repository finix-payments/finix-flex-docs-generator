curl https://finix.sandbox-payments-api.com/identities/IDsbTBawhnLBAVeinRb84vFR/merchants \
        -H "Content-Type: application/vnd.json+api" \
        -u  USjHFGYvecE4LBitYG8KDE2g:b698f403-d9b7-4157-82d8-162cea8c8cc3 \
        -d '
        {
            "processor": "VANTIV_V1",
            "gateway": "TRIPOS_CLOUD_V1"
        }'
