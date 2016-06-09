import base64

partner_configs = [
    {
        'api_name': "Finix",
        'api_name_downcase': "finix",
        'base_url': 'https://api-staging.finix.io',
        'admin_basic_auth_username': 'US7AQLoX6FtZcPDttFAafEz2',
        'admin_basic_auth_password': 'f3276399-20f4-4bc3-aff0-71131cb347b8',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'application': None,
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/"
    },
    # {
    #     'api_name': "Payline",
    #     'api_name_downcase': "payline",
    #     'base_url': 'https://api-test.payline.io',
    #     'admin_basic_auth_username': 'USkoFNY73WEiP8tYmZtPa6e4',
    #     'admin_basic_auth_password': 'e28fe471-5b2c-4f20-9db9-0a3e5fd06110',
    #     'admin_encoded_auth': base64.b64encode('USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110'),
    #     'basic_auth_username': None,
    #     'basic_auth_password': None,
    #     'encoded_auth': None,
    #     'payment_processor': "DUMMY_V1",
    #     'identity_verification_processor': "DUMMY_V1",
    #     'application': None,
    #     'jsfiddle': "http://jsfiddle.net/rserna2010/sab76Lne/"
    # },
    # {
    #     'api_name': "Payscout",
    #     'api_name_downcase': "payscout",
    #     'base_url': 'https://payscout-staging.finix.io',
    #     'admin_basic_auth_username': 'USkoFNY73WEiP8tYmZtPa6e4',
    #     'admin_basic_auth_password': 'e28fe471-5b2c-4f20-9db9-0a3e5fd06110',
    #     'admin_encoded_auth': base64.b64encode('USrcWo52PSPyvRMx8N9kjYDQ:48502c0d-dfed-450f-b1d9-fb0f30abd498'),
    #     'basic_auth_username': None,
    #     'basic_auth_password': None,
    #     'encoded_auth': None,
    #     'payment_processor': "LITLE_V1",
    #     'identity_verification_processor': "DUMMY_V1",
    #     'application': None,
    #     'jsfiddle': "http://jsfiddle.net/rserna2010/9hbny54d/"
    # }
]


# this provides the ordering for the docs by section and individual snippet
snippets_by_resource = {
    "guides": [
        "definition",
        "getting_started",
        "create_merchant_identity",
        "create_bank_account",
        # "perform_identity_verification",
        "provision_merchant",
        "create_buyer_identity",
        "create_card",
        "create_card_debit",
        "refund_debit",
        "settle_funds",
        ],
    "tokenization": [
        "definition",
        ],
    "authorizations": [
        "definition",
        "create_authorization",
        "capture_authorization",
        "fetch_authorization",
        # "list_authorizations"
    ],

    "disputes": [
        "definition",
        # "create_dispute",
        "fetch_dispute",
        # "list_disputes"
    ],

    "identities": [
        "definition",
        "create_buyer_identity",
        "create_merchant_identity",
        "fetch_identity",
        # # "list_identities",
        # # "list_merchants",
        "provision_merchant"
    ],

    # "identity_verifications": [
    #     "definition",
    #     "create_identity_verification",
    #     "fetch_identity_verification",
    #     # "list_identity_verifications"
    # ],

    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
        # "list_settlements"
    ],

    "transfers": [
        "definition",
        "create_debit",
        "create_refund",
        "fetch_transfer",
        # "list_transfers"
    ],

    "webhooks": [
        "definition",
        "create_webhook",
        "fetch_webhook",
        # "list_webhooks"
    ],

    "payment_instruments": [
        "definition",
        "create_card",
        "create_bank_account",
        # "fetch_payment_instrument",
        # "list_payment_instruments"
    ],
    }

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "guides",
    "tokenization",
    "authorizations",
    "disputes",
    "identities",
    # "identity_verifications",
    "settlements",
    "transfers",
    "webhooks",
    "payment_instruments"
]

# Determine which client libraries to include
included_clients = [
    "curl",
    "php",
    "java"
]